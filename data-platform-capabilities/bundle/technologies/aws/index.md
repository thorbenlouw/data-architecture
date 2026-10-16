# Amazon Web Services

# Ingestion and integration

* [Amazon AppFlow](aws-appflow.md) - No-code service that moves data on demand, on schedule or on event between SaaS applications and AWS services.
* [Amazon Data Firehose](aws-data-firehose.md) - Managed delivery stream that buffers events, optionally transforms them, and writes them to S3, Iceberg tables, Redshift, OpenSearch, Splunk or HTTP endpoints.
* [Amazon Kinesis Data Streams](aws-kinesis-data-streams.md) - Serverless, sharded event stream that stores ordered records for up to 365 days and lets many consumers read them independently.
* [Amazon Managed Streaming for Apache Kafka](aws-msk.md) - Managed Apache Kafka offering provisioned clusters with Standard or Express brokers and a serverless option.
* [Amazon Redshift auto-copy](aws-redshift-auto-copy.md) - COPY jobs that watch an S3 prefix and load each new file into a Redshift table once, as it arrives.
* [Amazon Redshift streaming ingestion](aws-redshift-streaming-ingestion.md) - Reads Kinesis Data Streams and Kafka topics directly into Redshift materialised views with seconds-level latency, without staging in S3.
* [AWS Database Migration Service](aws-dms.md) - Service that copies data between databases with a full load followed by ongoing change capture from transaction logs, and converts schemas between engines.
* [AWS DataSync](aws-datasync.md) - Online transfer service that copies files and objects between on-premises storage, other clouds and AWS storage with verification and incremental runs.
* [AWS IoT Core](aws-iot-core.md) - Managed MQTT and HTTPS message broker that authenticates devices and routes their telemetry to other AWS services through rules.
* [AWS IoT SiteWise](aws-iot-sitewise.md) - Service for collecting, modelling and storing industrial equipment telemetry as asset hierarchies with time-series properties.
* [AWS Snowball Edge](aws-snowball-edge.md) (deprecated) - Rugged storage and compute device shipped to a site to load large datasets offline and return them to S3.
* [AWS Transfer Family](aws-transfer-family.md) - Managed SFTP, FTPS, FTP and AS2 endpoints that store exchanged files directly in S3 or EFS.
* [AWS zero-ETL integrations](aws-zero-etl-integrations.md) - Managed replication that keeps tables from AWS databases, self-managed databases and SaaS applications continuously in step in Amazon Redshift or the SageMaker lakehouse.

# Storage and table management

* [Amazon S3](aws-s3.md) - Object storage service that holds files of any size in buckets and is the usual foundation for data lakes on AWS.
* [Amazon S3 Files](aws-s3-files.md) - Presents an existing S3 bucket as a shared file system so file-based applications and agents can read and write the same data that S3 APIs see.
* [Amazon S3 storage classes and S3 Lifecycle](aws-s3-storage-classes-lifecycle.md) - Set of S3 storage tiers from Standard to Glacier Deep Archive, with Intelligent-Tiering and lifecycle rules that move or expire objects by age.
* [Amazon S3 Tables](aws-s3-tables.md) - S3 bucket type (table buckets) that stores Apache Iceberg tables and runs compaction, snapshot expiry and unreferenced-file removal automatically.
* [AWS Glue Data Catalog](aws-glue-data-catalog.md) - Central metastore for databases, tables, schemas and partitions that AWS engines and external Iceberg clients use to find and govern data.

# Processing and transformation

* [Amazon Athena for Apache Spark](aws-athena-spark.md) - Serverless, interactive Apache Spark sessions in Athena that start quickly and are billed per DPU-hour, used through notebooks, Spark Connect or APIs.
* [Amazon Bedrock Data Automation](aws-bedrock-data-automation.md) - Generative AI service that turns documents, images, audio and video into structured fields, summaries and classifications through one API.
* [Amazon EMR on EC2](aws-emr-on-ec2.md) - Managed clusters on EC2 that run Apache Spark, Hive, Trino, Flink, HBase and other open-source frameworks with versioned release labels.
* [Amazon EMR on EKS](aws-emr-on-eks.md) - Runs EMR's Spark runtime as jobs on an existing Amazon EKS cluster so data processing shares Kubernetes capacity with other workloads.
* [Amazon EMR Serverless](aws-emr-serverless.md) - Serverless option for running Spark and Hive jobs on the EMR runtime without sizing or managing clusters.
* [Amazon Managed Service for Apache Flink](aws-managed-flink.md) - Managed runtime for Apache Flink applications in Java, Scala, Python or SQL, with checkpoints, scaling and a notebook-based Studio for interactive streaming SQL.
* [Amazon Textract](aws-textract.md) - Extracts printed and handwritten text, tables, form fields and specific document types from scanned documents and images.
* [AWS Glue DataBrew](aws-glue-databrew.md) - No-code visual tool for profiling, cleaning and reshaping datasets with more than 250 reusable transformation steps saved as recipes.
* [AWS Glue ETL](aws-glue-etl.md) - Serverless Apache Spark and Python job service for extracting, transforming and loading data, with a visual editor in Glue Studio and native connectors.

# Orchestration

* [Amazon EventBridge](aws-eventbridge.md) - Serverless event bus, scheduler and point-to-point pipes that route events from AWS services, SaaS partners and applications to targets by rule.
* [Amazon Managed Workflows for Apache Airflow](aws-mwaa.md) - Managed Apache Airflow environments in your VPC that run Python DAGs with autoscaled workers and CloudWatch logging.
* [Amazon MWAA Serverless](aws-mwaa-serverless.md) - Deployment option for Amazon MWAA that runs Airflow 3 workflows defined in YAML without a standing environment, charging only for task run time.
* [AWS Step Functions](aws-step-functions.md) - Serverless state-machine service that coordinates AWS service calls, Lambda functions and human approvals with retries and error handling.

# Query and compute

* [Amazon Athena](aws-athena.md) - Serverless Trino-based SQL engine that queries data in S3 and other sources through the Glue Data Catalog, billed per data scanned or per reserved capacity.
* [Amazon Redshift](aws-redshift.md) - Massively parallel columnar data warehouse, offered as provisioned RA3 clusters with Redshift Managed Storage or as Redshift Serverless.
* [Amazon Redshift concurrency scaling](aws-redshift-concurrency-scaling.md) - Adds transient compute automatically when queries queue on a Redshift warehouse and removes it when load drops.
* [Amazon Redshift federated query](aws-redshift-federated-query.md) - Queries live data in Aurora and RDS PostgreSQL and MySQL databases from Redshift SQL without loading it first.
* [Amazon Redshift materialized views](aws-redshift-materialized-views.md) - Precomputed query results in Redshift that refresh incrementally where possible and can be used automatically to rewrite matching queries.
* [Amazon Redshift Serverless](aws-redshift-serverless.md) - Deployment option for Redshift that allocates compute in RPUs automatically, scales with load and charges only while queries run.
* [Amazon Redshift Spectrum](aws-redshift-spectrum.md) - Lets Redshift query and join open-format files and Iceberg tables in S3 through external schemas in the Glue Data Catalog.
* [AWS Glue Data Catalog materialized views](aws-glue-materialized-views.md) - Iceberg-based materialised views defined in the Glue Data Catalog that store query results and refresh on a schedule, fully or incrementally.
* [Lakehouse architecture of Amazon SageMaker](aws-sagemaker-lakehouse.md) - Logical layer that organises S3, S3 Tables and Redshift Managed Storage into catalogues, and mounts other sources as federated catalogues, all queryable through Iceberg-compatible engines.

# Serving and activation

* [Amazon Aurora](aws-aurora.md) - MySQL- and PostgreSQL-compatible relational database with distributed storage, read replicas, global databases and copy-on-write cloning.
* [Amazon DynamoDB](aws-dynamodb.md) - Serverless key-value and document database with single-digit millisecond reads and writes, which partitions data automatically as tables grow.

# Analytics and BI

* [Amazon Quick Sight](aws-quick-sight.md) - Serverless BI for building interactive dashboards, pixel-perfect paginated reports and embedded analytics, with natural-language questions over curated topics.

# Machine learning development

* [Amazon Redshift ML](aws-redshift-ml.md) - Trains and runs machine learning models from Redshift SQL with CREATE MODEL, using SageMaker AI for training and Bedrock models for text tasks.
* [Amazon SageMaker AI training jobs](aws-sagemaker-training.md) - Managed, ephemeral training jobs that run containers on CPU, GPU or Trainium instances, with distributed training libraries and automatic model tuning.
* [Amazon SageMaker AI with MLflow](aws-sagemaker-mlflow.md) - Managed MLflow, provided as serverless MLflow Apps, for tracking experiments, comparing runs and tracing generative AI applications.
* [Amazon SageMaker Autopilot](aws-sagemaker-autopilot.md) - AutoML API that explores feature processing, algorithms and hyperparameters to produce ranked candidate models for tabular, text, image and time-series tasks.
* [Amazon SageMaker Canvas](aws-sagemaker-canvas.md) - No-code ML workspace where analysts prepare data, build and evaluate models automatically, and generate predictions.
* [Amazon SageMaker Clarify](aws-sagemaker-clarify.md) (deprecated) - Processing jobs that compute pre- and post-training bias metrics and SHAP feature attributions for models and datasets.
* [Amazon SageMaker Feature Store](aws-sagemaker-feature-store.md) - Feature repository with an online store holding the latest values for low-latency lookup and an append-only offline store in S3 for training.
* [Amazon SageMaker Ground Truth](aws-sagemaker-ground-truth.md) (deprecated) - Labelling service that runs annotation jobs for images, text, video and point clouds using private, vendor or automated workforces.
* [Amazon SageMaker HyperPod](aws-sagemaker-hyperpod.md) - Persistent, self-healing accelerator clusters orchestrated by Slurm or Amazon EKS for large-scale model training, fine-tuning and inference.
* [Amazon SageMaker Model Registry](aws-sagemaker-model-registry.md) - Catalogue of versioned model packages grouped by use case, with approval status, metadata, lineage and Model Cards for documentation.
* [Amazon SageMaker Pipelines](aws-sagemaker-pipelines.md) - Serverless workflow service for ML steps such as processing, training, evaluation, registration and deployment, defined in Python.

# ML operations

* [Amazon SageMaker AI inference](aws-sagemaker-inference.md) - Model hosting options covering real-time, serverless and asynchronous endpoints and batch transform jobs, with traffic-shifting deployment controls.
* [Amazon SageMaker Model Monitor](aws-sagemaker-model-monitor.md) (deprecated) - Scheduled jobs that compare captured endpoint traffic with a baseline to report data quality, model quality, bias and attribution drift.

# Generative AI

* [Amazon Bedrock](aws-bedrock.md) - Managed API for invoking foundation models from Amazon and third parties, with on-demand, batch, cross-Region and provisioned inference options.
* [Amazon Bedrock AgentCore](aws-bedrock-agentcore.md) - Platform for hosting and operating AI agents built with any framework or model, providing isolated runtime sessions, memory, identity, code and browser tools and tracing.
* [Amazon Bedrock AgentCore Evaluations](aws-bedrock-agentcore-evaluations.md) - Scores agent sessions, traces and tool calls with built-in, third-party or custom evaluators, online or in batch, and supports A/B tests between agent versions.
* [Amazon Bedrock AgentCore Gateway](aws-bedrock-agentcore-gateway.md) - Managed MCP endpoint that turns APIs, Lambda functions and existing MCP servers into governed agent tools and can front model providers with rate and token limits.
* [Amazon Bedrock AgentCore Policy](aws-bedrock-agentcore-policy.md) - Deterministic rules, written in natural language or a Cedar-compatible language, that decide which tools an agent may call and with which parameters.
* [Amazon Bedrock Agents Classic](aws-bedrock-agents-classic.md) (deprecated) - Original configuration-based Bedrock agent service that orchestrates a model with action groups and knowledge bases.
* [Amazon Bedrock custom models](aws-bedrock-model-customization.md) - Adapts supported foundation models with fine-tuning, continued pre-training or distillation, and imports externally trained weights for serving.
* [Amazon Bedrock Evaluations](aws-bedrock-evaluations.md) - Evaluation jobs that score models and RAG sources against built-in or custom datasets using metrics, LLM-as-a-judge or human reviewers.
* [Amazon Bedrock Guardrails](aws-bedrock-guardrails.md) - Configurable filters that check model inputs and outputs for harmful content, denied topics, banned words, personal data, ungrounded answers and rule violations.
* [Amazon Bedrock Knowledge Bases](aws-bedrock-knowledge-bases.md) - Managed retrieval-augmented generation that ingests content, parses and chunks it, embeds and indexes it, and retrieves relevant passages with citations.
* [Amazon Bedrock Prompt management](aws-bedrock-prompt-management.md) - Library for storing prompts with variables, model settings and variants, saving immutable versions and optimising prompts for a chosen model.
* [Amazon Q Business](aws-q-business.md) (deprecated) - Generative AI assistant for employees that answered questions and ran Q Apps over indexed enterprise content.
* [Amazon Quick](aws-quick.md) - Workplace AI service combining chat agents, deep research, workflow automation, BI and generated apps over company data and connected applications.
* [Amazon S3 Vectors](aws-s3-vectors.md) - S3 bucket type (vector buckets) that stores embeddings in vector indexes and answers similarity queries with metadata filters, without provisioned infrastructure.
* [Amazon SageMaker JumpStart](aws-sagemaker-jumpstart.md) - Hub of open-weight and proprietary foundation models and solution templates that can be fine-tuned and deployed to SageMaker AI endpoints in your account.
* [AWS Agent Registry](aws-agent-registry.md) - Private, governed catalogue of agents, tools, skills and MCP servers that people and agents can search through the console, APIs or an MCP endpoint.

# Metadata and discovery

* [Amazon S3 Metadata](aws-s3-metadata.md) - Captures object metadata for a general purpose bucket into read-only, S3-managed Iceberg tables (journal, live inventory and annotation tables) that can be queried with SQL.
* [Amazon SageMaker Catalog](aws-sagemaker-catalog.md) - Business data catalogue in SageMaker Unified Studio where producers publish assets and data products with glossary terms and metadata forms, and consumers search and subscribe.
* [Amazon SageMaker Catalog data lineage](aws-sagemaker-catalog-lineage.md) - OpenLineage-compatible lineage graph that records how catalogued assets are produced and consumed, captured automatically from supported connections and tools or posted through APIs.
* [AWS Glue Schema Registry](aws-glue-schema-registry.md) - Registry of versioned Avro, JSON Schema and Protobuf schemas that Kafka, Kinesis and Flink clients use to serialise data and check compatibility.

# Data quality and observability

* [AWS Glue Data Quality](aws-glue-data-quality.md) - Rule engine built on Deequ that evaluates DQDL rulesets on catalogue tables or inside Glue jobs, recommends rules and flags statistical anomalies.

# Master and reference data

* [AWS Entity Resolution](aws-entity-resolution.md) - Matches and links records that describe the same person or business using rules, machine learning or licensed provider data, and maintains match IDs.

# Governance and compliance

* [Amazon Comprehend](aws-comprehend.md) - Natural language processing API that detects entities, key phrases, sentiment, language and personal data in text, with custom classifiers.
* [Amazon Macie](aws-macie.md) - Samples and scans S3 objects with managed and custom identifiers to find personal and sensitive data, and evaluates bucket access settings.
* [AWS Config](aws-config.md) - Records resource configurations over time and evaluates them against managed or custom rules and conformance packs.

# Security and access

* [Amazon Redshift row-level security and dynamic data masking](aws-redshift-fine-grained-security.md) - Redshift policies that filter rows and mask column values per role at query time, alongside role-based SQL permissions.
* [AWS CloudTrail](aws-cloudtrail.md) - Records API calls and data-access events across an account or organisation to S3 and CloudWatch Logs, with integrity validation.
* [AWS IAM Identity Center](aws-iam-identity-center.md) - Workforce single sign-on that federates an external identity provider and propagates the user's identity to data services for per-user authorisation and auditing.
* [AWS Identity and Access Management](aws-iam.md) - Account-wide service that authenticates principals with short-lived role credentials and authorises every AWS API call through JSON policies.
* [AWS Key Management Service](aws-kms.md) - Managed service for creating, rotating and controlling encryption keys used by AWS services and applications.
* [AWS Lake Formation](aws-lake-formation.md) - Permission layer over the Glue Data Catalog that grants database, table, column, row and cell access and shares data across accounts.
* [AWS PrivateLink](aws-privatelink.md) - Interface VPC endpoints that let workloads reach AWS and partner services over private IP addresses without crossing the internet.
* [AWS Secrets Manager](aws-secrets-manager.md) - Stores database credentials, API keys and tokens encrypted with KMS and rotates them on a schedule.

# Data sharing and collaboration

* [Amazon Redshift data sharing](aws-redshift-data-sharing.md) - Shares live tables and views between Redshift warehouses in the same or other accounts and Regions without copying, so separate compute can read the same data.
* [AWS Clean Rooms](aws-clean-rooms.md) - Collaboration service in which organisations run approved SQL or PySpark analyses and ML on combined data without exposing each other's raw records.
* [AWS Data Exchange](aws-data-exchange.md) - Marketplace for finding, subscribing to and publishing third-party datasets as files, APIs, Redshift data shares, Lake Formation tables or S3 access.

# Development and DataOps

* [Amazon SageMaker Data Agent](aws-sagemaker-data-agent.md) - AI assistant in SageMaker Unified Studio notebooks and the query editor that writes SQL and code from natural language, explains its plan and fixes failed queries.
* [Amazon SageMaker Studio](aws-sagemaker-studio.md) - Web-based ML development environment in SageMaker AI offering JupyterLab, Code Editor and RStudio spaces with managed compute.
* [Amazon SageMaker Unified Studio](aws-sagemaker-unified-studio.md) - Browser-based workbench that brings SQL querying, notebooks, visual ETL, workflows, ML and Bedrock tools together in domains and projects with shared permissions.
* [AWS CodePipeline](aws-codepipeline.md) - Continuous delivery service that builds, tests and deploys code and infrastructure through staged pipelines with approvals.
* [Kiro](aws-kiro.md) - AWS agentic IDE and command-line tool for spec-driven development, with chat, code generation and MCP support.

# Platform operations

* [Amazon CloudWatch](aws-cloudwatch.md) - Collects metrics, logs and traces from AWS services and applications, with alarms, dashboards, anomaly detection and log queries.
* [AWS Backup](aws-backup.md) - Central policy-based backup for AWS services such as S3, DynamoDB, Aurora, RDS, Redshift and EFS, with cross-Region and cross-account copies.
* [AWS Budgets](aws-budgets.md) - Sets cost and usage budgets with alerts and optional actions that apply restrictive policies or stop resources when limits are reached.
* [AWS Cloud Development Kit](aws-cdk.md) - Open-source framework for defining AWS infrastructure in TypeScript, Python, Java, C# or Go that synthesises CloudFormation templates.
* [AWS CloudFormation](aws-cloudformation.md) - Provisions and updates AWS resources from declarative JSON or YAML templates as versioned stacks.
* [AWS Cost Explorer](aws-cost-explorer.md) - Interactive tool for analysing spend and usage by service, account and cost allocation tag, with forecasts and rightsizing recommendations.
* [AWS Data Exports](aws-data-exports.md) - Delivers billing, cost optimisation and carbon emissions data to S3 on a schedule as CUR 2.0 or FOCUS tables, with SQL column selection.
* [AWS Outposts](aws-outposts.md) - AWS-managed racks and servers installed on premises that run a subset of AWS services locally.
* [AWS Transform](aws-transform.md) - Agentic AI service that plans and carries out migration and modernisation work for mainframe, VMware and .NET workloads.

# Specialised data types

* [Amazon Kendra](aws-kendra.md) (deprecated) - Enterprise search service that indexes documents from many connectors and returns ranked, permission-filtered results.
* [Amazon Location Service](aws-location-service.md) - APIs for maps, geocoding, place search, routing, geofencing and device tracking.
* [Amazon Neptune](aws-neptune.md) - Managed graph database for property graphs (Gremlin, openCypher) and RDF (SPARQL) with read replicas and global databases.
* [Amazon Neptune Analytics](aws-neptune-analytics.md) - In-memory graph analytics engine that loads graphs from Neptune or S3 and runs graph algorithms, openCypher queries and vector similarity search.
* [Amazon OpenSearch Service](aws-opensearch-service.md) - Managed OpenSearch for full-text search, log analytics and vector search, available as provisioned domains or OpenSearch Serverless collections.
* [Amazon Timestream for InfluxDB](aws-timestream-influxdb.md) - Managed InfluxDB instances for storing and querying time-stamped measurements with Multi-AZ failover.
* [Amazon Timestream for LiveAnalytics](aws-timestream-liveanalytics.md) (deprecated) - Serverless time-series database with memory and magnetic tiers and SQL time-series functions.
