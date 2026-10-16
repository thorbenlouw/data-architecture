#!/usr/bin/env python3
"""dpc - tooling for the data platform capabilities OKF bundle.

The bundle (``bundle/``) is the source of truth: one Markdown file per concept,
with YAML frontmatter. Relationships are authored in frontmatter, on one side
only. This tool derives everything else:

  validate   check frontmatter, ids, relationships, links and generated sections
  build      regenerate the generated part of every concept and all index.md files
  export     write graph JSON, CSVs, SKOS Turtle, a mind map and an HTML explorer to dist/
  show       print one concept, its relationships and what links to it (--json for agents)
  search     find concepts by words in ids, titles, aliases, product families and text
  usecase    list the capabilities a use case needs and what realises them
  coverage   show which capabilities a platform covers
  new        create a new concept file from a template
  stats      count concepts by type

Only dependency: PyYAML. Run ``python tools/dpc.py --help``.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import posixpath
import re
import signal
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

if hasattr(signal, "SIGPIPE"):
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

REPO = Path(__file__).resolve().parent.parent
DEFAULT_BUNDLE = REPO / "bundle"
DEFAULT_DIST = REPO / "dist"

OKF_VERSION = "0.2"
GEN_MARKER = "<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->"
GEN_LINE_RE = re.compile(r"^<!-- dpc:generated:[^\n]*-->[ \t]*$\n?", re.M)
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
STATUSES = {"draft", "stable", "deprecated"}
LEVEL_NAMES = {1: "Initial", 2: "Managed", 3: "Defined", 4: "Measured", 5: "Optimising"}
AVAILABILITY = {"ga", "preview", "unconfirmed", "deprecated", "retired"}
INACTIVE = {"deprecated", "retired"}
SPELLING = [  # applied to text and queries so UK and US spellings match
    (r"isation", "ization"), (r"ise\b", "ize"), (r"ised\b", "ized"), (r"ises\b", "izes"), (r"ising\b", "izing"),
    (r"yse\b", "yze"), (r"ysed\b", "yzed"), (r"modelling", "modeling"), (r"modelled", "modeled"),
    (r"labelling", "labeling"), (r"labelled", "labeled"), (r"catalogue", "catalog"), (r"centre", "center"),
    (r"behaviour", "behavior"), (r"licence", "license"), (r"colour", "color"), (r"artefact", "artifact"),
]

# type -> folder and relationship fields (field -> target types, '|' separated).
# A trailing '*' marks a list of mappings whose `capability` key holds the target id.
TYPES: dict[str, dict] = {
    "Capability": {"folder": "capabilities", "rels": {"broader": "Capability", "related": "Capability", "depends_on": "Capability"}},
    "Technology": {"folder": "technologies", "rels": {"realises": "Capability", "platform": "Platform", "distribution_of": "Platform|Technology"}},
    "Pattern": {"folder": "patterns", "rels": {"uses": "Capability", "related": "Pattern"}},
    "Persona": {"folder": "personas", "rels": {"cares_about": "Capability", "patterns": "Pattern"}},
    "Use Case": {"folder": "use-cases", "rels": {"requires": "Capability*", "benefits_from": "Capability*", "personas": "Persona", "patterns": "Pattern"}},
    "Maturity Track": {"folder": "maturity", "rels": {"covers": "Capability", "related_tracks": "Maturity Track"}},
    "Platform": {"folder": "platforms", "rels": {}},
    "Framework": {"folder": "frameworks", "rels": {"related": "Framework", "applies_to": "Use Case|Persona|Pattern"}},
    "Reference": {"folder": "about", "rels": {}},
}
TYPE_ORDER = list(TYPES)
TYPE_PLURAL = {"Capability": "capabilities", "Technology": "technologies", "Pattern": "patterns", "Persona": "personas",
               "Use Case": "use cases", "Maturity Track": "maturity tracks", "Platform": "platform groups",
               "Framework": "frameworks", "Reference": "reference pages"}
FOLDER_TITLES = {
    "capabilities": "Capabilities", "technologies": "Technologies", "patterns": "Patterns", "personas": "Personas",
    "use-cases": "Use cases", "maturity": "Maturity tracks", "platforms": "Platforms",
    "frameworks": "Frameworks, standards and regulations", "about": "About this bundle",
}


def norm(text: str) -> str:
    t = text.lower()
    for a, b in SPELLING:
        t = re.sub(a, b, t)
    return t


def type_from_arg(s: str) -> str | None:
    k = re.sub(r"[\s_-]+", "", s.lower())
    for t in TYPES:
        if re.sub(r"\s+", "", t.lower()) == k or re.sub(r"\s+", "", t.lower()) + "s" == k:
            return t
    return {"usecases": "Use Case", "track": "Maturity Track", "tracks": "Maturity Track", "tech": "Technology"}.get(k)


# --------------------------------------------------------------------------- YAML

class FMDumper(yaml.SafeDumper):
    """Readable frontmatter: short scalar lists and small mappings in flow style."""


def _is_scalar(x) -> bool:
    return x is None or isinstance(x, (str, int, float, bool))


def _repr_list(dumper, data):
    flow = all(_is_scalar(x) for x in data) and sum(len(str(x)) + 2 for x in data) <= 100
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=flow)


def _repr_dict(dumper, data):
    flow = (
        0 < len(data) <= 4
        and "type" not in data
        and all(_is_scalar(v) for v in data.values())
        and sum(len(str(k)) + len(str(v)) + 4 for k, v in data.items()) <= 160
    )
    return dumper.represent_mapping("tag:yaml.org,2002:map", data.items(), flow_style=flow)


FMDumper.add_representer(list, _repr_list)
FMDumper.add_representer(dict, _repr_dict)


def dump_frontmatter(fm: dict) -> str:
    return yaml.dump(fm, Dumper=FMDumper, sort_keys=False, allow_unicode=True, width=4096)


# --------------------------------------------------------------------------- model

class Concept:
    def __init__(self, path: Path, rel: str, fm: dict, authored: str, generated: str):
        self.path = path            # absolute file path
        self.rel = rel              # posix path relative to bundle root
        self.fm = fm
        self.authored = authored    # body text above the generated marker
        self.generated = generated  # body text below the marker (as found on disk)

    @property
    def id(self) -> str:
        return self.fm.get("id") or Path(self.rel).stem

    @property
    def type(self) -> str:
        return self.fm.get("type", "")

    @property
    def title(self) -> str:
        return self.fm.get("title") or self.id

    @property
    def description(self) -> str:
        return self.fm.get("description", "")

    @property
    def names(self) -> list[str]:
        return [self.title] + [str(a) for a in (self.fm.get("aliases") or []) + (self.fm.get("formerly") or [])]

    def ids(self, field: str) -> list[str]:
        """Target ids of a relationship field, whatever its shape."""
        val = self.fm.get(field)
        if val is None:
            return []
        if isinstance(val, str):
            return [val]
        out = []
        for item in val:
            if isinstance(item, dict):
                if item.get("capability"):
                    out.append(item["capability"])
            elif isinstance(item, str):
                out.append(item)
        return out


def split_doc(text: str) -> tuple[dict | None, str, str, str | None]:
    """Return (frontmatter, authored body, generated body, error)."""
    if not text.startswith("---\n"):
        return None, text, "", "missing YAML frontmatter"
    end = text.find("\n---\n", 4)
    if end == -1:
        if text.rstrip().endswith("\n---"):
            end = len(text.rstrip()) - 4
        else:
            return None, text, "", "unterminated frontmatter"
    raw = text[4:end]
    body = text[end + 5:]
    try:
        fm = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        return None, body, "", f"frontmatter is not valid YAML: {exc}"
    if not isinstance(fm, dict):
        return None, body, "", "frontmatter is not a mapping"
    m = GEN_LINE_RE.search(body)
    if not m:
        return fm, body, "", None
    return fm, body[:m.start()], body[m.end():].lstrip("\n"), None


class Bundle:
    def __init__(self, root: Path):
        self.root = root
        self.concepts: dict[str, Concept] = {}
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self._load()
        self._index()

    # ------------------------------------------------------------ loading
    def _load(self):
        if not self.root.is_dir():
            sys.exit(f"Bundle folder not found: {self.root}")
        for path in sorted(self.root.rglob("*.md")):
            rel = path.relative_to(self.root).as_posix()
            if path.name in ("index.md", "log.md"):
                continue
            fm, authored, gen, err = split_doc(path.read_text(encoding="utf-8"))
            if err:
                self.errors.append(f"{rel}: {err}")
                continue
            c = Concept(path, rel, fm, authored, gen)
            if c.id in self.concepts:
                self.errors.append(f"{rel}: duplicate id '{c.id}' (also {self.concepts[c.id].rel})")
                continue
            self.concepts[c.id] = c

    def of_type(self, t: str) -> list[Concept]:
        return [c for c in self.concepts.values() if c.type == t]

    # ------------------------------------------------------------ derived indexes
    def _index(self):
        C = self.concepts
        self.children = defaultdict(list)          # cap -> children (any parent)
        self.primary_children = defaultdict(list)  # cap -> children via first broader
        caps = [c for c in C.values() if c.type == "Capability"]
        self.cap_order = {c.id: i for i, c in enumerate(sorted(caps, key=lambda c: (c.fm.get("order", 9999), c.title.lower())))}
        for c in caps:
            for i, p in enumerate(c.ids("broader")):
                if p in C:
                    self.children[p].append(c.id)
                    if i == 0:
                        self.primary_children[p].append(c.id)
        for k in self.children:
            self.children[k].sort(key=self._cap_sort)
            self.primary_children[k].sort(key=self._cap_sort)
        self.domains = sorted([c.id for c in caps if not c.ids("broader")], key=self._cap_sort)
        self._desc_cache: dict[str, list[str]] = {}

        self.realised_by = defaultdict(list)       # cap -> tech ids (all, including inactive)
        self.techs_by_platform = defaultdict(list)
        for t in self.of_type("Technology"):
            for cap in t.ids("realises"):
                self.realised_by[cap].append(t.id)
            self.techs_by_platform[t.fm.get("platform", "")].append(t.id)
        for k in self.realised_by:
            self.realised_by[k].sort(key=lambda i: C[i].title.lower())

        self.inbound = defaultdict(lambda: defaultdict(list))  # target -> (type, field) -> sources
        for c in C.values():
            for field in TYPES.get(c.type, {}).get("rels", {}):
                for target in c.ids(field):
                    self.inbound[target][(c.type, field)].append(c.id)
            if c.type == "Maturity Track":
                for lvl in c.fm.get("levels") or []:
                    for cap in lvl.get("capabilities") or []:
                        self.inbound[cap][("Maturity Track", f"level-{lvl.get('level')}")].append(c.id)
                    for fw in (lvl.get("external_levels") or {}):
                        self.inbound[fw][("Maturity Track", "external_levels")].append(c.id)
            if c.type == "Framework":
                for m in c.fm.get("mappings") or []:
                    for cap in m.get("capabilities") or []:
                        self.inbound[cap][("Framework", "mappings")].append(c.id)
            if c.type == "Platform":
                for cap in (c.fm.get("terminology") or {}):
                    self.inbound[cap][("Platform", "terminology")].append(c.id)
        self.families = []  # (platform id, family dict)
        for p in self.of_type("Platform"):
            for f in p.fm.get("families") or []:
                self.families.append((p.id, f))

    def _cap_sort(self, cid: str):
        c = self.concepts.get(cid)
        return (self.cap_order.get(cid, 9999), c.title.lower() if c else cid)

    def domain_of(self, cid: str) -> str | None:
        seen = set()
        cur = cid
        while cur in self.concepts and cur not in seen:
            seen.add(cur)
            parents = self.concepts[cur].ids("broader")
            if not parents:
                return cur
            cur = parents[0]
        return None

    def descendants(self, cid: str) -> list[str]:
        if cid in self._desc_cache:
            return self._desc_cache[cid]
        out, stack, seen = [], [cid], {cid}
        while stack:
            for ch in self.children.get(stack.pop(), []):
                if ch not in seen:
                    seen.add(ch)
                    out.append(ch)
                    stack.append(ch)
        self._desc_cache[cid] = out
        return out

    def ancestors(self, cid: str) -> list[str]:
        out, stack, seen = [], [cid], {cid}
        while stack:
            cur = self.concepts.get(stack.pop())
            if not cur:
                continue
            for p in cur.ids("broader"):
                if p not in seen:
                    seen.add(p)
                    out.append(p)
                    stack.append(p)
        return out

    def depth(self, cid: str) -> int:
        d, cur, seen = 0, cid, set()
        while cur in self.concepts and cur not in seen:
            seen.add(cur)
            ps = self.concepts[cur].ids("broader")
            if not ps:
                break
            cur, d = ps[0], d + 1
        return d

    def domain_caps(self, dom: str) -> list[str]:
        return [x for x in [dom] + self.descendants(dom) if self.domain_of(x) == dom]

    def platforms(self) -> list[Concept]:
        return sorted(self.of_type("Platform"), key=lambda p: (p.fm.get("order", 999), p.title.lower()))

    def plat_short(self, pid: str) -> str:
        p = self.concepts.get(pid)
        return (p.fm.get("short") or p.title) if p else pid

    # ------------------------------------------------------------ technology state
    def availability(self, tid: str) -> str:
        return str(self.concepts[tid].fm.get("availability", "ga"))

    def is_counted(self, tid: str, allow_preview: bool = True) -> bool:
        """Does this technology count towards its platform's coverage?"""
        t = self.concepts[tid]
        a = self.availability(tid)
        if a in INACTIVE or t.fm.get("distribution_of"):
            return False
        return allow_preview or a != "preview"

    def platform_caps(self, pid: str, allow_preview: bool = True, counted_only: bool = True) -> dict[str, list[str]]:
        """capability id -> technologies on this platform that realise it directly."""
        out = defaultdict(list)
        for tid in self.techs_by_platform.get(pid, []):
            if counted_only and not self.is_counted(tid, allow_preview):
                continue
            for cap in self.concepts[tid].ids("realises"):
                out[cap].append(tid)
        return out

    def covered(self, cap: str, platform_caps: dict) -> bool:
        """A capability counts as covered if it or any narrower capability is realised."""
        return cap in platform_caps or any(d in platform_caps for d in self.descendants(cap))

    def fit(self, pid: str, caps: list[str]) -> tuple[list[str], list[str], list[str]]:
        """(covered by GA or unconfirmed, covered only in preview, not covered)."""
        ga = self.platform_caps(pid, allow_preview=False)
        anyc = self.platform_caps(pid, allow_preview=True)
        cov = [x for x in caps if self.covered(x, ga)]
        prev = [x for x in caps if x not in cov and self.covered(x, anyc)]
        miss = [x for x in caps if x not in cov and x not in prev]
        return cov, prev, miss

    def suffix(self, tid: str) -> str:
        t = self.concepts[tid]
        a = self.availability(tid)
        bits = []
        if a != "ga":
            bits.append(a)
        if t.fm.get("distribution_of"):
            d = self.concepts.get(t.fm["distribution_of"])
            bits.append(f"distribution of {d.title if d else t.fm['distribution_of']}")
        return f" ({'; '.join(bits)})" if bits else ""

    def link(self, src: Concept, target_id: str, label: str | None = None) -> str:
        t = self.concepts.get(target_id)
        if not t:
            return label or target_id
        relp = posixpath.relpath(t.rel, posixpath.dirname(src.rel) or ".")
        return f"[{label or t.title}]({relp})"

    def tlink(self, src: Concept, tid: str, with_platform: bool = False) -> str:
        t = self.concepts[tid]
        label = t.title
        if with_platform:
            label = f"{label} ({self.plat_short(t.fm.get('platform', ''))})"
        return self.link(src, tid, label) + self.suffix(tid)

    def equivalents(self, tid: str, per_platform: int = 3) -> dict[str, list[tuple[str, list[str]]]]:
        """Closest technologies on other platforms, by overlap of realised capabilities."""
        C = self.concepts
        t = C[tid]
        mine = t.ids("realises")
        if not mine:
            return {}
        primary, mset = mine[0], set(mine)
        scored = defaultdict(list)
        for other in self.of_type("Technology"):
            op = other.fm.get("platform")
            if op == t.fm.get("platform") or not self.is_counted(other.id):
                continue
            oset = set(other.ids("realises"))
            shared = mset & oset
            if not shared:
                continue
            j = len(shared) / len(mset | oset)
            if primary not in oset and j < 0.4:
                continue
            score = j + (0.5 if primary in oset else 0) + (0.2 if other.ids("realises")[:1] == [primary] else 0)
            scored[op].append((score, other.id, sorted(shared, key=self._cap_sort)))
        out = {}
        for p, items in scored.items():
            items.sort(key=lambda x: (-x[0], C[x[1]].title.lower()))
            out[p] = [(i, s) for _, i, s in items[:per_platform]]
        return out


# --------------------------------------------------------------------------- validation

def validate(b: Bundle, check_generated: bool = False, quiet_coverage: bool = False) -> int:
    E, W = list(b.errors), list(b.warnings)
    C = b.concepts
    alias_owner: dict[str, str] = {}
    titles: dict[str, list[str]] = defaultdict(list)
    cap_titles = {c.title.lower() for c in b.of_type("Capability")}
    referenced = set()
    for c in C.values():
        where = c.rel
        if c.type not in TYPES:
            E.append(f"{where}: unknown type '{c.type}' (expected one of: {', '.join(TYPES)})")
            continue
        if not ID_RE.match(c.id):
            E.append(f"{where}: id '{c.id}' must be lower-case kebab-case")
        if Path(c.rel).stem != c.id:
            E.append(f"{where}: file name must equal id '{c.id}'")
        folder = TYPES[c.type]["folder"]
        if c.type != "Reference" and c.rel.split("/")[0] != folder:
            E.append(f"{where}: {c.type} concepts belong under {folder}/")
        for key in ("title", "description"):
            if not c.fm.get(key):
                E.append(f"{where}: missing '{key}'")
        d = c.description or ""
        if "\n" in d.strip():
            E.append(f"{where}: description must be one line")
        if d and not d.rstrip().endswith((".", "?", ")")):
            W.append(f"{where}: description should be a full sentence ending with a full stop")
        if len(d) > 240:
            W.append(f"{where}: description is {len(d)} characters; aim for under 200")
        st = c.fm.get("status", "stable")
        if st not in STATUSES:
            E.append(f"{where}: status '{st}' must be one of {sorted(STATUSES)}")
        for key in ("aliases", "formerly", "tags"):
            v = c.fm.get(key)
            if v is not None and (not isinstance(v, list) or not all(isinstance(x, (str, int, float)) for x in v)):
                E.append(f"{where}: '{key}' must be a list of strings")
        for field, target in TYPES[c.type]["rels"].items():
            wants = target.rstrip("*").split("|")
            val = c.fm.get(field)
            if val is None:
                continue
            if target.endswith("*"):
                if not isinstance(val, list) or not all(isinstance(x, dict) and x.get("capability") for x in val):
                    E.append(f"{where}: '{field}' must be a list of mappings with a 'capability' key")
                    continue
                for x in val:
                    if None in x or any(v is None for v in x.values()) or set(x) - {"capability", "level", "why"}:
                        E.append(f"{where}: '{field}' entry for {x.get('capability')} has empty or unknown keys (quote text containing commas)")
                    lvl = x.get("level")
                    if lvl is not None and lvl not in LEVEL_NAMES:
                        E.append(f"{where}: '{field}' level for {x['capability']} must be 1-5")
            for tid in c.ids(field):
                tc = C.get(tid)
                if not tc:
                    E.append(f"{where}: '{field}' points to unknown id '{tid}'")
                elif tc.type not in wants:
                    E.append(f"{where}: '{field}' must point to a {' or '.join(wants)}, but '{tid}' is a {tc.type}")
                elif tc.type == "Capability" and not tc.ids("broader") and c.type in ("Use Case", "Persona", "Pattern", "Technology"):
                    W.append(f"{where}: '{field}' points to the whole domain '{tid}'; name specific capabilities")
                if c.type != "Capability" and tc and tc.type == "Capability":
                    referenced.add(tid)
            ids = c.ids(field)
            if len(ids) != len(set(ids)):
                W.append(f"{where}: '{field}' lists the same id twice")
        # type-specific checks
        if c.type == "Capability":
            parents = c.ids("broader")
            if c.id in parents:
                E.append(f"{where}: a capability cannot be its own parent")
            if c.id in b.ancestors(c.id):
                E.append(f"{where}: 'broader' creates a cycle")
            dom = b.domain_of(c.id)
            if dom and c.rel.split("/")[1:2] != [dom]:
                W.append(f"{where}: lives outside its domain folder capabilities/{dom}/")
            overlap = set(c.ids("related")) & (set(parents) | set(b.children.get(c.id, [])))
            if overlap:
                W.append(f"{where}: 'related' repeats a parent or child: {', '.join(sorted(overlap))}")
            for a in c.names:
                k = norm(a)
                if k in alias_owner and alias_owner[k] != c.id:
                    W.append(f"{where}: name or alias '{a}' is also used by capability {alias_owner[k]}")
                alias_owner.setdefault(k, c.id)
        if c.type == "Technology":
            if not c.fm.get("platform"):
                E.append(f"{where}: technology needs a 'platform'")
            if not c.ids("realises"):
                W.append(f"{where}: technology realises no capability")
            a = c.fm.get("availability", "ga")
            if a not in AVAILABILITY:
                E.append(f"{where}: availability '{a}' must be one of {sorted(AVAILABILITY)}")
            plat = C.get(c.fm.get("platform", ""))
            if plat and c.rel.split("/")[1:2] != [plat.fm.get("folder", plat.id.replace("platform-", ""))]:
                W.append(f"{where}: lives outside its platform folder")
            titles[c.title.lower()].append(c.id)
            if c.title.lower() in cap_titles:
                W.append(f"{where}: technology title '{c.title}' is the same as a capability title; add the product or vendor name")
        if c.type == "Maturity Track":
            levels = c.fm.get("levels") or []
            got = [lv.get("level") for lv in levels]
            if got != [1, 2, 3, 4, 5]:
                E.append(f"{where}: levels must be 1 to 5 in order (found {got})")
            for lv in levels:
                if None in lv or set(lv) - {"level", "name", "summary", "criteria", "capabilities", "external_levels"}:
                    E.append(f"{where}: level {lv.get('level')} has empty or unknown keys")
                for cap in lv.get("capabilities") or []:
                    if cap not in C or C[cap].type != "Capability":
                        E.append(f"{where}: level {lv.get('level')} lists unknown capability '{cap}'")
                    referenced.add(cap)
                for fw in (lv.get("external_levels") or {}):
                    if fw not in C or C[fw].type != "Framework":
                        E.append(f"{where}: level {lv.get('level')} external_levels key '{fw}' is not a framework")
                if not lv.get("criteria"):
                    E.append(f"{where}: level {lv.get('level')} has no criteria")
        if c.type == "Framework":
            for lv in c.fm.get("maturity_levels") or []:
                if None in lv or any(v is None for v in lv.values()):
                    E.append(f"{where}: maturity level {lv.get('level')} has empty keys (quote text containing commas)")
            for m in c.fm.get("mappings") or []:
                if None in m or any(v is None for v in m.values()):
                    E.append(f"{where}: mapping '{m.get('ref')}' has empty keys")
                for cap in m.get("capabilities") or []:
                    if cap not in C or C[cap].type != "Capability":
                        E.append(f"{where}: mapping '{m.get('ref')}' lists unknown capability '{cap}'")
                    else:
                        referenced.add(cap)
                        if not C[cap].ids("broader"):
                            W.append(f"{where}: mapping '{m.get('ref')}' points to the whole domain '{cap}'; name specific capabilities")
        if c.type == "Platform":
            for cap in (c.fm.get("terminology") or {}):
                if cap not in C or C[cap].type != "Capability":
                    E.append(f"{where}: terminology key '{cap}' is not a capability")
            for f in c.fm.get("families") or []:
                if not f.get("name"):
                    E.append(f"{where}: product family without a name")
                for tid in f.get("technologies") or []:
                    if tid not in C or C[tid].type != "Technology":
                        E.append(f"{where}: family '{f.get('name')}' lists unknown technology '{tid}'")
        # links in the authored body
        for _, target in LINK_RE.findall(c.authored):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = target.split("#")[0]
            if not path:
                continue
            full = (b.root / path.lstrip("/")) if path.startswith("/") else (c.path.parent / path)
            if not full.resolve().exists():
                W.append(f"{where}: broken link to {target}")
    for t, ids in titles.items():
        if len(ids) > 1:
            W.append(f"technologies: title '{C[ids[0]].title}' is used by {', '.join(ids)}")
    for cap in b.of_type("Capability"):
        if not cap.ids("broader"):
            continue
        if not quiet_coverage and not b.realised_by.get(cap.id) and not b.descendants(cap.id):
            W.append(f"{cap.rel}: no technology realises this capability yet")
        if cap.id not in referenced and not any(d in referenced for d in b.descendants(cap.id)):
            W.append(f"{cap.rel}: no use case, persona, pattern, maturity track or framework refers to this capability")
    if check_generated and not E:
        changed = build(b, write=False)
        for rel in changed:
            E.append(f"{rel}: generated content is out of date; run `python tools/dpc.py build`")
    for w in W:
        print(f"warning: {w}")
    for e in E:
        print(f"error: {e}")
    counts = defaultdict(int)
    for c in C.values():
        counts[c.type] += 1
    summary = ", ".join(f"{counts[t]} {TYPE_PLURAL[t]}" for t in TYPE_ORDER if counts[t])
    print(f"\n{len(C)} concepts ({summary}). {len(E)} errors, {len(W)} warnings.")
    return 1 if E else 0


# --------------------------------------------------------------------------- generated sections

def md_list(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def esc_cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def fit_cell(cov, prev, total) -> str:
    return f"{len(cov)} of {total}" + (f" (+{len(prev)} in preview)" if prev else "")


def appears_in(b: Bundle, c: Concept) -> list[str]:
    """Reverse links from use cases, patterns, personas, tracks and frameworks to a capability."""
    C, L = b.concepts, b.link
    appears = []
    ucs = []
    for u in sorted(b.of_type("Use Case"), key=lambda x: x.title.lower()):
        for x in u.fm.get("requires") or []:
            if x.get("capability") == c.id:
                lvl = x.get("level")
                ucs.append(f"{L(c, u.id)} (requires{f', level {lvl}' if lvl else ''})")
        for x in u.fm.get("benefits_from") or []:
            if x.get("capability") == c.id:
                ucs.append(f"{L(c, u.id)} (benefits from)")
    if ucs:
        appears.append("**Use cases:** " + " · ".join(ucs))
    pats = b.inbound[c.id].get(("Pattern", "uses"), [])
    if pats:
        appears.append("**Patterns:** " + " · ".join(L(c, p) for p in sorted(pats)))
    pers = b.inbound[c.id].get(("Persona", "cares_about"), [])
    if pers:
        appears.append("**Personas:** " + " · ".join(L(c, p) for p in sorted(pers, key=lambda i: C[i].title)))
    tracks = []
    named = set()
    for (t, field), srcs in b.inbound[c.id].items():
        if t == "Maturity Track" and field.startswith("level-"):
            lvl = int(field.split("-")[1])
            for s in srcs:
                named.add(s)
                tracks.append((C[s].title, f"{L(c, s)} (from level {lvl}, {LEVEL_NAMES.get(lvl, '')})"))
    for s in set(b.inbound[c.id].get(("Maturity Track", "covers"), [])) - named:
        tracks.append((C[s].title, L(c, s)))
    if tracks:
        appears.append("**Maturity tracks:** " + " · ".join(x for _, x in sorted(tracks)))
    fws = []
    for f in sorted(b.of_type("Framework"), key=lambda x: x.title.lower()):
        refs = [str(m.get("ref")) for m in f.fm.get("mappings") or [] if c.id in (m.get("capabilities") or [])]
        if refs:
            fws.append(f"{L(c, f.id)}: {'; '.join(refs)}")
    if fws:
        appears.append("**Frameworks:** " + " · ".join(fws))
    return appears


def gen_capability(b: Bundle, c: Concept) -> str:
    C, L = b.concepts, b.link
    out = []
    rows = []
    dom = b.domain_of(c.id)
    if dom and dom != c.id:
        rows.append(("Domain", L(c, dom)))
    if c.ids("broader"):
        rows.append(("Broader", ", ".join(L(c, p) for p in c.ids("broader"))))
    if b.children.get(c.id):
        rows.append(("Narrower", ", ".join(L(c, ch) for ch in b.children[c.id])))
    rel = list(dict.fromkeys(c.ids("related") + b.inbound[c.id].get(("Capability", "related"), [])))
    if rel:
        rows.append(("Related", ", ".join(L(c, r) for r in sorted(rel, key=b._cap_sort))))
    if c.ids("depends_on"):
        rows.append(("Depends on", ", ".join(L(c, r) for r in c.ids("depends_on"))))
    needed = b.inbound[c.id].get(("Capability", "depends_on"), [])
    if needed:
        rows.append(("Needed by", ", ".join(L(c, r) for r in sorted(needed, key=b._cap_sort))))
    out.append("# Relationships\n")
    out.append("| Relationship | Capabilities |\n|---|---|")
    out += [f"| {k} | {v} |" for k, v in rows]

    appears = appears_in(b, c)
    if appears:
        out.append("\n# Where it appears\n")
        out.append("\n".join(f"- {a}" for a in appears))

    out.append("\n# How platforms provide it\n")
    techs = b.realised_by.get(c.id, [])
    rows = []
    for p in b.platforms():
        ts = [t for t in techs if C[t].fm.get("platform") == p.id]
        ts.sort(key=lambda t: (not b.is_counted(t), C[t].title.lower()))
        term = (p.fm.get("terminology") or {}).get(c.id)
        if ts or term:
            rows.append(f"| {L(c, p.id)} | {esc_cell(term or '')} | {', '.join(b.tlink(c, t) for t in ts)} |")
    if rows:
        out.append("| Platform | Name used | Technologies |\n|---|---|---|")
        out += rows
    else:
        out.append("No technology in this bundle realises this capability directly yet.")
    desc = b.descendants(c.id)
    if desc:
        n = len({t for d in desc for t in b.realised_by.get(d, [])})
        if n:
            out.append(f"\nNarrower capabilities are realised by a further {n} technologies; see their pages.")
    return "\n".join(out) + "\n"


def gen_technology(b: Bundle, c: Concept) -> str:
    C, L = b.concepts, b.link
    out = ["# Realises\n"]
    for i, cap in enumerate(c.ids("realises")):
        if cap in C:
            dom = b.domain_of(cap)
            extra = f" ({C[dom].title})" if dom and dom != cap else ""
            out.append(f"- {L(c, cap)}{extra}{' (primary)' if i == 0 else ''}: {C[cap].description}")
    pid = c.fm.get("platform")
    facts = []
    if pid in C:
        facts.append(f"**Platform:** {L(c, pid)}")
    a = c.fm.get("availability", "ga")
    facts.append(f"**Availability:** {a}")
    fams = [f.get("name") for p, f in b.families if p == pid and c.id in (f.get("technologies") or [])]
    if fams:
        facts.append(f"**Product family:** {', '.join(fams)}")
    if c.fm.get("distribution_of"):
        facts.append(f"**Distribution of:** {L(c, c.fm['distribution_of'])}. It is not counted in {C[pid].title if pid in C else 'its platform'}'s coverage.")
    if a in INACTIVE:
        facts.append("Not counted in platform coverage because it is " + a + ".")
    out.append("\n" + "  \n".join(facts))
    if not c.fm.get("distribution_of"):
        eq = b.equivalents(c.id)
        if eq:
            out.append("\n# Equivalents on other platforms\n")
            out.append("The closest technologies on each other platform, ranked by how many of the same capabilities they realise.\n")
            out.append("| Platform | Technologies | Shared capabilities |\n|---|---|---|")
            for p in b.platforms():
                if p.id in eq:
                    items = eq[p.id]
                    shared = list(dict.fromkeys(x for _, s in items for x in s))[:4]
                    out.append(f"| {L(c, p.id)} | {', '.join(b.tlink(c, t) for t, _ in items)} | {', '.join(L(c, x) for x in shared)} |")
    return "\n".join(out) + "\n"


def gen_pattern(b: Bundle, c: Concept) -> str:
    C, L = b.concepts, b.link
    out = ["# Capabilities it relies on\n"]
    out.append(md_list([f"{L(c, x)}: {C[x].description}" for x in c.ids("uses") if x in C]) or "None listed.")
    rel = list(dict.fromkeys(c.ids("related") + b.inbound[c.id].get(("Pattern", "related"), [])))
    if rel:
        out.append("\n# Related patterns\n")
        out.append(md_list([L(c, r) for r in rel]))
    ucs = b.inbound[c.id].get(("Use Case", "patterns"), [])
    pers = b.inbound[c.id].get(("Persona", "patterns"), [])
    if ucs or pers:
        out.append("\n# Where it appears\n")
        if ucs:
            out.append("- **Use cases:** " + " · ".join(L(c, u) for u in sorted(ucs)))
        if pers:
            out.append("- **Personas:** " + " · ".join(L(c, p) for p in sorted(pers)))
    return "\n".join(out) + "\n"


def gen_persona(b: Bundle, c: Concept) -> str:
    C, L = b.concepts, b.link
    out = ["# Capabilities they rely on most\n"]
    out.append("| Capability | Domain | What it does |\n|---|---|---|")
    for x in c.ids("cares_about"):
        if x in C:
            dom = b.domain_of(x)
            out.append(f"| {L(c, x)} | {L(c, dom) if dom and dom != x else ''} | {esc_cell(C[x].description)} |")
    if c.ids("patterns"):
        out.append("\n# Patterns\n")
        out.append(md_list([L(c, p) for p in c.ids("patterns")]))
    ucs = b.inbound[c.id].get(("Use Case", "personas"), [])
    if ucs:
        out.append("\n# Use cases they take part in\n")
        out.append(md_list([f"{L(c, u)}: {C[u].description}" for u in sorted(ucs, key=lambda i: C[i].title)]))
    fws = b.inbound[c.id].get(("Framework", "applies_to"), [])
    if fws:
        out.append("\n# Frameworks they work with\n")
        out.append(md_list([f"{L(c, f)}: {C[f].description}" for f in sorted(fws, key=lambda i: C[i].title)]))
    return "\n".join(out) + "\n"


def gen_use_case(b: Bundle, c: Concept) -> str:
    C, L = b.concepts, b.link
    out = ["# Required capabilities\n"]
    out.append("| Capability | Domain | Minimum level | Why |\n|---|---|---|---|")
    req = c.fm.get("requires") or []
    for x in req:
        cap = x.get("capability")
        if cap in C:
            dom = b.domain_of(cap)
            lvl = x.get("level")
            out.append(f"| {L(c, cap)} | {L(c, dom) if dom and dom != cap else ''} | {f'{lvl} ({LEVEL_NAMES[lvl]})' if lvl in LEVEL_NAMES else ''} | {esc_cell(x.get('why', ''))} |")
    ben = c.fm.get("benefits_from") or []
    if ben:
        out.append("\n# Capabilities that help\n")
        out.append("| Capability | Why |\n|---|---|")
        for x in ben:
            cap = x.get("capability")
            if cap in C:
                out.append(f"| {L(c, cap)} | {esc_cell(x.get('why', ''))} |")
    if c.ids("personas"):
        out.append("\n# Personas\n")
        out.append(md_list([f"{L(c, p)}: {C[p].description}" for p in c.ids("personas") if p in C]))
    if c.ids("patterns"):
        out.append("\n# Patterns\n")
        out.append(md_list([L(c, p) for p in c.ids("patterns")]))
    fws = b.inbound[c.id].get(("Framework", "applies_to"), [])
    if fws:
        out.append("\n# Frameworks that apply\n")
        out.append(md_list([f"{L(c, f)}: {C[f].description}" for f in sorted(fws, key=lambda i: C[i].title)]))
    caps = [x.get("capability") for x in req if x.get("capability") in C]
    if caps:
        out.append("\n# Platform fit\n")
        out.append("How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered "
                   "when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); "
                   "preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. "
                   "This is a starting point for a conversation, not a recommendation.\n")
        out.append("| Platform | Covered | Not covered |\n|---|---|---|")
        for p in b.platforms():
            if not b.techs_by_platform.get(p.id):
                continue
            cov, prev, miss = b.fit(p.id, caps)
            gaps = [L(c, m) for m in miss] + [L(c, m) + " (preview only)" for m in prev]
            out.append(f"| {L(c, p.id)} | {fit_cell(cov, prev, len(caps))} | {', '.join(gaps)} |")
    return "\n".join(out) + "\n"


def gen_track(b: Bundle, c: Concept) -> str:
    C, L = b.concepts, b.link
    out = ["# Levels\n"]
    for lv in c.fm.get("levels") or []:
        n = lv.get("level")
        out.append(f"## Level {n}: {lv.get('name') or LEVEL_NAMES.get(n, '')}\n")
        if lv.get("summary"):
            out.append(lv["summary"] + "\n")
        out.append(md_list(lv.get("criteria") or []))
        caps = [x for x in lv.get("capabilities") or [] if x in C]
        if caps:
            out.append("\n**Capabilities first relied on:** " + ", ".join(L(c, x) for x in caps))
        ext = lv.get("external_levels") or {}
        if ext:
            out.append("\n**Corresponds to:** " + "; ".join(f"{L(c, f)} level {v}" for f, v in ext.items() if f in C))
        out.append("")
    if c.ids("covers"):
        out.append("# Capabilities in scope\n")
        out.append(", ".join(L(c, x) for x in sorted(c.ids("covers"), key=b._cap_sort) if x in C))
    rel = list(dict.fromkeys(c.ids("related_tracks") + b.inbound[c.id].get(("Maturity Track", "related_tracks"), [])))
    if rel:
        out.append("\n# Related tracks\n")
        out.append(md_list([f"{L(c, t)}: {C[t].description}" for t in rel if t in C]))
    if "maturity-scale" in C:
        out.append(f"\nLevels follow the shared {L(c, 'maturity-scale', 'maturity scale')}.")
    return "\n".join(out) + "\n"


def gen_platform(b: Bundle, c: Concept) -> str:
    C, L = b.concepts, b.link
    techs = sorted(b.techs_by_platform.get(c.id, []), key=lambda t: C[t].title.lower())
    out = []
    if techs:
        ga = b.platform_caps(c.id, allow_preview=False)
        anyc = b.platform_caps(c.id, allow_preview=True)
        out.append("# Coverage by domain\n")
        out.append("A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. "
                   "Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform "
                   "lacks the capability, or that the bundle has not mapped it yet.\n")
        out.append("| Domain | Covered | Not covered |\n|---|---|---|")
        for dom in b.domains:
            caps = b.domain_caps(dom)
            cov = [x for x in caps if b.covered(x, ga)]
            prev = [x for x in caps if x not in cov and b.covered(x, anyc)]
            miss = [x for x in caps if x not in cov and x not in prev]
            gaps = [L(c, m) for m in miss] + [L(c, m) + " (preview only)" for m in prev]
            out.append(f"| {L(c, dom)} | {fit_cell(cov, prev, len(caps))} | {', '.join(gaps)} |")
    fams = c.fm.get("families") or []
    if fams:
        out.append("\n# Product families\n")
        for f in fams:
            members = [b.tlink(c, t) for t in f.get("technologies") or [] if t in C]
            alias = f" (also: {', '.join(f['aliases'])})" if f.get("aliases") else ""
            out.append(f"- **{f['name']}**{alias}: {', '.join(members)}")
    terms = c.fm.get("terminology") or {}
    if terms:
        out.append("\n# Terminology\n")
        out.append("| Name used on this platform | Capability |\n|---|---|")
        for cap, name in sorted(terms.items(), key=lambda kv: str(kv[1]).lower()):
            if cap in C:
                out.append(f"| {esc_cell(name)} | {L(c, cap)} |")
    if techs:
        out.append("\n# Technologies\n")
        by_dom = defaultdict(list)
        for t in techs:
            r = C[t].ids("realises")
            by_dom[b.domain_of(r[0]) if r and r[0] in C else None].append(t)
        for dom in b.domains + [None]:
            if by_dom.get(dom):
                out.append(f"## {C[dom].title if dom else 'Other'}\n")
                out.append(md_list([f"{b.tlink(c, t)}: {C[t].description}" for t in by_dom[dom]]))
                out.append("")
    return "\n".join(out) + "\n" if out else ""


def gen_framework(b: Bundle, c: Concept) -> str:
    C, L = b.concepts, b.link
    out = []
    levels = c.fm.get("maturity_levels") or []
    if levels:
        out.append("# Maturity levels\n")
        out.append("| Level | Name | Summary |\n|---|---|---|")
        out += [f"| {esc_cell(lv.get('level'))} | {esc_cell(lv.get('name', ''))} | {esc_cell(lv.get('summary', ''))} |" for lv in levels]
        tracks = b.inbound[c.id].get(("Maturity Track", "external_levels"), [])
        for t in dict.fromkeys(tracks):
            pairs = [(lv.get("level"), (lv.get("external_levels") or {}).get(c.id)) for lv in C[t].fm.get("levels") or []]
            pairs = [f"bundle level {a} ≈ level {v}" for a, v in pairs if v is not None]
            out.append(f"\nAligned with {L(c, t)}: {'; '.join(pairs)}.")
        out.append("")
    maps = c.fm.get("mappings") or []
    if maps:
        out.append("# Mapping to capabilities\n")
        out.append("| Area | Summary | Capabilities |\n|---|---|---|")
        for m in maps:
            caps = ", ".join(L(c, x) for x in m.get("capabilities") or [] if x in C)
            out.append(f"| {esc_cell(m.get('ref', ''))} | {esc_cell(m.get('summary', ''))} | {caps} |")
    rel = list(dict.fromkeys(c.ids("related") + b.inbound[c.id].get(("Framework", "related"), [])))
    if rel:
        out.append("\n# Related frameworks\n")
        out.append(md_list([f"{L(c, f)}: {C[f].description}" for f in rel if f in C]))
    if c.ids("applies_to"):
        out.append("\n# Applies to\n")
        out.append(md_list([f"{L(c, x)} ({C[x].type.lower()}): {C[x].description}" for x in c.ids("applies_to") if x in C]))
    return "\n".join(out) + "\n" if out else ""


GENERATORS = {
    "Capability": gen_capability,
    "Technology": gen_technology,
    "Pattern": gen_pattern,
    "Persona": gen_persona,
    "Use Case": gen_use_case,
    "Maturity Track": gen_track,
    "Platform": gen_platform,
    "Framework": gen_framework,
}


def render_concept(b: Bundle, c: Concept) -> str:
    fm = dump_frontmatter(c.fm)
    authored = c.authored.rstrip() + "\n"
    if not authored.startswith("\n"):
        authored = "\n" + authored
    gen = GENERATORS.get(c.type)
    text = f"---\n{fm}---\n{authored}"
    if gen:
        g = gen(b, c)
        if g.strip():
            text += f"\n{GEN_MARKER}\n\n{g}"
    return text


# --------------------------------------------------------------------------- indexes

def index_entry(b: Bundle, from_dir: str, cid: str, indent: int = 0, suffix: str = "") -> str:
    c = b.concepts[cid]
    relp = posixpath.relpath(c.rel, from_dir or ".")
    return f"{'  ' * indent}* [{c.title}]({relp}){suffix} - {c.description}"


def build_indexes(b: Bundle) -> dict[str, str]:
    C = b.concepts
    files: dict[str, str] = {}
    counts = defaultdict(int)
    for c in C.values():
        counts[c.type] += 1

    root = ["---", f'okf_version: "{OKF_VERSION}"', "---", "", "# Data platform capabilities", ""]
    root.append("A vendor-neutral map of what a data platform can do, how vendors provide it, which use cases need it and how maturity grows. "
                f"It holds {counts['Capability']} capabilities in {len(b.domains)} domains, {counts['Technology']} technologies across "
                f"{counts['Platform']} platform groups, {counts['Use Case']} use cases, {counts['Persona']} personas, {counts['Pattern']} patterns, "
                f"{counts['Maturity Track']} maturity tracks and {counts['Framework']} frameworks.")
    root.append("")
    root.append("Every concept is a Markdown file with YAML frontmatter. Relationships are written in frontmatter on one side only; the section "
                "below the `dpc:generated` line in each file is derived from them. All content is an unreviewed draft (`status: draft`).")
    root.append("")
    refs = sorted(b.of_type("Reference"), key=lambda x: (x.fm.get("order", 99), x.title))
    if refs:
        root.append("# Start here\n")
        root += [index_entry(b, "", r.id) for r in refs]
        root.append("")
    root.append("# Capability domains\n")
    for d in b.domains:
        root.append(f"* [{C[d].title}](capabilities/{d}/) - {C[d].description} ({len(b.domain_caps(d))} capabilities)")
    root.append("")
    root.append("# Other concepts\n")
    for folder, t in [("use-cases", "Use Case"), ("personas", "Persona"), ("patterns", "Pattern"), ("maturity", "Maturity Track"),
                      ("platforms", "Platform"), ("technologies", "Technology"), ("frameworks", "Framework")]:
        root.append(f"* [{FOLDER_TITLES[folder]}]({folder}/) - {counts[t]} {TYPE_PLURAL[t]}")
    root.append("")
    root.append("# Machine-readable exports\n")
    root.append("Run `python tools/dpc.py export` in the repository to write these to `dist/`:\n")
    root.append("* `graph.json` - every concept and typed edge, for graph tools and agents")
    root.append("* `capabilities.csv`, `technologies.csv`, `coverage-matrix.csv`, `use-case-requirements.csv` - flat tables for spreadsheets")
    root.append("* `capabilities.ttl` - the capability tree and links as SKOS/RDF")
    root.append("* `mindmap.md` - the capability tree as a Markmap mind map")
    root.append("* `explorer.html` - a single-file browser for the whole bundle, with use case, persona, platform and maturity lenses")
    files["index.md"] = "\n".join(root) + "\n"

    caps_idx = ["# Capability domains", ""]
    for d in b.domains:
        caps_idx.append(f"* [{C[d].title}]({d}/) - {C[d].description}")
    files["capabilities/index.md"] = "\n".join(caps_idx) + "\n"
    for d in b.domains:
        folder = f"capabilities/{d}"
        lines = [f"# {C[d].title}", ""]

        def walk(cid, depth):
            if b.domain_of(cid) != d:
                return
            lines.append(index_entry(b, folder, cid, depth))
            for ch in b.primary_children.get(cid, []):
                walk(ch, depth + 1)
        walk(d, 0)
        here = set(b.domain_caps(d))
        also = sorted({x for p in here for x in b.children.get(p, []) if b.domain_of(x) != d}, key=b._cap_sort)
        if also:
            lines += ["", "# Also part of this domain", ""]
            lines += [index_entry(b, folder, x, suffix=f" (main home: {C[b.domain_of(x)].title})") for x in also]
        files[f"{folder}/index.md"] = "\n".join(lines) + "\n"

    plat_folders = {p.id: p.fm.get("folder", p.id.replace("platform-", "")) for p in b.platforms()}
    tech_idx = ["# Technologies by platform", ""]
    for p in b.platforms():
        n = len(b.techs_by_platform.get(p.id, []))
        if n:
            tech_idx.append(f"* [{p.title}]({plat_folders[p.id]}/) - {n} technologies. {p.description}")
    files["technologies/index.md"] = "\n".join(tech_idx) + "\n"
    for p in b.platforms():
        ts = b.techs_by_platform.get(p.id, [])
        if not ts:
            continue
        folder = f"technologies/{plat_folders[p.id]}"
        lines = [f"# {p.title}", ""]
        by_dom = defaultdict(list)
        for t in ts:
            r = C[t].ids("realises")
            by_dom[b.domain_of(r[0]) if r and r[0] in C else None].append(t)
        for dom in b.domains + [None]:
            if by_dom.get(dom):
                lines.append(f"# {C[dom].title if dom else 'Other'}\n")
                lines += [index_entry(b, folder, t, suffix=b.suffix(t)) for t in sorted(by_dom[dom], key=lambda i: C[i].title.lower())]
                lines.append("")
        files[f"{folder}/index.md"] = "\n".join(lines).rstrip() + "\n"

    for folder, t in [("patterns", "Pattern"), ("personas", "Persona"), ("use-cases", "Use Case"),
                      ("platforms", "Platform"), ("frameworks", "Framework")]:
        items = b.of_type(t)
        if not items:
            continue
        key = (lambda x: (x.fm.get("order", 999), x.title.lower())) if t == "Platform" else (lambda x: x.title.lower())
        lines = [f"# {FOLDER_TITLES[folder]}", ""] + [index_entry(b, folder, x.id) for x in sorted(items, key=key)]
        files[f"{folder}/index.md"] = "\n".join(lines) + "\n"
    about = [r for r in refs if r.rel.startswith("about/")]
    if about:
        files["about/index.md"] = "\n".join([f"# {FOLDER_TITLES['about']}", ""] + [index_entry(b, "about", r.id) for r in about]) + "\n"
    tracks = b.of_type("Maturity Track")
    if tracks:
        lines = ["# Maturity", ""]
        mrefs = [r for r in refs if r.rel.startswith("maturity/")]
        if mrefs:
            lines += [index_entry(b, "maturity", r.id) for r in mrefs] + ["", "# Tracks", ""]
        lines += [index_entry(b, "maturity", x.id) for x in sorted(tracks, key=lambda x: x.title.lower())]
        files["maturity/index.md"] = "\n".join(lines) + "\n"
    return files


def build(b: Bundle, write: bool = True) -> list[str]:
    changed = []
    for c in b.concepts.values():
        new = render_concept(b, c)
        old = c.path.read_text(encoding="utf-8")
        if new != old:
            changed.append(c.rel)
            if write:
                c.path.write_text(new, encoding="utf-8")
    for rel, text in build_indexes(b).items():
        p = b.root / rel
        old = p.read_text(encoding="utf-8") if p.exists() else None
        if old != text:
            changed.append(rel)
            if write:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(text, encoding="utf-8")
    return changed


# --------------------------------------------------------------------------- export

def graph(b: Bundle) -> dict:
    nodes, edges = [], []
    for c in sorted(b.concepts.values(), key=lambda x: (TYPE_ORDER.index(x.type) if x.type in TYPE_ORDER else 99, x.id)):
        n = {"id": c.id, "type": c.type, "title": c.title, "description": c.description, "path": c.rel,
             "aliases": c.fm.get("aliases") or [], "status": c.fm.get("status", "stable")}
        if c.type == "Capability":
            n["domain"] = b.domain_of(c.id)
            n["depth"] = b.depth(c.id)
        if c.type == "Technology":
            for k in ("platform", "vendor", "kind", "availability", "resource", "formerly", "distribution_of"):
                if c.fm.get(k):
                    n[k] = c.fm[k]
            n["counted"] = b.is_counted(c.id)
        nodes.append(n)
        for field in TYPES.get(c.type, {}).get("rels", {}):
            val = c.fm.get(field)
            if isinstance(val, list) and val and isinstance(val[0], dict):
                for x in val:
                    e = {"source": c.id, "target": x["capability"], "type": field}
                    if x.get("level"):
                        e["level"] = x["level"]
                    edges.append(e)
            else:
                for t in c.ids(field):
                    edges.append({"source": c.id, "target": t, "type": field})
        if c.type == "Maturity Track":
            for lv in c.fm.get("levels") or []:
                for cap in lv.get("capabilities") or []:
                    edges.append({"source": c.id, "target": cap, "type": "introduces", "level": lv.get("level")})
        if c.type == "Framework":
            for m in c.fm.get("mappings") or []:
                for cap in m.get("capabilities") or []:
                    edges.append({"source": c.id, "target": cap, "type": "maps_to", "ref": m.get("ref")})
    return {"generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "okf_version": OKF_VERSION,
            "nodes": nodes, "edges": edges,
            "families": [{"platform": p, **f} for p, f in b.families]}


def ttl_str(s: str) -> str:
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def skos(b: Bundle, base: str) -> str:
    out = [f"@prefix dpc: <{base}> .", "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
           "@prefix dcterms: <http://purl.org/dc/terms/> .", "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
           "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .", ""]
    out.append("dpc:capabilities a skos:ConceptScheme ;\n  skos:prefLabel \"Data platform capabilities\"@en ;")
    out.append("  " + " ,\n  ".join(f"skos:hasTopConcept dpc:{d}" for d in b.domains) + " .\n")
    for t in ["Technology", "Pattern", "Persona", "UseCase", "MaturityTrack", "Platform", "Framework", "Reference"]:
        out.append(f"dpc:{t} a rdfs:Class .")
    for p in ["dependsOn", "realises", "platform", "uses", "caresAbout", "requires", "benefitsFrom", "covers", "mapsTo",
              "involvesPersona", "usesPattern", "distributionOf"]:
        out.append(f"dpc:{p} a rdf:Property .")
    out.append("")
    for c in sorted(b.concepts.values(), key=lambda x: x.id):
        lines = []
        if c.type == "Capability":
            lines.append("a skos:Concept")
            lines.append("skos:inScheme dpc:capabilities")
            if not c.ids("broader"):
                lines.append("skos:topConceptOf dpc:capabilities")
            lines += [f"skos:broader dpc:{p}" for p in c.ids("broader")]
            lines += [f"skos:related dpc:{p}" for p in c.ids("related")]
            lines += [f"dpc:dependsOn dpc:{p}" for p in c.ids("depends_on")]
            lines += [f"skos:altLabel {ttl_str(a)}@en" for a in c.fm.get("aliases") or []]
            lines.append(f"skos:definition {ttl_str(c.description)}@en")
        else:
            cls = {"Use Case": "UseCase", "Maturity Track": "MaturityTrack"}.get(c.type, c.type)
            lines.append(f"a dpc:{cls}")
            lines.append(f"dcterms:description {ttl_str(c.description)}@en")
            lines += [f"skos:altLabel {ttl_str(a)}@en" for a in (c.fm.get("aliases") or []) + (c.fm.get("formerly") or [])]
            if c.type == "Technology":
                lines += [f"dpc:realises dpc:{x}" for x in c.ids("realises")]
                if c.fm.get("platform"):
                    lines.append(f"dpc:platform dpc:{c.fm['platform']}")
                if c.fm.get("distribution_of"):
                    lines.append(f"dpc:distributionOf dpc:{c.fm['distribution_of']}")
            elif c.type == "Pattern":
                lines += [f"dpc:uses dpc:{x}" for x in c.ids("uses")]
            elif c.type == "Persona":
                lines += [f"dpc:caresAbout dpc:{x}" for x in c.ids("cares_about")]
            elif c.type == "Use Case":
                lines += [f"dpc:requires dpc:{x}" for x in c.ids("requires")]
                lines += [f"dpc:benefitsFrom dpc:{x}" for x in c.ids("benefits_from")]
                lines += [f"dpc:involvesPersona dpc:{x}" for x in c.ids("personas")]
                lines += [f"dpc:usesPattern dpc:{x}" for x in c.ids("patterns")]
            elif c.type == "Maturity Track":
                lines += [f"dpc:covers dpc:{x}" for x in c.ids("covers")]
            elif c.type == "Framework":
                caps = sorted({x for m in c.fm.get("mappings") or [] for x in m.get("capabilities") or []})
                lines += [f"dpc:mapsTo dpc:{x}" for x in caps]
            if c.fm.get("resource") and str(c.fm["resource"]).startswith("http"):
                lines.append(f"rdfs:seeAlso <{c.fm['resource']}>")
        lines.insert(1, f"skos:prefLabel {ttl_str(c.title)}@en")
        out.append(f"dpc:{c.id} " + " ;\n  ".join(lines) + " .\n")
    return "\n".join(out)


def mindmap(b: Bundle) -> str:
    C = b.concepts
    out = ["---", "title: Data platform capabilities", "markmap:", "  initialExpandLevel: 2", "---", "", "# Data platform capabilities", ""]

    def walk(cid, depth):
        out.append(f"{'  ' * depth}- **{C[cid].title}** `{cid}`")
        for ch in b.primary_children.get(cid, []):
            walk(ch, depth + 1)
    for d in b.domains:
        out.append(f"## {C[d].title}")
        for ch in b.primary_children.get(d, []):
            walk(ch, 0)
        out.append("")
    return "\n".join(out)


def export(b: Bundle, out_dir: Path, base: str):
    out_dir.mkdir(parents=True, exist_ok=True)
    g = graph(b)
    (out_dir / "graph.json").write_text(json.dumps(g, indent=1, ensure_ascii=False), encoding="utf-8")

    def write_csv(name, header, rows):
        with open(out_dir / name, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(rows)

    caps = sorted(b.of_type("Capability"), key=lambda c: (b.domains.index(b.domain_of(c.id)) if b.domain_of(c.id) in b.domains else 99, b._cap_sort(c.id)))
    write_csv("capabilities.csv", ["id", "title", "domain", "parents", "depth", "description", "aliases", "technologies"],
              [[c.id, c.title, b.domain_of(c.id), ";".join(c.ids("broader")), b.depth(c.id), c.description,
                ";".join(c.fm.get("aliases") or []), len(b.realised_by.get(c.id, []))] for c in caps])
    techs = sorted(b.of_type("Technology"), key=lambda t: (t.fm.get("platform", ""), t.title.lower()))
    write_csv("technologies.csv", ["id", "title", "platform", "vendor", "kind", "availability", "counted", "realises", "aliases", "formerly",
                                   "description", "resource"],
              [[t.id, t.title, t.fm.get("platform", ""), t.fm.get("vendor", ""), t.fm.get("kind", ""), t.fm.get("availability", ""),
                b.is_counted(t.id), ";".join(t.ids("realises")), ";".join(map(str, t.fm.get("aliases") or [])),
                ";".join(map(str, t.fm.get("formerly") or [])), t.description, t.fm.get("resource", "")] for t in techs])
    plats = [p for p in b.platforms() if b.techs_by_platform.get(p.id)]
    pcs = {p.id: b.platform_caps(p.id) for p in plats}
    write_csv("coverage-matrix.csv", ["capability", "title", "domain"] + [p.id for p in plats],
              [[c.id, c.title, b.domain_of(c.id)] + [len(pcs[p.id].get(c.id, [])) for p in plats] for c in caps])
    rows = []
    for u in sorted(b.of_type("Use Case"), key=lambda x: x.id):
        for kind in ("requires", "benefits_from"):
            for x in u.fm.get(kind) or []:
                rows.append([u.id, u.title, kind, x.get("capability"), x.get("level", ""), x.get("why", "")])
    write_csv("use-case-requirements.csv", ["use_case", "title", "relation", "capability", "min_level", "why"], rows)
    (out_dir / "capabilities.ttl").write_text(skos(b, base), encoding="utf-8")
    (out_dir / "mindmap.md").write_text(mindmap(b), encoding="utf-8")
    (out_dir / "explorer.html").write_text(explorer_html(b), encoding="utf-8")
    print(f"Wrote {len(list(out_dir.iterdir()))} files to {out_dir}")


# --------------------------------------------------------------------------- explorer

def explorer_data(b: Bundle) -> dict:
    C = b.concepts
    concepts = {}
    for c in C.values():
        body = render_concept(b, c).split("\n---\n", 1)[1]
        body = body.replace(GEN_MARKER, "")
        d = {"t": c.type, "ti": c.title, "d": c.description, "p": c.rel, "b": body.strip()}
        names = [str(a) for a in (c.fm.get("aliases") or []) + (c.fm.get("formerly") or [])]
        if names:
            d["a"] = names
        if c.type == "Capability":
            d["dom"] = b.domain_of(c.id)
            d["ch"] = b.primary_children.get(c.id, [])
        if c.type == "Technology":
            d["pl"] = c.fm.get("platform")
            d["r"] = c.ids("realises")
        concepts[c.id] = d
    for pid, f in b.families:  # let family names find their members
        for tid in f.get("technologies") or []:
            if tid in concepts:
                concepts[tid].setdefault("a", []).extend([f["name"]] + list(f.get("aliases") or []))
    plats = [p for p in b.platforms() if b.techs_by_platform.get(p.id)]
    coverage = {p.id: dict(b.platform_caps(p.id)) for p in plats}
    uc = {u.id: {"req": [[x["capability"], x.get("level")] for x in u.fm.get("requires") or []],
                 "ben": [x["capability"] for x in u.fm.get("benefits_from") or []]} for u in b.of_type("Use Case")}
    personas = {p.id: p.ids("cares_about") for p in b.of_type("Persona")}
    tracks = {t.id: {str(lv.get("level")): lv.get("capabilities") or [] for lv in t.fm.get("levels") or []} for t in b.of_type("Maturity Track")}
    desc = {cap.id: b.descendants(cap.id) for cap in b.of_type("Capability")}
    return {"concepts": concepts, "domains": b.domains, "platforms": [p.id for p in plats], "coverage": coverage,
            "uc": uc, "personas": personas, "tracks": tracks, "desc": desc,
            "generated": dt.date.today().isoformat()}


def explorer_html(b: Bundle) -> str:
    data = json.dumps(explorer_data(b), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = Path(__file__).with_name("explorer_template.html").read_text(encoding="utf-8")
    return tpl.replace("/*__DATA__*/null", data)


# --------------------------------------------------------------------------- query commands

def wrap(text: str, indent: str = "  ") -> str:
    return textwrap.fill(str(text), width=100, initial_indent=indent, subsequent_indent=indent)


def realisations(b: Bundle, cap: str, platform: str | None = None) -> dict:
    """{'direct': {platform: [tech]}, 'narrower': {platform: [(tech, cap)]}}"""
    out = {"direct": defaultdict(list), "narrower": defaultdict(list)}
    for t in b.realised_by.get(cap, []):
        p = b.concepts[t].fm.get("platform")
        if not platform or p == platform:
            out["direct"][p].append(t)
    for d in b.descendants(cap):
        for t in b.realised_by.get(d, []):
            p = b.concepts[t].fm.get("platform")
            if (not platform or p == platform) and t not in out["direct"][p]:
                out["narrower"][p].append((t, d))
    return out


def concept_json(b: Bundle, c: Concept) -> dict:
    C = b.concepts
    d = {"id": c.id, "type": c.type, "path": c.rel, "frontmatter": c.fm, "body": c.authored.strip()}
    inbound = {f"{t}.{f}": sorted(set(v)) for (t, f), v in b.inbound[c.id].items()}
    if inbound:
        d["inbound"] = inbound
    if c.type == "Capability":
        d["domain"] = b.domain_of(c.id)
        d["narrower"] = b.children.get(c.id, [])
        r = realisations(b, c.id)
        d["realised_by"] = {C[p].title if p in C else p: [{"id": t, "title": C[t].title, "availability": b.availability(t),
                                                           "counted": b.is_counted(t)} for t in ts] for p, ts in r["direct"].items()}
        d["realised_via_narrower"] = {C[p].title if p in C else p: [{"id": t, "title": C[t].title, "capability": cap} for t, cap in ts]
                                      for p, ts in r["narrower"].items()}
    if c.type == "Technology":
        d["equivalents"] = {C[p].title: [{"id": t, "title": C[t].title, "shared": s} for t, s in items] for p, items in b.equivalents(c.id).items()}
    if c.type == "Use Case":
        caps = c.ids("requires")
        d["platform_fit"] = {}
        for p in b.platforms():
            if b.techs_by_platform.get(p.id):
                cov, prev, miss = b.fit(p.id, caps)
                d["platform_fit"][p.id] = {"covered": cov, "preview_only": prev, "not_covered": miss}
    return d


def cmd_show(b: Bundle, cid: str, as_json: bool = False):
    c = b.concepts.get(cid)
    if not c:
        hits = search(b, cid, 5)
        sys.exit(f"No concept '{cid}'. Did you mean: {', '.join(h.id for h in hits)}?" if hits else f"No concept '{cid}'.")
    if as_json:
        print(json.dumps(concept_json(b, c), indent=1, ensure_ascii=False, default=str))
        return
    C = b.concepts
    print(f"{c.title} [{c.type}] ({c.id})\n{c.rel}\n")
    print(wrap(c.description, ""))
    for k in ("aliases", "formerly"):
        if c.fm.get(k):
            print(f"{k}: {', '.join(map(str, c.fm[k]))}")
    if c.type == "Capability":
        print(f"\ndomain: {b.domain_of(c.id)}")
        for label, ids in [("broader", c.ids("broader")), ("narrower", b.children.get(c.id, [])), ("related", c.ids("related")),
                           ("depends on", c.ids("depends_on")), ("needed by", b.inbound[c.id].get(("Capability", "depends_on"), []))]:
            if ids:
                print(f"{label}: {', '.join(ids)}")
        r = realisations(b, c.id)
        if r["direct"] or r["narrower"]:
            print("\nrealised by:")
            for p in b.platforms():
                direct = [C[t].title + b.suffix(t) for t in r["direct"].get(p.id, [])]
                narrow = r["narrower"].get(p.id, [])
                if direct:
                    print(wrap(f"{p.title}: {'; '.join(direct)}", "  "))
                if narrow:
                    print(wrap(f"{p.title} (via narrower): {'; '.join(f'{C[t].title} [{cap}]' for t, cap in narrow[:8])}"
                               + (f" and {len(narrow) - 8} more" if len(narrow) > 8 else ""), "  "))
        appears = appears_in(b, c)
        if appears:
            print("\nappears in:")
            for a in appears:
                print(wrap(re.sub(r"\]\([^)]*\)", "]", a).replace("**", "").replace("[", ""), "  "))
    elif c.type == "Technology":
        print(f"\nplatform: {c.fm.get('platform')}   availability: {c.fm.get('availability', 'ga')}"
              + (f"   distribution of: {c.fm['distribution_of']}" if c.fm.get("distribution_of") else ""))
        print(f"realises: {', '.join(c.ids('realises'))}")
        if c.fm.get("resource"):
            print(f"resource: {c.fm['resource']}")
        eq = b.equivalents(c.id)
        if eq:
            print("\nequivalents:")
            for p in b.platforms():
                if p.id in eq:
                    print(wrap(f"{p.title}: {'; '.join(C[t].title for t, _ in eq[p.id])}", "  "))
    elif c.type == "Use Case":
        for kind in ("requires", "benefits_from"):
            for x in c.fm.get(kind) or []:
                lvl = f" level {x['level']}" if x.get("level") else ""
                print(f"{kind}: {x['capability']}{lvl} - {x.get('why', '')}")
        for f in ("personas", "patterns"):
            if c.ids(f):
                print(f"{f}: {', '.join(c.ids(f))}")
    elif c.type == "Maturity Track":
        for lv in c.fm.get("levels") or []:
            print(f"\nLevel {lv['level']} {lv.get('name', '')}: {lv.get('summary', '')}")
            for cr in lv.get("criteria") or []:
                print(wrap("- " + cr, "  "))
            if lv.get("capabilities"):
                print(wrap("introduces: " + ", ".join(lv["capabilities"]), "  "))
            if lv.get("external_levels"):
                print(wrap("corresponds to: " + ", ".join(f"{k} level {v}" for k, v in lv["external_levels"].items()), "  "))
    elif c.type == "Framework":
        for m in c.fm.get("mappings") or []:
            print(wrap(f"- {m.get('ref')}: {', '.join(m.get('capabilities') or [])}", ""))
    elif c.type == "Platform":
        for f in c.fm.get("families") or []:
            print(wrap(f"family {f['name']}: {', '.join(f.get('technologies') or [])}", ""))
        if c.fm.get("terminology"):
            print("\nterminology:")
            for cap, name in c.fm["terminology"].items():
                print(f"  {name} -> {cap}")
    else:
        for field in TYPES.get(c.type, {}).get("rels", {}):
            ids = c.ids(field)
            if ids:
                print(f"{field}: {', '.join(ids)}")
    body = c.authored.strip()
    if body:
        print("\n" + body)


def _has_word(word: str, text: str) -> bool:
    return re.search(r"(?<![a-z0-9])" + re.escape(word) + r"(?![a-z0-9])", text) is not None


def search(b: Bundle, q: str, limit: int = 20, types: list[str] | None = None) -> list[Concept]:
    qn = norm(q).strip()
    words = [w for w in re.split(r"[^a-z0-9.&+/]+", qn) if w]
    fam_hits = defaultdict(int)
    for pid, f in b.families:
        names = [norm(f["name"])] + [norm(a) for a in f.get("aliases") or []]
        if any(qn == n for n in names):
            fam_hits[pid] = max(fam_hits[pid], 40)
            for t in f.get("technologies") or []:
                fam_hits[t] = max(fam_hits[t], 60)
        elif any(qn in n or n in qn for n in names if len(n) > 4):
            for t in f.get("technologies") or []:
                fam_hits[t] = max(fam_hits[t], 15)
    scored = []
    for c in b.concepts.values():
        if types and c.type not in types:
            continue
        names = [norm(n) for n in c.names]
        fields = [(norm(c.id.replace("-", " ")), 6), (names[0], 8), (" | ".join(names[1:]), 7),
                  (norm(c.description), 3), (norm(c.authored), 1)]
        score = 0
        for w in words:
            hit = 0
            for text, wt in fields:
                found = _has_word(w, text) if len(w) <= 4 else (w in text)
                if found:
                    hit += wt
            if not hit:
                score = 0
                break
            score += hit
        if any(qn == n for n in names) or qn == c.id:
            score += 100
        elif any(_has_word(qn, n) for n in names):
            score += 20
        score += fam_hits.get(c.id, 0)
        if score:
            boost = {"Capability": 5, "Use Case": 2, "Pattern": 2}.get(c.type, 0)
            scored.append((score + boost, c))
    scored.sort(key=lambda x: (-x[0], x[1].title))
    return [c for _, c in scored[:limit]]


def cmd_usecase(b: Bundle, uid: str, platform: str | None):
    u = b.concepts.get(uid)
    if not u or u.type != "Use Case":
        sys.exit(f"No use case '{uid}'. Use cases: {', '.join(sorted(x.id for x in b.of_type('Use Case')))}")
    C = b.concepts
    print(f"{u.title}: {u.description}\n")
    for kind, label in (("requires", "Requires"), ("benefits_from", "Benefits from")):
        items = u.fm.get(kind) or []
        if not items:
            continue
        print(f"{label}:")
        for x in items:
            cap = x["capability"]
            c = C.get(cap)
            lvl = f" [level {x['level']}]" if x.get("level") else ""
            print(f"  - {c.title if c else cap} ({cap}){lvl}")
            if x.get("why"):
                print(wrap(x["why"], "      "))
            if platform:
                r = realisations(b, cap, platform)
                direct = r["direct"].get(platform, [])
                narrow = r["narrower"].get(platform, [])
                if direct:
                    print(wrap("realised by: " + "; ".join(C[t].title + b.suffix(t) for t in direct), "      "))
                if narrow:
                    print(wrap("via narrower: " + "; ".join(f"{C[t].title}{b.suffix(t)} [{C[d].title}]" for t, d in narrow), "      "))
                if not direct and not narrow:
                    print("      realised by: nothing mapped")
        print()
    if platform:
        cov, prev, miss = b.fit(platform, u.ids("requires"))
        print(f"Fit: {fit_cell(cov, prev, len(u.ids('requires')))} required capabilities covered on {C[platform].title if platform in C else platform}.")
        if miss:
            print(wrap("Not covered: " + ", ".join(miss), "  "))


def cmd_coverage(b: Bundle, pid: str):
    p = b.concepts.get(pid)
    if not p or p.type != "Platform":
        sys.exit(f"No platform '{pid}'. Platforms: {', '.join(x.id for x in b.platforms())}")
    ga = b.platform_caps(pid, allow_preview=False)
    anyc = b.platform_caps(pid)
    print(f"{p.title}: {len(b.techs_by_platform.get(pid, []))} technologies\n")
    for dom in b.domains:
        caps = b.domain_caps(dom)
        cov = [x for x in caps if b.covered(x, ga)]
        prev = [x for x in caps if x not in cov and b.covered(x, anyc)]
        miss = [x for x in caps if x not in cov and x not in prev]
        print(f"{b.concepts[dom].title}: {fit_cell(cov, prev, len(caps))}")
        if prev:
            print(wrap("preview only: " + ", ".join(prev), "    "))
        if miss:
            print(wrap("not covered: " + ", ".join(miss), "    "))


TEMPLATES = {
    "Capability": "{explanation}\n\n# Key considerations\n\n- \n\n# Questions to ask\n\n- \n",
    "Technology": "{explanation}\n",
    "Pattern": "{explanation}\n\n# When to use\n\n- \n\n# Watch out for\n\n- \n",
    "Persona": "{explanation}\n\n# Goals\n\n- \n\n# Jobs\n\n- \n\n# Pain points\n\n- \n\n# Questions they ask\n\n- \n",
    "Use Case": "{explanation}\n\n# Non-functional requirements\n\n- \n\n# Risks\n\n- \n",
    "Maturity Track": "{explanation}\n",
    "Platform": "{explanation}\n",
    "Framework": "{explanation}\n",
    "Reference": "{explanation}\n",
}


def cmd_new(b: Bundle, args):
    t = type_from_arg(args.type)
    if not t:
        sys.exit(f"Unknown type '{args.type}'. Types: {', '.join(k.lower().replace(' ', '-') for k in TYPES)}")
    if not ID_RE.match(args.id):
        sys.exit("id must be lower-case kebab-case, e.g. column-lineage")
    if args.id in b.concepts:
        sys.exit(f"id '{args.id}' already exists at {b.concepts[args.id].rel}")
    fm = {"type": t, "id": args.id, "title": args.title, "description": args.description or "TODO: one sentence."}
    folder = TYPES[t]["folder"]
    if t == "Capability":
        if args.broader and args.broader not in b.concepts:
            sys.exit(f"Unknown parent '{args.broader}'")
        fm["aliases"] = []
        fm["broader"] = [args.broader] if args.broader else []
        dom = b.domain_of(args.broader) if args.broader else args.id
        folder = f"capabilities/{dom}"
        fm["tags"] = [dom]
    elif t == "Technology":
        if not args.platform or args.platform not in b.concepts:
            sys.exit("--platform is required and must be an existing platform id")
        fm["platform"] = args.platform
        fm["kind"] = "feature"
        fm["availability"] = "ga"
        fm["realises"] = [args.realises] if args.realises else []
        folder = f"technologies/{b.concepts[args.platform].fm.get('folder', args.platform.replace('platform-', ''))}"
    fm["status"] = "draft"
    fm["generated"] = {"by": f"human:{os.environ.get('USER', 'unknown')}", "at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    path = b.root / folder / f"{args.id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{dump_frontmatter(fm)}---\n\n" + TEMPLATES[t].format(explanation="TODO: explain it."), encoding="utf-8")
    print(f"Created {path}. Fill it in, then run `python tools/dpc.py build`.")


# --------------------------------------------------------------------------- CLI

def main(argv=None):
    ap = argparse.ArgumentParser(prog="dpc", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE, help="bundle folder (default: bundle/)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate", help="check the bundle")
    v.add_argument("--check-generated", action="store_true", help="also fail if `build` would change any file (use in CI)")
    v.add_argument("--quiet-coverage", action="store_true", help="hide warnings about capabilities no technology realises")
    sub.add_parser("build", help="regenerate generated sections and index.md files")
    e = sub.add_parser("export", help="write machine-readable exports and the HTML explorer")
    e.add_argument("--out", type=Path, default=DEFAULT_DIST)
    e.add_argument("--base-iri", default="https://example.org/data-platform-capabilities/",
                   help="namespace for the SKOS export (set this to your own)")
    s = sub.add_parser("show", help="show one concept")
    s.add_argument("id")
    s.add_argument("--json", action="store_true", help="print machine-readable JSON")
    q = sub.add_parser("search", help="search concepts")
    q.add_argument("query", nargs="+")
    q.add_argument("--type", action="append", help="limit to a type, e.g. capability or use-case (repeatable)")
    q.add_argument("--limit", type=int, default=20)
    q.add_argument("--long", action="store_true", help="also print descriptions")
    u = sub.add_parser("usecase", help="what a use case needs")
    u.add_argument("id")
    u.add_argument("--platform", help="show technologies from this platform, e.g. platform-aws")
    c = sub.add_parser("coverage", help="what a platform covers")
    c.add_argument("platform")
    n = sub.add_parser("new", help="create a concept from a template")
    n.add_argument("type", help="capability, technology, pattern, persona, use-case, maturity-track, platform, framework, reference")
    n.add_argument("id")
    n.add_argument("--title", required=True)
    n.add_argument("--description")
    n.add_argument("--broader", help="parent capability id (capabilities)")
    n.add_argument("--platform", help="platform id (technologies)")
    n.add_argument("--realises", help="capability id (technologies)")
    sub.add_parser("stats", help="count concepts")
    args = ap.parse_args(argv)

    b = Bundle(args.bundle)
    if args.cmd == "validate":
        return validate(b, args.check_generated, args.quiet_coverage)
    if args.cmd == "build":
        changed = build(b)
        print(f"Updated {len(changed)} files." if changed else "Everything is up to date.")
        return 0
    if args.cmd == "export":
        export(b, args.out, args.base_iri)
        return 0
    if args.cmd == "show":
        cmd_show(b, args.id, args.json)
        return 0
    if args.cmd == "search":
        types = None
        if args.type:
            types = [type_from_arg(t) for t in args.type]
            if None in types:
                sys.exit(f"Unknown type in {args.type}. Types: {', '.join(k.lower().replace(' ', '-') for k in TYPES)}")
        for c in search(b, " ".join(args.query), args.limit, types):
            where = b.domain_of(c.id) if c.type == "Capability" else c.fm.get("platform", "")
            print(f"{c.id:48} {c.type:15} {c.title}" + (f"  [{where}]" if where else ""))
            if args.long:
                print(wrap(c.description, "    "))
        return 0
    if args.cmd == "usecase":
        cmd_usecase(b, args.id, args.platform)
        return 0
    if args.cmd == "coverage":
        cmd_coverage(b, args.platform)
        return 0
    if args.cmd == "new":
        cmd_new(b, args)
        return 0
    if args.cmd == "stats":
        counts = defaultdict(int)
        for c in b.concepts.values():
            counts[c.type] += 1
        for t in TYPE_ORDER:
            print(f"{t:15} {counts[t]}")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
