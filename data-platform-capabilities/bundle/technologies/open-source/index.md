# Open-source ecosystem

# Ingestion and integration

* [Airbyte](airbyte.md) - Data integration platform with hundreds of prebuilt connectors for loading data from databases, APIs and SaaS applications into warehouses and lakes.
* [Apache Fluss (incubating)](apache-fluss.md) (preview) - Streaming storage for real-time analytics that holds fresh data in primary-key and columnar log tables and tiers it into lakehouse formats.
* [Apache Kafka](apache-kafka.md) - Distributed event streaming platform that stores ordered, replayable logs of events in topics for publish and subscribe at high throughput.
* [Apache Pulsar](apache-pulsar.md) - Distributed messaging and event streaming platform with built-in multi-tenancy, geo-replication, tiered storage and both stream and queue subscriptions.
* [Debezium](debezium.md) - Log-based change data capture platform that streams row-level changes from databases such as PostgreSQL, MySQL, SQL Server, Oracle and MongoDB.
* [dlt (data load tool)](dlt.md) - Python library for writing extract-and-load pipelines that infer and evolve schemas, load incrementally and write to warehouses, lakes and lakehouse tables.
* [Flink CDC](apache-flink-cdc.md) - Change data capture framework on Flink that reads database logs and syncs changes, including schema changes, to lakes, warehouses and streams through YAML-defined pipelines.
* [Kafka Connect](apache-kafka-connect.md) - Kafka framework for running source and sink connectors that move data between Kafka and external systems with offset tracking and scaling.

# Storage and table management

* [Apache Avro](apache-avro.md) - Row-based binary serialisation format with an embedded schema and well-defined schema evolution rules, widely used for Kafka messages.
* [Apache Gravitino](apache-gravitino.md) - Federated metadata catalogue that manages tables, filesets, message topics and models across many sources, with an Iceberg REST service and unified access control.
* [Apache Hadoop (HDFS and YARN)](apache-hadoop.md) - Distributed file system (HDFS) and cluster resource manager (YARN) that formed the first generation of on-premises data lakes.
* [Apache Hive Metastore](apache-hive-metastore.md) - Metadata service that stores table definitions, schemas, partitions and locations for Hive-style data lakes, used by Spark, Trino, Flink and others.
* [Apache Hudi](apache-hudi.md) - Open table format and platform for incremental processing, with record-level indexes, upserts and deletes, and incremental queries over lake tables.
* [Apache Iceberg](apache-iceberg.md) - Open table format that manages files in object storage as transactional tables with snapshots, hidden partitioning, schema evolution and time travel.
* [Apache ORC](apache-orc.md) - Open columnar file format with lightweight indexes and statistics, originally designed for Hive.
* [Apache Paimon](apache-paimon.md) - Lake table format that uses an LSM-tree layout to support high-frequency streaming upserts and changelog generation, designed to work with Flink and Spark.
* [Apache Parquet](apache-parquet.md) - Open columnar file format with compression, encoding and per-column statistics, the default storage format for data lakes and lakehouses.
* [Apache Polaris](apache-polaris.md) - Catalogue service that implements the Iceberg REST specification, with role-based access control, credential vending and federation to other catalogues.
* [Apache XTable (incubating)](apache-xtable.md) (preview) - Converter that translates table metadata between Iceberg, Delta Lake and Hudi so one copy of the data can be read as any of the three formats.
* [Delta Lake](delta-lake.md) - Open table format and libraries that add ACID transactions, schema enforcement, time travel and row-level updates to Parquet files.
* [DuckLake](ducklake.md) - Lakehouse table format that keeps data in Parquet files on object storage and all table metadata in an ordinary SQL database.
* [DVC (Data Version Control)](dvc.md) - Command-line tool that versions datasets and models alongside code in Git, storing the large files in remote storage.
* [Iceberg REST Catalog specification](apache-iceberg-rest-catalog-spec.md) - OpenAPI specification for how engines talk to an Iceberg catalogue to list, create, load and commit tables and views, independent of the catalogue's implementation.
* [lakeFS](lakefs.md) - Version control layer over object storage that gives data lakes Git-like branches, commits, merges and rollbacks, independent of file or table format.
* [Lance](lance.md) - Columnar data format and table format for AI and multimodal data, with fast random access, versioning and built-in vector indexes.
* [MinIO (community edition)](minio.md) (deprecated) - Self-hosted, S3-compatible object storage server, widely used for on-premises and development data lakes.
* [Project Nessie](project-nessie.md) - Transactional catalogue for Iceberg that adds Git-like branches, tags and commits across many tables at once.
* [Unity Catalog (open source)](unity-catalog.md) - Open-source catalogue for tables, volumes of files, functions and AI models, with an Iceberg REST and Hive Metastore compatible API.
* [Vortex](vortex.md) - Extensible columnar file format and toolkit with pluggable encodings and compression, designed for fast random access and scans on object storage.

# Processing and transformation

* [Apache Beam](apache-beam.md) - Portable programming model and SDKs for batch and streaming pipelines that run on several engines, such as Flink, Spark and Google Cloud Dataflow.
* [Apache DataFusion](apache-datafusion.md) - Extensible query engine library in Rust, built on Apache Arrow, that projects embed to get SQL and DataFrame execution.
* [Apache Flink](apache-flink.md) - Distributed stream processing engine with exactly-once state, event-time semantics and a unified batch and streaming SQL and Table API.
* [Apache NiFi](apache-nifi.md) - Visual dataflow tool for routing, transforming and delivering data between systems, with back-pressure and record-level data provenance.
* [Apache Spark](apache-spark.md) - Distributed engine for batch, SQL, streaming and machine learning workloads, with DataFrame APIs in Python, Scala, Java, R and SQL.
* [Dask](dask.md) - Python library that scales NumPy, pandas and custom Python code in parallel across cores or a cluster.
* [dbt Core (v1.x)](dbt-core.md) - Python framework for SQL and Python transformations as version-controlled models, with dependency resolution, tests, documentation and lineage.
* [dbt OSS](dbt-oss.md) - Open-source distribution of the Rust-based dbt v2 engine, which parses and compiles dbt projects much faster and checks them against a strict language specification.
* [Docling](docling.md) - Library that converts PDFs, Office files, HTML and images into structured text, tables and layout for retrieval and AI pipelines.
* [DuckDB](duckdb.md) - In-process analytical SQL database that runs inside an application or notebook and queries local files, object storage and lakehouse tables quickly on one machine.
* [Kafka Streams](apache-kafka-streams.md) - Java library for building stateful stream processing applications that read from and write to Kafka.
* [pandas](pandas.md) - Python library for in-memory tabular data analysis and manipulation, the most widely used DataFrame API in data science.
* [Polars](polars.md) - DataFrame library written in Rust with Python bindings, using lazy query optimisation and a streaming engine to process data larger than memory on one machine.
* [RisingWave](risingwave.md) - Streaming database that keeps SQL materialised views continuously up to date over streams and CDC sources, with a PostgreSQL-compatible interface.
* [Spark Declarative Pipelines](apache-spark-declarative-pipelines.md) - Spark framework in which you declare datasets and the queries that produce them, and Spark works out execution order, parallelism, checkpoints and retries.
* [Spark Structured Streaming](apache-spark-structured-streaming.md) - Spark's stream processing API, which treats a stream as an unbounded table and processes it incrementally with stateful operators and event-time windows.
* [SQLMesh](sqlmesh.md) - Transformation framework that understands SQL semantically, plans changes before applying them and uses virtual data environments to test and promote models without rebuilding tables.

# Orchestration

* [Apache Airflow](apache-airflow.md) - Workflow orchestrator in which pipelines are defined in Python as task graphs (DAGs) and run on schedules, data events or on demand.
* [Dagster](dagster.md) - Data orchestrator built around software-defined assets, where you declare the data assets you want and their dependencies and Dagster schedules and tracks them.
* [Kestra](kestra.md) - Declarative orchestration platform where workflows are written in YAML and started by schedules, events, webhooks or messages.
* [Prefect](prefect.md) - Python workflow orchestration framework that turns ordinary functions into observable, retryable flows with schedules and event-based automations.

# Query and compute

* [Apache Arrow](apache-arrow.md) - Language-independent in-memory columnar format, with libraries that let engines and tools exchange data without serialisation.
* [Apache Doris](apache-doris.md) - MPP analytical database for real-time reporting, ad hoc queries and lakehouse queries, with a MySQL-compatible interface.
* [Apache Druid](apache-druid.md) - Real-time analytical database that ingests streams and batches and answers aggregation queries over high-cardinality event data in under a second.
* [Apache Gluten](apache-gluten.md) - Plug-in that offloads Spark SQL execution to native, vectorised C++ engines such as Velox or ClickHouse while keeping Spark's APIs and scheduling.
* [Apache Pinot](apache-pinot.md) - Real-time distributed OLAP datastore designed for low-latency, high-concurrency analytical queries in user-facing applications.
* [Presto](presto.md) - Distributed SQL query engine for interactive analytics over data lakes and federated sources, originally developed at Meta.
* [StarRocks](starrocks.md) - MPP analytical database with a vectorised engine, used for real-time analytics and as a fast query layer over Iceberg, Hudi, Delta and Paimon tables.
* [Trino](trino.md) - Distributed SQL query engine that queries data in place across object storage, lakehouse tables and many databases through connectors.

# Serving and activation

* [ADBC (Arrow Database Connectivity)](apache-arrow-adbc.md) - Database connectivity API and drivers, similar in purpose to JDBC and ODBC, that move query results as Arrow columnar data.
* [Apache Kyuubi](apache-kyuubi.md) - Multi-tenant SQL gateway that gives JDBC, ODBC and REST clients shared, authenticated access to Spark, Flink, Trino and other engines.
* [Arrow Flight SQL](apache-arrow-flight-sql.md) - Protocol for running SQL against databases and returning results as Arrow record batches over gRPC, avoiding row-by-row conversion.
* [PostgreSQL](postgresql.md) - Open-source relational database used as an operational system of record and, with extensions, for analytics, vectors, geospatial and time-series data.

# Analytics and BI

* [Apache Ossie (incubating)](apache-ossie.md) (preview) - Vendor-neutral specification for exchanging semantic models, metrics, dimensions and relationships between BI, semantic layer and AI tools.
* [Apache Superset](apache-superset.md) - Web-based BI tool with a no-code chart builder, SQL Lab editor, interactive dashboards, a lightweight semantic layer of datasets and metrics, and scheduled alerts and reports.
* [Cube Core](cube-core.md) - Semantic layer that defines data models and metrics once and serves them through SQL, REST and GraphQL APIs with caching and pre-aggregations.
* [GrowthBook](growthbook.md) - Open-core feature flagging and experimentation platform that analyses A/B tests with SQL against data already in the warehouse.
* [Lightdash](lightdash.md) - BI tool that reads metrics and dimensions defined in dbt projects and lets users explore them and build dashboards.
* [Metabase](metabase.md) - BI tool for asking questions with a visual query builder or SQL and sharing dashboards, aimed at non-technical users.
* [MetricFlow](metricflow.md) - Metric definition and SQL generation engine that compiles semantic models and metrics into correct SQL for the target warehouse.

# Machine learning development

* [Feast](feast.md) - Feature store that defines features once and serves them from offline stores for training and online stores for low-latency inference, with point-in-time correct joins.
* [Kubeflow](kubeflow.md) - Collection of Kubernetes-native ML tools, including Kubeflow Pipelines, Trainer for distributed training, Katib for tuning, notebooks and a model registry.
* [MLflow](mlflow.md) - Platform for the ML and generative AI lifecycle, covering experiment tracking, model registry, model packaging, tracing, evaluation and prompt management.
* [Ray](ray.md) - Distributed compute framework for Python, with libraries for data processing (Ray Data), training (Ray Train), tuning (Ray Tune) and model serving (Ray Serve).

# ML operations

* [Evidently](evidently.md) - Python library for evaluating and monitoring ML models and LLM applications, with data drift, data quality and model quality reports and tests.
* [KServe](kserve.md) - Kubernetes model serving platform that deploys predictive and generative models as autoscaling inference services, including canary rollouts.
* [vLLM](vllm.md) - High-throughput inference and serving engine for large language models, with an OpenAI-compatible API.

# Generative AI

* [Agent2Agent (A2A) protocol](agent2agent-protocol.md) - Open protocol for AI agents built on different frameworks to discover each other's capabilities and delegate tasks to one another.
* [LangChain](langchain.md) - Framework with standard interfaces for models, tools, retrievers and vector stores for building LLM applications and agents.
* [LangGraph](langgraph.md) - Library for building stateful, multi-step agents as graphs, with persistence, human-in-the-loop interruption and streaming.
* [LiteLLM](litellm.md) - Python SDK and proxy server that call more than 100 model providers through one OpenAI-compatible API, with keys, budgets, rate limits, fallbacks and logging.
* [LlamaIndex](llamaindex.md) - Framework for connecting LLMs to your own data, with document loaders, indexing, retrieval, query engines and agent workflows.
* [Milvus](milvus.md) - Distributed vector database for storing and searching billions of embeddings, with several index types and hybrid scalar filtering.
* [Model Context Protocol (MCP)](model-context-protocol.md) - Open protocol through which AI applications and agents discover and call external tools, data sources and prompts provided by MCP servers.
* [NeMo Guardrails](nemo-guardrails.md) - Toolkit for adding programmable input, output, dialogue and retrieval rails to LLM applications to block unsafe or off-topic content and jailbreak attempts.
* [OpenTelemetry semantic conventions for generative AI](opentelemetry-genai-semantic-conventions.md) (preview) - Standard attribute names and structures for tracing LLM calls, agents and MCP interactions, including model, token usage, prompts and responses.
* [pgvector](pgvector.md) - PostgreSQL extension that adds a vector type, distance operators and HNSW and IVFFlat indexes for similarity search.
* [Qdrant](qdrant.md) - Vector database and similarity search engine written in Rust, with payload filtering, hybrid search and quantisation.

# Metadata and discovery

* [Apache Atlas](apache-atlas.md) - Metadata and governance service for Hadoop-style estates that records entities, lineage and classifications and propagates classifications along lineage.
* [Apicurio Registry](apicurio-registry.md) - Schema and API registry that stores and versions Avro, Protobuf, JSON Schema, OpenAPI and AsyncAPI artefacts and checks compatibility rules.
* [DataHub](datahub.md) - Metadata platform and data catalogue with search, column-level lineage, glossary, ownership, quality assertions and an event-driven metadata model.
* [Marquez](marquez.md) - Metadata service that collects OpenLineage events and shows dataset and job lineage and run history through an API and web UI.
* [OpenLineage](openlineage.md) - Open specification and client libraries for emitting lineage events about jobs, runs and datasets, with extensible facets such as column-level lineage.
* [OpenMetadata](openmetadata.md) - Metadata platform combining a data catalogue, lineage, glossary, data quality tests, data contracts, domains and data products.

# Data quality and observability

* [GX Core (Great Expectations)](great-expectations.md) - Python framework for defining data quality tests, called Expectations, running them against data and producing human-readable validation reports.

# Governance and compliance

* [Microsoft Presidio](presidio.md) - Toolkit that detects personal data in text, images and structured data and masks, replaces or encrypts it.
* [Open Policy Agent (OPA)](open-policy-agent.md) - General-purpose policy engine that evaluates policies written in Rego to make authorisation and compliance decisions for applications, APIs, Kubernetes and pipelines.

# Security and access

* [Apache Ranger](apache-ranger.md) - Centralised security administration that defines and enforces access policies, row filters and column masking across Hadoop, Hive, Kafka, Trino and other services, with audit.
* [Keycloak](keycloak.md) - Identity and access management server providing single sign-on, OpenID Connect, OAuth 2.0 and SAML for applications and services.
* [OpenBao](openbao.md) - Secrets management server that stores, issues and rotates credentials, keys and certificates, forked from HashiCorp Vault.
* [OpenSSF Model Signing](sigstore-model-signing.md) - Open specification and library for signing machine learning model files with Sigstore so consumers can check who produced a model and that it has not been altered.

# Data sharing and collaboration

* [OpenSharing protocol](delta-sharing.md) - Open protocol, the successor to Delta Sharing, for sharing live tables, unstructured data, AI models and agent skills with other organisations and tools without copying the data.

# Data products

* [Data Contract CLI](data-contract-cli.md) - Command-line tool that lints data contracts, tests live data against them, detects breaking changes and generates code and documentation from them.
* [Open Data Contract Standard (ODCS)](open-data-contract-standard.md) - YAML specification for data contracts covering schema, quality rules, service levels, roles, support channels, pricing and servers.
* [Open Data Product Standard (ODPS)](open-data-product-standard.md) - YAML specification describing a data product's purpose, input and output ports, owners, contracts and lifecycle status.
* [Soda Core](soda-core.md) - Data quality and data contract verification engine that checks schema and data against YAML contracts from a CLI, Python or a pipeline.

# Development and DataOps

* [Flyway Community](flyway.md) - Database migration tool that applies versioned SQL or Java migration scripts in order and records which have run.
* [Liquibase Community](liquibase.md) - Database change management tool that tracks, versions and applies schema changes defined in SQL, XML, YAML or JSON changelogs.
* [marimo](marimo.md) - Reactive Python notebook stored as a plain Python file, where changing a cell reruns its dependants, and which can be deployed as an app or run as a script.
* [Project Jupyter (JupyterLab, Notebook, JupyterHub)](jupyter.md) - Interactive notebook environment that combines live code, results and narrative, with JupyterHub providing multi-user servers.
* [SQLFluff](sqlfluff.md) - Linter and auto-formatter for SQL that supports many dialects and dbt or Jinja templating.
* [Streamlit](streamlit.md) - Python framework for building interactive data and AI web applications from scripts without front-end code.
* [Synthetic Data Vault (SDV)](sdv.md) - Python library that learns from real tabular, relational and time-series data and generates synthetic data with similar statistical properties.

# Platform operations

* [HashiCorp Terraform](terraform.md) - Infrastructure-as-code tool that declares infrastructure in HCL and creates, changes and destroys it through providers.
* [OpenTelemetry](opentelemetry.md) - Vendor-neutral standard, SDKs and Collector for producing and exporting traces, metrics and logs from applications and infrastructure.
* [OpenTofu](opentofu.md) - Infrastructure-as-code tool that declares cloud and platform resources in HCL and applies changes through plans, as a fork of Terraform.

# Specialised data types

* [Apache Sedona](apache-sedona.md) - Spatial computing engine that adds geospatial types, functions and spatial joins to Spark, Flink and other engines.
* [GeoParquet](geoparquet.md) - Specification for storing geospatial vector data such as points, lines and polygons in Parquet files with standard metadata.
* [OpenSearch](opensearch.md) - Search and analytics engine for full-text search, log analytics and vector search, with dashboards for visualisation.
* [PostGIS](postgis.md) - PostgreSQL extension that adds spatial types, spatial indexes and hundreds of geospatial functions.
