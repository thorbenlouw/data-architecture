# Palantir

# Ingestion and integration

* [Palantir Data Connection](palantir-data-connection.md) - Application for configuring sources and running batch, file, streaming and media syncs into Foundry, exports back to external systems, and virtual tables that query external platforms without copying.

# Storage and table management

* [Iceberg tables in Palantir Foundry](palantir-iceberg-tables.md) (preview) - Apache Iceberg as an alternative Foundry table type, with an Iceberg REST catalogue that lets external clients such as Snowflake and Jupyter read Foundry-governed tables.
* [Palantir Global Branching](palantir-global-branching.md) - Branching that spans pipelines, the Ontology and applications so a change can be built and tested end to end in isolation and merged after per-resource approval.

# Processing and transformation

* [Palantir Code Repositories](palantir-code-repositories.md) - Web-based IDE backed by Git for writing Python, Java and SQL transforms and Ontology functions, with branches, pull requests, checks and builds.
* [Palantir Pipeline Builder](palantir-pipeline-builder.md) - Visual pipeline tool for building batch, incremental and streaming transformations with typed functions, LLM nodes, data expectations, unit tests, schedules and branch-based review.

# Orchestration

* [Palantir Automate](palantir-automate.md) - Rules that watch Ontology data or schedules and send notifications, run actions or call AIP Logic when conditions are met.

# Analytics and BI

* [AIP Analyst](palantir-aip-analyst.md) - AI assistant that answers analytical questions over Ontology data in natural language and can be embedded in Workshop and other applications.
* [Palantir Contour and Quiver](palantir-contour-quiver.md) - Point-and-click analysis tools, Contour for large tabular datasets and Quiver for Ontology objects and time series, producing shareable analyses and dashboards.

# Machine learning development

* [Palantir Modeling Objectives and model assets](palantir-modeling-objectives.md) - Foundry's model management, in which model assets built in Foundry or imported are evaluated, reviewed, released and deployed for batch or live use, then bound to the Ontology.

# Generative AI

* [AIP Chatbot Studio](palantir-aip-chatbot-studio.md) - Builder for chat agents that use retrieval context, Ontology tools and actions and give cited answers, distributable through Workshop, Marketplace or APIs.
* [AIP Logic and AIP Evals](palantir-aip-logic.md) - No-code builder for LLM-powered functions that read Ontology data, call tools and propose or apply edits, with AIP Evals test suites and metrics for checking their outputs.
* [Palantir AIP and AIP Model Catalog](palantir-aip.md) - Palantir's generative AI layer that provides governed access to commercial and open LLMs, capacity management and the AIP applications on top of Foundry and the Ontology.
* [Palantir MCP and Ontology MCP](palantir-mcp.md) - MCP servers that let external AI coding tools build on Foundry (Palantir MCP) and let external agents read and write Ontology data and run actions within set limits (Ontology MCP).

# Metadata and discovery

* [Palantir Data Lineage](palantir-data-lineage.md) - Interactive graph of how datasets, transforms, objects and applications depend on each other across Foundry, with schedules, build status and permissions shown in context.

# Data quality and observability

* [Palantir Data Health and data expectations](palantir-data-health.md) - Health checks on datasets and builds for freshness, schema, row counts and content, plus expectations declared in pipelines that fail or warn when data breaks rules.

# Governance and compliance

* [Palantir Sensitive Data Scanner and Cipher](palantir-sensitive-data-scanner-cipher.md) - Tools that scan Foundry datasets for sensitive data such as personal identifiers, and that encrypt, hash or obscure columns with managed keys and algorithms.

# Security and access

* [Palantir Foundry security controls](palantir-security-controls.md) - Mandatory controls (Organizations and Markings that follow data through lineage) combined with discretionary project roles, row and column policies, justification prompts and audit logs.

# Development and DataOps

* [Palantir Code Workspaces](palantir-code-workspaces.md) - Hosted JupyterLab, RStudio Workbench and VS Code environments in Foundry for exploratory analysis, data science and code-based work on Foundry data.
* [Palantir DevOps and Marketplace](palantir-devops-marketplace.md) - Packaging of pipelines, Ontology, models and applications into versioned products with release channels, and a storefront for installing and upgrading them across spaces and organisations.
* [Palantir Workshop](palantir-workshop.md) - Low-code builder for operational applications over Ontology objects, with tables, charts, maps, forms that run actions, and embedded AIP widgets.

# Platform operations

* [Palantir Apollo](palantir-apollo.md) - Continuous delivery system that deploys and upgrades Palantir and customer software across many environments, including on-premises, edge and disconnected networks, with release channels and change approvals.
* [Palantir Foundry](palantir-foundry.md) - Integrated data platform that combines connectors, pipelines, storage, the Ontology, analytics, application building, model integration and governance in one environment with shared lineage and security.
* [Palantir Resource Management](palantir-resource-management.md) - Administration views of compute and storage usage by project and resource, with limits for controlling consumption.

# Specialised data types

* [Palantir media sets and AIP Document Intelligence](palantir-media-sets.md) - Foundry storage and pipelines for unstructured files such as PDFs, images, audio and video, with AIP Document Intelligence strategies for extracting text, tables and fields.
* [Palantir Ontology](palantir-ontology.md) - Semantic and operational layer that maps datasets, virtual tables and models to business object types, properties and links, with action types and functions that write decisions back.
