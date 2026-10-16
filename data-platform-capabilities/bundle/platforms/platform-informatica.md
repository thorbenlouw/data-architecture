---
type: Platform
id: platform-informatica
title: Informatica
description: An enterprise data management suite for integration, quality, governance, MDM and privacy, now owned by Salesforce.
vendor: Informatica
resource: https://www.informatica.com/
folder: informatica
order: 7
terminology:
  agent-tool-access: Informatica Headless and MCP servers
  ai-agents: CLAIRE Agents and AI Agent Engineering
  ai-assisted-development: CLAIRE Copilot
  application-integration: Application Integration processes
  bad-data-quarantine: exception management
  change-data-capture: incremental load in Database Ingestion and Replication
  conversational-analytics: CLAIRE GPT
  cost-attribution: IPU consumption metering
  data-anomaly-detection: data observability events
  data-apis: managed APIs in API Center
  data-catalogue: Cloud Data Governance and Catalog (CDGC)
  data-marketplace: Cloud Data Marketplace data collections
  data-policy-management: Data Access Management policies
  data-quality-rules: rule specifications
  data-reconciliation: Data Validation test cases
  database-replication: Database Ingestion and Replication (formerly Mass Ingestion)
  deidentification: data de-identification policies and Data Masking
  deployment-options: Secure Agent and points of delivery (PODs)
  distributed-processing: advanced mode on an advanced cluster
  file-ingestion: File Ingestion and Replication
  low-code-transformation: mappings (Mapping Designer)
  managed-file-transfer: B2B Gateway
  master-data-management: MDM SaaS and 360 applications (Business 360)
  metadata-harvesting: catalog sources and scanners in Metadata Command Center
  multi-tenancy: sub-organisations
  reference-data-management: Reference 360
  serverless-compute: serverless runtime environment
  sql-transformation: SQL ELT mode
  streaming-ingestion: Streaming Ingestion and Replication
  workflow-orchestration: taskflows
families:
- name: Intelligent Data Management Cloud
  aliases: [IDMC, IICS]
  technologies:
  - informatica-idmc
  - informatica-administrator
  - informatica-ipu-pricing
  - informatica-serverless-runtime-environment
  - informatica-operational-insights
  - informatica-cloud-data-integration
  - informatica-cdi-advanced-mode
  - informatica-cdi-sql-elt-mode
  - informatica-cdi-finops
  - informatica-cdi-pc
  - informatica-data-masking-transformation
  - informatica-application-ingestion-and-replication
  - informatica-database-ingestion-and-replication
  - informatica-file-ingestion-and-replication
  - informatica-streaming-ingestion-and-replication
  - informatica-cloud-application-integration
  - informatica-api-center
  - informatica-b2b-gateway
  - informatica-ai-recipes
  - informatica-cloud-data-quality
  - informatica-data-profiling
  - informatica-data-observability
  - informatica-data-validation
  - informatica-cloud-data-governance-and-catalog
  - informatica-metadata-command-center
  - informatica-cdgc-lineage
  - informatica-cdgc-ai-governance
  - informatica-unstructured-data-governance
  - informatica-cloud-data-access-management
  - informatica-cloud-data-marketplace
  - informatica-multidomain-mdm-saas
  - informatica-customer-360
  - informatica-product-360
  - informatica-supplier-360
  - informatica-reference-360
  - informatica-claire-gpt
  - informatica-claire-copilot-data-integration
  - informatica-claire-agents
  - informatica-claire-data-quality-agent
  - informatica-ai-agent-engineering
  - informatica-headless-data-management
  - informatica-data-360-connector-and-scanner
  - informatica-powercenter-cloud-edition
- name: Cloud Data Integration
  aliases: [CDI, Data Integration and Engineering]
  technologies:
  - informatica-cloud-data-integration
  - informatica-cdi-advanced-mode
  - informatica-cdi-sql-elt-mode
  - informatica-cdi-finops
  - informatica-cdi-pc
  - informatica-data-masking-transformation
  - informatica-claire-copilot-data-integration
  - informatica-serverless-runtime-environment
- name: Data Ingestion and Replication
  aliases: [Mass Ingestion, Cloud Mass Ingestion]
  technologies:
  - informatica-application-ingestion-and-replication
  - informatica-database-ingestion-and-replication
  - informatica-file-ingestion-and-replication
  - informatica-streaming-ingestion-and-replication
- name: Informatica Application Integration
  aliases: [CAI]
  technologies: [informatica-cloud-application-integration, informatica-api-center, informatica-ai-recipes]
- name: Informatica Data Quality and Observability
  aliases: [CDQ, Cloud Data Quality]
  technologies:
  - informatica-cloud-data-quality
  - informatica-data-profiling
  - informatica-data-observability
  - informatica-claire-data-quality-agent
- name: Cloud Data Governance and Catalog
  aliases: [CDGC]
  technologies:
  - informatica-cloud-data-governance-and-catalog
  - informatica-metadata-command-center
  - informatica-cdgc-lineage
  - informatica-cdgc-ai-governance
  - informatica-data-observability
  - informatica-unstructured-data-governance
- name: Informatica MDM SaaS
  aliases: [Informatica MDM, Business 360]
  technologies:
  - informatica-multidomain-mdm-saas
  - informatica-customer-360
  - informatica-product-360
  - informatica-supplier-360
  - informatica-reference-360
- name: CLAIRE
  aliases: [CLAIRE AI]
  technologies:
  - informatica-claire-gpt
  - informatica-claire-copilot-data-integration
  - informatica-claire-agents
  - informatica-claire-data-quality-agent
- name: PowerCenter
  aliases: [Informatica PowerCenter modernisation]
  technologies:
  - informatica-powercenter
  - informatica-powercenter-cloud-edition
  - informatica-cdi-pc
  - informatica-data-validation
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Informatica has been owned by Salesforce since 18 November 2025 and now trades as Informatica from Salesforce. It sells enterprise data management software rather than a storage or compute platform. The main product is the Intelligent Data Management Cloud (IDMC), a SaaS control plane hosted in regional points of delivery (PODs) on AWS, Azure and Google Cloud. Jobs run either on customer-installed Secure Agents, which keep data inside the customer's network, or on Informatica-managed serverless runtimes, and every service is paid for in Informatica Processing Units (IPUs).

IDMC services fall into groups. Integration covers Cloud Data Integration (with standard, advanced and SQL ELT mapping modes), Data Ingestion and Replication, Application Integration, API Center and B2B Gateway. Data Quality and Observability, Cloud Data Governance and Catalog with Metadata Command Center, Data Marketplace and Data Access Management cover quality, governance and access. MDM SaaS and the 360 applications master customer, product, supplier and reference data. The AI layer is CLAIRE (GPT, Copilot and Agents), AI Agent Engineering and the MCP servers marketed as Informatica Headless. On-premises PowerCenter is still widely deployed, and PowerCenter Cloud Edition is the route from it to IDMC.

# Notes

- Salesforce positions Informatica as the enterprise data management layer alongside Data 360, MuleSoft, Tableau and Agentforce. Application Integration overlaps with MuleSoft, and the Data 360 connector and scanner (GA Spring 2026) are the main product links so far.
- Much of the processing happens inside other platforms: SQL ELT mode pushes mappings into Snowflake, Databricks, BigQuery, Redshift and Fabric, Data Access Management pushes policies into the same platforms, and Cloud Data Governance and Catalog scans them for metadata and lineage.
- Names have changed over time: Informatica Intelligent Cloud Services (IICS) became IDMC, Cloud Mass Ingestion became Data Ingestion and Replication, and CDI-Elastic became advanced mode. CDI and CDQ are now marketed as Data Integration and Engineering and as Data Quality and Observability.
- Standard support for PowerCenter 10.5.x ended on 31 March 2026, and extended support runs to 31 March 2027.
- On-premises products that architects still meet, such as Informatica Data Quality, Enterprise Data Catalog, Axon Data Governance and on-premises MDM, have cloud successors in CDQ, CDGC and MDM SaaS.
- IPUs come as Standard IPUs, whose allowance expires monthly, or Flex IPUs, whose allowance expires each contract year, and can be bought through the AWS, Azure and Google Cloud marketplaces.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 14 of 22 | [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 2 of 23 | [Data versioning](../capabilities/storage/data-versioning.md), [Object storage](../capabilities/storage/object-storage.md), [Open file formats](../capabilities/storage/file-formats.md), [Open table formats](../capabilities/storage/open-table-formats.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Platform-managed storage](../capabilities/storage/managed-storage.md), [Table catalogue](../capabilities/storage/table-catalogue.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Time travel](../capabilities/storage/time-travel.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 5 of 18 | [AI functions in SQL](../capabilities/processing/ai-functions.md), [DataFrame APIs](../capabilities/processing/dataframe-apis.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Document processing](../capabilities/processing/document-processing.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Self-service data preparation](../capabilities/processing/data-preparation.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [Stream processing](../capabilities/processing/stream-processing.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 3 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md) |
| [Query and compute](../capabilities/compute/compute.md) | 5 of 22 | [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md), [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md), [Query acceleration](../capabilities/compute/query-acceleration.md), [Query federation](../capabilities/compute/query-federation.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Workload management](../capabilities/compute/workload-management.md), [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Materialised views](../capabilities/compute/materialised-views.md), [Result caching](../capabilities/compute/result-caching.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Container services](../capabilities/compute/container-services.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Provisioned compute](../capabilities/compute/provisioned-compute.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 3 of 13 | [Change feeds](../capabilities/serving/change-feeds.md), [Data export](../capabilities/serving/data-export.md), [Decision management](../capabilities/serving/decision-management.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Operational database integration](../capabilities/serving/operational-database.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 2 of 20 | [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 0 of 20 | [Machine learning development](../capabilities/machine-learning/machine-learning.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Feature store](../capabilities/machine-learning/feature-store.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Model training](../capabilities/machine-learning/model-training.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [AutoML](../capabilities/machine-learning/automl.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 2 of 18 | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model deployment](../capabilities/mlops/model-deployment.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 6 of 23 | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Model customisation](../capabilities/generative-ai/model-customisation.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 10 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Model lineage](../capabilities/metadata/model-lineage.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 10 of 12 (+1 in preview) | [Data issue management](../capabilities/data-quality/data-issue-management.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md) (preview only) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 7 of 7 |  |
| [Governance and compliance](../capabilities/governance/governance.md) | 11 of 24 | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data domains](../capabilities/governance/data-domains.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 8 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Encryption](../capabilities/security/encryption.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 3 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 0 of 7 | [Data products](../capabilities/data-products/data-products.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 6 of 16 | [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Data application hosting](../capabilities/development-lifecycle/data-applications.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md), [Notebooks](../capabilities/development-lifecycle/notebooks.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Version control integration](../capabilities/development-lifecycle/version-control.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 11 of 27 | [Backup and disaster recovery](../capabilities/platform-operations/business-continuity.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Database migration](../capabilities/platform-operations/database-migration.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 1 of 10 (+1 in preview) | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Geospatial data](../capabilities/specialised-data/geospatial-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md) (preview only) |

# Product families

- **Intelligent Data Management Cloud** (also: IDMC, IICS): [Informatica Intelligent Data Management Cloud (IDMC)](../technologies/informatica/informatica-idmc.md), [IDMC Administrator](../technologies/informatica/informatica-administrator.md), [Informatica Processing Unit (IPU) consumption pricing](../technologies/informatica/informatica-ipu-pricing.md), [IDMC serverless runtime environment](../technologies/informatica/informatica-serverless-runtime-environment.md), [Informatica Operational Insights](../technologies/informatica/informatica-operational-insights.md), [Informatica Cloud Data Integration (CDI)](../technologies/informatica/informatica-cloud-data-integration.md), [Informatica Cloud Data Integration advanced mode](../technologies/informatica/informatica-cdi-advanced-mode.md), [Informatica Cloud Data Integration SQL ELT mode](../technologies/informatica/informatica-cdi-sql-elt-mode.md), [Informatica Cloud Data Integration FinOps](../technologies/informatica/informatica-cdi-finops.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../technologies/informatica/informatica-cdi-pc.md), [Informatica Data Masking transformation](../technologies/informatica/informatica-data-masking-transformation.md), [Informatica Application Ingestion and Replication](../technologies/informatica/informatica-application-ingestion-and-replication.md), [Informatica Database Ingestion and Replication](../technologies/informatica/informatica-database-ingestion-and-replication.md), [Informatica File Ingestion and Replication](../technologies/informatica/informatica-file-ingestion-and-replication.md), [Informatica Streaming Ingestion and Replication](../technologies/informatica/informatica-streaming-ingestion-and-replication.md), [Informatica Cloud Application Integration (CAI)](../technologies/informatica/informatica-cloud-application-integration.md), [Informatica API Center](../technologies/informatica/informatica-api-center.md), [Informatica B2B Gateway](../technologies/informatica/informatica-b2b-gateway.md), [Informatica AI recipes (Application Integration)](../technologies/informatica/informatica-ai-recipes.md), [Informatica Cloud Data Quality (CDQ)](../technologies/informatica/informatica-cloud-data-quality.md), [Informatica Data Profiling](../technologies/informatica/informatica-data-profiling.md), [Informatica data observability](../technologies/informatica/informatica-data-observability.md), [Informatica Data Validation](../technologies/informatica/informatica-data-validation.md), [Informatica Cloud Data Governance and Catalog (CDGC)](../technologies/informatica/informatica-cloud-data-governance-and-catalog.md), [Informatica Metadata Command Center (MCC)](../technologies/informatica/informatica-metadata-command-center.md), [Informatica CDGC lineage](../technologies/informatica/informatica-cdgc-lineage.md), [Informatica CDGC AI governance](../technologies/informatica/informatica-cdgc-ai-governance.md), [Informatica Unstructured Data Governance](../technologies/informatica/informatica-unstructured-data-governance.md) (preview), [Informatica Cloud Data Access Management (CDAM)](../technologies/informatica/informatica-cloud-data-access-management.md), [Informatica Cloud Data Marketplace (CDMP)](../technologies/informatica/informatica-cloud-data-marketplace.md), [Informatica Multidomain MDM SaaS](../technologies/informatica/informatica-multidomain-mdm-saas.md), [Informatica Customer 360 SaaS](../technologies/informatica/informatica-customer-360.md), [Informatica Product 360 SaaS](../technologies/informatica/informatica-product-360.md), [Informatica Supplier 360 SaaS](../technologies/informatica/informatica-supplier-360.md), [Informatica Reference 360](../technologies/informatica/informatica-reference-360.md), [CLAIRE GPT](../technologies/informatica/informatica-claire-gpt.md), [CLAIRE Copilot for Data Integration](../technologies/informatica/informatica-claire-copilot-data-integration.md), [CLAIRE Agents](../technologies/informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../technologies/informatica/informatica-claire-data-quality-agent.md), [Informatica AI Agent Engineering](../technologies/informatica/informatica-ai-agent-engineering.md) (unconfirmed), [Informatica Headless Data Management (Informatica MCP servers)](../technologies/informatica/informatica-headless-data-management.md), [Informatica Data 360 Connector and Scanner](../technologies/informatica/informatica-data-360-connector-and-scanner.md), [Informatica PowerCenter Cloud Edition (PCCE)](../technologies/informatica/informatica-powercenter-cloud-edition.md)
- **Cloud Data Integration** (also: CDI, Data Integration and Engineering): [Informatica Cloud Data Integration (CDI)](../technologies/informatica/informatica-cloud-data-integration.md), [Informatica Cloud Data Integration advanced mode](../technologies/informatica/informatica-cdi-advanced-mode.md), [Informatica Cloud Data Integration SQL ELT mode](../technologies/informatica/informatica-cdi-sql-elt-mode.md), [Informatica Cloud Data Integration FinOps](../technologies/informatica/informatica-cdi-finops.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../technologies/informatica/informatica-cdi-pc.md), [Informatica Data Masking transformation](../technologies/informatica/informatica-data-masking-transformation.md), [CLAIRE Copilot for Data Integration](../technologies/informatica/informatica-claire-copilot-data-integration.md), [IDMC serverless runtime environment](../technologies/informatica/informatica-serverless-runtime-environment.md)
- **Data Ingestion and Replication** (also: Mass Ingestion, Cloud Mass Ingestion): [Informatica Application Ingestion and Replication](../technologies/informatica/informatica-application-ingestion-and-replication.md), [Informatica Database Ingestion and Replication](../technologies/informatica/informatica-database-ingestion-and-replication.md), [Informatica File Ingestion and Replication](../technologies/informatica/informatica-file-ingestion-and-replication.md), [Informatica Streaming Ingestion and Replication](../technologies/informatica/informatica-streaming-ingestion-and-replication.md)
- **Informatica Application Integration** (also: CAI): [Informatica Cloud Application Integration (CAI)](../technologies/informatica/informatica-cloud-application-integration.md), [Informatica API Center](../technologies/informatica/informatica-api-center.md), [Informatica AI recipes (Application Integration)](../technologies/informatica/informatica-ai-recipes.md)
- **Informatica Data Quality and Observability** (also: CDQ, Cloud Data Quality): [Informatica Cloud Data Quality (CDQ)](../technologies/informatica/informatica-cloud-data-quality.md), [Informatica Data Profiling](../technologies/informatica/informatica-data-profiling.md), [Informatica data observability](../technologies/informatica/informatica-data-observability.md), [CLAIRE Data Quality Agent](../technologies/informatica/informatica-claire-data-quality-agent.md)
- **Cloud Data Governance and Catalog** (also: CDGC): [Informatica Cloud Data Governance and Catalog (CDGC)](../technologies/informatica/informatica-cloud-data-governance-and-catalog.md), [Informatica Metadata Command Center (MCC)](../technologies/informatica/informatica-metadata-command-center.md), [Informatica CDGC lineage](../technologies/informatica/informatica-cdgc-lineage.md), [Informatica CDGC AI governance](../technologies/informatica/informatica-cdgc-ai-governance.md), [Informatica data observability](../technologies/informatica/informatica-data-observability.md), [Informatica Unstructured Data Governance](../technologies/informatica/informatica-unstructured-data-governance.md) (preview)
- **Informatica MDM SaaS** (also: Informatica MDM, Business 360): [Informatica Multidomain MDM SaaS](../technologies/informatica/informatica-multidomain-mdm-saas.md), [Informatica Customer 360 SaaS](../technologies/informatica/informatica-customer-360.md), [Informatica Product 360 SaaS](../technologies/informatica/informatica-product-360.md), [Informatica Supplier 360 SaaS](../technologies/informatica/informatica-supplier-360.md), [Informatica Reference 360](../technologies/informatica/informatica-reference-360.md)
- **CLAIRE** (also: CLAIRE AI): [CLAIRE GPT](../technologies/informatica/informatica-claire-gpt.md), [CLAIRE Copilot for Data Integration](../technologies/informatica/informatica-claire-copilot-data-integration.md), [CLAIRE Agents](../technologies/informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../technologies/informatica/informatica-claire-data-quality-agent.md)
- **PowerCenter** (also: Informatica PowerCenter modernisation): [Informatica PowerCenter](../technologies/informatica/informatica-powercenter.md), [Informatica PowerCenter Cloud Edition (PCCE)](../technologies/informatica/informatica-powercenter-cloud-edition.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../technologies/informatica/informatica-cdi-pc.md), [Informatica Data Validation](../technologies/informatica/informatica-data-validation.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| advanced mode on an advanced cluster | [Distributed processing](../capabilities/processing/distributed-processing.md) |
| Application Integration processes | [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| B2B Gateway | [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md) |
| catalog sources and scanners in Metadata Command Center | [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md) |
| CLAIRE Agents and AI Agent Engineering | [AI agents](../capabilities/generative-ai/ai-agents.md) |
| CLAIRE Copilot | [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md) |
| CLAIRE GPT | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| Cloud Data Governance and Catalog (CDGC) | [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| Cloud Data Marketplace data collections | [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| Data Access Management policies | [Policy management](../capabilities/governance/data-policy-management.md) |
| data de-identification policies and Data Masking | [De-identification](../capabilities/governance/deidentification.md) |
| data observability events | [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md) |
| Data Validation test cases | [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) |
| Database Ingestion and Replication (formerly Mass Ingestion) | [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md) |
| exception management | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md) |
| File Ingestion and Replication | [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| incremental load in Database Ingestion and Replication | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) |
| Informatica Headless and MCP servers | [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) |
| IPU consumption metering | [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) |
| managed APIs in API Center | [Data APIs](../capabilities/serving/data-apis.md) |
| mappings (Mapping Designer) | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| MDM SaaS and 360 applications (Business 360) | [Master data management](../capabilities/master-data/master-data-management.md) |
| Reference 360 | [Reference data management](../capabilities/master-data/reference-data-management.md) |
| rule specifications | [Data quality rules](../capabilities/data-quality/data-quality-rules.md) |
| Secure Agent and points of delivery (PODs) | [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md) |
| serverless runtime environment | [Serverless compute](../capabilities/compute/serverless-compute.md) |
| SQL ELT mode | [SQL transformation](../capabilities/processing/sql-transformation.md) |
| Streaming Ingestion and Replication | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |
| sub-organisations | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| taskflows | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |

# Technologies

## Ingestion and integration

- [Informatica Application Ingestion and Replication](../technologies/informatica/informatica-application-ingestion-and-replication.md): Replicates objects from SaaS and on-premises applications such as Salesforce, SAP and Workday to warehouses, lakes and streaming targets, as a snapshot or continuous change propagation.
- [Informatica B2B Gateway](../technologies/informatica/informatica-b2b-gateway.md): Exchanges EDI messages and files with trading partners and maps them to back-end systems using prebuilt mappings, with a partners portal for tracking exchanged files.
- [Informatica Cloud Application Integration (CAI)](../technologies/informatica/informatica-cloud-application-integration.md): Designs and runs event-driven and API-driven processes and service connectors that integrate applications in near real time, including over Kafka, JMS, AMQP, Azure Service Bus, Amazon SQS/SNS and Google Pub/Sub.
- [Informatica Data 360 Connector and Scanner](../technologies/informatica/informatica-data-360-connector-and-scanner.md): Native connector for two-way batch and real-time data exchange with Salesforce Data 360, plus a catalogue scanner that brings Data 360 and Agentforce Marketing objects into CDGC lineage.
- [Informatica Database Ingestion and Replication](../technologies/informatica/informatica-database-ingestion-and-replication.md): Replicates relational and some non-relational databases to cloud warehouses, lakes, streaming platforms and databases, as an initial bulk load, as continuous log-based change capture, or as both in sequence.
- [Informatica File Ingestion and Replication](../technologies/informatica/informatica-file-ingestion-and-replication.md): Moves large numbers of files of any type between on-premises and cloud repositories, and tracks and monitors each transfer.
- [Informatica Streaming Ingestion and Replication](../technologies/informatica/informatica-streaming-ingestion-and-replication.md): Moves real-time streaming and machine data from sources such as message brokers, logs and IoT hubs to messaging systems and to lake or warehouse targets.

## Processing and transformation

- [Informatica Cloud Data Integration (CDI)](../technologies/informatica/informatica-cloud-data-integration.md): Visual ETL and ELT service: you design mappings from prebuilt transformations and connectors, run them as tasks, and chain tasks into taskflows.
- [Informatica Cloud Data Integration advanced mode](../technologies/informatica/informatica-cdi-advanced-mode.md): Runs Data Integration mappings on a Kubernetes-based advanced cluster for distributed processing of large and hierarchical data, with Python and Java code steps and machine learning model calls.
- [Informatica Cloud Data Integration SQL ELT mode](../technologies/informatica/informatica-cdi-sql-elt-mode.md): Converts mapping logic into native SQL and platform commands that run inside the target cloud warehouse, so data does not leave the warehouse's cloud while it is transformed.
- [Informatica PowerCenter](../technologies/informatica/informatica-powercenter.md): On-premises enterprise ETL server with a client designer, repository and workflow engine, and the historical core of Informatica's integration business.

## Query and compute

- [IDMC serverless runtime environment](../technologies/informatica/informatica-serverless-runtime-environment.md): Informatica-managed, single-tenant runtime that runs jobs, chiefly advanced-mode mappings, without the customer installing or maintaining Secure Agents, scaling the underlying cluster with the workload.

## Serving and activation

- [Informatica API Center](../technologies/informatica/informatica-api-center.md): Designs, publishes, secures with policies, groups and monitors REST APIs, either top-down from an API definition or bottom-up from published Application Integration processes.

## Analytics and BI

- [CLAIRE GPT](../technologies/informatica/informatica-claire-gpt.md): Conversational IDMC service that answers natural-language questions about metadata and data, finds assets, checks quality and creates or runs data management tasks with human oversight.

## Generative AI

- [CLAIRE Agents](../technologies/informatica/informatica-claire-agents.md): Prebuilt AI agents that plan and carry out multi-step data management work such as discovering trusted data, exploring MDM data, building ELT pipelines and writing data quality rules.
- [Informatica AI Agent Engineering](../technologies/informatica/informatica-ai-agent-engineering.md) (unconfirmed): No-code IDMC service for building, connecting and managing AI agents and multi-agent systems, including connecting to Informatica-managed MCP servers and building composite MCP servers from Application Integration processes.
- [Informatica AI recipes (Application Integration)](../technologies/informatica/informatica-ai-recipes.md): Prebuilt Application Integration processes for generative AI patterns such as AI agents, retrieval over documents, chat with a file, and LLM calls to several model providers.
- [Informatica Headless Data Management (Informatica MCP servers)](../technologies/informatica/informatica-headless-data-management.md): Exposes IDMC functions such as catalogue search, lineage, data quality, MDM lookups, job control and administration as governed MCP servers that external agents and AI tools can call without custom code.

## Metadata and discovery

- [Informatica CDGC lineage](../technologies/informatica/informatica-cdgc-lineage.md): Builds end-to-end lineage, including inferred links, across scanned databases, ETL tools, cloud platforms and BI tools, down to column level, for tracing and impact analysis.
- [Informatica Cloud Data Governance and Catalog (CDGC)](../technologies/informatica/informatica-cloud-data-governance-and-catalog.md): Catalogue and governance service that inventories technical, business and AI assets, links them to a business glossary, policies and stewards, classifies sensitive data, and shows data quality scores per asset.
- [Informatica Metadata Command Center (MCC)](../technologies/informatica/informatica-metadata-command-center.md): Administration service where you configure catalog sources and scanners that harvest metadata, lineage, profiles and classifications from source systems into the IDMC metadata repository.

## Data quality and observability

- [CLAIRE Data Quality Agent](../technologies/informatica/informatica-claire-data-quality-agent.md): AI agent that turns data quality requirements written in plain language into rule logic that can be reviewed and deployed to production.
- [Informatica Cloud Data Quality (CDQ)](../technologies/informatica/informatica-cloud-data-quality.md): Defines and runs rule specifications, cleansing, parsing, standardisation, deduplication and verification assets using reference dictionaries, and routes exceptions to people for review.
- [Informatica data observability](../technologies/informatica/informatica-data-observability.md): Learns normal trends in scanned source data, raises events for sudden deviations, grouped by metric and severity, and improves its alerts from how users respond to them.
- [Informatica Data Profiling](../technologies/informatica/informatica-data-profiling.md): Profiles columns in data sources to show value frequencies, patterns, data types and completeness.
- [Informatica Data Validation](../technologies/informatica/informatica-data-validation.md): Compares two data sets through repeatable test cases and test suites to verify that integration or migration output is complete and accurate, with reports and REST APIs.

## Master and reference data

- [Informatica Customer 360 SaaS](../technologies/informatica/informatica-customer-360.md): Prebuilt customer master application on MDM SaaS that consolidates customer records, relationships and inferred attributes into one shared view.
- [Informatica Multidomain MDM SaaS](../technologies/informatica/informatica-multidomain-mdm-saas.md): Cloud MDM service for modelling any business entity, matching and merging records from many sources into golden records with survivorship rules, and managing relationships and hierarchies through the Business 360 Console.
- [Informatica Product 360 SaaS](../technologies/informatica/informatica-product-360.md): Product information management application that centralises product data and digital assets, classifies products into hierarchies and prepares content for sales channels.
- [Informatica Reference 360](../technologies/informatica/informatica-reference-360.md): Manages shared reference data such as code lists, hierarchies and cross-system mappings with versions and approval workflows.
- [Informatica Supplier 360 SaaS](../technologies/informatica/informatica-supplier-360.md): Supplier master application covering supplier onboarding workflows, mastering, hierarchies, risk, performance and compliance data.

## Governance and compliance

- [Informatica CDGC AI governance](../technologies/informatica/informatica-cdgc-ai-governance.md): Catalogues AI models, multi-agent systems and their data and links them to policies, owners and lineage, including assets scanned from platforms such as Google Vertex AI.
- [Informatica Cloud Data Access Management (CDAM)](../technologies/informatica/informatica-cloud-data-access-management.md): Defines data filter, access control and de-identification policies once, driven by catalogue metadata, and enforces them by pushing them into data platforms or by applying them inside Informatica pipelines and marketplace deliveries.
- [Informatica Data Masking transformation](../technologies/informatica/informatica-data-masking-transformation.md): Mapping transformation that replaces sensitive values with realistic masked values per column while keeping referential integrity across tables, for non-production copies.

## Security and access

- [IDMC Administrator](../technologies/informatica/informatica-administrator.md): Organisation-wide administration service for users, groups, roles, SAML single sign-on, licences, runtime environments, connections and sub-organisations.

## Data sharing and collaboration

- [Informatica Cloud Data Marketplace (CDMP)](../technologies/informatica/informatica-cloud-data-marketplace.md): Internal data shop where owners publish data collections with terms of use, and consumers search, compare, order and receive data through approval and delivery workflows.

## Development and DataOps

- [CLAIRE Copilot for Data Integration](../technologies/informatica/informatica-claire-copilot-data-integration.md): Assistant in the Data Integration and Application Integration designers that generates, explains and summarises pipelines from natural-language prompts.
- [Informatica Test Data Management (TDM)](../technologies/informatica/informatica-test-data-management.md): On-premises product for configuring data subsetting, masking, synthetic data generation and sensitive data discovery for test environments from one web console.

## Platform operations

- [Informatica Cloud Data Integration FinOps](../technologies/informatica/informatica-cdi-finops.md): Shows the cost and resource use of each workload and pipeline, and recommends or applies tuning to lower IPU and cloud compute spend.
- [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../technologies/informatica/informatica-cdi-pc.md): Runs existing PowerCenter sessions and workflows unchanged in a customer-hosted domain whose management, monitoring and upgrades are handled from IDMC.
- [Informatica Intelligent Data Management Cloud (IDMC)](../technologies/informatica/informatica-idmc.md): Multi-cloud SaaS platform that hosts all of Informatica's cloud data management services behind one control plane, with jobs run either on customer-hosted Secure Agents or on Informatica-managed serverless runtimes.
- [Informatica Operational Insights](../technologies/informatica/informatica-operational-insights.md): Monitoring service that shows the performance, health and efficiency of Informatica assets, including registered on-premises PowerCenter and Data Engineering domains as well as IDMC jobs.
- [Informatica PowerCenter Cloud Edition (PCCE)](../technologies/informatica/informatica-powercenter-cloud-edition.md): Modernisation bundle that runs PowerCenter workloads under IDMC management (CDI-PC), converts PowerCenter assets to native Cloud Data Integration (PC2CDI) and checks the converted output with Data Validation.
- [Informatica Processing Unit (IPU) consumption pricing](../technologies/informatica/informatica-ipu-pricing.md): Single consumption currency for IDMC services, with usage metered and reported by service, runtime, sub-organisation and sandbox, so spend can be tracked and charged back.

## Specialised data types

- [Informatica Unstructured Data Governance](../technologies/informatica/informatica-unstructured-data-governance.md) (preview): Scans, extracts metadata from and classifies unstructured files such as PDFs and text documents, and catalogues them in CDGC.

