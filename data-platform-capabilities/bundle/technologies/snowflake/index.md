# Snowflake

# Ingestion and integration

* [Data mirroring for Snowflake Postgres](snowflake-postgres-data-mirroring.md) - Continuously replicates Postgres tables or whole schemas into Snowflake tables from the write-ahead log, with sub-minute lag and source transaction boundaries kept.
* [Snowflake bulk loading (COPY INTO <table>)](snowflake-copy-into.md) - Loads staged files in bulk into tables on a warehouse, tracking which files were loaded so they are not loaded twice.
* [Snowflake Connector for Kafka](snowflake-connector-for-kafka.md) - A Kafka Connect sink connector that loads topics into Snowflake tables using Snowpipe Streaming.
* [Snowflake external network access (external access integrations)](snowflake-external-access-integrations.md) - Lets UDFs, procedures and container services call approved external endpoints over the network, using network rules and secrets, for example to pull data from REST APIs.
* [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](snowflake-native-connectors.md) - Connectors packaged as Snowflake Native Apps that ingest and refresh data from SaaS applications and databases incrementally, some using a customer-run agent for change data capture.
* [Snowflake Openflow](snowflake-openflow.md) - A managed integration service, built on Apache NiFi, that runs prebuilt and custom connectors for databases, SaaS, streams and unstructured content in batch or streaming mode.
* [Snowpipe](snowflake-snowpipe.md) - A serverless pipe that loads files continuously from stages as they arrive, triggered by cloud storage event notifications or REST calls.
* [Snowpipe Streaming](snowflake-snowpipe-streaming.md) - Ingests rows directly into tables through SDKs (Java, Python, Node.js) or a REST API, with no files, making data queryable within seconds.

# Storage and table management

* [Apache Iceberg tables in Snowflake](snowflake-iceberg-tables.md) - Tables stored as Parquet files with Apache Iceberg metadata, managed either by Snowflake as catalogue or by an external catalogue, in customer storage or in Snowflake storage.
* [Snowflake catalog-linked databases](snowflake-catalog-linked-databases.md) - Databases linked to an external Iceberg REST catalogue (for example AWS Glue, Unity Catalog, Open Catalog, BigLake or S3 Tables) that discover and sync remote namespaces and tables automatically for querying and writing.
* [Snowflake clustering keys and Automatic Clustering](snowflake-clustering-keys.md) - Lets you declare clustering columns on large tables, then reorganises micro-partitions in the background to keep them well clustered so pruning stays effective.
* [Snowflake micro-partitioned table storage](snowflake-managed-storage.md) - Stores standard tables in immutable, compressed, columnar micro-partitions with per-partition statistics that Snowflake manages, giving ACID transactions and partition pruning.
* [Snowflake Open Catalog](snowflake-open-catalog.md) (deprecated) - A separate managed Apache Polaris service that acts as an Iceberg REST catalogue with central access control for Iceberg tables shared across engines.
* [Snowflake semi-structured data types (VARIANT, OBJECT, ARRAY)](snowflake-semi-structured-data.md) - Stores JSON, Avro, ORC, Parquet and XML in VARIANT, OBJECT and ARRAY columns, extracting columns for pruning, and queries them with path notation and FLATTEN.
* [Snowflake stages and directory tables](snowflake-stages-directory-tables.md) - Internal and external stages hold files in object storage, and directory tables catalogue the staged files with metadata so unstructured content can be listed, governed and processed with SQL.
* [Snowflake storage lifecycle policies](snowflake-storage-lifecycle-policies.md) - Schema-level policies that archive table rows to cheaper COOL or COLD tiers, or delete them permanently, according to conditions such as age.
* [Snowflake Time Travel](snowflake-time-travel.md) - Queries, clones or undrops tables, schemas and databases as they were at an earlier point within a retention period of up to 90 days.
* [Snowflake zero-copy cloning](snowflake-zero-copy-cloning.md) - Creates instant writable copies of tables, schemas or databases that share micro-partitions with the source until either side changes.

# Processing and transformation

* [dbt Projects on Snowflake](snowflake-dbt-projects.md) - Deploys, runs, schedules and monitors dbt projects as Snowflake objects on a dbt Core or dbt Fusion runtime that Snowflake manages, developed in Workspaces or from Git.
* [pandas on Snowflake](snowflake-pandas-on-snowflake.md) - A Modin-based pandas API that turns pandas operations on Snowflake data into SQL, and chooses per operation whether to run them locally or in Snowflake (hybrid execution).
* [Snowflake Cortex AI Functions](snowflake-cortex-ai-functions.md) - SQL functions such as AI_COMPLETE, AI_CLASSIFY, AI_FILTER, AI_AGG, AI_SUMMARIZE_AGG, AI_EMBED, AI_SENTIMENT, AI_TRANSLATE, AI_TRANSCRIBE and AI_REDACT that apply hosted models to columns and files.
* [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](snowflake-cortex-document-functions.md) - AI_PARSE_DOCUMENT turns PDFs and images into text and layout, and AI_EXTRACT pulls named fields, tables and entities out of documents.
* [Snowflake Dynamic Tables](snowflake-dynamic-tables.md) - Tables defined by a query and a target lag that Snowflake keeps refreshed, incrementally where possible, working out dependency order across chains of dynamic tables.
* [Snowflake user-defined functions and stored procedures](snowflake-udfs-and-procedures.md) - Custom scalar, table and aggregate functions and stored procedures written in SQL, Snowflake Scripting, JavaScript, Python, Java or Scala that run inside Snowflake.
* [Snowpark](snowflake-snowpark.md) - DataFrame and function APIs for Python, Java and Scala that push processing down into Snowflake warehouses as SQL, plus runtimes for running that code in the engine.
* [Snowpark Connect for Apache Spark](snowflake-snowpark-connect-for-spark.md) - Runs existing Spark DataFrame and Spark SQL code on Snowflake compute through the Spark Connect protocol, so there is no Spark cluster to manage.

# Orchestration

* [Snowflake tasks and task graphs](snowflake-tasks.md) - Run SQL, procedures or code on a schedule, in dependency graphs, or when a stream has new data, on serverless or user-managed compute.

# Query and compute

* [pg_lake](snowflake-pg-lake.md) (preview) - An open-source Postgres extension from Snowflake that reads and writes Iceberg tables and Parquet files in object storage from Postgres.
* [Snowflake Adaptive Compute](snowflake-adaptive-compute.md) - A warehouse type (adaptive warehouses) for which Snowflake decides the resources for each query, so you do not set a size, multi-cluster settings or suspend policies.
* [Snowflake external tables](snowflake-external-tables.md) - Read-only tables over files in external stages, with optional automatic metadata refresh, so data in a lake can be queried without loading it.
* [Snowflake generation 2 standard warehouses](snowflake-gen2-warehouses.md) - The newer generation of standard warehouses, running on faster hardware with optimisations for DELETE, UPDATE, MERGE and table scans.
* [Snowflake Horizon Iceberg REST Catalog API](snowflake-horizon-iceberg-rest-catalog.md) - An Apache Polaris-based Iceberg REST catalogue endpoint in each account that lets Spark, Trino, Flink, DuckDB, PyIceberg and other engines read and write Snowflake-managed Iceberg tables under Snowflake RBAC.
* [Snowflake interactive tables and interactive warehouses](snowflake-interactive-tables.md) - A table type and a matching warehouse type built for sub-second, highly concurrent queries such as user-facing dashboards and data APIs.
* [Snowflake materialized views](snowflake-materialized-views.md) - Stores the results of a single-table query and keeps them up to date automatically in the background, so queries read precomputed results.
* [Snowflake multi-cluster warehouses](snowflake-multi-cluster-warehouses.md) - Adds and removes clusters of the same size automatically, according to a scaling policy, to absorb bursts of concurrent queries without queuing.
* [Snowflake persisted query results (result cache)](snowflake-result-cache.md) - Returns the stored result of an identical earlier query, for 24 hours and up to 31 days with reuse, when the underlying data has not changed, without using warehouse compute.
* [Snowflake Query Acceleration Service](snowflake-query-acceleration-service.md) - Offloads parts of large scans and filters in eligible queries to shared serverless compute, so outlier queries finish faster without enlarging the warehouse.
* [Snowflake Search Optimization Service](snowflake-search-optimization-service.md) - Builds and maintains a persistent search access path on chosen tables and columns, so point lookups, substring, semi-structured, geospatial and full-text SEARCH queries skip most micro-partitions.
* [Snowflake virtual warehouses](snowflake-virtual-warehouses.md) - Named clusters of compute, sized from X-Small to 6X-Large, that run SQL and Snowpark workloads against shared storage and suspend and resume automatically.
* [Snowpark Container Services](snowflake-snowpark-container-services.md) - Runs OCI container images as long-running services or finite jobs on Snowflake-managed compute pools, including GPU nodes, inside the account's security boundary.
* [Snowpark-optimized warehouses](snowflake-snowpark-optimized-warehouses.md) - Warehouses with much more memory per node, and configurable CPU architecture, for memory-intensive Snowpark, UDF and single-node ML training work.

# Serving and activation

* [Snowflake data unloading (COPY INTO <location>)](snowflake-unload.md) - Writes query results or tables to files in internal or external stages as CSV, JSON or Parquet, optionally partitioned.
* [Snowflake drivers, connectors and SQL API](snowflake-drivers-sql-api.md) - JDBC, ODBC, Python, Go, .NET and Node.js drivers, the Spark connector and a REST SQL API for connecting tools and applications to Snowflake.
* [Snowflake hybrid tables (Unistore)](snowflake-hybrid-tables.md) - A row-oriented table type with enforced primary, unique and foreign keys, indexes and row locking, for low-latency point reads and writes in the same engine as analytical tables.
* [Snowflake Postgres](snowflake-postgres.md) - Fully managed PostgreSQL instances, on versions 16 to 18, created and governed from Snowflake, running on dedicated Snowflake-managed machines with PgBouncer pooling and private networking.
* [Snowflake streams](snowflake-streams.md) - Track inserts, updates and deletes on tables, views and other objects since an offset, so downstream jobs process only the changes.

# Analytics and BI

* [Snowflake alerts and notifications](snowflake-alerts.md) - Scheduled or event-driven conditions written in SQL that run an action, such as sending email, webhook or cloud-queue notifications, when data meets them.
* [Snowflake Cortex Analyst](snowflake-cortex-analyst.md) - Turns natural-language questions into SQL over semantic views and returns the answers, through a REST API or as an agent tool.
* [Snowflake CoWork](snowflake-cowork.md) - A conversational agent application for business users that answers questions over structured and unstructured data, runs deep research, and produces artefacts, documents and scheduled automations.
* [Snowflake Horizon Context](snowflake-horizon-context.md) (preview) - A layer of Horizon Catalog that gathers external metadata and lineage, enriches it with semantics, popularity and AI descriptions, and exposes it to agents and BI tools through search and MCP.
* [Snowflake semantic views](snowflake-semantic-views.md) - Schema-level objects that define logical tables, relationships, facts, dimensions and metrics, queried with SQL and used by Cortex Analyst, agents and BI tools.
* [Snowsight dashboards](snowflake-snowsight-dashboards.md) - Simple dashboards built from charts and tables of query results in Snowsight, shared with other Snowflake users.
* [Snowsight Workspaces](snowflake-workspaces.md) - A file-based editor in Snowsight for SQL, Python, notebooks, dbt projects, Streamlit apps and semantic views, with Git integration, sharing and AI code suggestions.

# Machine learning development

* [Snowflake Container Runtime for ML](snowflake-container-runtime.md) - A prebuilt CPU and GPU ML environment on Snowpark Container Services, with distributed data loading, training and hyperparameter tuning built on Ray.
* [Snowflake Feature Store](snowflake-feature-store.md) - Python APIs and objects for defining entities and feature views (as Dynamic Tables or views), generating point-in-time correct training sets and retrieving features for batch inference.
* [Snowflake ML Experiments](snowflake-ml-experiments.md) - Records runs with parameters, metrics, artefacts and logs inside experiments, with autologging for common libraries and side-by-side comparison in Snowsight.
* [Snowflake ML Functions](snowflake-ml-functions.md) - SQL-callable model classes for time-series forecasting, anomaly detection, classification and top insights, which train and run without ML code.
* [Snowflake ML Jobs](snowflake-ml-jobs.md) - Submits Python functions, files or code bundles from any IDE or from SQL to run as jobs on Container Runtime compute pools, including on multiple nodes.
* [Snowflake Model Registry](snowflake-model-registry.md) - Stores versioned models trained in Snowflake or elsewhere as schema-level objects with metadata, metrics and aliases, and runs their methods from SQL or Python for batch inference.
* [Snowflake Online Feature Store](snowflake-online-feature-store.md) (preview) - Syncs feature views to a low-latency online store and serves them by key through a REST API, with stream and real-time feature views for sub-minute freshness.

# ML operations

* [Snowflake ML Observability (model monitors)](snowflake-ml-observability.md) - Model monitor objects that compute drift, performance and statistical metrics from logged inference data, with dashboards and threshold alerts.
* [Snowflake Model Serving in Snowpark Container Services](snowflake-model-serving.md) - Deploys registry models as autoscaling CPU or GPU inference services with HTTP endpoints, with gateway-based traffic splitting for shadow and canary releases.

# Generative AI

* [Snowflake AI Observability](snowflake-ai-observability.md) - Tracing, cost tracking and batch evaluation for agents, Cortex Search, CoCo and custom TruLens-instrumented apps, stored in an account event table and viewed in Snowsight.
* [Snowflake Cortex Agents](snowflake-cortex-agents.md) - Schema-level agent objects that plan, call tools such as Cortex Analyst, Cortex Search, custom procedures, sandboxed Python code execution and web search, and answer with governed data.
* [Snowflake Cortex AI Function Studio](snowflake-cortex-ai-function-studio.md) (preview) - A Snowsight workspace for designing prompts for Cortex AI Functions, evaluating them against labelled data and optimising them.
* [Snowflake Cortex AI Gateway](snowflake-cortex-ai-gateway.md) (preview) - A single governed endpoint for AI clients that routes model calls, records traces and token use, and attributes spend to teams and users under budgets and quotas.
* [Snowflake Cortex AI Guardrails](snowflake-cortex-ai-guardrails.md) - Runtime checks that detect prompt injection and jailbreak attempts, including indirect injection in tool outputs, for Cortex Agents, CoWork and CoCo.
* [Snowflake Cortex Fine-tuning](snowflake-cortex-fine-tuning.md) - Builds parameter-efficient fine-tuned adaptors for supported base models from training data in Snowflake, for inference through AI_COMPLETE.
* [Snowflake Cortex Knowledge Extensions](snowflake-cortex-knowledge-extensions.md) - Cortex Search services shared as Marketplace or private listings, so a consumer's agents and RAG apps can search a provider's content, with citations.
* [Snowflake Cortex REST API](snowflake-cortex-rest-api.md) - REST endpoints, including chat-completions-style APIs, that give applications access to the large language models hosted in Snowflake's security boundary.
* [Snowflake Cortex Search](snowflake-cortex-search.md) - A managed hybrid vector and keyword search service, with reranking, that embeds, indexes and refreshes text from a query or stage on a target lag.
* [Snowflake-managed MCP server](snowflake-managed-mcp-server.md) - A Snowflake object that exposes Cortex Agents, Cortex Analyst, Cortex Search, SQL execution and custom functions as Model Context Protocol tools to external AI clients under RBAC.

# Metadata and discovery

* [Snowflake AI-generated descriptions](snowflake-cortex-descriptions.md) - Uses Cortex models to draft descriptions of tables, views and columns in Snowsight for owners to review and save as comments.
* [Snowflake data lineage (Snowsight lineage)](snowflake-data-lineage.md) - Records table and column lineage from DML, CTAS and view dependencies, plus ML lineage across datasets, feature views, models and monitors, shown as a graph in Catalog Explorer.
* [Snowflake external lineage](snowflake-external-lineage.md) - Accepts OpenLineage COMPLETE events through a REST endpoint, so tools such as dbt and Airflow can add lineage from outside Snowflake to the lineage graph.
* [Snowflake Horizon Catalog](snowflake-horizon-catalog.md) - Snowflake's built-in catalogue and governance layer, covering object discovery, tagging, policies, quality, lineage, access history and Iceberg catalogue services for Snowflake and external data.
* [Snowflake Universal Search](snowflake-universal-search.md) - Searches object metadata across the account, the Snowflake Marketplace and the Internal Marketplace in Snowsight, in natural language, filtered by the user's privileges.

# Data quality and observability

* [Snowflake data quality monitoring (data metric functions)](snowflake-data-quality-monitoring.md) - Schedules system and custom data metric functions on tables and views, compares results with expectations, and detects volume and freshness anomalies, with results in Snowsight.

# Governance and compliance

* [Snowflake aggregation policies](snowflake-aggregation-policies.md) - Require queries on a protected table to aggregate rows into groups above a minimum size, at row or entity level, so individual records cannot be returned.
* [Snowflake differential privacy](snowflake-differential-privacy.md) - Privacy policies that add calibrated noise to aggregate results on protected tables and track each analyst's cumulative privacy loss against a budget.
* [Snowflake Intent-Driven Governance](snowflake-intent-driven-governance.md) (preview) - A review-first CoCo workflow that turns a governance goal stated in plain language into a scope, a governance specification and SQL for tags and protections, which a person approves before it runs.
* [Snowflake object tagging](snowflake-object-tagging.md) - Schema-level tags with allowed values that are attached to objects and columns, inherited down the hierarchy, and used for classification, cost attribution and tag-based policies.
* [Snowflake projection policies](snowflake-projection-policies.md) - Stop a column from being returned in query output while still allowing it in joins, filters and aggregations.
* [Snowflake sensitive data classification](snowflake-sensitive-data-classification.md) - Scans tables in databases with a classification profile, assigns semantic and privacy categories to sensitive columns, and can map them to your own tags automatically.

# Security and access

* [Snowflake access control (RBAC and database roles)](snowflake-access-control.md) - A hierarchy of account roles, database roles and application roles that hold privileges on securable objects, with secondary roles and managed access schemas.
* [Snowflake Access History](snowflake-access-history.md) - An ACCOUNT_USAGE view that records which columns each query read and which objects it wrote, including through views and policies.
* [Snowflake authentication (SSO, OAuth, key pair, PATs, workload identity federation)](snowflake-authentication.md) - Authenticates users and services through SAML SSO, Snowflake or external OAuth, key pairs, programmatic access tokens, MFA and workload identity federation with cloud identities.
* [Snowflake masking policies](snowflake-masking-policies.md) - Schema-level policies that mask, tokenise or reveal column values at query time depending on role, other context or tags, including external tokenisation through external functions.
* [Snowflake network policies and network rules](snowflake-network-policies.md) - Restrict which IP ranges, VPC endpoints or private endpoints can reach an account or user, and which external destinations workloads can reach.
* [Snowflake private connectivity (AWS PrivateLink, Azure Private Link, Google Cloud Private Service Connect)](snowflake-private-connectivity.md) - Connects clients, internal stages and Snowflake-hosted endpoints to Snowflake over the cloud provider's private network rather than the public internet.
* [Snowflake row access policies](snowflake-row-access-policies.md) - Schema-level policies that decide, using the querying role and mapping tables, which rows of a table or view a query returns.
* [Snowflake secrets](snowflake-secrets.md) - Schema-level secret objects that hold credentials, OAuth tokens and keys for integrations, UDFs, Openflow and container services, so code does not contain them.
* [Snowflake Tri-Secret Secure](snowflake-tri-secret-secure.md) - Combines a Snowflake-maintained key with a customer-managed key in the cloud provider's KMS to create the composite master key for account data, so revoking the customer key makes data unreadable.
* [Snowflake Trust Center](snowflake-trust-center.md) - Runs scanner packages (Security Essentials, CIS Benchmarks, Threat Intelligence, AI Security) against accounts and reports violations, detections and at-risk entities.

# Data sharing and collaboration

* [Snowflake Data Clean Rooms](snowflake-data-clean-rooms.md) - Collaborations defined in YAML, in which owners, data providers and analysis runners combine data through approved templates without exposing raw rows to one another.
* [Snowflake Internal Marketplace (organisational listings)](snowflake-internal-marketplace.md) - A private marketplace inside a Snowflake organisation where teams publish organisational listings as data products for discovery and access requests by other accounts.
* [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](snowflake-listings.md) - Package a share, app or service with descriptive metadata as a data product for chosen accounts, replicating it automatically to consumers in other regions and clouds.
* [Snowflake Marketplace](snowflake-marketplace.md) - A public catalogue where providers publish free, paid or trial listings of data, Native Apps, Cortex Knowledge Extensions and agents, and consumers subscribe to them.
* [Snowflake Open Data Sharing](snowflake-open-data-sharing.md) (preview) - Shares Iceberg tables as live, read-only data with external consumers outside Snowflake, who read them through standard Iceberg REST Catalog APIs using a programmatic access token.
* [Snowflake Secure Data Sharing](snowflake-secure-data-sharing.md) - Shares live, read-only database objects with other Snowflake accounts through shares, without copying data, with consumers paying for their own compute.

# Development and DataOps

* [Snowflake CLI](snowflake-cli.md) - An open-source command-line tool for running SQL and for building, testing and deploying Snowflake apps, Snowpark code, Streamlit apps, dbt and DCM projects from local machines and CI pipelines.
* [Snowflake CoCo](snowflake-coco.md) - An AI coding agent, available in Snowsight, as a CLI, as a desktop app and in VS Code, that uses Snowflake skills and MCP tools to explore data, write SQL, and build pipelines, dbt projects and apps.
* [Snowflake Copilot](snowflake-copilot.md) (deprecated) - An SQL assistant in Snowsight that generates and explains queries from natural language.
* [Snowflake DCM Projects](snowflake-dcm-projects.md) - Database Change Management projects that declare the desired state of databases, schemas, tables, dynamic tables, views, warehouses, roles, grants and data quality checks in SQL DEFINE files, then plan and deploy the changes.
* [Snowflake Extension for Visual Studio Code](snowflake-vscode-extension.md) (preview) - An IDE extension for connecting to Snowflake, running SQL and Snowpark code, and using CoCo from a local editor.
* [Snowflake Git integration (Git repository objects)](snowflake-git-integration.md) - Syncs remote Git repositories into Snowflake as repository clones, so code can be run with EXECUTE IMMEDIATE FROM and Workspaces, notebooks and Streamlit apps can commit and push.
* [Snowflake Native App Framework](snowflake-native-app-framework.md) - Packages data, code, Streamlit UIs, containers, agents and MCP servers as applications that consumers install and run in their own accounts through listings.
* [Snowflake Notebooks in Workspaces](snowflake-notebooks.md) - Jupyter-compatible notebooks in Snowsight Workspaces that run on Container Runtime CPU or GPU compute, with Git integration, a terminal and scheduling.
* [Snowflake synthetic data generation](snowflake-synthetic-data.md) - The GENERATE_SYNTHETIC_DATA procedure creates statistically similar tables, with the same column names and types, from up to five source tables without linking output rows to real records.
* [Streamlit in Snowflake](snowflake-streamlit.md) - Hosts Streamlit Python apps as Snowflake objects, on warehouse or container runtimes, with access governed by Snowflake roles.

# Platform operations

* [SnowConvert AI](snowflake-snowconvert-ai.md) - A migration tool that assesses and converts SQL code and objects from Teradata, Oracle, SQL Server, Redshift, Synapse, BigQuery, Databricks SQL and other platforms to Snowflake.
* [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](snowflake-account-usage.md) - Shared SNOWFLAKE database schemas that expose query, login, metering, storage, access, task, AI and billing history as views, for one account or the whole organisation.
* [Snowflake backups](snowflake-backups.md) - Point-in-time, zero-copy backups of tables, schemas and databases, managed through backup sets and backup policies, with optional retention locks and legal holds.
* [Snowflake budgets](snowflake-budgets.md) - Monthly credit limits for the account or for custom groups of objects (including by tag) that forecast spend, send notifications and can run stored procedures, for example to suspend warehouses.
* [Snowflake cost anomaly detection](snowflake-cost-anomaly-detection.md) - Flags days when account or organisation consumption falls outside the expected range, with optional anomaly monitors scoped by tags or service types.
* [Snowflake Fail-safe](snowflake-fail-safe.md) - Keeps a further non-configurable 7 days of historical data for permanent tables after Time Travel ends, recoverable only by Snowflake Support after a disaster.
* [Snowflake organisations](snowflake-organizations.md) - Group multiple Snowflake accounts across regions and clouds under one organisation for account creation, organisation-wide usage views, organisation users and organisational listings.
* [Snowflake Query History, Query Profile and query insights](snowflake-query-profile.md) - Snowsight views of query history, operator-level execution plans and automatic insights, used to diagnose slow or expensive queries.
* [Snowflake replication and failover groups](snowflake-replication-failover.md) - Replicate databases, users, roles, warehouses, policies and integrations to accounts in other regions or clouds, with promotion on failover and client redirect through connection objects.
* [Snowflake resource monitors](snowflake-resource-monitors.md) - Credit quotas on warehouses or the whole account that notify or suspend warehouses when thresholds are reached.
* [Snowflake Terraform provider](snowflake-terraform-provider.md) - A Terraform provider for managing Snowflake accounts, warehouses, databases, roles, grants and policies as code.
* [Snowflake Trail (event tables, logging, tracing and metrics)](snowflake-trail.md) - Collects logs, OpenTelemetry-style traces and metrics from UDFs, procedures, Snowpark, Native Apps, container services and pipelines into event tables, with Snowsight dashboards.
* [Virtual Private Snowflake (VPS)](snowflake-virtual-private-snowflake.md) - The highest Snowflake edition, which runs a dedicated, isolated Snowflake deployment for a single customer, with its own metadata store and compute.

# Specialised data types

* [Observe by Snowflake](snowflake-observe.md) - An observability platform for logs, metrics and traces, built on a Snowflake lakehouse and available standalone or paid for with Snowflake credits.
* [Snowflake geospatial data types and functions](snowflake-geospatial.md) - GEOGRAPHY and GEOMETRY types with spatial functions, H3 indexing and spatial joins in SQL.
* [Snowflake time-series functions (ASOF JOIN, TIME_SLICE, RESAMPLE)](snowflake-time-series-functions.md) - SQL constructs for aligning, bucketing and joining time-stamped data, including ASOF JOIN and gap filling.
