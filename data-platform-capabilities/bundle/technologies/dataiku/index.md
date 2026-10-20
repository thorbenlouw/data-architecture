# Dataiku

# Ingestion and integration

* [Dataiku connections](dataiku-connections.md) - Connectors that read and write data in SQL databases, cloud warehouses, object storage, Iceberg tables, NoSQL stores and business applications, and let recipes run inside the connected engine.

# Processing and transformation

* [Dataiku Flow and visual recipes](dataiku-flow-visual-recipes.md) - Visual pipeline of datasets and recipes, in which the Prepare recipe and recipes such as join, group, window, pivot and fuzzy join transform data without code and can run in the underlying database or Spark.

# Orchestration

* [Dataiku scenarios](dataiku-scenarios.md) - Automation that builds datasets, verifies data quality rules, retrains models and runs other steps on schedules or triggers, and reports results by email, chat or webhook.

# Analytics and BI

* [Dataiku dashboards and Stories](dataiku-dashboards-stories.md) - Charts, dashboards with filters, cross-filtering and drill-down, and Stories, slide-style presentations of live data that an assistant can draft from instructions.

# Machine learning development

* [Dataiku Feature Store](dataiku-feature-store.md) - Registry of curated feature groups, shared datasets that other projects join in batch or look up from API services in real time.
* [Dataiku labeling](dataiku-labeling.md) - Labeling recipe in which people classify or annotate images, text and tabular records to create training data.
* [Dataiku Visual ML](dataiku-visual-ml.md) - Visual and code-assisted model building for prediction, clustering, time series forecasting and causal prediction, with automatic feature handling, algorithm search, explanations and stress tests.

# ML operations

* [Dataiku Govern](dataiku-govern.md) - Separate governance node that keeps registries of projects, bundles, models and agents, with sign-off workflows, deployment policies and custom governance templates.
* [Dataiku model evaluation stores and Unified Monitoring](dataiku-model-monitoring.md) - Stores of repeated model evaluations with drift and performance metrics, and dashboards that show the health of deployed projects, Dataiku API endpoints and external endpoints.

# Generative AI

* [Dataiku Agent Hub](dataiku-agent-hub.md) (unconfirmed) - Portal in which business users chat with the agents an organisation publishes and build their own quick agents over documents and data.
* [Dataiku Knowledge Banks](dataiku-knowledge-banks.md) - Retrieval stores built by recipes that extract text and fields from documents, split and embed them, and index them for retrieval-augmented generation and agents.
* [Dataiku LLM Mesh](dataiku-llm-mesh.md) - Gateway through which Dataiku projects, agents and applications call commercial, cloud-hosted and self-hosted LLMs, with guardrails, cost quotas, rate limits, evaluation and logging.
* [Dataiku Prompt Studios](dataiku-prompt-studios.md) - Workspace for writing, testing and comparing prompts across LLMs, and the Prompt recipe that applies a saved prompt to every row of a dataset.
* [Dataiku Visual Agents and Code Agents](dataiku-agents.md) - Agents built visually or in Python on the LLM Mesh, using managed tools, knowledge banks, semantic models and MCP tools, with human approval steps, tracing, evaluation and MCP and A2A servers for other systems.

# Metadata and discovery

* [Dataiku Catalog](dataiku-catalog.md) - Instance-wide catalogue for finding datasets, models, agents, knowledge banks and other project assets, with curated collections, a most-used datasets view and AI-generated descriptions.
* [Dataiku Data Lineage](dataiku-data-lineage.md) - Column-level lineage across datasets and projects in a Dataiku instance, with manual lineage entries and exports of the lineage graph.
* [Dataiku Semantic Models](dataiku-semantic-models.md) (unconfirmed) - Business models of tables, columns, relationships and metrics that agents use to turn natural-language questions into correct SQL.

# Data quality and observability

* [Dataiku Data Quality rules](dataiku-data-quality.md) - Rules on dataset contents, such as value ranges, uniqueness, record counts, schema and values within their usual range, that can run automatically after each build and roll up into dataset, project and instance views.

# Governance and compliance

* [Dataiku Agent Management](dataiku-agent-management.md) (preview) - Standalone product that finds AI agents running on Dataiku and other vendors' platforms, maps the tools and models they use, and tracks their performance, risk and certification status.

# Development and DataOps

* [Dataiku Cobuild](dataiku-cobuild.md) - Agent inside a Dataiku project that builds and edits Flows, recipes, models, knowledge banks, agents, dashboards, notebooks and scenarios from natural-language requests.
* [Dataiku code recipes and notebooks](dataiku-code-recipes-notebooks.md) - Python, R, SQL, Hive, Impala, PySpark, SparkR, SparkSQL, Spark Scala and shell recipes and Jupyter and SQL notebooks that run inside the Flow alongside visual recipes.
* [Dataiku Code Studios](dataiku-code-studios.md) - Browser-based development environments such as VS Code, JupyterLab and RStudio that run in containers next to a project, with coding agents such as Claude Code, OpenAI Codex and GitHub Copilot.
* [Dataiku Deployer and API nodes](dataiku-deployer.md) - Deployment of project bundles to automation nodes and of models and functions as real-time API services on API nodes, Kubernetes or external machine learning platforms, with several endpoint versions able to share traffic.
* [Dataiku DSS](dataiku.md) - Platform in which teams build data pipelines, models, generative AI applications and agents as shared projects, with managed code environments, Git-based version control, containerised execution and per-user security.
* [Dataiku webapps and Dataiku Applications](dataiku-webapps.md) - Hosted web applications written in HTML and JavaScript, Python (Dash, Streamlit, Bokeh, FastAPI) or R Shiny, and Dataiku Applications, which package a project as a reusable form-driven tool.

# Platform operations

* [Dataiku Cloud](dataiku-cloud.md) - Edition of Dataiku that Dataiku hosts, operates and upgrades as a service, administered through a Launchpad and connected to the customer's own data sources.
* [Dataiku Cloud Stacks and Fleet Manager](dataiku-cloud-stacks.md) - Self-managed deployment of Dataiku in the customer's AWS, Azure or Google Cloud account, where Fleet Manager creates, upgrades, backs up and configures the Dataiku instances.
