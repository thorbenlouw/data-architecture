---
type: Platform
id: platform-ibm
title: IBM
description: IBM's watsonx data, AI and governance products, with integration tools and Confluent streaming.
vendor: IBM
resource: https://www.ibm.com/
folder: ibm
order: 12
terminology:
  ai-agents: watsonx Orchestrate
  change-data-capture: Data Replication
  data-catalogue: watsonx.data intelligence (Knowledge Catalog)
  data-marketplace: Data Product Hub
  data-observability: Data observability (Databand)
  low-code-transformation: DataStage flows
  model-governance: AI factsheets / watsonx.governance
  multi-tenancy: Projects and spaces (Software Hub)
  retrieval-augmented-generation: OpenRAG
families:
- name: IBM watsonx
  aliases: [watsonx]
  technologies:
  - ibm-watsonx-data
  - ibm-watsonx-data-integration
  - ibm-watsonx-data-intelligence
  - ibm-watsonx-ai
  - ibm-watsonx-governance
  - ibm-watsonx-orchestrate
- name: IBM watsonx.data
  technologies:
  - ibm-watsonx-data
  - ibm-watsonx-data-presto
  - ibm-watsonx-data-spark
  - ibm-watsonx-data-opensearch-openrag
  - ibm-astra-db
- name: IBM watsonx.data integration
  aliases: [DataStage, IBM DataStage]
  technologies: [ibm-watsonx-data-integration, ibm-streamsets, ibm-data-replication, ibm-data-observability]
- name: IBM watsonx.data intelligence
  aliases: [IBM Knowledge Catalog]
  technologies:
  - ibm-watsonx-data-intelligence
  - ibm-watsonx-data-intelligence-quality
  - ibm-manta-data-lineage
  - ibm-data-product-hub
- name: Confluent
  aliases: [Confluent data streaming platform]
  technologies:
  - confluent-cloud
  - confluent-platform
  - confluent-cloud-flink
  - confluent-tableflow
  - confluent-intelligence
  - warpstream
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

IBM organises its data and AI portfolio under the watsonx brand. watsonx.data is an open lakehouse that runs Presto, Spark, OpenSearch and Cassandra engines over Iceberg, Delta and Hive tables with a shared catalogue. watsonx.data integration brings DataStage batch ETL, StreamSets streaming, IBM Data Replication and Databand observability under one control plane, and watsonx.data intelligence (formerly IBM Knowledge Catalog) covers cataloguing, data quality, Manta lineage and Data Product Hub. watsonx.ai is the studio and runtime for foundation models and machine learning, watsonx.governance governs AI systems and watsonx Orchestrate builds and runs agents. Db2, Netezza, Guardium and Optim continue alongside, and IBM Software Hub (Cloud Pak for Data) runs the self-managed versions on Red Hat OpenShift.

Event streaming comes from Confluent, whose acquisition IBM completed on 17 March 2026. The Confluent products keep their names: Confluent Cloud (managed Apache Kafka with connectors and Stream Governance), Confluent Platform (self-managed Kafka), Confluent Cloud for Apache Flink, Tableflow (topics materialised as Iceberg or Delta tables), WarpStream (Kafka-compatible streaming that runs in the customer's cloud account) and Confluent Intelligence for streaming agents. IBM positions Confluent beside watsonx.data, IBM MQ and webMethods.

# Notes

- Older product names persist in documentation and contracts, among them DataStage, Knowledge Catalog, Watson Studio, Watson Machine Learning, Cloud Pak for Data and Databand.
- Acquisitions that shape the portfolio are Databand (2022), Manta (2023), StreamSets and webMethods from Software AG (2024), DataStax (2025, bringing Astra DB and Langflow) and Confluent (2026).
- watsonx products are offered as SaaS and as self-managed software on IBM Software Hub, which is the usual route for regulated customers that cannot use SaaS.
- Db2 for z/OS remains the system of record in many banks and insurers, which shapes change data capture and offload designs.
- watsonx.governance can govern models and agents built outside IBM, for example on AWS and Azure.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 10 of 22 | [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Database extraction](../capabilities/ingestion-integration/database-extraction.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md), [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 7 of 23 | [Data versioning](../capabilities/storage/data-versioning.md), [Object storage](../capabilities/storage/object-storage.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Platform-managed storage](../capabilities/storage/managed-storage.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Time travel](../capabilities/storage/time-travel.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 9 of 18 (+1 in preview) | [Data enrichment](../capabilities/processing/data-enrichment.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Self-service data preparation](../capabilities/processing/data-preparation.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [AI functions in SQL](../capabilities/processing/ai-functions.md) (preview only) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 1 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| [Query and compute](../capabilities/compute/compute.md) | 10 of 22 | [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Workload management](../capabilities/compute/workload-management.md), [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Materialised views](../capabilities/compute/materialised-views.md), [Result caching](../capabilities/compute/result-caching.md), [Container services](../capabilities/compute/container-services.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 3 of 13 | [Change feeds](../capabilities/serving/change-feeds.md), [Data APIs](../capabilities/serving/data-apis.md), [Data export](../capabilities/serving/data-export.md), [Decision management](../capabilities/serving/decision-management.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 0 of 20 | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md), [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 6 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Feature store](../capabilities/machine-learning/feature-store.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 8 of 18 (+1 in preview) | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) (preview only) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 16 of 23 (+1 in preview) | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md) (preview only) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 12 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Table-level lineage](../capabilities/metadata/table-lineage.md), [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 7 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 0 of 7 | [Master and reference data](../capabilities/master-data/master-data.md), [Master data management](../capabilities/master-data/master-data-management.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 11 of 24 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 9 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Privileged access management](../capabilities/security/privileged-access.md), [Role-based access control](../capabilities/security/role-based-access.md), [Row-level security](../capabilities/security/row-level-security.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 2 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 3 of 7 | [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 5 of 16 | [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Data application hosting](../capabilities/development-lifecycle/data-applications.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 9 of 27 | [Cost management](../capabilities/platform-operations/cost-management.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Platform migration](../capabilities/platform-operations/platform-migration.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 3 of 10 | [Geospatial data](../capabilities/specialised-data/geospatial-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) |

# Product families

- **IBM watsonx** (also: watsonx): [IBM watsonx.data](../technologies/ibm/ibm-watsonx-data.md), [IBM watsonx.data integration](../technologies/ibm/ibm-watsonx-data-integration.md), [IBM watsonx.data intelligence](../technologies/ibm/ibm-watsonx-data-intelligence.md), [IBM watsonx.ai](../technologies/ibm/ibm-watsonx-ai.md), [IBM watsonx.governance](../technologies/ibm/ibm-watsonx-governance.md), [IBM watsonx Orchestrate](../technologies/ibm/ibm-watsonx-orchestrate.md)
- **IBM watsonx.data**: [IBM watsonx.data](../technologies/ibm/ibm-watsonx-data.md), [Presto (C++) engine in IBM watsonx.data](../technologies/ibm/ibm-watsonx-data-presto.md), [Spark engine in IBM watsonx.data](../technologies/ibm/ibm-watsonx-data-spark.md), [OpenSearch and OpenRAG in IBM watsonx.data](../technologies/ibm/ibm-watsonx-data-opensearch-openrag.md), [IBM Astra DB (DataStax)](../technologies/ibm/ibm-astra-db.md)
- **IBM watsonx.data integration** (also: DataStage, IBM DataStage): [IBM watsonx.data integration](../technologies/ibm/ibm-watsonx-data-integration.md), [IBM StreamSets](../technologies/ibm/ibm-streamsets.md), [IBM Data Replication](../technologies/ibm/ibm-data-replication.md), [Data observability in IBM watsonx.data integration](../technologies/ibm/ibm-data-observability.md)
- **IBM watsonx.data intelligence** (also: IBM Knowledge Catalog): [IBM watsonx.data intelligence](../technologies/ibm/ibm-watsonx-data-intelligence.md), [Data quality in IBM watsonx.data intelligence](../technologies/ibm/ibm-watsonx-data-intelligence-quality.md), [IBM Manta Data Lineage](../technologies/ibm/ibm-manta-data-lineage.md), [IBM Data Product Hub](../technologies/ibm/ibm-data-product-hub.md)
- **Confluent** (also: Confluent data streaming platform): [Confluent Cloud](../technologies/ibm/confluent-cloud.md), [Confluent Platform](../technologies/ibm/confluent-platform.md), [Confluent Cloud for Apache Flink](../technologies/ibm/confluent-cloud-flink.md), [Confluent Tableflow](../technologies/ibm/confluent-tableflow.md), [Confluent Intelligence](../technologies/ibm/confluent-intelligence.md) (preview), [WarpStream](../technologies/ibm/warpstream.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| AI factsheets / watsonx.governance | [Model governance](../capabilities/mlops/model-governance.md) |
| Data observability (Databand) | [Data observability](../capabilities/data-quality/data-observability.md) |
| Data Product Hub | [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| Data Replication | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) |
| DataStage flows | [Low-code transformation](../capabilities/processing/low-code-transformation.md) |
| OpenRAG | [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) |
| Projects and spaces (Software Hub) | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| watsonx Orchestrate | [AI agents](../capabilities/generative-ai/ai-agents.md) |
| watsonx.data intelligence (Knowledge Catalog) | [Data catalogue](../capabilities/metadata/data-catalogue.md) |

# Technologies

## Ingestion and integration

- [Confluent Cloud](../technologies/ibm/confluent-cloud.md): Fully managed Apache Kafka service on AWS, Azure and Google Cloud, with managed connectors, Schema Registry, Stream Governance and cluster linking.
- [Confluent Platform](../technologies/ibm/confluent-platform.md): Self-managed Kafka distribution for on-premises and private cloud, with connectors, Schema Registry, Flink and management tooling.
- [Confluent Tableflow](../technologies/ibm/confluent-tableflow.md): Materialises Kafka topics and their schemas as Apache Iceberg or Delta Lake tables, taking care of type conversion, schema evolution, compaction and catalogue sync.
- [IBM Data Replication](../technologies/ibm/ibm-data-replication.md): Log-based change data capture that replicates changes from Db2, Db2 for z/OS, Oracle, SQL Server and other databases to databases, Kafka and lakehouse targets.
- [IBM StreamSets](../technologies/ibm/ibm-streamsets.md): Low-code streaming and batch ingestion tool whose pipelines detect and adapt to schema drift, deployable as SaaS or in the customer's cloud or data centre.
- [WarpStream](../technologies/ibm/warpstream.md): Kafka-compatible streaming service that runs as stateless agents in the customer's cloud account and writes data directly to object storage, managed by Confluent.

## Processing and transformation

- [Confluent Cloud for Apache Flink](../technologies/ibm/confluent-cloud-flink.md): Serverless Apache Flink service for continuous SQL and Table API processing over Kafka topics, with autoscaling and built-in functions.
- [IBM watsonx.data integration](../technologies/ibm/ibm-watsonx-data-integration.md): Integration product with one control plane for batch ETL and ELT, streaming pipelines, change data replication, unstructured data preparation and pipeline observability, with an agent that builds pipelines from natural language.
- [Spark engine in IBM watsonx.data](../technologies/ibm/ibm-watsonx-data-spark.md): Managed Apache Spark engine in watsonx.data for data engineering, table maintenance and ML pipelines on lakehouse tables.

## Query and compute

- [IBM Netezza Performance Server](../technologies/ibm/ibm-netezza.md): MPP data warehouse, now offered as a cloud service and on appliances, that can also read and write Iceberg tables shared with watsonx.data.
- [IBM watsonx.data](../technologies/ibm/ibm-watsonx-data.md): Open lakehouse service that runs Presto, Spark, OpenSearch and Cassandra engines over Iceberg, Delta and Hive tables in object storage with shared catalogues and access policies.
- [Presto (C++) engine in IBM watsonx.data](../technologies/ibm/ibm-watsonx-data-presto.md): Distributed SQL engine in watsonx.data for interactive analytics and federation across lakehouse tables and external databases.

## Serving and activation

- [IBM Astra DB (DataStax)](../technologies/ibm/ibm-astra-db.md): Managed Apache Cassandra database with vector search, offered as the operational NoSQL engine in watsonx.data and as a standalone service.
- [IBM Db2](../technologies/ibm/ibm-db2.md): IBM's relational database for transactional and analytical workloads, available on Linux, Unix, Windows and z/OS, self-managed or as managed services, with vector support and AI-driven tuning.

## Generative AI

- [Confluent Intelligence](../technologies/ibm/confluent-intelligence.md) (preview): Confluent Cloud's AI layer. It runs event-driven agents on Flink, serves the latest topic state to external agents over MCP, and applies built-in ML functions and model calls to streams.
- [IBM watsonx Orchestrate](../technologies/ibm/ibm-watsonx-orchestrate.md): Agent platform for building agents, orchestrating IBM and third-party agents and tools, and tracing, evaluating and governing them from one control plane.
- [IBM watsonx.ai](../technologies/ibm/ibm-watsonx-ai.md): Studio and runtime for foundation models and ML, including Prompt Lab, model tuning, AutoAI, notebooks, RAG tooling and deployment of models and AI services through APIs.
- [OpenSearch and OpenRAG in IBM watsonx.data](../technologies/ibm/ibm-watsonx-data-opensearch-openrag.md): Vector and keyword search engine in watsonx.data, with OpenRAG tooling for document processing, hybrid search and agentic retrieval for grounding AI applications.

## Metadata and discovery

- [IBM Manta Data Lineage](../technologies/ibm/ibm-manta-data-lineage.md): Automated lineage service that scans code, ETL tools, databases and BI reports to build column-level, end-to-end lineage across more than 50 technologies.
- [IBM watsonx.data intelligence](../technologies/ibm/ibm-watsonx-data-intelligence.md): Governance product that catalogues structured and unstructured data with business terms, classifications, policies, quality scores and lineage, and uses AI to enrich metadata.

## Data quality and observability

- [Data observability in IBM watsonx.data integration](../technologies/ibm/ibm-data-observability.md): Monitoring of pipeline runs and datasets for failures, durations, row-count and quality deviations and missed freshness SLAs, with alert routing and root cause analysis.
- [Data quality in IBM watsonx.data intelligence](../technologies/ibm/ibm-watsonx-data-intelligence-quality.md): Profiling, rule definitions, anomaly detection and quality scores for catalogued data, with remediation ranked by downstream impact.

## Governance and compliance

- [IBM watsonx.governance](../technologies/ibm/ibm-watsonx-governance.md): AI governance product that inventories AI use cases and models, including detected unapproved use, maps them to regulations, monitors them and records evidence and decisions.

## Security and access

- [IBM Guardium Data Security Center](../technologies/ibm/ibm-guardium-data-security-center.md): Data security suite that discovers and classifies sensitive data, monitors database activity, assesses vulnerabilities, detects risky behaviour and manages cryptography.

## Data sharing and collaboration

- [IBM Data Product Hub](../technologies/ibm/ibm-data-product-hub.md): Marketplace in watsonx.data intelligence where producers package data with business meaning, quality, ownership and contracts, and consumers find and request it.

## Development and DataOps

- [IBM InfoSphere Optim](../technologies/ibm/ibm-optim.md): Tools for archiving application data and creating masked, subsetted test data from production databases.

## Platform operations

- [IBM Software Hub (Cloud Pak for Data)](../technologies/ibm/ibm-software-hub.md): Red Hat OpenShift-based platform for installing and running IBM data and AI services, including watsonx.data, watsonx.ai and data intelligence, on premises or in any cloud.

