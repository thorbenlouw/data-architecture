---
type: Platform
id: platform-palantir
title: Palantir
description: A platform that models enterprise data as an operational ontology for analytics, applications and AI agents.
vendor: Palantir
resource: https://www.palantir.com/
folder: palantir
order: 13
terminology:
  attribute-based-access: Markings
  data-applications: Workshop
  data-branching: Global Branching
  data-marketplace: Marketplace
  data-observability: Data Health
  data-quality-rules: Data expectations
  knowledge-graphs: Ontology
  low-code-transformation: Pipeline Builder
  model-registry: Modeling Objectives
  multi-tenancy: Organizations and Spaces
  query-federation: Virtual tables
  semantic-layer: Ontology
  unstructured-data: Media sets
families:
- name: Palantir Foundry
  technologies:
  - palantir-foundry
  - palantir-ontology
  - palantir-data-connection
  - palantir-pipeline-builder
  - palantir-code-repositories
  - palantir-code-workspaces
  - palantir-iceberg-tables
  - palantir-media-sets
  - palantir-data-health
  - palantir-data-lineage
  - palantir-global-branching
  - palantir-devops-marketplace
  - palantir-security-controls
  - palantir-sensitive-data-scanner-cipher
  - palantir-resource-management
  - palantir-contour-quiver
  - palantir-workshop
  - palantir-automate
  - palantir-modeling-objectives
- name: Palantir AIP
  aliases: [AIP, Artificial Intelligence Platform]
  technologies:
  - palantir-aip
  - palantir-aip-logic
  - palantir-aip-chatbot-studio
  - palantir-aip-analyst
  - palantir-media-sets
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Palantir's data platform is Foundry, a single integrated environment for connecting, transforming, governing, analysing and acting on data. It is organised around the Ontology, a model of business objects, links, actions and functions that sits over datasets, virtual tables and models; Workshop applications, automations, AIP agents and external systems all work through it. Data Connection, Pipeline Builder and Code Repositories handle ingestion and transformation, and lineage, branching, health checks and Markings-based security apply to everything built in the platform.

AIP (Artificial Intelligence Platform) adds governed access to commercial and open models, and builders such as AIP Logic, AIP Chatbot Studio and AIP Evals, on top of Foundry and the Ontology. Apollo deploys and upgrades Palantir software across Palantir-hosted, customer cloud, on-premises, edge and classified environments. Gotham, Palantir's defence and intelligence product, is outside the scope of this data platform.

# Notes

- Foundry is closed and opinionated: storage, versioned datasets, lineage and security propagation are properties of the platform rather than separate products, so plan open-format access and exports deliberately. Iceberg tables with an Iceberg REST catalogue, still in beta, open some of this up.
- The Ontology plays several roles at once: semantic layer, knowledge graph, operational data store and API layer for applications and agents.
- Foundry is licensed on compute and storage use, so Resource Management is the main tool for controlling cost.
- Recent renames include AIP Agent Studio to AIP Chatbot Studio and Foundry Branching to Global Branching.
- Palantir MCP lets external coding assistants build on Foundry, and Ontology MCP lets external agents read and write Ontology data and run permitted actions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 7 of 22 | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 4 of 23 (+2 in preview) | [Object storage](../capabilities/storage/object-storage.md), [Open file formats](../capabilities/storage/file-formats.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Time travel](../capabilities/storage/time-travel.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md), [Open table formats](../capabilities/storage/open-table-formats.md) (preview only), [Table catalogue](../capabilities/storage/table-catalogue.md) (preview only) |
| [Processing and transformation](../capabilities/processing/processing.md) | 12 of 18 | [Data enrichment](../capabilities/processing/data-enrichment.md), [DataFrame APIs](../capabilities/processing/dataframe-apis.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 2 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| [Query and compute](../capabilities/compute/compute.md) | 3 of 22 (+1 in preview) | [Compute provisioning options](../capabilities/compute/compute-options.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Query acceleration](../capabilities/compute/query-acceleration.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Workload management](../capabilities/compute/workload-management.md), [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Materialised views](../capabilities/compute/materialised-views.md), [Result caching](../capabilities/compute/result-caching.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Container services](../capabilities/compute/container-services.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Provisioned compute](../capabilities/compute/provisioned-compute.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Serverless compute](../capabilities/compute/serverless-compute.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md), [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md) (preview only) |
| [Serving and activation](../capabilities/serving/serving.md) | 5 of 13 | [Change feeds](../capabilities/serving/change-feeds.md), [Decision management](../capabilities/serving/decision-management.md), [Operational database integration](../capabilities/serving/operational-database.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 8 of 20 | [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 4 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Feature store](../capabilities/machine-learning/feature-store.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [AutoML](../capabilities/machine-learning/automl.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 4 of 18 | [Continuous training](../capabilities/mlops/continuous-training.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 10 of 23 | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Model customisation](../capabilities/generative-ai/model-customisation.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 7 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 4 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 6 of 24 | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Policy management](../capabilities/governance/data-policy-management.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md) |
| [Security and access](../capabilities/security/security.md) | 8 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 3 of 8 (+2 in preview) | [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md) (preview only), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) (preview only) |
| [Data products](../capabilities/data-products/data-products.md) | 2 of 7 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 10 of 16 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 12 of 27 | [Backup and disaster recovery](../capabilities/platform-operations/business-continuity.md), [Platform migration](../capabilities/platform-operations/platform-migration.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 6 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Geospatial data](../capabilities/specialised-data/geospatial-data.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md) |

# Product families

- **Palantir Foundry**: [Palantir Foundry](../technologies/palantir/palantir-foundry.md), [Palantir Ontology](../technologies/palantir/palantir-ontology.md), [Palantir Data Connection](../technologies/palantir/palantir-data-connection.md), [Palantir Pipeline Builder](../technologies/palantir/palantir-pipeline-builder.md), [Palantir Code Repositories](../technologies/palantir/palantir-code-repositories.md), [Palantir Code Workspaces](../technologies/palantir/palantir-code-workspaces.md), [Iceberg tables in Palantir Foundry](../technologies/palantir/palantir-iceberg-tables.md) (preview), [Palantir media sets and AIP Document Intelligence](../technologies/palantir/palantir-media-sets.md), [Palantir Data Health and data expectations](../technologies/palantir/palantir-data-health.md), [Palantir Data Lineage](../technologies/palantir/palantir-data-lineage.md), [Palantir Global Branching](../technologies/palantir/palantir-global-branching.md), [Palantir DevOps and Marketplace](../technologies/palantir/palantir-devops-marketplace.md), [Palantir Foundry security controls](../technologies/palantir/palantir-security-controls.md), [Palantir Sensitive Data Scanner and Cipher](../technologies/palantir/palantir-sensitive-data-scanner-cipher.md), [Palantir Resource Management](../technologies/palantir/palantir-resource-management.md), [Palantir Contour and Quiver](../technologies/palantir/palantir-contour-quiver.md), [Palantir Workshop](../technologies/palantir/palantir-workshop.md), [Palantir Automate](../technologies/palantir/palantir-automate.md), [Palantir Modeling Objectives and model assets](../technologies/palantir/palantir-modeling-objectives.md)
- **Palantir AIP** (also: AIP, Artificial Intelligence Platform): [Palantir AIP and AIP Model Catalog](../technologies/palantir/palantir-aip.md), [AIP Logic and AIP Evals](../technologies/palantir/palantir-aip-logic.md), [AIP Chatbot Studio](../technologies/palantir/palantir-aip-chatbot-studio.md), [AIP Analyst](../technologies/palantir/palantir-aip-analyst.md), [Palantir media sets and AIP Document Intelligence](../technologies/palantir/palantir-media-sets.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Data expectations | [Data quality rules](../capabilities/data-quality/data-quality-rules.md) |
| Data Health | [Data observability](../capabilities/data-quality/data-observability.md) |
| Global Branching | [Data branching and tagging](../capabilities/storage/data-branching.md) |
| Marketplace | [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| Markings | [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md) |
| Media sets | [Unstructured data management](../capabilities/specialised-data/unstructured-data.md) |
| Modeling Objectives | [Model registry](../capabilities/machine-learning/model-registry.md) |
| Ontology | [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |
| Ontology | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) |
| Organizations and Spaces | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| Pipeline Builder | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| Virtual tables | [Query federation](../capabilities/compute/query-federation.md) |
| Workshop | [Data application hosting](../capabilities/development-lifecycle/data-applications.md) |

# Technologies

## Ingestion and integration

- [Palantir Data Connection](../technologies/palantir/palantir-data-connection.md): Application for configuring sources and running batch, file, streaming and media syncs into Foundry, exports back to external systems, and virtual tables that query external platforms without copying.

## Storage and table management

- [Iceberg tables in Palantir Foundry](../technologies/palantir/palantir-iceberg-tables.md) (preview): Apache Iceberg as an alternative Foundry table type, with an Iceberg REST catalogue that lets external clients such as Snowflake and Jupyter read Foundry-governed tables.
- [Palantir Global Branching](../technologies/palantir/palantir-global-branching.md): Branching that spans pipelines, the Ontology and applications so a change can be built and tested end to end in isolation and merged after per-resource approval.

## Processing and transformation

- [Palantir Code Repositories](../technologies/palantir/palantir-code-repositories.md): Web-based IDE backed by Git for writing Python, Java and SQL transforms and Ontology functions, with branches, pull requests, checks and builds.
- [Palantir Pipeline Builder](../technologies/palantir/palantir-pipeline-builder.md): Visual pipeline tool for building batch, incremental and streaming transformations with typed functions, LLM nodes, data expectations, unit tests, schedules and branch-based review.

## Orchestration

- [Palantir Automate](../technologies/palantir/palantir-automate.md): Rules that watch Ontology data or schedules and send notifications, run actions or call AIP Logic when conditions are met.

## Analytics and BI

- [AIP Analyst](../technologies/palantir/palantir-aip-analyst.md): AI assistant that answers analytical questions over Ontology data in natural language and can be embedded in Workshop and other applications.
- [Palantir Contour and Quiver](../technologies/palantir/palantir-contour-quiver.md): Point-and-click analysis tools, Contour for large tabular datasets and Quiver for Ontology objects and time series, producing shareable analyses and dashboards.

## Machine learning development

- [Palantir Modeling Objectives and model assets](../technologies/palantir/palantir-modeling-objectives.md): Foundry's model management, in which model assets built in Foundry or imported are evaluated, reviewed, released and deployed for batch or live use, then bound to the Ontology.

## Generative AI

- [AIP Chatbot Studio](../technologies/palantir/palantir-aip-chatbot-studio.md): Builder for chat agents that use retrieval context, Ontology tools and actions and give cited answers, distributable through Workshop, Marketplace or APIs.
- [AIP Logic and AIP Evals](../technologies/palantir/palantir-aip-logic.md): No-code builder for LLM-powered functions that read Ontology data, call tools and propose or apply edits, with AIP Evals test suites and metrics for checking their outputs.
- [Palantir AIP and AIP Model Catalog](../technologies/palantir/palantir-aip.md): Palantir's generative AI layer that provides governed access to commercial and open LLMs, capacity management and the AIP applications on top of Foundry and the Ontology.
- [Palantir MCP and Ontology MCP](../technologies/palantir/palantir-mcp.md): MCP servers that let external AI coding tools build on Foundry (Palantir MCP) and let external agents read and write Ontology data and run actions within set limits (Ontology MCP).

## Metadata and discovery

- [Palantir Data Lineage](../technologies/palantir/palantir-data-lineage.md): Interactive graph of how datasets, transforms, objects and applications depend on each other across Foundry, with schedules, build status and permissions shown in context.

## Data quality and observability

- [Palantir Data Health and data expectations](../technologies/palantir/palantir-data-health.md): Health checks on datasets and builds for freshness, schema, row counts and content, plus expectations declared in pipelines that fail or warn when data breaks rules.

## Governance and compliance

- [Palantir Sensitive Data Scanner and Cipher](../technologies/palantir/palantir-sensitive-data-scanner-cipher.md): Tools that scan Foundry datasets for sensitive data such as personal identifiers, and that encrypt, hash or obscure columns with managed keys and algorithms.

## Security and access

- [Palantir Foundry security controls](../technologies/palantir/palantir-security-controls.md): Mandatory controls (Organizations and Markings that follow data through lineage) combined with discretionary project roles, row and column policies, justification prompts and audit logs.

## Development and DataOps

- [Palantir Code Workspaces](../technologies/palantir/palantir-code-workspaces.md): Hosted JupyterLab, RStudio Workbench and VS Code environments in Foundry for exploratory analysis, data science and code-based work on Foundry data.
- [Palantir DevOps and Marketplace](../technologies/palantir/palantir-devops-marketplace.md): Packaging of pipelines, Ontology, models and applications into versioned products with release channels, and a storefront for installing and upgrading them across spaces and organisations.
- [Palantir Workshop](../technologies/palantir/palantir-workshop.md): Low-code builder for operational applications over Ontology objects, with tables, charts, maps, forms that run actions, and embedded AIP widgets.

## Platform operations

- [Palantir Apollo](../technologies/palantir/palantir-apollo.md): Continuous delivery system that deploys and upgrades Palantir and customer software across many environments, including on-premises, edge and disconnected networks, with release channels and change approvals.
- [Palantir Foundry](../technologies/palantir/palantir-foundry.md): Integrated data platform that combines connectors, pipelines, storage, the Ontology, analytics, application building, model integration and governance in one environment with shared lineage and security.
- [Palantir Resource Management](../technologies/palantir/palantir-resource-management.md): Administration views of compute and storage usage by project and resource, with limits for controlling consumption.

## Specialised data types

- [Palantir media sets and AIP Document Intelligence](../technologies/palantir/palantir-media-sets.md): Foundry storage and pipelines for unstructured files such as PDFs, images, audio and video, with AIP Document Intelligence strategies for extracting text, tables and fields.
- [Palantir Ontology](../technologies/palantir/palantir-ontology.md): Semantic and operational layer that maps datasets, virtual tables and models to business object types, properties and links, with action types and functions that write decisions back.

