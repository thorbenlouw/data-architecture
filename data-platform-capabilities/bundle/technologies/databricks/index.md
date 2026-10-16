# Databricks

# Ingestion and integration

* [Databricks Auto Loader](databricks-auto-loader.md) - A Structured Streaming source (cloudFiles) that discovers new files in cloud storage and processes each one exactly once, with schema inference, schema evolution and a rescued-data column.
* [Lakeflow Connect](databricks-lakeflow-connect.md) - Managed connectors that ingest data incrementally from SaaS applications, databases (including change data capture), file sources and message buses into Unity Catalog tables, running on serverless Lakeflow pipelines.
* [Zerobus Ingest](databricks-zerobus-ingest.md) - A serverless push API that writes records straight into Unity Catalog Delta tables. Clients can use gRPC SDKs, REST, OpenTelemetry (OTLP), MQTT or Kafka-compatible producers, and no message broker is needed.

# Storage and table management

* [Databricks catalog federation](databricks-catalog-federation.md) - Mounts external catalogues such as Hive metastore, AWS Glue, Snowflake Horizon and Salesforce Data 360 as foreign catalogs, read from object storage under Unity Catalog governance.
* [Databricks liquid clustering](databricks-liquid-clustering.md) - A data layout method that clusters table files by key columns you can change at any time, replacing partitioning and Z-ordering. With CLUSTER BY AUTO, Databricks chooses the keys from query history.
* [Databricks predictive optimization](databricks-predictive-optimization.md) - Runs OPTIMIZE, VACUUM and ANALYZE automatically on Unity Catalog managed tables and chooses liquid clustering keys, based on how each table is used.
* [Databricks table clone (shallow and deep clone)](databricks-table-clone.md) - Copies a table at a given version. A shallow clone copies only metadata and points at the source files, while a deep clone copies the data as well.
* [Databricks VARIANT data type](databricks-variant.md) - A binary type for semi-structured data such as JSON that is queried without a fixed schema, with shredding into columns for faster reads.
* [Delta Lake on Databricks](databricks-delta-lake.md) - Databricks' managed implementation of Delta Lake tables, with ACID commits, MERGE, UPDATE and DELETE, schema enforcement, time travel, deletion vectors and type widening.
* [Unity Catalog](databricks-unity-catalog.md) - The account-wide catalogue and governance layer for tables, volumes, functions, models, AI services and connections. It provides a three-level namespace, SQL privileges, audit and workspace bindings.
* [Unity Catalog managed Iceberg tables](databricks-managed-iceberg-tables.md) - Apache Iceberg tables (v1 to v3) that Unity Catalog manages, with compaction, snapshot expiry and liquid clustering. Databricks and external engines can read and write them through the Iceberg REST catalogue.
* [Unity Catalog managed tables](databricks-unity-catalog-managed-tables.md) - Delta or Iceberg tables whose storage location, file layout, maintenance and lifecycle Unity Catalog manages, including on Databricks-managed default storage.

# Processing and transformation

* [Databricks AI Functions](databricks-ai-functions.md) - SQL and Python functions that call models over table data. They include ai_query, ai_extract, ai_classify, ai_summarize, ai_translate, ai_mask, ai_forecast and ai_similarity, with ai_search, ai_prep_search and ai_transcribe in Beta.
* [Databricks ai_parse_document](databricks-ai-parse-document.md) - An AI Function that extracts text, tables and layout elements from PDFs, images and office documents stored in volumes, returning structured output.
* [Lakeflow Designer](databricks-lakeflow-designer.md) - A visual, no-code canvas where analysts build data preparation flows from operators or natural-language prompts. The flows are backed by generated code governed in Unity Catalog.
* [Lakeflow pipelines](databricks-lakeflow-pipelines.md) - A declarative framework in which you define streaming tables, materialised views and flows in SQL or Python. The platform then works out dependencies, incremental refresh, retries and infrastructure.
* [Unity Catalog functions (UDFs)](databricks-unity-catalog-functions.md) - SQL, Python, Scala and Java user-defined functions registered and governed in Unity Catalog. They run on serverless and standard compute with sandboxing.

# Orchestration

* [Lakeflow Jobs](databricks-lakeflow-jobs.md) - Built-in orchestrator that runs dependency graphs of notebooks, pipelines, SQL, dbt and other tasks on schedules or on file-arrival, table-update and continuous triggers, with retries and loops.

# Query and compute

* [Databricks AI Runtime](databricks-ai-runtime.md) (preview) - Serverless GPU compute for deep learning, used to train and fine-tune models on one or many GPUs with PyTorch DDP and FSDP, DeepSpeed or Ray.
* [Databricks classic compute (Databricks Runtime clusters)](databricks-classic-compute.md) - All-purpose and job clusters, plus instance pools, running Databricks Runtime in the customer's cloud account. You choose instance types, autoscaling and access mode.
* [Databricks Free Edition](databricks-free-edition.md) - A no-cost, serverless-only, quota-limited Databricks environment for learning and experiments. It includes notebooks, SQL, Lakeflow, dashboards, Genie, Genie Code and Lakebase.
* [Databricks Iceberg reads (UniForm)](databricks-iceberg-reads-uniform.md) - Generates Iceberg metadata asynchronously for Delta tables so that Iceberg clients can read them without copying the data.
* [Databricks Lakehouse Real-Time](databricks-lakehouse-real-time.md) (preview) - A serverless SQL warehouse type tuned for sub-second reads of Unity Catalog tables by many concurrent users and applications.
* [Databricks Photon](databricks-photon.md) - Databricks' native C++ vectorised execution engine. It runs Spark SQL and DataFrame operations on columnar batches and falls back to Spark for operations it does not support.
* [Databricks serverless compute](databricks-serverless-compute.md) - Databricks-managed, versionless compute for notebooks, jobs and pipelines. It starts quickly, scales automatically and is billed in DBUs per use.
* [Databricks SQL](databricks-sql.md) - The data warehousing product on the lakehouse. It includes the SQL editor, queries, ANSI SQL engine, SQL transformations, materialised views and BI connectivity, running on SQL warehouses.
* [Databricks SQL warehouses (serverless, pro and classic)](databricks-sql-warehouses.md) - Compute for Databricks SQL in serverless, pro or classic form. Serverless warehouses start in seconds and use intelligent workload management to scale and queue queries.
* [Lakehouse Federation (query federation)](databricks-lakehouse-federation.md) - Read-only queries against external databases such as PostgreSQL, Oracle, SQL Server, Snowflake, BigQuery, Redshift and Teradata through Unity Catalog foreign catalogs, with query pushdown.
* [Unity Catalog Iceberg REST Catalog API](databricks-iceberg-rest-catalog.md) - An Iceberg REST catalogue endpoint with credential vending. Spark, Flink, Trino, Snowflake and other engines can use it to read and write Unity Catalog tables.

# Serving and activation

* [Databricks change data feed](databricks-change-data-feed.md) - Records row-level inserts, updates and deletes on Delta tables so downstream jobs and streams can read only the changes.
* [Databricks JDBC, ODBC and ADBC drivers](databricks-sql-drivers.md) - Client drivers and connectors (JDBC, ODBC, ADBC, Python, Go and Node.js) plus the SQL Statement Execution REST API, used to query Databricks SQL warehouses from tools and code.
* [Lakebase](databricks-lakebase.md) - Fully managed Postgres in the Databricks platform. Compute is separate from storage, and it offers autoscaling, scale-to-zero, copy-on-write branching, instant point-in-time restore and read replicas.

# Analytics and BI

* [Databricks AI/BI dashboards](databricks-ai-bi-dashboards.md) - Built-in dashboards with AI-assisted authoring, cross-filtering and drill-through. They can be shared at account level, sent on schedules by email or Slack, and embedded in external applications.
* [Databricks Excel Add-in](databricks-excel-add-in.md) - A Microsoft Excel add-in for querying governed Databricks tables and metric views from a workbook.
* [Databricks SQL alerts](databricks-sql-alerts.md) - Scheduled queries that evaluate a condition and send email, Slack or webhook notifications when it is met.
* [Genie Agents](databricks-genie-agents.md) - Domain-specific chat interfaces that analysts curate with tables, metric views, example SQL and instructions. They answer business questions in natural language with SQL, tables and charts.
* [Genie One](databricks-genie-one.md) - A simplified interface for business users that combines chat across governed data, dashboards and apps in one place, available in the browser, desktop, Excel and Google Sheets.
* [Unity Catalog metric views](databricks-metric-views.md) - YAML- or SQL-defined semantic objects that keep measures apart from dimensions. They are registered in Unity Catalog and queried from SQL, dashboards, Genie and external BI tools.

# Machine learning development

* [Databricks AutoML](databricks-automl.md) - Generates baseline classification, regression and forecasting models through a UI or Python API, and produces editable notebooks for each trial.
* [Databricks Feature Store](databricks-feature-store.md) - A feature registry in Unity Catalog that stores features in primary-keyed Delta tables, with point-in-time training set creation, automatic lookup at inference and lineage to models.
* [Databricks Feature Views](databricks-feature-views.md) - Declarative feature definitions, including time-windowed aggregations over batch, streaming and request-time data, for which Databricks builds and runs the pipelines.
* [Databricks Online Feature Store](databricks-online-feature-store.md) - A Lakebase-backed store that publishes feature tables for millisecond lookups by Model Serving endpoints and feature serving endpoints.
* [Managed MLflow on Databricks](databricks-managed-mlflow.md) - MLflow 3 hosted by Databricks, with experiment and run tracking, logged models, prompt management and deployment jobs, all integrated with Unity Catalog permissions and lineage.
* [Models in Unity Catalog](databricks-models-in-unity-catalog.md) - The MLflow model registry hosted in Unity Catalog, with versions, aliases, permissions, tags and lineage to training data and features shared across workspaces.

# ML operations

* [Databricks inference tables](databricks-inference-tables.md) - Logs requests and responses from serving endpoints, foundation model calls and agents to Unity Catalog Delta tables for monitoring, audit and retraining.
* [Databricks Model Serving](databricks-model-serving.md) - Serverless CPU and GPU endpoints for serving custom MLflow models, Databricks-hosted foundation models and external models in real time, with traffic splitting between model versions.

# Generative AI

* [Agent Bricks](databricks-agent-bricks.md) - Databricks' platform for developing agents. It brings together agent hosting, sandboxed code execution, memory, MCP tools, retrieval, tracing, evaluation and governed model access.
* [Agent Bricks Knowledge Assistant and Supervisor Agent](databricks-knowledge-assistant-supervisor-agent.md) (deprecated) - No-code agents. Knowledge Assistant answers questions over documents with citations, and Supervisor Agent coordinates Genie Agents, tables, AI Search indexes, MCP servers and other agents.
* [Databricks Agent Evaluation (MLflow GenAI evaluation)](databricks-agent-evaluation.md) - Evaluates agents and LLM applications against datasets, using built-in and custom scorers, LLM judges and human feedback, and also monitors production traces.
* [Databricks Agent Runtime and Agent Bricks CLI](databricks-agent-runtime.md) (preview) - Serverless hosting for code-based agents on Databricks Apps, with durable run state, an authenticated endpoint, a service-principal identity and MLflow tracing, deployed with the agentbricks CLI.
* [Databricks AI Search](databricks-ai-search.md) - A managed vector and full-text search service. Delta Sync indexes stay in step with source tables and can compute embeddings, and hybrid retrieval is supported.
* [Databricks Foundation Model APIs](databricks-foundation-model-apis.md) - Databricks-hosted proprietary and open language and embedding models, available pay-per-token or with provisioned throughput. They are exposed as governed model services in the system.ai schema.
* [Databricks managed MCP servers](databricks-managed-mcp-servers.md) (preview) - Hosted Model Context Protocol servers that expose Unity Catalog functions, AI Search indexes, Genie Agents and Genie One to agents as tools. External MCP servers can also be registered as Unity Catalog MCP services.
* [MLflow Tracing on Databricks](databricks-mlflow-tracing.md) - Records each step of agent and LLM calls, including inputs, outputs, latency, tokens and feedback, and stores the traces in Unity Catalog tables that can be queried with SQL.
* [Unity Gateway](databricks-unity-gateway.md) - A governance and routing layer in Unity Catalog for model, MCP and agent traffic, with provider fallbacks, rate and consumption limits, guardrails, inference logging and budgets.

# Metadata and discovery

* [Databricks Catalog Explorer](databricks-catalog-explorer.md) - The workspace UI for browsing and managing Unity Catalog assets. It shows schemas, permissions, lineage, popularity, table health indicators and AI-generated comments.
* [Databricks Discover](databricks-discover.md) - A curated browsing page that groups governed tables, dashboards, notebooks and Genie Agents into business domains and subdomains, with highlighted assets chosen by admins and AI recommendations.
* [Unity Catalog data lineage](databricks-unity-catalog-lineage.md) - Captures table- and column-level lineage automatically for queries, notebooks, jobs, pipelines, dashboards and models. External sources and BI tools can be registered so they appear in the same graph.

# Data quality and observability

* [Databricks data profiling](databricks-data-profiling.md) - Computes profile and drift metrics for a table over time as snapshot, time-series or inference profiles, and stores them in Delta tables with a generated dashboard.
* [Databricks data quality monitoring anomaly detection](databricks-dqm-anomaly-detection.md) (preview) - Monitors every table in a schema with one setting. It learns each table's update and volume patterns, flags late or incomplete tables, and suggests root causes using lineage.
* [Lakeflow pipelines expectations](databricks-pipeline-expectations.md) - Declarative data quality constraints on pipeline datasets. For each failing record you choose to warn, drop it or fail the update, and the results are recorded in the pipeline event log.

# Governance and compliance

* [Databricks compliance security profile](databricks-compliance-security-profile.md) - A workspace setting that applies a hardened, FIPS-validated compute image, enhanced security monitoring and encrypted egress, required for HIPAA, PCI-DSS, FedRAMP and similar regulated data.
* [Databricks Data Classification](databricks-data-classification.md) - A serverless agent that scans Unity Catalog tables incrementally, detects sensitive data such as PII and payment-card data, and tags the columns.
* [Databricks governed tags](databricks-governed-tags.md) - Account-level tag definitions with controlled values and assignment permissions, applied to Unity Catalog objects and workspace assets and used by ABAC, classification and cost reporting.

# Security and access

* [Databricks automatic identity management](databricks-automatic-identity-management.md) - Synchronises users, groups and service principals from Microsoft Entra ID or Okta on demand, without configuring SCIM provisioning. It works alongside SSO, OAuth and service principals.
* [Databricks customer-managed keys](databricks-customer-managed-keys.md) - Customer-held cloud KMS keys that encrypt control-plane data (notebooks, secrets, queries), workspace storage and, at catalogue level, Unity Catalog managed data.
* [Databricks Governance Hub](databricks-governance-hub.md) (preview) - An account-level console that brings together data health and governance coverage, tag usage, AI usage and spend, and cost drivers, with recommended actions.
* [Databricks serverless egress control](databricks-serverless-egress-control.md) - Account-level network policies that limit which destinations serverless compute, apps and model serving can reach, used with network connectivity configurations and private endpoint rules.
* [Lakeguard](databricks-lakeguard.md) - Isolation technology that sandboxes each user's code and UDFs away from the Spark engine and from other users, so shared compute can enforce Unity Catalog row filters and column masks.
* [Private Link for Databricks](databricks-private-link.md) - AWS PrivateLink, Azure Private Link and Private Service Connect connectivity for front-end access, classic compute to the control plane, and inbound access to serverless services such as Lakebase and Zerobus Ingest.
* [Secrets in Unity Catalog](databricks-secrets-in-unity-catalog.md) - Credentials stored as governed Unity Catalog securables under a catalog.schema.secret name, with grants and audit.
* [Unity Catalog attribute-based access control (ABAC)](databricks-abac.md) - Policies attached at catalogue, schema or table level that use governed tags and user attributes to apply row filters, column masks and dynamic grants automatically.

# Data sharing and collaboration

* [Databricks Clean Rooms](databricks-clean-rooms.md) - Isolated serverless environments where up to ten organisations share data through OpenSharing and run notebooks that every party has approved. No party sees the others' underlying data.
* [Databricks Marketplace](databricks-marketplace.md) - An exchange for publishing and finding datasets, AI models, notebooks, apps and MCP servers, either publicly or through private exchanges, delivered with OpenSharing.
* [Databricks OpenSharing](databricks-opensharing.md) - Live sharing of tables, views, materialised views, metric views, volumes, models and notebooks with other Databricks accounts, or tabular data with any client through an open protocol, without copying.

# Development and DataOps

* [Databricks Apps](databricks-apps.md) - Serverless hosting for Python and Node.js web applications (for example Streamlit, Dash, Gradio and React) that run inside the workspace with Unity Catalog, SQL warehouse and OAuth integration.
* [Databricks Connect](databricks-connect.md) - A client library built on Spark Connect. Python, Scala and R DataFrame code written in an IDE or application runs on remote Databricks compute, including serverless.
* [Databricks Declarative Automation Bundles](databricks-declarative-automation-bundles.md) - A Databricks CLI feature that defines jobs, pipelines, dashboards, apps, serving endpoints, AI Search, Lakebase and other resources in YAML with per-target settings. The CLI then validates, plans and deploys them from CI/CD.
* [Databricks Git folders](databricks-git-folders.md) - Workspace folders backed by a Git repository. Users clone, branch, commit, merge and resolve conflicts from the UI, the API or Git CLI commands.
* [Databricks notebooks](databricks-notebooks.md) - Collaborative notebooks with Python, SQL, Scala and R cells, comments, version history, widgets and visualisations that can be scheduled as jobs.
* [Genie Code](databricks-genie-code.md) - An AI coding and data agent in notebooks, the SQL editor, the pipelines editor, dashboards and MLflow. It plans, writes and runs code, fixes errors and builds pipelines and dashboards, using Unity Catalog context and the user's permissions.

# Platform operations

* [Databricks agentic code converter](databricks-agentic-code-converter.md) (preview) - A Genie Code-based migration project that converts T-SQL, Snowflake, Redshift, Oracle, BigQuery and Teradata SQL into Databricks SQL or DataFrame notebooks.
* [Databricks budgets](databricks-budgets.md) - Account-level spend tracking at list price, filtered by workspace, resource type and tags. You set monthly thresholds with email alerts and, for Unity Gateway, optional per-user blocking.
* [Databricks managed disaster recovery](databricks-managed-disaster-recovery.md) (preview) - Replicates Unity Catalog metadata, managed table data and workspace assets to a secondary region, behind a stable URL that survives failover.
* [Databricks serverless usage policies](databricks-serverless-usage-policies.md) (preview) - Sets of tags applied automatically to the serverless usage of the users assigned to a policy, so that spend from notebooks, jobs, pipelines, serving, apps and Lakebase can be attributed.
* [Databricks system tables](databricks-system-tables.md) - Databricks-hosted tables in the system catalog that cover billing, audit, lineage, compute, query history, jobs, pipelines, serving, MLflow, classification, data quality and Lakebase activity.
* [Databricks Terraform provider](databricks-terraform-provider.md) - A Terraform provider (databricks/databricks) that manages workspaces, Unity Catalog objects, permissions, compute, jobs and other Databricks resources as code.
* [Lakebridge](databricks-lakebridge.md) - A Databricks Labs migration toolkit. It assesses legacy warehouse and ETL estates, transpiles their SQL and ETL code to Databricks, and reconciles the migrated data against the source.

# Specialised data types

* [Databricks spatial SQL (GEOMETRY and GEOGRAPHY)](databricks-spatial-sql.md) - Native GEOMETRY and GEOGRAPHY types with ST_ functions for constructing, measuring, relating and transforming spatial data, plus H3 functions.
* [Unity Catalog volumes](databricks-volumes.md) - Governed, path-addressable storage for non-tabular files such as documents, images, libraries and landing data. Volumes can be managed or external.
