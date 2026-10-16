# Google Cloud

# Ingestion and integration

* [BigQuery change data capture](gcp-bigquery-cdc.md) - Applies streamed upserts and deletes, keyed on a declared primary key, to BigQuery tables in the background with a configurable staleness bound.
* [BigQuery Data Transfer Service](gcp-bigquery-data-transfer-service.md) - Scheduled, managed loads into BigQuery from Google marketing products, SaaS applications, other warehouses, databases and cloud object stores.
* [BigQuery Storage Write API](gcp-bigquery-storage-write-api.md) - High-throughput API for streaming or batch-committing rows into BigQuery tables with exactly-once semantics, readable within seconds.
* [Datastream](gcp-datastream.md) - Serverless change data capture and replication from MySQL, PostgreSQL, Oracle, SQL Server, Spanner, MongoDB and Salesforce into BigQuery, Lakehouse Iceberg tables or Cloud Storage.
* [Google Cloud Application Integration](gcp-application-integration.md) - Integration-platform-as-a-service for building API, event and process integrations visually, using Integration Connectors to reach SaaS and on-premises systems.
* [Google Cloud Database Migration Service](gcp-database-migration-service.md) - Migrates MySQL, PostgreSQL, SQL Server and Oracle databases to Cloud SQL and AlloyDB using an initial copy followed by continuous replication.
* [Google Cloud Managed Service for Apache Kafka](gcp-managed-kafka.md) - Runs Apache Kafka clusters, managed Kafka Connect clusters and a schema registry on Google Cloud, with Google handling brokers, scaling and patching.
* [Google Cloud Pub/Sub](gcp-pubsub.md) - Global publish-subscribe messaging service with push, pull and export subscriptions that write directly to BigQuery, Cloud Storage and Bigtable.
* [Google Cloud Storage Transfer Service](gcp-storage-transfer-service.md) - Managed, scheduled or event-driven copying of large object and file datasets from other clouds, HTTP sources and on-premises file systems into Cloud Storage.
* [Google Cloud Transfer Appliance](gcp-transfer-appliance.md) - Rentable, encrypted storage device shipped to a customer site to move hundreds of terabytes to petabytes into Cloud Storage offline.

# Storage and table management

* [BigQuery external tables and load jobs](gcp-bigquery-external-tables.md) - Reads or loads Parquet, ORC, Avro, JSON and CSV files from Cloud Storage, including Hive-partitioned layouts, as queryable external tables or native tables.
* [BigQuery managed storage](gcp-bigquery-managed-storage.md) - Internal columnar storage for native BigQuery tables, with automatic compression, replication, partitioning, clustering and transactional writes.
* [BigQuery table clones](gcp-bigquery-table-clones.md) - Writable copies of a table that share storage with the base table and are billed only for data that later changes in either.
* [BigQuery tables for Apache Iceberg](gcp-bigquery-iceberg-managed-tables.md) - BigQuery-managed tables stored as Apache Iceberg files in your Cloud Storage bucket, with BigQuery handling writes, clustering, compaction and garbage collection.
* [BigQuery time travel](gcp-bigquery-time-travel.md) - Lets you query or restore a table as it was at any point within a configurable window of two to seven days, backed by a further fail-safe period.
* [Dataproc Metastore](gcp-dataproc-metastore.md) - Fully managed Apache Hive metastore for Spark, Hive and Trino workloads on Google Cloud.
* [Google Cloud Lakehouse runtime catalog](gcp-lakehouse-runtime-catalog.md) - Serverless metastore that holds Iceberg table metadata for BigQuery and open-source engines and serves it through Apache Iceberg REST catalog and Hive endpoints with credential vending.
* [Google Cloud Storage](gcp-cloud-storage.md) - Object storage with regional, dual-region and multi-region buckets and Standard, Nearline, Coldline and Archive storage classes.
* [Google Cloud Storage Autoclass](gcp-cloud-storage-autoclass.md) - Moves each object between storage classes automatically according to how recently it was accessed, without retrieval or early-deletion fees.

# Processing and transformation

* [BigQuery continuous queries](gcp-bigquery-continuous-queries.md) - Long-running SQL statements that process rows as they arrive in a table and write results to BigQuery or Iceberg tables, Pub/Sub, Bigtable or Spanner.
* [BigQuery data preparation](gcp-bigquery-data-preparation.md) (preview) - Visual, Gemini-assisted editor for cleaning, joining and reshaping BigQuery data that saves its steps as runnable SQLX.
* [BigQuery DataFrames](gcp-bigquery-dataframes.md) - Python library (bigframes) offering pandas- and scikit-learn-style APIs that compile to BigQuery SQL so data stays in BigQuery.
* [BigQuery generative AI functions](gcp-bigquery-ai-functions.md) - SQL functions such as AI.GENERATE, AI.GENERATE_TABLE, AI.IF, AI.CLASSIFY, AI.SCORE, AI.AGG and AI.EMBED that call Gemini and partner models over table rows and unstructured objects.
* [BigQuery user-defined functions](gcp-bigquery-udfs.md) - Extends GoogleSQL with SQL, JavaScript and Python UDFs, remote functions on Cloud Run, stored procedures and stored procedures for Apache Spark.
* [Cloud Data Fusion](gcp-data-fusion.md) - Visual, plugin-based integration service built on open-source CDAP for designing batch and real-time pipelines that run on Managed Service for Apache Spark.
* [Dataflow templates](gcp-dataflow-templates.md) - Google-provided and custom Flex templates, plus the visual job builder, for running common ingestion and transformation pipelines without writing Beam code.
* [Dataform](gcp-dataform.md) - Develops, tests, version-controls and runs SQL transformation workflows in BigQuery, defined in SQLX with dependencies resolved automatically.
* [Google Cloud Dataflow](gcp-dataflow.md) - Serverless runner for Apache Beam batch and streaming pipelines with autoscaling, exactly-once processing and event-time windowing.
* [Google Cloud Document AI](gcp-document-ai.md) - Document processing service with OCR, form, layout and custom extraction and classification processors for PDFs and images.
* [Google Cloud Managed Service for Apache Spark on clusters](gcp-managed-spark-clusters.md) - Provisions and manages Spark, Hadoop, Hive, Flink and Trino clusters on Compute Engine that you size, configure and can access directly.
* [Google Cloud Managed Service for Apache Spark serverless](gcp-managed-spark-serverless.md) - Runs Spark batch jobs and interactive sessions without clusters, billed for execution time only.

# Orchestration

* [BigQuery pipelines](gcp-bigquery-pipelines.md) - Console-built, Dataform-backed pipelines that run SQL, notebook, data preparation and SQLX tasks in dependency order on a schedule.
* [Eventarc](gcp-eventarc.md) - Routes events from Google Cloud services, audit logs, Cloud Storage and Pub/Sub to Cloud Run, Workflows and other targets.
* [Google Cloud Managed Service for Apache Airflow](gcp-managed-airflow.md) - Managed Apache Airflow environments for scheduling and monitoring DAGs of data and ML tasks across Google Cloud and external systems.
* [Google Cloud Workflows](gcp-workflows.md) - Serverless orchestrator that runs YAML- or JSON-defined sequences of HTTP and Google Cloud API calls with retries, branching and waiting.

# Query and compute

* [BigQuery](gcp-bigquery.md) - Serverless analytical database that runs GoogleSQL over managed and open-format tables with storage and compute billed and scaled separately.
* [BigQuery BI Engine](gcp-bigquery-bi-engine.md) - In-memory cache in front of BigQuery that speeds up dashboard-style SQL queries, sized as a regional memory reservation.
* [BigQuery editions](gcp-bigquery-editions.md) - Slot-based capacity model in Standard, Enterprise and Enterprise Plus tiers, with autoscaling reservations, optional baseline slots and one- or three-year commitments.
* [BigQuery federated queries](gcp-bigquery-federated-queries.md) - Sends queries from BigQuery to Cloud SQL, AlloyDB, Spanner and SAP Datasphere through connections and joins the results with BigQuery data.
* [BigQuery materialized views](gcp-bigquery-materialized-views.md) - Precomputed query results that BigQuery refreshes incrementally and uses to rewrite matching queries automatically.
* [BigQuery Omni](gcp-bigquery-omni.md) - Runs BigQuery queries on data held in Amazon S3 or Azure Blob Storage, using BigQuery-managed compute in the corresponding AWS or Azure region.
* [BigQuery search indexes](gcp-bigquery-search-indexes.md) - Indexes text and JSON columns so the SEARCH function and equality or LIKE filters can find matching rows without full scans.
* [BigQuery workload management](gcp-bigquery-workload-management.md) - Reservations, assignments, idle-slot sharing, target concurrency, query queues and reservation groups that divide slot capacity between projects and workload types.
* [Cloud Run](gcp-cloud-run.md) - Serverless platform for running containers, functions and jobs that scale to zero, often used for data APIs, remote functions and data applications.
* [Cloud TPU](gcp-cloud-tpu.md) - Google's tensor processing unit accelerators, offered as VMs, slices and pods for training and serving large models.
* [Google Cloud Lakehouse](gcp-lakehouse.md) - Google Cloud's open lakehouse layer for Apache Iceberg and other formats on object storage, combining a shared catalogue, automatic table management and fine-grained security for BigQuery, Spark, Trino and Flink.

# Serving and activation

* [AlloyDB for PostgreSQL](gcp-alloydb.md) - PostgreSQL-compatible database with a disaggregated storage layer, columnar engine for analytical queries and built-in vector search and AI functions.
* [Apigee](gcp-apigee.md) - API management platform for publishing, securing, rate-limiting and monitoring APIs, including APIs that expose data products and LLM endpoints.
* [BigQuery change history (APPENDS and CHANGES)](gcp-bigquery-change-history.md) - Table-valued functions that return rows appended to, or changed in, a table over a time range so downstream jobs can process only the delta.
* [BigQuery EXPORT DATA](gcp-bigquery-export-data.md) - SQL statement that writes query results to Cloud Storage files or directly into Bigtable, Spanner, Pub/Sub and AlloyDB.
* [Bigtable](gcp-bigtable.md) - Wide-column NoSQL database for very high-throughput, low-latency reads and writes, often used for time series, events and feature serving.
* [Cloud SQL](gcp-cloud-sql.md) - Managed MySQL, PostgreSQL and SQL Server databases with automated backups, high availability and read replicas.
* [Firestore](gcp-firestore.md) - Serverless document database for web, mobile and server applications, with real-time listeners, vector search and an edition compatible with the MongoDB API.
* [Memorystore](gcp-memorystore.md) - Managed in-memory data stores (Memorystore for Valkey, Redis Cluster and Redis) for caching and sub-millisecond lookups.
* [Spanner](gcp-spanner.md) - Globally distributed relational database with strong consistency, horizontal scaling and up to 99.999% availability, plus graph, full-text and vector search.

# Analytics and BI

* [BigQuery conversational analytics](gcp-bigquery-conversational-analytics.md) - Natural-language question answering over BigQuery tables, views, graphs and Lakehouse tables through configurable data agents with instructions, glossary terms and verified queries.
* [BigQuery data canvas](gcp-bigquery-data-canvas.md) - Visual canvas in BigQuery where users chain search, SQL, chart and insight nodes, driven by natural-language prompts to Gemini.
* [BigQuery Studio](gcp-bigquery-studio.md) - Workspace in the BigQuery console that combines the SQL editor, Colab Enterprise notebooks, Spark sessions, data canvas and saved assets.
* [Connected Sheets](gcp-connected-sheets.md) - Lets Google Sheets users analyse BigQuery and Looker data with pivots, formulas and charts that run in the source rather than in the sheet.
* [Conversational Analytics in Looker](gcp-looker-conversational-analytics.md) - Gemini-based agents that answer natural-language questions over LookML Explores and dashboards, grounded in the semantic model.
* [Google Data Studio](gcp-data-studio.md) - Self-service reporting and dashboard tool with hundreds of connectors, free for individuals and sold as Data Studio Pro for organisations.
* [Looker](gcp-looker.md) - Enterprise BI platform with a governed semantic model, dashboards, scheduled delivery, alerts and embedding, querying the database directly.
* [LookML](gcp-lookml.md) - Looker's Git-backed modelling language for defining dimensions, measures, joins and access rules once for all queries.

# Machine learning development

* [Agent Platform AutoML](gcp-agent-platform-automl.md) - Trains tabular, image and video models from labelled data with automatic feature engineering, architecture search and tuning.
* [Agent Platform Feature Store](gcp-agent-platform-feature-store.md) - Feature management that uses BigQuery tables as the offline store and syncs selected features to online stores for low-latency serving.
* [Agent Platform Managed Training](gcp-agent-platform-managed-training.md) - Runs custom training jobs in prebuilt or custom containers on CPUs, GPUs or TPUs, including multi-node distributed training and hyperparameter tuning.
* [Agent Platform Model Evaluation](gcp-agent-platform-model-evaluation.md) - Computes evaluation metrics for registered models on test data, including data and model bias metrics, and, with Explainable AI, gives feature attributions for predictions.
* [Agent Platform Model Registry](gcp-agent-platform-model-registry.md) - Central registry for versioning custom, AutoML and BigQuery ML models, with aliases and deployment to endpoints or batch jobs.
* [Agent Platform Pipelines](gcp-agent-platform-pipelines.md) - Serverless execution of Kubeflow Pipelines and TFX workflows, with each run's artefacts and parameters recorded in ML Metadata.
* [BigQuery ML](gcp-bigquery-ml.md) - Creates, trains, evaluates and runs machine learning models with SQL inside BigQuery, including imported and remote models.
* [Data Labeling on Agent Platform](gcp-data-labeling.md) - Manages labelling of image, video, text and tabular datasets by human labellers for supervised training on Agent Platform.
* [Experiments on Agent Platform](gcp-agent-platform-experiments.md) - Tracks parameters, metrics and artefacts of training runs and pipeline runs so they can be compared, with a managed TensorBoard for visualisation.

# ML operations

* [Agent Platform Endpoints](gcp-agent-platform-endpoints.md) - Managed online prediction endpoints, plus batch prediction jobs, for serving registered models with autoscaling, GPUs and traffic splitting between model versions.
* [Dataflow ML](gcp-dataflow-ml.md) - Beam transforms such as RunInference and MLTransform that run model inference and feature preprocessing, including embeddings, inside batch and streaming Dataflow pipelines.
* [Model Monitoring on Agent Platform](gcp-model-monitoring.md) - Scheduled or on-demand monitoring jobs that compare production inputs and predictions with training data to detect drift and skew.

# Generative AI

* [Agent Platform RAG Engine](gcp-rag-engine.md) - Managed retrieval-augmented generation service that ingests, chunks and embeds documents into a corpus and retrieves context for Gemini calls.
* [Agent Platform Vector Search](gcp-vector-search.md) - Managed approximate nearest-neighbour index service based on ScaNN for low-latency similarity search over billions of vectors.
* [BigQuery vector search](gcp-bigquery-vector-search.md) - Stores embeddings in BigQuery tables and finds nearest neighbours with VECTOR_SEARCH and AI.SEARCH, optionally using IVF or TreeAH vector indexes.
* [Gemini Enterprise](gcp-gemini-enterprise.md) - Employee-facing agent platform that combines enterprise search over connected applications, prebuilt and custom agents and Gemini chat under company permissions.
* [Gemini Enterprise Agent Platform](gcp-gemini-enterprise-agent-platform.md) - Google Cloud's platform, formerly Vertex AI, for building, deploying and governing ML models, generative AI applications and agents.
* [Gemini models on Agent Platform](gcp-gemini-models.md) - Hosted access to Google's Gemini multimodal, embedding, image and speech models through Agent Platform APIs with pay-as-you-go, priority or provisioned throughput.
* [Gen AI evals on Agent Platform](gcp-gen-ai-evals.md) - Evaluates model and agent outputs with computed metrics, model-based judges and rubrics, offline, against simulated users or as online monitoring.
* [Google Agent Development Kit](gcp-agent-development-kit.md) - Open-source framework for writing single- and multi-agent applications with tools, memory and evaluation, deployable to Agent Runtime, Cloud Run or GKE.
* [Google Cloud Agent Gateway](gcp-agent-gateway.md) - Gateway that sits between agents, models and tools to enforce identity, policy, content screening and network controls on agent traffic.
* [Google Cloud Agent Observability](gcp-agent-observability.md) - Traces, logs, metrics and topology views of agent runs, tool calls and model calls on Agent Platform, built on Cloud Observability.
* [Google Cloud Agent Registry](gcp-agent-registry.md) - Inventory of the agents, tools and MCP servers in an organisation, used to register, discover and govern them.
* [Google Cloud Agent Runtime](gcp-agent-runtime.md) - Managed runtime for deploying and scaling agents built with ADK or other frameworks, with managed sessions and long-term memory.
* [Google Cloud Agent Search](gcp-agent-search.md) - Managed enterprise search and retrieval over websites, documents, structured data and connected applications, used to ground agents and chat applications.
* [Google Cloud Agent Studio](gcp-agent-studio.md) - Console workspace for designing and testing prompts and agents, comparing models and tuning Gemini models.
* [Google Cloud remote MCP servers](gcp-remote-mcp-servers.md) - Google-hosted Model Context Protocol endpoints that let AI agents query and manage BigQuery, Spanner, AlloyDB, Cloud SQL, Bigtable, Firestore, Knowledge Catalog, Dataform, Pub/Sub and other services under IAM.
* [MCP Toolbox for Databases](gcp-mcp-toolbox-for-databases.md) - Open-source MCP server for building parameterised, governed database tools for agents over BigQuery, AlloyDB, Spanner, Cloud SQL and third-party databases.
* [Model Armor](gcp-model-armor.md) - Screens prompts and responses for prompt injection, jailbreaks, harmful content, malicious URLs and sensitive data, for any model or agent.
* [Model Garden](gcp-model-garden.md) - Catalogue of Google, partner and open models that can be called as managed APIs or deployed to your own endpoints.

# Metadata and discovery

* [Google Cloud Data Catalog](gcp-data-catalog.md) (deprecated) - Google Cloud's earlier metadata catalogue for search and tagging of BigQuery, Pub/Sub and Cloud Storage assets.
* [Knowledge Catalog](gcp-knowledge-catalog.md) - Google Cloud's metadata catalogue for data and AI assets, providing automatic metadata ingestion, keyword and semantic search, aspects, a business glossary and metadata APIs.
* [Knowledge Catalog data insights](gcp-knowledge-catalog-data-insights.md) - Uses Gemini to draft table and column descriptions, suggested questions and SQL queries from metadata and profiles.
* [Knowledge Catalog data lineage](gcp-knowledge-catalog-data-lineage.md) - Records table- and column-level lineage automatically for BigQuery, Managed Service for Apache Spark, Managed Airflow and Dataflow, and accepts OpenLineage events from other systems.

# Data quality and observability

* [Knowledge Catalog data profiling](gcp-knowledge-catalog-data-profiling.md) - Profile scans that compute column statistics, distributions, null rates and top values for BigQuery tables.
* [Knowledge Catalog data quality](gcp-knowledge-catalog-data-quality.md) - Runs declarative or recommended data quality rules against BigQuery and Lakehouse tables as scheduled scans and publishes results and scores.

# Governance and compliance

* [Assured Workloads](gcp-assured-workloads.md) - Applies controls for data location, personnel access and supported services to folders so workloads meet regulatory regimes such as FedRAMP, CJIS and EU sovereignty requirements.
* [Google Cloud Sensitive Data Protection](gcp-sensitive-data-protection.md) - Discovers, classifies and de-identifies sensitive data across BigQuery, Cloud SQL, Cloud Storage and arbitrary content, and measures re-identification risk.

# Security and access

* [BigQuery data masking](gcp-bigquery-data-masking.md) - Masks column values at query time according to data policies, using rules such as hashing, nullifying, partial masking or custom masking routines.
* [BigQuery policy tags](gcp-bigquery-policy-tags.md) - Hierarchical taxonomies of tags attached to columns that drive column-level access control and data masking policies.
* [BigQuery row-level security](gcp-bigquery-row-level-security.md) - Row access policies that filter which rows of a table each user or group can see, using SQL filter expressions and optional lookup subqueries.
* [Google Cloud Identity and Access Management](gcp-iam.md) - Grants roles to users, groups and service accounts on organisation, folder, project and resource levels, with conditions, deny policies and identity federation.
* [Google Cloud Key Management Service](gcp-cloud-kms.md) - Creates and manages encryption keys, including hardware-backed and externally held keys, used as customer-managed encryption keys by Google Cloud services.
* [Google Cloud Logging](gcp-cloud-logging.md) - Collects, stores and routes logs, including Cloud Audit Logs of admin and data access, with Log Analytics for SQL queries over logs.
* [Google Cloud Secret Manager](gcp-secret-manager.md) - Stores, versions and rotates API keys, passwords and certificates for pipelines and applications under IAM.
* [Google Cloud Security Command Center](gcp-security-command-center.md) - Security and risk management service that finds misconfigurations, vulnerabilities and threats across Google Cloud, including where sensitive data is exposed.
* [VPC Service Controls](gcp-vpc-service-controls.md) - Defines security perimeters around Google Cloud projects and services so that data in services such as BigQuery and Cloud Storage cannot be copied outside them.

# Data sharing and collaboration

* [BigQuery data clean rooms](gcp-bigquery-data-clean-rooms.md) - Built on BigQuery sharing, lets several parties contribute data that others can query only through analysis rules or approved query templates.
* [BigQuery sharing](gcp-bigquery-sharing.md) - Data exchange service where publishers list datasets, views, models and Pub/Sub topics for subscribers, who get linked read-only copies without data duplication.

# Data products

* [Knowledge Catalog data products](gcp-knowledge-catalog-data-products.md) - Packages catalogued assets into data products with owners, documentation, contracts covering refresh and quality expectations, and access groups that consumers request to join.

# Development and DataOps

* [Agent Platform Workbench](gcp-agent-platform-workbench.md) - Managed JupyterLab instances with configurable CPUs, GPUs and Google Cloud integrations for data science and ML development.
* [BigQuery Data Engineering Agent](gcp-bigquery-data-engineering-agent.md) - Gemini agent in BigQuery pipelines and Dataform that writes or changes pipeline code (SQLX) from natural-language requests and investigates failed runs.
* [Colab Enterprise](gcp-colab-enterprise.md) - Managed Colab notebooks with shared runtimes and IAM, used both on Agent Platform and as the notebook engine inside BigQuery Studio.
* [Data Agent Kit](gcp-data-agent-kit.md) (preview) - IDE extension that connects coding agents and developers to Google Cloud data services through their remote MCP servers.
* [Gemini in BigQuery](gcp-gemini-in-bigquery.md) - Gemini assistance in BigQuery for generating, completing, explaining and fixing SQL and Python, and for generating dataset insights.
* [Google Cloud Build](gcp-cloud-build.md) - Serverless CI/CD service that builds, tests and deploys code and infrastructure in response to repository events.

# Platform operations

* [BigQuery INFORMATION_SCHEMA views](gcp-bigquery-information-schema.md) - System views exposing jobs, slot usage, reservations, storage, table metadata and replication state as queryable tables.
* [BigQuery managed disaster recovery](gcp-bigquery-managed-disaster-recovery.md) - Cross-region dataset replication paired with failover reservations so compute and storage can be switched to a secondary region in a hard or soft failover.
* [BigQuery Migration Service](gcp-bigquery-migration-service.md) - Tooling for moving warehouses to BigQuery, covering assessment, batch and interactive SQL translation, data transfer and validation.
* [BigQuery table snapshots](gcp-bigquery-table-snapshots.md) - Read-only, point-in-time copies of a table that store only the bytes that differ from the base table and can be kept beyond the time travel window.
* [Google Cloud Billing](gcp-cloud-billing.md) - Billing accounts, budgets and alerts, detailed billing export to BigQuery and FinOps reports for attributing and controlling Google Cloud spend.
* [Google Cloud Carbon Footprint](gcp-carbon-footprint.md) - Console dashboard and export that estimate location- and market-based greenhouse gas emissions from Google Cloud usage by project, region and product.
* [Google Cloud Infrastructure Manager](gcp-infrastructure-manager.md) - Managed service that runs Terraform deployments of Google Cloud resources and keeps their state.
* [Google Cloud Monitoring](gcp-cloud-monitoring.md) - Collects metrics from Google Cloud services and applications, with dashboards, uptime checks and alerting policies.
* [Google Cloud Resource Manager](gcp-resource-manager.md) - Organises resources into an organisation, folders and projects, with tags and organisation policies inherited down the hierarchy.

# Specialised data types

* [BigQuery geospatial analytics](gcp-bigquery-geospatial.md) - GEOGRAPHY type, spatial functions and spatial clustering for storing and analysing points, lines and polygons in BigQuery.
* [BigQuery Graph](gcp-bigquery-graph.md) - Defines property graphs over existing BigQuery tables and queries them with ISO GQL, without copying data.
* [BigQuery object tables and ObjectRef](gcp-bigquery-object-tables.md) - Exposes files in Cloud Storage as rows of metadata (object tables) or as ObjectRef values inside ordinary tables so images, documents and audio can be governed and processed with SQL.
* [Google Earth Engine](gcp-earth-engine.md) - Cloud platform with a large catalogue of satellite imagery and other raster geospatial datasets, and APIs for analysing them at regional to global scale.
