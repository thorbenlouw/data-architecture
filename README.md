# Data platform capabilities

A vendor-neutral map of what an enterprise data platform can do, for data architects and the AI agents that help them. It answers questions such as:

- Which capabilities does this use case need, and how mature must each be?
- How mature are we at lineage, MLOps or path to live, judged against observable criteria?
- What does Snowflake, Databricks, AWS or Microsoft call this, and which product provides it?
- What is the closest equivalent of this product on another platform?
- Which capabilities does BCBS 239, the EU AI Act or DCAM touch?

The knowledge lives in `bundle/` as an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (OKF v0.2) bundle: one Markdown file per concept with YAML frontmatter, readable without any tooling.

| Concept | Count | What it is |
|---|---|---|
| Capability | 338 in 20 domains | Something a data platform can do, without naming a product, arranged from domains such as *Metadata and discovery* down to detail such as *Column-level lineage* |
| Technology | 1,090 | A product, feature, open-source project or open standard, mapped to the capabilities it realises, with availability and former names |
| Platform | 15 | AWS, Microsoft, Google Cloud, Snowflake, Databricks, ClickHouse, Informatica, Cloudera, Oracle, SAP, Teradata, IBM, Palantir, open source and independent vendors |
| Use case | 25 | A business outcome with the capabilities it requires, the minimum maturity level and why |
| Persona | 16 | People who use or run the platform, their jobs, pain points and the capabilities they rely on |
| Pattern | 21 | Architectures and modelling approaches, such as lakehouse, medallion or Data Vault |
| Maturity track | 27 | Five observable levels for one area, aligned with external models where they exist |
| Framework | 16 | DAMA-DMBOK, DCAM, CDMC, BCBS 239, EU AI Act, GDPR, DORA, ISO/IEC 42001, NIST AI RMF and others, mapped onto capabilities |

All content is an **unreviewed draft** produced on 16 October 2026 (`status: draft`). Read `bundle/about/sources-and-method.md` before relying on it.

## Start here

- `bundle/index.md`: the root index, with the 20 domains.
- `bundle/about/using-this-bundle.md`: how to answer the common questions.
- `bundle/about/mapping-a-use-case.md` and `bundle/about/assessing-maturity.md`: methods for the two most common architect tasks.
- `dist/explorer.html`: open it in a browser to browse the tree, highlight it for a use case, persona, platform or maturity track, and see a platform coverage heat map. Rebuild it with `python tools/dpc.py export`.

## Tooling

Needs Python 3.10 or later and PyYAML (`pip install -r requirements.txt`).

```sh
python tools/dpc.py search lineage                    # find concepts, including by vendor name or former name
python tools/dpc.py show column-lineage               # a concept, its relationships and what provides it
python tools/dpc.py show databricks-unity-catalog --json
python tools/dpc.py usecase usecase-fraud-detection --platform platform-databricks
python tools/dpc.py coverage platform-snowflake
python tools/dpc.py new capability my-capability --title "My capability" --broader data-lineage
python tools/dpc.py build                             # regenerate generated sections and index.md files
python tools/dpc.py validate --check-generated        # what CI runs
python tools/dpc.py export                            # graph.json, CSVs, SKOS Turtle, mind map, explorer into dist/
python tools/test_dpc.py                              # self-tests
```

Relationships are written in frontmatter on one side only (for example a technology says which capabilities it `realises`). `build` writes the reverse view into the part of each file below the `dpc:generated` line, and rebuilds every `index.md`. Edit above that line only.

## Repository layout

```
bundle/               the OKF bundle (source of truth)
  index.md            root index (okf_version)
  log.md              update history
  about/              guidance pages
  capabilities/       one folder per domain
  technologies/       one folder per platform
  platforms/ patterns/ personas/ use-cases/ maturity/ frameworks/
tools/dpc.py          validator, builder, exporter and query CLI
tools/explorer_template.html
tools/test_dpc.py     self-tests
dist/                 generated exports (not committed; rebuilt by CI)
AGENTS.md             instructions for AI agents working with the bundle
CONTRIBUTING.md       how to add and review content
```

## Using it with agents

Point an agent at `AGENTS.md`. The bundle also works with OKF tooling such as `okflib`, which can serve it over MCP. `dist/graph.json` holds every concept and typed edge for graph tools, and `dist/capabilities.ttl` is the capability tree as SKOS for RDF tools (set `--base-iri` to your own namespace).

## Licence

No licence has been chosen yet. Add one before sharing outside your organisation. Product names belong to their owners.
