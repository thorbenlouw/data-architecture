---
type: Platform
id: platform-sap
title: SAP
description: SAP's data and analytics services for data from SAP business applications and other sources.
vendor: SAP
resource: https://www.sap.com/
folder: sap
order: 10
terminology:
  ai-agents: Joule Agents / Joule Assistants
  change-data-capture: Replication flows
  conversational-analytics: Joule / Just Ask
  data-marketplace: Data Marketplace (Datasphere)
  data-products: Data products (BDC)
  foundation-model-access: Generative AI hub
  low-code-transformation: Data flows / transformation flows
  multi-tenancy: Spaces
  row-level-security: Data access controls
  semantic-layer: Business Builder / analytic models
  workflow-orchestration: Task chains
families:
- name: SAP Business Data Cloud
  aliases: [BDC, SAP BDC]
  technologies:
  - sap-business-data-cloud
  - sap-bdc-data-products
  - sap-bdc-data-product-studio
  - sap-bdc-connect
  - sap-datasphere
  - sap-analytics-cloud
  - sap-business-warehouse-bdc
  - sap-databricks
  - sap-snowflake
- name: SAP Datasphere
  technologies: [sap-datasphere, sap-datasphere-catalog, sap-datasphere-replication-flows]
- name: SAP HANA Cloud
  technologies:
  - sap-hana-cloud
  - sap-hana-cloud-vector-engine
  - sap-hana-cloud-knowledge-graph-engine
  - sap-hana-cloud-data-lake
- name: SAP Business Warehouse
  aliases: [SAP BW]
  technologies: [sap-bw4hana, sap-business-warehouse-bdc]
- name: SAP Joule
  aliases: [Joule]
  technologies: [sap-joule, sap-joule-studio]
- name: SAP Business AI Platform
  aliases: [SAP Business AI]
  technologies: [sap-business-data-cloud, sap-knowledge-graph, sap-joule-studio]
- name: SAP Business Technology Platform
  aliases: [SAP BTP, BTP]
  technologies: [sap-hana-cloud, sap-ai-foundation, sap-integration-suite, sap-joule-studio]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

SAP's data offering centres on SAP Business Data Cloud (BDC), a managed SaaS service launched in February 2025. BDC lands SAP-managed data products from SAP applications in a shared object store and shares them, without copying, with SAP Datasphere (modelling, federation and integration), SAP Analytics Cloud (BI and planning), SAP Business Warehouse in BDC and the partner engines that SAP sells and runs inside BDC: SAP Databricks and, announced in November 2025, SAP Snowflake. BDC Connect shares the same data products with customers' existing Databricks, Google BigQuery and Snowflake estates. SAP HANA Cloud is the multi-model database underneath, with vector, knowledge graph and data lake components.

For AI, SAP groups BDC, SAP Knowledge Graph and Joule Studio as the SAP Business AI Platform. Joule and its agents are the user-facing assistant, and the AI Foundation on SAP BTP (SAP AI Core and the generative AI hub) gives governed access to models. SAP Master Data Governance, SAP Integration Suite and the SLT replication server cover master data, application integration and replication from SAP systems.

On 4 May 2026 SAP announced that it would acquire Dremio, the Apache Iceberg lakehouse and catalogue vendor and a co-creator of Apache Polaris, to become the open lakehouse and catalogue layer of Business Data Cloud. Dremio now presents itself as part of SAP; its product is described under [Dremio Cloud](../technologies/sap/dremio-cloud.md).

# Notes

- SAP Databricks and SAP Snowflake are redistributions: SAP sells and operates them inside BDC, and their detailed features are those of the Databricks and Snowflake platforms.
- SAP Data Intelligence Cloud is no longer developed as a strategic product; Datasphere replication and transformation flows and BDC replace it.
- Many SAP estates still run SAP BW 7.5 or BW/4HANA. SAP's direction is BW in BDC and Datasphere, and BW 7.5 reaches the end of mainstream maintenance at the end of 2027.
- Replication from Datasphere to non-SAP targets is licensed separately, by premium outbound volume.
- SAP AI Agent Hub, part of SAP LeanIX, keeps an inventory of SAP and non-SAP agents and MCP servers and records which are approved.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 10 of 22 | [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Database extraction](../capabilities/ingestion-integration/database-extraction.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 7 of 23 | [Data versioning](../capabilities/storage/data-versioning.md), [Open file formats](../capabilities/storage/file-formats.md), [Open table formats](../capabilities/storage/open-table-formats.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Time travel](../capabilities/storage/time-travel.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 3 of 18 | [AI functions in SQL](../capabilities/processing/ai-functions.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [DataFrame APIs](../capabilities/processing/dataframe-apis.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Distributed processing](../capabilities/processing/distributed-processing.md), [Document processing](../capabilities/processing/document-processing.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Self-service data preparation](../capabilities/processing/data-preparation.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [Stream processing](../capabilities/processing/stream-processing.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 2 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md) |
| [Query and compute](../capabilities/compute/compute.md) | 5 of 22 | [Compute provisioning options](../capabilities/compute/compute-options.md), [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Workload management](../capabilities/compute/workload-management.md), [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Materialised views](../capabilities/compute/materialised-views.md), [Result caching](../capabilities/compute/result-caching.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Container services](../capabilities/compute/container-services.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Provisioned compute](../capabilities/compute/provisioned-compute.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Serverless compute](../capabilities/compute/serverless-compute.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 5 of 13 | [Decision management](../capabilities/serving/decision-management.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 11 of 20 | [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Feature store](../capabilities/machine-learning/feature-store.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Model training](../capabilities/machine-learning/model-training.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [AutoML](../capabilities/machine-learning/automl.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 2 of 18 | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model governance](../capabilities/mlops/model-governance.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 12 of 23 | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Model customisation](../capabilities/generative-ai/model-customisation.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 8 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [Model lineage](../capabilities/metadata/model-lineage.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 2 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 4 of 7 | [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 6 of 24 | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data classification](../capabilities/governance/data-classification.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Policy management](../capabilities/governance/data-policy-management.md), [Privacy management](../capabilities/governance/privacy-management.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [De-identification](../capabilities/governance/deidentification.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md) |
| [Security and access](../capabilities/security/security.md) | 3 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Audit logging](../capabilities/security/audit-logging.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Encryption](../capabilities/security/encryption.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Privileged access management](../capabilities/security/privileged-access.md), [Role-based access control](../capabilities/security/role-based-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 5 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 4 of 7 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 2 of 16 | [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Data application hosting](../capabilities/development-lifecycle/data-applications.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md), [Notebooks](../capabilities/development-lifecycle/notebooks.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 4 of 27 | [Backup and disaster recovery](../capabilities/platform-operations/business-continuity.md), [Cost management](../capabilities/platform-operations/cost-management.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Platform observability](../capabilities/platform-operations/platform-observability.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Customer-hosted data plane](../capabilities/platform-operations/hybrid-data-plane.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 6 of 10 | [Full-text search](../capabilities/specialised-data/full-text-search.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md) |

# Product families

- **SAP Business Data Cloud** (also: BDC, SAP BDC): [SAP Business Data Cloud](../technologies/sap/sap-business-data-cloud.md), [SAP Business Data Cloud data products](../technologies/sap/sap-bdc-data-products.md), [SAP Business Data Cloud data product studio](../technologies/sap/sap-bdc-data-product-studio.md) (unconfirmed), [SAP Business Data Cloud Connect](../technologies/sap/sap-bdc-connect.md), [SAP Datasphere](../technologies/sap/sap-datasphere.md), [SAP Analytics Cloud](../technologies/sap/sap-analytics-cloud.md), [SAP Business Warehouse in SAP Business Data Cloud](../technologies/sap/sap-business-warehouse-bdc.md), [SAP Databricks](../technologies/sap/sap-databricks.md) (distribution of Databricks), [SAP Snowflake](../technologies/sap/sap-snowflake.md) (unconfirmed; distribution of Snowflake)
- **SAP Datasphere**: [SAP Datasphere](../technologies/sap/sap-datasphere.md), [SAP Datasphere catalog and Data Marketplace](../technologies/sap/sap-datasphere-catalog.md), [SAP Datasphere replication flows](../technologies/sap/sap-datasphere-replication-flows.md)
- **SAP HANA Cloud**: [SAP HANA Cloud](../technologies/sap/sap-hana-cloud.md), [SAP HANA Cloud vector engine](../technologies/sap/sap-hana-cloud-vector-engine.md), [SAP HANA Cloud knowledge graph engine](../technologies/sap/sap-hana-cloud-knowledge-graph-engine.md), [SAP HANA Cloud, data lake](../technologies/sap/sap-hana-cloud-data-lake.md)
- **SAP Business Warehouse** (also: SAP BW): [SAP BW/4HANA](../technologies/sap/sap-bw4hana.md), [SAP Business Warehouse in SAP Business Data Cloud](../technologies/sap/sap-business-warehouse-bdc.md)
- **SAP Joule** (also: Joule): [SAP Joule and Joule agents](../technologies/sap/sap-joule.md), [SAP Joule Studio](../technologies/sap/sap-joule-studio.md)
- **SAP Business AI Platform** (also: SAP Business AI): [SAP Business Data Cloud](../technologies/sap/sap-business-data-cloud.md), [SAP Knowledge Graph](../technologies/sap/sap-knowledge-graph.md), [SAP Joule Studio](../technologies/sap/sap-joule-studio.md)
- **SAP Business Technology Platform** (also: SAP BTP, BTP): [SAP HANA Cloud](../technologies/sap/sap-hana-cloud.md), [SAP AI Foundation (SAP AI Core and generative AI hub)](../technologies/sap/sap-ai-foundation.md), [SAP Integration Suite](../technologies/sap/sap-integration-suite.md), [SAP Joule Studio](../technologies/sap/sap-joule-studio.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Business Builder / analytic models | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) |
| Data access controls | [Row-level security](../capabilities/security/row-level-security.md) |
| Data flows / transformation flows | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| Data Marketplace (Datasphere) | [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| Data products (BDC) | [Data products](../capabilities/data-products/data-products.md) |
| Generative AI hub | [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |
| Joule / Just Ask | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| Joule Agents / Joule Assistants | [AI agents](../capabilities/generative-ai/ai-agents.md) |
| Replication flows | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) |
| Spaces | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| Task chains | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |

# Technologies

## Ingestion and integration

- [SAP Datasphere replication flows](../technologies/sap/sap-datasphere-replication-flows.md): Datasphere feature that copies tables and CDS views from SAP and other sources in initial and delta mode into Datasphere or into external targets such as object stores, Kafka and cloud warehouses.
- [SAP Integration Suite](../technologies/sap/sap-integration-suite.md): SAP BTP integration platform for process integration, API management, B2B and EDI exchange and event brokering between SAP and third-party applications.
- [SAP Landscape Transformation Replication Server](../technologies/sap/sap-landscape-transformation.md): Trigger-based replication server that captures changes from SAP ABAP systems and other databases and applies them in near real time to HANA or other targets.

## Storage and table management

- [SAP HANA Cloud, data lake](../technologies/sap/sap-hana-cloud-data-lake.md): Low-cost storage tier of SAP HANA Cloud with data lake Files for object storage and a data lake Relational Engine for SQL over large, colder datasets.

## Processing and transformation

- [SAP Business Warehouse in SAP Business Data Cloud](../technologies/sap/sap-business-warehouse-bdc.md): Hosted SAP BW in BDC whose Data Product Generator turns BW InfoProvider data into data products in the BDC object store for Datasphere and Databricks to use.
- [SAP BW/4HANA](../technologies/sap/sap-bw4hana.md): SAP's on-premises data warehouse application on SAP HANA, with modelled InfoProviders, extractors for SAP sources and query design for BI.
- [SAP Databricks](../technologies/sap/sap-databricks.md) (distribution of Databricks): SAP-sold and SAP-managed Databricks workspace embedded in BDC, for notebooks, Spark pipelines, serverless SQL and ML over SAP data products shared with Delta Sharing.
- [SAP Datasphere](../technologies/sap/sap-datasphere.md): SAP's cloud data warehouse and data fabric service for integrating, modelling, federating and governing SAP and non-SAP data in isolated spaces with business semantics.

## Orchestration

- [SAP Data Intelligence Cloud](../technologies/sap/sap-data-intelligence-cloud.md) (deprecated): SAP's earlier pipeline, orchestration and metadata service for integrating SAP and non-SAP data and running ML pipelines.

## Query and compute

- [Dremio Cloud](../technologies/sap/dremio-cloud.md): Managed lakehouse query service built on Apache Iceberg, with an Iceberg catalogue, automatic query acceleration and an AI semantic layer.
- [SAP Business Data Cloud Connect](../technologies/sap/sap-bdc-connect.md): Bidirectional, zero-copy sharing of data and metadata between BDC and a customer's existing Databricks, Google BigQuery or Snowflake environment.
- [SAP Snowflake](../technologies/sap/sap-snowflake.md) (unconfirmed; distribution of Snowflake): SAP-sold and SAP-operated Snowflake offering added to BDC as a solution extension, sharing SAP data products with Snowflake in both directions without copying.

## Serving and activation

- [SAP HANA Cloud](../technologies/sap/sap-hana-cloud.md): Managed in-memory, multi-model database on SAP BTP for transactional and analytical work across relational, document, spatial, graph, time-series and vector data.

## Analytics and BI

- [SAP Analytics Cloud](../technologies/sap/sap-analytics-cloud.md): SaaS service that combines BI stories and dashboards, enterprise planning and predictive analysis, with live connections to SAP sources and Joule for natural-language questions.

## Generative AI

- [SAP AI Agent Hub](../technologies/sap/sap-ai-agent-hub.md): Capability of SAP LeanIX that discovers SAP and non-SAP AI agents and MCP servers, maps them to applications and processes, and tracks which are approved for use.
- [SAP AI Foundation (SAP AI Core and generative AI hub)](../technologies/sap/sap-ai-foundation.md): SAP BTP services for running custom AI, with the generative AI hub giving governed access to many LLMs plus orchestration, grounding, content filtering and data masking.
- [SAP HANA Cloud vector engine](../technologies/sap/sap-hana-cloud-vector-engine.md): Vector data type, similarity functions and indexes in SAP HANA Cloud for semantic search and retrieval next to business data.
- [SAP Joule and Joule agents](../technologies/sap/sap-joule.md): SAP's AI assistant across its applications, with agents (marketed in 2026 as Joule Assistants) that carry out multi-step business tasks under the user's authorisations.
- [SAP Joule Studio](../technologies/sap/sap-joule-studio.md): Capability in SAP Build for building Joule skills and custom agents, from no-code to pro-code, with model choice, tool access and connection to MCP servers.

## Metadata and discovery

- [SAP Datasphere catalog and Data Marketplace](../technologies/sap/sap-datasphere-catalog.md): Catalogue for discovering and describing assets across Datasphere and connected systems, with glossary terms and KPIs, plus a marketplace for publishing and subscribing to data products.

## Master and reference data

- [SAP Master Data Governance](../technologies/sap/sap-master-data-governance.md): Application for central creation, consolidation and governed maintenance of master data with workflows, validation rules and quality monitoring, on S/4HANA or as a cloud edition on BTP.

## Data sharing and collaboration

- [SAP Business Data Cloud](../technologies/sap/sap-business-data-cloud.md): Managed SaaS data platform that unifies SAP application data as governed data products on a shared object store and exposes it to Datasphere, SAP Analytics Cloud, SAP Databricks and SAP Snowflake without copying.

## Data products

- [SAP Business Data Cloud data product studio](../technologies/sap/sap-bdc-data-product-studio.md) (unconfirmed): Tooling in BDC for creating, modelling and managing customer-defined data products with SQL or visual transformations, schema, lineage, versioning and lifecycle states.
- [SAP Business Data Cloud data products](../technologies/sap/sap-bdc-data-products.md): SAP-managed, curated datasets with business metadata for core processes in SAP Cloud ERP, SuccessFactors and other applications, populated automatically from the source systems.

## Specialised data types

- [SAP HANA Cloud knowledge graph engine](../technologies/sap/sap-hana-cloud-knowledge-graph-engine.md): RDF triple store with SPARQL in SAP HANA Cloud, which can generate graphs automatically from database metadata for semantic search and agent grounding.
- [SAP Knowledge Graph](../technologies/sap/sap-knowledge-graph.md): SAP-managed graph of business entities, fields and relationships across SAP applications that gives Joule and custom agents business context.

