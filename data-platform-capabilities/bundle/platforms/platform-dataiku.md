---
type: Platform
id: platform-dataiku
title: Dataiku
description: A platform for building data pipelines, machine learning models, generative AI applications and AI agents visually or in code, on top of an organisation's existing data platforms.
vendor: Dataiku
resource: https://www.dataiku.com/product/
folder: dataiku
order: 15
terminology:
  ai-context-layer: Semantic Models
  ai-gateway: LLM Mesh
  ai-guardrails: Guardrails (Safe Guard)
  ai-spend-controls: Cost Control (Cost Guard)
  automl: Visual ML
  container-services: Elastic AI computation
  data-applications: Webapps and Dataiku Applications
  data-consumer-portal: Workspaces
  data-engineering-agents: Cobuild
  data-labelling: Labeling
  data-preparation: Prepare recipe
  data-quality-rules: Data Quality rules
  enterprise-ai-assistant: Agent Hub
  environment-promotion: Bundles and Project Deployer
  genai-evaluation: Quality Guard
  local-development: Code Studios
  low-code-transformation: Visual recipes
  model-performance-monitoring: Model evaluation stores
  model-registry: Saved models
  prompt-management: Prompt Studios
  real-time-inference: API node
  retrieval-pipelines: Knowledge Banks
  runtime-management: Code environments
  workflow-orchestration: Scenarios
families:
- name: Dataiku Platform for AI Success
  aliases: [Dataiku DSS, Data Science Studio, Universal AI Platform]
  technologies:
  - dataiku
  - dataiku-cloud
  - dataiku-cloud-stacks
  - dataiku-connections
  - dataiku-flow-visual-recipes
  - dataiku-code-recipes-notebooks
  - dataiku-code-studios
  - dataiku-scenarios
  - dataiku-data-quality
  - dataiku-catalog
  - dataiku-data-lineage
  - dataiku-dashboards-stories
  - dataiku-webapps
  - dataiku-visual-ml
  - dataiku-labeling
  - dataiku-feature-store
  - dataiku-deployer
  - dataiku-model-monitoring
  - dataiku-govern
  - dataiku-cobuild
  - dataiku-semantic-models
  - dataiku-llm-mesh
  - dataiku-prompt-studios
  - dataiku-knowledge-banks
  - dataiku-agents
  - dataiku-agent-hub
- name: Dataiku LLM Mesh
  aliases: [LLM Guard Services, Cost Guard, Safe Guard, Quality Guard]
  technologies: [dataiku-llm-mesh, dataiku-prompt-studios, dataiku-knowledge-banks]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Dataiku sells one platform, marketed since March 2026 as the Platform for AI Success, in which analysts, data scientists and engineers build data pipelines, machine learning models, generative AI applications and agents in shared projects. Work is laid out as a Flow of datasets, visual and code recipes, models, knowledge banks and agents. Dataiku stores little data itself: it connects to warehouses, lakehouses, databases and object storage, and pushes recipes down to engines such as Snowflake, Databricks, BigQuery, Spark and Kubernetes. Scenarios automate builds, checks and retraining; the Deployer moves bundles and API services into production; Govern keeps a registry of models, projects and agents with sign-off workflows.

The generative AI layer is the LLM Mesh, a gateway through which projects call commercial, cloud-hosted and self-hosted models with guardrails, cost quotas and logging. On top of it sit Prompt Studios, Knowledge Banks for retrieval, Visual and Code Agents, Agent Hub for putting agents in front of business users, and Cobuild, an agent that builds Flows, models and dashboards from natural-language requests. Agent Management, a separate product that Dataiku said in September 2026 would become generally available in October, inventories and monitors agents built on other vendors' platforms as well as Dataiku's. The platform runs as Dataiku Cloud, a service hosted by Dataiku, or self-managed in the customer's cloud account with Cloud Stacks and Fleet Manager, or on the customer's own Linux servers.

# Notes

- Dataiku is a layer over other platforms rather than a storage or query engine, so performance and cost depend on pushing recipes down to the underlying warehouse, lakehouse or Kubernetes cluster. Check which recipes and processors run in-database on each connection.
- Product names change with marketing. The platform has been called Dataiku DSS (Data Science Studio) and the Universal AI Platform; the Data Catalog became the Catalog in version 15, and the LLM Guard Services names (Cost Guard, Safe Guard, Quality Guard) map to cost control, guardrails and evaluation features of the LLM Mesh.
- Dataiku Answers and Agent Connect, the earlier chat interfaces, are being replaced by Agent Hub.
- Several features need higher licence tiers, including custom LLM cost quotas (Advanced LLM Mesh) and agent registries and custom templates in Govern (Advanced Govern). Agent Management is a separate product priced per instance with per-agent monitoring.
- Dataiku exposes agents and tools to other systems through an MCP server and an A2A server, and can call agents built on Snowflake Cortex, Databricks, Amazon Bedrock and Google Vertex AI.
- Reasoning Systems are packaged, industry-specific combinations of data, models, agents and business rules; the first, for manufacturing operations, was released in March 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 5 of 22 | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 0 of 23 | [Storage and table management](../capabilities/storage/storage.md), [Data versioning](../capabilities/storage/data-versioning.md), [Object storage](../capabilities/storage/object-storage.md), [Open file formats](../capabilities/storage/file-formats.md), [Open table formats](../capabilities/storage/open-table-formats.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Platform-managed storage](../capabilities/storage/managed-storage.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Table catalogue](../capabilities/storage/table-catalogue.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Time travel](../capabilities/storage/time-travel.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 8 of 18 | [Data enrichment](../capabilities/processing/data-enrichment.md), [DataFrame APIs](../capabilities/processing/dataframe-apis.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [Stream processing](../capabilities/processing/stream-processing.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 3 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md) |
| [Query and compute](../capabilities/compute/compute.md) | 4 of 22 | [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Query acceleration](../capabilities/compute/query-acceleration.md), [Query federation](../capabilities/compute/query-federation.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Workload management](../capabilities/compute/workload-management.md), [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Materialised views](../capabilities/compute/materialised-views.md), [Result caching](../capabilities/compute/result-caching.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Provisioned compute](../capabilities/compute/provisioned-compute.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Serverless compute](../capabilities/compute/serverless-compute.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 1 of 13 | [Change feeds](../capabilities/serving/change-feeds.md), [Data APIs](../capabilities/serving/data-apis.md), [Data export](../capabilities/serving/data-export.md), [Decision management](../capabilities/serving/decision-management.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Operational database integration](../capabilities/serving/operational-database.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 8 of 20 | [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 11 of 20 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 13 of 18 | [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 17 of 23 | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 8 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Table-level lineage](../capabilities/metadata/table-lineage.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 6 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 3 of 24 (+1 in preview) | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data classification](../capabilities/governance/data-classification.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Policy management](../capabilities/governance/data-policy-management.md), [Privacy management](../capabilities/governance/privacy-management.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [De-identification](../capabilities/governance/deidentification.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md) (preview only) |
| [Security and access](../capabilities/security/security.md) | 4 of 23 | [Access control](../capabilities/security/access-control.md), [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Encryption](../capabilities/security/encryption.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Privileged access management](../capabilities/security/privileged-access.md), [Role-based access control](../capabilities/security/role-based-access.md), [Row-level security](../capabilities/security/row-level-security.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 0 of 8 | [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md), [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 0 of 7 | [Data products](../capabilities/data-products/data-products.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 11 of 16 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 6 of 27 | [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Platform migration](../capabilities/platform-operations/platform-migration.md), [Platform observability](../capabilities/platform-operations/platform-observability.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Customer-hosted data plane](../capabilities/platform-operations/hybrid-data-plane.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 1 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Geospatial data](../capabilities/specialised-data/geospatial-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Product families

- **Dataiku Platform for AI Success** (also: Dataiku DSS, Data Science Studio, Universal AI Platform): [Dataiku DSS](../technologies/dataiku/dataiku.md), [Dataiku Cloud](../technologies/dataiku/dataiku-cloud.md), [Dataiku Cloud Stacks and Fleet Manager](../technologies/dataiku/dataiku-cloud-stacks.md), [Dataiku connections](../technologies/dataiku/dataiku-connections.md), [Dataiku Flow and visual recipes](../technologies/dataiku/dataiku-flow-visual-recipes.md), [Dataiku code recipes and notebooks](../technologies/dataiku/dataiku-code-recipes-notebooks.md), [Dataiku Code Studios](../technologies/dataiku/dataiku-code-studios.md), [Dataiku scenarios](../technologies/dataiku/dataiku-scenarios.md), [Dataiku Data Quality rules](../technologies/dataiku/dataiku-data-quality.md), [Dataiku Catalog](../technologies/dataiku/dataiku-catalog.md), [Dataiku Data Lineage](../technologies/dataiku/dataiku-data-lineage.md), [Dataiku dashboards and Stories](../technologies/dataiku/dataiku-dashboards-stories.md), [Dataiku webapps and Dataiku Applications](../technologies/dataiku/dataiku-webapps.md), [Dataiku Visual ML](../technologies/dataiku/dataiku-visual-ml.md), [Dataiku labeling](../technologies/dataiku/dataiku-labeling.md), [Dataiku Feature Store](../technologies/dataiku/dataiku-feature-store.md), [Dataiku Deployer and API nodes](../technologies/dataiku/dataiku-deployer.md), [Dataiku model evaluation stores and Unified Monitoring](../technologies/dataiku/dataiku-model-monitoring.md), [Dataiku Govern](../technologies/dataiku/dataiku-govern.md), [Dataiku Cobuild](../technologies/dataiku/dataiku-cobuild.md), [Dataiku Semantic Models](../technologies/dataiku/dataiku-semantic-models.md) (unconfirmed), [Dataiku LLM Mesh](../technologies/dataiku/dataiku-llm-mesh.md), [Dataiku Prompt Studios](../technologies/dataiku/dataiku-prompt-studios.md), [Dataiku Knowledge Banks](../technologies/dataiku/dataiku-knowledge-banks.md), [Dataiku Visual Agents and Code Agents](../technologies/dataiku/dataiku-agents.md), [Dataiku Agent Hub](../technologies/dataiku/dataiku-agent-hub.md) (unconfirmed)
- **Dataiku LLM Mesh** (also: LLM Guard Services, Cost Guard, Safe Guard, Quality Guard): [Dataiku LLM Mesh](../technologies/dataiku/dataiku-llm-mesh.md), [Dataiku Prompt Studios](../technologies/dataiku/dataiku-prompt-studios.md), [Dataiku Knowledge Banks](../technologies/dataiku/dataiku-knowledge-banks.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Agent Hub | [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md) |
| API node | [Real-time inference](../capabilities/mlops/real-time-inference.md) |
| Bundles and Project Deployer | [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) |
| Cobuild | [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md) |
| Code environments | [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md) |
| Code Studios | [IDE and local development](../capabilities/development-lifecycle/local-development.md) |
| Cost Control (Cost Guard) | [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| Data Quality rules | [Data quality rules](../capabilities/data-quality/data-quality-rules.md) |
| Elastic AI computation | [Container services](../capabilities/compute/container-services.md) |
| Guardrails (Safe Guard) | [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| Knowledge Banks | [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md) |
| Labeling | [Data labelling](../capabilities/machine-learning/data-labelling.md) |
| LLM Mesh | [AI gateway](../capabilities/generative-ai/ai-gateway.md) |
| Model evaluation stores | [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) |
| Prepare recipe | [Self-service data preparation](../capabilities/processing/data-preparation.md) |
| Prompt Studios | [Prompt management](../capabilities/generative-ai/prompt-management.md) |
| Quality Guard | [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) |
| Saved models | [Model registry](../capabilities/machine-learning/model-registry.md) |
| Scenarios | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| Semantic Models | [AI context layer](../capabilities/metadata/ai-context-layer.md) |
| Visual ML | [AutoML](../capabilities/machine-learning/automl.md) |
| Visual recipes | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| Webapps and Dataiku Applications | [Data application hosting](../capabilities/development-lifecycle/data-applications.md) |
| Workspaces | [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md) |

# Technologies

## Ingestion and integration

- [Dataiku connections](../technologies/dataiku/dataiku-connections.md): Connectors that read and write data in SQL databases, cloud warehouses, object storage, Iceberg tables, NoSQL stores and business applications, and let recipes run inside the connected engine.

## Processing and transformation

- [Dataiku Flow and visual recipes](../technologies/dataiku/dataiku-flow-visual-recipes.md): Visual pipeline of datasets and recipes, in which the Prepare recipe and recipes such as join, group, window, pivot and fuzzy join transform data without code and can run in the underlying database or Spark.

## Orchestration

- [Dataiku scenarios](../technologies/dataiku/dataiku-scenarios.md): Automation that builds datasets, verifies data quality rules, retrains models and runs other steps on schedules or triggers, and reports results by email, chat or webhook.

## Analytics and BI

- [Dataiku dashboards and Stories](../technologies/dataiku/dataiku-dashboards-stories.md): Charts, dashboards with filters, cross-filtering and drill-down, and Stories, slide-style presentations of live data that an assistant can draft from instructions.

## Machine learning development

- [Dataiku Feature Store](../technologies/dataiku/dataiku-feature-store.md): Registry of curated feature groups, shared datasets that other projects join in batch or look up from API services in real time.
- [Dataiku labeling](../technologies/dataiku/dataiku-labeling.md): Labeling recipe in which people classify or annotate images, text and tabular records to create training data.
- [Dataiku Visual ML](../technologies/dataiku/dataiku-visual-ml.md): Visual and code-assisted model building for prediction, clustering, time series forecasting and causal prediction, with automatic feature handling, algorithm search, explanations and stress tests.

## ML operations

- [Dataiku Govern](../technologies/dataiku/dataiku-govern.md): Separate governance node that keeps registries of projects, bundles, models and agents, with sign-off workflows, deployment policies and custom governance templates.
- [Dataiku model evaluation stores and Unified Monitoring](../technologies/dataiku/dataiku-model-monitoring.md): Stores of repeated model evaluations with drift and performance metrics, and dashboards that show the health of deployed projects, Dataiku API endpoints and external endpoints.

## Generative AI

- [Dataiku Agent Hub](../technologies/dataiku/dataiku-agent-hub.md) (unconfirmed): Portal in which business users chat with the agents an organisation publishes and build their own quick agents over documents and data.
- [Dataiku Knowledge Banks](../technologies/dataiku/dataiku-knowledge-banks.md): Retrieval stores built by recipes that extract text and fields from documents, split and embed them, and index them for retrieval-augmented generation and agents.
- [Dataiku LLM Mesh](../technologies/dataiku/dataiku-llm-mesh.md): Gateway through which Dataiku projects, agents and applications call commercial, cloud-hosted and self-hosted LLMs, with guardrails, cost quotas, rate limits, evaluation and logging.
- [Dataiku Prompt Studios](../technologies/dataiku/dataiku-prompt-studios.md): Workspace for writing, testing and comparing prompts across LLMs, and the Prompt recipe that applies a saved prompt to every row of a dataset.
- [Dataiku Visual Agents and Code Agents](../technologies/dataiku/dataiku-agents.md): Agents built visually or in Python on the LLM Mesh, using managed tools, knowledge banks, semantic models and MCP tools, with human approval steps, tracing, evaluation and MCP and A2A servers for other systems.

## Metadata and discovery

- [Dataiku Catalog](../technologies/dataiku/dataiku-catalog.md): Instance-wide catalogue for finding datasets, models, agents, knowledge banks and other project assets, with curated collections, a most-used datasets view and AI-generated descriptions.
- [Dataiku Data Lineage](../technologies/dataiku/dataiku-data-lineage.md): Column-level lineage across datasets and projects in a Dataiku instance, with manual lineage entries and exports of the lineage graph.
- [Dataiku Semantic Models](../technologies/dataiku/dataiku-semantic-models.md) (unconfirmed): Business models of tables, columns, relationships and metrics that agents use to turn natural-language questions into correct SQL.

## Data quality and observability

- [Dataiku Data Quality rules](../technologies/dataiku/dataiku-data-quality.md): Rules on dataset contents, such as value ranges, uniqueness, record counts, schema and values within their usual range, that can run automatically after each build and roll up into dataset, project and instance views.

## Governance and compliance

- [Dataiku Agent Management](../technologies/dataiku/dataiku-agent-management.md) (preview): Standalone product that finds AI agents running on Dataiku and other vendors' platforms, maps the tools and models they use, and tracks their performance, risk and certification status.

## Development and DataOps

- [Dataiku Cobuild](../technologies/dataiku/dataiku-cobuild.md): Agent inside a Dataiku project that builds and edits Flows, recipes, models, knowledge banks, agents, dashboards, notebooks and scenarios from natural-language requests.
- [Dataiku code recipes and notebooks](../technologies/dataiku/dataiku-code-recipes-notebooks.md): Python, R, SQL, Hive, Impala, PySpark, SparkR, SparkSQL, Spark Scala and shell recipes and Jupyter and SQL notebooks that run inside the Flow alongside visual recipes.
- [Dataiku Code Studios](../technologies/dataiku/dataiku-code-studios.md): Browser-based development environments such as VS Code, JupyterLab and RStudio that run in containers next to a project, with coding agents such as Claude Code, OpenAI Codex and GitHub Copilot.
- [Dataiku Deployer and API nodes](../technologies/dataiku/dataiku-deployer.md): Deployment of project bundles to automation nodes and of models and functions as real-time API services on API nodes, Kubernetes or external machine learning platforms, with several endpoint versions able to share traffic.
- [Dataiku DSS](../technologies/dataiku/dataiku.md): Platform in which teams build data pipelines, models, generative AI applications and agents as shared projects, with managed code environments, Git-based version control, containerised execution and per-user security.
- [Dataiku webapps and Dataiku Applications](../technologies/dataiku/dataiku-webapps.md): Hosted web applications written in HTML and JavaScript, Python (Dash, Streamlit, Bokeh, FastAPI) or R Shiny, and Dataiku Applications, which package a project as a reusable form-driven tool.

## Platform operations

- [Dataiku Cloud](../technologies/dataiku/dataiku-cloud.md): Edition of Dataiku that Dataiku hosts, operates and upgrades as a service, administered through a Launchpad and connected to the customer's own data sources.
- [Dataiku Cloud Stacks and Fleet Manager](../technologies/dataiku/dataiku-cloud-stacks.md): Self-managed deployment of Dataiku in the customer's AWS, Azure or Google Cloud account, where Fleet Manager creates, upgrades, backs up and configures the Dataiku instances.

