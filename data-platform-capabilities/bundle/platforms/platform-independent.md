---
type: Platform
id: platform-independent
title: Independent vendors
description: Commercial tools from vendors that work across platforms rather than offering a complete platform.
folder: independent
order: 15
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Commercial products from vendors that work across clouds and data platforms rather than offering a complete platform of their own. Most run on top of a customer's warehouse, lakehouse or cloud account and connect to several platforms at once. They cover ingestion and integration (Fivetran, Airbyte Cloud, Estuary, Qlik Talend Cloud, Matillion, Boomi, MuleSoft, Striim, Redpanda), transformation and orchestration (dbt platform, Coalesce, Astronomer Astro, Dagster+, Prefect Cloud), query, serving and search engines (Starburst, Dremio, MotherDuck, Materialize, Tinybird, StarTree, Imply, Denodo, MongoDB Atlas, Redis, Neo4j, Pinecone, Weaviate, Elastic), BI and semantic layers (Tableau, Qlik, ThoughtSpot, Sigma, Omni, Hex, Domo, Sisense, Cube, AtScale) and customer data activation (Hightouch, Twilio Segment, mParticle, Fivetran Activations).

The rest govern and assure data and AI: catalogues and lineage (Collibra, Alation, Atlan, DataHub Cloud, data.world, Select Star, Secoda, Solidatus), data quality and observability (Monte Carlo, Anomalo, Bigeye, Sifflet, Soda, GX Cloud, Ataccama, Precisely, Experian), master data (Reltio, Profisee, Semarchy, Stibo Systems, Syndigo, Tamr, K2view), privacy and data security (OneTrust, BigID, Securiti, Cyera, Varonis, Immuta, Trust3 AI, Protegrity, Skyflow), test and synthetic data (Delphix, Tonic.ai, MOSTLY AI), and ML and AI tooling (Dataiku, DataRobot, Domino, H2O.ai, Weights & Biases, Comet, Arize, Fiddler, Braintrust, LangSmith, Splunk Agent Observability, Scale AI, Labelbox, Snorkel AI, Credo AI, Holistic AI). Each entry's vendor field names the current owner where a brand has been acquired.

# Notes

- The market has consolidated sharply. Fivetran and dbt Labs merged on 1 June 2026 and operate as Fivetran + dbt Labs, after Fivetran had bought Census (now Fivetran Activations) and Tobiko Data (SQLMesh). SAP owns Reltio and announced on 4 May 2026 that it would buy Dremio. Snowflake owns Select Star, Atlassian owns Secoda, ServiceNow owns data.world, Veeam owns Securiti, CoreWeave owns Weights & Biases and NVIDIA absorbed Gretel. Cisco has completed its purchase of Galileo, now Splunk Agent Observability.
- Some owners have their own pages. Salesforce owns Tableau and MuleSoft, which are listed here, and Informatica, which has its own platform page. IBM owns Confluent, whose products are listed under IBM.
- Recent renames: Privacera now trades as Trust3 AI, Mode is ThoughtSpot Analyst Studio, Rivery is Boomi Data Integration, Matillion's Data Productivity Cloud is Maia Foundation, dbt Cloud is the dbt platform, dbt Explorer is dbt Catalog, Acryl Data is DataHub and mParticle is sold as mParticle by Rokt.
- Many vendors can process data inside the customer's own network or cloud account while running the control plane themselves (Fivetran Hybrid Deployment, Airbyte Enterprise Flex, Astro Remote Execution, Dagster+ Hybrid, Redpanda BYOC, Estuary, StarTree, Pinecone). Check where data is processed and stored, not only where the service is hosted.
- Several products are commercial services around open-source projects: Astro (Airflow), Starburst (Trino), Imply (Druid), StarTree (Pinot), MotherDuck (DuckDB), Dagster+, Prefect Cloud, DataHub Cloud, GX Cloud, Soda Cloud and Cube Cloud. The projects are described on the open-source platform page; check which features need the commercial edition.
- Nearly every vendor now ships AI agents and an MCP server, and release stages for these features are often not published. Access policy can also be enforced by several tools at once (Immuta, Collibra Data Access, OneTrust Data Use Governance, Trust3 AI), so decide which one owns enforcement on each platform.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Coverage by domain

A capability counts as covered when a generally available technology in this bundle realises it or a narrower capability. Preview-only coverage is shown separately; deprecated products and redistributions are not counted. A gap can mean the platform lacks the capability, or that the bundle has not mapped it yet.

| Domain | Covered | Not covered |
|---|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 18 of 22 | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md) |
| [Storage and table management](../capabilities/storage/storage.md) | 8 of 23 | [Object storage](../capabilities/storage/object-storage.md), [Open file formats](../capabilities/storage/file-formats.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Platform-managed storage](../capabilities/storage/managed-storage.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Time travel](../capabilities/storage/time-travel.md) |
| [Processing and transformation](../capabilities/processing/processing.md) | 11 of 18 | [AI functions in SQL](../capabilities/processing/ai-functions.md), [DataFrame APIs](../capabilities/processing/dataframe-apis.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Distributed processing](../capabilities/processing/distributed-processing.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md) |
| [Orchestration](../capabilities/orchestration/orchestration.md) | 4 of 5 | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md) |
| [Query and compute](../capabilities/compute/compute.md) | 13 of 22 | [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Workload management](../capabilities/compute/workload-management.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Container services](../capabilities/compute/container-services.md), [Provisioned compute](../capabilities/compute/provisioned-compute.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) |
| [Serving and activation](../capabilities/serving/serving.md) | 10 of 13 | [Change feeds](../capabilities/serving/change-feeds.md), [Data export](../capabilities/serving/data-export.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 16 of 20 | [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md) |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 14 of 20 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) |
| [ML operations](../capabilities/mlops/mlops.md) | 8 of 18 | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | 22 of 23 | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md) |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | 18 of 20 | [Schema registry](../capabilities/metadata/schema-registry.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | 10 of 12 | [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) |
| [Master and reference data](../capabilities/master-data/master-data.md) | 7 of 7 |  |
| [Governance and compliance](../capabilities/governance/governance.md) | 21 of 24 | [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [AI incident management](../capabilities/governance/ai-incident-management.md) |
| [Security and access](../capabilities/security/security.md) | 12 of 23 | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Privileged access management](../capabilities/security/privileged-access.md), [Role-based access control](../capabilities/security/role-based-access.md) |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 3 of 8 | [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) |
| [Data products](../capabilities/data-products/data-products.md) | 4 of 7 | [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 14 of 16 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md) |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | 12 of 27 | [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Platform migration](../capabilities/platform-operations/platform-migration.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md) |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 7 of 10 | [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md) |

# Technologies

## Ingestion and integration

- [Airbyte Cloud](../technologies/independent/airbyte-cloud.md): Managed version of the Airbyte data movement platform, with more than 600 source and destination connectors, a low-code Connector Builder and API and Terraform control.
- [Boomi Data Integration](../technologies/independent/boomi-data-integration.md): Managed ELT service with no-code connectors, CDC replication, Python steps, pipeline orchestration and reverse ETL to operational applications.
- [Boomi Enterprise Platform](../technologies/independent/boomi-enterprise-platform.md): Integration platform as a service covering application integration, API management, event streams, B2B/EDI, managed file transfer and AI agent building.
- [Estuary](../technologies/independent/estuary.md): Data movement platform that combines CDC, streaming and batch pipelines, backfilling history and then capturing changes into collections stored in the customer's bucket.
- [Fivetran](../technologies/independent/fivetran.md): Managed ELT service that extracts data from SaaS applications, databases, files and APIs through prebuilt connectors and loads it into warehouses and lakes on a schedule.
- [Fivetran HVR](../technologies/independent/fivetran-hvr.md): Self-hosted replication software from Fivetran that captures changes from database transaction logs and replicates databases and file systems at high volume.
- [mParticle](../technologies/independent/mparticle.md): Customer data platform for real-time event collection, identity resolution, audience segmentation and predictions, with a hybrid architecture that can use the customer's warehouse.
- [MuleSoft Anypoint Platform](../technologies/independent/mulesoft-anypoint-platform.md): Integration and API management platform for building Mule applications, APIs and event flows that connect systems in near real time.
- [Qlik Replicate](../technologies/independent/qlik-replicate.md): Customer-managed replication software that runs a full load and then reads source transaction logs to send changes continuously to warehouses, lakes and streaming targets.
- [Qlik Talend Cloud](../technologies/independent/qlik-talend-cloud.md): Qlik's cloud data integration service, combining real-time data movement and CDC, ELT and ETL transformation, data quality and data products.
- [Redpanda Cloud](../technologies/independent/redpanda-cloud.md): Managed Kafka-compatible streaming service on a C++ engine with no external dependencies, offered as Serverless, Dedicated or BYOC clusters.
- [Striim Cloud](../technologies/independent/striim-cloud.md): Managed streaming integration service that loads an initial snapshot, then captures changes and processes them with continuous SQL queries before delivery to cloud targets.
- [Twilio Segment](../technologies/independent/twilio-segment.md): Customer data platform that collects behavioural events through SDKs, validates them against tracking plans, unifies profiles and sends data to destinations, including from the warehouse.

## Storage and table management

- [Fivetran Managed Data Lake Service](../technologies/independent/fivetran-managed-data-lake-service.md): Destination option that writes replicated data as Parquet files with Iceberg metadata, and optionally Delta Lake metadata, into the customer's S3, ADLS or GCS storage, and maintains the tables.
- [Qlik Open Lakehouse](../technologies/independent/qlik-open-lakehouse.md): Managed service within Qlik Talend Cloud that lands replicated and streaming data as Apache Iceberg tables in the customer's AWS account and keeps them optimised.

## Processing and transformation

- [Alteryx One](../technologies/independent/alteryx-one.md): Analytics automation platform for no-code data preparation, blending and analytic workflows, with conversational analytics and an agent studio.
- [Coalesce Transform](../technologies/independent/coalesce-transform.md): Metadata-driven, column-aware workspace for designing and deploying SQL transformation pipelines on Snowflake, Databricks and other cloud platforms, using reusable node types.
- [Dataiku](../technologies/independent/dataiku.md): Collaborative platform for data preparation, visual and code-based machine learning, AutoML, deployment, monitoring and building AI agents, used by both analysts and data scientists.
- [dbt platform](../technologies/independent/dbt-platform.md): Hosted service for developing, testing, scheduling and deploying dbt transformation projects, with a browser IDE, a visual editor, job scheduling, CI on pull requests and environments.
- [dbt v2 engine](../technologies/independent/dbt-fusion-engine.md): Rust-based dbt v2 engine, distributed as "dbt", that parses and understands SQL across warehouse dialects, so it can catch errors and resolve dependencies before anything runs in the warehouse.
- [LlamaParse](../technologies/independent/llamaparse.md): Hosted document processing that parses complex documents with vision and language models and offers extraction, splitting, classification and indexing services.
- [Materialize](../technologies/independent/materialize.md): PostgreSQL-compatible engine that keeps SQL views up to date incrementally as source data changes, so applications and agents can read fresh results with low latency.
- [Matillion Maia Foundation](../technologies/independent/matillion-maia-foundation.md): Matillion's cloud data integration platform for building ingestion, transformation and orchestration pipelines visually or in SQL and Python, pushed down to Snowflake, Databricks, BigQuery or Redshift.
- [Unstructured.io](../technologies/independent/unstructured.md): Managed service that partitions documents into structured elements, then chunks and embeds them and loads them into vector stores and data platforms, from 20+ source connectors.

## Orchestration

- [Astronomer Astro](../technologies/independent/astronomer-astro.md): Fully managed Apache Airflow service for authoring, running and observing data pipelines, with Airflow 3 support, CI/CD templates and a browser IDE.
- [Dagster+](../technologies/independent/dagster-plus.md): Managed control plane for Dagster's asset-based orchestration, with an asset catalogue, branch deployments, cost and performance insights and alerting.
- [Prefect Cloud](../technologies/independent/prefect-cloud.md): Hosted control plane for Prefect Python workflows, with managed or serverless execution, hybrid workers, event-driven automations, RBAC and audit logs.

## Query and compute

- [dbt Lake Compute](../technologies/independent/dbt-lake-compute.md) (preview): Hosted serverless DuckDB-based compute that runs dbt models directly against Apache Iceberg tables, either alongside a warehouse or as a project's main engine.
- [Denodo Platform](../technologies/independent/denodo-platform.md): Logical data management and virtualisation platform that presents many sources as one governed semantic model and pushes queries down to them.
- [Imply Polaris](../technologies/independent/imply-polaris.md): Fully managed Apache Druid service for sub-second analytical queries over streaming and batch data.
- [MotherDuck](../technologies/independent/motherduck.md): Serverless cloud data warehouse built on DuckDB that gives each user or agent its own isolated compute instance and can split one query across a laptop and the cloud.
- [Starburst Enterprise](../technologies/independent/starburst-enterprise.md): Self-managed, supported Trino distribution for running federated and lakehouse SQL on Kubernetes in the customer's own environment.
- [Starburst Galaxy](../technologies/independent/starburst-galaxy.md): Managed Trino-based query service that queries lake tables and federated sources in place, with Iceberg lake management, streaming ingest into live tables and built-in governance.
- [StarTree Cloud](../technologies/independent/startree-cloud.md): Managed Apache Pinot service for low-latency, high-concurrency analytics on fresh event data, including user-facing and agent-facing applications.
- [Tinybird](../technologies/independent/tinybird.md): Managed ClickHouse platform that ingests events and files, transforms them with SQL pipes and incremental materialised views, and publishes the results as authenticated HTTP API endpoints.

## Serving and activation

- [Fivetran Activations](../technologies/independent/fivetran-activations.md): Syncs modelled data from a warehouse or lake back into operational tools such as CRM, advertising and marketing platforms.
- [Hightouch](../technologies/independent/hightouch.md): Warehouse-native activation platform that syncs modelled data to business tools and adds audience building, identity resolution and event collection on top of the warehouse.
- [K2view Data Product Platform](../technologies/independent/k2view-data-product-platform.md): Integrates and stores data per business entity, such as one customer, in small entity-level stores, keeps them in sync with sources and serves them in real time.
- [MongoDB Atlas](../technologies/independent/mongodb-atlas.md): Managed MongoDB document database with integrated full-text search, vector search and automated embedding generation using Voyage AI models.
- [Redis Cloud](../technologies/independent/redis-cloud.md): Managed Redis in-memory database for sub-millisecond key-value, JSON, stream and vector workloads, with active-active geo-distribution.
- [Workiva](../technologies/independent/workiva.md): Cloud platform for financial, regulatory and sustainability reporting that links reported figures to their source data and produces filings in formats such as XBRL and ESEF.

## Analytics and BI

- [AtScale](../technologies/independent/atscale.md): Universal semantic layer platform that presents governed dimensional models to Power BI, Excel, Tableau, Looker and AI agents, and generates aggregates to speed up queries.
- [Cube Cloud](../technologies/independent/cube-cloud.md): Managed semantic layer and agentic analytics platform that defines governed metrics once and serves them to BI tools, applications and AI agents through SQL and chat APIs.
- [dbt Charts](../technologies/independent/dbt-charts.md) (unconfirmed): Dashboard product in which each dashboard is a YAML file of queries, charts and layout, kept beside dbt models and validated in CI, with a hosted platform for editing, sharing and chat.
- [dbt Semantic Layer](../technologies/independent/dbt-semantic-layer.md): Defines metrics and semantic models alongside dbt models, using MetricFlow, and serves them through APIs to BI tools, spreadsheets and AI assistants.
- [Domo](../technologies/independent/domo.md): Cloud BI platform with its own connectors, drag-and-drop Magic ETL, dashboards, low-code App Studio, workflows and embedded analytics.
- [Omni Analytics](../technologies/independent/omni.md): BI platform that builds a shared semantic model as people query, combining SQL, spreadsheet-style formulas, dashboards and AI agents over the warehouse.
- [Qlik Cloud Analytics](../technologies/independent/qlik-cloud-analytics.md): Qlik's SaaS analytics service, built on its associative engine, for dashboards, self-service exploration, scheduled reports, alerts and embedding.
- [Sigma Computing](../technologies/independent/sigma.md): Warehouse-native BI and apps service with a spreadsheet interface that compiles to SQL, input tables that write back to the warehouse, and AI agents and apps.
- [Sisense](../technologies/independent/sisense.md): Analytics platform aimed mainly at embedding dashboards and AI-driven analytics in other products, with the Compose SDK for API-first development.
- [Tableau Cloud](../technologies/independent/tableau-cloud.md): Hosted Tableau analytics service for building, sharing and embedding interactive dashboards, with Tableau Agent for natural-language questions, data preparation and authoring help.
- [Tableau Next](../technologies/independent/tableau-next.md): API-first agentic analytics product on Salesforce's Hyperforce that uses Data 360 as its data layer and Tableau Semantics as its semantic model.
- [Tableau Pulse](../technologies/independent/tableau-pulse.md): Metric-following experience in Tableau Cloud that defines metrics once and then sends followers automated summaries of trends, drivers and outliers in Slack, Teams, email and mobile.
- [ThoughtSpot Analyst Studio](../technologies/independent/thoughtspot-analyst-studio.md): Data preparation and modelling environment with a SQL IDE, Python and R notebooks, data mash-ups and cached snapshots for repeated querying.
- [ThoughtSpot Analytics](../technologies/independent/thoughtspot-analytics.md): Search- and AI-driven analytics service for business users, with governed models, Liveboards (interactive dashboards) and an embedding SDK.
- [ThoughtSpot Spotter](../technologies/independent/thoughtspot-spotter.md): ThoughtSpot's AI analyst agent, which answers natural-language questions over governed models and investigates follow-ups, including over unstructured data.

## Machine learning development

- [Comet ML](../technologies/independent/comet.md): ML experiment management (tracking, artefacts, model registry and production monitoring) together with Opik for tracing, evaluating and optimising LLM applications and agents.
- [DataRobot AI Platform](../technologies/independent/datarobot-ai-platform.md): Platform for building, deploying, monitoring and governing predictive models, generative AI applications and agents, known for its AutoML.
- [Domino Enterprise AI Platform](../technologies/independent/domino-enterprise-ai-platform.md): Governed workbench for code-first data science that provides compute and GPUs across clouds and on premises, with experiment reproducibility, model deployment, governance and cost controls.
- [H2O.ai Platform (Driverless AI and h2oGPTe)](../technologies/independent/h2o-ai.md): Self-hostable AI platform that combines Driverless AI for AutoML with explanations and h2oGPTe for document question answering, retrieval-augmented generation and agents.
- [Labelbox](../technologies/independent/labelbox.md): Labelling and data curation software together with an expert network (Alignerr) that produces preference, rubric and evaluation data for model training.
- [Scale Data Engine](../technologies/independent/scale-data-engine.md): Managed labelling and training data production that combines human experts and model assistance, covering computer vision, text, preference and evaluation data.
- [Snorkel AI](../technologies/independent/snorkel-ai.md): Builds expert-labelled datasets, rubrics and evaluation environments for training and testing models and agents, having started with programmatic labelling (Snorkel Flow).
- [Weights & Biases](../technologies/independent/weights-and-biases.md): Experiment tracking, hyperparameter sweeps, artefact versioning and a model registry (W&B Models), plus tracing and evaluation of LLM and agent applications (W&B Weave).

## ML operations

- [Fiddler AI Control Plane](../technologies/independent/fiddler-ai-control-plane.md): Monitoring, explainability and guardrails for ML models, LLM applications and agents, using Fiddler's own small evaluation models to score outputs quickly.

## Generative AI

- [Airbyte Agents](../technologies/independent/airbyte-agents.md) (unconfirmed): Type-safe connectors that give AI agents live read access to business applications through an MCP server, a Python SDK and an HTTP API.
- [Arize AX](../technologies/independent/arize-ax.md): Managed observability and evaluation platform for LLM applications, agents and traditional ML models, covering tracing, online evaluations, drift and performance monitoring.
- [Braintrust](../technologies/independent/braintrust.md): Evaluation and observability platform for AI products that runs experiments on datasets with LLM, code and human scorers and logs production traces.
- [Dataiku LLM Mesh](../technologies/independent/dataiku-llm-mesh.md): Abstraction layer that routes calls from Dataiku projects to many LLM providers, with quotas, cost tracking, PII screening and monitoring.
- [Kong Konnect](../technologies/independent/kong-konnect.md): API platform whose AI Gateway governs and meters LLM traffic and whose Event Gateway applies policies to Kafka traffic, such as virtual clusters and access control.
- [LangSmith](../technologies/independent/langsmith.md): Platform for tracing, monitoring and evaluating LLM agents, managing prompts, and deploying and running agents in production.
- [Monte Carlo Agent Observability](../technologies/independent/monte-carlo-agent-observability.md): Records AI agent runs as OpenTelemetry traces and scores them with LLM judges and deterministic checks, alerting on quality, cost, latency and tool-call trajectories.
- [Pinecone](../technologies/independent/pinecone.md): Managed vector database for dense, sparse, full-text and hybrid retrieval, with hosted embedding and reranking models and a managed RAG assistant.
- [Redpanda Agentic Data Plane](../technologies/independent/redpanda-agentic-data-plane.md) (unconfirmed): Infrastructure for running and governing AI agents on enterprise data, with managed agents, an MCP gateway for tool access and an AI gateway for model access and cost control.
- [Splunk Agent Observability](../technologies/independent/galileo.md): Evaluation and observability for AI agents and LLM applications, formerly Galileo, that uses small evaluation models to score outputs and block bad ones at runtime.
- [Weaviate Cloud](../technologies/independent/weaviate-cloud.md): Managed deployment of the Weaviate vector database with hybrid keyword and vector search, hosted embeddings and an agentic Query Agent.

## Metadata and discovery

- [Alation Intelligence Operating System (AIOS)](../technologies/independent/alation-aios.md): Alation's catalogue platform, which combines search, curation, lineage, glossary, trust flags, data products and a marketplace with AI agents that document and curate assets.
- [Atlan](../technologies/independent/atlan.md): Metadata platform that builds a graph of data, BI and business systems and serves it to people through a catalogue and marketplace and to AI agents through an MCP server and APIs.
- [Collibra Data Catalog](../technologies/independent/collibra-data-catalog.md): Searchable inventory of data assets across warehouses, lakes, applications and BI tools, built from automatically harvested metadata and enriched with descriptions and classifications.
- [Collibra Data Governance](../technologies/independent/collibra-data-governance.md): Governance workspace for business glossaries, ownership and stewardship roles, policies and the workflows that route approvals and issues to stewards.
- [Collibra Data Lineage](../technologies/independent/collibra-data-lineage.md): Automatically extracts lineage from SQL, ETL tools and BI reports and shows it at table and column level across systems.
- [data.world](../technologies/independent/data-world.md): Data catalogue and governance service built on a knowledge graph, which links technical assets to business concepts.
- [DataHub Cloud](../technologies/independent/datahub-cloud.md): Managed, extended edition of the open-source DataHub metadata platform that adds data observability assertions, AI documentation, access request workflows and an AI assistant.
- [dbt Catalog](../technologies/independent/dbt-catalog.md): Searchable catalogue of the models, sources, metrics and exposures in dbt projects, with lineage, documentation and run health.
- [Secoda](../technologies/independent/secoda.md): Catalogue for analytics teams that combines search, lineage, documentation, monitors, a quality score and access requests with AI agents for search and documentation.
- [Select Star](../technologies/independent/select-star.md): Automated catalogue that builds column-level lineage, usage-based popularity and entity relationships from query logs and generates semantic models from BI logic.
- [Solidatus](../technologies/independent/solidatus.md): Lineage modelling tool that combines automatically harvested technical lineage with business process lineage in versioned, bi-temporal models.

## Data quality and observability

- [Anomalo](../technologies/independent/anomalo.md): Uses unsupervised machine learning to detect anomalies in table contents, freshness and schema without hand-written rules, adds validation rules and monitors documents for AI readiness.
- [Ataccama ONE](../technologies/independent/ataccama-one.md): Data management platform for profiling, rule-based quality and cleansing, observability, catalogue and lineage, which shares one rule library and metadata model across its modules.
- [Bigeye AI Trust Platform](../technologies/independent/bigeye.md): Data observability with automatic anomaly detection and end-to-end lineage across modern and legacy stacks, extended with sensitive-data scanning and runtime policy enforcement for AI applications.
- [Collibra Data Quality & Observability](../technologies/independent/collibra-data-quality-observability.md): Profiles data, generates and runs quality rules, and monitors tables for schema changes, missing or duplicate records and other anomalies, publishing scores to the catalogue.
- [Experian Aperture Data Studio](../technologies/independent/experian-aperture-data-studio.md): Self-service tool for profiling, validating, cleansing, matching and deduplicating data, with Experian address, email and phone validation and reference data built in.
- [GX Cloud](../technologies/independent/gx-cloud.md): Managed service for writing, scheduling and running Great Expectations data tests against connected data sources, with alerts and a data health view of coverage and results.
- [Monte Carlo Data + AI Observability](../technologies/independent/monte-carlo-data-observability.md): Monitors warehouse, lake and pipeline data for freshness, volume, schema and distribution anomalies using learnt baselines, and links incidents to lineage for triage.
- [Precisely Data Integrity Suite](../technologies/independent/precisely-data-integrity-suite.md): Modular SaaS suite of interoperable services for data integration, observability, governance and catalogue, quality, address verification, spatial analytics and enrichment.
- [Sifflet](../technologies/independent/sifflet.md): Data observability service that combines monitors, field-level lineage, a catalogue and incident management, with AI agents that recommend monitors and investigate root causes.

## Master and reference data

- [Ataccama ONE Master Data Management](../technologies/independent/ataccama-one-mdm.md): Multidomain master data and reference data management module of Ataccama ONE, with matching, merging and stewardship built on the platform's data quality engine.
- [Precisely EnterWorks](../technologies/independent/precisely-enterworks.md): Multidomain master data and product information management with workflows, hierarchies and syndication of product content to channels.
- [Profisee MDM](../technologies/independent/profisee-mdm.md): Multidomain MDM for matching, merging, stewardship and hierarchy management, closely integrated with Microsoft Azure, Purview and Fabric.
- [Reltio Multidomain MDM](../technologies/independent/reltio-multidomain-mdm.md): Cloud-native multidomain MDM that resolves entities with rules and machine learning, merges them into profiles and serves them to applications through real-time APIs.
- [Semarchy Data Platform](../technologies/independent/semarchy-data-platform.md): Platform that combines multidomain MDM, reference data management, data quality and governance for publishing mastered entities as data products.
- [Stibo Systems STEP](../technologies/independent/stibo-systems-step.md): Multidomain MDM and product information management for product, customer, supplier and location data, with validation, enrichment and configurable hierarchies.
- [Syndigo MDM](../technologies/independent/syndigo-mdm.md): Master data management for product, customer, supplier and location records, alongside Syndigo's product information management and retailer content syndication.
- [Tamr](../technologies/independent/tamr.md): Machine-learning-led MDM that matches and enriches records with built-in external reference data to produce golden records, made available in real time.

## Governance and compliance

- [BigID Next](../technologies/independent/bigid-next.md): Discovers and classifies sensitive data across cloud, SaaS and on-premises stores and uses that inventory for security posture, privacy rights, retention and AI governance.
- [Collibra AI Command Center](../technologies/independent/collibra-ai-command-center.md) (unconfirmed): Registry and control plane for AI use cases, models and agents that links each one to its data, policies and assessments and tracks production trust signals.
- [Credo AI Governance Platform](../technologies/independent/credo-ai-governance-platform.md): Keeps a registry of AI systems, agents, models and vendors and turns regulations and policies into controls, risk assessments and evidence.
- [Holistic AI Governance Platform](../technologies/independent/holistic-ai-governance-platform.md): Discovers and inventories AI systems, tests models and agents for bias, safety and security, and maps controls to AI regulations with approval gates.
- [OneTrust AI Governance](../technologies/independent/onetrust-ai-governance.md): Keeps an inventory of AI systems, models and vendors and runs risk assessments and approvals against regulations such as the EU AI Act.
- [OneTrust Data Use Governance](../technologies/independent/onetrust-data-use-governance.md): Turns privacy and purpose rules into data access and masking policies and applies them on cloud data platforms.
- [OneTrust Privacy Automation](../technologies/independent/onetrust-privacy-automation.md): Automates privacy programme work including data mapping, records of processing, privacy impact assessments, data subject requests and, through Consent & Preferences, consent capture.
- [Protegrity Data Security Platform](../technologies/independent/protegrity-data-security-platform.md): Protects sensitive fields with vaultless tokenisation, encryption and masking applied consistently across databases, data platforms, applications and AI pipelines, with central policy.
- [Skyflow Data Privacy Vault](../technologies/independent/skyflow-data-privacy-vault.md): Isolates sensitive personal data in a dedicated vault and gives applications, analytics and AI tokens or policy-controlled detokenised values instead.
- [Tonic Textual](../technologies/independent/tonic-textual.md): Detects named entities in free text, documents and audio and redacts them or replaces them with consistent synthetic values.

## Security and access

- [Collibra Data Access](../technologies/independent/collibra-data-access.md): Manages access requests, masking, row filtering and role-based grants centrally and provisions them into Snowflake, Databricks and BigQuery.
- [Cyera DSPM](../technologies/independent/cyera-dspm.md): Agentless discovery and AI-based classification of sensitive data across cloud, SaaS and on-premises stores, showing who and what can reach it and which exposures matter.
- [Immuta Data Authorization Platform](../technologies/independent/immuta-data-authorization-platform.md): Defines attribute- and purpose-based access policies once and enforces them natively on cloud data platforms, with access request workflows, discovery, tagging and audit reports.
- [Privacera](../technologies/independent/privacera.md): Data access governance based on Apache Ranger that discovers sensitive data and applies central access, masking and encryption policies across cloud data and analytics services.
- [Securiti DataAI Command Platform](../technologies/independent/securiti-dataai-command-platform.md): Builds a knowledge graph of data, AI systems, identities and regulations across hybrid multicloud and SaaS and uses it for security posture, privacy operations and AI security.
- [Varonis Data Security Platform](../technologies/independent/varonis-data-security-platform.md): Classifies sensitive data, maps permissions and monitors activity across file shares, SaaS, cloud and databases to remove excess access and detect threats to data.

## Data products

- [Soda Cloud](../technologies/independent/soda-cloud.md): Collaborative workspace for defining data contracts, running checks in pipelines and on schedules, monitoring metrics for anomalies and triaging data incidents.

## Development and DataOps

- [dbt Copilot](../technologies/independent/dbt-copilot.md): AI assistant in the dbt platform that drafts models, tests, documentation, semantic models and SQL from natural language.
- [Gretel](../technologies/independent/gretel.md) (retired): Synthetic data and privacy service for generating tabular and text data, now absorbed into NVIDIA.
- [Hex](../technologies/independent/hex.md): Collaborative data workspace that combines SQL and Python notebooks, interactive apps and natural-language Threads, with AI agents that write and run analysis.
- [Matillion Maia](../technologies/independent/matillion-maia.md): Team of AI agents that plans, builds, tests, deploys and repairs Matillion pipelines from natural-language requests, with human review before execution.
- [MOSTLY AI Data Intelligence Platform](../technologies/independent/mostly-ai-data-intelligence-platform.md): Trains generative models on tabular production data to produce privacy-safe synthetic datasets for sharing, analytics, testing and AI development.
- [Perforce Delphix](../technologies/independent/perforce-delphix.md): Provides masked, virtualised copies of production databases to non-production environments on demand, with synthetic data generation and continuous data protection.
- [Tonic Structural](../technologies/independent/tonic-structural.md): De-identifies and subsets structured production databases into realistic, referentially intact copies for development and testing.

## Platform operations

- [PagerDuty](../technologies/independent/pagerduty.md): Incident management service that routes alerts to on-call responders, runs escalation policies and records incidents and post-incident reviews.

## Specialised data types

- [Elastic Cloud](../technologies/independent/elastic-cloud.md): Managed Elasticsearch, offered serverless or as hosted clusters, for full-text, log and vector search, with observability and security solutions and an agent builder.
- [Neo4j Aura](../technologies/independent/neo4j-aura.md): Managed Neo4j graph database (AuraDB) with vector indexes, graph data science and on-demand graph analytics sessions.

