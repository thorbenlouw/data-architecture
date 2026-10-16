---
type: Platform
id: platform-snowflake
title: Snowflake
description: A multi-cloud SaaS data platform built around a managed SQL engine, with engineering, AI and sharing services on top.
vendor: Snowflake
resource: https://www.snowflake.com/
folder: snowflake
order: 4
terminology:
  agent-tool-access: Snowflake-managed MCP server
  ai-assisted-development: CoCo (formerly Cortex Code; replacing Snowflake Copilot)
  ai-functions: Cortex AI Functions (formerly Cortex AISQL)
  attribute-based-access: tag-based masking policies
  backup-restore: backups (formerly snapshots); Fail-safe
  change-data-capture: Openflow CDC connectors; data mirroring (Snowflake Postgres)
  change-feeds: streams
  column-masking: masking policies
  container-services: Snowpark Container Services (SPCS), compute pools
  conversational-analytics: Cortex Analyst and Snowflake CoWork (formerly Snowflake Intelligence)
  cross-region-failover: replication and failover groups
  cross-region-sharing: Cross-Cloud Auto-Fulfillment
  customer-managed-keys: Tri-Secret Secure
  data-applications: Streamlit in Snowflake and Snowflake Native Apps
  data-catalogue: Horizon Catalog (Catalog Explorer, Universal Search)
  data-export: unloading (COPY INTO <location>)
  data-marketplace: Snowflake Marketplace and Internal Marketplace
  data-quality-rules: data metric functions (DMFs) with expectations
  data-security-posture: Trust Center
  data-skipping-indexes: Search Optimization Service and micro-partition pruning
  dataframe-apis: Snowpark, pandas on Snowflake, Snowpark Connect
  declarative-pipelines: Dynamic Tables
  document-processing: AI_PARSE_DOCUMENT and AI_EXTRACT (formerly Document AI)
  file-ingestion: Snowpipe (continuous) and COPY INTO (bulk)
  internal-data-sharing: Secure Data Sharing and organisational listings
  materialised-views: materialized views
  model-monitoring: ML Observability (model monitors)
  multi-tenancy: organisations and accounts
  notebooks: Notebooks in Workspaces
  operational-database: hybrid tables (Unistore) and Snowflake Postgres
  partitioning-clustering: clustering keys and Automatic Clustering
  platform-observability: Snowflake Trail (event tables)
  privacy-enhancing-technologies: aggregation, projection, join and privacy (differential privacy) policies
  provisioned-compute: virtual warehouses
  query-federation: catalog-linked databases and external tables
  real-time-analytics: interactive tables and interactive warehouses
  result-caching: persisted query results
  row-level-security: row access policies
  schema-change-management: DCM Projects (Database Change Management)
  semantic-layer: semantic views
  serverless-compute: serverless features (Snowpipe, serverless tasks, Automatic Clustering) and Adaptive Compute
  spend-controls: resource monitors, budgets and per-user quotas
  storage-tiering: storage lifecycle policies (COOL and COLD archive tiers)
  streaming-ingestion: Snowpipe Streaming
  system-telemetry: ACCOUNT_USAGE and ORGANIZATION_USAGE schemas
  table-catalogue: Horizon Catalog / Horizon Iceberg REST Catalog
  time-travel: Time Travel
  vector-search: Cortex Search
  workflow-orchestration: tasks and task graphs
families:
- name: Snowflake Cortex AI
  aliases: [Snowflake Cortex, Cortex AI]
  technologies:
  - snowflake-cortex-ai-functions
  - snowflake-cortex-document-functions
  - snowflake-cortex-search
  - snowflake-cortex-analyst
  - snowflake-cortex-agents
  - snowflake-cortex-rest-api
  - snowflake-cortex-fine-tuning
  - snowflake-cortex-knowledge-extensions
  - snowflake-cortex-ai-guardrails
  - snowflake-cortex-ai-gateway
  - snowflake-cortex-ai-function-studio
  - snowflake-ai-observability
  - snowflake-managed-mcp-server
- name: Snowflake Horizon Catalog
  aliases: [Snowflake Horizon, Horizon]
  technologies:
  - snowflake-horizon-catalog
  - snowflake-horizon-context
  - snowflake-horizon-iceberg-rest-catalog
  - snowflake-catalog-linked-databases
  - snowflake-universal-search
  - snowflake-internal-marketplace
  - snowflake-data-lineage
  - snowflake-external-lineage
  - snowflake-object-tagging
  - snowflake-sensitive-data-classification
  - snowflake-masking-policies
  - snowflake-row-access-policies
  - snowflake-aggregation-policies
  - snowflake-projection-policies
  - snowflake-differential-privacy
  - snowflake-access-history
  - snowflake-data-quality-monitoring
  - snowflake-trust-center
  - snowflake-cortex-descriptions
  - snowflake-intent-driven-governance
- name: Snowpark
  technologies:
  - snowflake-snowpark
  - snowflake-pandas-on-snowflake
  - snowflake-snowpark-connect-for-spark
  - snowflake-snowpark-container-services
  - snowflake-snowpark-optimized-warehouses
  - snowflake-udfs-and-procedures
- name: Snowflake ML
  aliases: [Snowpark ML]
  technologies:
  - snowflake-feature-store
  - snowflake-online-feature-store
  - snowflake-ml-experiments
  - snowflake-ml-jobs
  - snowflake-container-runtime
  - snowflake-model-registry
  - snowflake-model-serving
  - snowflake-ml-observability
  - snowflake-ml-functions
- name: Snowflake Collaboration
  aliases: [Snowflake data sharing]
  technologies:
  - snowflake-secure-data-sharing
  - snowflake-listings
  - snowflake-marketplace
  - snowflake-internal-marketplace
  - snowflake-native-app-framework
  - snowflake-data-clean-rooms
  - snowflake-open-data-sharing
  - snowflake-cortex-knowledge-extensions
- name: Snowflake warehouses
  aliases: [Snowflake warehouse types]
  technologies:
  - snowflake-virtual-warehouses
  - snowflake-gen2-warehouses
  - snowflake-multi-cluster-warehouses
  - snowflake-snowpark-optimized-warehouses
  - snowflake-adaptive-compute
  - snowflake-interactive-tables
  - snowflake-query-acceleration-service
- name: Snowpipe
  technologies: [snowflake-snowpipe, snowflake-snowpipe-streaming]
- name: Snowflake Postgres
  technologies: [snowflake-postgres, snowflake-postgres-data-mirroring, snowflake-pg-lake]
- name: Snowsight
  technologies:
  - snowflake-workspaces
  - snowflake-notebooks
  - snowflake-snowsight-dashboards
  - snowflake-query-profile
  - snowflake-universal-search
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Snowflake, marketed as the AI Data Cloud, is a SaaS data platform that runs in regions of AWS, Azure and Google Cloud. Snowflake manages table storage, either in its own micro-partitioned format or as Apache Iceberg tables in Snowflake or customer storage, and customers run work on separately billed compute: virtual warehouses (standard, multi-cluster, Snowpark-optimised, interactive and adaptive), serverless features and Snowpark Container Services compute pools. Accounts are grouped into organisations, and the edition (Standard, Enterprise, Business Critical or Virtual Private Snowflake) decides which governance, resilience and security features are available.

Services are layered on that core. Openflow, Snowpipe, Snowpipe Streaming and COPY INTO load data; Dynamic Tables, streams, tasks, dbt Projects and Snowpark transform it; and DCM Projects, Snowflake CLI and Git integration manage change. Horizon Catalog holds governance and discovery: tagging, classification, masking and row access policies, privacy policies, lineage, data quality monitoring, the Trust Center and the Iceberg REST catalogue. Cortex AI provides AI functions, Cortex Search, Cortex Analyst and Cortex Agents, which Snowflake CoWork puts in front of business users, while CoCo is the coding agent for developers and Snowflake ML covers features, training, registry, serving and monitoring. Collaboration covers Secure Data Sharing, listings, Snowflake Marketplace, Native Apps and Data Clean Rooms. Hybrid tables and Snowflake Postgres serve transactional workloads.

# Notes

- Renamed in 2026: Snowflake Intelligence became Snowflake CoWork and Cortex Code became CoCo (both June 2026), and snapshots became backups. CoCo is replacing Snowflake Copilot. Earlier renames include Cortex AISQL to Cortex AI Functions, Polaris Catalog to Snowflake Open Catalog and Snowpark ML to Snowflake ML.
- Several products came from acquisitions: Data Clean Rooms from Samooha, Openflow from Datavolo (second generation GA September 2026), Snowflake Postgres from Crunchy Data (GA February 2026) and Observe by Snowflake from Observe.
- Many governance features, such as masking and row access policies, tagging, lineage and data quality monitoring, need Enterprise Edition. Failover, Tri-Secret Secure and private connectivity need Business Critical Edition.
- Snowflake-managed Iceberg tables and the Horizon Iceberg REST Catalog let Spark, Trino and other engines work on the same tables. Snowflake Open Catalog, the separate managed Apache Polaris service, is closed to new customers.
- There is no customer-hosted deployment. Virtual Private Snowflake gives a dedicated deployment, and Openflow can run its data plane in the customer's cloud. SAP resells Snowflake inside SAP Business Data Cloud as [SAP Snowflake](../technologies/sap/sap-snowflake.md), which is in preview.
- Snowflake has no native master data management, reverse ETL, graph database or managed file transfer. Partners supply these through Marketplace listings and Native Apps.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 13 of 22 | [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Database extraction](../capabilities/ingestion-integration/database-extraction.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 21 of 23 | [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [Data branching and tagging](../capabilities/storage/data-branching.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 11 of 18 | [Data enrichment](../capabilities/processing/data-enrichment.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Low-code transformation](../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../capabilities/processing/data-preparation.md), [Stream processing](../capabilities/processing/stream-processing.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 4 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md) |
| [Query and compute](../capabilities/compute/compute.md) | 18 of 22 | [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 8 of 13 | [Data APIs](../capabilities/serving/data-apis.md), [Decision management](../capabilities/serving/decision-management.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 9 of 20 | [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 16 of 20 (+1 in preview) | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md) (preview only) |
| [ML operations](../capabilities/mlops/mlops.md) | 13 of 18 | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 14 of 23 (+2 in preview) | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md), [Prompt management](../capabilities/generative-ai/prompt-management.md) (preview only), [AI gateway](../capabilities/generative-ai/ai-gateway.md) (preview only) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 14 of 20 | [Schema registry](../capabilities/metadata/schema-registry.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 6 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 8 of 24 | [AI governance](../capabilities/governance/ai-governance.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 15 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 7 of 8 (+1 in preview) | [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) (preview only) |
| [Data products](../capabilities/data-products/data-products.md) | 4 of 7 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 15 of 16 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 21 of 27 | [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 7 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Product families

- **Snowflake Cortex AI** (also: Snowflake Cortex, Cortex AI): [Snowflake Cortex AI Functions](../technologies/snowflake/snowflake-cortex-ai-functions.md), [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../technologies/snowflake/snowflake-cortex-document-functions.md), [Snowflake Cortex Search](../technologies/snowflake/snowflake-cortex-search.md), [Snowflake Cortex Analyst](../technologies/snowflake/snowflake-cortex-analyst.md), [Snowflake Cortex Agents](../technologies/snowflake/snowflake-cortex-agents.md), [Snowflake Cortex REST API](../technologies/snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex Fine-tuning](../technologies/snowflake/snowflake-cortex-fine-tuning.md), [Snowflake Cortex Knowledge Extensions](../technologies/snowflake/snowflake-cortex-knowledge-extensions.md), [Snowflake Cortex AI Guardrails](../technologies/snowflake/snowflake-cortex-ai-guardrails.md), [Snowflake Cortex AI Gateway](../technologies/snowflake/snowflake-cortex-ai-gateway.md) (preview), [Snowflake Cortex AI Function Studio](../technologies/snowflake/snowflake-cortex-ai-function-studio.md) (preview), [Snowflake AI Observability](../technologies/snowflake/snowflake-ai-observability.md), [Snowflake-managed MCP server](../technologies/snowflake/snowflake-managed-mcp-server.md)
- **Snowflake Horizon Catalog** (also: Snowflake Horizon, Horizon): [Snowflake Horizon Catalog](../technologies/snowflake/snowflake-horizon-catalog.md), [Snowflake Horizon Context](../technologies/snowflake/snowflake-horizon-context.md) (preview), [Snowflake Horizon Iceberg REST Catalog API](../technologies/snowflake/snowflake-horizon-iceberg-rest-catalog.md), [Snowflake catalog-linked databases](../technologies/snowflake/snowflake-catalog-linked-databases.md), [Snowflake Universal Search](../technologies/snowflake/snowflake-universal-search.md), [Snowflake Internal Marketplace (organisational listings)](../technologies/snowflake/snowflake-internal-marketplace.md), [Snowflake data lineage (Snowsight lineage)](../technologies/snowflake/snowflake-data-lineage.md), [Snowflake external lineage](../technologies/snowflake/snowflake-external-lineage.md), [Snowflake object tagging](../technologies/snowflake/snowflake-object-tagging.md), [Snowflake sensitive data classification](../technologies/snowflake/snowflake-sensitive-data-classification.md), [Snowflake masking policies](../technologies/snowflake/snowflake-masking-policies.md), [Snowflake row access policies](../technologies/snowflake/snowflake-row-access-policies.md), [Snowflake aggregation policies](../technologies/snowflake/snowflake-aggregation-policies.md), [Snowflake projection policies](../technologies/snowflake/snowflake-projection-policies.md), [Snowflake differential privacy](../technologies/snowflake/snowflake-differential-privacy.md), [Snowflake Access History](../technologies/snowflake/snowflake-access-history.md), [Snowflake data quality monitoring (data metric functions)](../technologies/snowflake/snowflake-data-quality-monitoring.md), [Snowflake Trust Center](../technologies/snowflake/snowflake-trust-center.md), [Snowflake AI-generated descriptions](../technologies/snowflake/snowflake-cortex-descriptions.md), [Snowflake Intent-Driven Governance](../technologies/snowflake/snowflake-intent-driven-governance.md) (preview)
- **Snowpark**: [Snowpark](../technologies/snowflake/snowflake-snowpark.md), [pandas on Snowflake](../technologies/snowflake/snowflake-pandas-on-snowflake.md), [Snowpark Connect for Apache Spark](../technologies/snowflake/snowflake-snowpark-connect-for-spark.md), [Snowpark Container Services](../technologies/snowflake/snowflake-snowpark-container-services.md), [Snowpark-optimized warehouses](../technologies/snowflake/snowflake-snowpark-optimized-warehouses.md), [Snowflake user-defined functions and stored procedures](../technologies/snowflake/snowflake-udfs-and-procedures.md)
- **Snowflake ML** (also: Snowpark ML): [Snowflake Feature Store](../technologies/snowflake/snowflake-feature-store.md), [Snowflake Online Feature Store](../technologies/snowflake/snowflake-online-feature-store.md) (preview), [Snowflake ML Experiments](../technologies/snowflake/snowflake-ml-experiments.md), [Snowflake ML Jobs](../technologies/snowflake/snowflake-ml-jobs.md), [Snowflake Container Runtime for ML](../technologies/snowflake/snowflake-container-runtime.md), [Snowflake Model Registry](../technologies/snowflake/snowflake-model-registry.md), [Snowflake Model Serving in Snowpark Container Services](../technologies/snowflake/snowflake-model-serving.md), [Snowflake ML Observability (model monitors)](../technologies/snowflake/snowflake-ml-observability.md), [Snowflake ML Functions](../technologies/snowflake/snowflake-ml-functions.md)
- **Snowflake Collaboration** (also: Snowflake data sharing): [Snowflake Secure Data Sharing](../technologies/snowflake/snowflake-secure-data-sharing.md), [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../technologies/snowflake/snowflake-listings.md), [Snowflake Marketplace](../technologies/snowflake/snowflake-marketplace.md), [Snowflake Internal Marketplace (organisational listings)](../technologies/snowflake/snowflake-internal-marketplace.md), [Snowflake Native App Framework](../technologies/snowflake/snowflake-native-app-framework.md), [Snowflake Data Clean Rooms](../technologies/snowflake/snowflake-data-clean-rooms.md), [Snowflake Open Data Sharing](../technologies/snowflake/snowflake-open-data-sharing.md) (preview), [Snowflake Cortex Knowledge Extensions](../technologies/snowflake/snowflake-cortex-knowledge-extensions.md)
- **Snowflake warehouses** (also: Snowflake warehouse types): [Snowflake virtual warehouses](../technologies/snowflake/snowflake-virtual-warehouses.md), [Snowflake generation 2 standard warehouses](../technologies/snowflake/snowflake-gen2-warehouses.md), [Snowflake multi-cluster warehouses](../technologies/snowflake/snowflake-multi-cluster-warehouses.md), [Snowpark-optimized warehouses](../technologies/snowflake/snowflake-snowpark-optimized-warehouses.md), [Snowflake Adaptive Compute](../technologies/snowflake/snowflake-adaptive-compute.md), [Snowflake interactive tables and interactive warehouses](../technologies/snowflake/snowflake-interactive-tables.md), [Snowflake Query Acceleration Service](../technologies/snowflake/snowflake-query-acceleration-service.md)
- **Snowpipe**: [Snowpipe](../technologies/snowflake/snowflake-snowpipe.md), [Snowpipe Streaming](../technologies/snowflake/snowflake-snowpipe-streaming.md)
- **Snowflake Postgres**: [Snowflake Postgres](../technologies/snowflake/snowflake-postgres.md), [Data mirroring for Snowflake Postgres](../technologies/snowflake/snowflake-postgres-data-mirroring.md), [pg_lake](../technologies/snowflake/snowflake-pg-lake.md) (preview)
- **Snowsight**: [Snowsight Workspaces](../technologies/snowflake/snowflake-workspaces.md), [Snowflake Notebooks in Workspaces](../technologies/snowflake/snowflake-notebooks.md), [Snowsight dashboards](../technologies/snowflake/snowflake-snowsight-dashboards.md), [Snowflake Query History, Query Profile and query insights](../technologies/snowflake/snowflake-query-profile.md), [Snowflake Universal Search](../technologies/snowflake/snowflake-universal-search.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| ACCOUNT_USAGE and ORGANIZATION_USAGE schemas | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) |
| aggregation, projection, join and privacy (differential privacy) policies | [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md) |
| AI_PARSE_DOCUMENT and AI_EXTRACT (formerly Document AI) | [Document processing](../capabilities/processing/document-processing.md) |
| backups (formerly snapshots); Fail-safe | [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| catalog-linked databases and external tables | [Query federation](../capabilities/compute/query-federation.md) |
| clustering keys and Automatic Clustering | [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md) |
| CoCo (formerly Cortex Code; replacing Snowflake Copilot) | [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md) |
| Cortex AI Functions (formerly Cortex AISQL) | [AI functions in SQL](../capabilities/processing/ai-functions.md) |
| Cortex Analyst and Snowflake CoWork (formerly Snowflake Intelligence) | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| Cortex Search | [Vector search](../capabilities/generative-ai/vector-search.md) |
| Cross-Cloud Auto-Fulfillment | [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md) |
| data metric functions (DMFs) with expectations | [Data quality rules](../capabilities/data-quality/data-quality-rules.md) |
| DCM Projects (Database Change Management) | [Schema change management](../capabilities/development-lifecycle/schema-change-management.md) |
| Dynamic Tables | [Declarative pipelines](../capabilities/processing/declarative-pipelines.md) |
| Horizon Catalog (Catalog Explorer, Universal Search) | [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| Horizon Catalog / Horizon Iceberg REST Catalog | [Table catalogue](../capabilities/storage/table-catalogue.md) |
| hybrid tables (Unistore) and Snowflake Postgres | [Operational database integration](../capabilities/serving/operational-database.md) |
| interactive tables and interactive warehouses | [Real-time analytical database](../capabilities/compute/real-time-analytics.md) |
| masking policies | [Column security and dynamic masking](../capabilities/security/column-masking.md) |
| materialized views | [Materialised views](../capabilities/compute/materialised-views.md) |
| ML Observability (model monitors) | [Model monitoring](../capabilities/mlops/model-monitoring.md) |
| Notebooks in Workspaces | [Notebooks](../capabilities/development-lifecycle/notebooks.md) |
| Openflow CDC connectors; data mirroring (Snowflake Postgres) | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) |
| organisations and accounts | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| persisted query results | [Result caching](../capabilities/compute/result-caching.md) |
| replication and failover groups | [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md) |
| resource monitors, budgets and per-user quotas | [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) |
| row access policies | [Row-level security](../capabilities/security/row-level-security.md) |
| Search Optimization Service and micro-partition pruning | [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md) |
| Secure Data Sharing and organisational listings | [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md) |
| semantic views | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) |
| serverless features (Snowpipe, serverless tasks, Automatic Clustering) and Adaptive Compute | [Serverless compute](../capabilities/compute/serverless-compute.md) |
| Snowflake Marketplace and Internal Marketplace | [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| Snowflake Trail (event tables) | [Platform observability](../capabilities/platform-operations/platform-observability.md) |
| Snowflake-managed MCP server | [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) |
| Snowpark Container Services (SPCS), compute pools | [Container services](../capabilities/compute/container-services.md) |
| Snowpark, pandas on Snowflake, Snowpark Connect | [DataFrame APIs](../capabilities/processing/dataframe-apis.md) |
| Snowpipe (continuous) and COPY INTO (bulk) | [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| Snowpipe Streaming | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |
| storage lifecycle policies (COOL and COLD archive tiers) | [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) |
| Streamlit in Snowflake and Snowflake Native Apps | [Data application hosting](../capabilities/development-lifecycle/data-applications.md) |
| streams | [Change feeds](../capabilities/serving/change-feeds.md) |
| tag-based masking policies | [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md) |
| tasks and task graphs | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| Time Travel | [Time travel](../capabilities/storage/time-travel.md) |
| Tri-Secret Secure | [Customer-managed keys](../capabilities/security/customer-managed-keys.md) |
| Trust Center | [Data security posture management](../capabilities/security/data-security-posture.md) |
| unloading (COPY INTO <location>) | [Data export](../capabilities/serving/data-export.md) |
| virtual warehouses | [Provisioned compute](../capabilities/compute/provisioned-compute.md) |

# Technologies

## Ingestion and integration

- [Data mirroring for Snowflake Postgres](../technologies/snowflake/snowflake-postgres-data-mirroring.md): Continuously replicates Postgres tables or whole schemas into Snowflake tables from the write-ahead log, with sub-minute lag and source transaction boundaries kept.
- [Snowflake bulk loading (COPY INTO <table>)](../technologies/snowflake/snowflake-copy-into.md): Loads staged files in bulk into tables on a warehouse, tracking which files were loaded so they are not loaded twice.
- [Snowflake Connector for Kafka](../technologies/snowflake/snowflake-connector-for-kafka.md): A Kafka Connect sink connector that loads topics into Snowflake tables using Snowpipe Streaming.
- [Snowflake external network access (external access integrations)](../technologies/snowflake/snowflake-external-access-integrations.md): Lets UDFs, procedures and container services call approved external endpoints over the network, using network rules and secrets, for example to pull data from REST APIs.
- [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../technologies/snowflake/snowflake-native-connectors.md): Connectors packaged as Snowflake Native Apps that ingest and refresh data from SaaS applications and databases incrementally, some using a customer-run agent for change data capture.
- [Snowflake Openflow](../technologies/snowflake/snowflake-openflow.md): A managed integration service, built on Apache NiFi, that runs prebuilt and custom connectors for databases, SaaS, streams and unstructured content in batch or streaming mode.
- [Snowpipe](../technologies/snowflake/snowflake-snowpipe.md): A serverless pipe that loads files continuously from stages as they arrive, triggered by cloud storage event notifications or REST calls.
- [Snowpipe Streaming](../technologies/snowflake/snowflake-snowpipe-streaming.md): Ingests rows directly into tables through SDKs (Java, Python, Node.js) or a REST API, with no files, making data queryable within seconds.

## Storage and table management

- [Apache Iceberg tables in Snowflake](../technologies/snowflake/snowflake-iceberg-tables.md): Tables stored as Parquet files with Apache Iceberg metadata, managed either by Snowflake as catalogue or by an external catalogue, in customer storage or in Snowflake storage.
- [Snowflake catalog-linked databases](../technologies/snowflake/snowflake-catalog-linked-databases.md): Databases linked to an external Iceberg REST catalogue (for example AWS Glue, Unity Catalog, Open Catalog, BigLake or S3 Tables) that discover and sync remote namespaces and tables automatically for querying and writing.
- [Snowflake clustering keys and Automatic Clustering](../technologies/snowflake/snowflake-clustering-keys.md): Lets you declare clustering columns on large tables, then reorganises micro-partitions in the background to keep them well clustered so pruning stays effective.
- [Snowflake micro-partitioned table storage](../technologies/snowflake/snowflake-managed-storage.md): Stores standard tables in immutable, compressed, columnar micro-partitions with per-partition statistics that Snowflake manages, giving ACID transactions and partition pruning.
- [Snowflake Open Catalog](../technologies/snowflake/snowflake-open-catalog.md) (deprecated): A separate managed Apache Polaris service that acts as an Iceberg REST catalogue with central access control for Iceberg tables shared across engines.
- [Snowflake semi-structured data types (VARIANT, OBJECT, ARRAY)](../technologies/snowflake/snowflake-semi-structured-data.md): Stores JSON, Avro, ORC, Parquet and XML in VARIANT, OBJECT and ARRAY columns, extracting columns for pruning, and queries them with path notation and FLATTEN.
- [Snowflake stages and directory tables](../technologies/snowflake/snowflake-stages-directory-tables.md): Internal and external stages hold files in object storage, and directory tables catalogue the staged files with metadata so unstructured content can be listed, governed and processed with SQL.
- [Snowflake storage lifecycle policies](../technologies/snowflake/snowflake-storage-lifecycle-policies.md): Schema-level policies that archive table rows to cheaper COOL or COLD tiers, or delete them permanently, according to conditions such as age.
- [Snowflake Time Travel](../technologies/snowflake/snowflake-time-travel.md): Queries, clones or undrops tables, schemas and databases as they were at an earlier point within a retention period of up to 90 days.
- [Snowflake zero-copy cloning](../technologies/snowflake/snowflake-zero-copy-cloning.md): Creates instant writable copies of tables, schemas or databases that share micro-partitions with the source until either side changes.

## Processing and transformation

- [dbt Projects on Snowflake](../technologies/snowflake/snowflake-dbt-projects.md): Deploys, runs, schedules and monitors dbt projects as Snowflake objects on a dbt Core or dbt Fusion runtime that Snowflake manages, developed in Workspaces or from Git.
- [pandas on Snowflake](../technologies/snowflake/snowflake-pandas-on-snowflake.md): A Modin-based pandas API that turns pandas operations on Snowflake data into SQL, and chooses per operation whether to run them locally or in Snowflake (hybrid execution).
- [Snowflake Cortex AI Functions](../technologies/snowflake/snowflake-cortex-ai-functions.md): SQL functions such as AI_COMPLETE, AI_CLASSIFY, AI_FILTER, AI_AGG, AI_SUMMARIZE_AGG, AI_EMBED, AI_SENTIMENT, AI_TRANSLATE, AI_TRANSCRIBE and AI_REDACT that apply hosted models to columns and files.
- [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../technologies/snowflake/snowflake-cortex-document-functions.md): AI_PARSE_DOCUMENT turns PDFs and images into text and layout, and AI_EXTRACT pulls named fields, tables and entities out of documents.
- [Snowflake Dynamic Tables](../technologies/snowflake/snowflake-dynamic-tables.md): Tables defined by a query and a target lag that Snowflake keeps refreshed, incrementally where possible, working out dependency order across chains of dynamic tables.
- [Snowflake user-defined functions and stored procedures](../technologies/snowflake/snowflake-udfs-and-procedures.md): Custom scalar, table and aggregate functions and stored procedures written in SQL, Snowflake Scripting, JavaScript, Python, Java or Scala that run inside Snowflake.
- [Snowpark](../technologies/snowflake/snowflake-snowpark.md): DataFrame and function APIs for Python, Java and Scala that push processing down into Snowflake warehouses as SQL, plus runtimes for running that code in the engine.
- [Snowpark Connect for Apache Spark](../technologies/snowflake/snowflake-snowpark-connect-for-spark.md): Runs existing Spark DataFrame and Spark SQL code on Snowflake compute through the Spark Connect protocol, so there is no Spark cluster to manage.

## Orchestration

- [Snowflake tasks and task graphs](../technologies/snowflake/snowflake-tasks.md): Run SQL, procedures or code on a schedule, in dependency graphs, or when a stream has new data, on serverless or user-managed compute.

## Query and compute

- [pg_lake](../technologies/snowflake/snowflake-pg-lake.md) (preview): An open-source Postgres extension from Snowflake that reads and writes Iceberg tables and Parquet files in object storage from Postgres.
- [Snowflake Adaptive Compute](../technologies/snowflake/snowflake-adaptive-compute.md): A warehouse type (adaptive warehouses) for which Snowflake decides the resources for each query, so you do not set a size, multi-cluster settings or suspend policies.
- [Snowflake external tables](../technologies/snowflake/snowflake-external-tables.md): Read-only tables over files in external stages, with optional automatic metadata refresh, so data in a lake can be queried without loading it.
- [Snowflake generation 2 standard warehouses](../technologies/snowflake/snowflake-gen2-warehouses.md): The newer generation of standard warehouses, running on faster hardware with optimisations for DELETE, UPDATE, MERGE and table scans.
- [Snowflake Horizon Iceberg REST Catalog API](../technologies/snowflake/snowflake-horizon-iceberg-rest-catalog.md): An Apache Polaris-based Iceberg REST catalogue endpoint in each account that lets Spark, Trino, Flink, DuckDB, PyIceberg and other engines read and write Snowflake-managed Iceberg tables under Snowflake RBAC.
- [Snowflake interactive tables and interactive warehouses](../technologies/snowflake/snowflake-interactive-tables.md): A table type and a matching warehouse type built for sub-second, highly concurrent queries such as user-facing dashboards and data APIs.
- [Snowflake materialized views](../technologies/snowflake/snowflake-materialized-views.md): Stores the results of a single-table query and keeps them up to date automatically in the background, so queries read precomputed results.
- [Snowflake multi-cluster warehouses](../technologies/snowflake/snowflake-multi-cluster-warehouses.md): Adds and removes clusters of the same size automatically, according to a scaling policy, to absorb bursts of concurrent queries without queuing.
- [Snowflake persisted query results (result cache)](../technologies/snowflake/snowflake-result-cache.md): Returns the stored result of an identical earlier query, for 24 hours and up to 31 days with reuse, when the underlying data has not changed, without using warehouse compute.
- [Snowflake Query Acceleration Service](../technologies/snowflake/snowflake-query-acceleration-service.md): Offloads parts of large scans and filters in eligible queries to shared serverless compute, so outlier queries finish faster without enlarging the warehouse.
- [Snowflake Search Optimization Service](../technologies/snowflake/snowflake-search-optimization-service.md): Builds and maintains a persistent search access path on chosen tables and columns, so point lookups, substring, semi-structured, geospatial and full-text SEARCH queries skip most micro-partitions.
- [Snowflake virtual warehouses](../technologies/snowflake/snowflake-virtual-warehouses.md): Named clusters of compute, sized from X-Small to 6X-Large, that run SQL and Snowpark workloads against shared storage and suspend and resume automatically.
- [Snowpark Container Services](../technologies/snowflake/snowflake-snowpark-container-services.md): Runs OCI container images as long-running services or finite jobs on Snowflake-managed compute pools, including GPU nodes, inside the account's security boundary.
- [Snowpark-optimized warehouses](../technologies/snowflake/snowflake-snowpark-optimized-warehouses.md): Warehouses with much more memory per node, and configurable CPU architecture, for memory-intensive Snowpark, UDF and single-node ML training work.

## Serving and activation

- [Snowflake data unloading (COPY INTO <location>)](../technologies/snowflake/snowflake-unload.md): Writes query results or tables to files in internal or external stages as CSV, JSON or Parquet, optionally partitioned.
- [Snowflake drivers, connectors and SQL API](../technologies/snowflake/snowflake-drivers-sql-api.md): JDBC, ODBC, Python, Go, .NET and Node.js drivers, the Spark connector and a REST SQL API for connecting tools and applications to Snowflake.
- [Snowflake hybrid tables (Unistore)](../technologies/snowflake/snowflake-hybrid-tables.md): A row-oriented table type with enforced primary, unique and foreign keys, indexes and row locking, for low-latency point reads and writes in the same engine as analytical tables.
- [Snowflake Postgres](../technologies/snowflake/snowflake-postgres.md): Fully managed PostgreSQL instances, on versions 16 to 18, created and governed from Snowflake, running on dedicated Snowflake-managed machines with PgBouncer pooling and private networking.
- [Snowflake streams](../technologies/snowflake/snowflake-streams.md): Track inserts, updates and deletes on tables, views and other objects since an offset, so downstream jobs process only the changes.

## Analytics and BI

- [Snowflake alerts and notifications](../technologies/snowflake/snowflake-alerts.md): Scheduled or event-driven conditions written in SQL that run an action, such as sending email, webhook or cloud-queue notifications, when data meets them.
- [Snowflake Cortex Analyst](../technologies/snowflake/snowflake-cortex-analyst.md): Turns natural-language questions into SQL over semantic views and returns the answers, through a REST API or as an agent tool.
- [Snowflake CoWork](../technologies/snowflake/snowflake-cowork.md): A conversational agent application for business users that answers questions over structured and unstructured data, runs deep research, and produces artefacts, documents and scheduled automations.
- [Snowflake Horizon Context](../technologies/snowflake/snowflake-horizon-context.md) (preview): A layer of Horizon Catalog that gathers external metadata and lineage, enriches it with semantics, popularity and AI descriptions, and exposes it to agents and BI tools through search and MCP.
- [Snowflake semantic views](../technologies/snowflake/snowflake-semantic-views.md): Schema-level objects that define logical tables, relationships, facts, dimensions and metrics, queried with SQL and used by Cortex Analyst, agents and BI tools.
- [Snowsight dashboards](../technologies/snowflake/snowflake-snowsight-dashboards.md): Simple dashboards built from charts and tables of query results in Snowsight, shared with other Snowflake users.
- [Snowsight Workspaces](../technologies/snowflake/snowflake-workspaces.md): A file-based editor in Snowsight for SQL, Python, notebooks, dbt projects, Streamlit apps and semantic views, with Git integration, sharing and AI code suggestions.

## Machine learning development

- [Snowflake Container Runtime for ML](../technologies/snowflake/snowflake-container-runtime.md): A prebuilt CPU and GPU ML environment on Snowpark Container Services, with distributed data loading, training and hyperparameter tuning built on Ray.
- [Snowflake Feature Store](../technologies/snowflake/snowflake-feature-store.md): Python APIs and objects for defining entities and feature views (as Dynamic Tables or views), generating point-in-time correct training sets and retrieving features for batch inference.
- [Snowflake ML Experiments](../technologies/snowflake/snowflake-ml-experiments.md): Records runs with parameters, metrics, artefacts and logs inside experiments, with autologging for common libraries and side-by-side comparison in Snowsight.
- [Snowflake ML Functions](../technologies/snowflake/snowflake-ml-functions.md): SQL-callable model classes for time-series forecasting, anomaly detection, classification and top insights, which train and run without ML code.
- [Snowflake ML Jobs](../technologies/snowflake/snowflake-ml-jobs.md): Submits Python functions, files or code bundles from any IDE or from SQL to run as jobs on Container Runtime compute pools, including on multiple nodes.
- [Snowflake Model Registry](../technologies/snowflake/snowflake-model-registry.md): Stores versioned models trained in Snowflake or elsewhere as schema-level objects with metadata, metrics and aliases, and runs their methods from SQL or Python for batch inference.
- [Snowflake Online Feature Store](../technologies/snowflake/snowflake-online-feature-store.md) (preview): Syncs feature views to a low-latency online store and serves them by key through a REST API, with stream and real-time feature views for sub-minute freshness.

## ML operations

- [Snowflake ML Observability (model monitors)](../technologies/snowflake/snowflake-ml-observability.md): Model monitor objects that compute drift, performance and statistical metrics from logged inference data, with dashboards and threshold alerts.
- [Snowflake Model Serving in Snowpark Container Services](../technologies/snowflake/snowflake-model-serving.md): Deploys registry models as autoscaling CPU or GPU inference services with HTTP endpoints, with gateway-based traffic splitting for shadow and canary releases.

## Generative AI

- [Snowflake AI Observability](../technologies/snowflake/snowflake-ai-observability.md): Tracing, cost tracking and batch evaluation for agents, Cortex Search, CoCo and custom TruLens-instrumented apps, stored in an account event table and viewed in Snowsight.
- [Snowflake Cortex Agents](../technologies/snowflake/snowflake-cortex-agents.md): Schema-level agent objects that plan, call tools such as Cortex Analyst, Cortex Search, custom procedures, sandboxed Python code execution and web search, and answer with governed data.
- [Snowflake Cortex AI Function Studio](../technologies/snowflake/snowflake-cortex-ai-function-studio.md) (preview): A Snowsight workspace for designing prompts for Cortex AI Functions, evaluating them against labelled data and optimising them.
- [Snowflake Cortex AI Gateway](../technologies/snowflake/snowflake-cortex-ai-gateway.md) (preview): A single governed endpoint for AI clients that routes model calls, records traces and token use, and attributes spend to teams and users under budgets and quotas.
- [Snowflake Cortex AI Guardrails](../technologies/snowflake/snowflake-cortex-ai-guardrails.md): Runtime checks that detect prompt injection and jailbreak attempts, including indirect injection in tool outputs, for Cortex Agents, CoWork and CoCo.
- [Snowflake Cortex Fine-tuning](../technologies/snowflake/snowflake-cortex-fine-tuning.md): Builds parameter-efficient fine-tuned adaptors for supported base models from training data in Snowflake, for inference through AI_COMPLETE.
- [Snowflake Cortex Knowledge Extensions](../technologies/snowflake/snowflake-cortex-knowledge-extensions.md): Cortex Search services shared as Marketplace or private listings, so a consumer's agents and RAG apps can search a provider's content, with citations.
- [Snowflake Cortex REST API](../technologies/snowflake/snowflake-cortex-rest-api.md): REST endpoints, including chat-completions-style APIs, that give applications access to the large language models hosted in Snowflake's security boundary.
- [Snowflake Cortex Search](../technologies/snowflake/snowflake-cortex-search.md): A managed hybrid vector and keyword search service, with reranking, that embeds, indexes and refreshes text from a query or stage on a target lag.
- [Snowflake-managed MCP server](../technologies/snowflake/snowflake-managed-mcp-server.md): A Snowflake object that exposes Cortex Agents, Cortex Analyst, Cortex Search, SQL execution and custom functions as Model Context Protocol tools to external AI clients under RBAC.

## Metadata and discovery

- [Snowflake AI-generated descriptions](../technologies/snowflake/snowflake-cortex-descriptions.md): Uses Cortex models to draft descriptions of tables, views and columns in Snowsight for owners to review and save as comments.
- [Snowflake data lineage (Snowsight lineage)](../technologies/snowflake/snowflake-data-lineage.md): Records table and column lineage from DML, CTAS and view dependencies, plus ML lineage across datasets, feature views, models and monitors, shown as a graph in Catalog Explorer.
- [Snowflake external lineage](../technologies/snowflake/snowflake-external-lineage.md): Accepts OpenLineage COMPLETE events through a REST endpoint, so tools such as dbt and Airflow can add lineage from outside Snowflake to the lineage graph.
- [Snowflake Horizon Catalog](../technologies/snowflake/snowflake-horizon-catalog.md): Snowflake's built-in catalogue and governance layer, covering object discovery, tagging, policies, quality, lineage, access history and Iceberg catalogue services for Snowflake and external data.
- [Snowflake Universal Search](../technologies/snowflake/snowflake-universal-search.md): Searches object metadata across the account, the Snowflake Marketplace and the Internal Marketplace in Snowsight, in natural language, filtered by the user's privileges.

## Data quality and observability

- [Snowflake data quality monitoring (data metric functions)](../technologies/snowflake/snowflake-data-quality-monitoring.md): Schedules system and custom data metric functions on tables and views, compares results with expectations, and detects volume and freshness anomalies, with results in Snowsight.

## Governance and compliance

- [Snowflake aggregation policies](../technologies/snowflake/snowflake-aggregation-policies.md): Require queries on a protected table to aggregate rows into groups above a minimum size, at row or entity level, so individual records cannot be returned.
- [Snowflake differential privacy](../technologies/snowflake/snowflake-differential-privacy.md): Privacy policies that add calibrated noise to aggregate results on protected tables and track each analyst's cumulative privacy loss against a budget.
- [Snowflake Intent-Driven Governance](../technologies/snowflake/snowflake-intent-driven-governance.md) (preview): A review-first CoCo workflow that turns a governance goal stated in plain language into a scope, a governance specification and SQL for tags and protections, which a person approves before it runs.
- [Snowflake object tagging](../technologies/snowflake/snowflake-object-tagging.md): Schema-level tags with allowed values that are attached to objects and columns, inherited down the hierarchy, and used for classification, cost attribution and tag-based policies.
- [Snowflake projection policies](../technologies/snowflake/snowflake-projection-policies.md): Stop a column from being returned in query output while still allowing it in joins, filters and aggregations.
- [Snowflake sensitive data classification](../technologies/snowflake/snowflake-sensitive-data-classification.md): Scans tables in databases with a classification profile, assigns semantic and privacy categories to sensitive columns, and can map them to your own tags automatically.

## Security and access

- [Snowflake access control (RBAC and database roles)](../technologies/snowflake/snowflake-access-control.md): A hierarchy of account roles, database roles and application roles that hold privileges on securable objects, with secondary roles and managed access schemas.
- [Snowflake Access History](../technologies/snowflake/snowflake-access-history.md): An ACCOUNT_USAGE view that records which columns each query read and which objects it wrote, including through views and policies.
- [Snowflake authentication (SSO, OAuth, key pair, PATs, workload identity federation)](../technologies/snowflake/snowflake-authentication.md): Authenticates users and services through SAML SSO, Snowflake or external OAuth, key pairs, programmatic access tokens, MFA and workload identity federation with cloud identities.
- [Snowflake masking policies](../technologies/snowflake/snowflake-masking-policies.md): Schema-level policies that mask, tokenise or reveal column values at query time depending on role, other context or tags, including external tokenisation through external functions.
- [Snowflake network policies and network rules](../technologies/snowflake/snowflake-network-policies.md): Restrict which IP ranges, VPC endpoints or private endpoints can reach an account or user, and which external destinations workloads can reach.
- [Snowflake private connectivity (AWS PrivateLink, Azure Private Link, Google Cloud Private Service Connect)](../technologies/snowflake/snowflake-private-connectivity.md): Connects clients, internal stages and Snowflake-hosted endpoints to Snowflake over the cloud provider's private network rather than the public internet.
- [Snowflake row access policies](../technologies/snowflake/snowflake-row-access-policies.md): Schema-level policies that decide, using the querying role and mapping tables, which rows of a table or view a query returns.
- [Snowflake secrets](../technologies/snowflake/snowflake-secrets.md): Schema-level secret objects that hold credentials, OAuth tokens and keys for integrations, UDFs, Openflow and container services, so code does not contain them.
- [Snowflake Tri-Secret Secure](../technologies/snowflake/snowflake-tri-secret-secure.md): Combines a Snowflake-maintained key with a customer-managed key in the cloud provider's KMS to create the composite master key for account data, so revoking the customer key makes data unreadable.
- [Snowflake Trust Center](../technologies/snowflake/snowflake-trust-center.md): Runs scanner packages (Security Essentials, CIS Benchmarks, Threat Intelligence, AI Security) against accounts and reports violations, detections and at-risk entities.

## Data sharing and collaboration

- [Snowflake Data Clean Rooms](../technologies/snowflake/snowflake-data-clean-rooms.md): Collaborations defined in YAML, in which owners, data providers and analysis runners combine data through approved templates without exposing raw rows to one another.
- [Snowflake Internal Marketplace (organisational listings)](../technologies/snowflake/snowflake-internal-marketplace.md): A private marketplace inside a Snowflake organisation where teams publish organisational listings as data products for discovery and access requests by other accounts.
- [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../technologies/snowflake/snowflake-listings.md): Package a share, app or service with descriptive metadata as a data product for chosen accounts, replicating it automatically to consumers in other regions and clouds.
- [Snowflake Marketplace](../technologies/snowflake/snowflake-marketplace.md): A public catalogue where providers publish free, paid or trial listings of data, Native Apps, Cortex Knowledge Extensions and agents, and consumers subscribe to them.
- [Snowflake Open Data Sharing](../technologies/snowflake/snowflake-open-data-sharing.md) (preview): Shares Iceberg tables as live, read-only data with external consumers outside Snowflake, who read them through standard Iceberg REST Catalog APIs using a programmatic access token.
- [Snowflake Secure Data Sharing](../technologies/snowflake/snowflake-secure-data-sharing.md): Shares live, read-only database objects with other Snowflake accounts through shares, without copying data, with consumers paying for their own compute.

## Development and DataOps

- [Snowflake CLI](../technologies/snowflake/snowflake-cli.md): An open-source command-line tool for running SQL and for building, testing and deploying Snowflake apps, Snowpark code, Streamlit apps, dbt and DCM projects from local machines and CI pipelines.
- [Snowflake CoCo](../technologies/snowflake/snowflake-coco.md): An AI coding agent, available in Snowsight, as a CLI, as a desktop app and in VS Code, that uses Snowflake skills and MCP tools to explore data, write SQL, and build pipelines, dbt projects and apps.
- [Snowflake Copilot](../technologies/snowflake/snowflake-copilot.md) (deprecated): An SQL assistant in Snowsight that generates and explains queries from natural language.
- [Snowflake DCM Projects](../technologies/snowflake/snowflake-dcm-projects.md): Database Change Management projects that declare the desired state of databases, schemas, tables, dynamic tables, views, warehouses, roles, grants and data quality checks in SQL DEFINE files, then plan and deploy the changes.
- [Snowflake Extension for Visual Studio Code](../technologies/snowflake/snowflake-vscode-extension.md) (preview): An IDE extension for connecting to Snowflake, running SQL and Snowpark code, and using CoCo from a local editor.
- [Snowflake Git integration (Git repository objects)](../technologies/snowflake/snowflake-git-integration.md): Syncs remote Git repositories into Snowflake as repository clones, so code can be run with EXECUTE IMMEDIATE FROM and Workspaces, notebooks and Streamlit apps can commit and push.
- [Snowflake Native App Framework](../technologies/snowflake/snowflake-native-app-framework.md): Packages data, code, Streamlit UIs, containers, agents and MCP servers as applications that consumers install and run in their own accounts through listings.
- [Snowflake Notebooks in Workspaces](../technologies/snowflake/snowflake-notebooks.md): Jupyter-compatible notebooks in Snowsight Workspaces that run on Container Runtime CPU or GPU compute, with Git integration, a terminal and scheduling.
- [Snowflake synthetic data generation](../technologies/snowflake/snowflake-synthetic-data.md): The GENERATE_SYNTHETIC_DATA procedure creates statistically similar tables, with the same column names and types, from up to five source tables without linking output rows to real records.
- [Streamlit in Snowflake](../technologies/snowflake/snowflake-streamlit.md): Hosts Streamlit Python apps as Snowflake objects, on warehouse or container runtimes, with access governed by Snowflake roles.

## Platform operations

- [SnowConvert AI](../technologies/snowflake/snowflake-snowconvert-ai.md): A migration tool that assesses and converts SQL code and objects from Teradata, Oracle, SQL Server, Redshift, Synapse, BigQuery, Databricks SQL and other platforms to Snowflake.
- [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../technologies/snowflake/snowflake-account-usage.md): Shared SNOWFLAKE database schemas that expose query, login, metering, storage, access, task, AI and billing history as views, for one account or the whole organisation.
- [Snowflake backups](../technologies/snowflake/snowflake-backups.md): Point-in-time, zero-copy backups of tables, schemas and databases, managed through backup sets and backup policies, with optional retention locks and legal holds.
- [Snowflake budgets](../technologies/snowflake/snowflake-budgets.md): Monthly credit limits for the account or for custom groups of objects (including by tag) that forecast spend, send notifications and can run stored procedures, for example to suspend warehouses.
- [Snowflake cost anomaly detection](../technologies/snowflake/snowflake-cost-anomaly-detection.md): Flags days when account or organisation consumption falls outside the expected range, with optional anomaly monitors scoped by tags or service types.
- [Snowflake Fail-safe](../technologies/snowflake/snowflake-fail-safe.md): Keeps a further non-configurable 7 days of historical data for permanent tables after Time Travel ends, recoverable only by Snowflake Support after a disaster.
- [Snowflake organisations](../technologies/snowflake/snowflake-organizations.md): Group multiple Snowflake accounts across regions and clouds under one organisation for account creation, organisation-wide usage views, organisation users and organisational listings.
- [Snowflake Query History, Query Profile and query insights](../technologies/snowflake/snowflake-query-profile.md): Snowsight views of query history, operator-level execution plans and automatic insights, used to diagnose slow or expensive queries.
- [Snowflake replication and failover groups](../technologies/snowflake/snowflake-replication-failover.md): Replicate databases, users, roles, warehouses, policies and integrations to accounts in other regions or clouds, with promotion on failover and client redirect through connection objects.
- [Snowflake resource monitors](../technologies/snowflake/snowflake-resource-monitors.md): Credit quotas on warehouses or the whole account that notify or suspend warehouses when thresholds are reached.
- [Snowflake Terraform provider](../technologies/snowflake/snowflake-terraform-provider.md): A Terraform provider for managing Snowflake accounts, warehouses, databases, roles, grants and policies as code.
- [Snowflake Trail (event tables, logging, tracing and metrics)](../technologies/snowflake/snowflake-trail.md): Collects logs, OpenTelemetry-style traces and metrics from UDFs, procedures, Snowpark, Native Apps, container services and pipelines into event tables, with Snowsight dashboards.
- [Virtual Private Snowflake (VPS)](../technologies/snowflake/snowflake-virtual-private-snowflake.md): The highest Snowflake edition, which runs a dedicated, isolated Snowflake deployment for a single customer, with its own metadata store and compute.

## Specialised data types

- [Observe by Snowflake](../technologies/snowflake/snowflake-observe.md): An observability platform for logs, metrics and traces, built on a Snowflake lakehouse and available standalone or paid for with Snowflake credits.
- [Snowflake geospatial data types and functions](../technologies/snowflake/snowflake-geospatial.md): GEOGRAPHY and GEOMETRY types with spatial functions, H3 indexing and spatial joins in SQL.
- [Snowflake time-series functions (ASOF JOIN, TIME_SLICE, RESAMPLE)](../technologies/snowflake/snowflake-time-series-functions.md): SQL constructs for aligning, bucketing and joining time-stamped data, including ASOF JOIN and gap filling.

