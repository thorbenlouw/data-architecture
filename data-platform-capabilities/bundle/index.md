---
okf_version: "0.2"
---

# Data platform capabilities

A vendor-neutral map of what a data platform can do, how vendors provide it, which use cases need it and how maturity grows. It holds 338 capabilities in 20 domains, 1090 technologies across 15 platform groups, 25 use cases, 16 personas, 21 patterns, 27 maturity tracks and 16 frameworks.

Every concept is a Markdown file with YAML frontmatter. Relationships are written in frontmatter on one side only; the section below the `dpc:generated` line in each file is derived from them. All content is an unreviewed draft (`status: draft`).

# Start here

* [Using this bundle](about/using-this-bundle.md) - What the bundle contains, how it is organised and how to answer the common questions with it.
* [Conventions](about/conventions.md) - The frontmatter fields, relationship rules, naming rules and editorial rules every concept follows.
* [Sources and method](about/sources-and-method.md) - How the first version of the bundle was researched and written, how it was checked, and its known limitations.
* [Maturity scale](maturity/maturity-scale.md) - The five maturity levels used by every maturity track and every use case requirement in the bundle.
* [Choosing between similar capabilities](about/similar-capabilities.md) - Groups of capabilities that are easily confused, with one line on what each is and when to choose it.
* [Read paths for applications](about/application-read-paths.md) - How an application should read data from the platform, or publish data to it, compared by latency, concurrency, freshness, consistency and coupling.
* [Mapping a use case to capabilities](about/mapping-a-use-case.md) - A practical method for turning a business use case into required capabilities with minimum maturity levels, checking platform fit and recording the result.
* [Running a maturity assessment](about/assessing-maturity.md) - How to assess maturity with the tracks, from scope and evidence to scoring, gap analysis against use cases, presentation and re-assessment.

# Capability domains

* [Ingestion and integration](capabilities/ingestion-integration/) - Bring data from source systems into the platform and keep it in step with them. (22 capabilities)
* [Storage and table management](capabilities/storage/) - Store data durably and cheaply in formats that many tools can read and manage it as reliable tables. (23 capabilities)
* [Processing and transformation](capabilities/processing/) - Transform, clean, join and aggregate data into forms ready for use. (18 capabilities)
* [Orchestration](capabilities/orchestration/) - Schedule, sequence and coordinate the jobs that move and transform data. (5 capabilities)
* [Query and compute](capabilities/compute/) - Provide the query engines and processing power that run workloads, sized and isolated appropriately. (22 capabilities)
* [Serving and activation](capabilities/serving/) - Deliver data to the applications, people and processes that use it, at the latency and volume they need. (13 capabilities)
* [Analytics and BI](capabilities/analytics-bi/) - Help people explore, visualise and report on data to make decisions. (20 capabilities)
* [Machine learning development](capabilities/machine-learning/) - Develop, train and evaluate machine learning models on platform data. (20 capabilities)
* [ML operations](capabilities/mlops/) - Deploy, run, monitor and improve models in production reliably. (18 capabilities)
* [Generative AI](capabilities/generative-ai/) - Build applications that use large language models and other generative models with enterprise data. (23 capabilities)
* [Metadata and discovery](capabilities/metadata/) - Capture, organise and expose information about data so people and machines can find, understand and trust it. (20 capabilities)
* [Data quality and observability](capabilities/data-quality/) - Measure, monitor and improve whether data is fit for its intended use. (12 capabilities)
* [Master and reference data](capabilities/master-data/) - Create and maintain consistent, trusted versions of core business entities and shared code lists. (7 capabilities)
* [Governance and compliance](capabilities/governance/) - Set and enforce the rules, roles and controls for how data is managed and used. (24 capabilities)
* [Security and access](capabilities/security/) - Protect data from unauthorised access, loss and misuse. (23 capabilities)
* [Data sharing and collaboration](capabilities/data-sharing/) - Share data within and beyond the organisation safely, without unnecessary copies. (8 capabilities)
* [Data products](capabilities/data-products/) - Manage data as products with owners, consumers, contracts and service levels. (7 capabilities)
* [Development and DataOps](capabilities/development-lifecycle/) - Build, test and release data and AI workloads safely and repeatably, from first commit to production. (16 capabilities)
* [Platform operations](capabilities/platform-operations/) - Run the data platform itself, including provisioning, tenancy, cost, monitoring and resilience. (27 capabilities)
* [Specialised data types](capabilities/specialised-data/) - Store and analyse data types that need specialised models, functions or engines. (10 capabilities)

# Other concepts

* [Use cases](use-cases/) - 25 use cases
* [Personas](personas/) - 16 personas
* [Patterns](patterns/) - 21 patterns
* [Maturity tracks](maturity/) - 27 maturity tracks
* [Platforms](platforms/) - 15 platform groups
* [Technologies](technologies/) - 1090 technologies
* [Frameworks, standards and regulations](frameworks/) - 16 frameworks

# Machine-readable exports

Run `python tools/dpc.py export` in the repository to write these to `dist/`:

* `graph.json` - every concept and typed edge, for graph tools and agents
* `capabilities.csv`, `technologies.csv`, `coverage-matrix.csv`, `use-case-requirements.csv` - flat tables for spreadsheets
* `capabilities.ttl` - the capability tree and links as SKOS/RDF
* `mindmap.md` - the capability tree as a Markmap mind map
* `explorer.html` - a single-file browser for the whole bundle, with use case, persona, platform and maturity lenses
