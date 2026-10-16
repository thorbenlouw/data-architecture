---
type: Platform
id: platform-clickhouse
title: ClickHouse
description: An open-source columnar database for real-time analytics, also sold as a managed cloud service.
vendor: ClickHouse
resource: https://clickhouse.com/
folder: clickhouse
order: 6
terminology:
  agent-tool-access: ClickHouse MCP server / Remote MCP
  change-data-capture: ClickPipes CDC (PeerDB)
  column-masking: Masking policies
  conversational-analytics: ClickHouse Assistant (AI Chat) and ClickHouse Agents
  data-apis: Query API Endpoints
  data-retention: TTL
  data-skipping-indexes: Primary (sparse) index and data skipping indexes
  decoupled-storage-compute: SharedMergeTree
  deployment-options: BYOC, ClickHouse Private
  file-ingestion: S3Queue and ClickPipes object storage pipes
  full-text-search: Text index
  genai-observability: Langfuse
  materialised-views: Materialized views (incremental) and refreshable materialized views
  operational-database: ClickHouse Managed Postgres
  partitioning-clustering: PARTITION BY and the sorting key (ORDER BY / primary key)
  query-federation: Table functions and integration table engines
  query-performance-analysis: Query Insights, system.query_log
  read-optimised-views: Materialized views and projections
  real-time-analytics: ClickHouse (real-time analytical database)
  result-caching: Query cache
  row-level-security: Row policies
  row-level-updates: Lightweight updates and deletes, mutations, ReplacingMergeTree
  semi-structured-data: JSON, Dynamic and Variant types
  single-node-processing: clickhouse-local, chDB
  storage-tiering: TTL TO DISK / TO VOLUME (tiered storage)
  streaming-ingestion: ClickPipes and the Kafka table engine
  table-catalogue: DataLakeCatalog database engine (data catalogs)
  table-maintenance: Background merges, OPTIMIZE
  user-defined-functions: UDFs (SQL and executable)
  vector-search: Vector similarity index
  workload-isolation: Warehouses (compute-compute separation)
  workload-management: Workload scheduling, settings profiles and quotas
families:
- name: ClickHouse Cloud
  technologies:
  - clickhouse-cloud
  - clickhouse-sharedmergetree
  - clickhouse-warehouses
  - clickhouse-clickpipes
  - clickhouse-clickpipes-cdc
  - clickhouse-sql-console
  - clickhouse-query-api-endpoints
  - clickhouse-cloud-monitoring
  - clickhouse-cost-controls
  - clickhouse-backups
  - clickhouse-cmek
  - clickhouse-private-link
  - clickhouse-byoc
  - clickhouse-managed-postgres
  - clickhouse-agents
- name: ClickPipes
  technologies: [clickhouse-clickpipes, clickhouse-clickpipes-cdc]
- name: ClickHouse table engines
  aliases: [table engines]
  technologies:
  - clickhouse-mergetree
  - clickhouse-sharedmergetree
  - clickhouse-kafka-engine
  - clickhouse-s3queue
  - clickhouse-integration-engines
  - clickhouse-data-lake
  - clickhouse-datalakecatalog
  - clickhouse-timeseries
- name: ClickHouse materialized views
  aliases: [ClickHouse materialised views]
  technologies: [clickhouse-materialized-views, clickhouse-refreshable-materialized-views]
- name: ClickHouse Agentic Data Stack
  aliases: [Agentic Data Stack]
  technologies: [clickhouse-agents, clickhouse-mcp-server, clickhouse-langfuse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ClickHouse is an open-source (Apache 2.0) column-oriented database for real-time analytics. Its core is the MergeTree family of table engines, which write sorted, compressed parts and merge them in the background, together with incremental and refreshable materialised views and a large set of table engines and functions that read from Kafka, object storage, other databases and lakehouse tables. The same binary also provides clickhouse-local, and chDB embeds the engine inside application processes.

ClickHouse Inc. sells the database as ClickHouse Cloud on AWS, Google Cloud and Azure in Basic, Scale and Enterprise tiers, where SharedMergeTree keeps data in object storage and Warehouses give separate compute to different workloads over the same data. BYOC runs the Cloud data plane in the customer's own cloud account, and ClickHouse Private serves self-managed estates. ClickPipes provides managed ingestion and change data capture. Around the database the company now offers ClickStack for observability, ClickHouse Managed Postgres, and an agentic data stack of MCP servers, ClickHouse Agents and Langfuse.

# Notes

- Several products came from acquisitions: ClickPipes CDC from PeerDB (2024), ClickStack from HyperDX (2025), ClickHouse Agents from LibreChat (November 2025) and Langfuse (January 2026).
- Some features exist only in ClickHouse Cloud (SharedMergeTree, ClickPipes, Query API Endpoints) or in Cloud, BYOC and ClickHouse Private (masking policies). Tiered storage with TTL TO DISK, JDBC and ODBC bridges and WebAssembly UDFs are for self-managed servers only.
- Deduplication and upserts happen at merge time in ReplacingMergeTree and related engines, so exact results need FINAL or GROUP BY. CDC targets follow the same pattern.
- Materialised views are insert triggers rather than a windowed stream processor, and there is no production event-time windowing engine.
- ClickHouse offers little for catalogues, lineage, data quality or MDM. It relies on external catalogues, reached through the DataLakeCatalog engine, and on dbt.
- Release stages moved quickly in 2026 (MySQL CDC GA, MongoDB CDC beta, Iceberg INSERT beta, text indexes GA), so behaviour depends on the server version in use.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 9 of 22 | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 14 of 23 (+2 in preview) | [Storage credential vending](../capabilities/storage/credential-vending.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md), [Table catalogue](../capabilities/storage/table-catalogue.md) (preview only), [Catalogue federation](../capabilities/storage/catalogue-federation.md) (preview only) |
| [Processing and transformation](../capabilities/processing/processing.md) | 8 of 18 (+2 in preview) | [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Document processing](../capabilities/processing/document-processing.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Low-code transformation](../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../capabilities/processing/data-preparation.md), [Stream processing](../capabilities/processing/stream-processing.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [AI functions in SQL](../capabilities/processing/ai-functions.md) (preview only), [Transformation as code](../capabilities/processing/transformation-as-code.md) (preview only) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 3 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md) |
| [Query and compute](../capabilities/compute/compute.md) | 16 of 22 | [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Container services](../capabilities/compute/container-services.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Provisioned compute](../capabilities/compute/provisioned-compute.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 5 of 13 (+1 in preview) | [Change feeds](../capabilities/serving/change-feeds.md), [Decision management](../capabilities/serving/decision-management.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Audience building and activation](../capabilities/serving/audience-activation.md), [Operational database integration](../capabilities/serving/operational-database.md) (preview only) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 5 of 20 | [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Feature store](../capabilities/machine-learning/feature-store.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Model training](../capabilities/machine-learning/model-training.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [AutoML](../capabilities/machine-learning/automl.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 0 of 18 | [ML operations](../capabilities/mlops/mlops.md), [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model deployment](../capabilities/mlops/model-deployment.md), [Model governance](../capabilities/mlops/model-governance.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 7 of 23 (+3 in preview) | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../capabilities/generative-ai/model-customisation.md), [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md) (preview only), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) (preview only), [Agent memory](../capabilities/generative-ai/agent-memory.md) (preview only) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 0 of 20 | [Metadata and discovery](../capabilities/metadata/metadata.md), [Active metadata](../capabilities/metadata/active-metadata.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Table-level lineage](../capabilities/metadata/table-lineage.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 2 of 12 | [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 3 of 24 | [AI governance](../capabilities/governance/ai-governance.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data classification](../capabilities/governance/data-classification.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Policy management](../capabilities/governance/data-policy-management.md), [Privacy management](../capabilities/governance/privacy-management.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [De-identification](../capabilities/governance/deidentification.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 10 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 0 of 8 | [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md), [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 0 of 7 | [Data products](../capabilities/data-products/data-products.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 4 of 16 (+1 in preview) | [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Data application hosting](../capabilities/development-lifecycle/data-applications.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [Notebooks](../capabilities/development-lifecycle/notebooks.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) (preview only) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 13 of 27 | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Platform migration](../capabilities/platform-operations/platform-migration.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 5 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Product families

- **ClickHouse Cloud**: [ClickHouse Cloud](../technologies/clickhouse/clickhouse-cloud.md), [SharedMergeTree](../technologies/clickhouse/clickhouse-sharedmergetree.md), [ClickHouse Cloud Warehouses (compute-compute separation)](../technologies/clickhouse/clickhouse-warehouses.md), [ClickPipes](../technologies/clickhouse/clickhouse-clickpipes.md), [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../technologies/clickhouse/clickhouse-clickpipes-cdc.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../technologies/clickhouse/clickhouse-sql-console.md), [ClickHouse Cloud Query API Endpoints](../technologies/clickhouse/clickhouse-query-api-endpoints.md), [ClickHouse Query Insights and system tables](../technologies/clickhouse/clickhouse-cloud-monitoring.md), [ClickHouse Cloud usage breakdown and spend alerts](../technologies/clickhouse/clickhouse-cost-controls.md), [ClickHouse Cloud backups and BACKUP/RESTORE](../technologies/clickhouse/clickhouse-backups.md), [ClickHouse Cloud TDE and customer-managed encryption keys (CMEK)](../technologies/clickhouse/clickhouse-cmek.md), [ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)](../technologies/clickhouse/clickhouse-private-link.md), [ClickHouse BYOC (Bring Your Own Cloud)](../technologies/clickhouse/clickhouse-byoc.md), [ClickHouse Managed Postgres](../technologies/clickhouse/clickhouse-managed-postgres.md) (preview), [ClickHouse Agents](../technologies/clickhouse/clickhouse-agents.md) (preview)
- **ClickPipes**: [ClickPipes](../technologies/clickhouse/clickhouse-clickpipes.md), [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../technologies/clickhouse/clickhouse-clickpipes-cdc.md)
- **ClickHouse table engines** (also: table engines): [MergeTree table engine family](../technologies/clickhouse/clickhouse-mergetree.md), [SharedMergeTree](../technologies/clickhouse/clickhouse-sharedmergetree.md), [ClickHouse Kafka table engine](../technologies/clickhouse/clickhouse-kafka-engine.md), [S3Queue and AzureQueue table engines](../technologies/clickhouse/clickhouse-s3queue.md), [ClickHouse integration table engines and table functions](../technologies/clickhouse/clickhouse-integration-engines.md), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../technologies/clickhouse/clickhouse-data-lake.md), [ClickHouse DataLakeCatalog database engine](../technologies/clickhouse/clickhouse-datalakecatalog.md) (preview), [ClickHouse TimeSeries table engine](../technologies/clickhouse/clickhouse-timeseries.md) (preview)
- **ClickHouse materialized views** (also: ClickHouse materialised views): [ClickHouse incremental materialized views](../technologies/clickhouse/clickhouse-materialized-views.md), [ClickHouse refreshable materialized views](../technologies/clickhouse/clickhouse-refreshable-materialized-views.md)
- **ClickHouse Agentic Data Stack** (also: Agentic Data Stack): [ClickHouse Agents](../technologies/clickhouse/clickhouse-agents.md) (preview), [ClickHouse MCP server (open-source and Remote MCP in Cloud)](../technologies/clickhouse/clickhouse-mcp-server.md), [Langfuse](../technologies/clickhouse/clickhouse-langfuse.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Background merges, OPTIMIZE | [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md) |
| BYOC, ClickHouse Private | [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md) |
| ClickHouse (real-time analytical database) | [Real-time analytical database](../capabilities/compute/real-time-analytics.md) |
| ClickHouse Assistant (AI Chat) and ClickHouse Agents | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| ClickHouse Managed Postgres | [Operational database integration](../capabilities/serving/operational-database.md) |
| ClickHouse MCP server / Remote MCP | [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) |
| clickhouse-local, chDB | [Single-node processing](../capabilities/processing/single-node-processing.md) |
| ClickPipes and the Kafka table engine | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |
| ClickPipes CDC (PeerDB) | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) |
| DataLakeCatalog database engine (data catalogs) | [Table catalogue](../capabilities/storage/table-catalogue.md) |
| JSON, Dynamic and Variant types | [Semi-structured data](../capabilities/storage/semi-structured-data.md) |
| Langfuse | [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| Lightweight updates and deletes, mutations, ReplacingMergeTree | [Row-level updates and deletes](../capabilities/storage/row-level-updates.md) |
| Masking policies | [Column security and dynamic masking](../capabilities/security/column-masking.md) |
| Materialized views (incremental) and refreshable materialized views | [Materialised views](../capabilities/compute/materialised-views.md) |
| Materialized views and projections | [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| PARTITION BY and the sorting key (ORDER BY / primary key) | [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md) |
| Primary (sparse) index and data skipping indexes | [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md) |
| Query API Endpoints | [Data APIs](../capabilities/serving/data-apis.md) |
| Query cache | [Result caching](../capabilities/compute/result-caching.md) |
| Query Insights, system.query_log | [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) |
| Row policies | [Row-level security](../capabilities/security/row-level-security.md) |
| S3Queue and ClickPipes object storage pipes | [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| SharedMergeTree | [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md) |
| Table functions and integration table engines | [Query federation](../capabilities/compute/query-federation.md) |
| Text index | [Full-text search](../capabilities/specialised-data/full-text-search.md) |
| TTL | [Retention and disposal](../capabilities/governance/data-retention.md) |
| TTL TO DISK / TO VOLUME (tiered storage) | [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) |
| UDFs (SQL and executable) | [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md) |
| Vector similarity index | [Vector search](../capabilities/generative-ai/vector-search.md) |
| Warehouses (compute-compute separation) | [Workload isolation](../capabilities/compute/workload-isolation.md) |
| Workload scheduling, settings profiles and quotas | [Workload management](../capabilities/compute/workload-management.md) |

# Technologies

## Ingestion and integration

- [ClickHouse Kafka table engine](../technologies/clickhouse/clickhouse-kafka-engine.md): Table engine that consumes Kafka topics as a consumer group and, with a materialised view, writes messages continuously into MergeTree tables; RabbitMQ and NATS engines work the same way.
- [ClickPipes](../technologies/clickhouse/clickhouse-clickpipes.md): Managed ingestion service in ClickHouse Cloud that runs continuous or one-off pipes from streaming platforms and object storage into ClickHouse tables, with scaling separate from the database.
- [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../technologies/clickhouse/clickhouse-clickpipes-cdc.md): ClickPipes connectors that take an initial snapshot of source tables and then replicate inserts, updates and deletes from Postgres, MySQL or MongoDB logs into ClickHouse, plus a BigQuery connector for bulk and incremental loads.
- [S3Queue and AzureQueue table engines](../technologies/clickhouse/clickhouse-s3queue.md): Table engines that watch an S3 or Azure Blob path and load new files in the background through a materialised view, tracking which files have been processed in Keeper.

## Storage and table management

- [ClickHouse DataLakeCatalog database engine](../technologies/clickhouse/clickhouse-datalakecatalog.md) (preview): Database engine that connects to an external lakehouse catalogue and exposes its tables as ClickHouse tables for querying and joining.
- [ClickHouse JSON, Dynamic and Variant data types](../technologies/clickhouse/clickhouse-json-types.md): Column types that store semi-structured JSON as typed sub-columns per path, and values whose type varies from row to row, without flattening them first.
- [ClickHouse lightweight updates and deletes](../technologies/clickhouse/clickhouse-lightweight-updates-deletes.md): Changes or removes individual rows in MergeTree tables by writing small patch parts or a deleted-row mask that queries apply at once, instead of rewriting whole parts.
- [MergeTree table engine family](../technologies/clickhouse/clickhouse-mergetree.md): Core storage engines that write sorted, compressed column parts, merge them in the background, and index them with a sparse primary index, with variants that deduplicate, sum, aggregate or collapse rows during merges.

## Processing and transformation

- [chDB](../technologies/clickhouse/clickhouse-chdb.md): In-process OLAP engine built on ClickHouse that runs inside Python, Go, Rust, Node.js or C/C++ programs, with a pandas-compatible DataStore API.
- [ClickHouse AI functions](../technologies/clickhouse/clickhouse-ai-functions.md) (preview): SQL functions such as aiGenerate, aiClassify, aiExtract, aiTranslate, aiRedact and aiEmbed that call an LLM or embedding endpoint for each row.
- [ClickHouse user-defined functions](../technologies/clickhouse/clickhouse-udfs.md): Extends ClickHouse with SQL lambda functions, executable functions that call external scripts such as Python over standard input and output, and experimental WebAssembly functions.
- [clickhouse-local](../technologies/clickhouse/clickhouse-local.md): Mode of the ClickHouse binary that runs SQL over local or remote files and piped data without starting a server.
- [dbt-clickhouse adapter](../technologies/clickhouse/clickhouse-dbt.md) (preview): ClickHouse-supported dbt adapter that builds views, tables, incremental and microbatch models, materialised views and dictionaries in ClickHouse.

## Query and compute

- [ClickHouse Cloud](../technologies/clickhouse/clickhouse-cloud.md): Fully managed ClickHouse on AWS, GCP and Azure that stores data in object storage and scales, idles and upgrades services automatically.
- [ClickHouse Cloud Warehouses (compute-compute separation)](../technologies/clickhouse/clickhouse-warehouses.md): Groups several Cloud services with their own replicas and endpoints over the same data, so ingestion, reporting and ad hoc workloads can run on separately sized compute.
- [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../technologies/clickhouse/clickhouse-data-lake.md): Table functions and engines that query Apache Iceberg, Delta Lake, Apache Hudi and Apache Paimon tables in object storage, with Iceberg time travel and the ability to create and insert into Iceberg tables.
- [ClickHouse data skipping indexes](../technologies/clickhouse/clickhouse-skipping-indexes.md): Per-block minmax, set and Bloom filter indexes that let queries skip granules which cannot match a filter, after the primary index has pruned data.
- [ClickHouse dictionaries](../technologies/clickhouse/clickhouse-dictionaries.md): In-memory key-value lookups loaded from ClickHouse tables, external databases, HTTP or files, refreshed on a set lifetime and queried with dictGet functions or as tables.
- [ClickHouse incremental materialized views](../technologies/clickhouse/clickhouse-materialized-views.md): Insert triggers that run a query over each newly inserted block and write the results to a target table, usually an AggregatingMergeTree or SummingMergeTree that merges partial aggregates.
- [ClickHouse integration table engines and table functions](../technologies/clickhouse/clickhouse-integration-engines.md): Engines and functions such as postgresql, mysql, mongodb, s3, url, jdbc, odbc and arrowflight that read from and write to external databases and storage directly in SQL.
- [ClickHouse projections](../technologies/clickhouse/clickhouse-projections.md): Hidden, automatically maintained copies of a table with a different sort order or pre-aggregation that the optimiser picks when they reduce the data read.
- [ClickHouse query cache](../technologies/clickhouse/clickhouse-query-cache.md): Stores the results of SELECT queries in memory, or optionally on disk, and serves repeats until a time to live expires.
- [ClickHouse refreshable materialized views](../technologies/clickhouse/clickhouse-refreshable-materialized-views.md): Views that rerun a full query on a schedule and replace or append to a target table, with optional dependencies between views.
- [ClickHouse server](../technologies/clickhouse/clickhouse-server.md): Open-source column-oriented SQL database that runs analytical queries over very large tables with vectorised, parallel execution on single servers or sharded and replicated clusters.
- [ClickHouse workload scheduling](../technologies/clickhouse/clickhouse-workload-scheduling.md): Divides CPU, disk I/O, memory and query slots between a hierarchy of SQL-defined workloads using priorities, weights and limits.
- [SharedMergeTree](../technologies/clickhouse/clickhouse-sharedmergetree.md): Cloud-native counterpart of the MergeTree family that keeps table data and metadata in shared object storage and coordinates replicas through Keeper instead of copying data between them.

## Serving and activation

- [ClickHouse Cloud Query API Endpoints](../technologies/clickhouse/clickhouse-query-api-endpoints.md): Turns a saved, parameterised SQL query in the Cloud console into an authenticated HTTP endpoint that returns results in any ClickHouse format.
- [ClickHouse interfaces and client drivers](../technologies/clickhouse/clickhouse-clients.md): HTTP, native TCP, gRPC and Arrow Flight interfaces, MySQL and PostgreSQL wire-protocol compatibility, and official clients including JDBC, ODBC, ADBC, Python, Go, Node.js, Rust, C++ and .NET.
- [ClickHouse Managed Postgres](../technologies/clickhouse/clickhouse-managed-postgres.md) (preview): Managed PostgreSQL on local NVMe storage with high availability, read replicas and point-in-time recovery, wired to ClickHouse through built-in CDC and the pg_clickhouse extension.

## Analytics and BI

- [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../technologies/clickhouse/clickhouse-sql-console.md): Browser workspace for writing and sharing queries, charting results, building parameterised dashboards from saved queries and asking an AI assistant to write SQL or explore data.
- [ClickHouse data source plugin for Grafana](../technologies/clickhouse/clickhouse-grafana-plugin.md): Signed Grafana data source with a query builder for building dashboards and exploring logs and traces stored in ClickHouse.

## Generative AI

- [ClickHouse Agents](../technologies/clickhouse/clickhouse-agents.md) (preview): Managed agent service in ClickHouse Cloud with a chat interface, no-code agent builder, skills, memory, sandboxed code execution and MCP tool access, using Claude models by default.
- [ClickHouse MCP server (open-source and Remote MCP in Cloud)](../technologies/clickhouse/clickhouse-mcp-server.md): Model Context Protocol servers that let AI assistants list ClickHouse databases and tables and run read-only queries, including a managed remote endpoint for ClickHouse Cloud.
- [ClickHouse vector similarity indexes](../technologies/clickhouse/clickhouse-vector-search.md): HNSW indexes on embedding columns for approximate nearest-neighbour search with L2, cosine or dot-product distance, alongside exact brute-force search and the QBit type.
- [Langfuse](../technologies/clickhouse/clickhouse-langfuse.md): LLM engineering platform that traces model and agent calls, runs evaluations and experiments on datasets, and versions prompts, available self-hosted or as Langfuse Cloud.

## Governance and compliance

- [ClickHouse TTL (time to live)](../technologies/clickhouse/clickhouse-ttl.md): Table and column rules that delete, roll up, recompress or move data once it reaches a given age, applied during background merges.

## Security and access

- [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../technologies/clickhouse/clickhouse-access-control.md): SQL-managed access entities that grant privileges to roles, filter rows per user, mask column values per user, and cap settings and resource use per user or role.
- [ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)](../technologies/clickhouse/clickhouse-private-link.md): Connects ClickHouse Cloud services and ClickPipes to customer virtual networks over the cloud providers' private endpoint services, and restricts public access with IP filters.
- [ClickHouse Cloud TDE and customer-managed encryption keys (CMEK)](../technologies/clickhouse/clickhouse-cmek.md): Adds database-level encryption to Cloud services and lets the customer supply and rotate the wrapping key in AWS KMS, GCP KMS or Azure Key Vault.

## Platform operations

- [ClickHouse BYOC (Bring Your Own Cloud)](../technologies/clickhouse/clickhouse-byoc.md): Runs the ClickHouse Cloud data plane, including clusters, data and backups, inside the customer's own cloud account while ClickHouse operates the control plane.
- [ClickHouse Cloud backups and BACKUP/RESTORE](../technologies/clickhouse/clickhouse-backups.md): Scheduled Cloud backups restored to a new service, and SQL BACKUP and RESTORE statements that write full or incremental backups to disk, S3 or Azure in self-managed clusters.
- [ClickHouse Cloud usage breakdown and spend alerts](../technologies/clickhouse/clickhouse-cost-controls.md): Console usage breakdown by service and cost category, a usage cost API, and organisation spend alerts at set thresholds of committed or budgeted spend.
- [ClickHouse Keeper](../technologies/clickhouse/clickhouse-keeper.md): Raft-based coordination service, compatible with the ZooKeeper client protocol, that coordinates replication, distributed DDL and queue engines.
- [ClickHouse Query Insights and system tables](../technologies/clickhouse/clickhouse-cloud-monitoring.md): Console views of query volume, latency and errors built on system.query_log, alongside system tables, Cloud monitoring dashboards and Prometheus endpoints that expose server, query and ClickPipes metrics.
- [ClickHouse Terraform provider](../technologies/clickhouse/clickhouse-terraform.md): Official Terraform provider for ClickHouse Cloud services, scaling, private endpoints, organisation roles and API keys, ClickPipes, ClickStack resources and Managed Postgres.

## Specialised data types

- [ClickHouse geo data types and functions](../technologies/clickhouse/clickhouse-geo.md): Point, polygon and line types plus functions for great-circle distances, point-in-polygon tests, geohash, H3 and S2 indexing and Mapbox vector tile encoding.
- [ClickHouse text indexes (full-text search)](../technologies/clickhouse/clickhouse-text-indexes.md): Inverted indexes on string, array and map columns with configurable tokenisers that answer token, phrase and pattern searches without scanning.
- [ClickHouse TimeSeries table engine](../technologies/clickhouse/clickhouse-timeseries.md) (preview): Experimental engine that stores Prometheus-style metrics as samples, tags and metric tables and accepts Prometheus remote-write and remote-read traffic.
- [ClickStack](../technologies/clickhouse/clickhouse-clickstack.md): Observability stack that combines the HyperDX UI, a preconfigured OpenTelemetry collector and ClickHouse to store and search logs, traces, metrics and session replays, with dashboards and alerts.

