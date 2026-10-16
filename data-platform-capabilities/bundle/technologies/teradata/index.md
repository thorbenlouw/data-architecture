# Teradata

# Storage and table management

* [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](teradata-open-table-format.md) - Ability for the Teradata engine to read and write Apache Iceberg and Delta Lake tables in object storage through external catalogues, alongside Native Object Store access to Parquet, CSV and JSON files.

# Processing and transformation

* [Teradata Elastic Python Compute](teradata-elastic-python-compute.md) - Managed, distributed Python environment based on Ray that runs ML, AI and data engineering code on CPUs or GPUs next to Teradata Database and open-format tables.

# Query and compute

* [Teradata Cloud](teradata-cloud.md) - Teradata-managed deployment of the platform on AWS, Azure and Google Cloud, combining always-on active compute with elastic compute that scales on demand over database and object-storage data.
* [Teradata Database](teradata-database.md) - Shared-nothing MPP SQL database engine that underlies all Teradata deployments, with mixed-workload management, temporal tables and support for semi-structured data.
* [Teradata Fabric](teradata-fabric.md) - Query federation layer that joins data across Teradata systems and other engines such as Hive, Spark SQL, Oracle and BigQuery, pushing processing to where the data sits.

# Machine learning development

* [Teradata in-database analytics functions](teradata-in-database-analytics.md) - Large library of SQL functions for data preparation, statistics, machine learning, time-series and path analysis that run in parallel inside the database, also callable from Python and R.

# ML operations

* [Teradata Bring Your Own Model (BYOM)](teradata-byom.md) - Database functions that score externally trained models, such as ONNX and PMML, in parallel inside Teradata without exporting data.
* [Teradata ModelOps](teradata-modelops.md) - Model lifecycle service that validates, deploys and monitors in-database and imported models, with drift alerts, a feature catalogue and audit trails of the data used.

# Generative AI

* [Teradata Enterprise AgentStack](teradata-agentstack.md) (preview) - Suite for building, running and governing AI agents on Teradata, made up of AgentBuilder, Enterprise MCP, AgentEngine and AgentOps.
* [Teradata Enterprise MCP](teradata-enterprise-mcp.md) - Governed MCP server that exposes Teradata data, metadata, analytics, vector store and administration functions to AI agents as tools, bound to each user's identity and database roles.
* [Teradata Enterprise Vector Store](teradata-enterprise-vector-store.md) - Vector storage and retrieval inside the Teradata platform, with hybrid keyword and semantic search across structured data and embeddings of text, images and audio.

# Security and access

* [Teradata Database security (roles, row-level security, encryption)](teradata-security.md) - Built-in database controls for role-based privileges, row-level security constraints, column masking through views and functions, access logging and encryption.

# Development and DataOps

* [Teradata AI Studio](teradata-ai-studio.md) - Umbrella environment for in-database analytics, open Python compute, ModelOps, vector storage and agent tooling on the Teradata platform.
* [Teradata Tera](teradata-tera.md) (preview) - Agentic workspace in which Teradata agents analyse data, write code, tune queries and run multi-step data tasks, grounded in governed metadata, lineage and policies.

# Platform operations

* [Teradata Autonomous Knowledge Platform](teradata-autonomous-knowledge-platform.md) - Umbrella name for Teradata's platform of database, open-format storage access, analytics, vector and agent services, run either as Teradata Cloud or Teradata Factory.
* [Teradata Backup, Archive and Restore and Data Mover](teradata-bar-data-mover.md) - Tools for backing up Teradata systems, restoring them, and copying tables and databases between systems for disaster recovery or environment refresh.
* [Teradata Factory](teradata-factory.md) - On-premises Teradata system on Dell compute and storage with NVIDIA GPUs, running warehouse, lakehouse and AI workloads together inside the customer's data centre.
* [Teradata Viewpoint](teradata-viewpoint.md) - Web console for monitoring Teradata systems, queries, sessions and workloads and for managing workload rules.
