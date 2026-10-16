---
type: Platform
id: platform-google-cloud
title: Google Cloud
description: Google's cloud, centred on BigQuery for analytics and its agent platform for AI.
vendor: Google
resource: https://cloud.google.com/
folder: google-cloud
order: 3
terminology:
  access-requests: data product access groups and governance workflows
  active-metadata: Knowledge Catalog metadata change feeds
  agent-tool-access: Google Cloud remote MCP servers
  ai-agents: Agent Development Kit and Agent Runtime (formerly Agent Engine)
  ai-functions: BigQuery generative AI functions (AI.GENERATE and related)
  ai-gateway: Agent Gateway
  ai-guardrails: Model Armor
  attribute-based-access: policy tags; IAM Conditions; data governance tags
  change-data-capture: Datastream; BigQuery CDC upserts
  change-feeds: Spanner and Bigtable change streams; BigQuery CHANGES function
  column-masking: data masking with data policies
  conversational-analytics: Conversational Analytics and data agents
  cross-region-failover: BigQuery managed disaster recovery
  customer-managed-keys: CMEK with Cloud KMS
  dashboards-reports: Looker; Data Studio (formerly Looker Studio)
  data-catalogue: Knowledge Catalog (formerly Dataplex Universal Catalog)
  data-clean-rooms: BigQuery data clean rooms
  data-contracts: data product contract
  data-loss-prevention: VPC Service Controls perimeters
  data-marketplace: BigQuery sharing with Google Cloud Marketplace
  data-products: Knowledge Catalog data products
  data-security-posture: Sensitive Data Protection discovery; Security Command Center
  deidentification: Sensitive Data Protection de-identification
  distributed-processing: Managed Service for Apache Spark (formerly Dataproc)
  engine-interoperability: Lakehouse Iceberg REST catalog
  event-streaming: Pub/Sub
  external-data-sharing: BigQuery sharing (formerly Analytics Hub) exchanges and listings
  feature-store: Agent Platform Feature Store
  foundation-model-access: Gemini Enterprise Agent Platform (formerly Vertex AI); Model Garden
  genai-evaluation: Gen AI evals
  in-database-ml: BigQuery ML
  metadata-harvesting: Knowledge Catalog automatic discovery and metadata import
  multi-tenancy: resource hierarchy (organisation, folders, projects)
  open-table-formats: BigQuery tables for Apache Iceberg / Iceberg managed tables
  privacy-enhancing-technologies: analysis rules (aggregation threshold, differential privacy, list overlap)
  provisioned-compute: BigQuery editions reservations (slots)
  retrieval-augmented-generation: RAG Engine; Agent Search (formerly Vertex AI Search)
  semantic-layer: LookML
  serverless-compute: BigQuery on-demand pricing
  spreadsheet-integration: Connected Sheets
  storage-tiering: storage classes, Object Lifecycle Management and Autoclass
  stream-processing: Dataflow (Apache Beam)
  streaming-ingestion: Pub/Sub BigQuery subscriptions; Storage Write API
  streaming-sql: BigQuery continuous queries
  system-telemetry: INFORMATION_SCHEMA views
  table-catalogue: Lakehouse runtime catalog (formerly BigLake metastore)
  transformation-as-code: Dataform (SQLX)
  workflow-orchestration: Managed Service for Apache Airflow (formerly Cloud Composer); BigQuery pipelines
  workload-isolation: reservation assignments
  workload-management: BigQuery workload management (formerly capacity management)
  zero-copy-cloning: table clones
families:
- name: BigQuery
  aliases: [Google BigQuery]
  technologies:
  - gcp-bigquery
  - gcp-bigquery-ai-functions
  - gcp-bigquery-bi-engine
  - gcp-bigquery-cdc
  - gcp-bigquery-change-history
  - gcp-bigquery-continuous-queries
  - gcp-bigquery-conversational-analytics
  - gcp-bigquery-data-canvas
  - gcp-bigquery-data-clean-rooms
  - gcp-bigquery-data-engineering-agent
  - gcp-bigquery-data-masking
  - gcp-bigquery-data-preparation
  - gcp-bigquery-data-transfer-service
  - gcp-bigquery-dataframes
  - gcp-bigquery-editions
  - gcp-bigquery-export-data
  - gcp-bigquery-external-tables
  - gcp-bigquery-federated-queries
  - gcp-bigquery-geospatial
  - gcp-bigquery-graph
  - gcp-bigquery-iceberg-managed-tables
  - gcp-bigquery-information-schema
  - gcp-bigquery-managed-disaster-recovery
  - gcp-bigquery-managed-storage
  - gcp-bigquery-materialized-views
  - gcp-bigquery-migration-service
  - gcp-bigquery-ml
  - gcp-bigquery-object-tables
  - gcp-bigquery-omni
  - gcp-bigquery-pipelines
  - gcp-bigquery-policy-tags
  - gcp-bigquery-row-level-security
  - gcp-bigquery-search-indexes
  - gcp-bigquery-sharing
  - gcp-bigquery-storage-write-api
  - gcp-bigquery-studio
  - gcp-bigquery-table-clones
  - gcp-bigquery-table-snapshots
  - gcp-bigquery-time-travel
  - gcp-bigquery-udfs
  - gcp-bigquery-vector-search
  - gcp-bigquery-workload-management
  - gcp-gemini-in-bigquery
- name: Knowledge Catalog
  aliases: [Dataplex, Dataplex Universal Catalog]
  technologies:
  - gcp-knowledge-catalog
  - gcp-knowledge-catalog-data-insights
  - gcp-knowledge-catalog-data-lineage
  - gcp-knowledge-catalog-data-products
  - gcp-knowledge-catalog-data-profiling
  - gcp-knowledge-catalog-data-quality
- name: Gemini Enterprise Agent Platform
  aliases: [Vertex AI, Agent Platform]
  technologies:
  - gcp-gemini-enterprise-agent-platform
  - gcp-gemini-models
  - gcp-model-garden
  - gcp-agent-studio
  - gcp-agent-runtime
  - gcp-agent-search
  - gcp-rag-engine
  - gcp-vector-search
  - gcp-gen-ai-evals
  - gcp-agent-gateway
  - gcp-agent-registry
  - gcp-agent-observability
  - gcp-agent-platform-automl
  - gcp-agent-platform-endpoints
  - gcp-agent-platform-experiments
  - gcp-agent-platform-feature-store
  - gcp-agent-platform-managed-training
  - gcp-agent-platform-model-evaluation
  - gcp-agent-platform-model-registry
  - gcp-agent-platform-pipelines
  - gcp-agent-platform-workbench
  - gcp-model-monitoring
  - gcp-data-labeling
  - gcp-colab-enterprise
- name: Google Cloud Lakehouse
  aliases: [BigLake, Lakehouse for Apache Iceberg]
  technologies: [gcp-lakehouse, gcp-lakehouse-runtime-catalog, gcp-bigquery-iceberg-managed-tables]
- name: Managed Service for Apache Spark
  aliases: [Dataproc]
  technologies: [gcp-managed-spark-clusters, gcp-managed-spark-serverless, gcp-dataproc-metastore]
- name: Looker
  technologies: [gcp-looker, gcp-lookml, gcp-looker-conversational-analytics]
- name: Dataflow
  aliases: [Google Cloud Dataflow]
  technologies: [gcp-dataflow, gcp-dataflow-ml, gcp-dataflow-templates]
- name: Google Cloud Observability
  aliases: [Google Cloud operations suite, Stackdriver]
  technologies: [gcp-cloud-logging, gcp-cloud-monitoring]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Google Cloud's data offering centres on BigQuery, a serverless analytical database that also provides BigQuery ML, generative AI functions in SQL, continuous queries, notebooks in BigQuery Studio, data sharing and clean rooms, and conversational data agents. Google Cloud Lakehouse (formerly BigLake) extends BigQuery's security and table management to Apache Iceberg tables in Cloud Storage, and its runtime catalog serves those tables to Spark, Trino, Flink and other Iceberg REST clients. Knowledge Catalog (formerly Dataplex Universal Catalog) provides metadata search, a business glossary, lineage, profiling, data quality and data products across the estate.

Processing and streaming come from Dataflow (Apache Beam), Managed Service for Apache Spark (formerly Dataproc), Pub/Sub, Managed Service for Apache Kafka and Datastream for change data capture, orchestrated by Managed Service for Apache Airflow (formerly Cloud Composer), Dataform and Workflows. Looker, with its LookML semantic model, and Data Studio (formerly Looker Studio) cover BI. Gemini Enterprise Agent Platform (formerly Vertex AI) is the platform for machine learning, generative AI and agents, and Gemini Enterprise is the employee-facing assistant and search product.

# Notes

- Most data and AI products were renamed in April 2026: Vertex AI became Gemini Enterprise Agent Platform (its components became "Agent Platform X", with Vertex AI Agent Engine now Agent Runtime and Vertex AI Search now Agent Search), Dataplex Universal Catalog became Knowledge Catalog, BigLake became Lakehouse, BigLake metastore became the Lakehouse runtime catalog, Cloud Composer became Managed Service for Apache Airflow, Dataproc and Serverless for Apache Spark became Managed Service for Apache Spark, and Looker Studio became Data Studio.
- APIs, IAM roles, gcloud commands and Terraform resources mostly keep the old identifiers (aiplatform, dataplex, biglake, composer, dataproc, and datacatalog for policy tags), so both sets of names appear side by side in real estates.
- Many capabilities are BigQuery features rather than separate services, and some depend on the edition: continuous queries, vector indexes and materialised view creation need Enterprise or higher, BigQuery Omni runs only on Enterprise edition or on-demand pricing, and managed disaster recovery and Assured Workloads controls need Enterprise Plus.
- Google Cloud has no first-party master data management, entity resolution, managed SFTP or AS2 file transfer, or IoT ingestion service (IoT Core was retired in 2023); partners fill these gaps.
- Projects are the unit of isolation, billing and quota for most data services, and VPC Service Controls perimeters are the main control against data exfiltration, so folder, project and perimeter design is the central tenancy decision.
- Google-hosted remote MCP servers cover most data services, including BigQuery, Spanner, AlloyDB, Cloud SQL, Knowledge Catalog and Pub/Sub, and Agent Gateway and Model Armor add policy enforcement and content screening for agent traffic.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 16 of 22 | [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 19 of 23 | [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [Data branching and tagging](../capabilities/storage/data-branching.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 16 of 18 | [Edge data processing](../capabilities/processing/edge-data-processing.md), [Single-node processing](../capabilities/processing/single-node-processing.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 5 of 5 |  |
| [Query and compute](../capabilities/compute/compute.md) | 21 of 22 | [Real-time analytical database](../capabilities/compute/real-time-analytics.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 8 of 13 | [Decision management](../capabilities/serving/decision-management.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 13 of 20 | [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 19 of 20 | [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 13 of 18 | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Edge inference](../capabilities/mlops/edge-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 22 of 23 | [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 17 of 20 | [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Data certification](../capabilities/metadata/data-certification.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 6 of 12 (+2 in preview) | [Data issue management](../capabilities/data-quality/data-issue-management.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md) (preview only), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md) (preview only) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 12 of 24 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Policy management](../capabilities/governance/data-policy-management.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 19 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 7 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 5 of 7 | [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 11 of 16 (+1 in preview) | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md) (preview only) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 23 of 27 | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Customer-hosted data plane](../capabilities/platform-operations/hybrid-data-plane.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 8 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md) |

# Product families

- **BigQuery** (also: Google BigQuery): [BigQuery](../technologies/google-cloud/gcp-bigquery.md), [BigQuery generative AI functions](../technologies/google-cloud/gcp-bigquery-ai-functions.md), [BigQuery BI Engine](../technologies/google-cloud/gcp-bigquery-bi-engine.md), [BigQuery change data capture](../technologies/google-cloud/gcp-bigquery-cdc.md), [BigQuery change history (APPENDS and CHANGES)](../technologies/google-cloud/gcp-bigquery-change-history.md), [BigQuery continuous queries](../technologies/google-cloud/gcp-bigquery-continuous-queries.md), [BigQuery conversational analytics](../technologies/google-cloud/gcp-bigquery-conversational-analytics.md), [BigQuery data canvas](../technologies/google-cloud/gcp-bigquery-data-canvas.md), [BigQuery data clean rooms](../technologies/google-cloud/gcp-bigquery-data-clean-rooms.md), [BigQuery Data Engineering Agent](../technologies/google-cloud/gcp-bigquery-data-engineering-agent.md), [BigQuery data masking](../technologies/google-cloud/gcp-bigquery-data-masking.md), [BigQuery data preparation](../technologies/google-cloud/gcp-bigquery-data-preparation.md) (preview), [BigQuery Data Transfer Service](../technologies/google-cloud/gcp-bigquery-data-transfer-service.md), [BigQuery DataFrames](../technologies/google-cloud/gcp-bigquery-dataframes.md), [BigQuery editions](../technologies/google-cloud/gcp-bigquery-editions.md), [BigQuery EXPORT DATA](../technologies/google-cloud/gcp-bigquery-export-data.md), [BigQuery external tables and load jobs](../technologies/google-cloud/gcp-bigquery-external-tables.md), [BigQuery federated queries](../technologies/google-cloud/gcp-bigquery-federated-queries.md), [BigQuery geospatial analytics](../technologies/google-cloud/gcp-bigquery-geospatial.md), [BigQuery Graph](../technologies/google-cloud/gcp-bigquery-graph.md), [BigQuery tables for Apache Iceberg](../technologies/google-cloud/gcp-bigquery-iceberg-managed-tables.md), [BigQuery INFORMATION_SCHEMA views](../technologies/google-cloud/gcp-bigquery-information-schema.md), [BigQuery managed disaster recovery](../technologies/google-cloud/gcp-bigquery-managed-disaster-recovery.md), [BigQuery managed storage](../technologies/google-cloud/gcp-bigquery-managed-storage.md), [BigQuery materialized views](../technologies/google-cloud/gcp-bigquery-materialized-views.md), [BigQuery Migration Service](../technologies/google-cloud/gcp-bigquery-migration-service.md), [BigQuery ML](../technologies/google-cloud/gcp-bigquery-ml.md), [BigQuery object tables and ObjectRef](../technologies/google-cloud/gcp-bigquery-object-tables.md), [BigQuery Omni](../technologies/google-cloud/gcp-bigquery-omni.md), [BigQuery pipelines](../technologies/google-cloud/gcp-bigquery-pipelines.md), [BigQuery policy tags](../technologies/google-cloud/gcp-bigquery-policy-tags.md), [BigQuery row-level security](../technologies/google-cloud/gcp-bigquery-row-level-security.md), [BigQuery search indexes](../technologies/google-cloud/gcp-bigquery-search-indexes.md), [BigQuery sharing](../technologies/google-cloud/gcp-bigquery-sharing.md), [BigQuery Storage Write API](../technologies/google-cloud/gcp-bigquery-storage-write-api.md), [BigQuery Studio](../technologies/google-cloud/gcp-bigquery-studio.md), [BigQuery table clones](../technologies/google-cloud/gcp-bigquery-table-clones.md), [BigQuery table snapshots](../technologies/google-cloud/gcp-bigquery-table-snapshots.md), [BigQuery time travel](../technologies/google-cloud/gcp-bigquery-time-travel.md), [BigQuery user-defined functions](../technologies/google-cloud/gcp-bigquery-udfs.md), [BigQuery vector search](../technologies/google-cloud/gcp-bigquery-vector-search.md), [BigQuery workload management](../technologies/google-cloud/gcp-bigquery-workload-management.md), [Gemini in BigQuery](../technologies/google-cloud/gcp-gemini-in-bigquery.md)
- **Knowledge Catalog** (also: Dataplex, Dataplex Universal Catalog): [Knowledge Catalog](../technologies/google-cloud/gcp-knowledge-catalog.md), [Knowledge Catalog data insights](../technologies/google-cloud/gcp-knowledge-catalog-data-insights.md), [Knowledge Catalog data lineage](../technologies/google-cloud/gcp-knowledge-catalog-data-lineage.md), [Knowledge Catalog data products](../technologies/google-cloud/gcp-knowledge-catalog-data-products.md), [Knowledge Catalog data profiling](../technologies/google-cloud/gcp-knowledge-catalog-data-profiling.md), [Knowledge Catalog data quality](../technologies/google-cloud/gcp-knowledge-catalog-data-quality.md)
- **Gemini Enterprise Agent Platform** (also: Vertex AI, Agent Platform): [Gemini Enterprise Agent Platform](../technologies/google-cloud/gcp-gemini-enterprise-agent-platform.md), [Gemini models on Agent Platform](../technologies/google-cloud/gcp-gemini-models.md), [Model Garden](../technologies/google-cloud/gcp-model-garden.md), [Google Cloud Agent Studio](../technologies/google-cloud/gcp-agent-studio.md), [Google Cloud Agent Runtime](../technologies/google-cloud/gcp-agent-runtime.md), [Google Cloud Agent Search](../technologies/google-cloud/gcp-agent-search.md), [Agent Platform RAG Engine](../technologies/google-cloud/gcp-rag-engine.md), [Agent Platform Vector Search](../technologies/google-cloud/gcp-vector-search.md), [Gen AI evals on Agent Platform](../technologies/google-cloud/gcp-gen-ai-evals.md), [Google Cloud Agent Gateway](../technologies/google-cloud/gcp-agent-gateway.md), [Google Cloud Agent Registry](../technologies/google-cloud/gcp-agent-registry.md), [Google Cloud Agent Observability](../technologies/google-cloud/gcp-agent-observability.md), [Agent Platform AutoML](../technologies/google-cloud/gcp-agent-platform-automl.md), [Agent Platform Endpoints](../technologies/google-cloud/gcp-agent-platform-endpoints.md), [Experiments on Agent Platform](../technologies/google-cloud/gcp-agent-platform-experiments.md), [Agent Platform Feature Store](../technologies/google-cloud/gcp-agent-platform-feature-store.md), [Agent Platform Managed Training](../technologies/google-cloud/gcp-agent-platform-managed-training.md), [Agent Platform Model Evaluation](../technologies/google-cloud/gcp-agent-platform-model-evaluation.md), [Agent Platform Model Registry](../technologies/google-cloud/gcp-agent-platform-model-registry.md), [Agent Platform Pipelines](../technologies/google-cloud/gcp-agent-platform-pipelines.md), [Agent Platform Workbench](../technologies/google-cloud/gcp-agent-platform-workbench.md), [Model Monitoring on Agent Platform](../technologies/google-cloud/gcp-model-monitoring.md), [Data Labeling on Agent Platform](../technologies/google-cloud/gcp-data-labeling.md), [Colab Enterprise](../technologies/google-cloud/gcp-colab-enterprise.md)
- **Google Cloud Lakehouse** (also: BigLake, Lakehouse for Apache Iceberg): [Google Cloud Lakehouse](../technologies/google-cloud/gcp-lakehouse.md), [Google Cloud Lakehouse runtime catalog](../technologies/google-cloud/gcp-lakehouse-runtime-catalog.md), [BigQuery tables for Apache Iceberg](../technologies/google-cloud/gcp-bigquery-iceberg-managed-tables.md)
- **Managed Service for Apache Spark** (also: Dataproc): [Google Cloud Managed Service for Apache Spark on clusters](../technologies/google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Managed Service for Apache Spark serverless](../technologies/google-cloud/gcp-managed-spark-serverless.md), [Dataproc Metastore](../technologies/google-cloud/gcp-dataproc-metastore.md)
- **Looker**: [Looker](../technologies/google-cloud/gcp-looker.md), [LookML](../technologies/google-cloud/gcp-lookml.md), [Conversational Analytics in Looker](../technologies/google-cloud/gcp-looker-conversational-analytics.md)
- **Dataflow** (also: Google Cloud Dataflow): [Google Cloud Dataflow](../technologies/google-cloud/gcp-dataflow.md), [Dataflow ML](../technologies/google-cloud/gcp-dataflow-ml.md), [Dataflow templates](../technologies/google-cloud/gcp-dataflow-templates.md)
- **Google Cloud Observability** (also: Google Cloud operations suite, Stackdriver): [Google Cloud Logging](../technologies/google-cloud/gcp-cloud-logging.md), [Google Cloud Monitoring](../technologies/google-cloud/gcp-cloud-monitoring.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| Agent Development Kit and Agent Runtime (formerly Agent Engine) | [AI agents](../capabilities/generative-ai/ai-agents.md) |
| Agent Gateway | [AI gateway](../capabilities/generative-ai/ai-gateway.md) |
| Agent Platform Feature Store | [Feature store](../capabilities/machine-learning/feature-store.md) |
| analysis rules (aggregation threshold, differential privacy, list overlap) | [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md) |
| BigQuery continuous queries | [Streaming SQL](../capabilities/processing/streaming-sql.md) |
| BigQuery data clean rooms | [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md) |
| BigQuery editions reservations (slots) | [Provisioned compute](../capabilities/compute/provisioned-compute.md) |
| BigQuery generative AI functions (AI.GENERATE and related) | [AI functions in SQL](../capabilities/processing/ai-functions.md) |
| BigQuery managed disaster recovery | [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md) |
| BigQuery ML | [In-database machine learning](../capabilities/machine-learning/in-database-ml.md) |
| BigQuery on-demand pricing | [Serverless compute](../capabilities/compute/serverless-compute.md) |
| BigQuery sharing (formerly Analytics Hub) exchanges and listings | [External data sharing](../capabilities/data-sharing/external-data-sharing.md) |
| BigQuery sharing with Google Cloud Marketplace | [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| BigQuery tables for Apache Iceberg / Iceberg managed tables | [Open table formats](../capabilities/storage/open-table-formats.md) |
| BigQuery workload management (formerly capacity management) | [Workload management](../capabilities/compute/workload-management.md) |
| CMEK with Cloud KMS | [Customer-managed keys](../capabilities/security/customer-managed-keys.md) |
| Connected Sheets | [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md) |
| Conversational Analytics and data agents | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| data masking with data policies | [Column security and dynamic masking](../capabilities/security/column-masking.md) |
| data product access groups and governance workflows | [Access requests and reviews](../capabilities/security/access-requests.md) |
| data product contract | [Data contracts](../capabilities/data-products/data-contracts.md) |
| Dataflow (Apache Beam) | [Stream processing](../capabilities/processing/stream-processing.md) |
| Dataform (SQLX) | [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| Datastream; BigQuery CDC upserts | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) |
| Gemini Enterprise Agent Platform (formerly Vertex AI); Model Garden | [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |
| Gen AI evals | [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) |
| Google Cloud remote MCP servers | [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) |
| INFORMATION_SCHEMA views | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) |
| Knowledge Catalog (formerly Dataplex Universal Catalog) | [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| Knowledge Catalog automatic discovery and metadata import | [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md) |
| Knowledge Catalog data products | [Data products](../capabilities/data-products/data-products.md) |
| Knowledge Catalog metadata change feeds | [Active metadata](../capabilities/metadata/active-metadata.md) |
| Lakehouse Iceberg REST catalog | [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md) |
| Lakehouse runtime catalog (formerly BigLake metastore) | [Table catalogue](../capabilities/storage/table-catalogue.md) |
| Looker; Data Studio (formerly Looker Studio) | [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md) |
| LookML | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) |
| Managed Service for Apache Airflow (formerly Cloud Composer); BigQuery pipelines | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| Managed Service for Apache Spark (formerly Dataproc) | [Distributed processing](../capabilities/processing/distributed-processing.md) |
| Model Armor | [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| policy tags; IAM Conditions; data governance tags | [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md) |
| Pub/Sub | [Event streaming](../capabilities/ingestion-integration/event-streaming.md) |
| Pub/Sub BigQuery subscriptions; Storage Write API | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |
| RAG Engine; Agent Search (formerly Vertex AI Search) | [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) |
| reservation assignments | [Workload isolation](../capabilities/compute/workload-isolation.md) |
| resource hierarchy (organisation, folders, projects) | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| Sensitive Data Protection de-identification | [De-identification](../capabilities/governance/deidentification.md) |
| Sensitive Data Protection discovery; Security Command Center | [Data security posture management](../capabilities/security/data-security-posture.md) |
| Spanner and Bigtable change streams; BigQuery CHANGES function | [Change feeds](../capabilities/serving/change-feeds.md) |
| storage classes, Object Lifecycle Management and Autoclass | [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) |
| table clones | [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| VPC Service Controls perimeters | [Data loss prevention](../capabilities/security/data-loss-prevention.md) |

# Technologies

## Ingestion and integration

- [BigQuery change data capture](../technologies/google-cloud/gcp-bigquery-cdc.md): Applies streamed upserts and deletes, keyed on a declared primary key, to BigQuery tables in the background with a configurable staleness bound.
- [BigQuery Data Transfer Service](../technologies/google-cloud/gcp-bigquery-data-transfer-service.md): Scheduled, managed loads into BigQuery from Google marketing products, SaaS applications, other warehouses, databases and cloud object stores.
- [BigQuery Storage Write API](../technologies/google-cloud/gcp-bigquery-storage-write-api.md): High-throughput API for streaming or batch-committing rows into BigQuery tables with exactly-once semantics, readable within seconds.
- [Datastream](../technologies/google-cloud/gcp-datastream.md): Serverless change data capture and replication from MySQL, PostgreSQL, Oracle, SQL Server, Spanner, MongoDB and Salesforce into BigQuery, Lakehouse Iceberg tables or Cloud Storage.
- [Google Cloud Application Integration](../technologies/google-cloud/gcp-application-integration.md): Integration-platform-as-a-service for building API, event and process integrations visually, using Integration Connectors to reach SaaS and on-premises systems.
- [Google Cloud Database Migration Service](../technologies/google-cloud/gcp-database-migration-service.md): Migrates MySQL, PostgreSQL, SQL Server and Oracle databases to Cloud SQL and AlloyDB using an initial copy followed by continuous replication.
- [Google Cloud Managed Service for Apache Kafka](../technologies/google-cloud/gcp-managed-kafka.md): Runs Apache Kafka clusters, managed Kafka Connect clusters and a schema registry on Google Cloud, with Google handling brokers, scaling and patching.
- [Google Cloud Pub/Sub](../technologies/google-cloud/gcp-pubsub.md): Global publish-subscribe messaging service with push, pull and export subscriptions that write directly to BigQuery, Cloud Storage and Bigtable.
- [Google Cloud Storage Transfer Service](../technologies/google-cloud/gcp-storage-transfer-service.md): Managed, scheduled or event-driven copying of large object and file datasets from other clouds, HTTP sources and on-premises file systems into Cloud Storage.
- [Google Cloud Transfer Appliance](../technologies/google-cloud/gcp-transfer-appliance.md): Rentable, encrypted storage device shipped to a customer site to move hundreds of terabytes to petabytes into Cloud Storage offline.

## Storage and table management

- [BigQuery external tables and load jobs](../technologies/google-cloud/gcp-bigquery-external-tables.md): Reads or loads Parquet, ORC, Avro, JSON and CSV files from Cloud Storage, including Hive-partitioned layouts, as queryable external tables or native tables.
- [BigQuery managed storage](../technologies/google-cloud/gcp-bigquery-managed-storage.md): Internal columnar storage for native BigQuery tables, with automatic compression, replication, partitioning, clustering and transactional writes.
- [BigQuery table clones](../technologies/google-cloud/gcp-bigquery-table-clones.md): Writable copies of a table that share storage with the base table and are billed only for data that later changes in either.
- [BigQuery tables for Apache Iceberg](../technologies/google-cloud/gcp-bigquery-iceberg-managed-tables.md): BigQuery-managed tables stored as Apache Iceberg files in your Cloud Storage bucket, with BigQuery handling writes, clustering, compaction and garbage collection.
- [BigQuery time travel](../technologies/google-cloud/gcp-bigquery-time-travel.md): Lets you query or restore a table as it was at any point within a configurable window of two to seven days, backed by a further fail-safe period.
- [Dataproc Metastore](../technologies/google-cloud/gcp-dataproc-metastore.md): Fully managed Apache Hive metastore for Spark, Hive and Trino workloads on Google Cloud.
- [Google Cloud Lakehouse runtime catalog](../technologies/google-cloud/gcp-lakehouse-runtime-catalog.md): Serverless metastore that holds Iceberg table metadata for BigQuery and open-source engines and serves it through Apache Iceberg REST catalog and Hive endpoints with credential vending.
- [Google Cloud Storage](../technologies/google-cloud/gcp-cloud-storage.md): Object storage with regional, dual-region and multi-region buckets and Standard, Nearline, Coldline and Archive storage classes.
- [Google Cloud Storage Autoclass](../technologies/google-cloud/gcp-cloud-storage-autoclass.md): Moves each object between storage classes automatically according to how recently it was accessed, without retrieval or early-deletion fees.

## Processing and transformation

- [BigQuery continuous queries](../technologies/google-cloud/gcp-bigquery-continuous-queries.md): Long-running SQL statements that process rows as they arrive in a table and write results to BigQuery or Iceberg tables, Pub/Sub, Bigtable or Spanner.
- [BigQuery data preparation](../technologies/google-cloud/gcp-bigquery-data-preparation.md) (preview): Visual, Gemini-assisted editor for cleaning, joining and reshaping BigQuery data that saves its steps as runnable SQLX.
- [BigQuery DataFrames](../technologies/google-cloud/gcp-bigquery-dataframes.md): Python library (bigframes) offering pandas- and scikit-learn-style APIs that compile to BigQuery SQL so data stays in BigQuery.
- [BigQuery generative AI functions](../technologies/google-cloud/gcp-bigquery-ai-functions.md): SQL functions such as AI.GENERATE, AI.GENERATE_TABLE, AI.IF, AI.CLASSIFY, AI.SCORE, AI.AGG and AI.EMBED that call Gemini and partner models over table rows and unstructured objects.
- [BigQuery user-defined functions](../technologies/google-cloud/gcp-bigquery-udfs.md): Extends GoogleSQL with SQL, JavaScript and Python UDFs, remote functions on Cloud Run, stored procedures and stored procedures for Apache Spark.
- [Cloud Data Fusion](../technologies/google-cloud/gcp-data-fusion.md): Visual, plugin-based integration service built on open-source CDAP for designing batch and real-time pipelines that run on Managed Service for Apache Spark.
- [Dataflow templates](../technologies/google-cloud/gcp-dataflow-templates.md): Google-provided and custom Flex templates, plus the visual job builder, for running common ingestion and transformation pipelines without writing Beam code.
- [Dataform](../technologies/google-cloud/gcp-dataform.md): Develops, tests, version-controls and runs SQL transformation workflows in BigQuery, defined in SQLX with dependencies resolved automatically.
- [Google Cloud Dataflow](../technologies/google-cloud/gcp-dataflow.md): Serverless runner for Apache Beam batch and streaming pipelines with autoscaling, exactly-once processing and event-time windowing.
- [Google Cloud Document AI](../technologies/google-cloud/gcp-document-ai.md): Document processing service with OCR, form, layout and custom extraction and classification processors for PDFs and images.
- [Google Cloud Managed Service for Apache Spark on clusters](../technologies/google-cloud/gcp-managed-spark-clusters.md): Provisions and manages Spark, Hadoop, Hive, Flink and Trino clusters on Compute Engine that you size, configure and can access directly.
- [Google Cloud Managed Service for Apache Spark serverless](../technologies/google-cloud/gcp-managed-spark-serverless.md): Runs Spark batch jobs and interactive sessions without clusters, billed for execution time only.

## Orchestration

- [BigQuery pipelines](../technologies/google-cloud/gcp-bigquery-pipelines.md): Console-built, Dataform-backed pipelines that run SQL, notebook, data preparation and SQLX tasks in dependency order on a schedule.
- [Eventarc](../technologies/google-cloud/gcp-eventarc.md): Routes events from Google Cloud services, audit logs, Cloud Storage and Pub/Sub to Cloud Run, Workflows and other targets.
- [Google Cloud Managed Service for Apache Airflow](../technologies/google-cloud/gcp-managed-airflow.md): Managed Apache Airflow environments for scheduling and monitoring DAGs of data and ML tasks across Google Cloud and external systems.
- [Google Cloud Workflows](../technologies/google-cloud/gcp-workflows.md): Serverless orchestrator that runs YAML- or JSON-defined sequences of HTTP and Google Cloud API calls with retries, branching and waiting.

## Query and compute

- [BigQuery](../technologies/google-cloud/gcp-bigquery.md): Serverless analytical database that runs GoogleSQL over managed and open-format tables with storage and compute billed and scaled separately.
- [BigQuery BI Engine](../technologies/google-cloud/gcp-bigquery-bi-engine.md): In-memory cache in front of BigQuery that speeds up dashboard-style SQL queries, sized as a regional memory reservation.
- [BigQuery editions](../technologies/google-cloud/gcp-bigquery-editions.md): Slot-based capacity model in Standard, Enterprise and Enterprise Plus tiers, with autoscaling reservations, optional baseline slots and one- or three-year commitments.
- [BigQuery federated queries](../technologies/google-cloud/gcp-bigquery-federated-queries.md): Sends queries from BigQuery to Cloud SQL, AlloyDB, Spanner and SAP Datasphere through connections and joins the results with BigQuery data.
- [BigQuery materialized views](../technologies/google-cloud/gcp-bigquery-materialized-views.md): Precomputed query results that BigQuery refreshes incrementally and uses to rewrite matching queries automatically.
- [BigQuery Omni](../technologies/google-cloud/gcp-bigquery-omni.md): Runs BigQuery queries on data held in Amazon S3 or Azure Blob Storage, using BigQuery-managed compute in the corresponding AWS or Azure region.
- [BigQuery search indexes](../technologies/google-cloud/gcp-bigquery-search-indexes.md): Indexes text and JSON columns so the SEARCH function and equality or LIKE filters can find matching rows without full scans.
- [BigQuery workload management](../technologies/google-cloud/gcp-bigquery-workload-management.md): Reservations, assignments, idle-slot sharing, target concurrency, query queues and reservation groups that divide slot capacity between projects and workload types.
- [Cloud Run](../technologies/google-cloud/gcp-cloud-run.md): Serverless platform for running containers, functions and jobs that scale to zero, often used for data APIs, remote functions and data applications.
- [Cloud TPU](../technologies/google-cloud/gcp-cloud-tpu.md): Google's tensor processing unit accelerators, offered as VMs, slices and pods for training and serving large models.
- [Google Cloud Lakehouse](../technologies/google-cloud/gcp-lakehouse.md): Google Cloud's open lakehouse layer for Apache Iceberg and other formats on object storage, combining a shared catalogue, automatic table management and fine-grained security for BigQuery, Spark, Trino and Flink.

## Serving and activation

- [AlloyDB for PostgreSQL](../technologies/google-cloud/gcp-alloydb.md): PostgreSQL-compatible database with a disaggregated storage layer, columnar engine for analytical queries and built-in vector search and AI functions.
- [Apigee](../technologies/google-cloud/gcp-apigee.md): API management platform for publishing, securing, rate-limiting and monitoring APIs, including APIs that expose data products and LLM endpoints.
- [BigQuery change history (APPENDS and CHANGES)](../technologies/google-cloud/gcp-bigquery-change-history.md): Table-valued functions that return rows appended to, or changed in, a table over a time range so downstream jobs can process only the delta.
- [BigQuery EXPORT DATA](../technologies/google-cloud/gcp-bigquery-export-data.md): SQL statement that writes query results to Cloud Storage files or directly into Bigtable, Spanner, Pub/Sub and AlloyDB.
- [Bigtable](../technologies/google-cloud/gcp-bigtable.md): Wide-column NoSQL database for very high-throughput, low-latency reads and writes, often used for time series, events and feature serving.
- [Cloud SQL](../technologies/google-cloud/gcp-cloud-sql.md): Managed MySQL, PostgreSQL and SQL Server databases with automated backups, high availability and read replicas.
- [Firestore](../technologies/google-cloud/gcp-firestore.md): Serverless document database for web, mobile and server applications, with real-time listeners, vector search and an edition compatible with the MongoDB API.
- [Memorystore](../technologies/google-cloud/gcp-memorystore.md): Managed in-memory data stores (Memorystore for Valkey, Redis Cluster and Redis) for caching and sub-millisecond lookups.
- [Spanner](../technologies/google-cloud/gcp-spanner.md): Globally distributed relational database with strong consistency, horizontal scaling and up to 99.999% availability, plus graph, full-text and vector search.

## Analytics and BI

- [BigQuery conversational analytics](../technologies/google-cloud/gcp-bigquery-conversational-analytics.md): Natural-language question answering over BigQuery tables, views, graphs and Lakehouse tables through configurable data agents with instructions, glossary terms and verified queries.
- [BigQuery data canvas](../technologies/google-cloud/gcp-bigquery-data-canvas.md): Visual canvas in BigQuery where users chain search, SQL, chart and insight nodes, driven by natural-language prompts to Gemini.
- [BigQuery Studio](../technologies/google-cloud/gcp-bigquery-studio.md): Workspace in the BigQuery console that combines the SQL editor, Colab Enterprise notebooks, Spark sessions, data canvas and saved assets.
- [Connected Sheets](../technologies/google-cloud/gcp-connected-sheets.md): Lets Google Sheets users analyse BigQuery and Looker data with pivots, formulas and charts that run in the source rather than in the sheet.
- [Conversational Analytics in Looker](../technologies/google-cloud/gcp-looker-conversational-analytics.md): Gemini-based agents that answer natural-language questions over LookML Explores and dashboards, grounded in the semantic model.
- [Google Data Studio](../technologies/google-cloud/gcp-data-studio.md): Self-service reporting and dashboard tool with hundreds of connectors, free for individuals and sold as Data Studio Pro for organisations.
- [Looker](../technologies/google-cloud/gcp-looker.md): Enterprise BI platform with a governed semantic model, dashboards, scheduled delivery, alerts and embedding, querying the database directly.
- [LookML](../technologies/google-cloud/gcp-lookml.md): Looker's Git-backed modelling language for defining dimensions, measures, joins and access rules once for all queries.

## Machine learning development

- [Agent Platform AutoML](../technologies/google-cloud/gcp-agent-platform-automl.md): Trains tabular, image and video models from labelled data with automatic feature engineering, architecture search and tuning.
- [Agent Platform Feature Store](../technologies/google-cloud/gcp-agent-platform-feature-store.md): Feature management that uses BigQuery tables as the offline store and syncs selected features to online stores for low-latency serving.
- [Agent Platform Managed Training](../technologies/google-cloud/gcp-agent-platform-managed-training.md): Runs custom training jobs in prebuilt or custom containers on CPUs, GPUs or TPUs, including multi-node distributed training and hyperparameter tuning.
- [Agent Platform Model Evaluation](../technologies/google-cloud/gcp-agent-platform-model-evaluation.md): Computes evaluation metrics for registered models on test data, including data and model bias metrics, and, with Explainable AI, gives feature attributions for predictions.
- [Agent Platform Model Registry](../technologies/google-cloud/gcp-agent-platform-model-registry.md): Central registry for versioning custom, AutoML and BigQuery ML models, with aliases and deployment to endpoints or batch jobs.
- [Agent Platform Pipelines](../technologies/google-cloud/gcp-agent-platform-pipelines.md): Serverless execution of Kubeflow Pipelines and TFX workflows, with each run's artefacts and parameters recorded in ML Metadata.
- [BigQuery ML](../technologies/google-cloud/gcp-bigquery-ml.md): Creates, trains, evaluates and runs machine learning models with SQL inside BigQuery, including imported and remote models.
- [Data Labeling on Agent Platform](../technologies/google-cloud/gcp-data-labeling.md): Manages labelling of image, video, text and tabular datasets by human labellers for supervised training on Agent Platform.
- [Experiments on Agent Platform](../technologies/google-cloud/gcp-agent-platform-experiments.md): Tracks parameters, metrics and artefacts of training runs and pipeline runs so they can be compared, with a managed TensorBoard for visualisation.

## ML operations

- [Agent Platform Endpoints](../technologies/google-cloud/gcp-agent-platform-endpoints.md): Managed online prediction endpoints, plus batch prediction jobs, for serving registered models with autoscaling, GPUs and traffic splitting between model versions.
- [Dataflow ML](../technologies/google-cloud/gcp-dataflow-ml.md): Beam transforms such as RunInference and MLTransform that run model inference and feature preprocessing, including embeddings, inside batch and streaming Dataflow pipelines.
- [Model Monitoring on Agent Platform](../technologies/google-cloud/gcp-model-monitoring.md): Scheduled or on-demand monitoring jobs that compare production inputs and predictions with training data to detect drift and skew.

## Generative AI

- [Agent Platform RAG Engine](../technologies/google-cloud/gcp-rag-engine.md): Managed retrieval-augmented generation service that ingests, chunks and embeds documents into a corpus and retrieves context for Gemini calls.
- [Agent Platform Vector Search](../technologies/google-cloud/gcp-vector-search.md): Managed approximate nearest-neighbour index service based on ScaNN for low-latency similarity search over billions of vectors.
- [BigQuery vector search](../technologies/google-cloud/gcp-bigquery-vector-search.md): Stores embeddings in BigQuery tables and finds nearest neighbours with VECTOR_SEARCH and AI.SEARCH, optionally using IVF or TreeAH vector indexes.
- [Gemini Enterprise](../technologies/google-cloud/gcp-gemini-enterprise.md): Employee-facing agent platform that combines enterprise search over connected applications, prebuilt and custom agents and Gemini chat under company permissions.
- [Gemini Enterprise Agent Platform](../technologies/google-cloud/gcp-gemini-enterprise-agent-platform.md): Google Cloud's platform, formerly Vertex AI, for building, deploying and governing ML models, generative AI applications and agents.
- [Gemini models on Agent Platform](../technologies/google-cloud/gcp-gemini-models.md): Hosted access to Google's Gemini multimodal, embedding, image and speech models through Agent Platform APIs with pay-as-you-go, priority or provisioned throughput.
- [Gen AI evals on Agent Platform](../technologies/google-cloud/gcp-gen-ai-evals.md): Evaluates model and agent outputs with computed metrics, model-based judges and rubrics, offline, against simulated users or as online monitoring.
- [Google Agent Development Kit](../technologies/google-cloud/gcp-agent-development-kit.md): Open-source framework for writing single- and multi-agent applications with tools, memory and evaluation, deployable to Agent Runtime, Cloud Run or GKE.
- [Google Cloud Agent Gateway](../technologies/google-cloud/gcp-agent-gateway.md): Gateway that sits between agents, models and tools to enforce identity, policy, content screening and network controls on agent traffic.
- [Google Cloud Agent Observability](../technologies/google-cloud/gcp-agent-observability.md): Traces, logs, metrics and topology views of agent runs, tool calls and model calls on Agent Platform, built on Cloud Observability.
- [Google Cloud Agent Registry](../technologies/google-cloud/gcp-agent-registry.md): Inventory of the agents, tools and MCP servers in an organisation, used to register, discover and govern them.
- [Google Cloud Agent Runtime](../technologies/google-cloud/gcp-agent-runtime.md): Managed runtime for deploying and scaling agents built with ADK or other frameworks, with managed sessions and long-term memory.
- [Google Cloud Agent Search](../technologies/google-cloud/gcp-agent-search.md): Managed enterprise search and retrieval over websites, documents, structured data and connected applications, used to ground agents and chat applications.
- [Google Cloud Agent Studio](../technologies/google-cloud/gcp-agent-studio.md): Console workspace for designing and testing prompts and agents, comparing models and tuning Gemini models.
- [Google Cloud remote MCP servers](../technologies/google-cloud/gcp-remote-mcp-servers.md): Google-hosted Model Context Protocol endpoints that let AI agents query and manage BigQuery, Spanner, AlloyDB, Cloud SQL, Bigtable, Firestore, Knowledge Catalog, Dataform, Pub/Sub and other services under IAM.
- [MCP Toolbox for Databases](../technologies/google-cloud/gcp-mcp-toolbox-for-databases.md): Open-source MCP server for building parameterised, governed database tools for agents over BigQuery, AlloyDB, Spanner, Cloud SQL and third-party databases.
- [Model Armor](../technologies/google-cloud/gcp-model-armor.md): Screens prompts and responses for prompt injection, jailbreaks, harmful content, malicious URLs and sensitive data, for any model or agent.
- [Model Garden](../technologies/google-cloud/gcp-model-garden.md): Catalogue of Google, partner and open models that can be called as managed APIs or deployed to your own endpoints.

## Metadata and discovery

- [Google Cloud Data Catalog](../technologies/google-cloud/gcp-data-catalog.md) (deprecated): Google Cloud's earlier metadata catalogue for search and tagging of BigQuery, Pub/Sub and Cloud Storage assets.
- [Knowledge Catalog](../technologies/google-cloud/gcp-knowledge-catalog.md): Google Cloud's metadata catalogue for data and AI assets, providing automatic metadata ingestion, keyword and semantic search, aspects, a business glossary and metadata APIs.
- [Knowledge Catalog data insights](../technologies/google-cloud/gcp-knowledge-catalog-data-insights.md): Uses Gemini to draft table and column descriptions, suggested questions and SQL queries from metadata and profiles.
- [Knowledge Catalog data lineage](../technologies/google-cloud/gcp-knowledge-catalog-data-lineage.md): Records table- and column-level lineage automatically for BigQuery, Managed Service for Apache Spark, Managed Airflow and Dataflow, and accepts OpenLineage events from other systems.

## Data quality and observability

- [Knowledge Catalog data profiling](../technologies/google-cloud/gcp-knowledge-catalog-data-profiling.md): Profile scans that compute column statistics, distributions, null rates and top values for BigQuery tables.
- [Knowledge Catalog data quality](../technologies/google-cloud/gcp-knowledge-catalog-data-quality.md): Runs declarative or recommended data quality rules against BigQuery and Lakehouse tables as scheduled scans and publishes results and scores.

## Governance and compliance

- [Assured Workloads](../technologies/google-cloud/gcp-assured-workloads.md): Applies controls for data location, personnel access and supported services to folders so workloads meet regulatory regimes such as FedRAMP, CJIS and EU sovereignty requirements.
- [Google Cloud Sensitive Data Protection](../technologies/google-cloud/gcp-sensitive-data-protection.md): Discovers, classifies and de-identifies sensitive data across BigQuery, Cloud SQL, Cloud Storage and arbitrary content, and measures re-identification risk.

## Security and access

- [BigQuery data masking](../technologies/google-cloud/gcp-bigquery-data-masking.md): Masks column values at query time according to data policies, using rules such as hashing, nullifying, partial masking or custom masking routines.
- [BigQuery policy tags](../technologies/google-cloud/gcp-bigquery-policy-tags.md): Hierarchical taxonomies of tags attached to columns that drive column-level access control and data masking policies.
- [BigQuery row-level security](../technologies/google-cloud/gcp-bigquery-row-level-security.md): Row access policies that filter which rows of a table each user or group can see, using SQL filter expressions and optional lookup subqueries.
- [Google Cloud Identity and Access Management](../technologies/google-cloud/gcp-iam.md): Grants roles to users, groups and service accounts on organisation, folder, project and resource levels, with conditions, deny policies and identity federation.
- [Google Cloud Key Management Service](../technologies/google-cloud/gcp-cloud-kms.md): Creates and manages encryption keys, including hardware-backed and externally held keys, used as customer-managed encryption keys by Google Cloud services.
- [Google Cloud Logging](../technologies/google-cloud/gcp-cloud-logging.md): Collects, stores and routes logs, including Cloud Audit Logs of admin and data access, with Log Analytics for SQL queries over logs.
- [Google Cloud Secret Manager](../technologies/google-cloud/gcp-secret-manager.md): Stores, versions and rotates API keys, passwords and certificates for pipelines and applications under IAM.
- [Google Cloud Security Command Center](../technologies/google-cloud/gcp-security-command-center.md): Security and risk management service that finds misconfigurations, vulnerabilities and threats across Google Cloud, including where sensitive data is exposed.
- [VPC Service Controls](../technologies/google-cloud/gcp-vpc-service-controls.md): Defines security perimeters around Google Cloud projects and services so that data in services such as BigQuery and Cloud Storage cannot be copied outside them.

## Data sharing and collaboration

- [BigQuery data clean rooms](../technologies/google-cloud/gcp-bigquery-data-clean-rooms.md): Built on BigQuery sharing, lets several parties contribute data that others can query only through analysis rules or approved query templates.
- [BigQuery sharing](../technologies/google-cloud/gcp-bigquery-sharing.md): Data exchange service where publishers list datasets, views, models and Pub/Sub topics for subscribers, who get linked read-only copies without data duplication.

## Data products

- [Knowledge Catalog data products](../technologies/google-cloud/gcp-knowledge-catalog-data-products.md): Packages catalogued assets into data products with owners, documentation, contracts covering refresh and quality expectations, and access groups that consumers request to join.

## Development and DataOps

- [Agent Platform Workbench](../technologies/google-cloud/gcp-agent-platform-workbench.md): Managed JupyterLab instances with configurable CPUs, GPUs and Google Cloud integrations for data science and ML development.
- [BigQuery Data Engineering Agent](../technologies/google-cloud/gcp-bigquery-data-engineering-agent.md): Gemini agent in BigQuery pipelines and Dataform that writes or changes pipeline code (SQLX) from natural-language requests and investigates failed runs.
- [Colab Enterprise](../technologies/google-cloud/gcp-colab-enterprise.md): Managed Colab notebooks with shared runtimes and IAM, used both on Agent Platform and as the notebook engine inside BigQuery Studio.
- [Data Agent Kit](../technologies/google-cloud/gcp-data-agent-kit.md) (preview): IDE extension that connects coding agents and developers to Google Cloud data services through their remote MCP servers.
- [Gemini in BigQuery](../technologies/google-cloud/gcp-gemini-in-bigquery.md): Gemini assistance in BigQuery for generating, completing, explaining and fixing SQL and Python, and for generating dataset insights.
- [Google Cloud Build](../technologies/google-cloud/gcp-cloud-build.md): Serverless CI/CD service that builds, tests and deploys code and infrastructure in response to repository events.

## Platform operations

- [BigQuery INFORMATION_SCHEMA views](../technologies/google-cloud/gcp-bigquery-information-schema.md): System views exposing jobs, slot usage, reservations, storage, table metadata and replication state as queryable tables.
- [BigQuery managed disaster recovery](../technologies/google-cloud/gcp-bigquery-managed-disaster-recovery.md): Cross-region dataset replication paired with failover reservations so compute and storage can be switched to a secondary region in a hard or soft failover.
- [BigQuery Migration Service](../technologies/google-cloud/gcp-bigquery-migration-service.md): Tooling for moving warehouses to BigQuery, covering assessment, batch and interactive SQL translation, data transfer and validation.
- [BigQuery table snapshots](../technologies/google-cloud/gcp-bigquery-table-snapshots.md): Read-only, point-in-time copies of a table that store only the bytes that differ from the base table and can be kept beyond the time travel window.
- [Google Cloud Billing](../technologies/google-cloud/gcp-cloud-billing.md): Billing accounts, budgets and alerts, detailed billing export to BigQuery and FinOps reports for attributing and controlling Google Cloud spend.
- [Google Cloud Carbon Footprint](../technologies/google-cloud/gcp-carbon-footprint.md): Console dashboard and export that estimate location- and market-based greenhouse gas emissions from Google Cloud usage by project, region and product.
- [Google Cloud Infrastructure Manager](../technologies/google-cloud/gcp-infrastructure-manager.md): Managed service that runs Terraform deployments of Google Cloud resources and keeps their state.
- [Google Cloud Monitoring](../technologies/google-cloud/gcp-cloud-monitoring.md): Collects metrics from Google Cloud services and applications, with dashboards, uptime checks and alerting policies.
- [Google Cloud Resource Manager](../technologies/google-cloud/gcp-resource-manager.md): Organises resources into an organisation, folders and projects, with tags and organisation policies inherited down the hierarchy.

## Specialised data types

- [BigQuery geospatial analytics](../technologies/google-cloud/gcp-bigquery-geospatial.md): GEOGRAPHY type, spatial functions and spatial clustering for storing and analysing points, lines and polygons in BigQuery.
- [BigQuery Graph](../technologies/google-cloud/gcp-bigquery-graph.md): Defines property graphs over existing BigQuery tables and queries them with ISO GQL, without copying data.
- [BigQuery object tables and ObjectRef](../technologies/google-cloud/gcp-bigquery-object-tables.md): Exposes files in Cloud Storage as rows of metadata (object tables) or as ObjectRef values inside ordinary tables so images, documents and audio can be governed and processed with SQL.
- [Google Earth Engine](../technologies/google-cloud/gcp-earth-engine.md): Cloud platform with a large catalogue of satellite imagery and other raster geospatial datasets, and APIs for analysing them at regional to global scale.

