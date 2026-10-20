---
type: Platform
id: platform-sas
title: SAS
description: An analytics and AI platform, SAS Viya, for preparing and governing data, building and managing models, and running automated decisions, alongside the long-standing SAS 9 software.
vendor: SAS
resource: https://www.sas.com/en_us/software/viya.html
folder: sas
order: 14
terminology:
  agent-tool-access: SAS Viya MCP Server
  ai-assisted-development: SAS Viya Copilot
  augmented-analytics: Automated explanation
  automl: Automated pipeline generation
  batch-inference: In-database scoring
  data-catalogue: SAS Data Governance
  data-cleansing: Quality Knowledge Base
  database-extraction: SAS/ACCESS engines
  dataframe-apis: SWAT
  decision-management: Decisions
  distributed-processing: CAS (Cloud Analytic Services)
  hyperparameter-tuning: Autotuning
  low-code-transformation: Flows
  metadata-harvesting: Discovery agents
  model-governance: Model cards
  model-registry: Model repositories
  query-federation: SQL pass-through
  real-time-inference: Micro Analytic Service
  role-based-access: General authorization rules
  row-level-security: Row-level permissions
  single-node-processing: SAS Compute Server
  sql-query-engine: FedSQL
  workload-management: SAS Workload Orchestrator
families:
- name: SAS Viya
  aliases: [Viya, Viya 4]
  technologies:
  - sas-viya
  - sas-cloud-analytic-services
  - sas-compute-server
  - sas-data-and-ai-studio
  - sas-data-hub
  - sas-data-engineering
  - sas-data-accelerator
  - sas-speedystore
  - sas-data-governance
  - sas-visual-analytics
  - sas-model-studio
  - sas-visual-forecasting
  - sas-visual-text-analytics
  - sas-model-manager
  - sas-container-runtime
  - sas-intelligent-decisioning
  - sas-event-stream-processing
  - sas-viya-workbench
  - sas-viya-copilot
  - sas-viya-mcp-server
  - sas-agentic-ai-accelerator
  - sas-workload-management
  - sas-viya-security
- name: SAS Data Management
  technologies:
  - sas-data-and-ai-studio
  - sas-data-hub
  - sas-data-engineering
  - sas-data-accelerator
  - sas-data-governance
  - sas-speedystore
  - sas-data-maker
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

SAS's current platform is SAS Viya, a set of containerised services on Kubernetes that runs on the main public clouds, on Red Hat OpenShift or on premises, managed by the customer or by SAS. Two engines do the work: CAS (Cloud Analytic Services), which holds data in memory across a cluster and runs analytics in parallel, and the SAS Compute Server, which runs traditional SAS and Python programs on one machine. Around them sit the data management products (SAS Data Hub, SAS Data and AI Studio, SAS Data Accelerator and SAS Data Governance, sold together as SAS Data Engineering), SAS Visual Analytics, SAS Model Studio for machine learning, SAS Model Manager, SAS Intelligent Decisioning and SAS Event Stream Processing.

SAS Viya Copilot adds AI assistants inside these applications, and the SAS Viya MCP Server and SAS Agentic AI Accelerator let external and SAS-built agents use SAS models, analytics and decisions. Some newer products stand apart from Viya: SAS Data Maker and SAS AI Navigator are sold through Microsoft Marketplace. SAS 9.4, with SAS Enterprise Guide, is still maintained and further releases are planned, but most new work goes into SAS Viya. SAS's industry solutions, such as fraud, anti-money laundering and risk, are outside the scope of this data platform.

# Notes

- SAS Viya is an analytics and decisioning layer rather than a data warehouse: data usually stays in a database, lakehouse or object store and is read through SAS/ACCESS engines or loaded into CAS memory. SAS SpeedyStore, a SingleStore database embedded in Viya, is the exception.
- SAS has renamed much of its data management range: SAS Studio became SAS Data and AI Studio with the 2026.06 release, SAS Data Explorer became SAS Data Hub, SAS In-Database Technologies became SAS Data Accelerator, and SAS Information Catalog and SAS Information Governance became the two tiers of SAS Data Governance. Documentation and contracts often still use the old names.
- SAS Viya is licensed in editions (SAS Viya, Advanced, Enterprise and Programming), so whether a capability is available depends on the edition bought; building decisions and streaming analytics are only in SAS Viya Enterprise, and in-database acceleration only in Enterprise and Programming.
- SAS Viya releases monthly as Stable versions, with Long-Term Support versions every six months; features in this bundle are tied to releases such as 2026.06.
- The SAS Viya MCP Server and SAS Agentic AI Accelerator are open-source projects on GitHub that still need a licensed SAS Viya environment.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 5 of 22 | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md), [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 0 of 23 | [Storage and table management](../capabilities/storage/storage.md), [Data versioning](../capabilities/storage/data-versioning.md), [Object storage](../capabilities/storage/object-storage.md), [Open file formats](../capabilities/storage/file-formats.md), [Open table formats](../capabilities/storage/open-table-formats.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Platform-managed storage](../capabilities/storage/managed-storage.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Table catalogue](../capabilities/storage/table-catalogue.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Time travel](../capabilities/storage/time-travel.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 10 of 18 | [AI functions in SQL](../capabilities/processing/ai-functions.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 0 of 5 | [Orchestration](../capabilities/orchestration/orchestration.md), [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| [Query and compute](../capabilities/compute/compute.md) | 8 of 22 | [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md), [Query acceleration](../capabilities/compute/query-acceleration.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Materialised views](../capabilities/compute/materialised-views.md), [Result caching](../capabilities/compute/result-caching.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Container services](../capabilities/compute/container-services.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Serverless compute](../capabilities/compute/serverless-compute.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 3 of 13 | [Change feeds](../capabilities/serving/change-feeds.md), [Data APIs](../capabilities/serving/data-apis.md), [Data export](../capabilities/serving/data-export.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 6 of 20 | [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 11 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Feature store](../capabilities/machine-learning/feature-store.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 14 of 18 | [Continuous training](../capabilities/mlops/continuous-training.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Inference logging](../capabilities/mlops/inference-logging.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 9 of 23 | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Model customisation](../capabilities/generative-ai/model-customisation.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 8 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 3 of 7 | [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 4 of 24 | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Privacy management](../capabilities/governance/privacy-management.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [De-identification](../capabilities/governance/deidentification.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 6 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Encryption](../capabilities/security/encryption.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 0 of 8 | [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md), [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 0 of 7 | [Data products](../capabilities/data-products/data-products.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 8 of 16 | [Data application hosting](../capabilities/development-lifecycle/data-applications.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 of 27 | [Backup and disaster recovery](../capabilities/platform-operations/business-continuity.md), [Cost management](../capabilities/platform-operations/cost-management.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Platform migration](../capabilities/platform-operations/platform-migration.md), [Platform observability](../capabilities/platform-operations/platform-observability.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Customer-hosted data plane](../capabilities/platform-operations/hybrid-data-plane.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 1 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Geospatial data](../capabilities/specialised-data/geospatial-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Product families

- **SAS Viya** (also: Viya, Viya 4): [SAS Viya](../technologies/sas/sas-viya.md), [SAS Cloud Analytic Services (CAS)](../technologies/sas/sas-cloud-analytic-services.md), [SAS Compute Server](../technologies/sas/sas-compute-server.md), [SAS Data and AI Studio](../technologies/sas/sas-data-and-ai-studio.md), [SAS Data Hub](../technologies/sas/sas-data-hub.md), [SAS Data Engineering](../technologies/sas/sas-data-engineering.md), [SAS Data Accelerator](../technologies/sas/sas-data-accelerator.md), [SAS SpeedyStore](../technologies/sas/sas-speedystore.md), [SAS Data Governance](../technologies/sas/sas-data-governance.md), [SAS Visual Analytics](../technologies/sas/sas-visual-analytics.md), [SAS Model Studio](../technologies/sas/sas-model-studio.md), [SAS Visual Forecasting](../technologies/sas/sas-visual-forecasting.md), [SAS Visual Text Analytics](../technologies/sas/sas-visual-text-analytics.md), [SAS Model Manager](../technologies/sas/sas-model-manager.md), [SAS Container Runtime](../technologies/sas/sas-container-runtime.md), [SAS Intelligent Decisioning](../technologies/sas/sas-intelligent-decisioning.md), [SAS Event Stream Processing](../technologies/sas/sas-event-stream-processing.md), [SAS Viya Workbench](../technologies/sas/sas-viya-workbench.md), [SAS Viya Copilot](../technologies/sas/sas-viya-copilot.md), [SAS Viya MCP Server](../technologies/sas/sas-viya-mcp-server.md), [SAS Agentic AI Accelerator](../technologies/sas/sas-agentic-ai-accelerator.md), [SAS Workload Management](../technologies/sas/sas-workload-management.md), [SAS Viya security controls](../technologies/sas/sas-viya-security.md)
- **SAS Data Management**: [SAS Data and AI Studio](../technologies/sas/sas-data-and-ai-studio.md), [SAS Data Hub](../technologies/sas/sas-data-hub.md), [SAS Data Engineering](../technologies/sas/sas-data-engineering.md), [SAS Data Accelerator](../technologies/sas/sas-data-accelerator.md), [SAS Data Governance](../technologies/sas/sas-data-governance.md), [SAS SpeedyStore](../technologies/sas/sas-speedystore.md), [SAS Data Maker](../technologies/sas/sas-data-maker.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Automated explanation | [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md) |
| Automated pipeline generation | [AutoML](../capabilities/machine-learning/automl.md) |
| Autotuning | [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md) |
| CAS (Cloud Analytic Services) | [Distributed processing](../capabilities/processing/distributed-processing.md) |
| Decisions | [Decision management](../capabilities/serving/decision-management.md) |
| Discovery agents | [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md) |
| FedSQL | [SQL query engine](../capabilities/compute/sql-query-engine.md) |
| Flows | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| General authorization rules | [Role-based access control](../capabilities/security/role-based-access.md) |
| In-database scoring | [Batch inference](../capabilities/mlops/batch-inference.md) |
| Micro Analytic Service | [Real-time inference](../capabilities/mlops/real-time-inference.md) |
| Model cards | [Model governance](../capabilities/mlops/model-governance.md) |
| Model repositories | [Model registry](../capabilities/machine-learning/model-registry.md) |
| Quality Knowledge Base | [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md) |
| Row-level permissions | [Row-level security](../capabilities/security/row-level-security.md) |
| SAS Compute Server | [Single-node processing](../capabilities/processing/single-node-processing.md) |
| SAS Data Governance | [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| SAS Viya Copilot | [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md) |
| SAS Viya MCP Server | [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) |
| SAS Workload Orchestrator | [Workload management](../capabilities/compute/workload-management.md) |
| SAS/ACCESS engines | [Database extraction](../capabilities/ingestion-integration/database-extraction.md) |
| SQL pass-through | [Query federation](../capabilities/compute/query-federation.md) |
| SWAT | [DataFrame APIs](../capabilities/processing/dataframe-apis.md) |

# Technologies

## Ingestion and integration

- [SAS Data Hub](../technologies/sas/sas-data-hub.md): Data connectivity application in SAS Viya for defining and monitoring connections to databases, cloud data platforms and file stores, and for browsing and previewing their data.

## Processing and transformation

- [SAS 9.4 and SAS Enterprise Guide](../technologies/sas/sas-9.md): Earlier SAS platform of Base SAS, SAS/STAT and other products running on Windows and Linux servers, with the SAS Enterprise Guide desktop client for code and point-and-click tasks.
- [SAS Cloud Analytic Services (CAS)](../technologies/sas/sas-cloud-analytic-services.md): In-memory engine in SAS Viya that loads tables across a cluster of workers and runs data preparation, SQL, statistics and machine learning on them in parallel.
- [SAS Compute Server](../technologies/sas/sas-compute-server.md): Single-machine server in SAS Viya that runs traditional SAS programs, such as DATA step and procedures, and Python code in sessions started for each user or job.
- [SAS Data and AI Studio](../technologies/sas/sas-data-and-ai-studio.md): Browser-based development environment in SAS Viya for writing SAS and Python code and building visual flows that extract, transform and load data and run analytics.
- [SAS Event Stream Processing](../technologies/sas/sas-event-stream-processing.md): Streaming engine that filters, aggregates, joins and scores events in continuous queries, running from edge devices to Kubernetes clusters, with a low-code designer.
- [SAS Visual Text Analytics](../technologies/sas/sas-visual-text-analytics.md): Natural language processing application in SAS Viya that parses text, discovers topics, classifies documents, analyses sentiment and extracts information with linguistic rules, machine learning and LLMs.

## Query and compute

- [SAS Managed Cloud Services](../technologies/sas/sas-managed-cloud-services.md): SAS-operated hosting and management of SAS software on Microsoft Azure or AWS, or in a customer's own cloud, including SAS Viya Essentials, a fixed-price set of SAS Viya products on Azure.
- [SAS SpeedyStore](../technologies/sas/sas-speedystore.md): SingleStore database embedded in SAS Viya, so that transactional and analytical workloads and SAS analytics run against one copy of the data.
- [SAS Workload Management](../technologies/sas/sas-workload-management.md): Scheduler for SAS Viya compute sessions and jobs on Kubernetes that routes work through rule-based queues and priorities, balances it across nodes by capacity and restarts pre-empted jobs.

## Serving and activation

- [SAS Intelligent Decisioning](../technologies/sas/sas-intelligent-decisioning.md): Application in SAS Viya for building decision flows that combine business rules, model scores, code and calls to external APIs such as LLMs, then testing them and publishing them as batch, API or real-time services.

## Analytics and BI

- [SAS Visual Analytics](../technologies/sas/sas-visual-analytics.md): Web application in SAS Viya for building interactive reports and dashboards, exploring data, and running automated explanations, forecasts and scenario analysis without code.

## Machine learning development

- [SAS Model Manager](../technologies/sas/sas-model-manager.md): Model lifecycle application in SAS Viya that registers and versions SAS, Python and R models, documents them with model cards, publishes them to run-time destinations and monitors their performance and drift.
- [SAS Model Studio](../technologies/sas/sas-model-studio.md): Browser-based machine learning application in SAS Viya that builds, compares and explains pipelines of data preparation, feature engineering and models, with automated pipeline generation and tuning.
- [SAS Visual Forecasting](../technologies/sas/sas-visual-forecasting.md): Forecasting application in SAS Viya that builds pipelines of time series, machine learning and hybrid models for each level of a hierarchy, selects the best model for each series and reconciles forecasts across levels.

## ML operations

- [SAS Container Runtime](../technologies/sas/sas-container-runtime.md): Packaging of SAS and Python models and decisions as lightweight OCI containers with a REST scoring endpoint that run on any container platform without a SAS Viya deployment.
- [SAS Data Accelerator](../technologies/sas/sas-data-accelerator.md): Capability of SAS Viya that runs SAS model scoring, data quality functions and some analytics inside external databases and cloud data platforms instead of moving the data to SAS.

## Generative AI

- [SAS Agentic AI Accelerator](../technologies/sas/sas-agentic-ai-accelerator.md): Open-source kit of code, deployment recipes and interfaces for building, governing and deploying AI agents on SAS Viya, including a no-code prompt engineering interface and recipes for hosting LLMs and embedding models.
- [SAS Retrieval Agent Manager](../technologies/sas/sas-retrieval-agent-manager.md): No-code retrieval-augmented generation product that ingests documents, tests and selects retrieval configurations, and serves cited answers through an API, chatbot or retrieval agents.
- [SAS Viya MCP Server](../technologies/sas/sas-viya-mcp-server.md): Self-hosted Model Context Protocol server that lets external AI agents and coding assistants run SAS code, train AutoML projects, score models and work with SAS Viya content as tools, under the user's Viya permissions.

## Metadata and discovery

- [SAS Data Governance](../technologies/sas/sas-data-governance.md): Catalogue and governance product in SAS Viya that discovers and profiles data assets, detects personal data, records lineage from data to reports and models, and holds a business glossary.

## Data quality and observability

- [SAS Data Engineering](../technologies/sas/sas-data-engineering.md): Packaged SAS Viya offering for building data pipelines that bundles visual and code-based development, data connectivity, data profiling, data quality, entity resolution and governance.

## Governance and compliance

- [SAS AI Navigator](../technologies/sas/sas-ai-navigator.md): SaaS application that keeps an inventory of an organisation's AI models, agents and use cases, from SAS or elsewhere, and checks them against internal policies and imported regulatory policy packs.

## Security and access

- [SAS Viya security controls](../technologies/sas/sas-viya-security.md): Authentication through SAS Logon with OpenID Connect, SAML or LDAP, rule-based permissions on folders, reports and services, row-level permissions on CAS tables, and audit records of user activity.

## Development and DataOps

- [SAS Data Maker](../technologies/sas/sas-data-maker.md): Low-code application that generates synthetic tables, including related tables and time series, which keep the statistical patterns of real data, and reports the quality and privacy of the result.
- [SAS Viya Copilot](../technologies/sas/sas-viya-copilot.md): Family of AI assistants embedded in SAS Viya applications that generate and explain SAS and Python code, guide model pipeline building and help manage models and decisions from natural-language requests.
- [SAS Viya Workbench](../technologies/sas/sas-viya-workbench.md): Self-service cloud development environment in which data scientists code in SAS, Python or R through Jupyter, Visual Studio Code or SAS Enterprise Guide on CPU or GPU compute that scales and stops on demand.

## Platform operations

- [SAS Viya](../technologies/sas/sas-viya.md): Cloud-native analytics and AI platform on Kubernetes that hosts SAS's data management, visual analytics, machine learning, model management, decisioning and streaming products.

