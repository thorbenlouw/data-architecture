# Cloudera

# Ingestion and integration

* [Cloudera Data Flow](cloudera-data-flow.md) - Managed Apache NiFi service for building, deploying and autoscaling flows that collect, route and transform data from files, databases, APIs and streams.
* [Cloudera Streams Messaging](cloudera-streams-messaging.md) - Cloudera's Apache Kafka distribution with Schema Registry, Streams Messaging Manager, Streams Replication Manager and Cruise Control.

# Storage and table management

* [Apache Iceberg in Cloudera](cloudera-lakehouse-iceberg.md) - Native Apache Iceberg v2 table support across Spark, Hive, Impala, Trino, Flink and NiFi, including time travel, partition evolution and row-level changes.
* [Apache Ozone in Cloudera](cloudera-ozone.md) - S3-compatible, scale-out object store for on-premises Cloudera clusters, intended to replace HDFS for very large file counts.
* [Cloudera Iceberg REST Catalog](cloudera-iceberg-rest-catalog.md) - Implementation of the Iceberg REST catalogue API on the Hive Metastore that lets external engines read Cloudera-governed Iceberg tables using short-lived, scoped storage credentials.
* [Cloudera Lakehouse Optimizer](cloudera-lakehouse-optimizer.md) - Policy-driven service that schedules and runs Iceberg table maintenance such as compaction, snapshot expiry and statistics collection.

# Processing and transformation

* [Cloudera Base on premises](cloudera-base-on-premises.md) - The on-premises cluster platform with Cloudera Runtime (HDFS, Ozone, Hive, Impala, Spark, Kafka, HBase and others) managed by Cloudera Manager.
* [Cloudera Data Engineering](cloudera-data-engineering.md) - Containerised, autoscaling Apache Spark service with job management and an embedded Apache Airflow for orchestrating pipelines.
* [Cloudera Streaming Analytics](cloudera-streaming-analytics.md) - Apache Flink distribution with SQL Stream Builder, a console for writing continuous SQL jobs and materialised views over streams.

# Query and compute

* [Cloudera Data Warehouse](cloudera-data-warehouse.md) - Containerised SQL service in which teams create isolated, autoscaling Virtual Warehouses running Impala, Hive LLAP or Trino over shared data lake tables.

# Serving and activation

* [Cloudera Operational Database](cloudera-operational-database.md) - Autoscaling Apache HBase service with Apache Phoenix SQL for low-latency reads and writes on large, sparse operational datasets.

# Analytics and BI

* [Cloudera Data Visualization](cloudera-data-visualization.md) - Built-in BI tool for dashboards and applications over Cloudera warehouses and AI projects, including an AI visual that answers natural-language questions.

# Machine learning development

* [Cloudera AI Registry](cloudera-ai-registry.md) - Central registry that stores model versions and metadata from AI Workbench and makes them available for deployment to the AI Inference service.

# ML operations

* [Cloudera AI Inference service](cloudera-ai-inference-service.md) - Kubernetes-based serving for predictive models and large language models, using NVIDIA NIM and Triton, with REST endpoints, monitoring and canary rollouts.

# Generative AI

* [Cloudera AI Agent Studio](cloudera-agent-studio.md) (preview) - Low-code studio inside Cloudera AI for building, testing and deploying multi-agent workflows that call tools, including tools registered from MCP servers.
* [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](cloudera-ai-studios.md) (preview) - Low-code applications in Cloudera AI for building retrieval-augmented chat over documents, fine-tuning open models and generating synthetic datasets.

# Metadata and discovery

* [Cloudera Data Catalog](cloudera-data-catalog.md) - Catalogue service over SDX metadata for searching assets, viewing Atlas lineage and running profilers that collect statistics and detect sensitive data.
* [Cloudera Data Lineage](cloudera-data-lineage.md) - SaaS metadata and lineage service that harvests ETL tools, databases and BI reports to map dependencies across systems inside and outside Cloudera.

# Security and access

* [Cloudera Shared Data Experience (SDX)](cloudera-sdx.md) - Common security and governance layer, built on Apache Ranger, Apache Atlas and Apache Knox, applied to every engine on the same data.

# Development and DataOps

* [Cloudera AI Workbench](cloudera-ai-workbench.md) - Containerised data science environment with projects, sessions in Jupyter or other editors, experiments, jobs, model endpoints and hosted applications on CPUs or GPUs.

# Platform operations

* [Cloudera Anywhere Cloud](cloudera-anywhere-cloud.md) (unconfirmed) - A central control plane that provisions and manages Cloudera data and AI services across public clouds, sovereign clouds and customer data centres, with uniform governance.
* [Cloudera Data Services on premises](cloudera-data-services-on-premises.md) - Kubernetes-based deployment of the Data Engineering, Data Warehouse and Cloudera AI services on customer infrastructure, attached to a Cloudera Base cluster.
* [Cloudera Observability](cloudera-observability.md) - Monitoring and analysis service for Cloudera workloads that shows job and query performance, recommends fixes and reports resource use and cost by workload.
* [Cloudera on cloud](cloudera-on-cloud.md) - Cloudera's platform running in the customer's AWS, Azure or Google Cloud account, with a Cloudera-hosted Management Console that creates environments, data lakes and Data Hub clusters.
* [Cloudera Replication Manager](cloudera-replication-manager.md) - Service that schedules replication of HDFS, Hive, Iceberg and HBase data and metadata between clusters and to cloud storage.
