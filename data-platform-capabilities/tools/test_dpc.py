#!/usr/bin/env python3
"""Self-tests for dpc.py and the bundle. Run: python tools/test_dpc.py"""
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dpc  # noqa: E402

B = dpc.Bundle(dpc.DEFAULT_BUNDLE)


def run(*args) -> str:
    buf = io.StringIO()
    with redirect_stdout(buf):
        dpc.main(list(args))
    return buf.getvalue()


class BundleTests(unittest.TestCase):
    def test_validates_without_errors(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = dpc.validate(B, check_generated=True)
        self.assertEqual(code, 0, buf.getvalue()[-2000:])

    def test_every_capability_has_a_domain_and_track(self):
        covered = {x for t in B.of_type("Maturity Track") for x in t.ids("covers")}
        for c in B.of_type("Capability"):
            self.assertIn(B.domain_of(c.id), B.domains, c.id)
            if c.ids("broader"):
                self.assertIn(c.id, covered, f"{c.id} is in no maturity track")

    def test_use_case_levels_in_range(self):
        for u in B.of_type("Use Case"):
            self.assertTrue(u.ids("requires"), u.id)
            for x in u.fm["requires"]:
                self.assertIn(x.get("level"), dpc.LEVEL_NAMES, (u.id, x))

    def test_marker_only_matches_whole_line(self):
        text = "---\ntype: Reference\n---\n\nSee `<!-- dpc:generated ... -->` in text.\n\nMore.\n"
        fm, authored, gen, err = dpc.split_doc(text)
        self.assertIsNone(err)
        self.assertIn("More.", authored)


class SearchTests(unittest.TestCase):
    def first(self, q, **kw):
        hits = dpc.search(B, q, 5, **kw)
        return hits[0].id if hits else None

    def test_acronyms(self):
        self.assertEqual(self.first("RAG"), "retrieval-augmented-generation")
        self.assertEqual(self.first("ODS"), "operational-data-store")

    def test_us_spelling(self):
        self.assertEqual(self.first("materialized views", types=["Capability"]), "materialised-views")

    def test_vendor_terms(self):
        hits = [c.id for c in dpc.search(B, "Delta Live Tables", 5)]
        self.assertIn("databricks-lakeflow-pipelines", hits)

    def test_user_phrases(self):
        self.assertEqual(self.first("fast read views"), "read-optimised-views")


class CommandTests(unittest.TestCase):
    def test_show_json(self):
        d = json.loads(run("show", "column-lineage", "--json"))
        self.assertEqual(d["domain"], "metadata")
        self.assertTrue(d["realised_by"])

    def test_usecase_with_platform(self):
        out = run("usecase", "usecase-fraud-detection", "--platform", "platform-databricks")
        self.assertIn("Fit:", out)

    def test_export(self):
        with tempfile.TemporaryDirectory() as d:
            with redirect_stdout(io.StringIO()):
                dpc.export(B, Path(d), "https://example.org/dpc/")
            g = json.loads((Path(d) / "graph.json").read_text())
            ids = {n["id"] for n in g["nodes"]}
            for e in g["edges"]:
                self.assertIn(e["target"], ids, e)
            self.assertIn("<title>", (Path(d) / "explorer.html").read_text()[:2000])


if __name__ == "__main__":
    unittest.main(verbosity=1)
