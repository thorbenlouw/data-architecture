---
type: Platform
id: platform-databricks
title: Databricks
description: A multi-cloud data and AI platform built on Apache Spark, Delta Lake and Unity Catalog.
vendor: Databricks
resource: https://www.databricks.com/
folder: databricks
order: 5
terminology:
  ai-agents: Agent Bricks
  ai-assisted-development: Genie Code
  ai-gateway: Unity Gateway
  ci-cd: Declarative Automation Bundles
  conversational-analytics: Genie Agents and Genie One
  cost-attribution: Serverless usage policies and tags
  dashboards-reports: AI/BI dashboards
  data-anomaly-detection: Data quality monitoring anomaly detection
  data-applications: Databricks Apps
  data-marketplace: Databricks Marketplace
  data-profiling: Data profiling (formerly Lakehouse Monitoring)
  data-quality-rules: Expectations
  declarative-pipelines: Lakeflow pipelines (Spark Declarative Pipelines)
  engine-interoperability: Iceberg reads (UniForm) and the Iceberg REST Catalog API
  external-data-sharing: OpenSharing
  file-ingestion: Auto Loader
  foundation-model-access: Foundation Model APIs (model services)
  genai-evaluation: Agent Evaluation
  genai-observability: MLflow Tracing
  low-code-transformation: Lakeflow Designer
  managed-storage: Unity Catalog managed tables and default storage
  model-registry: Models in Unity Catalog
  operational-database: Lakebase
  partitioning-clustering: Liquid clustering
  query-federation: Lakehouse Federation
  real-time-analytics: Lakehouse Real-Time
  saas-connectors: Lakeflow Connect managed connectors
  secrets-management: Secrets in Unity Catalog
  semantic-layer: Unity Catalog metric views
  streaming-ingestion: Zerobus Ingest
  system-telemetry: System tables
  table-catalogue: Unity Catalog metastore
  table-maintenance: Predictive optimization
  unstructured-data: Unity Catalog volumes
  vector-search: AI Search
  version-control: Git folders
  workflow-orchestration: Lakeflow Jobs
  workload-isolation: Lakeguard (user-code isolation) and separate warehouses
families:
- name: Lakeflow
  aliases: [Databricks Lakeflow]
  technologies:
  - databricks-lakeflow-connect
  - databricks-zerobus-ingest
  - databricks-lakeflow-pipelines
  - databricks-pipeline-expectations
  - databricks-lakeflow-jobs
  - databricks-lakeflow-designer
- name: Agent Bricks
  aliases: [Mosaic AI, Databricks Mosaic AI]
  technologies:
  - databricks-agent-bricks
  - databricks-agent-runtime
  - databricks-agent-evaluation
  - databricks-knowledge-assistant-supervisor-agent
  - databricks-ai-search
  - databricks-model-serving
  - databricks-foundation-model-apis
  - databricks-ai-runtime
  - databricks-managed-mcp-servers
  - databricks-mlflow-tracing
  - databricks-unity-gateway
- name: Unity Catalog
  aliases: [UC]
  technologies:
  - databricks-unity-catalog
  - databricks-unity-catalog-managed-tables
  - databricks-managed-iceberg-tables
  - databricks-volumes
  - databricks-unity-catalog-functions
  - databricks-models-in-unity-catalog
  - databricks-secrets-in-unity-catalog
  - databricks-abac
  - databricks-governed-tags
  - databricks-data-classification
  - databricks-unity-catalog-lineage
  - databricks-catalog-explorer
  - databricks-discover
  - databricks-metric-views
  - databricks-iceberg-rest-catalog
  - databricks-catalog-federation
  - databricks-lakehouse-federation
  - databricks-unity-gateway
- name: Genie
  aliases: [Databricks Genie]
  technologies: [databricks-genie-one, databricks-genie-agents, databricks-genie-code]
- name: Databricks AI/BI
  aliases: [AI/BI]
  technologies: [databricks-ai-bi-dashboards, databricks-genie-agents]
- name: Databricks SQL
  aliases: [DBSQL]
  technologies:
  - databricks-sql
  - databricks-sql-warehouses
  - databricks-lakehouse-real-time
  - databricks-photon
  - databricks-sql-alerts
  - databricks-sql-drivers
- name: OpenSharing
  technologies: [databricks-opensharing, databricks-marketplace, databricks-clean-rooms]
- name: Databricks Machine Learning
  aliases: [Databricks ML]
  technologies:
  - databricks-managed-mlflow
  - databricks-models-in-unity-catalog
  - databricks-feature-store
  - databricks-feature-views
  - databricks-online-feature-store
  - databricks-automl
  - databricks-inference-tables
  - databricks-ai-runtime
- name: Databricks data quality monitoring
  aliases: [Lakehouse Monitoring]
  technologies: [databricks-data-profiling, databricks-dqm-anomaly-detection]
- name: Delta Lake on Databricks
  technologies:
  - databricks-delta-lake
  - databricks-liquid-clustering
  - databricks-change-data-feed
  - databricks-table-clone
  - databricks-iceberg-reads-uniform
  - databricks-predictive-optimization
  - databricks-variant
- name: Databricks compute
  technologies:
  - databricks-classic-compute
  - databricks-serverless-compute
  - databricks-sql-warehouses
  - databricks-ai-runtime
  - databricks-photon
  - databricks-lakeguard
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Databricks is a lakehouse platform on AWS, Azure and Google Cloud, marketed as the Data Intelligence Platform. Data sits in Delta Lake and Apache Iceberg tables in cloud object storage, either in the customer's buckets or in Databricks-managed default storage, and Unity Catalog governs tables, volumes, functions, models and AI services across the workspaces of an account. Compute comes as classic clusters in the customer's cloud account, serverless compute in Databricks' account, and SQL warehouses in serverless, pro or classic form, with Photon as the native execution engine.

The data offering is grouped into product families. Lakeflow (Connect, pipelines, Jobs and Designer) covers ingestion, transformation and orchestration. Databricks SQL and AI/BI (dashboards and Genie Agents) cover warehousing and analytics, with Genie One as the business-user interface and Genie Code as the coding agent. Lakebase provides managed Postgres next to the lakehouse. Agent Bricks groups the AI tooling, including Model Serving, Foundation Model APIs, AI Search, Agent Runtime and Agent Evaluation, alongside managed MLflow, the feature store and Unity Gateway. OpenSharing, Marketplace and Clean Rooms handle sharing, and Databricks Apps hosts applications next to the data.

# Notes

- Many products were renamed in 2025-26: Delta Live Tables became Lakeflow pipelines, Workflows became Lakeflow Jobs, Vector Search became AI Search, Databricks Asset Bundles became Declarative Automation Bundles, Databricks Assistant became Genie Code, Genie spaces became Genie Agents, Databricks One became Genie One and Lakehouse Monitoring became data profiling. The Mosaic AI brand was folded into Agent Bricks in March 2026, and Mosaic AI Gateway is now Unity Gateway.
- Databricks announced OpenSharing on 10 June 2026 as the successor to the Delta Sharing protocol. The [open protocol](../technologies/open-source/delta-sharing.md) is now a Linux Foundation project, and Delta Sharing remains the name of a sub-project within Delta Lake.
- Databricks created several open-source projects that its managed products extend: [Apache Spark](../technologies/open-source/apache-spark.md), [Delta Lake](../technologies/open-source/delta-lake.md), [MLflow](../technologies/open-source/mlflow.md), [Unity Catalog](../technologies/open-source/unity-catalog.md) and [Spark Declarative Pipelines](../technologies/open-source/apache-spark-declarative-pipelines.md).
- Serverless compute runs in Databricks' cloud account and needs Unity Catalog. Serverless workspaces also use Databricks-managed default storage, while classic compute and pro or classic SQL warehouses run in the customer's account.
- Microsoft sells Databricks as the first-party [Azure Databricks](../technologies/microsoft/azure-databricks.md) service, and SAP embeds it in SAP Business Data Cloud as [SAP Databricks](../technologies/sap/sap-databricks.md).
- Databricks has no native reverse ETL, event-streaming broker, master data management or paginated reports. Partners fill these gaps.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 11 of 22 | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 19 of 23 | [Open file formats](../capabilities/storage/file-formats.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 13 of 18 | [Data enrichment](../capabilities/processing/data-enrichment.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 5 of 5 |  |
| [Query and compute](../capabilities/compute/compute.md) | 20 of 22 (+1 in preview) | [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md) (preview only) |
| [Serving and activation](../capabilities/serving/serving.md) | 6 of 13 | [Data APIs](../capabilities/serving/data-apis.md), [Data export](../capabilities/serving/data-export.md), [Decision management](../capabilities/serving/decision-management.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 12 of 20 | [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 16 of 20 | [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 14 of 18 | [Continuous training](../capabilities/mlops/continuous-training.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Edge inference](../capabilities/mlops/edge-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 14 of 23 (+4 in preview) | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md), [Model customisation](../capabilities/generative-ai/model-customisation.md) (preview only), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) (preview only), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md) (preview only), [Agent memory](../capabilities/generative-ai/agent-memory.md) (preview only) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 16 of 20 | [Schema registry](../capabilities/metadata/schema-registry.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 7 of 12 (+2 in preview) | [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data issue management](../capabilities/data-quality/data-issue-management.md) (preview only), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md) (preview only) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 10 of 24 (+1 in preview) | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md) (preview only) |
| [Security and access](../capabilities/security/security.md) | 15 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 8 of 8 |  |
| [Data products](../capabilities/data-products/data-products.md) | 0 of 7 | [Data products](../capabilities/data-products/data-products.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 12 of 16 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 19 of 27 (+1 in preview) | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md) (preview only) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 5 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Product families

- **Lakeflow** (also: Databricks Lakeflow): [Lakeflow Connect](../technologies/databricks/databricks-lakeflow-connect.md), [Zerobus Ingest](../technologies/databricks/databricks-zerobus-ingest.md), [Lakeflow pipelines](../technologies/databricks/databricks-lakeflow-pipelines.md), [Lakeflow pipelines expectations](../technologies/databricks/databricks-pipeline-expectations.md), [Lakeflow Jobs](../technologies/databricks/databricks-lakeflow-jobs.md), [Lakeflow Designer](../technologies/databricks/databricks-lakeflow-designer.md)
- **Agent Bricks** (also: Mosaic AI, Databricks Mosaic AI): [Agent Bricks](../technologies/databricks/databricks-agent-bricks.md), [Databricks Agent Runtime and Agent Bricks CLI](../technologies/databricks/databricks-agent-runtime.md) (preview), [Databricks Agent Evaluation (MLflow GenAI evaluation)](../technologies/databricks/databricks-agent-evaluation.md), [Agent Bricks Knowledge Assistant and Supervisor Agent](../technologies/databricks/databricks-knowledge-assistant-supervisor-agent.md) (deprecated), [Databricks AI Search](../technologies/databricks/databricks-ai-search.md), [Databricks Model Serving](../technologies/databricks/databricks-model-serving.md), [Databricks Foundation Model APIs](../technologies/databricks/databricks-foundation-model-apis.md), [Databricks AI Runtime](../technologies/databricks/databricks-ai-runtime.md) (preview), [Databricks managed MCP servers](../technologies/databricks/databricks-managed-mcp-servers.md) (preview), [MLflow Tracing on Databricks](../technologies/databricks/databricks-mlflow-tracing.md), [Unity Gateway](../technologies/databricks/databricks-unity-gateway.md)
- **Unity Catalog** (also: UC): [Unity Catalog](../technologies/databricks/databricks-unity-catalog.md), [Unity Catalog managed tables](../technologies/databricks/databricks-unity-catalog-managed-tables.md), [Unity Catalog managed Iceberg tables](../technologies/databricks/databricks-managed-iceberg-tables.md), [Unity Catalog volumes](../technologies/databricks/databricks-volumes.md), [Unity Catalog functions (UDFs)](../technologies/databricks/databricks-unity-catalog-functions.md), [Models in Unity Catalog](../technologies/databricks/databricks-models-in-unity-catalog.md), [Secrets in Unity Catalog](../technologies/databricks/databricks-secrets-in-unity-catalog.md), [Unity Catalog attribute-based access control (ABAC)](../technologies/databricks/databricks-abac.md), [Databricks governed tags](../technologies/databricks/databricks-governed-tags.md), [Databricks Data Classification](../technologies/databricks/databricks-data-classification.md), [Unity Catalog data lineage](../technologies/databricks/databricks-unity-catalog-lineage.md), [Databricks Catalog Explorer](../technologies/databricks/databricks-catalog-explorer.md), [Databricks Discover](../technologies/databricks/databricks-discover.md), [Unity Catalog metric views](../technologies/databricks/databricks-metric-views.md), [Unity Catalog Iceberg REST Catalog API](../technologies/databricks/databricks-iceberg-rest-catalog.md), [Databricks catalog federation](../technologies/databricks/databricks-catalog-federation.md), [Lakehouse Federation (query federation)](../technologies/databricks/databricks-lakehouse-federation.md), [Unity Gateway](../technologies/databricks/databricks-unity-gateway.md)
- **Genie** (also: Databricks Genie): [Genie One](../technologies/databricks/databricks-genie-one.md), [Genie Agents](../technologies/databricks/databricks-genie-agents.md), [Genie Code](../technologies/databricks/databricks-genie-code.md)
- **Databricks AI/BI** (also: AI/BI): [Databricks AI/BI dashboards](../technologies/databricks/databricks-ai-bi-dashboards.md), [Genie Agents](../technologies/databricks/databricks-genie-agents.md)
- **Databricks SQL** (also: DBSQL): [Databricks SQL](../technologies/databricks/databricks-sql.md), [Databricks SQL warehouses (serverless, pro and classic)](../technologies/databricks/databricks-sql-warehouses.md), [Databricks Lakehouse Real-Time](../technologies/databricks/databricks-lakehouse-real-time.md) (preview), [Databricks Photon](../technologies/databricks/databricks-photon.md), [Databricks SQL alerts](../technologies/databricks/databricks-sql-alerts.md), [Databricks JDBC, ODBC and ADBC drivers](../technologies/databricks/databricks-sql-drivers.md)
- **OpenSharing**: [Databricks OpenSharing](../technologies/databricks/databricks-opensharing.md), [Databricks Marketplace](../technologies/databricks/databricks-marketplace.md), [Databricks Clean Rooms](../technologies/databricks/databricks-clean-rooms.md)
- **Databricks Machine Learning** (also: Databricks ML): [Managed MLflow on Databricks](../technologies/databricks/databricks-managed-mlflow.md), [Models in Unity Catalog](../technologies/databricks/databricks-models-in-unity-catalog.md), [Databricks Feature Store](../technologies/databricks/databricks-feature-store.md), [Databricks Feature Views](../technologies/databricks/databricks-feature-views.md), [Databricks Online Feature Store](../technologies/databricks/databricks-online-feature-store.md), [Databricks AutoML](../technologies/databricks/databricks-automl.md), [Databricks inference tables](../technologies/databricks/databricks-inference-tables.md), [Databricks AI Runtime](../technologies/databricks/databricks-ai-runtime.md) (preview)
- **Databricks data quality monitoring** (also: Lakehouse Monitoring): [Databricks data profiling](../technologies/databricks/databricks-data-profiling.md), [Databricks data quality monitoring anomaly detection](../technologies/databricks/databricks-dqm-anomaly-detection.md) (preview)
- **Delta Lake on Databricks**: [Delta Lake on Databricks](../technologies/databricks/databricks-delta-lake.md), [Databricks liquid clustering](../technologies/databricks/databricks-liquid-clustering.md), [Databricks change data feed](../technologies/databricks/databricks-change-data-feed.md), [Databricks table clone (shallow and deep clone)](../technologies/databricks/databricks-table-clone.md), [Databricks Iceberg reads (UniForm)](../technologies/databricks/databricks-iceberg-reads-uniform.md), [Databricks predictive optimization](../technologies/databricks/databricks-predictive-optimization.md), [Databricks VARIANT data type](../technologies/databricks/databricks-variant.md)
- **Databricks compute**: [Databricks classic compute (Databricks Runtime clusters)](../technologies/databricks/databricks-classic-compute.md), [Databricks serverless compute](../technologies/databricks/databricks-serverless-compute.md), [Databricks SQL warehouses (serverless, pro and classic)](../technologies/databricks/databricks-sql-warehouses.md), [Databricks AI Runtime](../technologies/databricks/databricks-ai-runtime.md) (preview), [Databricks Photon](../technologies/databricks/databricks-photon.md), [Lakeguard](../technologies/databricks/databricks-lakeguard.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Agent Bricks | [AI agents](../capabilities/generative-ai/ai-agents.md) |
| Agent Evaluation | [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) |
| AI Search | [Vector search](../capabilities/generative-ai/vector-search.md) |
| AI/BI dashboards | [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md) |
| Auto Loader | [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| Data profiling (formerly Lakehouse Monitoring) | [Data profiling](../capabilities/data-quality/data-profiling.md) |
| Data quality monitoring anomaly detection | [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md) |
| Databricks Apps | [Data application hosting](../capabilities/development-lifecycle/data-applications.md) |
| Databricks Marketplace | [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| Declarative Automation Bundles | [CI/CD](../capabilities/development-lifecycle/ci-cd.md) |
| Expectations | [Data quality rules](../capabilities/data-quality/data-quality-rules.md) |
| Foundation Model APIs (model services) | [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |
| Genie Agents and Genie One | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| Genie Code | [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md) |
| Git folders | [Version control integration](../capabilities/development-lifecycle/version-control.md) |
| Iceberg reads (UniForm) and the Iceberg REST Catalog API | [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md) |
| Lakebase | [Operational database integration](../capabilities/serving/operational-database.md) |
| Lakeflow Connect managed connectors | [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md) |
| Lakeflow Designer | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| Lakeflow Jobs | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| Lakeflow pipelines (Spark Declarative Pipelines) | [Declarative pipelines](../capabilities/processing/declarative-pipelines.md) |
| Lakeguard (user-code isolation) and separate warehouses | [Workload isolation](../capabilities/compute/workload-isolation.md) |
| Lakehouse Federation | [Query federation](../capabilities/compute/query-federation.md) |
| Lakehouse Real-Time | [Real-time analytical database](../capabilities/compute/real-time-analytics.md) |
| Liquid clustering | [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md) |
| MLflow Tracing | [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| Models in Unity Catalog | [Model registry](../capabilities/machine-learning/model-registry.md) |
| OpenSharing | [External data sharing](../capabilities/data-sharing/external-data-sharing.md) |
| Predictive optimization | [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md) |
| Secrets in Unity Catalog | [Secrets management](../capabilities/security/secrets-management.md) |
| Serverless usage policies and tags | [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) |
| System tables | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) |
| Unity Catalog managed tables and default storage | [Platform-managed storage](../capabilities/storage/managed-storage.md) |
| Unity Catalog metastore | [Table catalogue](../capabilities/storage/table-catalogue.md) |
| Unity Catalog metric views | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) |
| Unity Catalog volumes | [Unstructured data management](../capabilities/specialised-data/unstructured-data.md) |
| Unity Gateway | [AI gateway](../capabilities/generative-ai/ai-gateway.md) |
| Zerobus Ingest | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |

# Technologies

## Ingestion and integration

- [Databricks Auto Loader](../technologies/databricks/databricks-auto-loader.md): A Structured Streaming source (cloudFiles) that discovers new files in cloud storage and processes each one exactly once, with schema inference, schema evolution and a rescued-data column.
- [Lakeflow Connect](../technologies/databricks/databricks-lakeflow-connect.md): Managed connectors that ingest data incrementally from SaaS applications, databases (including change data capture), file sources and message buses into Unity Catalog tables, running on serverless Lakeflow pipelines.
- [Zerobus Ingest](../technologies/databricks/databricks-zerobus-ingest.md): A serverless push API that writes records straight into Unity Catalog Delta tables. Clients can use gRPC SDKs, REST, OpenTelemetry (OTLP), MQTT or Kafka-compatible producers, and no message broker is needed.

## Storage and table management

- [Databricks catalog federation](../technologies/databricks/databricks-catalog-federation.md): Mounts external catalogues such as Hive metastore, AWS Glue, Snowflake Horizon and Salesforce Data 360 as foreign catalogs, read from object storage under Unity Catalog governance.
- [Databricks liquid clustering](../technologies/databricks/databricks-liquid-clustering.md): A data layout method that clusters table files by key columns you can change at any time, replacing partitioning and Z-ordering. With CLUSTER BY AUTO, Databricks chooses the keys from query history.
- [Databricks predictive optimization](../technologies/databricks/databricks-predictive-optimization.md): Runs OPTIMIZE, VACUUM and ANALYZE automatically on Unity Catalog managed tables and chooses liquid clustering keys, based on how each table is used.
- [Databricks table clone (shallow and deep clone)](../technologies/databricks/databricks-table-clone.md): Copies a table at a given version. A shallow clone copies only metadata and points at the source files, while a deep clone copies the data as well.
- [Databricks VARIANT data type](../technologies/databricks/databricks-variant.md): A binary type for semi-structured data such as JSON that is queried without a fixed schema, with shredding into columns for faster reads.
- [Delta Lake on Databricks](../technologies/databricks/databricks-delta-lake.md): Databricks' managed implementation of Delta Lake tables, with ACID commits, MERGE, UPDATE and DELETE, schema enforcement, time travel, deletion vectors and type widening.
- [Unity Catalog](../technologies/databricks/databricks-unity-catalog.md): The account-wide catalogue and governance layer for tables, volumes, functions, models, AI services and connections. It provides a three-level namespace, SQL privileges, audit and workspace bindings.
- [Unity Catalog managed Iceberg tables](../technologies/databricks/databricks-managed-iceberg-tables.md): Apache Iceberg tables (v1 to v3) that Unity Catalog manages, with compaction, snapshot expiry and liquid clustering. Databricks and external engines can read and write them through the Iceberg REST catalogue.
- [Unity Catalog managed tables](../technologies/databricks/databricks-unity-catalog-managed-tables.md): Delta or Iceberg tables whose storage location, file layout, maintenance and lifecycle Unity Catalog manages, including on Databricks-managed default storage.

## Processing and transformation

- [Databricks AI Functions](../technologies/databricks/databricks-ai-functions.md): SQL and Python functions that call models over table data. They include ai_query, ai_extract, ai_classify, ai_summarize, ai_translate, ai_mask, ai_forecast and ai_similarity, with ai_search, ai_prep_search and ai_transcribe in Beta.
- [Databricks ai_parse_document](../technologies/databricks/databricks-ai-parse-document.md): An AI Function that extracts text, tables and layout elements from PDFs, images and office documents stored in volumes, returning structured output.
- [Lakeflow Designer](../technologies/databricks/databricks-lakeflow-designer.md): A visual, no-code canvas where analysts build data preparation flows from operators or natural-language prompts. The flows are backed by generated code governed in Unity Catalog.
- [Lakeflow pipelines](../technologies/databricks/databricks-lakeflow-pipelines.md): A declarative framework in which you define streaming tables, materialised views and flows in SQL or Python. The platform then works out dependencies, incremental refresh, retries and infrastructure.
- [Unity Catalog functions (UDFs)](../technologies/databricks/databricks-unity-catalog-functions.md): SQL, Python, Scala and Java user-defined functions registered and governed in Unity Catalog. They run on serverless and standard compute with sandboxing.

## Orchestration

- [Lakeflow Jobs](../technologies/databricks/databricks-lakeflow-jobs.md): Built-in orchestrator that runs dependency graphs of notebooks, pipelines, SQL, dbt and other tasks on schedules or on file-arrival, table-update and continuous triggers, with retries and loops.

## Query and compute

- [Databricks AI Runtime](../technologies/databricks/databricks-ai-runtime.md) (preview): Serverless GPU compute for deep learning, used to train and fine-tune models on one or many GPUs with PyTorch DDP and FSDP, DeepSpeed or Ray.
- [Databricks classic compute (Databricks Runtime clusters)](../technologies/databricks/databricks-classic-compute.md): All-purpose and job clusters, plus instance pools, running Databricks Runtime in the customer's cloud account. You choose instance types, autoscaling and access mode.
- [Databricks Free Edition](../technologies/databricks/databricks-free-edition.md): A no-cost, serverless-only, quota-limited Databricks environment for learning and experiments. It includes notebooks, SQL, Lakeflow, dashboards, Genie, Genie Code and Lakebase.
- [Databricks Iceberg reads (UniForm)](../technologies/databricks/databricks-iceberg-reads-uniform.md): Generates Iceberg metadata asynchronously for Delta tables so that Iceberg clients can read them without copying the data.
- [Databricks Lakehouse Real-Time](../technologies/databricks/databricks-lakehouse-real-time.md) (preview): A serverless SQL warehouse type tuned for sub-second reads of Unity Catalog tables by many concurrent users and applications.
- [Databricks Photon](../technologies/databricks/databricks-photon.md): Databricks' native C++ vectorised execution engine. It runs Spark SQL and DataFrame operations on columnar batches and falls back to Spark for operations it does not support.
- [Databricks serverless compute](../technologies/databricks/databricks-serverless-compute.md): Databricks-managed, versionless compute for notebooks, jobs and pipelines. It starts quickly, scales automatically and is billed in DBUs per use.
- [Databricks SQL](../technologies/databricks/databricks-sql.md): The data warehousing product on the lakehouse. It includes the SQL editor, queries, ANSI SQL engine, SQL transformations, materialised views and BI connectivity, running on SQL warehouses.
- [Databricks SQL warehouses (serverless, pro and classic)](../technologies/databricks/databricks-sql-warehouses.md): Compute for Databricks SQL in serverless, pro or classic form. Serverless warehouses start in seconds and use intelligent workload management to scale and queue queries.
- [Lakehouse Federation (query federation)](../technologies/databricks/databricks-lakehouse-federation.md): Read-only queries against external databases such as PostgreSQL, Oracle, SQL Server, Snowflake, BigQuery, Redshift and Teradata through Unity Catalog foreign catalogs, with query pushdown.
- [Unity Catalog Iceberg REST Catalog API](../technologies/databricks/databricks-iceberg-rest-catalog.md): An Iceberg REST catalogue endpoint with credential vending. Spark, Flink, Trino, Snowflake and other engines can use it to read and write Unity Catalog tables.

## Serving and activation

- [Databricks change data feed](../technologies/databricks/databricks-change-data-feed.md): Records row-level inserts, updates and deletes on Delta tables so downstream jobs and streams can read only the changes.
- [Databricks JDBC, ODBC and ADBC drivers](../technologies/databricks/databricks-sql-drivers.md): Client drivers and connectors (JDBC, ODBC, ADBC, Python, Go and Node.js) plus the SQL Statement Execution REST API, used to query Databricks SQL warehouses from tools and code.
- [Lakebase](../technologies/databricks/databricks-lakebase.md): Fully managed Postgres in the Databricks platform. Compute is separate from storage, and it offers autoscaling, scale-to-zero, copy-on-write branching, instant point-in-time restore and read replicas.

## Analytics and BI

- [Databricks AI/BI dashboards](../technologies/databricks/databricks-ai-bi-dashboards.md): Built-in dashboards with AI-assisted authoring, cross-filtering and drill-through. They can be shared at account level, sent on schedules by email or Slack, and embedded in external applications.
- [Databricks Excel Add-in](../technologies/databricks/databricks-excel-add-in.md): A Microsoft Excel add-in for querying governed Databricks tables and metric views from a workbook.
- [Databricks SQL alerts](../technologies/databricks/databricks-sql-alerts.md): Scheduled queries that evaluate a condition and send email, Slack or webhook notifications when it is met.
- [Genie Agents](../technologies/databricks/databricks-genie-agents.md): Domain-specific chat interfaces that analysts curate with tables, metric views, example SQL and instructions. They answer business questions in natural language with SQL, tables and charts.
- [Genie One](../technologies/databricks/databricks-genie-one.md): A simplified interface for business users that combines chat across governed data, dashboards and apps in one place, available in the browser, desktop, Excel and Google Sheets.
- [Unity Catalog metric views](../technologies/databricks/databricks-metric-views.md): YAML- or SQL-defined semantic objects that keep measures apart from dimensions. They are registered in Unity Catalog and queried from SQL, dashboards, Genie and external BI tools.

## Machine learning development

- [Databricks AutoML](../technologies/databricks/databricks-automl.md): Generates baseline classification, regression and forecasting models through a UI or Python API, and produces editable notebooks for each trial.
- [Databricks Feature Store](../technologies/databricks/databricks-feature-store.md): A feature registry in Unity Catalog that stores features in primary-keyed Delta tables, with point-in-time training set creation, automatic lookup at inference and lineage to models.
- [Databricks Feature Views](../technologies/databricks/databricks-feature-views.md): Declarative feature definitions, including time-windowed aggregations over batch, streaming and request-time data, for which Databricks builds and runs the pipelines.
- [Databricks Online Feature Store](../technologies/databricks/databricks-online-feature-store.md): A Lakebase-backed store that publishes feature tables for millisecond lookups by Model Serving endpoints and feature serving endpoints.
- [Managed MLflow on Databricks](../technologies/databricks/databricks-managed-mlflow.md): MLflow 3 hosted by Databricks, with experiment and run tracking, logged models, prompt management and deployment jobs, all integrated with Unity Catalog permissions and lineage.
- [Models in Unity Catalog](../technologies/databricks/databricks-models-in-unity-catalog.md): The MLflow model registry hosted in Unity Catalog, with versions, aliases, permissions, tags and lineage to training data and features shared across workspaces.

## ML operations

- [Databricks inference tables](../technologies/databricks/databricks-inference-tables.md): Logs requests and responses from serving endpoints, foundation model calls and agents to Unity Catalog Delta tables for monitoring, audit and retraining.
- [Databricks Model Serving](../technologies/databricks/databricks-model-serving.md): Serverless CPU and GPU endpoints for serving custom MLflow models, Databricks-hosted foundation models and external models in real time, with traffic splitting between model versions.

## Generative AI

- [Agent Bricks](../technologies/databricks/databricks-agent-bricks.md): Databricks' platform for developing agents. It brings together agent hosting, sandboxed code execution, memory, MCP tools, retrieval, tracing, evaluation and governed model access.
- [Agent Bricks Knowledge Assistant and Supervisor Agent](../technologies/databricks/databricks-knowledge-assistant-supervisor-agent.md) (deprecated): No-code agents. Knowledge Assistant answers questions over documents with citations, and Supervisor Agent coordinates Genie Agents, tables, AI Search indexes, MCP servers and other agents.
- [Databricks Agent Evaluation (MLflow GenAI evaluation)](../technologies/databricks/databricks-agent-evaluation.md): Evaluates agents and LLM applications against datasets, using built-in and custom scorers, LLM judges and human feedback, and also monitors production traces.
- [Databricks Agent Runtime and Agent Bricks CLI](../technologies/databricks/databricks-agent-runtime.md) (preview): Serverless hosting for code-based agents on Databricks Apps, with durable run state, an authenticated endpoint, a service-principal identity and MLflow tracing, deployed with the agentbricks CLI.
- [Databricks AI Search](../technologies/databricks/databricks-ai-search.md): A managed vector and full-text search service. Delta Sync indexes stay in step with source tables and can compute embeddings, and hybrid retrieval is supported.
- [Databricks Foundation Model APIs](../technologies/databricks/databricks-foundation-model-apis.md): Databricks-hosted proprietary and open language and embedding models, available pay-per-token or with provisioned throughput. They are exposed as governed model services in the system.ai schema.
- [Databricks managed MCP servers](../technologies/databricks/databricks-managed-mcp-servers.md) (preview): Hosted Model Context Protocol servers that expose Unity Catalog functions, AI Search indexes, Genie Agents and Genie One to agents as tools. External MCP servers can also be registered as Unity Catalog MCP services.
- [MLflow Tracing on Databricks](../technologies/databricks/databricks-mlflow-tracing.md): Records each step of agent and LLM calls, including inputs, outputs, latency, tokens and feedback, and stores the traces in Unity Catalog tables that can be queried with SQL.
- [Unity Gateway](../technologies/databricks/databricks-unity-gateway.md): A governance and routing layer in Unity Catalog for model, MCP and agent traffic, with provider fallbacks, rate and consumption limits, guardrails, inference logging and budgets.

## Metadata and discovery

- [Databricks Catalog Explorer](../technologies/databricks/databricks-catalog-explorer.md): The workspace UI for browsing and managing Unity Catalog assets. It shows schemas, permissions, lineage, popularity, table health indicators and AI-generated comments.
- [Databricks Discover](../technologies/databricks/databricks-discover.md): A curated browsing page that groups governed tables, dashboards, notebooks and Genie Agents into business domains and subdomains, with highlighted assets chosen by admins and AI recommendations.
- [Unity Catalog data lineage](../technologies/databricks/databricks-unity-catalog-lineage.md): Captures table- and column-level lineage automatically for queries, notebooks, jobs, pipelines, dashboards and models. External sources and BI tools can be registered so they appear in the same graph.

## Data quality and observability

- [Databricks data profiling](../technologies/databricks/databricks-data-profiling.md): Computes profile and drift metrics for a table over time as snapshot, time-series or inference profiles, and stores them in Delta tables with a generated dashboard.
- [Databricks data quality monitoring anomaly detection](../technologies/databricks/databricks-dqm-anomaly-detection.md) (preview): Monitors every table in a schema with one setting. It learns each table's update and volume patterns, flags late or incomplete tables, and suggests root causes using lineage.
- [Lakeflow pipelines expectations](../technologies/databricks/databricks-pipeline-expectations.md): Declarative data quality constraints on pipeline datasets. For each failing record you choose to warn, drop it or fail the update, and the results are recorded in the pipeline event log.

## Governance and compliance

- [Databricks compliance security profile](../technologies/databricks/databricks-compliance-security-profile.md): A workspace setting that applies a hardened, FIPS-validated compute image, enhanced security monitoring and encrypted egress, required for HIPAA, PCI-DSS, FedRAMP and similar regulated data.
- [Databricks Data Classification](../technologies/databricks/databricks-data-classification.md): A serverless agent that scans Unity Catalog tables incrementally, detects sensitive data such as PII and payment-card data, and tags the columns.
- [Databricks governed tags](../technologies/databricks/databricks-governed-tags.md): Account-level tag definitions with controlled values and assignment permissions, applied to Unity Catalog objects and workspace assets and used by ABAC, classification and cost reporting.

## Security and access

- [Databricks automatic identity management](../technologies/databricks/databricks-automatic-identity-management.md): Synchronises users, groups and service principals from Microsoft Entra ID or Okta on demand, without configuring SCIM provisioning. It works alongside SSO, OAuth and service principals.
- [Databricks customer-managed keys](../technologies/databricks/databricks-customer-managed-keys.md): Customer-held cloud KMS keys that encrypt control-plane data (notebooks, secrets, queries), workspace storage and, at catalogue level, Unity Catalog managed data.
- [Databricks Governance Hub](../technologies/databricks/databricks-governance-hub.md) (preview): An account-level console that brings together data health and governance coverage, tag usage, AI usage and spend, and cost drivers, with recommended actions.
- [Databricks serverless egress control](../technologies/databricks/databricks-serverless-egress-control.md): Account-level network policies that limit which destinations serverless compute, apps and model serving can reach, used with network connectivity configurations and private endpoint rules.
- [Lakeguard](../technologies/databricks/databricks-lakeguard.md): Isolation technology that sandboxes each user's code and UDFs away from the Spark engine and from other users, so shared compute can enforce Unity Catalog row filters and column masks.
- [Private Link for Databricks](../technologies/databricks/databricks-private-link.md): AWS PrivateLink, Azure Private Link and Private Service Connect connectivity for front-end access, classic compute to the control plane, and inbound access to serverless services such as Lakebase and Zerobus Ingest.
- [Secrets in Unity Catalog](../technologies/databricks/databricks-secrets-in-unity-catalog.md): Credentials stored as governed Unity Catalog securables under a catalog.schema.secret name, with grants and audit.
- [Unity Catalog attribute-based access control (ABAC)](../technologies/databricks/databricks-abac.md): Policies attached at catalogue, schema or table level that use governed tags and user attributes to apply row filters, column masks and dynamic grants automatically.

## Data sharing and collaboration

- [Databricks Clean Rooms](../technologies/databricks/databricks-clean-rooms.md): Isolated serverless environments where up to ten organisations share data through OpenSharing and run notebooks that every party has approved. No party sees the others' underlying data.
- [Databricks Marketplace](../technologies/databricks/databricks-marketplace.md): An exchange for publishing and finding datasets, AI models, notebooks, apps and MCP servers, either publicly or through private exchanges, delivered with OpenSharing.
- [Databricks OpenSharing](../technologies/databricks/databricks-opensharing.md): Live sharing of tables, views, materialised views, metric views, volumes, models and notebooks with other Databricks accounts, or tabular data with any client through an open protocol, without copying.

## Development and DataOps

- [Databricks Apps](../technologies/databricks/databricks-apps.md): Serverless hosting for Python and Node.js web applications (for example Streamlit, Dash, Gradio and React) that run inside the workspace with Unity Catalog, SQL warehouse and OAuth integration.
- [Databricks Connect](../technologies/databricks/databricks-connect.md): A client library built on Spark Connect. Python, Scala and R DataFrame code written in an IDE or application runs on remote Databricks compute, including serverless.
- [Databricks Declarative Automation Bundles](../technologies/databricks/databricks-declarative-automation-bundles.md): A Databricks CLI feature that defines jobs, pipelines, dashboards, apps, serving endpoints, AI Search, Lakebase and other resources in YAML with per-target settings. The CLI then validates, plans and deploys them from CI/CD.
- [Databricks Git folders](../technologies/databricks/databricks-git-folders.md): Workspace folders backed by a Git repository. Users clone, branch, commit, merge and resolve conflicts from the UI, the API or Git CLI commands.
- [Databricks notebooks](../technologies/databricks/databricks-notebooks.md): Collaborative notebooks with Python, SQL, Scala and R cells, comments, version history, widgets and visualisations that can be scheduled as jobs.
- [Genie Code](../technologies/databricks/databricks-genie-code.md): An AI coding and data agent in notebooks, the SQL editor, the pipelines editor, dashboards and MLflow. It plans, writes and runs code, fixes errors and builds pipelines and dashboards, using Unity Catalog context and the user's permissions.

## Platform operations

- [Databricks agentic code converter](../technologies/databricks/databricks-agentic-code-converter.md) (preview): A Genie Code-based migration project that converts T-SQL, Snowflake, Redshift, Oracle, BigQuery and Teradata SQL into Databricks SQL or DataFrame notebooks.
- [Databricks budgets](../technologies/databricks/databricks-budgets.md): Account-level spend tracking at list price, filtered by workspace, resource type and tags. You set monthly thresholds with email alerts and, for Unity Gateway, optional per-user blocking.
- [Databricks managed disaster recovery](../technologies/databricks/databricks-managed-disaster-recovery.md) (preview): Replicates Unity Catalog metadata, managed table data and workspace assets to a secondary region, behind a stable URL that survives failover.
- [Databricks serverless usage policies](../technologies/databricks/databricks-serverless-usage-policies.md) (preview): Sets of tags applied automatically to the serverless usage of the users assigned to a policy, so that spend from notebooks, jobs, pipelines, serving, apps and Lakebase can be attributed.
- [Databricks system tables](../technologies/databricks/databricks-system-tables.md): Databricks-hosted tables in the system catalog that cover billing, audit, lineage, compute, query history, jobs, pipelines, serving, MLflow, classification, data quality and Lakebase activity.
- [Databricks Terraform provider](../technologies/databricks/databricks-terraform-provider.md): A Terraform provider (databricks/databricks) that manages workspaces, Unity Catalog objects, permissions, compute, jobs and other Databricks resources as code.
- [Lakebridge](../technologies/databricks/databricks-lakebridge.md): A Databricks Labs migration toolkit. It assesses legacy warehouse and ETL estates, transpiles their SQL and ETL code to Databricks, and reconciles the migrated data against the source.

## Specialised data types

- [Databricks spatial SQL (GEOMETRY and GEOGRAPHY)](../technologies/databricks/databricks-spatial-sql.md): Native GEOMETRY and GEOGRAPHY types with ST_ functions for constructing, measuring, relating and transforming spatial data, plus H3 functions.
- [Unity Catalog volumes](../technologies/databricks/databricks-volumes.md): Governed, path-addressable storage for non-tabular files such as documents, images, libraries and landing data. Volumes can be managed or external.

