# Microsoft Azure and Fabric

# Ingestion and integration

* [Azure Data Box](azure-data-box.md) - Physical appliances shipped to a site to move terabytes to petabytes of data into Azure Storage offline.
* [Azure Data Factory](azure-data-factory.md) - Managed data integration service for copy activities, mapping data flows on Spark and orchestrated pipelines across cloud and on-premises sources.
* [Azure Event Hubs](azure-event-hubs.md) - A partitioned event streaming service with an Apache Kafka-compatible endpoint, retention up to 90 days and Capture to storage.
* [Azure IoT Hub](azure-iot-hub.md) - A managed hub for secure, bidirectional messaging with millions of devices, with device identity, routing and device twins.
* [Azure IoT Operations](azure-iot-operations.md) - An edge data plane on Arc-enabled Kubernetes with an MQTT broker, OPC UA and other connectors, and data flows that send processed data to the cloud.
* [Azure Logic Apps](azure-logic-apps.md) - Low-code workflow service with hundreds of connectors for application integration, including SFTP and B2B protocols such as AS2 and EDI.
* [Azure Synapse Link for Azure Cosmos DB](azure-synapse-link-cosmos-db.md) (deprecated) - Replicates Cosmos DB containers to an analytical column store queryable from Synapse without ETL.
* [Fabric Copy job](fabric-copy-job.md) - Moves data from many sources to Fabric and other destinations in full, watermark-incremental or CDC mode, without building a pipeline.
* [Fabric Eventstream](fabric-eventstream.md) - No-code capture, transformation and routing of event streams from Event Hubs, Kafka, IoT Hub, database CDC and other sources into Fabric destinations.
* [Fabric open mirroring](fabric-open-mirroring.md) - Lets any application or partner write change data into a landing zone in OneLake, which Fabric merges into mirrored Delta tables.
* [Mirroring in Microsoft Fabric](fabric-mirroring.md) - Continuously replicates operational databases into OneLake as Delta tables, merging changes within seconds to minutes without building pipelines.
* [OneLake shortcut transformations](fabric-onelake-shortcut-transformations.md) - Converts CSV, Parquet, JSON or Excel files behind a shortcut into a managed Delta table and keeps it in step as files are added, changed or deleted.

# Storage and table management

* [Azure Data Lake Storage](azure-data-lake-storage.md) - Blob Storage with a hierarchical namespace, POSIX-style ACLs and hot, cool, cold and archive tiers, used as the lake for most Azure analytics.
* [Fabric Data Warehouse zero-copy table clone](fabric-warehouse-zero-copy-clone.md) - Creates a copy of a warehouse table, at the current or a past point in time, that shares the underlying files with the original.
* [Fabric Delta table optimization and V-Order](fabric-delta-optimisation-v-order.md) - Write-time sorting and compression (V-Order) plus compaction and vacuum operations that keep Fabric Delta tables fast to read.
* [Fabric Lakehouse](fabric-lakehouse.md) - A Fabric item that stores tables and files in OneLake, with Delta Lake tables, optional schemas and an automatic SQL analytics endpoint.
* [Mirrored Azure Databricks Catalog](fabric-mirrored-azure-databricks-catalog.md) - Synchronises Unity Catalog metadata into Fabric and exposes the tables through shortcuts, without copying data.
* [OneLake](fabric-onelake.md) - A single logical data lake per Fabric tenant, built on ADLS Gen2, in which every Fabric item stores its data, with tables held as Delta Parquet.
* [OneLake storage tiers and lifecycle management](fabric-onelake-storage-tiers.md) (preview) - Moves OneLake data between hot, cool and cold tiers using lifecycle policies to lower storage cost.
* [Time travel in Fabric Data Warehouse](fabric-warehouse-time-travel.md) - Queries warehouse tables as they were at an earlier timestamp within a retention window, with read-only warehouse snapshots for stable reporting.

# Processing and transformation

* [AI functions in Fabric](fabric-ai-functions.md) - One-line LLM calls on pandas and PySpark DataFrames, and in T-SQL, to classify, extract, summarise, translate, embed or analyse sentiment.
* [Apache Spark in Microsoft Fabric](fabric-spark.md) - Managed Spark runtime with starter pools, custom pools and a native vectorised execution engine for data engineering and data science jobs.
* [Azure Content Understanding in Foundry Tools](azure-content-understanding.md) - Uses generative models to extract structured fields and descriptions from documents, images, audio and video through configurable analysers.
* [Azure Databricks](azure-databricks.md) (distribution of Databricks) - The Databricks Data Intelligence Platform delivered as a first-party Azure service, billed through Azure and integrated with Entra ID and ADLS.
* [Azure Document Intelligence in Foundry Tools](azure-document-intelligence.md) - Extracts text, layout, tables, key-value pairs and fields from documents using prebuilt and custom models.
* [Azure Stream Analytics](azure-stream-analytics.md) - Serverless stream processing with a SQL-like language, event-time windows, reference data joins and calls to machine learning models.
* [Fabric Dataflow Gen2](fabric-dataflow-gen2.md) - Low-code data preparation using Power Query, with hundreds of connectors and output to lakehouses, warehouses and other destinations.
* [Fabric dbt job](fabric-dbt-job.md) (preview) - Runs dbt Core projects inside a Fabric workspace against Fabric Warehouse, Lakehouse and some external databases, with scheduling and monitoring.
* [Fabric materialized lake views](fabric-materialized-lake-views.md) - Declarative Spark SQL views persisted as Delta tables, refreshed incrementally in dependency order, with optional data quality constraints.
* [Fabric semantic link (SemPy)](fabric-semantic-link.md) - A Python library and Spark connector that lets notebooks read Power BI semantic models, evaluate their measures and use their relationships.
* [Fabric user data functions](fabric-user-data-functions.md) - Serverless Python functions hosted in Fabric, each with a REST endpoint, callable from pipelines, notebooks, Activator rules and Power BI reports.

# Orchestration

* [Azure Event Grid](azure-event-grid.md) - A publish-subscribe event routing service for Azure resource events and custom events, with an MQTT broker for devices.
* [Fabric Apache Airflow job](fabric-apache-airflow-job.md) - Managed Apache Airflow inside Fabric for running Python-defined DAGs without operating the Airflow infrastructure.
* [Fabric Real-Time hub](fabric-real-time-hub.md) - A tenant-wide catalogue of streams and system events (Fabric, OneLake, job and Azure events) that users can discover, subscribe to and route.
* [Pipelines in Fabric Data Factory](fabric-pipelines.md) - Orchestrates activities such as copies, notebooks, dataflows and stored procedures into scheduled or event-triggered workflows.

# Query and compute

* [Azure Data Explorer](azure-data-explorer.md) - A managed Kusto cluster for fast analytical queries over large volumes of log, telemetry and time-series data using KQL.
* [Azure Synapse Analytics](azure-synapse-analytics.md) - Analytics workspace combining dedicated SQL pools (MPP warehouse), serverless SQL over the lake, Apache Spark pools and pipelines.
* [Eventhouse and KQL database](fabric-eventhouse.md) - A Kusto-engine store for high-volume time-based and log data, queried with KQL or T-SQL in seconds, with optional copies of data in OneLake.
* [Fabric Data Warehouse](fabric-data-warehouse.md) - A T-SQL warehouse with multi-table transactions that stores its tables as Delta Parquet in OneLake and scales compute automatically.
* [Microsoft Fabric capacities (F SKUs)](fabric-capacities.md) - Pools of capacity units, bought through Azure in sizes from F2 upwards, that all Fabric workloads in assigned workspaces share.
* [OneLake shortcuts](fabric-onelake-shortcuts.md) - Virtual folders or tables in OneLake that point to data in other Fabric items or in external stores, so it can be used without copying.
* [OneLake table format virtualization (Delta Lake and Apache Iceberg)](fabric-onelake-table-format-virtualisation.md) (unconfirmed) - Generates Iceberg metadata for Delta tables and Delta metadata for Iceberg tables in OneLake, so readers of either format can use the same Parquet files.
* [Power BI Direct Lake](powerbi-direct-lake.md) - A semantic model storage mode that loads Delta tables from OneLake into memory on demand, avoiding scheduled import refreshes and DirectQuery latency.

# Serving and activation

* [Azure Cosmos DB](azure-cosmos-db.md) - A globally distributed NoSQL database with single-digit millisecond reads, multi-region writes, a change feed and vector search.
* [Azure Database for PostgreSQL](azure-database-for-postgresql.md) - Managed PostgreSQL (flexible server) with high availability, read replicas and extensions such as pgvector and DiskANN for vector search.
* [Azure HorizonDB](azure-horizondb.md) (preview) - A cloud-native PostgreSQL-compatible database with disaggregated compute and log-based storage for high scale.
* [Azure SQL Database](azure-sql.md) - Managed SQL Server engine in single database, elastic pool and Hyperscale forms, with Azure SQL Managed Instance for near-full SQL Server compatibility.
* [Cosmos DB in Microsoft Fabric](fabric-cosmos-db.md) - A NoSQL document database on the Azure Cosmos DB engine, managed inside Fabric and copied automatically into OneLake as Delta Parquet.
* [Fabric API for GraphQL](fabric-api-for-graphql.md) - Generates a GraphQL API over warehouses, SQL databases, lakehouse and mirrored database endpoints so applications can query and change data.
* [Fabric SQL analytics endpoint](fabric-sql-analytics-endpoint.md) - An automatically created, read-only T-SQL endpoint over the Delta tables of a lakehouse, mirrored database or SQL database.
* [SQL database in Microsoft Fabric](fabric-sql-database.md) - A SaaS operational database on the Azure SQL Database engine whose tables are replicated automatically into OneLake for analytics.

# Analytics and BI

* [Azure Analysis Services](azure-analysis-services.md) - A managed tabular model server for enterprise semantic models consumed by Power BI, Excel and other tools.
* [Copilot in Power BI](powerbi-copilot.md) - Natural-language assistance that summarises reports, answers data questions, creates report pages and helps write DAX and model descriptions.
* [Fabric Activator](fabric-activator.md) - A no-code rules engine that watches streams, reports and Fabric events per business object and triggers alerts, pipelines, functions or Power Automate flows.
* [Fabric data agent](fabric-data-agent.md) - A configurable conversational agent that answers natural-language questions by generating SQL, DAX or KQL over lakehouses, warehouses, semantic models, Eventhouses and ontologies.
* [Fabric Real-Time Dashboard](fabric-real-time-dashboards.md) - Dashboards built on KQL queries over Eventhouse data, refreshing continuously for operational monitoring.
* [Planning in Fabric IQ](fabric-iq-planning.md) - Budgeting, forecasting and scenario planning with planning sheets and editable tables connected to semantic models and OneLake data.
* [Power BI Analyze in Excel and connected tables](powerbi-excel-integration.md) - Lets Excel users build PivotTables and refreshable tables on live connections to Power BI semantic models, with model security and labels applied.
* [Power BI Embedded](powerbi-embedded.md) - Embeds Power BI reports and dashboards in custom applications, either for an organisation's own users or for external customers without Power BI licences.
* [Power BI paginated reports](powerbi-paginated-reports.md) - Pixel-precise, printable reports built in Power BI Report Builder and rendered to PDF, Excel, Word and other formats.
* [Power BI Q&A](powerbi-q-and-a.md) (deprecated) - The earlier natural-language query feature that answers typed questions about a semantic model with visuals.
* [Power BI reports and dashboards](powerbi-reports.md) - Interactive reports authored in Power BI Desktop or the web and shared in the Power BI service, with apps, subscriptions and data alerts.
* [Power BI scorecards and goals](powerbi-scorecards.md) - Tracks business goals against targets, with owners, status rules and check-ins, linked to values in reports or entered manually.
* [Power BI semantic models](powerbi-semantic-models.md) - Tabular models (VertiPaq/Analysis Services engine) holding tables, relationships, DAX measures, hierarchies and row-level security for reporting.

# Machine learning development

* [Automated machine learning (AutoML) in Azure Machine Learning](azure-ml-automl.md) - Tries algorithms, features and settings automatically for tabular, forecasting, vision and text tasks and returns ranked models.
* [Azure Machine Learning](azure-machine-learning.md) - A managed service for training models on CPU and GPU clusters or serverless compute, with jobs, sweeps and pipelines.
* [Azure Machine Learning data labeling](azure-ml-data-labeling.md) - Manages image and text labelling projects with human labellers and ML-assisted pre-labelling.
* [Azure Machine Learning managed feature store](azure-ml-managed-feature-store.md) - Defines feature sets as code, materialises them to offline and online stores, and retrieves point-in-time correct training data.
* [Azure Machine Learning registries and MLflow tracking](azure-ml-registries-mlflow.md) - Tracks runs, parameters and metrics with MLflow and versions models, environments and components in workspace or cross-workspace registries.
* [Azure Machine Learning Responsible AI dashboard](azure-ml-responsible-ai-dashboard.md) - Assesses models with error analysis, feature importance explanations, fairness metrics and counterfactuals before release.
* [Data Science in Microsoft Fabric](fabric-data-science.md) - Notebook-based machine learning with MLflow experiments, a model registry, AutoML and batch scoring with the PREDICT function.

# ML operations

* [Azure Machine Learning model monitoring](azure-ml-model-monitoring.md) - Monitors deployed models for data drift, prediction drift, data quality and performance against ground truth, with alerts.
* [Azure Machine Learning online and batch endpoints](azure-ml-endpoints.md) - Deploys models to managed real-time endpoints with traffic splitting and mirroring, or to batch endpoints that score large datasets.

# Generative AI

* [Azure AI Content Safety](azure-ai-content-safety.md) - Classifies text and images for harmful content and detects prompt injection, jailbreaks and ungrounded output, used by Foundry guardrails.
* [Azure AI Search](azure-ai-search.md) - A search service offering full-text, vector, hybrid and multimodal retrieval with indexers, integrated vectorisation and agentic retrieval.
* [Azure API Management](azure-api-management.md) - An API gateway for publishing, securing and rate-limiting APIs, including AI gateway policies for model token limits, load balancing and logging.
* [Azure Machine Learning prompt flow](azure-prompt-flow.md) (deprecated) - A visual and code tool in Foundry and Azure Machine Learning for building, testing and deploying LLM flows and prompt variants.
* [Azure OpenAI in Foundry Models](azure-openai.md) - OpenAI language, reasoning, embedding, image, video and audio models hosted in Azure under Azure data handling, networking and SLAs.
* [Fabric MCP server](fabric-mcp-server.md) - A Model Context Protocol server that gives AI coding assistants and agents access to Fabric APIs, item definitions and OneLake.
* [Fabric operations agent](fabric-operations-agent.md) - An agent that monitors Eventhouse or ontology data against goals and rules, and recommends or runs actions through Teams with approval.
* [Foundry Agent Service](azure-foundry-agent-service.md) - A managed runtime for prompt-based and hosted code agents with tools, MCP connections, threads and publishing to Teams and Microsoft 365 Copilot.
* [Foundry IQ](azure-foundry-iq.md) - A managed knowledge layer that unifies retrieval over Azure AI Search indexes, SharePoint, Fabric IQ, web and other sources behind knowledge bases for agents.
* [Microsoft Agent Framework](azure-agent-framework.md) - An open-source SDK for .NET and Python for building agents and graph-based multi-agent workflows across model providers.
* [Microsoft Foundry](azure-foundry.md) - Azure's platform for building generative AI applications and agents, combining a model catalogue, agent runtime, tools, evaluation and governance in projects.
* [Microsoft Foundry evaluations](azure-foundry-evaluations.md) - Scores model and agent outputs with built-in and custom evaluators for quality, groundedness and safety, offline or continuously in production.
* [Microsoft Foundry observability and tracing](azure-foundry-observability.md) - Captures OpenTelemetry traces of agent and model calls with latency, token use and tool steps, stored in Application Insights.

# Metadata and discovery

* [Azure Schema Registry in Event Hubs](azure-event-hubs-schema-registry.md) - Stores and versions Avro and JSON schemas for event producers and consumers with compatibility checks.
* [Data lineage in Microsoft Purview](purview-lineage.md) - Shows how data flows between sources, processes and targets across Azure Data Factory, Synapse, Databricks, Fabric, Power BI and other systems.
* [Microsoft Purview Data Map](purview-data-map.md) - Scans on-premises, multicloud and SaaS sources to harvest schemas, classifications and lineage into a metadata graph with Apache Atlas-compatible APIs.
* [Microsoft Purview Unified Catalog](purview-unified-catalog.md) - A business-facing data governance catalogue organised by governance domains, with glossary terms, critical data elements, OKRs and health management.
* [OneLake catalog](fabric-onelake-catalog.md) - The Fabric catalogue for finding, understanding, governing and securing items, with Explore, Govern and Secure views.

# Data quality and observability

* [Microsoft Purview Data Quality](purview-data-quality.md) - Profiles data and runs out-of-the-box, custom and AI-suggested quality rules on data products, rolling scores up to products and domains.

# Governance and compliance

* [Azure AI Language PII detection](azure-ai-language-pii.md) - Detects and redacts personal and health information in text and conversations.
* [Azure Policy](azure-policy.md) - Evaluates and enforces rules on Azure resources, such as allowed regions, required encryption or private endpoints, and reports compliance.
* [Fabric domains](fabric-domains.md) - Group workspaces by business area, with subdomains, domain admins and delegated settings, to support data mesh operating models.
* [Foundry Control Plane](azure-foundry-control-plane.md) (preview) - A fleet-wide view of agents, models and tools with inventory, compliance status, guardrail policies and health across Foundry projects.
* [Microsoft Priva](purview-priva.md) - Privacy tooling that finds personal data, flags privacy risks such as overexposure and transfers, and manages subject rights requests.
* [Microsoft Purview Compliance Manager](purview-compliance-manager.md) - Maps regulatory requirements to improvement actions and Microsoft controls, and tracks evidence and a compliance score.
* [Microsoft Purview Data Lifecycle Management](purview-data-lifecycle-management.md) - Applies retention policies and labels that keep or delete content for set periods, with records management for regulated items.
* [Microsoft Purview Information Protection](purview-information-protection.md) - Sensitivity labels applied manually or automatically to files, emails and Fabric and Power BI items, with encryption and inheritance downstream.

# Security and access

* [Azure Key Vault](azure-key-vault.md) - Stores secrets, keys and certificates with access control, rotation and HSM backing, including Managed HSM for single-tenant keys.
* [Azure Private Link](azure-private-link.md) - Exposes Azure PaaS services through private endpoints inside a virtual network so traffic stays off the public internet.
* [Customer-managed keys for Fabric workspaces](fabric-customer-managed-keys.md) - Encrypts all OneLake data in a workspace with a key held in Azure Key Vault, so revoking the key blocks access.
* [Data security posture management in Microsoft Defender for Cloud](azure-defender-for-cloud-dspm.md) - Discovers sensitive data in cloud storage and databases across Azure, AWS and GCP by sampling, and shows attack paths and exposures that put it at risk.
* [Fabric workspace identity](fabric-workspace-identity.md) - A Microsoft Entra identity managed by Fabric for a workspace, used to authenticate to ADLS, Event Hubs and other sources without stored secrets.
* [Fabric workspace outbound access protection](fabric-outbound-access-protection.md) - Blocks Fabric items in a workspace from connecting to destinations other than approved managed private endpoints or connections.
* [Microsoft Entra ID](azure-entra-id.md) - Microsoft's cloud identity service providing single sign-on, conditional access, managed identities, groups and access governance for Azure, Fabric and Microsoft 365.
* [Microsoft on-premises and virtual network data gateways](fabric-data-gateways.md) - Gateways that let Fabric and Power BI reach data sources inside private or on-premises networks without opening them to the internet.
* [Microsoft Purview Audit](purview-audit.md) - Records user and admin activity across Microsoft 365, Fabric and Power BI into a searchable unified audit log.
* [Microsoft Purview Data Loss Prevention](purview-data-loss-prevention.md) - Detects sensitive information in Microsoft 365, endpoints and Fabric items and raises policy tips, alerts or access restrictions.
* [Microsoft Purview Data Security Posture Management](purview-dspm.md) - Finds sensitive data and oversharing risks across Microsoft 365, AI apps and agents and connected third-party stores, and recommends DLP, labelling and insider risk policies.
* [Microsoft Purview Insider Risk Management](purview-insider-risk-management.md) - Correlates user activity signals to detect and investigate risky behaviour such as data theft or leaks by people inside the organisation.
* [OneLake security](fabric-onelake-security.md) - Role-based access rules defined once on OneLake data, down to table, folder, row and column, and enforced across Fabric engines.
* [Private links for Microsoft Fabric](fabric-private-links.md) - Restricts inbound access to a Fabric tenant or to individual workspaces through Azure Private Link, with managed virtual networks for Spark.

# Data sharing and collaboration

* [Azure Confidential Clean Rooms](azure-confidential-clean-rooms.md) (preview) - Lets several organisations run approved Spark SQL analytics over combined datasets inside attested trusted execution environments without exposing raw data.
* [Azure Data Share](azure-data-share.md) - Shares snapshots of storage and SQL data, or in-place Azure Data Explorer databases, with other Azure tenants under provider control.
* [External data sharing in Microsoft Fabric](fabric-external-data-sharing.md) - Shares lakehouse, warehouse and database data in place with users in another Fabric tenant, who receive a read-only shortcut.

# Data products

* [Data products in Microsoft Purview Unified Catalog](purview-data-products.md) - Groups related tables, files and reports into a published data product with owners, terms of use and an access request and approval workflow.

# Development and DataOps

* [Copilot in Fabric](fabric-copilot.md) (preview) - Generative AI assistance across Fabric workloads for writing code, SQL, KQL, pipeline expressions and Dataflow steps from natural language.
* [Fabric deployment pipelines](fabric-deployment-pipelines.md) - Promote workspace content through two to ten stages such as development, test and production, with item pairing and deployment rules.
* [Fabric Git integration](fabric-git-integration.md) - Connects a workspace to a branch in Azure DevOps, GitHub or GitHub Enterprise so item definitions can be committed, branched and updated.
* [Fabric notebooks](fabric-notebooks.md) - Browser-based notebooks for PySpark, Scala, Spark SQL, R and single-node Python, with scheduling, collaboration and Copilot assistance.
* [Fabric variable library](fabric-variable-library.md) - A workspace item holding variables with value sets per stage, consumed by pipelines, notebooks, shortcuts, dataflows and other items.
* [fabric-cicd](fabric-cicd-library.md) - A Microsoft-maintained Python library for deploying Fabric item definitions from a Git repository to target workspaces with environment-specific parameters.

# Platform operations

* [Azure Backup](azure-backup.md) - Managed backup with vaults, policies and retention for VMs, SQL and PostgreSQL databases, blobs and other Azure workloads.
* [Azure carbon optimization](azure-carbon-optimization.md) - Reports estimated carbon emissions of Azure resources and subscriptions and suggests reductions.
* [Azure Monitor](azure-monitor.md) - Collects metrics, logs and traces from Azure resources and applications into Log Analytics and Application Insights for querying, dashboards and alerts.
* [Bicep](azure-bicep.md) - A declarative language that compiles to Azure Resource Manager templates for deploying Azure resources as code.
* [Fabric workspace monitoring](fabric-workspace-monitoring.md) (preview) - Collects logs and metrics from warehouses, pipelines, Eventhouses, semantic models and other items into a KQL database for querying and alerting.
* [Fabric workspaces](fabric-workspaces.md) - Containers for Fabric items with their own roles, capacity assignment, Git connection and network settings.
* [Microsoft Cost Management](azure-cost-management.md) - Analyses Azure spend by subscription, resource and tag, with budgets, alerts, exports and Advisor savings recommendations.
* [Microsoft Fabric Capacity Metrics app](fabric-capacity-metrics-app.md) - A Power BI app that reports capacity unit consumption by workspace, item and operation, including throttling and storage.
* [OneLake disaster recovery](fabric-onelake-disaster-recovery.md) - A capacity setting that replicates OneLake data asynchronously to the Azure paired region so it can be read after a regional failover.
* [Power BI Report Server](powerbi-report-server.md) - An on-premises server for publishing Power BI and paginated reports where cloud services cannot be used.
* [Terraform Provider for Microsoft Fabric](fabric-terraform-provider.md) - A Terraform provider for creating and managing Fabric capacities, workspaces, items, role assignments and related resources as code.

# Specialised data types

* [Azure Maps](azure-maps.md) - Geospatial APIs and SDKs for rendering maps, geocoding, routing, traffic, weather and time zones.
* [Fabric IQ ontology](fabric-iq-ontology.md) (preview) - Defines business entity types, properties, relationships, rules and metrics and binds them to OneLake data, giving people and agents a shared business vocabulary.
* [Graph in Microsoft Fabric](fabric-graph.md) - A graph store and query engine over OneLake data that models nodes and edges and queries them with ISO GQL or natural language.
* [Maps in Microsoft Fabric](fabric-maps.md) (preview) - A geospatial visualisation item for static and streaming location data held in Fabric.
