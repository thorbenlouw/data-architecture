---
type: Platform
id: platform-open-source
title: Open-source ecosystem
description: Open-source projects and open standards that underpin or complement commercial platforms.
folder: open-source
order: 14
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The open-source ecosystem is a set of independently governed projects and open specifications rather than one product. Most are hosted by the Apache Software Foundation or by the Linux Foundation and its sub-foundations (LF AI & Data, CNCF, the PyTorch Foundation and the Agentic AI Foundation). Others, such as DuckDB, dlt, Kestra and Cube Core, are led by one company or a small foundation. Each entry gives the project's licence, its governing body and the main vendors that sell it as a service.

The projects fit together as layers. File formats (Parquet, ORC, Avro, Arrow, Lance, Vortex) and table formats (Iceberg, Delta Lake, Hudi, Paimon, DuckLake) hold data in object storage. Catalogues (Apache Polaris, Unity Catalog, Apache Gravitino, Project Nessie, Hive Metastore) track tables, and the Iceberg REST Catalog specification is becoming the common contract between catalogues and engines. Engines include Spark, Flink, Trino, Presto, DuckDB, DataFusion, StarRocks and Doris, with Kafka and Pulsar for event streams. Around them sit orchestration (Airflow, Dagster, Prefect, Kestra), transformation (dbt, SQLMesh), metadata and policy (DataHub, OpenMetadata, OpenLineage, Ranger, Open Policy Agent), ML and generative AI (MLflow, Kubeflow, Ray, vLLM, KServe, Feast, LangChain, LangGraph, MCP, A2A) and BI (Superset, Metabase, Lightdash). Open specifications such as ODCS, ODPS, Apache Ossie and OpenSharing describe contracts, data products, semantic models and sharing.

A project provides a capability only once someone deploys and runs it. Hardening, key management, residency, failover and cost control fall to whoever operates it, which is often a cloud provider's managed service or the project's main commercial vendor.

# Notes

- Licences differ more than the "open source" label suggests. Entries are marked open-source only under OSI-approved licences. Terraform (BSL), Liquibase Community 5.x (FSL), the Airbyte platform (ELv2) and SDV (BSL) are source-available and marked as software, which matters for procurement and lock-in. MetricFlow moved the other way, from BSL to Apache 2.0, in October 2025.
- Fivetran and dbt Labs merged on 1 June 2026. dbt v2 reached GA on 15 September 2026 as two builds: dbt OSS under Apache 2.0, and the default "dbt" distribution (formerly the dbt Fusion engine) under a separate licence. dbt Core 1.x stays in maintenance.
- Several projects changed home in 2025-26. Apache Polaris graduated in February 2026 and Apache Gluten in early 2026. SQLMesh moved to the Linux Foundation in March 2026. MCP (December 2025) and A2A (August 2026) joined the Agentic AI Foundation. Delta Sharing became the Linux Foundation's OpenSharing project in June 2026, and Open Semantic Interchange was renamed Apache Ossie on entering the ASF Incubator.
- Company-led projects follow their owners. Dremio, which leads Project Nessie, is now part of SAP. CoreWeave owns marimo, lakeFS owns DVC, Snowflake owns Streamlit and IBM owns HashiCorp. Langfuse, owned by ClickHouse, is listed with ClickHouse. Check who controls a project's roadmap before standardising on it.
- Table formats are converging. Iceberg has the widest vendor support, while Delta UniForm, Paimon's Iceberg-compatible metadata and Apache XTable let one copy of the data be read as more than one format.
- MinIO's community edition is archived and no longer receives releases, so self-hosted lakes built on it need another S3-compatible store.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 16 of 22 (+1 in preview) | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md) (preview only) |
| [Storage and table management](../capabilities/storage/storage.md) | 20 of 23 | [Platform-managed storage](../capabilities/storage/managed-storage.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 17 of 18 | [AI functions in SQL](../capabilities/processing/ai-functions.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 5 of 5 |  |
| [Query and compute](../capabilities/compute/compute.md) | 16 of 22 | [Workload management](../capabilities/compute/workload-management.md), [Result caching](../capabilities/compute/result-caching.md), [Container services](../capabilities/compute/container-services.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Serverless compute](../capabilities/compute/serverless-compute.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 9 of 13 | [Decision management](../capabilities/serving/decision-management.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 10 of 20 (+1 in preview) | [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md) (preview only) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 13 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [AutoML](../capabilities/machine-learning/automl.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 12 of 18 | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model governance](../capabilities/mlops/model-governance.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Edge inference](../capabilities/mlops/edge-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 14 of 23 | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Model customisation](../capabilities/generative-ai/model-customisation.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 13 of 20 | [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [Model lineage](../capabilities/metadata/model-lineage.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 10 of 24 | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md) |
| [Security and access](../capabilities/security/security.md) | 12 of 23 | [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Network security](../capabilities/security/network-security.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 5 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| [Data products](../capabilities/data-products/data-products.md) | 5 of 7 | [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 11 of 16 | [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 13 of 27 | [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Customer-hosted data plane](../capabilities/platform-operations/hybrid-data-plane.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 6 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Technologies

## Ingestion and integration

- [Airbyte](../technologies/open-source/airbyte.md): Data integration platform with hundreds of prebuilt connectors for loading data from databases, APIs and SaaS applications into warehouses and lakes.
- [Apache Fluss (incubating)](../technologies/open-source/apache-fluss.md) (preview): Streaming storage for real-time analytics that holds fresh data in primary-key and columnar log tables and tiers it into lakehouse formats.
- [Apache Kafka](../technologies/open-source/apache-kafka.md): Distributed event streaming platform that stores ordered, replayable logs of events in topics for publish and subscribe at high throughput.
- [Apache Pulsar](../technologies/open-source/apache-pulsar.md): Distributed messaging and event streaming platform with built-in multi-tenancy, geo-replication, tiered storage and both stream and queue subscriptions.
- [Debezium](../technologies/open-source/debezium.md): Log-based change data capture platform that streams row-level changes from databases such as PostgreSQL, MySQL, SQL Server, Oracle and MongoDB.
- [dlt (data load tool)](../technologies/open-source/dlt.md): Python library for writing extract-and-load pipelines that infer and evolve schemas, load incrementally and write to warehouses, lakes and lakehouse tables.
- [Flink CDC](../technologies/open-source/apache-flink-cdc.md): Change data capture framework on Flink that reads database logs and syncs changes, including schema changes, to lakes, warehouses and streams through YAML-defined pipelines.
- [Kafka Connect](../technologies/open-source/apache-kafka-connect.md): Kafka framework for running source and sink connectors that move data between Kafka and external systems with offset tracking and scaling.

## Storage and table management

- [Apache Avro](../technologies/open-source/apache-avro.md): Row-based binary serialisation format with an embedded schema and well-defined schema evolution rules, widely used for Kafka messages.
- [Apache Gravitino](../technologies/open-source/apache-gravitino.md): Federated metadata catalogue that manages tables, filesets, message topics and models across many sources, with an Iceberg REST service and unified access control.
- [Apache Hadoop (HDFS and YARN)](../technologies/open-source/apache-hadoop.md): Distributed file system (HDFS) and cluster resource manager (YARN) that formed the first generation of on-premises data lakes.
- [Apache Hive Metastore](../technologies/open-source/apache-hive-metastore.md): Metadata service that stores table definitions, schemas, partitions and locations for Hive-style data lakes, used by Spark, Trino, Flink and others.
- [Apache Hudi](../technologies/open-source/apache-hudi.md): Open table format and platform for incremental processing, with record-level indexes, upserts and deletes, and incremental queries over lake tables.
- [Apache Iceberg](../technologies/open-source/apache-iceberg.md): Open table format that manages files in object storage as transactional tables with snapshots, hidden partitioning, schema evolution and time travel.
- [Apache ORC](../technologies/open-source/apache-orc.md): Open columnar file format with lightweight indexes and statistics, originally designed for Hive.
- [Apache Paimon](../technologies/open-source/apache-paimon.md): Lake table format that uses an LSM-tree layout to support high-frequency streaming upserts and changelog generation, designed to work with Flink and Spark.
- [Apache Parquet](../technologies/open-source/apache-parquet.md): Open columnar file format with compression, encoding and per-column statistics, the default storage format for data lakes and lakehouses.
- [Apache Polaris](../technologies/open-source/apache-polaris.md): Catalogue service that implements the Iceberg REST specification, with role-based access control, credential vending and federation to other catalogues.
- [Apache XTable (incubating)](../technologies/open-source/apache-xtable.md) (preview): Converter that translates table metadata between Iceberg, Delta Lake and Hudi so one copy of the data can be read as any of the three formats.
- [Delta Lake](../technologies/open-source/delta-lake.md): Open table format and libraries that add ACID transactions, schema enforcement, time travel and row-level updates to Parquet files.
- [DuckLake](../technologies/open-source/ducklake.md): Lakehouse table format that keeps data in Parquet files on object storage and all table metadata in an ordinary SQL database.
- [DVC (Data Version Control)](../technologies/open-source/dvc.md): Command-line tool that versions datasets and models alongside code in Git, storing the large files in remote storage.
- [Iceberg REST Catalog specification](../technologies/open-source/apache-iceberg-rest-catalog-spec.md): OpenAPI specification for how engines talk to an Iceberg catalogue to list, create, load and commit tables and views, independent of the catalogue's implementation.
- [lakeFS](../technologies/open-source/lakefs.md): Version control layer over object storage that gives data lakes Git-like branches, commits, merges and rollbacks, independent of file or table format.
- [Lance](../technologies/open-source/lance.md): Columnar data format and table format for AI and multimodal data, with fast random access, versioning and built-in vector indexes.
- [MinIO (community edition)](../technologies/open-source/minio.md) (deprecated): Self-hosted, S3-compatible object storage server, widely used for on-premises and development data lakes.
- [Project Nessie](../technologies/open-source/project-nessie.md): Transactional catalogue for Iceberg that adds Git-like branches, tags and commits across many tables at once.
- [Unity Catalog (open source)](../technologies/open-source/unity-catalog.md): Open-source catalogue for tables, volumes of files, functions and AI models, with an Iceberg REST and Hive Metastore compatible API.
- [Vortex](../technologies/open-source/vortex.md): Extensible columnar file format and toolkit with pluggable encodings and compression, designed for fast random access and scans on object storage.

## Processing and transformation

- [Apache Beam](../technologies/open-source/apache-beam.md): Portable programming model and SDKs for batch and streaming pipelines that run on several engines, such as Flink, Spark and Google Cloud Dataflow.
- [Apache DataFusion](../technologies/open-source/apache-datafusion.md): Extensible query engine library in Rust, built on Apache Arrow, that projects embed to get SQL and DataFrame execution.
- [Apache Flink](../technologies/open-source/apache-flink.md): Distributed stream processing engine with exactly-once state, event-time semantics and a unified batch and streaming SQL and Table API.
- [Apache NiFi](../technologies/open-source/apache-nifi.md): Visual dataflow tool for routing, transforming and delivering data between systems, with back-pressure and record-level data provenance.
- [Apache Spark](../technologies/open-source/apache-spark.md): Distributed engine for batch, SQL, streaming and machine learning workloads, with DataFrame APIs in Python, Scala, Java, R and SQL.
- [Dask](../technologies/open-source/dask.md): Python library that scales NumPy, pandas and custom Python code in parallel across cores or a cluster.
- [dbt Core (v1.x)](../technologies/open-source/dbt-core.md): Python framework for SQL and Python transformations as version-controlled models, with dependency resolution, tests, documentation and lineage.
- [dbt OSS](../technologies/open-source/dbt-oss.md): Open-source distribution of the Rust-based dbt v2 engine, which parses and compiles dbt projects much faster and checks them against a strict language specification.
- [Docling](../technologies/open-source/docling.md): Library that converts PDFs, Office files, HTML and images into structured text, tables and layout for retrieval and AI pipelines.
- [DuckDB](../technologies/open-source/duckdb.md): In-process analytical SQL database that runs inside an application or notebook and queries local files, object storage and lakehouse tables quickly on one machine.
- [Kafka Streams](../technologies/open-source/apache-kafka-streams.md): Java library for building stateful stream processing applications that read from and write to Kafka.
- [pandas](../technologies/open-source/pandas.md): Python library for in-memory tabular data analysis and manipulation, the most widely used DataFrame API in data science.
- [Polars](../technologies/open-source/polars.md): DataFrame library written in Rust with Python bindings, using lazy query optimisation and a streaming engine to process data larger than memory on one machine.
- [RisingWave](../technologies/open-source/risingwave.md): Streaming database that keeps SQL materialised views continuously up to date over streams and CDC sources, with a PostgreSQL-compatible interface.
- [Spark Declarative Pipelines](../technologies/open-source/apache-spark-declarative-pipelines.md): Spark framework in which you declare datasets and the queries that produce them, and Spark works out execution order, parallelism, checkpoints and retries.
- [Spark Structured Streaming](../technologies/open-source/apache-spark-structured-streaming.md): Spark's stream processing API, which treats a stream as an unbounded table and processes it incrementally with stateful operators and event-time windows.
- [SQLMesh](../technologies/open-source/sqlmesh.md): Transformation framework that understands SQL semantically, plans changes before applying them and uses virtual data environments to test and promote models without rebuilding tables.

## Orchestration

- [Apache Airflow](../technologies/open-source/apache-airflow.md): Workflow orchestrator in which pipelines are defined in Python as task graphs (DAGs) and run on schedules, data events or on demand.
- [Dagster](../technologies/open-source/dagster.md): Data orchestrator built around software-defined assets, where you declare the data assets you want and their dependencies and Dagster schedules and tracks them.
- [Kestra](../technologies/open-source/kestra.md): Declarative orchestration platform where workflows are written in YAML and started by schedules, events, webhooks or messages.
- [Prefect](../technologies/open-source/prefect.md): Python workflow orchestration framework that turns ordinary functions into observable, retryable flows with schedules and event-based automations.

## Query and compute

- [Apache Arrow](../technologies/open-source/apache-arrow.md): Language-independent in-memory columnar format, with libraries that let engines and tools exchange data without serialisation.
- [Apache Doris](../technologies/open-source/apache-doris.md): MPP analytical database for real-time reporting, ad hoc queries and lakehouse queries, with a MySQL-compatible interface.
- [Apache Druid](../technologies/open-source/apache-druid.md): Real-time analytical database that ingests streams and batches and answers aggregation queries over high-cardinality event data in under a second.
- [Apache Gluten](../technologies/open-source/apache-gluten.md): Plug-in that offloads Spark SQL execution to native, vectorised C++ engines such as Velox or ClickHouse while keeping Spark's APIs and scheduling.
- [Apache Pinot](../technologies/open-source/apache-pinot.md): Real-time distributed OLAP datastore designed for low-latency, high-concurrency analytical queries in user-facing applications.
- [Presto](../technologies/open-source/presto.md): Distributed SQL query engine for interactive analytics over data lakes and federated sources, originally developed at Meta.
- [StarRocks](../technologies/open-source/starrocks.md): MPP analytical database with a vectorised engine, used for real-time analytics and as a fast query layer over Iceberg, Hudi, Delta and Paimon tables.
- [Trino](../technologies/open-source/trino.md): Distributed SQL query engine that queries data in place across object storage, lakehouse tables and many databases through connectors.

## Serving and activation

- [ADBC (Arrow Database Connectivity)](../technologies/open-source/apache-arrow-adbc.md): Database connectivity API and drivers, similar in purpose to JDBC and ODBC, that move query results as Arrow columnar data.
- [Apache Kyuubi](../technologies/open-source/apache-kyuubi.md): Multi-tenant SQL gateway that gives JDBC, ODBC and REST clients shared, authenticated access to Spark, Flink, Trino and other engines.
- [Arrow Flight SQL](../technologies/open-source/apache-arrow-flight-sql.md): Protocol for running SQL against databases and returning results as Arrow record batches over gRPC, avoiding row-by-row conversion.
- [PostgreSQL](../technologies/open-source/postgresql.md): Open-source relational database used as an operational system of record and, with extensions, for analytics, vectors, geospatial and time-series data.

## Analytics and BI

- [Apache Ossie (incubating)](../technologies/open-source/apache-ossie.md) (preview): Vendor-neutral specification for exchanging semantic models, metrics, dimensions and relationships between BI, semantic layer and AI tools.
- [Apache Superset](../technologies/open-source/apache-superset.md): Web-based BI tool with a no-code chart builder, SQL Lab editor, interactive dashboards, a lightweight semantic layer of datasets and metrics, and scheduled alerts and reports.
- [Cube Core](../technologies/open-source/cube-core.md): Semantic layer that defines data models and metrics once and serves them through SQL, REST and GraphQL APIs with caching and pre-aggregations.
- [GrowthBook](../technologies/open-source/growthbook.md): Open-core feature flagging and experimentation platform that analyses A/B tests with SQL against data already in the warehouse.
- [Lightdash](../technologies/open-source/lightdash.md): BI tool that reads metrics and dimensions defined in dbt projects and lets users explore them and build dashboards.
- [Metabase](../technologies/open-source/metabase.md): BI tool for asking questions with a visual query builder or SQL and sharing dashboards, aimed at non-technical users.
- [MetricFlow](../technologies/open-source/metricflow.md): Metric definition and SQL generation engine that compiles semantic models and metrics into correct SQL for the target warehouse.

## Machine learning development

- [Feast](../technologies/open-source/feast.md): Feature store that defines features once and serves them from offline stores for training and online stores for low-latency inference, with point-in-time correct joins.
- [Kubeflow](../technologies/open-source/kubeflow.md): Collection of Kubernetes-native ML tools, including Kubeflow Pipelines, Trainer for distributed training, Katib for tuning, notebooks and a model registry.
- [MLflow](../technologies/open-source/mlflow.md): Platform for the ML and generative AI lifecycle, covering experiment tracking, model registry, model packaging, tracing, evaluation and prompt management.
- [Ray](../technologies/open-source/ray.md): Distributed compute framework for Python, with libraries for data processing (Ray Data), training (Ray Train), tuning (Ray Tune) and model serving (Ray Serve).

## ML operations

- [Evidently](../technologies/open-source/evidently.md): Python library for evaluating and monitoring ML models and LLM applications, with data drift, data quality and model quality reports and tests.
- [KServe](../technologies/open-source/kserve.md): Kubernetes model serving platform that deploys predictive and generative models as autoscaling inference services, including canary rollouts.
- [vLLM](../technologies/open-source/vllm.md): High-throughput inference and serving engine for large language models, with an OpenAI-compatible API.

## Generative AI

- [Agent2Agent (A2A) protocol](../technologies/open-source/agent2agent-protocol.md): Open protocol for AI agents built on different frameworks to discover each other's capabilities and delegate tasks to one another.
- [LangChain](../technologies/open-source/langchain.md): Framework with standard interfaces for models, tools, retrievers and vector stores for building LLM applications and agents.
- [LangGraph](../technologies/open-source/langgraph.md): Library for building stateful, multi-step agents as graphs, with persistence, human-in-the-loop interruption and streaming.
- [LiteLLM](../technologies/open-source/litellm.md): Python SDK and proxy server that call more than 100 model providers through one OpenAI-compatible API, with keys, budgets, rate limits, fallbacks and logging.
- [LlamaIndex](../technologies/open-source/llamaindex.md): Framework for connecting LLMs to your own data, with document loaders, indexing, retrieval, query engines and agent workflows.
- [Milvus](../technologies/open-source/milvus.md): Distributed vector database for storing and searching billions of embeddings, with several index types and hybrid scalar filtering.
- [Model Context Protocol (MCP)](../technologies/open-source/model-context-protocol.md): Open protocol through which AI applications and agents discover and call external tools, data sources and prompts provided by MCP servers.
- [NeMo Guardrails](../technologies/open-source/nemo-guardrails.md): Toolkit for adding programmable input, output, dialogue and retrieval rails to LLM applications to block unsafe or off-topic content and jailbreak attempts.
- [OpenTelemetry semantic conventions for generative AI](../technologies/open-source/opentelemetry-genai-semantic-conventions.md) (preview): Standard attribute names and structures for tracing LLM calls, agents and MCP interactions, including model, token usage, prompts and responses.
- [pgvector](../technologies/open-source/pgvector.md): PostgreSQL extension that adds a vector type, distance operators and HNSW and IVFFlat indexes for similarity search.
- [Qdrant](../technologies/open-source/qdrant.md): Vector database and similarity search engine written in Rust, with payload filtering, hybrid search and quantisation.

## Metadata and discovery

- [Apache Atlas](../technologies/open-source/apache-atlas.md): Metadata and governance service for Hadoop-style estates that records entities, lineage and classifications and propagates classifications along lineage.
- [Apicurio Registry](../technologies/open-source/apicurio-registry.md): Schema and API registry that stores and versions Avro, Protobuf, JSON Schema, OpenAPI and AsyncAPI artefacts and checks compatibility rules.
- [DataHub](../technologies/open-source/datahub.md): Metadata platform and data catalogue with search, column-level lineage, glossary, ownership, quality assertions and an event-driven metadata model.
- [Marquez](../technologies/open-source/marquez.md): Metadata service that collects OpenLineage events and shows dataset and job lineage and run history through an API and web UI.
- [OpenLineage](../technologies/open-source/openlineage.md): Open specification and client libraries for emitting lineage events about jobs, runs and datasets, with extensible facets such as column-level lineage.
- [OpenMetadata](../technologies/open-source/openmetadata.md): Metadata platform combining a data catalogue, lineage, glossary, data quality tests, data contracts, domains and data products.

## Data quality and observability

- [GX Core (Great Expectations)](../technologies/open-source/great-expectations.md): Python framework for defining data quality tests, called Expectations, running them against data and producing human-readable validation reports.

## Governance and compliance

- [Microsoft Presidio](../technologies/open-source/presidio.md): Toolkit that detects personal data in text, images and structured data and masks, replaces or encrypts it.
- [Open Policy Agent (OPA)](../technologies/open-source/open-policy-agent.md): General-purpose policy engine that evaluates policies written in Rego to make authorisation and compliance decisions for applications, APIs, Kubernetes and pipelines.

## Security and access

- [Apache Ranger](../technologies/open-source/apache-ranger.md): Centralised security administration that defines and enforces access policies, row filters and column masking across Hadoop, Hive, Kafka, Trino and other services, with audit.
- [Keycloak](../technologies/open-source/keycloak.md): Identity and access management server providing single sign-on, OpenID Connect, OAuth 2.0 and SAML for applications and services.
- [OpenBao](../technologies/open-source/openbao.md): Secrets management server that stores, issues and rotates credentials, keys and certificates, forked from HashiCorp Vault.
- [OpenSSF Model Signing](../technologies/open-source/sigstore-model-signing.md): Open specification and library for signing machine learning model files with Sigstore so consumers can check who produced a model and that it has not been altered.

## Data sharing and collaboration

- [OpenSharing protocol](../technologies/open-source/delta-sharing.md): Open protocol, the successor to Delta Sharing, for sharing live tables, unstructured data, AI models and agent skills with other organisations and tools without copying the data.

## Data products

- [Data Contract CLI](../technologies/open-source/data-contract-cli.md): Command-line tool that lints data contracts, tests live data against them, detects breaking changes and generates code and documentation from them.
- [Open Data Contract Standard (ODCS)](../technologies/open-source/open-data-contract-standard.md): YAML specification for data contracts covering schema, quality rules, service levels, roles, support channels, pricing and servers.
- [Open Data Product Standard (ODPS)](../technologies/open-source/open-data-product-standard.md): YAML specification describing a data product's purpose, input and output ports, owners, contracts and lifecycle status.
- [Soda Core](../technologies/open-source/soda-core.md): Data quality and data contract verification engine that checks schema and data against YAML contracts from a CLI, Python or a pipeline.

## Development and DataOps

- [Flyway Community](../technologies/open-source/flyway.md): Database migration tool that applies versioned SQL or Java migration scripts in order and records which have run.
- [Liquibase Community](../technologies/open-source/liquibase.md): Database change management tool that tracks, versions and applies schema changes defined in SQL, XML, YAML or JSON changelogs.
- [marimo](../technologies/open-source/marimo.md): Reactive Python notebook stored as a plain Python file, where changing a cell reruns its dependants, and which can be deployed as an app or run as a script.
- [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../technologies/open-source/jupyter.md): Interactive notebook environment that combines live code, results and narrative, with JupyterHub providing multi-user servers.
- [SQLFluff](../technologies/open-source/sqlfluff.md): Linter and auto-formatter for SQL that supports many dialects and dbt or Jinja templating.
- [Streamlit](../technologies/open-source/streamlit.md): Python framework for building interactive data and AI web applications from scripts without front-end code.
- [Synthetic Data Vault (SDV)](../technologies/open-source/sdv.md): Python library that learns from real tabular, relational and time-series data and generates synthetic data with similar statistical properties.

## Platform operations

- [HashiCorp Terraform](../technologies/open-source/terraform.md): Infrastructure-as-code tool that declares infrastructure in HCL and creates, changes and destroys it through providers.
- [OpenTelemetry](../technologies/open-source/opentelemetry.md): Vendor-neutral standard, SDKs and Collector for producing and exporting traces, metrics and logs from applications and infrastructure.
- [OpenTofu](../technologies/open-source/opentofu.md): Infrastructure-as-code tool that declares cloud and platform resources in HCL and applies changes through plans, as a fork of Terraform.

## Specialised data types

- [Apache Sedona](../technologies/open-source/apache-sedona.md): Spatial computing engine that adds geospatial types, functions and spatial joins to Spark, Flink and other engines.
- [GeoParquet](../technologies/open-source/geoparquet.md): Specification for storing geospatial vector data such as points, lines and polygons in Parquet files with standard metadata.
- [OpenSearch](../technologies/open-source/opensearch.md): Search and analytics engine for full-text search, log analytics and vector search, with dashboards for visualisation.
- [PostGIS](../technologies/open-source/postgis.md): PostgreSQL extension that adds spatial types, spatial indexes and hundreds of geospatial functions.

