# IBM

# Ingestion and integration

* [Confluent Cloud](confluent-cloud.md) - Fully managed Apache Kafka service on AWS, Azure and Google Cloud, with managed connectors, Schema Registry, Stream Governance and cluster linking.
* [Confluent Platform](confluent-platform.md) - Self-managed Kafka distribution for on-premises and private cloud, with connectors, Schema Registry, Flink and management tooling.
* [Confluent Tableflow](confluent-tableflow.md) - Materialises Kafka topics and their schemas as Apache Iceberg or Delta Lake tables, taking care of type conversion, schema evolution, compaction and catalogue sync.
* [IBM Data Replication](ibm-data-replication.md) - Log-based change data capture that replicates changes from Db2, Db2 for z/OS, Oracle, SQL Server and other databases to databases, Kafka and lakehouse targets.
* [IBM StreamSets](ibm-streamsets.md) - Low-code streaming and batch ingestion tool whose pipelines detect and adapt to schema drift, deployable as SaaS or in the customer's cloud or data centre.
* [WarpStream](warpstream.md) - Kafka-compatible streaming service that runs as stateless agents in the customer's cloud account and writes data directly to object storage, managed by Confluent.

# Processing and transformation

* [Confluent Cloud for Apache Flink](confluent-cloud-flink.md) - Serverless Apache Flink service for continuous SQL and Table API processing over Kafka topics, with autoscaling and built-in functions.
* [IBM watsonx.data integration](ibm-watsonx-data-integration.md) - Integration product with one control plane for batch ETL and ELT, streaming pipelines, change data replication, unstructured data preparation and pipeline observability, with an agent that builds pipelines from natural language.
* [Spark engine in IBM watsonx.data](ibm-watsonx-data-spark.md) - Managed Apache Spark engine in watsonx.data for data engineering, table maintenance and ML pipelines on lakehouse tables.

# Query and compute

* [IBM Netezza Performance Server](ibm-netezza.md) - MPP data warehouse, now offered as a cloud service and on appliances, that can also read and write Iceberg tables shared with watsonx.data.
* [IBM watsonx.data](ibm-watsonx-data.md) - Open lakehouse service that runs Presto, Spark, OpenSearch and Cassandra engines over Iceberg, Delta and Hive tables in object storage with shared catalogues and access policies.
* [Presto (C++) engine in IBM watsonx.data](ibm-watsonx-data-presto.md) - Distributed SQL engine in watsonx.data for interactive analytics and federation across lakehouse tables and external databases.

# Serving and activation

* [IBM Astra DB (DataStax)](ibm-astra-db.md) - Managed Apache Cassandra database with vector search, offered as the operational NoSQL engine in watsonx.data and as a standalone service.
* [IBM Db2](ibm-db2.md) - IBM's relational database for transactional and analytical workloads, available on Linux, Unix, Windows and z/OS, self-managed or as managed services, with vector support and AI-driven tuning.

# Generative AI

* [Confluent Intelligence](confluent-intelligence.md) (preview) - Confluent Cloud's AI layer. It runs event-driven agents on Flink, serves the latest topic state to external agents over MCP, and applies built-in ML functions and model calls to streams.
* [IBM watsonx Orchestrate](ibm-watsonx-orchestrate.md) - Agent platform for building agents, orchestrating IBM and third-party agents and tools, and tracing, evaluating and governing them from one control plane.
* [IBM watsonx.ai](ibm-watsonx-ai.md) - Studio and runtime for foundation models and ML, including Prompt Lab, model tuning, AutoAI, notebooks, RAG tooling and deployment of models and AI services through APIs.
* [OpenSearch and OpenRAG in IBM watsonx.data](ibm-watsonx-data-opensearch-openrag.md) - Vector and keyword search engine in watsonx.data, with OpenRAG tooling for document processing, hybrid search and agentic retrieval for grounding AI applications.

# Metadata and discovery

* [IBM Manta Data Lineage](ibm-manta-data-lineage.md) - Automated lineage service that scans code, ETL tools, databases and BI reports to build column-level, end-to-end lineage across more than 50 technologies.
* [IBM watsonx.data intelligence](ibm-watsonx-data-intelligence.md) - Governance product that catalogues structured and unstructured data with business terms, classifications, policies, quality scores and lineage, and uses AI to enrich metadata.

# Data quality and observability

* [Data observability in IBM watsonx.data integration](ibm-data-observability.md) - Monitoring of pipeline runs and datasets for failures, durations, row-count and quality deviations and missed freshness SLAs, with alert routing and root cause analysis.
* [Data quality in IBM watsonx.data intelligence](ibm-watsonx-data-intelligence-quality.md) - Profiling, rule definitions, anomaly detection and quality scores for catalogued data, with remediation ranked by downstream impact.

# Governance and compliance

* [IBM watsonx.governance](ibm-watsonx-governance.md) - AI governance product that inventories AI use cases and models, including detected unapproved use, maps them to regulations, monitors them and records evidence and decisions.

# Security and access

* [IBM Guardium Data Security Center](ibm-guardium-data-security-center.md) - Data security suite that discovers and classifies sensitive data, monitors database activity, assesses vulnerabilities, detects risky behaviour and manages cryptography.

# Data sharing and collaboration

* [IBM Data Product Hub](ibm-data-product-hub.md) - Marketplace in watsonx.data intelligence where producers package data with business meaning, quality, ownership and contracts, and consumers find and request it.

# Development and DataOps

* [IBM InfoSphere Optim](ibm-optim.md) - Tools for archiving application data and creating masked, subsetted test data from production databases.

# Platform operations

* [IBM Software Hub (Cloud Pak for Data)](ibm-software-hub.md) - Red Hat OpenShift-based platform for installing and running IBM data and AI services, including watsonx.data, watsonx.ai and data intelligence, on premises or in any cloud.
