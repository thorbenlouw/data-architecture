---
type: Platform
id: platform-oracle
title: Oracle
description: Oracle's database-centred data and AI services on Oracle Cloud Infrastructure and other clouds.
vendor: Oracle
resource: https://www.oracle.com/
folder: oracle
order: 9
terminology:
  change-data-capture: GoldenGate
  conversational-analytics: Select AI
  data-security-posture: Data Safe security assessment
  foundation-model-access: OCI Generative AI (Enterprise AI)
  in-database-ml: Oracle Machine Learning / HeatWave AutoML
  model-registry: Model catalog
  real-time-analytics: HeatWave
  semantic-layer: Semantic model (RPD)
  sql-query-engine: Autonomous AI Lakehouse
  table-catalogue: Autonomous AI Database Catalog / Data Catalog metastore
families:
- name: Oracle AI Database
  aliases: [Oracle Database]
  technologies:
  - oracle-ai-database-26ai
  - oracle-ai-vector-search
  - oracle-database-security
  - oracle-ai-private-agent-factory
- name: Oracle Autonomous AI Database
  aliases: [Oracle Autonomous Database, ADB]
  technologies:
  - oracle-autonomous-ai-database
  - oracle-autonomous-ai-lakehouse
  - oracle-autonomous-ai-database-catalog
  - oracle-select-ai
  - oracle-select-ai-agent
- name: HeatWave
  aliases: [MySQL HeatWave]
  technologies: [oracle-mysql-heatwave, oracle-heatwave-automl-genai]
- name: Oracle Analytics
  technologies: [oracle-analytics-cloud, oracle-analytics-cloud-ai, oracle-fusion-data-intelligence]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Oracle's data offering is built around Oracle AI Database 26ai, the long-term-support release that replaced Oracle Database 23ai in October 2025. It runs on premises, on Exadata, as Oracle Autonomous AI Database on OCI and inside AWS, Azure and Google Cloud through Oracle Database@AWS, @Azure and @Google Cloud. The database is converged: relational, JSON, graph, spatial, text and vector data and in-database machine learning all sit in one engine. Autonomous AI Database adds Select AI for natural-language questions and in-database agents, and Autonomous AI Lakehouse, its analytics workload type, adds Apache Iceberg tables in object storage and a catalogue that federates external catalogues.

Around the database, OCI provides GoldenGate for change data capture and replication, OCI Data Integration and OCI Data Flow for ETL and Spark, the newer Oracle AI Data Platform as a Spark and Delta Lake workbench, managed Apache Kafka, Oracle Analytics Cloud and Fusion Data Intelligence for BI, OCI Data Science for machine learning and OCI Generative AI for models and agents. MySQL HeatWave is a separate managed MySQL service with in-memory analytics, AutoML and generative AI.

# Notes

- Several names changed in October 2025: Autonomous Database became Autonomous AI Database, Autonomous Data Warehouse became Autonomous AI Lakehouse and Oracle Database 23ai moved to 26ai.
- OCI Generative AI has been marketed as OCI Enterprise AI since March 2026, while the documentation keeps the Generative AI name.
- Services overlap: OCI Data Catalog, the Autonomous AI Database Catalog and the AI Data Platform Master Catalog all catalogue data, and OCI Data Flow, OCI Data Integration and the AI Data Platform all run Spark or ETL.
- Some database security features, such as Database Vault and Advanced Security, are separately licensed options on premises but are included in Autonomous AI Database.
- Oracle Database@AWS, @Azure and @Google Cloud are bought through the hyperscaler but operated by Oracle, which suits estates that need Oracle databases next to cloud-native analytics.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 8 of 22 | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 9 of 23 | [Data versioning](../capabilities/storage/data-versioning.md), [Object storage](../capabilities/storage/object-storage.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Time travel](../capabilities/storage/time-travel.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 7 of 18 | [Data enrichment](../capabilities/processing/data-enrichment.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Document processing](../capabilities/processing/document-processing.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 2 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md) |
| [Query and compute](../capabilities/compute/compute.md) | 13 of 22 | [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Workload management](../capabilities/compute/workload-management.md), [Materialised views](../capabilities/compute/materialised-views.md), [Result caching](../capabilities/compute/result-caching.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Container services](../capabilities/compute/container-services.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 2 of 13 | [Change feeds](../capabilities/serving/change-feeds.md), [Data APIs](../capabilities/serving/data-apis.md), [Data export](../capabilities/serving/data-export.md), [Decision management](../capabilities/serving/decision-management.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 7 of 20 | [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 9 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 4 of 18 | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model governance](../capabilities/mlops/model-governance.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 11 of 23 | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 5 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Table-level lineage](../capabilities/metadata/table-lineage.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 0 of 12 | [Data quality and observability](../capabilities/data-quality/data-quality.md), [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 4 of 24 | [AI governance](../capabilities/governance/ai-governance.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Policy management](../capabilities/governance/data-policy-management.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 10 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Privileged access management](../capabilities/security/privileged-access.md), [Role-based access control](../capabilities/security/role-based-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 3 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 2 of 7 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 5 of 16 | [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Data application hosting](../capabilities/development-lifecycle/data-applications.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 9 of 27 | [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Platform observability](../capabilities/platform-operations/platform-observability.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 5 of 10 | [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Product families

- **Oracle AI Database** (also: Oracle Database): [Oracle AI Database 26ai](../technologies/oracle/oracle-ai-database-26ai.md), [Oracle AI Vector Search](../technologies/oracle/oracle-ai-vector-search.md), [Oracle Database security features](../technologies/oracle/oracle-database-security.md), [Oracle AI Database Private Agent Factory](../technologies/oracle/oracle-ai-private-agent-factory.md)
- **Oracle Autonomous AI Database** (also: Oracle Autonomous Database, ADB): [Oracle Autonomous AI Database](../technologies/oracle/oracle-autonomous-ai-database.md), [Oracle Autonomous AI Lakehouse](../technologies/oracle/oracle-autonomous-ai-lakehouse.md), [Oracle Autonomous AI Database Catalog](../technologies/oracle/oracle-autonomous-ai-database-catalog.md), [Oracle Select AI](../technologies/oracle/oracle-select-ai.md), [Oracle Select AI Agent and Autonomous AI Database MCP Server](../technologies/oracle/oracle-select-ai-agent.md)
- **HeatWave** (also: MySQL HeatWave): [MySQL HeatWave](../technologies/oracle/oracle-mysql-heatwave.md), [MySQL HeatWave AutoML and HeatWave GenAI](../technologies/oracle/oracle-heatwave-automl-genai.md)
- **Oracle Analytics**: [Oracle Analytics Cloud](../technologies/oracle/oracle-analytics-cloud.md), [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../technologies/oracle/oracle-analytics-cloud-ai.md), [Oracle Fusion Data Intelligence](../technologies/oracle/oracle-fusion-data-intelligence.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Autonomous AI Database Catalog / Data Catalog metastore | [Table catalogue](../capabilities/storage/table-catalogue.md) |
| Autonomous AI Lakehouse | [SQL query engine](../capabilities/compute/sql-query-engine.md) |
| Data Safe security assessment | [Data security posture management](../capabilities/security/data-security-posture.md) |
| GoldenGate | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) |
| HeatWave | [Real-time analytical database](../capabilities/compute/real-time-analytics.md) |
| Model catalog | [Model registry](../capabilities/machine-learning/model-registry.md) |
| OCI Generative AI (Enterprise AI) | [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |
| Oracle Machine Learning / HeatWave AutoML | [In-database machine learning](../capabilities/machine-learning/in-database-ml.md) |
| Select AI | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| Semantic model (RPD) | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) |

# Technologies

## Ingestion and integration

- [OCI Streaming with Apache Kafka](../technologies/oracle/oracle-oci-streaming-kafka.md): Managed Apache Kafka clusters in an OCI tenancy, with SASL/SCRAM or mTLS authentication and Kafka ACLs.
- [Oracle Fusion Data Intelligence](../technologies/oracle/oracle-fusion-data-intelligence.md): Packaged analytics for Oracle Fusion ERP, HCM, SCM and CX applications, with managed pipelines, a prebuilt data model in Autonomous AI Database and Oracle Analytics Cloud content.
- [Oracle GoldenGate](../technologies/oracle/oracle-goldengate.md): Log-based change data capture and replication between databases, and from databases to Kafka, cloud warehouses and Iceberg tables, available as software and as the managed OCI GoldenGate.

## Processing and transformation

- [OCI Data Flow](../technologies/oracle/oracle-oci-data-flow.md): Serverless Apache Spark service on OCI that runs batch and streaming Spark applications without cluster management.
- [OCI Data Integration](../technologies/oracle/oracle-oci-data-integration.md): Serverless, visual ETL and ELT service on OCI for designing data flows, pipelines and schedules, with tasks that can run on OCI Data Flow Spark.
- [Oracle AI Data Platform](../technologies/oracle/oracle-ai-data-platform.md): OCI lakehouse workbench that combines Spark compute, notebooks, workflow orchestration, a Master Catalog over Delta Lake and Iceberg data, Delta Sharing and agent building.

## Query and compute

- [MySQL HeatWave](../technologies/oracle/oracle-mysql-heatwave.md): Managed MySQL service with an in-memory, scale-out query accelerator for analytics on transactional data, and HeatWave Lakehouse for querying files in object storage.
- [Oracle AI Database 26ai](../technologies/oracle/oracle-ai-database-26ai.md): Oracle's converged database release that supports relational, JSON, graph, spatial, text and vector data in one engine for transactional and analytical work.
- [Oracle Autonomous AI Database](../technologies/oracle/oracle-autonomous-ai-database.md): Self-managing Oracle database service on OCI and other clouds that automates provisioning, patching, tuning, scaling and backups, offered as Lakehouse, Transaction Processing, JSON Database and APEX workload types.
- [Oracle Autonomous AI Lakehouse](../technologies/oracle/oracle-autonomous-ai-lakehouse.md): The analytics workload type of Autonomous AI Database, which runs Oracle SQL over its own tables and over Apache Iceberg tables in object storage registered in external catalogues.
- [Oracle Exadata](../technologies/oracle/oracle-exadata.md): Engineered database platform with scale-out storage servers that offload SQL filtering and caching, available on premises, as Exadata Database Service on OCI and as Exadata Cloud@Customer.

## Analytics and BI

- [Oracle Analytics Cloud](../technologies/oracle/oracle-analytics-cloud.md): Oracle's BI service for self-service visual analysis, governed dashboards, a semantic model, pixel-perfect reports and data preparation.
- [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../technologies/oracle/oracle-analytics-cloud-ai.md): Generative AI features in Oracle Analytics Cloud for asking questions of data in natural language, building dataset-specific agents and exposing governed analytics to external AI clients through MCP.
- [Oracle Select AI](../technologies/oracle/oracle-select-ai.md): Autonomous AI Database feature that turns natural-language prompts into SQL, answers questions with retrieval over vector stores, and generates synthetic data, using configured LLM providers.

## Machine learning development

- [MySQL HeatWave AutoML and HeatWave GenAI](../technologies/oracle/oracle-heatwave-automl-genai.md): In-database machine learning and generative AI routines in MySQL HeatWave, covering model training and scoring, embeddings, a vector store, RAG and natural-language to SQL.

## Generative AI

- [OCI Generative AI (OCI Enterprise AI)](../technologies/oracle/oracle-oci-generative-ai.md): Managed access to hosted and imported foundation models on OCI, with dedicated AI clusters, OpenAI-compatible APIs, guardrails, vector stores and a Responses API for building agents.
- [Oracle AI Database Private Agent Factory](../technologies/oracle/oracle-ai-private-agent-factory.md): No-code builder and runtime for AI agents that runs as a container in the customer's chosen environment, working against Oracle AI Database data.
- [Oracle AI Vector Search](../technologies/oracle/oracle-ai-vector-search.md): Native VECTOR data type, vector indexes and similarity functions in Oracle AI Database, combinable with relational, text, JSON, graph and spatial predicates in one SQL query.
- [Oracle Select AI Agent and Autonomous AI Database MCP Server](../technologies/oracle/oracle-select-ai-agent.md): In-database framework for defining agents, tasks and PL/SQL tools, with an Oracle-hosted MCP server that exposes those tools to external AI clients under database authorisation.

## Metadata and discovery

- [OCI Data Catalog](../technologies/oracle/oracle-oci-data-catalog.md): Managed metadata service that harvests technical metadata from OCI and on-premises sources, adds business glossary terms and tags, and provides a Hive-compatible metastore.
- [Oracle Autonomous AI Database Catalog](../technologies/oracle/oracle-autonomous-ai-database-catalog.md): A "catalogue of catalogues" in Autonomous AI Database that brings metadata from external catalogues, clouds and on-premises sources into one searchable view for discovery and access.

## Security and access

- [Oracle Data Safe](../technologies/oracle/oracle-data-safe.md): Security service for Oracle databases that assesses configuration and users, discovers and masks sensitive data, collects audit records and manages SQL Firewall.
- [Oracle Database security features](../technologies/oracle/oracle-database-security.md): Built-in controls in Oracle AI Database for row-level policies, query-time masking, separation of duties and encryption of data at rest with managed keys.

## Development and DataOps

- [OCI Data Science](../technologies/oracle/oracle-oci-data-science.md): Managed ML platform on OCI with JupyterLab notebook sessions, jobs, pipelines, a model catalogue, model deployment endpoints and AI Quick Actions for fine-tuning and evaluating foundation models.

## Platform operations

- [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../technologies/oracle/oracle-database-multicloud.md): Oracle-operated Exadata and Autonomous AI Database services running inside hyperscaler data centres and bought through the hyperscaler.

