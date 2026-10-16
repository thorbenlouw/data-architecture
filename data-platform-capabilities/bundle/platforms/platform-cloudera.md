---
type: Platform
id: platform-cloudera
title: Cloudera
description: A hybrid data platform for on-premises and cloud deployments that grew out of the Hadoop ecosystem.
vendor: Cloudera
resource: https://www.cloudera.com/
folder: cloudera
order: 8
terminology:
  access-control: Apache Ranger (SDX)
  ad-hoc-analysis: Cloudera Data Explorer (Hue)
  data-applications: Applications (AI Workbench)
  experiment-tracking: Experiments
  low-code-transformation: Flow Designer (NiFi)
  model-registry: AI Registry
  multi-tenancy: Environments
  provisioned-compute: Data Hub clusters
  streaming-sql: SQL Stream Builder
  table-catalogue: Hive Metastore / Iceberg REST Catalog
  table-maintenance: Lakehouse Optimizer
  workflow-orchestration: Cloudera Data Engineering Airflow
  workload-isolation: Virtual Warehouses
families:
- name: Cloudera AI
  aliases: [Cloudera Machine Learning, CML]
  technologies:
  - cloudera-ai-workbench
  - cloudera-ai-registry
  - cloudera-ai-inference-service
  - cloudera-ai-studios
  - cloudera-agent-studio
- name: Cloudera Shared Data Experience
  aliases: [SDX]
  technologies: [cloudera-sdx, cloudera-data-catalog]
- name: Cloudera Open Data Lakehouse
  aliases: [Cloudera Lakehouse]
  technologies:
  - cloudera-lakehouse-iceberg
  - cloudera-iceberg-rest-catalog
  - cloudera-lakehouse-optimizer
  - cloudera-data-warehouse
  - cloudera-ozone
- name: Cloudera Stream Processing
  aliases: [CSP]
  technologies: [cloudera-streams-messaging, cloudera-streaming-analytics]
- name: Cloudera Data Platform
  aliases: [CDP]
  technologies: [cloudera-on-cloud, cloudera-data-services-on-premises, cloudera-base-on-premises]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cloudera sells a hybrid data and AI platform assembled from open-source engines (Spark, Hive, Impala, Trino, Kafka, Flink, NiFi, HBase and Ozone) over Apache Iceberg tables. The Shared Data Experience (SDX), made up of Apache Ranger, Apache Atlas, Apache Knox and the Hive Metastore, applies one set of security and governance policies to every engine. The same Cloudera Runtime is delivered in three forms: Cloudera on cloud, which runs in the customer's AWS, Azure or Google Cloud account under a Cloudera-hosted control plane; Cloudera Base on premises, the cluster platform managed by Cloudera Manager; and Cloudera Data Services on premises, the containerised services that run on Kubernetes beside a Base cluster.

On top sit the data services: Data Engineering (Spark with Airflow), Data Warehouse (Impala, Hive and Trino virtual warehouses), Data Flow (NiFi), Operational Database (HBase with Phoenix), Kafka and Flink for streaming, and Cloudera AI (AI Workbench, AI Registry, the AI Inference service, AI Studios and Agent Studio). Cloudera Data Lineage, based on the acquired Octopai, adds lineage across tools outside Cloudera. Cloudera Anywhere Cloud, announced in August 2026, is a new control plane that deploys Cloudera, partner and open-source engines from blueprints over Iceberg and an Apache Polaris catalogue across public clouds, sovereign clouds and data centres.

# Notes

- "CDP" is no longer a product name: CDP Public Cloud became Cloudera on cloud, CDP Private Cloud Base became Cloudera Base on premises and CDP Private Cloud Data Services became Cloudera Data Services on premises.
- Older CDH and HDP clusters are still common and usually move to Cloudera Base on premises or Cloudera on cloud. Cloudera states that it will support Runtime 7.3.2 until 2032.
- Governance is split: SDX governs data inside the platform, while Cloudera Data Lineage (also sold as Cloudera Octopai Data Lineage) is a separate SaaS product for estate-wide lineage.
- Most features come from Apache projects packaged in Cloudera Runtime, so the same feature can appear in Base, in Data Hub clusters on cloud and in the data services.
- On Cloudera on cloud, compute and storage run in the customer's own cloud account and are billed by the cloud provider, separately from Cloudera's charges.
- Acquisitions behind current products are Verta (2024, AI Registry), Octopai (2024, Data Lineage) and Taikun (2025, Kubernetes management).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 9 of 22 | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 11 of 23 | [Open file formats](../capabilities/storage/file-formats.md), [Platform-managed storage](../capabilities/storage/managed-storage.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 8 of 18 | [AI functions in SQL](../capabilities/processing/ai-functions.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Document processing](../capabilities/processing/document-processing.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Self-service data preparation](../capabilities/processing/data-preparation.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 2 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md) |
| [Query and compute](../capabilities/compute/compute.md) | 17 of 22 | [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Workload management](../capabilities/compute/workload-management.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 4 of 13 | [Change feeds](../capabilities/serving/change-feeds.md), [Data APIs](../capabilities/serving/data-apis.md), [Data export](../capabilities/serving/data-export.md), [Decision management](../capabilities/serving/decision-management.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 5 of 20 | [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 4 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Feature store](../capabilities/machine-learning/feature-store.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [AutoML](../capabilities/machine-learning/automl.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 7 of 18 | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 of 23 (+5 in preview) | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md), [Model customisation](../capabilities/generative-ai/model-customisation.md) (preview only), [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) (preview only), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md) (preview only), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) (preview only), [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) (preview only) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 11 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 2 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 2 of 24 | [AI governance](../capabilities/governance/ai-governance.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Policy management](../capabilities/governance/data-policy-management.md), [Privacy management](../capabilities/governance/privacy-management.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [De-identification](../capabilities/governance/deidentification.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 7 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Encryption](../capabilities/security/encryption.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 3 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 0 of 7 | [Data products](../capabilities/data-products/data-products.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 6 of 16 (+2 in preview) | [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md) (preview only), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md) (preview only) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 15 of 27 | [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 0 of 10 | [Specialised data types](../capabilities/specialised-data/specialised-data.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Geospatial data](../capabilities/specialised-data/geospatial-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Product families

- **Cloudera AI** (also: Cloudera Machine Learning, CML): [Cloudera AI Workbench](../technologies/cloudera/cloudera-ai-workbench.md), [Cloudera AI Registry](../technologies/cloudera/cloudera-ai-registry.md), [Cloudera AI Inference service](../technologies/cloudera/cloudera-ai-inference-service.md), [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../technologies/cloudera/cloudera-ai-studios.md) (preview), [Cloudera AI Agent Studio](../technologies/cloudera/cloudera-agent-studio.md) (preview)
- **Cloudera Shared Data Experience** (also: SDX): [Cloudera Shared Data Experience (SDX)](../technologies/cloudera/cloudera-sdx.md), [Cloudera Data Catalog](../technologies/cloudera/cloudera-data-catalog.md)
- **Cloudera Open Data Lakehouse** (also: Cloudera Lakehouse): [Apache Iceberg in Cloudera](../technologies/cloudera/cloudera-lakehouse-iceberg.md), [Cloudera Iceberg REST Catalog](../technologies/cloudera/cloudera-iceberg-rest-catalog.md), [Cloudera Lakehouse Optimizer](../technologies/cloudera/cloudera-lakehouse-optimizer.md), [Cloudera Data Warehouse](../technologies/cloudera/cloudera-data-warehouse.md), [Apache Ozone in Cloudera](../technologies/cloudera/cloudera-ozone.md)
- **Cloudera Stream Processing** (also: CSP): [Cloudera Streams Messaging](../technologies/cloudera/cloudera-streams-messaging.md), [Cloudera Streaming Analytics](../technologies/cloudera/cloudera-streaming-analytics.md)
- **Cloudera Data Platform** (also: CDP): [Cloudera on cloud](../technologies/cloudera/cloudera-on-cloud.md), [Cloudera Data Services on premises](../technologies/cloudera/cloudera-data-services-on-premises.md), [Cloudera Base on premises](../technologies/cloudera/cloudera-base-on-premises.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| AI Registry | [Model registry](../capabilities/machine-learning/model-registry.md) |
| Apache Ranger (SDX) | [Access control](../capabilities/security/access-control.md) |
| Applications (AI Workbench) | [Data application hosting](../capabilities/development-lifecycle/data-applications.md) |
| Cloudera Data Engineering Airflow | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| Cloudera Data Explorer (Hue) | [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md) |
| Data Hub clusters | [Provisioned compute](../capabilities/compute/provisioned-compute.md) |
| Environments | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| Experiments | [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md) |
| Flow Designer (NiFi) | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| Hive Metastore / Iceberg REST Catalog | [Table catalogue](../capabilities/storage/table-catalogue.md) |
| Lakehouse Optimizer | [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md) |
| SQL Stream Builder | [Streaming SQL](../capabilities/processing/streaming-sql.md) |
| Virtual Warehouses | [Workload isolation](../capabilities/compute/workload-isolation.md) |

# Technologies

## Ingestion and integration

- [Cloudera Data Flow](../technologies/cloudera/cloudera-data-flow.md): Managed Apache NiFi service for building, deploying and autoscaling flows that collect, route and transform data from files, databases, APIs and streams.
- [Cloudera Streams Messaging](../technologies/cloudera/cloudera-streams-messaging.md): Cloudera's Apache Kafka distribution with Schema Registry, Streams Messaging Manager, Streams Replication Manager and Cruise Control.

## Storage and table management

- [Apache Iceberg in Cloudera](../technologies/cloudera/cloudera-lakehouse-iceberg.md): Native Apache Iceberg v2 table support across Spark, Hive, Impala, Trino, Flink and NiFi, including time travel, partition evolution and row-level changes.
- [Apache Ozone in Cloudera](../technologies/cloudera/cloudera-ozone.md): S3-compatible, scale-out object store for on-premises Cloudera clusters, intended to replace HDFS for very large file counts.
- [Cloudera Iceberg REST Catalog](../technologies/cloudera/cloudera-iceberg-rest-catalog.md): Implementation of the Iceberg REST catalogue API on the Hive Metastore that lets external engines read Cloudera-governed Iceberg tables using short-lived, scoped storage credentials.
- [Cloudera Lakehouse Optimizer](../technologies/cloudera/cloudera-lakehouse-optimizer.md): Policy-driven service that schedules and runs Iceberg table maintenance such as compaction, snapshot expiry and statistics collection.

## Processing and transformation

- [Cloudera Base on premises](../technologies/cloudera/cloudera-base-on-premises.md): The on-premises cluster platform with Cloudera Runtime (HDFS, Ozone, Hive, Impala, Spark, Kafka, HBase and others) managed by Cloudera Manager.
- [Cloudera Data Engineering](../technologies/cloudera/cloudera-data-engineering.md): Containerised, autoscaling Apache Spark service with job management and an embedded Apache Airflow for orchestrating pipelines.
- [Cloudera Streaming Analytics](../technologies/cloudera/cloudera-streaming-analytics.md): Apache Flink distribution with SQL Stream Builder, a console for writing continuous SQL jobs and materialised views over streams.

## Query and compute

- [Cloudera Data Warehouse](../technologies/cloudera/cloudera-data-warehouse.md): Containerised SQL service in which teams create isolated, autoscaling Virtual Warehouses running Impala, Hive LLAP or Trino over shared data lake tables.

## Serving and activation

- [Cloudera Operational Database](../technologies/cloudera/cloudera-operational-database.md): Autoscaling Apache HBase service with Apache Phoenix SQL for low-latency reads and writes on large, sparse operational datasets.

## Analytics and BI

- [Cloudera Data Visualization](../technologies/cloudera/cloudera-data-visualization.md): Built-in BI tool for dashboards and applications over Cloudera warehouses and AI projects, including an AI visual that answers natural-language questions.

## Machine learning development

- [Cloudera AI Registry](../technologies/cloudera/cloudera-ai-registry.md): Central registry that stores model versions and metadata from AI Workbench and makes them available for deployment to the AI Inference service.

## ML operations

- [Cloudera AI Inference service](../technologies/cloudera/cloudera-ai-inference-service.md): Kubernetes-based serving for predictive models and large language models, using NVIDIA NIM and Triton, with REST endpoints, monitoring and canary rollouts.

## Generative AI

- [Cloudera AI Agent Studio](../technologies/cloudera/cloudera-agent-studio.md) (preview): Low-code studio inside Cloudera AI for building, testing and deploying multi-agent workflows that call tools, including tools registered from MCP servers.
- [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../technologies/cloudera/cloudera-ai-studios.md) (preview): Low-code applications in Cloudera AI for building retrieval-augmented chat over documents, fine-tuning open models and generating synthetic datasets.

## Metadata and discovery

- [Cloudera Data Catalog](../technologies/cloudera/cloudera-data-catalog.md): Catalogue service over SDX metadata for searching assets, viewing Atlas lineage and running profilers that collect statistics and detect sensitive data.
- [Cloudera Data Lineage](../technologies/cloudera/cloudera-data-lineage.md): SaaS metadata and lineage service that harvests ETL tools, databases and BI reports to map dependencies across systems inside and outside Cloudera.

## Security and access

- [Cloudera Shared Data Experience (SDX)](../technologies/cloudera/cloudera-sdx.md): Common security and governance layer, built on Apache Ranger, Apache Atlas and Apache Knox, applied to every engine on the same data.

## Development and DataOps

- [Cloudera AI Workbench](../technologies/cloudera/cloudera-ai-workbench.md): Containerised data science environment with projects, sessions in Jupyter or other editors, experiments, jobs, model endpoints and hosted applications on CPUs or GPUs.

## Platform operations

- [Cloudera Anywhere Cloud](../technologies/cloudera/cloudera-anywhere-cloud.md) (unconfirmed): A central control plane that provisions and manages Cloudera data and AI services across public clouds, sovereign clouds and customer data centres, with uniform governance.
- [Cloudera Data Services on premises](../technologies/cloudera/cloudera-data-services-on-premises.md): Kubernetes-based deployment of the Data Engineering, Data Warehouse and Cloudera AI services on customer infrastructure, attached to a Cloudera Base cluster.
- [Cloudera Observability](../technologies/cloudera/cloudera-observability.md): Monitoring and analysis service for Cloudera workloads that shows job and query performance, recommends fixes and reports resource use and cost by workload.
- [Cloudera on cloud](../technologies/cloudera/cloudera-on-cloud.md): Cloudera's platform running in the customer's AWS, Azure or Google Cloud account, with a Cloudera-hosted Management Console that creates environments, data lakes and Data Hub clusters.
- [Cloudera Replication Manager](../technologies/cloudera/cloudera-replication-manager.md): Service that schedules replication of HDFS, Hive, Iceberg and HBase data and metadata between clusters and to cloud storage.

