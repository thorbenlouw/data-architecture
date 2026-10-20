# Independent vendors

# Ingestion and integration

* [Airbyte Cloud](airbyte-cloud.md) - Managed version of the Airbyte data movement platform, with more than 600 source and destination connectors, a low-code Connector Builder and API and Terraform control.
* [Boomi Data Integration](boomi-data-integration.md) - Managed ELT service with no-code connectors, CDC replication, Python steps, pipeline orchestration and reverse ETL to operational applications.
* [Boomi Enterprise Platform](boomi-enterprise-platform.md) - Integration platform as a service covering application integration, API management, event streams, B2B/EDI, managed file transfer and AI agent building.
* [Estuary](estuary.md) - Data movement platform that combines CDC, streaming and batch pipelines, backfilling history and then capturing changes into collections stored in the customer's bucket.
* [Fivetran](fivetran.md) - Managed ELT service that extracts data from SaaS applications, databases, files and APIs through prebuilt connectors and loads it into warehouses and lakes on a schedule.
* [Fivetran HVR](fivetran-hvr.md) - Self-hosted replication software from Fivetran that captures changes from database transaction logs and replicates databases and file systems at high volume.
* [mParticle](mparticle.md) - Customer data platform for real-time event collection, identity resolution, audience segmentation and predictions, with a hybrid architecture that can use the customer's warehouse.
* [MuleSoft Anypoint Platform](mulesoft-anypoint-platform.md) - Integration and API management platform for building Mule applications, APIs and event flows that connect systems in near real time.
* [Qlik Replicate](qlik-replicate.md) - Customer-managed replication software that runs a full load and then reads source transaction logs to send changes continuously to warehouses, lakes and streaming targets.
* [Qlik Talend Cloud](qlik-talend-cloud.md) - Qlik's cloud data integration service, combining real-time data movement and CDC, ELT and ETL transformation, data quality and data products.
* [Redpanda Cloud](redpanda-cloud.md) - Managed Kafka-compatible streaming service on a C++ engine with no external dependencies, offered as Serverless, Dedicated or BYOC clusters.
* [Striim Cloud](striim-cloud.md) - Managed streaming integration service that loads an initial snapshot, then captures changes and processes them with continuous SQL queries before delivery to cloud targets.
* [Twilio Segment](twilio-segment.md) - Customer data platform that collects behavioural events through SDKs, validates them against tracking plans, unifies profiles and sends data to destinations, including from the warehouse.

# Storage and table management

* [Fivetran Managed Data Lake Service](fivetran-managed-data-lake-service.md) - Destination option that writes replicated data as Parquet files with Iceberg metadata, and optionally Delta Lake metadata, into the customer's S3, ADLS or GCS storage, and maintains the tables.
* [Qlik Open Lakehouse](qlik-open-lakehouse.md) - Managed service within Qlik Talend Cloud that lands replicated and streaming data as Apache Iceberg tables in the customer's AWS account and keeps them optimised.

# Processing and transformation

* [Alteryx One](alteryx-one.md) - Analytics automation platform for no-code data preparation, blending and analytic workflows, with conversational analytics and an agent studio.
* [Coalesce Transform](coalesce-transform.md) - Metadata-driven, column-aware workspace for designing and deploying SQL transformation pipelines on Snowflake, Databricks and other cloud platforms, using reusable node types.
* [dbt platform](dbt-platform.md) - Hosted service for developing, testing, scheduling and deploying dbt transformation projects, with a browser IDE, a visual editor, job scheduling, CI on pull requests and environments.
* [dbt v2 engine](dbt-fusion-engine.md) - Rust-based dbt v2 engine, distributed as "dbt", that parses and understands SQL across warehouse dialects, so it can catch errors and resolve dependencies before anything runs in the warehouse.
* [LlamaParse](llamaparse.md) - Hosted document processing that parses complex documents with vision and language models and offers extraction, splitting, classification and indexing services.
* [Materialize](materialize.md) - PostgreSQL-compatible engine that keeps SQL views up to date incrementally as source data changes, so applications and agents can read fresh results with low latency.
* [Matillion Maia Foundation](matillion-maia-foundation.md) - Matillion's cloud data integration platform for building ingestion, transformation and orchestration pipelines visually or in SQL and Python, pushed down to Snowflake, Databricks, BigQuery or Redshift.
* [Unstructured.io](unstructured.md) - Managed service that partitions documents into structured elements, then chunks and embeds them and loads them into vector stores and data platforms, from 20+ source connectors.

# Orchestration

* [Astronomer Astro](astronomer-astro.md) - Fully managed Apache Airflow service for authoring, running and observing data pipelines, with Airflow 3 support, CI/CD templates and a browser IDE.
* [Dagster+](dagster-plus.md) - Managed control plane for Dagster's asset-based orchestration, with an asset catalogue, branch deployments, cost and performance insights and alerting.
* [Prefect Cloud](prefect-cloud.md) - Hosted control plane for Prefect Python workflows, with managed or serverless execution, hybrid workers, event-driven automations, RBAC and audit logs.

# Query and compute

* [dbt Lake Compute](dbt-lake-compute.md) (preview) - Hosted serverless DuckDB-based compute that runs dbt models directly against Apache Iceberg tables, either alongside a warehouse or as a project's main engine.
* [Denodo Platform](denodo-platform.md) - Logical data management and virtualisation platform that presents many sources as one governed semantic model and pushes queries down to them.
* [Imply Polaris](imply-polaris.md) - Fully managed Apache Druid service for sub-second analytical queries over streaming and batch data.
* [MotherDuck](motherduck.md) - Serverless cloud data warehouse built on DuckDB that gives each user or agent its own isolated compute instance and can split one query across a laptop and the cloud.
* [Starburst Enterprise](starburst-enterprise.md) - Self-managed, supported Trino distribution for running federated and lakehouse SQL on Kubernetes in the customer's own environment.
* [Starburst Galaxy](starburst-galaxy.md) - Managed Trino-based query service that queries lake tables and federated sources in place, with Iceberg lake management, streaming ingest into live tables and built-in governance.
* [StarTree Cloud](startree-cloud.md) - Managed Apache Pinot service for low-latency, high-concurrency analytics on fresh event data, including user-facing and agent-facing applications.
* [Tinybird](tinybird.md) - Managed ClickHouse platform that ingests events and files, transforms them with SQL pipes and incremental materialised views, and publishes the results as authenticated HTTP API endpoints.

# Serving and activation

* [Fivetran Activations](fivetran-activations.md) - Syncs modelled data from a warehouse or lake back into operational tools such as CRM, advertising and marketing platforms.
* [Hightouch](hightouch.md) - Warehouse-native activation platform that syncs modelled data to business tools and adds audience building, identity resolution and event collection on top of the warehouse.
* [K2view Data Product Platform](k2view-data-product-platform.md) - Integrates and stores data per business entity, such as one customer, in small entity-level stores, keeps them in sync with sources and serves them in real time.
* [MongoDB Atlas](mongodb-atlas.md) - Managed MongoDB document database with integrated full-text search, vector search and automated embedding generation using Voyage AI models.
* [Redis Cloud](redis-cloud.md) - Managed Redis in-memory database for sub-millisecond key-value, JSON, stream and vector workloads, with active-active geo-distribution.
* [Workiva](workiva.md) - Cloud platform for financial, regulatory and sustainability reporting that links reported figures to their source data and produces filings in formats such as XBRL and ESEF.

# Analytics and BI

* [AtScale](atscale.md) - Universal semantic layer platform that presents governed dimensional models to Power BI, Excel, Tableau, Looker and AI agents, and generates aggregates to speed up queries.
* [Cube Cloud](cube-cloud.md) - Managed semantic layer and agentic analytics platform that defines governed metrics once and serves them to BI tools, applications and AI agents through SQL and chat APIs.
* [dbt Charts](dbt-charts.md) (unconfirmed) - Dashboard product in which each dashboard is a YAML file of queries, charts and layout, kept beside dbt models and validated in CI, with a hosted platform for editing, sharing and chat.
* [dbt Semantic Layer](dbt-semantic-layer.md) - Defines metrics and semantic models alongside dbt models, using MetricFlow, and serves them through APIs to BI tools, spreadsheets and AI assistants.
* [Domo](domo.md) - Cloud BI platform with its own connectors, drag-and-drop Magic ETL, dashboards, low-code App Studio, workflows and embedded analytics.
* [Omni Analytics](omni.md) - BI platform that builds a shared semantic model as people query, combining SQL, spreadsheet-style formulas, dashboards and AI agents over the warehouse.
* [Qlik Cloud Analytics](qlik-cloud-analytics.md) - Qlik's SaaS analytics service, built on its associative engine, for dashboards, self-service exploration, scheduled reports, alerts and embedding.
* [Sigma Computing](sigma.md) - Warehouse-native BI and apps service with a spreadsheet interface that compiles to SQL, input tables that write back to the warehouse, and AI agents and apps.
* [Sisense](sisense.md) - Analytics platform aimed mainly at embedding dashboards and AI-driven analytics in other products, with the Compose SDK for API-first development.
* [Tableau Cloud](tableau-cloud.md) - Hosted Tableau analytics service for building, sharing and embedding interactive dashboards, with Tableau Agent for natural-language questions, data preparation and authoring help.
* [Tableau Next](tableau-next.md) - API-first agentic analytics product on Salesforce's Hyperforce that uses Data 360 as its data layer and Tableau Semantics as its semantic model.
* [Tableau Pulse](tableau-pulse.md) - Metric-following experience in Tableau Cloud that defines metrics once and then sends followers automated summaries of trends, drivers and outliers in Slack, Teams, email and mobile.
* [ThoughtSpot Analyst Studio](thoughtspot-analyst-studio.md) - Data preparation and modelling environment with a SQL IDE, Python and R notebooks, data mash-ups and cached snapshots for repeated querying.
* [ThoughtSpot Analytics](thoughtspot-analytics.md) - Search- and AI-driven analytics service for business users, with governed models, Liveboards (interactive dashboards) and an embedding SDK.
* [ThoughtSpot Spotter](thoughtspot-spotter.md) - ThoughtSpot's AI analyst agent, which answers natural-language questions over governed models and investigates follow-ups, including over unstructured data.

# Machine learning development

* [Comet ML](comet.md) - ML experiment management (tracking, artefacts, model registry and production monitoring) together with Opik for tracing, evaluating and optimising LLM applications and agents.
* [DataRobot AI Platform](datarobot-ai-platform.md) - Platform for building, deploying, monitoring and governing predictive models, generative AI applications and agents, known for its AutoML.
* [Domino Enterprise AI Platform](domino-enterprise-ai-platform.md) - Governed workbench for code-first data science that provides compute and GPUs across clouds and on premises, with experiment reproducibility, model deployment, governance and cost controls.
* [H2O.ai Platform (Driverless AI and h2oGPTe)](h2o-ai.md) - Self-hostable AI platform that combines Driverless AI for AutoML with explanations and h2oGPTe for document question answering, retrieval-augmented generation and agents.
* [Labelbox](labelbox.md) - Labelling and data curation software together with an expert network (Alignerr) that produces preference, rubric and evaluation data for model training.
* [Scale Data Engine](scale-data-engine.md) - Managed labelling and training data production that combines human experts and model assistance, covering computer vision, text, preference and evaluation data.
* [Snorkel AI](snorkel-ai.md) - Builds expert-labelled datasets, rubrics and evaluation environments for training and testing models and agents, having started with programmatic labelling (Snorkel Flow).
* [Weights & Biases](weights-and-biases.md) - Experiment tracking, hyperparameter sweeps, artefact versioning and a model registry (W&B Models), plus tracing and evaluation of LLM and agent applications (W&B Weave).

# ML operations

* [Fiddler AI Control Plane](fiddler-ai-control-plane.md) - Monitoring, explainability and guardrails for ML models, LLM applications and agents, using Fiddler's own small evaluation models to score outputs quickly.

# Generative AI

* [Airbyte Agents](airbyte-agents.md) (unconfirmed) - Type-safe connectors that give AI agents live read access to business applications through an MCP server, a Python SDK and an HTTP API.
* [Arize AX](arize-ax.md) - Managed observability and evaluation platform for LLM applications, agents and traditional ML models, covering tracing, online evaluations, drift and performance monitoring.
* [Braintrust](braintrust.md) - Evaluation and observability platform for AI products that runs experiments on datasets with LLM, code and human scorers and logs production traces.
* [Kong Konnect](kong-konnect.md) - API platform whose AI Gateway governs and meters LLM traffic and whose Event Gateway applies policies to Kafka traffic, such as virtual clusters and access control.
* [LangSmith](langsmith.md) - Platform for tracing, monitoring and evaluating LLM agents, managing prompts, and deploying and running agents in production.
* [Monte Carlo Agent Observability](monte-carlo-agent-observability.md) - Records AI agent runs as OpenTelemetry traces and scores them with LLM judges and deterministic checks, alerting on quality, cost, latency and tool-call trajectories.
* [Pinecone](pinecone.md) - Managed vector database for dense, sparse, full-text and hybrid retrieval, with hosted embedding and reranking models and a managed RAG assistant.
* [Redpanda Agentic Data Plane](redpanda-agentic-data-plane.md) (unconfirmed) - Infrastructure for running and governing AI agents on enterprise data, with managed agents, an MCP gateway for tool access and an AI gateway for model access and cost control.
* [Splunk Agent Observability](galileo.md) - Evaluation and observability for AI agents and LLM applications, formerly Galileo, that uses small evaluation models to score outputs and block bad ones at runtime.
* [Weaviate Cloud](weaviate-cloud.md) - Managed deployment of the Weaviate vector database with hybrid keyword and vector search, hosted embeddings and an agentic Query Agent.

# Metadata and discovery

* [Alation Intelligence Operating System (AIOS)](alation-aios.md) - Alation's catalogue platform, which combines search, curation, lineage, glossary, trust flags, data products and a marketplace with AI agents that document and curate assets.
* [Atlan](atlan.md) - Metadata platform that builds a graph of data, BI and business systems and serves it to people through a catalogue and marketplace and to AI agents through an MCP server and APIs.
* [Collibra Data Catalog](collibra-data-catalog.md) - Searchable inventory of data assets across warehouses, lakes, applications and BI tools, built from automatically harvested metadata and enriched with descriptions and classifications.
* [Collibra Data Governance](collibra-data-governance.md) - Governance workspace for business glossaries, ownership and stewardship roles, policies and the workflows that route approvals and issues to stewards.
* [Collibra Data Lineage](collibra-data-lineage.md) - Automatically extracts lineage from SQL, ETL tools and BI reports and shows it at table and column level across systems.
* [data.world](data-world.md) - Data catalogue and governance service built on a knowledge graph, which links technical assets to business concepts.
* [DataHub Cloud](datahub-cloud.md) - Managed, extended edition of the open-source DataHub metadata platform that adds data observability assertions, AI documentation, access request workflows and an AI assistant.
* [dbt Catalog](dbt-catalog.md) - Searchable catalogue of the models, sources, metrics and exposures in dbt projects, with lineage, documentation and run health.
* [Secoda](secoda.md) - Catalogue for analytics teams that combines search, lineage, documentation, monitors, a quality score and access requests with AI agents for search and documentation.
* [Select Star](select-star.md) - Automated catalogue that builds column-level lineage, usage-based popularity and entity relationships from query logs and generates semantic models from BI logic.
* [Solidatus](solidatus.md) - Lineage modelling tool that combines automatically harvested technical lineage with business process lineage in versioned, bi-temporal models.

# Data quality and observability

* [Anomalo](anomalo.md) - Uses unsupervised machine learning to detect anomalies in table contents, freshness and schema without hand-written rules, adds validation rules and monitors documents for AI readiness.
* [Ataccama ONE](ataccama-one.md) - Data management platform for profiling, rule-based quality and cleansing, observability, catalogue and lineage, which shares one rule library and metadata model across its modules.
* [Bigeye AI Trust Platform](bigeye.md) - Data observability with automatic anomaly detection and end-to-end lineage across modern and legacy stacks, extended with sensitive-data scanning and runtime policy enforcement for AI applications.
* [Collibra Data Quality & Observability](collibra-data-quality-observability.md) - Profiles data, generates and runs quality rules, and monitors tables for schema changes, missing or duplicate records and other anomalies, publishing scores to the catalogue.
* [Experian Aperture Data Studio](experian-aperture-data-studio.md) - Self-service tool for profiling, validating, cleansing, matching and deduplicating data, with Experian address, email and phone validation and reference data built in.
* [GX Cloud](gx-cloud.md) - Managed service for writing, scheduling and running Great Expectations data tests against connected data sources, with alerts and a data health view of coverage and results.
* [Monte Carlo Data + AI Observability](monte-carlo-data-observability.md) - Monitors warehouse, lake and pipeline data for freshness, volume, schema and distribution anomalies using learnt baselines, and links incidents to lineage for triage.
* [Precisely Data Integrity Suite](precisely-data-integrity-suite.md) - Modular SaaS suite of interoperable services for data integration, observability, governance and catalogue, quality, address verification, spatial analytics and enrichment.
* [Sifflet](sifflet.md) - Data observability service that combines monitors, field-level lineage, a catalogue and incident management, with AI agents that recommend monitors and investigate root causes.

# Master and reference data

* [Ataccama ONE Master Data Management](ataccama-one-mdm.md) - Multidomain master data and reference data management module of Ataccama ONE, with matching, merging and stewardship built on the platform's data quality engine.
* [Precisely EnterWorks](precisely-enterworks.md) - Multidomain master data and product information management with workflows, hierarchies and syndication of product content to channels.
* [Profisee MDM](profisee-mdm.md) - Multidomain MDM for matching, merging, stewardship and hierarchy management, closely integrated with Microsoft Azure, Purview and Fabric.
* [Reltio Multidomain MDM](reltio-multidomain-mdm.md) - Cloud-native multidomain MDM that resolves entities with rules and machine learning, merges them into profiles and serves them to applications through real-time APIs.
* [Semarchy Data Platform](semarchy-data-platform.md) - Platform that combines multidomain MDM, reference data management, data quality and governance for publishing mastered entities as data products.
* [Stibo Systems STEP](stibo-systems-step.md) - Multidomain MDM and product information management for product, customer, supplier and location data, with validation, enrichment and configurable hierarchies.
* [Syndigo MDM](syndigo-mdm.md) - Master data management for product, customer, supplier and location records, alongside Syndigo's product information management and retailer content syndication.
* [Tamr](tamr.md) - Machine-learning-led MDM that matches and enriches records with built-in external reference data to produce golden records, made available in real time.

# Governance and compliance

* [BigID Next](bigid-next.md) - Discovers and classifies sensitive data across cloud, SaaS and on-premises stores and uses that inventory for security posture, privacy rights, retention and AI governance.
* [Collibra AI Command Center](collibra-ai-command-center.md) (unconfirmed) - Registry and control plane for AI use cases, models and agents that links each one to its data, policies and assessments and tracks production trust signals.
* [Credo AI Governance Platform](credo-ai-governance-platform.md) - Keeps a registry of AI systems, agents, models and vendors and turns regulations and policies into controls, risk assessments and evidence.
* [Holistic AI Governance Platform](holistic-ai-governance-platform.md) - Discovers and inventories AI systems, tests models and agents for bias, safety and security, and maps controls to AI regulations with approval gates.
* [OneTrust AI Governance](onetrust-ai-governance.md) - Keeps an inventory of AI systems, models and vendors and runs risk assessments and approvals against regulations such as the EU AI Act.
* [OneTrust Data Use Governance](onetrust-data-use-governance.md) - Turns privacy and purpose rules into data access and masking policies and applies them on cloud data platforms.
* [OneTrust Privacy Automation](onetrust-privacy-automation.md) - Automates privacy programme work including data mapping, records of processing, privacy impact assessments, data subject requests and, through Consent & Preferences, consent capture.
* [Protegrity Data Security Platform](protegrity-data-security-platform.md) - Protects sensitive fields with vaultless tokenisation, encryption and masking applied consistently across databases, data platforms, applications and AI pipelines, with central policy.
* [Skyflow Data Privacy Vault](skyflow-data-privacy-vault.md) - Isolates sensitive personal data in a dedicated vault and gives applications, analytics and AI tokens or policy-controlled detokenised values instead.
* [Tonic Textual](tonic-textual.md) - Detects named entities in free text, documents and audio and redacts them or replaces them with consistent synthetic values.

# Security and access

* [Collibra Data Access](collibra-data-access.md) - Manages access requests, masking, row filtering and role-based grants centrally and provisions them into Snowflake, Databricks and BigQuery.
* [Cyera DSPM](cyera-dspm.md) - Agentless discovery and AI-based classification of sensitive data across cloud, SaaS and on-premises stores, showing who and what can reach it and which exposures matter.
* [Immuta Data Authorization Platform](immuta-data-authorization-platform.md) - Defines attribute- and purpose-based access policies once and enforces them natively on cloud data platforms, with access request workflows, discovery, tagging and audit reports.
* [Privacera](privacera.md) - Data access governance based on Apache Ranger that discovers sensitive data and applies central access, masking and encryption policies across cloud data and analytics services.
* [Securiti DataAI Command Platform](securiti-dataai-command-platform.md) - Builds a knowledge graph of data, AI systems, identities and regulations across hybrid multicloud and SaaS and uses it for security posture, privacy operations and AI security.
* [Varonis Data Security Platform](varonis-data-security-platform.md) - Classifies sensitive data, maps permissions and monitors activity across file shares, SaaS, cloud and databases to remove excess access and detect threats to data.

# Data products

* [Soda Cloud](soda-cloud.md) - Collaborative workspace for defining data contracts, running checks in pipelines and on schedules, monitoring metrics for anomalies and triaging data incidents.

# Development and DataOps

* [dbt Copilot](dbt-copilot.md) - AI assistant in the dbt platform that drafts models, tests, documentation, semantic models and SQL from natural language.
* [Gretel](gretel.md) (retired) - Synthetic data and privacy service for generating tabular and text data, now absorbed into NVIDIA.
* [Hex](hex.md) - Collaborative data workspace that combines SQL and Python notebooks, interactive apps and natural-language Threads, with AI agents that write and run analysis.
* [Matillion Maia](matillion-maia.md) - Team of AI agents that plans, builds, tests, deploys and repairs Matillion pipelines from natural-language requests, with human review before execution.
* [MOSTLY AI Data Intelligence Platform](mostly-ai-data-intelligence-platform.md) - Trains generative models on tabular production data to produce privacy-safe synthetic datasets for sharing, analytics, testing and AI development.
* [Perforce Delphix](perforce-delphix.md) - Provides masked, virtualised copies of production databases to non-production environments on demand, with synthetic data generation and continuous data protection.
* [Tonic Structural](tonic-structural.md) - De-identifies and subsets structured production databases into realistic, referentially intact copies for development and testing.

# Platform operations

* [PagerDuty](pagerduty.md) - Incident management service that routes alerts to on-call responders, runs escalation policies and records incidents and post-incident reviews.

# Specialised data types

* [Elastic Cloud](elastic-cloud.md) - Managed Elasticsearch, offered serverless or as hosted clusters, for full-text, log and vector search, with observability and security solutions and an agent builder.
* [Neo4j Aura](neo4j-aura.md) - Managed Neo4j graph database (AuraDB) with vector indexes, graph data science and on-demand graph analytics sessions.
