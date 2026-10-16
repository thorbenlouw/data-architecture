---
type: Platform
id: platform-aws
title: Amazon Web Services
description: Amazon's cloud, with separate managed services for each part of the data and AI stack.
vendor: Amazon Web Services
resource: https://aws.amazon.com/
folder: aws
order: 1
terminology:
  access-requests: SageMaker Catalog subscription requests
  agent-tool-access: AgentCore Gateway
  ai-agents: Bedrock AgentCore (harness and Runtime)
  ai-guardrails: Bedrock Guardrails; AgentCore Policy
  attribute-based-access: LF-Tags (Lake Formation tag-based access control)
  audit-logging: AWS CloudTrail data events
  automl: SageMaker Canvas and Autopilot
  backup-restore: AWS Backup
  bulk-data-transfer: DataSync, Snowball Edge, Data Transfer Terminal
  change-data-capture: AWS DMS ongoing replication
  change-feeds: DynamoDB Streams
  column-masking: Redshift dynamic data masking
  conversational-analytics: Quick Sight topics and Amazon Quick chat
  cost-attribution: Cost allocation tags and cost categories
  customer-managed-keys: AWS KMS customer managed keys
  data-anomaly-detection: Glue Data Quality anomaly detection observations
  data-catalogue: Amazon SageMaker Catalog (Amazon DataZone)
  data-classification: Amazon Macie sensitive data discovery
  data-clean-rooms: AWS Clean Rooms collaborations
  data-marketplace: AWS Data Exchange
  data-product-specification: SageMaker Catalog data products
  data-quality-rules: DQDL rulesets (Glue Data Quality)
  database-replication: zero-ETL integrations
  decoupled-storage-compute: Lakehouse architecture of Amazon SageMaker; Redshift RA3
  document-processing: Amazon Textract; Bedrock Data Automation
  elastic-scaling: Redshift concurrency scaling
  event-driven-triggering: EventBridge rules and S3 Event Notifications
  experiment-tracking: SageMaker AI MLflow Apps
  file-ingestion: Redshift auto-copy (S3 event integration)
  foundation-model-access: Amazon Bedrock
  identity-authentication: IAM roles; IAM Identity Center trusted identity propagation
  in-database-ml: Redshift ML (CREATE MODEL)
  internal-data-sharing: Redshift data sharing; Lake Formation cross-account grants
  managed-file-transfer: AWS Transfer Family
  managed-storage: Redshift Managed Storage (RMS)
  multi-tenancy: SageMaker Unified Studio domains and projects
  notebooks: SageMaker Unified Studio notebooks
  object-storage: Amazon S3 general purpose buckets
  open-table-formats: S3 Tables (Apache Iceberg table buckets)
  paginated-reports: Quick Sight pixel-perfect reports
  query-federation: Athena federated query and federated catalogues
  result-caching: Athena query result reuse
  retrieval-augmented-generation: Bedrock Knowledge Bases
  row-level-security: Lake Formation data filters; Redshift RLS policies
  self-service-provisioning: Unified Studio project profiles
  semi-structured-data: Redshift SUPER data type
  spend-controls: AWS Budgets actions
  sql-query-engine: Amazon Athena; Amazon Redshift
  storage-tiering: S3 storage classes and S3 Lifecycle rules
  stream-processing: Amazon Managed Service for Apache Flink
  streaming-ingestion: Amazon Data Firehose; Redshift streaming ingestion
  system-telemetry: AWS Data Exports (CUR 2.0, FOCUS)
  table-catalogue: AWS Glue Data Catalog
  table-maintenance: S3 Tables automatic maintenance; Glue table optimizers
  vector-search: S3 Vectors; OpenSearch vector engine
  workflow-orchestration: Amazon MWAA; Step Functions state machines
  workload-isolation: Redshift multi-warehouse (data sharing); Athena workgroups and Capacity Reservations
  zero-copy-cloning: Aurora cloning
families:
- name: Amazon SageMaker
  aliases: [next generation of Amazon SageMaker]
  technologies:
  - aws-sagemaker-unified-studio
  - aws-sagemaker-catalog
  - aws-sagemaker-catalog-lineage
  - aws-sagemaker-lakehouse
  - aws-sagemaker-data-agent
- name: Amazon SageMaker AI
  technologies:
  - aws-sagemaker-studio
  - aws-sagemaker-training
  - aws-sagemaker-hyperpod
  - aws-sagemaker-inference
  - aws-sagemaker-jumpstart
  - aws-sagemaker-autopilot
  - aws-sagemaker-canvas
  - aws-sagemaker-feature-store
  - aws-sagemaker-mlflow
  - aws-sagemaker-model-registry
  - aws-sagemaker-pipelines
  - aws-sagemaker-model-monitor
  - aws-sagemaker-clarify
  - aws-sagemaker-ground-truth
- name: Amazon Bedrock
  technologies:
  - aws-bedrock
  - aws-bedrock-knowledge-bases
  - aws-bedrock-guardrails
  - aws-bedrock-evaluations
  - aws-bedrock-data-automation
  - aws-bedrock-model-customization
  - aws-bedrock-prompt-management
  - aws-bedrock-agents-classic
- name: Amazon Bedrock AgentCore
  aliases: [AgentCore]
  technologies:
  - aws-bedrock-agentcore
  - aws-bedrock-agentcore-gateway
  - aws-bedrock-agentcore-policy
  - aws-bedrock-agentcore-evaluations
- name: AWS Glue
  technologies:
  - aws-glue-etl
  - aws-glue-data-catalog
  - aws-glue-data-quality
  - aws-glue-databrew
  - aws-glue-materialized-views
  - aws-glue-schema-registry
- name: Amazon Redshift
  technologies:
  - aws-redshift
  - aws-redshift-serverless
  - aws-redshift-spectrum
  - aws-redshift-data-sharing
  - aws-redshift-federated-query
  - aws-redshift-materialized-views
  - aws-redshift-ml
  - aws-redshift-streaming-ingestion
  - aws-redshift-auto-copy
  - aws-redshift-concurrency-scaling
  - aws-redshift-fine-grained-security
- name: Amazon EMR
  aliases: [Amazon Elastic MapReduce]
  technologies: [aws-emr-on-ec2, aws-emr-on-eks, aws-emr-serverless]
- name: Amazon S3
  aliases: [Amazon Simple Storage Service]
  technologies:
  - aws-s3
  - aws-s3-tables
  - aws-s3-vectors
  - aws-s3-files
  - aws-s3-metadata
  - aws-s3-storage-classes-lifecycle
- name: Amazon Athena
  technologies: [aws-athena, aws-athena-spark]
- name: Amazon Quick
  aliases: [Amazon Quick Suite]
  technologies: [aws-quick, aws-quick-sight]
- name: Amazon Timestream
  technologies: [aws-timestream-influxdb, aws-timestream-liveanalytics]
- name: Amazon Neptune
  technologies: [aws-neptune, aws-neptune-analytics]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Amazon Web Services sells its data, analytics and AI capabilities as separately priced managed services that share IAM for access control, Amazon S3 for storage and the AWS Glue Data Catalog for table metadata. Since December 2024 the Amazon SageMaker brand has covered analytics as well as AI. SageMaker Unified Studio is the shared workbench; SageMaker Catalog, built on Amazon DataZone, handles business cataloguing, data products and access requests; the lakehouse architecture of Amazon SageMaker organises S3, S3 Tables and Redshift Managed Storage into catalogues governed by Lake Formation; and Amazon SageMaker AI is the machine learning service that previously carried the SageMaker name on its own.

Query and processing engines sit alongside these: Amazon Athena for serverless SQL, Amazon Redshift as the warehouse, AWS Glue and Amazon EMR for Spark, and Kinesis Data Streams, Amazon MSK, Amazon Data Firehose and Managed Service for Apache Flink for streaming, with Amazon MWAA and Step Functions for orchestration. Generative AI is split between Amazon Bedrock (model access, knowledge bases, guardrails and evaluation) and Bedrock AgentCore (hosting, tooling and policy for agents). Business users work in Amazon Quick, whose BI component is Amazon Quick Sight.

# Notes

- Amazon QuickSight became Quick Sight within Amazon Quick Suite in October 2025, and the suite was shortened to Amazon Quick in early 2026; existing QuickSight APIs keep their names. Earlier renames still seen in estates include Amazon SageMaker to Amazon SageMaker AI (December 2024) and Kinesis Data Firehose to Amazon Data Firehose.
- In 2025 and 2026 AWS moved a number of services to maintenance, closing them to new customers while supporting existing ones. They include Amazon Q Business, Amazon Kendra, Bedrock Agents Classic, SageMaker Model Monitor, Clarify and Ground Truth, Glue for Ray, CloudTrail Lake, AWS Audit Manager, Timestream for LiveAnalytics and the Snow family, so a service's status is worth checking before adopting it.
- The lakehouse architecture is a logical layer over the Glue Data Catalog, Lake Formation and Redshift Managed Storage rather than a separate store. Apache Iceberg is the common table format across Athena, Redshift, EMR, Glue and S3 Tables.
- Zero-ETL integrations replicate AWS databases, self-managed databases and SaaS applications into Redshift or the lakehouse without pipelines, and overlap with AWS DMS for change data capture.
- AWS has no first-party semantic layer, governed metric store, master data survivorship, reference data management, data contracts or transformation-as-code tool. AWS Entity Resolution matches records but does not build golden records. Partners such as dbt, Atlan, Collibra and Informatica usually fill these gaps, many of them through AWS Marketplace.
- All compute runs in the customer's own accounts and VPCs, so isolation between teams rests on account structure, IAM and network design rather than on a vendor-managed security boundary.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 16 of 22 | [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 19 of 23 | [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [Data branching and tagging](../capabilities/storage/data-branching.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 13 of 18 | [Data enrichment](../capabilities/processing/data-enrichment.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 5 of 5 |  |
| [Query and compute](../capabilities/compute/compute.md) | 20 of 22 | [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 6 of 13 | [Data APIs](../capabilities/serving/data-apis.md), [Decision management](../capabilities/serving/decision-management.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [SQL and programmatic access](../capabilities/serving/sql-access.md), [Audience building and activation](../capabilities/serving/audience-activation.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 9 of 20 | [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 15 of 20 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 12 of 18 | [Model monitoring](../capabilities/mlops/model-monitoring.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Edge inference](../capabilities/mlops/edge-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 22 of 23 | [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 14 of 20 | [Active metadata](../capabilities/metadata/active-metadata.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Data certification](../capabilities/metadata/data-certification.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 9 of 12 | [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 3 of 7 | [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md) |
| [Governance and compliance](../capabilities/governance/governance.md) | 12 of 24 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Policy management](../capabilities/governance/data-policy-management.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Records of processing](../capabilities/governance/records-of-processing.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Security and access](../capabilities/security/security.md) | 17 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 6 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 3 of 7 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 10 of 16 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 26 of 27 | [Platform incident management](../capabilities/platform-operations/platform-incident-management.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 9 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md) |

# Product families

- **Amazon SageMaker** (also: next generation of Amazon SageMaker): [Amazon SageMaker Unified Studio](../technologies/aws/aws-sagemaker-unified-studio.md), [Amazon SageMaker Catalog](../technologies/aws/aws-sagemaker-catalog.md), [Amazon SageMaker Catalog data lineage](../technologies/aws/aws-sagemaker-catalog-lineage.md), [Lakehouse architecture of Amazon SageMaker](../technologies/aws/aws-sagemaker-lakehouse.md), [Amazon SageMaker Data Agent](../technologies/aws/aws-sagemaker-data-agent.md)
- **Amazon SageMaker AI**: [Amazon SageMaker Studio](../technologies/aws/aws-sagemaker-studio.md), [Amazon SageMaker AI training jobs](../technologies/aws/aws-sagemaker-training.md), [Amazon SageMaker HyperPod](../technologies/aws/aws-sagemaker-hyperpod.md), [Amazon SageMaker AI inference](../technologies/aws/aws-sagemaker-inference.md), [Amazon SageMaker JumpStart](../technologies/aws/aws-sagemaker-jumpstart.md), [Amazon SageMaker Autopilot](../technologies/aws/aws-sagemaker-autopilot.md), [Amazon SageMaker Canvas](../technologies/aws/aws-sagemaker-canvas.md), [Amazon SageMaker Feature Store](../technologies/aws/aws-sagemaker-feature-store.md), [Amazon SageMaker AI with MLflow](../technologies/aws/aws-sagemaker-mlflow.md), [Amazon SageMaker Model Registry](../technologies/aws/aws-sagemaker-model-registry.md), [Amazon SageMaker Pipelines](../technologies/aws/aws-sagemaker-pipelines.md), [Amazon SageMaker Model Monitor](../technologies/aws/aws-sagemaker-model-monitor.md) (deprecated), [Amazon SageMaker Clarify](../technologies/aws/aws-sagemaker-clarify.md) (deprecated), [Amazon SageMaker Ground Truth](../technologies/aws/aws-sagemaker-ground-truth.md) (deprecated)
- **Amazon Bedrock**: [Amazon Bedrock](../technologies/aws/aws-bedrock.md), [Amazon Bedrock Knowledge Bases](../technologies/aws/aws-bedrock-knowledge-bases.md), [Amazon Bedrock Guardrails](../technologies/aws/aws-bedrock-guardrails.md), [Amazon Bedrock Evaluations](../technologies/aws/aws-bedrock-evaluations.md), [Amazon Bedrock Data Automation](../technologies/aws/aws-bedrock-data-automation.md), [Amazon Bedrock custom models](../technologies/aws/aws-bedrock-model-customization.md), [Amazon Bedrock Prompt management](../technologies/aws/aws-bedrock-prompt-management.md), [Amazon Bedrock Agents Classic](../technologies/aws/aws-bedrock-agents-classic.md) (deprecated)
- **Amazon Bedrock AgentCore** (also: AgentCore): [Amazon Bedrock AgentCore](../technologies/aws/aws-bedrock-agentcore.md), [Amazon Bedrock AgentCore Gateway](../technologies/aws/aws-bedrock-agentcore-gateway.md), [Amazon Bedrock AgentCore Policy](../technologies/aws/aws-bedrock-agentcore-policy.md), [Amazon Bedrock AgentCore Evaluations](../technologies/aws/aws-bedrock-agentcore-evaluations.md)
- **AWS Glue**: [AWS Glue ETL](../technologies/aws/aws-glue-etl.md), [AWS Glue Data Catalog](../technologies/aws/aws-glue-data-catalog.md), [AWS Glue Data Quality](../technologies/aws/aws-glue-data-quality.md), [AWS Glue DataBrew](../technologies/aws/aws-glue-databrew.md), [AWS Glue Data Catalog materialized views](../technologies/aws/aws-glue-materialized-views.md), [AWS Glue Schema Registry](../technologies/aws/aws-glue-schema-registry.md)
- **Amazon Redshift**: [Amazon Redshift](../technologies/aws/aws-redshift.md), [Amazon Redshift Serverless](../technologies/aws/aws-redshift-serverless.md), [Amazon Redshift Spectrum](../technologies/aws/aws-redshift-spectrum.md), [Amazon Redshift data sharing](../technologies/aws/aws-redshift-data-sharing.md), [Amazon Redshift federated query](../technologies/aws/aws-redshift-federated-query.md), [Amazon Redshift materialized views](../technologies/aws/aws-redshift-materialized-views.md), [Amazon Redshift ML](../technologies/aws/aws-redshift-ml.md), [Amazon Redshift streaming ingestion](../technologies/aws/aws-redshift-streaming-ingestion.md), [Amazon Redshift auto-copy](../technologies/aws/aws-redshift-auto-copy.md), [Amazon Redshift concurrency scaling](../technologies/aws/aws-redshift-concurrency-scaling.md), [Amazon Redshift row-level security and dynamic data masking](../technologies/aws/aws-redshift-fine-grained-security.md)
- **Amazon EMR** (also: Amazon Elastic MapReduce): [Amazon EMR on EC2](../technologies/aws/aws-emr-on-ec2.md), [Amazon EMR on EKS](../technologies/aws/aws-emr-on-eks.md), [Amazon EMR Serverless](../technologies/aws/aws-emr-serverless.md)
- **Amazon S3** (also: Amazon Simple Storage Service): [Amazon S3](../technologies/aws/aws-s3.md), [Amazon S3 Tables](../technologies/aws/aws-s3-tables.md), [Amazon S3 Vectors](../technologies/aws/aws-s3-vectors.md), [Amazon S3 Files](../technologies/aws/aws-s3-files.md), [Amazon S3 Metadata](../technologies/aws/aws-s3-metadata.md), [Amazon S3 storage classes and S3 Lifecycle](../technologies/aws/aws-s3-storage-classes-lifecycle.md)
- **Amazon Athena**: [Amazon Athena](../technologies/aws/aws-athena.md), [Amazon Athena for Apache Spark](../technologies/aws/aws-athena-spark.md)
- **Amazon Quick** (also: Amazon Quick Suite): [Amazon Quick](../technologies/aws/aws-quick.md), [Amazon Quick Sight](../technologies/aws/aws-quick-sight.md)
- **Amazon Timestream**: [Amazon Timestream for InfluxDB](../technologies/aws/aws-timestream-influxdb.md), [Amazon Timestream for LiveAnalytics](../technologies/aws/aws-timestream-liveanalytics.md) (deprecated)
- **Amazon Neptune**: [Amazon Neptune](../technologies/aws/aws-neptune.md), [Amazon Neptune Analytics](../technologies/aws/aws-neptune-analytics.md)

# Terminology

| Name used on this platform | Capability |
|---|---|
| AgentCore Gateway | [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) |
| Amazon Athena; Amazon Redshift | [SQL query engine](../capabilities/compute/sql-query-engine.md) |
| Amazon Bedrock | [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |
| Amazon Data Firehose; Redshift streaming ingestion | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |
| Amazon Macie sensitive data discovery | [Data classification](../capabilities/governance/data-classification.md) |
| Amazon Managed Service for Apache Flink | [Stream processing](../capabilities/processing/stream-processing.md) |
| Amazon MWAA; Step Functions state machines | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| Amazon S3 general purpose buckets | [Object storage](../capabilities/storage/object-storage.md) |
| Amazon SageMaker Catalog (Amazon DataZone) | [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| Amazon Textract; Bedrock Data Automation | [Document processing](../capabilities/processing/document-processing.md) |
| Athena federated query and federated catalogues | [Query federation](../capabilities/compute/query-federation.md) |
| Athena query result reuse | [Result caching](../capabilities/compute/result-caching.md) |
| Aurora cloning | [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) |
| AWS Backup | [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| AWS Budgets actions | [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) |
| AWS Clean Rooms collaborations | [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md) |
| AWS CloudTrail data events | [Audit logging](../capabilities/security/audit-logging.md) |
| AWS Data Exchange | [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| AWS Data Exports (CUR 2.0, FOCUS) | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) |
| AWS DMS ongoing replication | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) |
| AWS Glue Data Catalog | [Table catalogue](../capabilities/storage/table-catalogue.md) |
| AWS KMS customer managed keys | [Customer-managed keys](../capabilities/security/customer-managed-keys.md) |
| AWS Transfer Family | [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md) |
| Bedrock AgentCore (harness and Runtime) | [AI agents](../capabilities/generative-ai/ai-agents.md) |
| Bedrock Guardrails; AgentCore Policy | [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| Bedrock Knowledge Bases | [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) |
| Cost allocation tags and cost categories | [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) |
| DataSync, Snowball Edge, Data Transfer Terminal | [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md) |
| DQDL rulesets (Glue Data Quality) | [Data quality rules](../capabilities/data-quality/data-quality-rules.md) |
| DynamoDB Streams | [Change feeds](../capabilities/serving/change-feeds.md) |
| EventBridge rules and S3 Event Notifications | [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md) |
| Glue Data Quality anomaly detection observations | [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md) |
| IAM roles; IAM Identity Center trusted identity propagation | [Identity and authentication](../capabilities/security/identity-authentication.md) |
| Lake Formation data filters; Redshift RLS policies | [Row-level security](../capabilities/security/row-level-security.md) |
| Lakehouse architecture of Amazon SageMaker; Redshift RA3 | [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md) |
| LF-Tags (Lake Formation tag-based access control) | [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md) |
| Quick Sight pixel-perfect reports | [Paginated reports](../capabilities/analytics-bi/paginated-reports.md) |
| Quick Sight topics and Amazon Quick chat | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) |
| Redshift auto-copy (S3 event integration) | [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| Redshift concurrency scaling | [Elastic scaling](../capabilities/compute/elastic-scaling.md) |
| Redshift data sharing; Lake Formation cross-account grants | [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md) |
| Redshift dynamic data masking | [Column security and dynamic masking](../capabilities/security/column-masking.md) |
| Redshift Managed Storage (RMS) | [Platform-managed storage](../capabilities/storage/managed-storage.md) |
| Redshift ML (CREATE MODEL) | [In-database machine learning](../capabilities/machine-learning/in-database-ml.md) |
| Redshift multi-warehouse (data sharing); Athena workgroups and Capacity Reservations | [Workload isolation](../capabilities/compute/workload-isolation.md) |
| Redshift SUPER data type | [Semi-structured data](../capabilities/storage/semi-structured-data.md) |
| S3 storage classes and S3 Lifecycle rules | [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) |
| S3 Tables (Apache Iceberg table buckets) | [Open table formats](../capabilities/storage/open-table-formats.md) |
| S3 Tables automatic maintenance; Glue table optimizers | [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md) |
| S3 Vectors; OpenSearch vector engine | [Vector search](../capabilities/generative-ai/vector-search.md) |
| SageMaker AI MLflow Apps | [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md) |
| SageMaker Canvas and Autopilot | [AutoML](../capabilities/machine-learning/automl.md) |
| SageMaker Catalog data products | [Data product specification](../capabilities/data-products/data-product-specification.md) |
| SageMaker Catalog subscription requests | [Access requests and reviews](../capabilities/security/access-requests.md) |
| SageMaker Unified Studio domains and projects | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| SageMaker Unified Studio notebooks | [Notebooks](../capabilities/development-lifecycle/notebooks.md) |
| Unified Studio project profiles | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md) |
| zero-ETL integrations | [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md) |

# Technologies

## Ingestion and integration

- [Amazon AppFlow](../technologies/aws/aws-appflow.md): No-code service that moves data on demand, on schedule or on event between SaaS applications and AWS services.
- [Amazon Data Firehose](../technologies/aws/aws-data-firehose.md): Managed delivery stream that buffers events, optionally transforms them, and writes them to S3, Iceberg tables, Redshift, OpenSearch, Splunk or HTTP endpoints.
- [Amazon Kinesis Data Streams](../technologies/aws/aws-kinesis-data-streams.md): Serverless, sharded event stream that stores ordered records for up to 365 days and lets many consumers read them independently.
- [Amazon Managed Streaming for Apache Kafka](../technologies/aws/aws-msk.md): Managed Apache Kafka offering provisioned clusters with Standard or Express brokers and a serverless option.
- [Amazon Redshift auto-copy](../technologies/aws/aws-redshift-auto-copy.md): COPY jobs that watch an S3 prefix and load each new file into a Redshift table once, as it arrives.
- [Amazon Redshift streaming ingestion](../technologies/aws/aws-redshift-streaming-ingestion.md): Reads Kinesis Data Streams and Kafka topics directly into Redshift materialised views with seconds-level latency, without staging in S3.
- [AWS Database Migration Service](../technologies/aws/aws-dms.md): Service that copies data between databases with a full load followed by ongoing change capture from transaction logs, and converts schemas between engines.
- [AWS DataSync](../technologies/aws/aws-datasync.md): Online transfer service that copies files and objects between on-premises storage, other clouds and AWS storage with verification and incremental runs.
- [AWS IoT Core](../technologies/aws/aws-iot-core.md): Managed MQTT and HTTPS message broker that authenticates devices and routes their telemetry to other AWS services through rules.
- [AWS IoT SiteWise](../technologies/aws/aws-iot-sitewise.md): Service for collecting, modelling and storing industrial equipment telemetry as asset hierarchies with time-series properties.
- [AWS Snowball Edge](../technologies/aws/aws-snowball-edge.md) (deprecated): Rugged storage and compute device shipped to a site to load large datasets offline and return them to S3.
- [AWS Transfer Family](../technologies/aws/aws-transfer-family.md): Managed SFTP, FTPS, FTP and AS2 endpoints that store exchanged files directly in S3 or EFS.
- [AWS zero-ETL integrations](../technologies/aws/aws-zero-etl-integrations.md): Managed replication that keeps tables from AWS databases, self-managed databases and SaaS applications continuously in step in Amazon Redshift or the SageMaker lakehouse.

## Storage and table management

- [Amazon S3](../technologies/aws/aws-s3.md): Object storage service that holds files of any size in buckets and is the usual foundation for data lakes on AWS.
- [Amazon S3 Files](../technologies/aws/aws-s3-files.md): Presents an existing S3 bucket as a shared file system so file-based applications and agents can read and write the same data that S3 APIs see.
- [Amazon S3 storage classes and S3 Lifecycle](../technologies/aws/aws-s3-storage-classes-lifecycle.md): Set of S3 storage tiers from Standard to Glacier Deep Archive, with Intelligent-Tiering and lifecycle rules that move or expire objects by age.
- [Amazon S3 Tables](../technologies/aws/aws-s3-tables.md): S3 bucket type (table buckets) that stores Apache Iceberg tables and runs compaction, snapshot expiry and unreferenced-file removal automatically.
- [AWS Glue Data Catalog](../technologies/aws/aws-glue-data-catalog.md): Central metastore for databases, tables, schemas and partitions that AWS engines and external Iceberg clients use to find and govern data.

## Processing and transformation

- [Amazon Athena for Apache Spark](../technologies/aws/aws-athena-spark.md): Serverless, interactive Apache Spark sessions in Athena that start quickly and are billed per DPU-hour, used through notebooks, Spark Connect or APIs.
- [Amazon Bedrock Data Automation](../technologies/aws/aws-bedrock-data-automation.md): Generative AI service that turns documents, images, audio and video into structured fields, summaries and classifications through one API.
- [Amazon EMR on EC2](../technologies/aws/aws-emr-on-ec2.md): Managed clusters on EC2 that run Apache Spark, Hive, Trino, Flink, HBase and other open-source frameworks with versioned release labels.
- [Amazon EMR on EKS](../technologies/aws/aws-emr-on-eks.md): Runs EMR's Spark runtime as jobs on an existing Amazon EKS cluster so data processing shares Kubernetes capacity with other workloads.
- [Amazon EMR Serverless](../technologies/aws/aws-emr-serverless.md): Serverless option for running Spark and Hive jobs on the EMR runtime without sizing or managing clusters.
- [Amazon Managed Service for Apache Flink](../technologies/aws/aws-managed-flink.md): Managed runtime for Apache Flink applications in Java, Scala, Python or SQL, with checkpoints, scaling and a notebook-based Studio for interactive streaming SQL.
- [Amazon Textract](../technologies/aws/aws-textract.md): Extracts printed and handwritten text, tables, form fields and specific document types from scanned documents and images.
- [AWS Glue DataBrew](../technologies/aws/aws-glue-databrew.md): No-code visual tool for profiling, cleaning and reshaping datasets with more than 250 reusable transformation steps saved as recipes.
- [AWS Glue ETL](../technologies/aws/aws-glue-etl.md): Serverless Apache Spark and Python job service for extracting, transforming and loading data, with a visual editor in Glue Studio and native connectors.

## Orchestration

- [Amazon EventBridge](../technologies/aws/aws-eventbridge.md): Serverless event bus, scheduler and point-to-point pipes that route events from AWS services, SaaS partners and applications to targets by rule.
- [Amazon Managed Workflows for Apache Airflow](../technologies/aws/aws-mwaa.md): Managed Apache Airflow environments in your VPC that run Python DAGs with autoscaled workers and CloudWatch logging.
- [Amazon MWAA Serverless](../technologies/aws/aws-mwaa-serverless.md): Deployment option for Amazon MWAA that runs Airflow 3 workflows defined in YAML without a standing environment, charging only for task run time.
- [AWS Step Functions](../technologies/aws/aws-step-functions.md): Serverless state-machine service that coordinates AWS service calls, Lambda functions and human approvals with retries and error handling.

## Query and compute

- [Amazon Athena](../technologies/aws/aws-athena.md): Serverless Trino-based SQL engine that queries data in S3 and other sources through the Glue Data Catalog, billed per data scanned or per reserved capacity.
- [Amazon Redshift](../technologies/aws/aws-redshift.md): Massively parallel columnar data warehouse, offered as provisioned RA3 clusters with Redshift Managed Storage or as Redshift Serverless.
- [Amazon Redshift concurrency scaling](../technologies/aws/aws-redshift-concurrency-scaling.md): Adds transient compute automatically when queries queue on a Redshift warehouse and removes it when load drops.
- [Amazon Redshift federated query](../technologies/aws/aws-redshift-federated-query.md): Queries live data in Aurora and RDS PostgreSQL and MySQL databases from Redshift SQL without loading it first.
- [Amazon Redshift materialized views](../technologies/aws/aws-redshift-materialized-views.md): Precomputed query results in Redshift that refresh incrementally where possible and can be used automatically to rewrite matching queries.
- [Amazon Redshift Serverless](../technologies/aws/aws-redshift-serverless.md): Deployment option for Redshift that allocates compute in RPUs automatically, scales with load and charges only while queries run.
- [Amazon Redshift Spectrum](../technologies/aws/aws-redshift-spectrum.md): Lets Redshift query and join open-format files and Iceberg tables in S3 through external schemas in the Glue Data Catalog.
- [AWS Glue Data Catalog materialized views](../technologies/aws/aws-glue-materialized-views.md): Iceberg-based materialised views defined in the Glue Data Catalog that store query results and refresh on a schedule, fully or incrementally.
- [Lakehouse architecture of Amazon SageMaker](../technologies/aws/aws-sagemaker-lakehouse.md): Logical layer that organises S3, S3 Tables and Redshift Managed Storage into catalogues, and mounts other sources as federated catalogues, all queryable through Iceberg-compatible engines.

## Serving and activation

- [Amazon Aurora](../technologies/aws/aws-aurora.md): MySQL- and PostgreSQL-compatible relational database with distributed storage, read replicas, global databases and copy-on-write cloning.
- [Amazon DynamoDB](../technologies/aws/aws-dynamodb.md): Serverless key-value and document database with single-digit millisecond reads and writes, which partitions data automatically as tables grow.

## Analytics and BI

- [Amazon Quick Sight](../technologies/aws/aws-quick-sight.md): Serverless BI for building interactive dashboards, pixel-perfect paginated reports and embedded analytics, with natural-language questions over curated topics.

## Machine learning development

- [Amazon Redshift ML](../technologies/aws/aws-redshift-ml.md): Trains and runs machine learning models from Redshift SQL with CREATE MODEL, using SageMaker AI for training and Bedrock models for text tasks.
- [Amazon SageMaker AI training jobs](../technologies/aws/aws-sagemaker-training.md): Managed, ephemeral training jobs that run containers on CPU, GPU or Trainium instances, with distributed training libraries and automatic model tuning.
- [Amazon SageMaker AI with MLflow](../technologies/aws/aws-sagemaker-mlflow.md): Managed MLflow, provided as serverless MLflow Apps, for tracking experiments, comparing runs and tracing generative AI applications.
- [Amazon SageMaker Autopilot](../technologies/aws/aws-sagemaker-autopilot.md): AutoML API that explores feature processing, algorithms and hyperparameters to produce ranked candidate models for tabular, text, image and time-series tasks.
- [Amazon SageMaker Canvas](../technologies/aws/aws-sagemaker-canvas.md): No-code ML workspace where analysts prepare data, build and evaluate models automatically, and generate predictions.
- [Amazon SageMaker Clarify](../technologies/aws/aws-sagemaker-clarify.md) (deprecated): Processing jobs that compute pre- and post-training bias metrics and SHAP feature attributions for models and datasets.
- [Amazon SageMaker Feature Store](../technologies/aws/aws-sagemaker-feature-store.md): Feature repository with an online store holding the latest values for low-latency lookup and an append-only offline store in S3 for training.
- [Amazon SageMaker Ground Truth](../technologies/aws/aws-sagemaker-ground-truth.md) (deprecated): Labelling service that runs annotation jobs for images, text, video and point clouds using private, vendor or automated workforces.
- [Amazon SageMaker HyperPod](../technologies/aws/aws-sagemaker-hyperpod.md): Persistent, self-healing accelerator clusters orchestrated by Slurm or Amazon EKS for large-scale model training, fine-tuning and inference.
- [Amazon SageMaker Model Registry](../technologies/aws/aws-sagemaker-model-registry.md): Catalogue of versioned model packages grouped by use case, with approval status, metadata, lineage and Model Cards for documentation.
- [Amazon SageMaker Pipelines](../technologies/aws/aws-sagemaker-pipelines.md): Serverless workflow service for ML steps such as processing, training, evaluation, registration and deployment, defined in Python.

## ML operations

- [Amazon SageMaker AI inference](../technologies/aws/aws-sagemaker-inference.md): Model hosting options covering real-time, serverless and asynchronous endpoints and batch transform jobs, with traffic-shifting deployment controls.
- [Amazon SageMaker Model Monitor](../technologies/aws/aws-sagemaker-model-monitor.md) (deprecated): Scheduled jobs that compare captured endpoint traffic with a baseline to report data quality, model quality, bias and attribution drift.

## Generative AI

- [Amazon Bedrock](../technologies/aws/aws-bedrock.md): Managed API for invoking foundation models from Amazon and third parties, with on-demand, batch, cross-Region and provisioned inference options.
- [Amazon Bedrock AgentCore](../technologies/aws/aws-bedrock-agentcore.md): Platform for hosting and operating AI agents built with any framework or model, providing isolated runtime sessions, memory, identity, code and browser tools and tracing.
- [Amazon Bedrock AgentCore Evaluations](../technologies/aws/aws-bedrock-agentcore-evaluations.md): Scores agent sessions, traces and tool calls with built-in, third-party or custom evaluators, online or in batch, and supports A/B tests between agent versions.
- [Amazon Bedrock AgentCore Gateway](../technologies/aws/aws-bedrock-agentcore-gateway.md): Managed MCP endpoint that turns APIs, Lambda functions and existing MCP servers into governed agent tools and can front model providers with rate and token limits.
- [Amazon Bedrock AgentCore Policy](../technologies/aws/aws-bedrock-agentcore-policy.md): Deterministic rules, written in natural language or a Cedar-compatible language, that decide which tools an agent may call and with which parameters.
- [Amazon Bedrock Agents Classic](../technologies/aws/aws-bedrock-agents-classic.md) (deprecated): Original configuration-based Bedrock agent service that orchestrates a model with action groups and knowledge bases.
- [Amazon Bedrock custom models](../technologies/aws/aws-bedrock-model-customization.md): Adapts supported foundation models with fine-tuning, continued pre-training or distillation, and imports externally trained weights for serving.
- [Amazon Bedrock Evaluations](../technologies/aws/aws-bedrock-evaluations.md): Evaluation jobs that score models and RAG sources against built-in or custom datasets using metrics, LLM-as-a-judge or human reviewers.
- [Amazon Bedrock Guardrails](../technologies/aws/aws-bedrock-guardrails.md): Configurable filters that check model inputs and outputs for harmful content, denied topics, banned words, personal data, ungrounded answers and rule violations.
- [Amazon Bedrock Knowledge Bases](../technologies/aws/aws-bedrock-knowledge-bases.md): Managed retrieval-augmented generation that ingests content, parses and chunks it, embeds and indexes it, and retrieves relevant passages with citations.
- [Amazon Bedrock Prompt management](../technologies/aws/aws-bedrock-prompt-management.md): Library for storing prompts with variables, model settings and variants, saving immutable versions and optimising prompts for a chosen model.
- [Amazon Q Business](../technologies/aws/aws-q-business.md) (deprecated): Generative AI assistant for employees that answered questions and ran Q Apps over indexed enterprise content.
- [Amazon Quick](../technologies/aws/aws-quick.md): Workplace AI service combining chat agents, deep research, workflow automation, BI and generated apps over company data and connected applications.
- [Amazon S3 Vectors](../technologies/aws/aws-s3-vectors.md): S3 bucket type (vector buckets) that stores embeddings in vector indexes and answers similarity queries with metadata filters, without provisioned infrastructure.
- [Amazon SageMaker JumpStart](../technologies/aws/aws-sagemaker-jumpstart.md): Hub of open-weight and proprietary foundation models and solution templates that can be fine-tuned and deployed to SageMaker AI endpoints in your account.
- [AWS Agent Registry](../technologies/aws/aws-agent-registry.md): Private, governed catalogue of agents, tools, skills and MCP servers that people and agents can search through the console, APIs or an MCP endpoint.

## Metadata and discovery

- [Amazon S3 Metadata](../technologies/aws/aws-s3-metadata.md): Captures object metadata for a general purpose bucket into read-only, S3-managed Iceberg tables (journal, live inventory and annotation tables) that can be queried with SQL.
- [Amazon SageMaker Catalog](../technologies/aws/aws-sagemaker-catalog.md): Business data catalogue in SageMaker Unified Studio where producers publish assets and data products with glossary terms and metadata forms, and consumers search and subscribe.
- [Amazon SageMaker Catalog data lineage](../technologies/aws/aws-sagemaker-catalog-lineage.md): OpenLineage-compatible lineage graph that records how catalogued assets are produced and consumed, captured automatically from supported connections and tools or posted through APIs.
- [AWS Glue Schema Registry](../technologies/aws/aws-glue-schema-registry.md): Registry of versioned Avro, JSON Schema and Protobuf schemas that Kafka, Kinesis and Flink clients use to serialise data and check compatibility.

## Data quality and observability

- [AWS Glue Data Quality](../technologies/aws/aws-glue-data-quality.md): Rule engine built on Deequ that evaluates DQDL rulesets on catalogue tables or inside Glue jobs, recommends rules and flags statistical anomalies.

## Master and reference data

- [AWS Entity Resolution](../technologies/aws/aws-entity-resolution.md): Matches and links records that describe the same person or business using rules, machine learning or licensed provider data, and maintains match IDs.

## Governance and compliance

- [Amazon Comprehend](../technologies/aws/aws-comprehend.md): Natural language processing API that detects entities, key phrases, sentiment, language and personal data in text, with custom classifiers.
- [Amazon Macie](../technologies/aws/aws-macie.md): Samples and scans S3 objects with managed and custom identifiers to find personal and sensitive data, and evaluates bucket access settings.
- [AWS Config](../technologies/aws/aws-config.md): Records resource configurations over time and evaluates them against managed or custom rules and conformance packs.

## Security and access

- [Amazon Redshift row-level security and dynamic data masking](../technologies/aws/aws-redshift-fine-grained-security.md): Redshift policies that filter rows and mask column values per role at query time, alongside role-based SQL permissions.
- [AWS CloudTrail](../technologies/aws/aws-cloudtrail.md): Records API calls and data-access events across an account or organisation to S3 and CloudWatch Logs, with integrity validation.
- [AWS IAM Identity Center](../technologies/aws/aws-iam-identity-center.md): Workforce single sign-on that federates an external identity provider and propagates the user's identity to data services for per-user authorisation and auditing.
- [AWS Identity and Access Management](../technologies/aws/aws-iam.md): Account-wide service that authenticates principals with short-lived role credentials and authorises every AWS API call through JSON policies.
- [AWS Key Management Service](../technologies/aws/aws-kms.md): Managed service for creating, rotating and controlling encryption keys used by AWS services and applications.
- [AWS Lake Formation](../technologies/aws/aws-lake-formation.md): Permission layer over the Glue Data Catalog that grants database, table, column, row and cell access and shares data across accounts.
- [AWS PrivateLink](../technologies/aws/aws-privatelink.md): Interface VPC endpoints that let workloads reach AWS and partner services over private IP addresses without crossing the internet.
- [AWS Secrets Manager](../technologies/aws/aws-secrets-manager.md): Stores database credentials, API keys and tokens encrypted with KMS and rotates them on a schedule.

## Data sharing and collaboration

- [Amazon Redshift data sharing](../technologies/aws/aws-redshift-data-sharing.md): Shares live tables and views between Redshift warehouses in the same or other accounts and Regions without copying, so separate compute can read the same data.
- [AWS Clean Rooms](../technologies/aws/aws-clean-rooms.md): Collaboration service in which organisations run approved SQL or PySpark analyses and ML on combined data without exposing each other's raw records.
- [AWS Data Exchange](../technologies/aws/aws-data-exchange.md): Marketplace for finding, subscribing to and publishing third-party datasets as files, APIs, Redshift data shares, Lake Formation tables or S3 access.

## Development and DataOps

- [Amazon SageMaker Data Agent](../technologies/aws/aws-sagemaker-data-agent.md): AI assistant in SageMaker Unified Studio notebooks and the query editor that writes SQL and code from natural language, explains its plan and fixes failed queries.
- [Amazon SageMaker Studio](../technologies/aws/aws-sagemaker-studio.md): Web-based ML development environment in SageMaker AI offering JupyterLab, Code Editor and RStudio spaces with managed compute.
- [Amazon SageMaker Unified Studio](../technologies/aws/aws-sagemaker-unified-studio.md): Browser-based workbench that brings SQL querying, notebooks, visual ETL, workflows, ML and Bedrock tools together in domains and projects with shared permissions.
- [AWS CodePipeline](../technologies/aws/aws-codepipeline.md): Continuous delivery service that builds, tests and deploys code and infrastructure through staged pipelines with approvals.
- [Kiro](../technologies/aws/aws-kiro.md): AWS agentic IDE and command-line tool for spec-driven development, with chat, code generation and MCP support.

## Platform operations

- [Amazon CloudWatch](../technologies/aws/aws-cloudwatch.md): Collects metrics, logs and traces from AWS services and applications, with alarms, dashboards, anomaly detection and log queries.
- [AWS Backup](../technologies/aws/aws-backup.md): Central policy-based backup for AWS services such as S3, DynamoDB, Aurora, RDS, Redshift and EFS, with cross-Region and cross-account copies.
- [AWS Budgets](../technologies/aws/aws-budgets.md): Sets cost and usage budgets with alerts and optional actions that apply restrictive policies or stop resources when limits are reached.
- [AWS Cloud Development Kit](../technologies/aws/aws-cdk.md): Open-source framework for defining AWS infrastructure in TypeScript, Python, Java, C# or Go that synthesises CloudFormation templates.
- [AWS CloudFormation](../technologies/aws/aws-cloudformation.md): Provisions and updates AWS resources from declarative JSON or YAML templates as versioned stacks.
- [AWS Cost Explorer](../technologies/aws/aws-cost-explorer.md): Interactive tool for analysing spend and usage by service, account and cost allocation tag, with forecasts and rightsizing recommendations.
- [AWS Data Exports](../technologies/aws/aws-data-exports.md): Delivers billing, cost optimisation and carbon emissions data to S3 on a schedule as CUR 2.0 or FOCUS tables, with SQL column selection.
- [AWS Outposts](../technologies/aws/aws-outposts.md): AWS-managed racks and servers installed on premises that run a subset of AWS services locally.
- [AWS Transform](../technologies/aws/aws-transform.md): Agentic AI service that plans and carries out migration and modernisation work for mainframe, VMware and .NET workloads.

## Specialised data types

- [Amazon Kendra](../technologies/aws/aws-kendra.md) (deprecated): Enterprise search service that indexes documents from many connectors and returns ranked, permission-filtered results.
- [Amazon Location Service](../technologies/aws/aws-location-service.md): APIs for maps, geocoding, place search, routing, geofencing and device tracking.
- [Amazon Neptune](../technologies/aws/aws-neptune.md): Managed graph database for property graphs (Gremlin, openCypher) and RDF (SPARQL) with read replicas and global databases.
- [Amazon Neptune Analytics](../technologies/aws/aws-neptune-analytics.md): In-memory graph analytics engine that loads graphs from Neptune or S3 and runs graph algorithms, openCypher queries and vector similarity search.
- [Amazon OpenSearch Service](../technologies/aws/aws-opensearch-service.md): Managed OpenSearch for full-text search, log analytics and vector search, available as provisioned domains or OpenSearch Serverless collections.
- [Amazon Timestream for InfluxDB](../technologies/aws/aws-timestream-influxdb.md): Managed InfluxDB instances for storing and querying time-stamped measurements with Multi-AZ failover.
- [Amazon Timestream for LiveAnalytics](../technologies/aws/aws-timestream-liveanalytics.md) (deprecated): Serverless time-series database with memory and magnetic tiers and SQL time-series functions.

