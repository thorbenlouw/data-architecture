# Informatica

# Ingestion and integration

* [Informatica Application Ingestion and Replication](informatica-application-ingestion-and-replication.md) - Replicates objects from SaaS and on-premises applications such as Salesforce, SAP and Workday to warehouses, lakes and streaming targets, as a snapshot or continuous change propagation.
* [Informatica B2B Gateway](informatica-b2b-gateway.md) - Exchanges EDI messages and files with trading partners and maps them to back-end systems using prebuilt mappings, with a partners portal for tracking exchanged files.
* [Informatica Cloud Application Integration (CAI)](informatica-cloud-application-integration.md) - Designs and runs event-driven and API-driven processes and service connectors that integrate applications in near real time, including over Kafka, JMS, AMQP, Azure Service Bus, Amazon SQS/SNS and Google Pub/Sub.
* [Informatica Data 360 Connector and Scanner](informatica-data-360-connector-and-scanner.md) - Native connector for two-way batch and real-time data exchange with Salesforce Data 360, plus a catalogue scanner that brings Data 360 and Agentforce Marketing objects into CDGC lineage.
* [Informatica Database Ingestion and Replication](informatica-database-ingestion-and-replication.md) - Replicates relational and some non-relational databases to cloud warehouses, lakes, streaming platforms and databases, as an initial bulk load, as continuous log-based change capture, or as both in sequence.
* [Informatica File Ingestion and Replication](informatica-file-ingestion-and-replication.md) - Moves large numbers of files of any type between on-premises and cloud repositories, and tracks and monitors each transfer.
* [Informatica Streaming Ingestion and Replication](informatica-streaming-ingestion-and-replication.md) - Moves real-time streaming and machine data from sources such as message brokers, logs and IoT hubs to messaging systems and to lake or warehouse targets.

# Processing and transformation

* [Informatica Cloud Data Integration (CDI)](informatica-cloud-data-integration.md) - Visual ETL and ELT service: you design mappings from prebuilt transformations and connectors, run them as tasks, and chain tasks into taskflows.
* [Informatica Cloud Data Integration advanced mode](informatica-cdi-advanced-mode.md) - Runs Data Integration mappings on a Kubernetes-based advanced cluster for distributed processing of large and hierarchical data, with Python and Java code steps and machine learning model calls.
* [Informatica Cloud Data Integration SQL ELT mode](informatica-cdi-sql-elt-mode.md) - Converts mapping logic into native SQL and platform commands that run inside the target cloud warehouse, so data does not leave the warehouse's cloud while it is transformed.
* [Informatica PowerCenter](informatica-powercenter.md) - On-premises enterprise ETL server with a client designer, repository and workflow engine, and the historical core of Informatica's integration business.

# Query and compute

* [IDMC serverless runtime environment](informatica-serverless-runtime-environment.md) - Informatica-managed, single-tenant runtime that runs jobs, chiefly advanced-mode mappings, without the customer installing or maintaining Secure Agents, scaling the underlying cluster with the workload.

# Serving and activation

* [Informatica API Center](informatica-api-center.md) - Designs, publishes, secures with policies, groups and monitors REST APIs, either top-down from an API definition or bottom-up from published Application Integration processes.

# Analytics and BI

* [CLAIRE GPT](informatica-claire-gpt.md) - Conversational IDMC service that answers natural-language questions about metadata and data, finds assets, checks quality and creates or runs data management tasks with human oversight.

# Generative AI

* [CLAIRE Agents](informatica-claire-agents.md) - Prebuilt AI agents that plan and carry out multi-step data management work such as discovering trusted data, exploring MDM data, building ELT pipelines and writing data quality rules.
* [Informatica AI Agent Engineering](informatica-ai-agent-engineering.md) (unconfirmed) - No-code IDMC service for building, connecting and managing AI agents and multi-agent systems, including connecting to Informatica-managed MCP servers and building composite MCP servers from Application Integration processes.
* [Informatica AI recipes (Application Integration)](informatica-ai-recipes.md) - Prebuilt Application Integration processes for generative AI patterns such as AI agents, retrieval over documents, chat with a file, and LLM calls to several model providers.
* [Informatica Headless Data Management (Informatica MCP servers)](informatica-headless-data-management.md) - Exposes IDMC functions such as catalogue search, lineage, data quality, MDM lookups, job control and administration as governed MCP servers that external agents and AI tools can call without custom code.

# Metadata and discovery

* [Informatica CDGC lineage](informatica-cdgc-lineage.md) - Builds end-to-end lineage, including inferred links, across scanned databases, ETL tools, cloud platforms and BI tools, down to column level, for tracing and impact analysis.
* [Informatica Cloud Data Governance and Catalog (CDGC)](informatica-cloud-data-governance-and-catalog.md) - Catalogue and governance service that inventories technical, business and AI assets, links them to a business glossary, policies and stewards, classifies sensitive data, and shows data quality scores per asset.
* [Informatica Metadata Command Center (MCC)](informatica-metadata-command-center.md) - Administration service where you configure catalog sources and scanners that harvest metadata, lineage, profiles and classifications from source systems into the IDMC metadata repository.

# Data quality and observability

* [CLAIRE Data Quality Agent](informatica-claire-data-quality-agent.md) - AI agent that turns data quality requirements written in plain language into rule logic that can be reviewed and deployed to production.
* [Informatica Cloud Data Quality (CDQ)](informatica-cloud-data-quality.md) - Defines and runs rule specifications, cleansing, parsing, standardisation, deduplication and verification assets using reference dictionaries, and routes exceptions to people for review.
* [Informatica data observability](informatica-data-observability.md) - Learns normal trends in scanned source data, raises events for sudden deviations, grouped by metric and severity, and improves its alerts from how users respond to them.
* [Informatica Data Profiling](informatica-data-profiling.md) - Profiles columns in data sources to show value frequencies, patterns, data types and completeness.
* [Informatica Data Validation](informatica-data-validation.md) - Compares two data sets through repeatable test cases and test suites to verify that integration or migration output is complete and accurate, with reports and REST APIs.

# Master and reference data

* [Informatica Customer 360 SaaS](informatica-customer-360.md) - Prebuilt customer master application on MDM SaaS that consolidates customer records, relationships and inferred attributes into one shared view.
* [Informatica Multidomain MDM SaaS](informatica-multidomain-mdm-saas.md) - Cloud MDM service for modelling any business entity, matching and merging records from many sources into golden records with survivorship rules, and managing relationships and hierarchies through the Business 360 Console.
* [Informatica Product 360 SaaS](informatica-product-360.md) - Product information management application that centralises product data and digital assets, classifies products into hierarchies and prepares content for sales channels.
* [Informatica Reference 360](informatica-reference-360.md) - Manages shared reference data such as code lists, hierarchies and cross-system mappings with versions and approval workflows.
* [Informatica Supplier 360 SaaS](informatica-supplier-360.md) - Supplier master application covering supplier onboarding workflows, mastering, hierarchies, risk, performance and compliance data.

# Governance and compliance

* [Informatica CDGC AI governance](informatica-cdgc-ai-governance.md) - Catalogues AI models, multi-agent systems and their data and links them to policies, owners and lineage, including assets scanned from platforms such as Google Vertex AI.
* [Informatica Cloud Data Access Management (CDAM)](informatica-cloud-data-access-management.md) - Defines data filter, access control and de-identification policies once, driven by catalogue metadata, and enforces them by pushing them into data platforms or by applying them inside Informatica pipelines and marketplace deliveries.
* [Informatica Data Masking transformation](informatica-data-masking-transformation.md) - Mapping transformation that replaces sensitive values with realistic masked values per column while keeping referential integrity across tables, for non-production copies.

# Security and access

* [IDMC Administrator](informatica-administrator.md) - Organisation-wide administration service for users, groups, roles, SAML single sign-on, licences, runtime environments, connections and sub-organisations.

# Data sharing and collaboration

* [Informatica Cloud Data Marketplace (CDMP)](informatica-cloud-data-marketplace.md) - Internal data shop where owners publish data collections with terms of use, and consumers search, compare, order and receive data through approval and delivery workflows.

# Development and DataOps

* [CLAIRE Copilot for Data Integration](informatica-claire-copilot-data-integration.md) - Assistant in the Data Integration and Application Integration designers that generates, explains and summarises pipelines from natural-language prompts.
* [Informatica Test Data Management (TDM)](informatica-test-data-management.md) - On-premises product for configuring data subsetting, masking, synthetic data generation and sensitive data discovery for test environments from one web console.

# Platform operations

* [Informatica Cloud Data Integration FinOps](informatica-cdi-finops.md) - Shows the cost and resource use of each workload and pipeline, and recommends or applies tuning to lower IPU and cloud compute spend.
* [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](informatica-cdi-pc.md) - Runs existing PowerCenter sessions and workflows unchanged in a customer-hosted domain whose management, monitoring and upgrades are handled from IDMC.
* [Informatica Intelligent Data Management Cloud (IDMC)](informatica-idmc.md) - Multi-cloud SaaS platform that hosts all of Informatica's cloud data management services behind one control plane, with jobs run either on customer-hosted Secure Agents or on Informatica-managed serverless runtimes.
* [Informatica Operational Insights](informatica-operational-insights.md) - Monitoring service that shows the performance, health and efficiency of Informatica assets, including registered on-premises PowerCenter and Data Engineering domains as well as IDMC jobs.
* [Informatica PowerCenter Cloud Edition (PCCE)](informatica-powercenter-cloud-edition.md) - Modernisation bundle that runs PowerCenter workloads under IDMC management (CDI-PC), converts PowerCenter assets to native Cloud Data Integration (PC2CDI) and checks the converted output with Data Validation.
* [Informatica Processing Unit (IPU) consumption pricing](informatica-ipu-pricing.md) - Single consumption currency for IDMC services, with usage metered and reported by service, runtime, sub-organisation and sandbox, so spend can be tracked and charged back.

# Specialised data types

* [Informatica Unstructured Data Governance](informatica-unstructured-data-governance.md) (preview) - Scans, extracts metadata from and classifies unstructured files such as PDFs and text documents, and catalogues them in CDGC.
