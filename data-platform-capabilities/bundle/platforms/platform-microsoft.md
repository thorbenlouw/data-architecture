---
type: Platform
id: platform-microsoft
title: Microsoft Azure and Fabric
description: Microsoft's Azure services plus Fabric, its SaaS analytics platform, together with Power BI and Purview.
vendor: Microsoft
resource: https://www.microsoft.com/microsoft-fabric
folder: microsoft
order: 2
terminology:
  access-requests: Data product access policies (Purview)
  ai-functions: AI functions
  ai-guardrails: Guardrails and controls (formerly content filters)
  batch-ingestion: Copy job / Copy activity
  conversational-analytics: Copilot in Power BI; Fabric data agent
  data-alerting: Activator
  data-catalogue: OneLake catalog (Fabric); Unified Catalog (Purview)
  data-certification: Endorsement (promoted, certified, master data)
  data-classification: Sensitivity labels and classifications
  data-security-posture: DSPM
  database-replication: Mirroring
  declarative-pipelines: Materialized lake views
  environment-promotion: Deployment pipelines
  event-streaming: Eventstream; Event Hubs
  foundation-model-access: Foundry Models
  internal-data-sharing: OneLake shortcuts
  knowledge-graphs: Ontology (Fabric IQ)
  low-code-transformation: Dataflow Gen2 (Power Query)
  materialised-views: Materialized lake views (lakehouse); materialized views (Warehouse)
  metric-definitions: DAX measures; scorecard goals
  multi-tenancy: Workspaces and domains
  provisioned-compute: Capacity (F SKU)
  query-federation: Shortcuts and metadata mirroring
  real-time-analytics: Eventhouse / KQL database
  retrieval-augmented-generation: Foundry IQ knowledge bases; agentic retrieval
  semantic-layer: Semantic model (formerly dataset)
  system-telemetry: Capacity Metrics app; workspace monitoring
  table-catalogue: Lakehouse (schemas) in OneLake
  workflow-orchestration: Pipelines
families:
- name: Fabric Data Factory
  aliases: [Data Factory in Microsoft Fabric]
  technologies: [fabric-pipelines, fabric-copy-job, fabric-dataflow-gen2, fabric-apache-airflow-job, fabric-dbt-job]
- name: Fabric Data Engineering
  aliases: [Synapse Data Engineering]
  technologies:
  - fabric-lakehouse
  - fabric-spark
  - fabric-notebooks
  - fabric-materialized-lake-views
  - fabric-delta-optimisation-v-order
- name: Fabric Data Warehouse
  aliases: [Synapse Data Warehouse]
  technologies:
  - fabric-data-warehouse
  - fabric-sql-analytics-endpoint
  - fabric-warehouse-time-travel
  - fabric-warehouse-zero-copy-clone
- name: Fabric Databases
  technologies:
  - fabric-sql-database
  - fabric-cosmos-db
  - fabric-mirroring
  - fabric-open-mirroring
  - fabric-mirrored-azure-databricks-catalog
- name: Microsoft Fabric Real-Time Intelligence
  aliases: [Real-Time Intelligence, RTI, Synapse Real-Time Analytics]
  technologies:
  - fabric-eventstream
  - fabric-eventhouse
  - fabric-activator
  - fabric-real-time-dashboards
  - fabric-real-time-hub
  - fabric-maps
- name: Fabric IQ
  technologies: [fabric-iq-ontology, fabric-iq-planning, fabric-graph, fabric-data-agent, fabric-operations-agent]
- name: OneLake
  technologies:
  - fabric-onelake
  - fabric-onelake-shortcuts
  - fabric-onelake-shortcut-transformations
  - fabric-onelake-catalog
  - fabric-onelake-security
  - fabric-onelake-disaster-recovery
  - fabric-onelake-storage-tiers
  - fabric-onelake-table-format-virtualisation
- name: Power BI
  technologies:
  - powerbi-reports
  - powerbi-semantic-models
  - powerbi-direct-lake
  - powerbi-copilot
  - powerbi-paginated-reports
  - powerbi-embedded
  - powerbi-scorecards
  - powerbi-excel-integration
  - powerbi-q-and-a
  - powerbi-report-server
- name: Microsoft Purview
  aliases: [Azure Purview]
  technologies:
  - purview-unified-catalog
  - purview-data-map
  - purview-data-products
  - purview-data-quality
  - purview-lineage
  - purview-information-protection
  - purview-data-loss-prevention
  - purview-dspm
  - purview-insider-risk-management
  - purview-data-lifecycle-management
  - purview-audit
  - purview-compliance-manager
  - purview-priva
- name: Microsoft Foundry
  aliases: [Azure AI Foundry]
  technologies:
  - azure-foundry
  - azure-foundry-agent-service
  - azure-foundry-iq
  - azure-foundry-evaluations
  - azure-foundry-observability
  - azure-foundry-control-plane
  - azure-openai
- name: Foundry Tools
  aliases: [Azure AI services]
  technologies:
  - azure-ai-content-safety
  - azure-ai-language-pii
  - azure-content-understanding
  - azure-document-intelligence
- name: Azure Machine Learning
  aliases: [Azure ML]
  technologies:
  - azure-machine-learning
  - azure-ml-automl
  - azure-ml-data-labeling
  - azure-ml-endpoints
  - azure-ml-managed-feature-store
  - azure-ml-model-monitoring
  - azure-ml-registries-mlflow
  - azure-ml-responsible-ai-dashboard
  - azure-prompt-flow
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Microsoft's data offering centres on Microsoft Fabric, a SaaS analytics platform billed by capacity. Its workloads (Data Factory, Data Engineering, Data Warehouse, Databases, Real-Time Intelligence, Data Science, Fabric IQ and Power BI) share workspaces, capacities and security, and all store data in OneLake, a single logical lake per tenant in which tables are held as Delta Parquet. Microsoft Purview supplies cataloguing, data quality, information protection, data loss prevention and compliance tooling across Fabric, Azure, Microsoft 365 and other clouds.

Azure provides the platform services used with or instead of Fabric, such as Azure Data Lake Storage, Event Hubs, Azure SQL, Cosmos DB, Azure Data Explorer, Azure Data Factory, Azure Synapse Analytics and Azure Machine Learning. Microsoft Foundry is the platform for models, agents, evaluation and AI governance, and the former Azure AI services are now sold as Foundry Tools. Azure Databricks is a first-party Azure service that runs the Databricks platform.

# Notes

- Microsoft recommends Fabric for new analytics work. Azure Synapse Analytics and Azure Data Factory remain supported but receive little new development; Synapse Data Explorer was retired in October 2025 and Synapse Link for Cosmos DB closed to new accounts in March 2026, with Fabric mirroring as the replacement.
- A Fabric capacity (F SKU) is a fixed pool of capacity units shared by every workload in its assigned workspaces, paid per second or reserved, with smoothing of short bursts. Users never manage clusters, but cost behaves like provisioned compute; separate capacities are the main way to isolate workloads and budgets, and Spark can also bill pay-as-you-go outside the capacity.
- Several products overlap by design: Eventstream and Event Hubs, Eventhouse and Azure Data Explorer (the same Kusto engine), Fabric Data Factory and Azure Data Factory, the OneLake catalog and Purview Unified Catalog, and Purview DSPM and Defender for Cloud DSPM. The Fabric item usually suits Fabric-centred estates; the Azure service suits dedicated deployments in a customer's own subscription.
- Renames to translate include the Fabric workloads dropping their "Synapse" prefix in 2024 (Synapse Real-Time Analytics became Real-Time Intelligence), Data Activator becoming Activator, Power BI datasets becoming semantic models, Azure AI Foundry becoming Microsoft Foundry and Azure Active Directory becoming Microsoft Entra ID.
- Fabric IQ groups the ontology, graph, planning, data agents and operations agents into a semantic and agent layer over OneLake. Graph and Planning became generally available in mid-2026, while the ontology remained in preview in October 2026.
- Azure Databricks connects to Fabric through mirrored Unity Catalog metadata, OneLake shortcuts and Power BI. Microsoft positions it alongside Fabric for organisations already standardised on Databricks.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 16 of 22 | [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 19 of 23 | [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [Data branching and tagging](../capabilities/storage/data-branching.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 17 of 18 (+1 in preview) | [Transformation as code](../capabilities/processing/transformation-as-code.md) (preview only) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 3 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md) |
| [Query and compute](../capabilities/compute/compute.md) | 19 of 22 | [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Result caching](../capabilities/compute/result-caching.md), [Container services](../capabilities/compute/container-services.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 7 of 13 | [Decision management](../capabilities/serving/decision-management.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 16 of 20 | [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 17 of 20 | [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 16 of 18 | [Continuous training](../capabilities/mlops/continuous-training.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 20 of 23 (+1 in preview) | [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md) (preview only) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 17 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 7 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 17 of 24 (+1 in preview) | [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Policy management](../capabilities/governance/data-policy-management.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md) (preview only) |
| [Security and access](../capabilities/security/security.md) | 18 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 4 of 8 (+1 in preview) | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md) (preview only) |
| [Data products](../capabilities/data-products/data-products.md) | 3 of 7 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 10 of 16 (+1 in preview) | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) (preview only) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 23 of 27 (+1 in preview) | [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) (preview only) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 8 of 10 (+1 in preview) | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) (preview only) |

# Product families

- **Fabric Data Factory** (also: Data Factory in Microsoft Fabric): [Pipelines in Fabric Data Factory](../technologies/microsoft/fabric-pipelines.md), [Fabric Copy job](../technologies/microsoft/fabric-copy-job.md), [Fabric Dataflow Gen2](../technologies/microsoft/fabric-dataflow-gen2.md), [Fabric Apache Airflow job](../technologies/microsoft/fabric-apache-airflow-job.md), [Fabric dbt job](../technologies/microsoft/fabric-dbt-job.md) (preview)
- **Fabric Data Engineering** (also: Synapse Data Engineering): [Fabric Lakehouse](../technologies/microsoft/fabric-lakehouse.md), [Apache Spark in Microsoft Fabric](../technologies/microsoft/fabric-spark.md), [Fabric notebooks](../technologies/microsoft/fabric-notebooks.md), [Fabric materialized lake views](../technologies/microsoft/fabric-materialized-lake-views.md), [Fabric Delta table optimization and V-Order](../technologies/microsoft/fabric-delta-optimisation-v-order.md)
- **Fabric Data Warehouse** (also: Synapse Data Warehouse): [Fabric Data Warehouse](../technologies/microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../technologies/microsoft/fabric-sql-analytics-endpoint.md), [Time travel in Fabric Data Warehouse](../technologies/microsoft/fabric-warehouse-time-travel.md), [Fabric Data Warehouse zero-copy table clone](../technologies/microsoft/fabric-warehouse-zero-copy-clone.md)
- **Fabric Databases**: [SQL database in Microsoft Fabric](../technologies/microsoft/fabric-sql-database.md), [Cosmos DB in Microsoft Fabric](../technologies/microsoft/fabric-cosmos-db.md), [Mirroring in Microsoft Fabric](../technologies/microsoft/fabric-mirroring.md), [Fabric open mirroring](../technologies/microsoft/fabric-open-mirroring.md), [Mirrored Azure Databricks Catalog](../technologies/microsoft/fabric-mirrored-azure-databricks-catalog.md)
- **Microsoft Fabric Real-Time Intelligence** (also: Real-Time Intelligence, RTI, Synapse Real-Time Analytics): [Fabric Eventstream](../technologies/microsoft/fabric-eventstream.md), [Eventhouse and KQL database](../technologies/microsoft/fabric-eventhouse.md), [Fabric Activator](../technologies/microsoft/fabric-activator.md), [Fabric Real-Time Dashboard](../technologies/microsoft/fabric-real-time-dashboards.md), [Fabric Real-Time hub](../technologies/microsoft/fabric-real-time-hub.md), [Maps in Microsoft Fabric](../technologies/microsoft/fabric-maps.md) (preview)
- **Fabric IQ**: [Fabric IQ ontology](../technologies/microsoft/fabric-iq-ontology.md) (preview), [Planning in Fabric IQ](../technologies/microsoft/fabric-iq-planning.md), [Graph in Microsoft Fabric](../technologies/microsoft/fabric-graph.md), [Fabric data agent](../technologies/microsoft/fabric-data-agent.md), [Fabric operations agent](../technologies/microsoft/fabric-operations-agent.md)
- **OneLake**: [OneLake](../technologies/microsoft/fabric-onelake.md), [OneLake shortcuts](../technologies/microsoft/fabric-onelake-shortcuts.md), [OneLake shortcut transformations](../technologies/microsoft/fabric-onelake-shortcut-transformations.md), [OneLake catalog](../technologies/microsoft/fabric-onelake-catalog.md), [OneLake security](../technologies/microsoft/fabric-onelake-security.md), [OneLake disaster recovery](../technologies/microsoft/fabric-onelake-disaster-recovery.md), [OneLake storage tiers and lifecycle management](../technologies/microsoft/fabric-onelake-storage-tiers.md) (preview), [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../technologies/microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed)
- **Power BI**: [Power BI reports and dashboards](../technologies/microsoft/powerbi-reports.md), [Power BI semantic models](../technologies/microsoft/powerbi-semantic-models.md), [Power BI Direct Lake](../technologies/microsoft/powerbi-direct-lake.md), [Copilot in Power BI](../technologies/microsoft/powerbi-copilot.md), [Power BI paginated reports](../technologies/microsoft/powerbi-paginated-reports.md), [Power BI Embedded](../technologies/microsoft/powerbi-embedded.md), [Power BI scorecards and goals](../technologies/microsoft/powerbi-scorecards.md), [Power BI Analyze in Excel and connected tables](../technologies/microsoft/powerbi-excel-integration.md), [Power BI Q&A](../technologies/microsoft/powerbi-q-and-a.md) (deprecated), [Power BI Report Server](../technologies/microsoft/powerbi-report-server.md)
- **Microsoft Purview** (also: Azure Purview): [Microsoft Purview Unified Catalog](../technologies/microsoft/purview-unified-catalog.md), [Microsoft Purview Data Map](../technologies/microsoft/purview-data-map.md), [Data products in Microsoft Purview Unified Catalog](../technologies/microsoft/purview-data-products.md), [Microsoft Purview Data Quality](../technologies/microsoft/purview-data-quality.md), [Data lineage in Microsoft Purview](../technologies/microsoft/purview-lineage.md), [Microsoft Purview Information Protection](../technologies/microsoft/purview-information-protection.md), [Microsoft Purview Data Loss Prevention](../technologies/microsoft/purview-data-loss-prevention.md), [Microsoft Purview Data Security Posture Management](../technologies/microsoft/purview-dspm.md), [Microsoft Purview Insider Risk Management](../technologies/microsoft/purview-insider-risk-management.md), [Microsoft Purview Data Lifecycle Management](../technologies/microsoft/purview-data-lifecycle-management.md), [Microsoft Purview Audit](../technologies/microsoft/purview-audit.md), [Microsoft Purview Compliance Manager](../technologies/microsoft/purview-compliance-manager.md), [Microsoft Priva](../technologies/microsoft/purview-priva.md)
- **Microsoft Foundry** (also: Azure AI Foundry): [Microsoft Foundry](../technologies/microsoft/azure-foundry.md), [Foundry Agent Service](../technologies/microsoft/azure-foundry-agent-service.md), [Foundry IQ](../technologies/microsoft/azure-foundry-iq.md), [Microsoft Foundry evaluations](../technologies/microsoft/azure-foundry-evaluations.md), [Microsoft Foundry observability and tracing](../technologies/microsoft/azure-foundry-observability.md), [Foundry Control Plane](../technologies/microsoft/azure-foundry-control-plane.md) (preview), [Azure OpenAI in Foundry Models](../technologies/microsoft/azure-openai.md)
- **Foundry Tools** (also: Azure AI services): [Azure AI Content Safety](../technologies/microsoft/azure-ai-content-safety.md), [Azure AI Language PII detection](../technologies/microsoft/azure-ai-language-pii.md), [Azure Content Understanding in Foundry Tools](../technologies/microsoft/azure-content-understanding.md), [Azure Document Intelligence in Foundry Tools](../technologies/microsoft/azure-document-intelligence.md)
- **Azure Machine Learning** (also: Azure ML): [Azure Machine Learning](../technologies/microsoft/azure-machine-learning.md), [Automated machine learning (AutoML) in Azure Machine Learning](../technologies/microsoft/azure-ml-automl.md), [Azure Machine Learning data labeling](../technologies/microsoft/azure-ml-data-labeling.md), [Azure Machine Learning online and batch endpoints](../technologies/microsoft/azure-ml-endpoints.md), [Azure Machine Learning managed feature store](../technologies/microsoft/azure-ml-managed-feature-store.md), [Azure Machine Learning model monitoring](../technologies/microsoft/azure-ml-model-monitoring.md), [Azure Machine Learning registries and MLflow tracking](../technologies/microsoft/azure-ml-registries-mlflow.md), [Azure Machine Learning Responsible AI dashboard](../technologies/microsoft/azure-ml-responsible-ai-dashboard.md), [Azure Machine Learning prompt flow](../technologies/microsoft/azure-prompt-flow.md) (deprecated)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Activator | [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md) |
| AI functions | [AI functions in SQL](../capabilities/processing/ai-functions.md) |
| Capacity (F SKU) | [Provisioned compute](../capabilities/compute/provisioned-compute.md) |
| Capacity Metrics app; workspace monitoring | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) |
| Copilot in Power BI; Fabric data agent | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| Copy job / Copy activity | [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md) |
| Data product access policies (Purview) | [Access requests and reviews](../capabilities/security/access-requests.md) |
| Dataflow Gen2 (Power Query) | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| DAX measures; scorecard goals | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) |
| Deployment pipelines | [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) |
| DSPM | [Data security posture management](../capabilities/security/data-security-posture.md) |
| Endorsement (promoted, certified, master data) | [Data certification](../capabilities/metadata/data-certification.md) |
| Eventhouse / KQL database | [Real-time analytical database](../capabilities/compute/real-time-analytics.md) |
| Eventstream; Event Hubs | [Event streaming](../capabilities/ingestion-integration/event-streaming.md) |
| Foundry IQ knowledge bases; agentic retrieval | [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) |
| Foundry Models | [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |
| Guardrails and controls (formerly content filters) | [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| Lakehouse (schemas) in OneLake | [Table catalogue](../capabilities/storage/table-catalogue.md) |
| Materialized lake views | [Declarative pipelines](../capabilities/processing/declarative-pipelines.md) |
| Materialized lake views (lakehouse); materialized views (Warehouse) | [Materialised views](../capabilities/compute/materialised-views.md) |
| Mirroring | [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md) |
| OneLake catalog (Fabric); Unified Catalog (Purview) | [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| OneLake shortcuts | [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md) |
| Ontology (Fabric IQ) | [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |
| Pipelines | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| Semantic model (formerly dataset) | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) |
| Sensitivity labels and classifications | [Data classification](../capabilities/governance/data-classification.md) |
| Shortcuts and metadata mirroring | [Query federation](../capabilities/compute/query-federation.md) |
| Workspaces and domains | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |

# Technologies

## Ingestion and integration

- [Azure Data Box](../technologies/microsoft/azure-data-box.md): Physical appliances shipped to a site to move terabytes to petabytes of data into Azure Storage offline.
- [Azure Data Factory](../technologies/microsoft/azure-data-factory.md): Managed data integration service for copy activities, mapping data flows on Spark and orchestrated pipelines across cloud and on-premises sources.
- [Azure Event Hubs](../technologies/microsoft/azure-event-hubs.md): A partitioned event streaming service with an Apache Kafka-compatible endpoint, retention up to 90 days and Capture to storage.
- [Azure IoT Hub](../technologies/microsoft/azure-iot-hub.md): A managed hub for secure, bidirectional messaging with millions of devices, with device identity, routing and device twins.
- [Azure IoT Operations](../technologies/microsoft/azure-iot-operations.md): An edge data plane on Arc-enabled Kubernetes with an MQTT broker, OPC UA and other connectors, and data flows that send processed data to the cloud.
- [Azure Logic Apps](../technologies/microsoft/azure-logic-apps.md): Low-code workflow service with hundreds of connectors for application integration, including SFTP and B2B protocols such as AS2 and EDI.
- [Azure Synapse Link for Azure Cosmos DB](../technologies/microsoft/azure-synapse-link-cosmos-db.md) (deprecated): Replicates Cosmos DB containers to an analytical column store queryable from Synapse without ETL.
- [Fabric Copy job](../technologies/microsoft/fabric-copy-job.md): Moves data from many sources to Fabric and other destinations in full, watermark-incremental or CDC mode, without building a pipeline.
- [Fabric Eventstream](../technologies/microsoft/fabric-eventstream.md): No-code capture, transformation and routing of event streams from Event Hubs, Kafka, IoT Hub, database CDC and other sources into Fabric destinations.
- [Fabric open mirroring](../technologies/microsoft/fabric-open-mirroring.md): Lets any application or partner write change data into a landing zone in OneLake, which Fabric merges into mirrored Delta tables.
- [Mirroring in Microsoft Fabric](../technologies/microsoft/fabric-mirroring.md): Continuously replicates operational databases into OneLake as Delta tables, merging changes within seconds to minutes without building pipelines.
- [OneLake shortcut transformations](../technologies/microsoft/fabric-onelake-shortcut-transformations.md): Converts CSV, Parquet, JSON or Excel files behind a shortcut into a managed Delta table and keeps it in step as files are added, changed or deleted.

## Storage and table management

- [Azure Data Lake Storage](../technologies/microsoft/azure-data-lake-storage.md): Blob Storage with a hierarchical namespace, POSIX-style ACLs and hot, cool, cold and archive tiers, used as the lake for most Azure analytics.
- [Fabric Data Warehouse zero-copy table clone](../technologies/microsoft/fabric-warehouse-zero-copy-clone.md): Creates a copy of a warehouse table, at the current or a past point in time, that shares the underlying files with the original.
- [Fabric Delta table optimization and V-Order](../technologies/microsoft/fabric-delta-optimisation-v-order.md): Write-time sorting and compression (V-Order) plus compaction and vacuum operations that keep Fabric Delta tables fast to read.
- [Fabric Lakehouse](../technologies/microsoft/fabric-lakehouse.md): A Fabric item that stores tables and files in OneLake, with Delta Lake tables, optional schemas and an automatic SQL analytics endpoint.
- [Mirrored Azure Databricks Catalog](../technologies/microsoft/fabric-mirrored-azure-databricks-catalog.md): Synchronises Unity Catalog metadata into Fabric and exposes the tables through shortcuts, without copying data.
- [OneLake](../technologies/microsoft/fabric-onelake.md): A single logical data lake per Fabric tenant, built on ADLS Gen2, in which every Fabric item stores its data, with tables held as Delta Parquet.
- [OneLake storage tiers and lifecycle management](../technologies/microsoft/fabric-onelake-storage-tiers.md) (preview): Moves OneLake data between hot, cool and cold tiers using lifecycle policies to lower storage cost.
- [Time travel in Fabric Data Warehouse](../technologies/microsoft/fabric-warehouse-time-travel.md): Queries warehouse tables as they were at an earlier timestamp within a retention window, with read-only warehouse snapshots for stable reporting.

## Processing and transformation

- [AI functions in Fabric](../technologies/microsoft/fabric-ai-functions.md): One-line LLM calls on pandas and PySpark DataFrames, and in T-SQL, to classify, extract, summarise, translate, embed or analyse sentiment.
- [Apache Spark in Microsoft Fabric](../technologies/microsoft/fabric-spark.md): Managed Spark runtime with starter pools, custom pools and a native vectorised execution engine for data engineering and data science jobs.
- [Azure Content Understanding in Foundry Tools](../technologies/microsoft/azure-content-understanding.md): Uses generative models to extract structured fields and descriptions from documents, images, audio and video through configurable analysers.
- [Azure Databricks](../technologies/microsoft/azure-databricks.md) (distribution of Databricks): The Databricks Data Intelligence Platform delivered as a first-party Azure service, billed through Azure and integrated with Entra ID and ADLS.
- [Azure Document Intelligence in Foundry Tools](../technologies/microsoft/azure-document-intelligence.md): Extracts text, layout, tables, key-value pairs and fields from documents using prebuilt and custom models.
- [Azure Stream Analytics](../technologies/microsoft/azure-stream-analytics.md): Serverless stream processing with a SQL-like language, event-time windows, reference data joins and calls to machine learning models.
- [Fabric Dataflow Gen2](../technologies/microsoft/fabric-dataflow-gen2.md): Low-code data preparation using Power Query, with hundreds of connectors and output to lakehouses, warehouses and other destinations.
- [Fabric dbt job](../technologies/microsoft/fabric-dbt-job.md) (preview): Runs dbt Core projects inside a Fabric workspace against Fabric Warehouse, Lakehouse and some external databases, with scheduling and monitoring.
- [Fabric materialized lake views](../technologies/microsoft/fabric-materialized-lake-views.md): Declarative Spark SQL views persisted as Delta tables, refreshed incrementally in dependency order, with optional data quality constraints.
- [Fabric semantic link (SemPy)](../technologies/microsoft/fabric-semantic-link.md): A Python library and Spark connector that lets notebooks read Power BI semantic models, evaluate their measures and use their relationships.
- [Fabric user data functions](../technologies/microsoft/fabric-user-data-functions.md): Serverless Python functions hosted in Fabric, each with a REST endpoint, callable from pipelines, notebooks, Activator rules and Power BI reports.

## Orchestration

- [Azure Event Grid](../technologies/microsoft/azure-event-grid.md): A publish-subscribe event routing service for Azure resource events and custom events, with an MQTT broker for devices.
- [Fabric Apache Airflow job](../technologies/microsoft/fabric-apache-airflow-job.md): Managed Apache Airflow inside Fabric for running Python-defined DAGs without operating the Airflow infrastructure.
- [Fabric Real-Time hub](../technologies/microsoft/fabric-real-time-hub.md): A tenant-wide catalogue of streams and system events (Fabric, OneLake, job and Azure events) that users can discover, subscribe to and route.
- [Pipelines in Fabric Data Factory](../technologies/microsoft/fabric-pipelines.md): Orchestrates activities such as copies, notebooks, dataflows and stored procedures into scheduled or event-triggered workflows.

## Query and compute

- [Azure Data Explorer](../technologies/microsoft/azure-data-explorer.md): A managed Kusto cluster for fast analytical queries over large volumes of log, telemetry and time-series data using KQL.
- [Azure Synapse Analytics](../technologies/microsoft/azure-synapse-analytics.md): Analytics workspace combining dedicated SQL pools (MPP warehouse), serverless SQL over the lake, Apache Spark pools and pipelines.
- [Eventhouse and KQL database](../technologies/microsoft/fabric-eventhouse.md): A Kusto-engine store for high-volume time-based and log data, queried with KQL or T-SQL in seconds, with optional copies of data in OneLake.
- [Fabric Data Warehouse](../technologies/microsoft/fabric-data-warehouse.md): A T-SQL warehouse with multi-table transactions that stores its tables as Delta Parquet in OneLake and scales compute automatically.
- [Microsoft Fabric capacities (F SKUs)](../technologies/microsoft/fabric-capacities.md): Pools of capacity units, bought through Azure in sizes from F2 upwards, that all Fabric workloads in assigned workspaces share.
- [OneLake shortcuts](../technologies/microsoft/fabric-onelake-shortcuts.md): Virtual folders or tables in OneLake that point to data in other Fabric items or in external stores, so it can be used without copying.
- [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../technologies/microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed): Generates Iceberg metadata for Delta tables and Delta metadata for Iceberg tables in OneLake, so readers of either format can use the same Parquet files.
- [Power BI Direct Lake](../technologies/microsoft/powerbi-direct-lake.md): A semantic model storage mode that loads Delta tables from OneLake into memory on demand, avoiding scheduled import refreshes and DirectQuery latency.

## Serving and activation

- [Azure Cosmos DB](../technologies/microsoft/azure-cosmos-db.md): A globally distributed NoSQL database with single-digit millisecond reads, multi-region writes, a change feed and vector search.
- [Azure Database for PostgreSQL](../technologies/microsoft/azure-database-for-postgresql.md): Managed PostgreSQL (flexible server) with high availability, read replicas and extensions such as pgvector and DiskANN for vector search.
- [Azure HorizonDB](../technologies/microsoft/azure-horizondb.md) (preview): A cloud-native PostgreSQL-compatible database with disaggregated compute and log-based storage for high scale.
- [Azure SQL Database](../technologies/microsoft/azure-sql.md): Managed SQL Server engine in single database, elastic pool and Hyperscale forms, with Azure SQL Managed Instance for near-full SQL Server compatibility.
- [Cosmos DB in Microsoft Fabric](../technologies/microsoft/fabric-cosmos-db.md): A NoSQL document database on the Azure Cosmos DB engine, managed inside Fabric and copied automatically into OneLake as Delta Parquet.
- [Fabric API for GraphQL](../technologies/microsoft/fabric-api-for-graphql.md): Generates a GraphQL API over warehouses, SQL databases, lakehouse and mirrored database endpoints so applications can query and change data.
- [Fabric SQL analytics endpoint](../technologies/microsoft/fabric-sql-analytics-endpoint.md): An automatically created, read-only T-SQL endpoint over the Delta tables of a lakehouse, mirrored database or SQL database.
- [SQL database in Microsoft Fabric](../technologies/microsoft/fabric-sql-database.md): A SaaS operational database on the Azure SQL Database engine whose tables are replicated automatically into OneLake for analytics.

## Analytics and BI

- [Azure Analysis Services](../technologies/microsoft/azure-analysis-services.md): A managed tabular model server for enterprise semantic models consumed by Power BI, Excel and other tools.
- [Copilot in Power BI](../technologies/microsoft/powerbi-copilot.md): Natural-language assistance that summarises reports, answers data questions, creates report pages and helps write DAX and model descriptions.
- [Fabric Activator](../technologies/microsoft/fabric-activator.md): A no-code rules engine that watches streams, reports and Fabric events per business object and triggers alerts, pipelines, functions or Power Automate flows.
- [Fabric data agent](../technologies/microsoft/fabric-data-agent.md): A configurable conversational agent that answers natural-language questions by generating SQL, DAX or KQL over lakehouses, warehouses, semantic models, Eventhouses and ontologies.
- [Fabric Real-Time Dashboard](../technologies/microsoft/fabric-real-time-dashboards.md): Dashboards built on KQL queries over Eventhouse data, refreshing continuously for operational monitoring.
- [Planning in Fabric IQ](../technologies/microsoft/fabric-iq-planning.md): Budgeting, forecasting and scenario planning with planning sheets and editable tables connected to semantic models and OneLake data.
- [Power BI Analyze in Excel and connected tables](../technologies/microsoft/powerbi-excel-integration.md): Lets Excel users build PivotTables and refreshable tables on live connections to Power BI semantic models, with model security and labels applied.
- [Power BI Embedded](../technologies/microsoft/powerbi-embedded.md): Embeds Power BI reports and dashboards in custom applications, either for an organisation's own users or for external customers without Power BI licences.
- [Power BI paginated reports](../technologies/microsoft/powerbi-paginated-reports.md): Pixel-precise, printable reports built in Power BI Report Builder and rendered to PDF, Excel, Word and other formats.
- [Power BI Q&A](../technologies/microsoft/powerbi-q-and-a.md) (deprecated): The earlier natural-language query feature that answers typed questions about a semantic model with visuals.
- [Power BI reports and dashboards](../technologies/microsoft/powerbi-reports.md): Interactive reports authored in Power BI Desktop or the web and shared in the Power BI service, with apps, subscriptions and data alerts.
- [Power BI scorecards and goals](../technologies/microsoft/powerbi-scorecards.md): Tracks business goals against targets, with owners, status rules and check-ins, linked to values in reports or entered manually.
- [Power BI semantic models](../technologies/microsoft/powerbi-semantic-models.md): Tabular models (VertiPaq/Analysis Services engine) holding tables, relationships, DAX measures, hierarchies and row-level security for reporting.

## Machine learning development

- [Automated machine learning (AutoML) in Azure Machine Learning](../technologies/microsoft/azure-ml-automl.md): Tries algorithms, features and settings automatically for tabular, forecasting, vision and text tasks and returns ranked models.
- [Azure Machine Learning](../technologies/microsoft/azure-machine-learning.md): A managed service for training models on CPU and GPU clusters or serverless compute, with jobs, sweeps and pipelines.
- [Azure Machine Learning data labeling](../technologies/microsoft/azure-ml-data-labeling.md): Manages image and text labelling projects with human labellers and ML-assisted pre-labelling.
- [Azure Machine Learning managed feature store](../technologies/microsoft/azure-ml-managed-feature-store.md): Defines feature sets as code, materialises them to offline and online stores, and retrieves point-in-time correct training data.
- [Azure Machine Learning registries and MLflow tracking](../technologies/microsoft/azure-ml-registries-mlflow.md): Tracks runs, parameters and metrics with MLflow and versions models, environments and components in workspace or cross-workspace registries.
- [Azure Machine Learning Responsible AI dashboard](../technologies/microsoft/azure-ml-responsible-ai-dashboard.md): Assesses models with error analysis, feature importance explanations, fairness metrics and counterfactuals before release.
- [Data Science in Microsoft Fabric](../technologies/microsoft/fabric-data-science.md): Notebook-based machine learning with MLflow experiments, a model registry, AutoML and batch scoring with the PREDICT function.

## ML operations

- [Azure Machine Learning model monitoring](../technologies/microsoft/azure-ml-model-monitoring.md): Monitors deployed models for data drift, prediction drift, data quality and performance against ground truth, with alerts.
- [Azure Machine Learning online and batch endpoints](../technologies/microsoft/azure-ml-endpoints.md): Deploys models to managed real-time endpoints with traffic splitting and mirroring, or to batch endpoints that score large datasets.

## Generative AI

- [Azure AI Content Safety](../technologies/microsoft/azure-ai-content-safety.md): Classifies text and images for harmful content and detects prompt injection, jailbreaks and ungrounded output, used by Foundry guardrails.
- [Azure AI Search](../technologies/microsoft/azure-ai-search.md): A search service offering full-text, vector, hybrid and multimodal retrieval with indexers, integrated vectorisation and agentic retrieval.
- [Azure API Management](../technologies/microsoft/azure-api-management.md): An API gateway for publishing, securing and rate-limiting APIs, including AI gateway policies for model token limits, load balancing and logging.
- [Azure Machine Learning prompt flow](../technologies/microsoft/azure-prompt-flow.md) (deprecated): A visual and code tool in Foundry and Azure Machine Learning for building, testing and deploying LLM flows and prompt variants.
- [Azure OpenAI in Foundry Models](../technologies/microsoft/azure-openai.md): OpenAI language, reasoning, embedding, image, video and audio models hosted in Azure under Azure data handling, networking and SLAs.
- [Fabric MCP server](../technologies/microsoft/fabric-mcp-server.md): A Model Context Protocol server that gives AI coding assistants and agents access to Fabric APIs, item definitions and OneLake.
- [Fabric operations agent](../technologies/microsoft/fabric-operations-agent.md): An agent that monitors Eventhouse or ontology data against goals and rules, and recommends or runs actions through Teams with approval.
- [Foundry Agent Service](../technologies/microsoft/azure-foundry-agent-service.md): A managed runtime for prompt-based and hosted code agents with tools, MCP connections, threads and publishing to Teams and Microsoft 365 Copilot.
- [Foundry IQ](../technologies/microsoft/azure-foundry-iq.md): A managed knowledge layer that unifies retrieval over Azure AI Search indexes, SharePoint, Fabric IQ, web and other sources behind knowledge bases for agents.
- [Microsoft Agent Framework](../technologies/microsoft/azure-agent-framework.md): An open-source SDK for .NET and Python for building agents and graph-based multi-agent workflows across model providers.
- [Microsoft Foundry](../technologies/microsoft/azure-foundry.md): Azure's platform for building generative AI applications and agents, combining a model catalogue, agent runtime, tools, evaluation and governance in projects.
- [Microsoft Foundry evaluations](../technologies/microsoft/azure-foundry-evaluations.md): Scores model and agent outputs with built-in and custom evaluators for quality, groundedness and safety, offline or continuously in production.
- [Microsoft Foundry observability and tracing](../technologies/microsoft/azure-foundry-observability.md): Captures OpenTelemetry traces of agent and model calls with latency, token use and tool steps, stored in Application Insights.

## Metadata and discovery

- [Azure Schema Registry in Event Hubs](../technologies/microsoft/azure-event-hubs-schema-registry.md): Stores and versions Avro and JSON schemas for event producers and consumers with compatibility checks.
- [Data lineage in Microsoft Purview](../technologies/microsoft/purview-lineage.md): Shows how data flows between sources, processes and targets across Azure Data Factory, Synapse, Databricks, Fabric, Power BI and other systems.
- [Microsoft Purview Data Map](../technologies/microsoft/purview-data-map.md): Scans on-premises, multicloud and SaaS sources to harvest schemas, classifications and lineage into a metadata graph with Apache Atlas-compatible APIs.
- [Microsoft Purview Unified Catalog](../technologies/microsoft/purview-unified-catalog.md): A business-facing data governance catalogue organised by governance domains, with glossary terms, critical data elements, OKRs and health management.
- [OneLake catalog](../technologies/microsoft/fabric-onelake-catalog.md): The Fabric catalogue for finding, understanding, governing and securing items, with Explore, Govern and Secure views.

## Data quality and observability

- [Microsoft Purview Data Quality](../technologies/microsoft/purview-data-quality.md): Profiles data and runs out-of-the-box, custom and AI-suggested quality rules on data products, rolling scores up to products and domains.

## Governance and compliance

- [Azure AI Language PII detection](../technologies/microsoft/azure-ai-language-pii.md): Detects and redacts personal and health information in text and conversations.
- [Azure Policy](../technologies/microsoft/azure-policy.md): Evaluates and enforces rules on Azure resources, such as allowed regions, required encryption or private endpoints, and reports compliance.
- [Fabric domains](../technologies/microsoft/fabric-domains.md): Group workspaces by business area, with subdomains, domain admins and delegated settings, to support data mesh operating models.
- [Foundry Control Plane](../technologies/microsoft/azure-foundry-control-plane.md) (preview): A fleet-wide view of agents, models and tools with inventory, compliance status, guardrail policies and health across Foundry projects.
- [Microsoft Priva](../technologies/microsoft/purview-priva.md): Privacy tooling that finds personal data, flags privacy risks such as overexposure and transfers, and manages subject rights requests.
- [Microsoft Purview Compliance Manager](../technologies/microsoft/purview-compliance-manager.md): Maps regulatory requirements to improvement actions and Microsoft controls, and tracks evidence and a compliance score.
- [Microsoft Purview Data Lifecycle Management](../technologies/microsoft/purview-data-lifecycle-management.md): Applies retention policies and labels that keep or delete content for set periods, with records management for regulated items.
- [Microsoft Purview Information Protection](../technologies/microsoft/purview-information-protection.md): Sensitivity labels applied manually or automatically to files, emails and Fabric and Power BI items, with encryption and inheritance downstream.

## Security and access

- [Azure Key Vault](../technologies/microsoft/azure-key-vault.md): Stores secrets, keys and certificates with access control, rotation and HSM backing, including Managed HSM for single-tenant keys.
- [Azure Private Link](../technologies/microsoft/azure-private-link.md): Exposes Azure PaaS services through private endpoints inside a virtual network so traffic stays off the public internet.
- [Customer-managed keys for Fabric workspaces](../technologies/microsoft/fabric-customer-managed-keys.md): Encrypts all OneLake data in a workspace with a key held in Azure Key Vault, so revoking the key blocks access.
- [Data security posture management in Microsoft Defender for Cloud](../technologies/microsoft/azure-defender-for-cloud-dspm.md): Discovers sensitive data in cloud storage and databases across Azure, AWS and GCP by sampling, and shows attack paths and exposures that put it at risk.
- [Fabric workspace identity](../technologies/microsoft/fabric-workspace-identity.md): A Microsoft Entra identity managed by Fabric for a workspace, used to authenticate to ADLS, Event Hubs and other sources without stored secrets.
- [Fabric workspace outbound access protection](../technologies/microsoft/fabric-outbound-access-protection.md): Blocks Fabric items in a workspace from connecting to destinations other than approved managed private endpoints or connections.
- [Microsoft Entra ID](../technologies/microsoft/azure-entra-id.md): Microsoft's cloud identity service providing single sign-on, conditional access, managed identities, groups and access governance for Azure, Fabric and Microsoft 365.
- [Microsoft on-premises and virtual network data gateways](../technologies/microsoft/fabric-data-gateways.md): Gateways that let Fabric and Power BI reach data sources inside private or on-premises networks without opening them to the internet.
- [Microsoft Purview Audit](../technologies/microsoft/purview-audit.md): Records user and admin activity across Microsoft 365, Fabric and Power BI into a searchable unified audit log.
- [Microsoft Purview Data Loss Prevention](../technologies/microsoft/purview-data-loss-prevention.md): Detects sensitive information in Microsoft 365, endpoints and Fabric items and raises policy tips, alerts or access restrictions.
- [Microsoft Purview Data Security Posture Management](../technologies/microsoft/purview-dspm.md): Finds sensitive data and oversharing risks across Microsoft 365, AI apps and agents and connected third-party stores, and recommends DLP, labelling and insider risk policies.
- [Microsoft Purview Insider Risk Management](../technologies/microsoft/purview-insider-risk-management.md): Correlates user activity signals to detect and investigate risky behaviour such as data theft or leaks by people inside the organisation.
- [OneLake security](../technologies/microsoft/fabric-onelake-security.md): Role-based access rules defined once on OneLake data, down to table, folder, row and column, and enforced across Fabric engines.
- [Private links for Microsoft Fabric](../technologies/microsoft/fabric-private-links.md): Restricts inbound access to a Fabric tenant or to individual workspaces through Azure Private Link, with managed virtual networks for Spark.

## Data sharing and collaboration

- [Azure Confidential Clean Rooms](../technologies/microsoft/azure-confidential-clean-rooms.md) (preview): Lets several organisations run approved Spark SQL analytics over combined datasets inside attested trusted execution environments without exposing raw data.
- [Azure Data Share](../technologies/microsoft/azure-data-share.md): Shares snapshots of storage and SQL data, or in-place Azure Data Explorer databases, with other Azure tenants under provider control.
- [External data sharing in Microsoft Fabric](../technologies/microsoft/fabric-external-data-sharing.md): Shares lakehouse, warehouse and database data in place with users in another Fabric tenant, who receive a read-only shortcut.

## Data products

- [Data products in Microsoft Purview Unified Catalog](../technologies/microsoft/purview-data-products.md): Groups related tables, files and reports into a published data product with owners, terms of use and an access request and approval workflow.

## Development and DataOps

- [Copilot in Fabric](../technologies/microsoft/fabric-copilot.md) (preview): Generative AI assistance across Fabric workloads for writing code, SQL, KQL, pipeline expressions and Dataflow steps from natural language.
- [Fabric deployment pipelines](../technologies/microsoft/fabric-deployment-pipelines.md): Promote workspace content through two to ten stages such as development, test and production, with item pairing and deployment rules.
- [Fabric Git integration](../technologies/microsoft/fabric-git-integration.md): Connects a workspace to a branch in Azure DevOps, GitHub or GitHub Enterprise so item definitions can be committed, branched and updated.
- [Fabric notebooks](../technologies/microsoft/fabric-notebooks.md): Browser-based notebooks for PySpark, Scala, Spark SQL, R and single-node Python, with scheduling, collaboration and Copilot assistance.
- [Fabric variable library](../technologies/microsoft/fabric-variable-library.md): A workspace item holding variables with value sets per stage, consumed by pipelines, notebooks, shortcuts, dataflows and other items.
- [fabric-cicd](../technologies/microsoft/fabric-cicd-library.md): A Microsoft-maintained Python library for deploying Fabric item definitions from a Git repository to target workspaces with environment-specific parameters.

## Platform operations

- [Azure Backup](../technologies/microsoft/azure-backup.md): Managed backup with vaults, policies and retention for VMs, SQL and PostgreSQL databases, blobs and other Azure workloads.
- [Azure carbon optimization](../technologies/microsoft/azure-carbon-optimization.md): Reports estimated carbon emissions of Azure resources and subscriptions and suggests reductions.
- [Azure Monitor](../technologies/microsoft/azure-monitor.md): Collects metrics, logs and traces from Azure resources and applications into Log Analytics and Application Insights for querying, dashboards and alerts.
- [Bicep](../technologies/microsoft/azure-bicep.md): A declarative language that compiles to Azure Resource Manager templates for deploying Azure resources as code.
- [Fabric workspace monitoring](../technologies/microsoft/fabric-workspace-monitoring.md) (preview): Collects logs and metrics from warehouses, pipelines, Eventhouses, semantic models and other items into a KQL database for querying and alerting.
- [Fabric workspaces](../technologies/microsoft/fabric-workspaces.md): Containers for Fabric items with their own roles, capacity assignment, Git connection and network settings.
- [Microsoft Cost Management](../technologies/microsoft/azure-cost-management.md): Analyses Azure spend by subscription, resource and tag, with budgets, alerts, exports and Advisor savings recommendations.
- [Microsoft Fabric Capacity Metrics app](../technologies/microsoft/fabric-capacity-metrics-app.md): A Power BI app that reports capacity unit consumption by workspace, item and operation, including throttling and storage.
- [OneLake disaster recovery](../technologies/microsoft/fabric-onelake-disaster-recovery.md): A capacity setting that replicates OneLake data asynchronously to the Azure paired region so it can be read after a regional failover.
- [Power BI Report Server](../technologies/microsoft/powerbi-report-server.md): An on-premises server for publishing Power BI and paginated reports where cloud services cannot be used.
- [Terraform Provider for Microsoft Fabric](../technologies/microsoft/fabric-terraform-provider.md): A Terraform provider for creating and managing Fabric capacities, workspaces, items, role assignments and related resources as code.

## Specialised data types

- [Azure Maps](../technologies/microsoft/azure-maps.md): Geospatial APIs and SDKs for rendering maps, geocoding, routing, traffic, weather and time zones.
- [Fabric IQ ontology](../technologies/microsoft/fabric-iq-ontology.md) (preview): Defines business entity types, properties, relationships, rules and metrics and binds them to OneLake data, giving people and agents a shared business vocabulary.
- [Graph in Microsoft Fabric](../technologies/microsoft/fabric-graph.md): A graph store and query engine over OneLake data that models nodes and edges and queries them with ISO GQL or natural language.
- [Maps in Microsoft Fabric](../technologies/microsoft/fabric-maps.md) (preview): A geospatial visualisation item for static and streaming location data held in Fabric.

