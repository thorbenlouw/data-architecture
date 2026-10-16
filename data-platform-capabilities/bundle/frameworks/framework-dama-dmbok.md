---
type: Framework
id: framework-dama-dmbok
title: DAMA-DMBOK 2
description: The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.
aliases: [DMBOK, DMBOK2, DAMA-DMBOK, DAMA DMBOK, Data Management Body of Knowledge, DAMA wheel]
kind: body-of-knowledge
publisher: DAMA International
resource: https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/
related: [framework-edm-dcam, framework-iso-8000, framework-edm-cdmc]
applies_to:
- persona-data-architect
- persona-cdo
- persona-data-steward
- usecase-enterprise-reporting
- usecase-customer-360
mappings:
- ref: Data Governance
  summary: Setting up decision rights, accountability, policies and stewardship so that data is managed as an asset, and measuring how well that works.
  capabilities:
  - data-ownership
  - stewardship-workflows
  - data-policy-management
  - data-domains
  - governance-metrics
  - compliance-evidence
- ref: Data Architecture
  summary: Defining the enterprise blueprint for data, its flows and the technology that supports it, aligned with business strategy.
  capabilities: [data-modelling, data-lineage, metadata-interoperability, data-domains, deployment-options]
- ref: Data Modelling and Design
  summary: Discovering, analysing and documenting data requirements as conceptual, logical and physical models.
  capabilities: [data-modelling, schema-change-management, schema-evolution]
- ref: Data Storage and Operations
  summary: Designing, running and supporting stored data, including database administration, backup and recovery, performance tuning, archiving and migration.
  capabilities:
  - backup-restore
  - cross-region-failover
  - query-performance-analysis
  - table-maintenance
  - storage-tiering
  - database-migration
  - open-table-formats
- ref: Data Security
  summary: Protecting data through policies and controls for authentication, authorisation, access and auditing, based on how confidential the data is.
  capabilities:
  - identity-authentication
  - access-control
  - encryption
  - column-masking
  - data-classification
  - audit-logging
  - data-security-posture
- ref: Data Integration and Interoperability
  summary: Moving and consolidating data within and between systems through batch, replication, messaging and virtualisation.
  capabilities:
  - batch-ingestion
  - change-data-capture
  - database-replication
  - event-streaming
  - message-queuing
  - application-integration
  - query-federation
- ref: Document and Content Management
  summary: Managing the lifecycle of unstructured and semi-structured content such as documents, records and media.
  capabilities: [unstructured-data, unstructured-ingestion, document-processing, full-text-search, data-retention]
- ref: Reference and Master Data
  summary: Managing shared core entities and code lists so that they are consistent and trusted across systems.
  capabilities:
  - master-data-management
  - reference-data-management
  - entity-resolution
  - survivorship
  - hierarchy-management
- ref: Data Warehousing and Business Intelligence
  summary: Planning and running the analytical environment that integrates data for reporting, analysis and decision support.
  capabilities:
  - sql-transformation
  - sql-query-engine
  - semantic-layer
  - dashboards-reports
  - ad-hoc-analysis
  - paginated-reports
- ref: Metadata Management
  summary: Collecting, integrating and making available the business, technical and operational metadata that describes data.
  capabilities:
  - data-catalogue
  - business-glossary
  - metadata-harvesting
  - data-lineage
  - usage-metadata
  - metadata-interoperability
- ref: Data Quality
  summary: Planning and running activities that measure, monitor and improve data so it is fit for its intended use.
  capabilities:
  - data-quality-rules
  - data-profiling
  - data-quality-scorecards
  - data-observability
  - data-cleansing
  - data-issue-management
- ref: Data Handling Ethics
  summary: Using data in ways that are fair, transparent and respectful of the people it describes, beyond what the law requires.
  capabilities: [privacy-management, consent-management, data-usage-rights, fairness-assessment, ai-governance]
- ref: Big Data and Data Science
  summary: Managing large and varied data sets and the analytical and machine learning work that draws insight from them.
  capabilities:
  - distributed-processing
  - object-storage
  - notebooks
  - feature-engineering
  - model-training
  - experiment-tracking
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

DAMA-DMBOK is DAMA International's guide to the discipline of data management, organised as the "DAMA wheel" of eleven knowledge areas with data governance at the centre, plus chapters on data handling ethics and big data and data science. Data managers, governance teams and CDMP-certified practitioners use it as a shared vocabulary, and architects use it to check that a platform covers the whole data lifecycle rather than storage and processing alone. The current edition is the second edition, with a revised printing that DAMA released in 2024. DMBOK 3.0 is in development: the project started in mid-2025, its published plan has content development and iterative draft releases running from April to December 2026, finalisation from January 2027 and publication between April and July 2027, with new coverage of AI, cloud and modern data platforms.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Data Governance | Setting up decision rights, accountability, policies and stewardship so that data is managed as an asset, and measuring how well that works. | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Policy management](../capabilities/governance/data-policy-management.md), [Data domains](../capabilities/governance/data-domains.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| Data Architecture | Defining the enterprise blueprint for data, its flows and the technology that supports it, aligned with business strategy. | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Data domains](../capabilities/governance/data-domains.md), [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md) |
| Data Modelling and Design | Discovering, analysing and documenting data requirements as conceptual, logical and physical models. | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md) |
| Data Storage and Operations | Designing, running and supporting stored data, including database administration, backup and recovery, performance tuning, archiving and migration. | [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Open table formats](../capabilities/storage/open-table-formats.md) |
| Data Security | Protecting data through policies and controls for authentication, authorisation, access and auditing, based on how confidential the data is. | [Identity and authentication](../capabilities/security/identity-authentication.md), [Access control](../capabilities/security/access-control.md), [Encryption](../capabilities/security/encryption.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Data classification](../capabilities/governance/data-classification.md), [Audit logging](../capabilities/security/audit-logging.md), [Data security posture management](../capabilities/security/data-security-posture.md) |
| Data Integration and Interoperability | Moving and consolidating data within and between systems through batch, replication, messaging and virtualisation. | [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Query federation](../capabilities/compute/query-federation.md) |
| Document and Content Management | Managing the lifecycle of unstructured and semi-structured content such as documents, records and media. | [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Retention and disposal](../capabilities/governance/data-retention.md) |
| Reference and Master Data | Managing shared core entities and code lists so that they are consistent and trusted across systems. | [Master data management](../capabilities/master-data/master-data-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md) |
| Data Warehousing and Business Intelligence | Planning and running the analytical environment that integrates data for reporting, analysis and decision support. | [SQL transformation](../capabilities/processing/sql-transformation.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md) |
| Metadata Management | Collecting, integrating and making available the business, technical and operational metadata that describes data. | [Data catalogue](../capabilities/metadata/data-catalogue.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md) |
| Data Quality | Planning and running activities that measure, monitor and improve data so it is fit for its intended use. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md) |
| Data Handling Ethics | Using data in ways that are fair, transparent and respectful of the people it describes, beyond what the law requires. | [Privacy management](../capabilities/governance/privacy-management.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [AI governance](../capabilities/governance/ai-governance.md) |
| Big Data and Data Science | Managing large and varied data sets and the analytical and machine learning work that draws insight from them. | [Distributed processing](../capabilities/processing/distributed-processing.md), [Object storage](../capabilities/storage/object-storage.md), [Notebooks](../capabilities/development-lifecycle/notebooks.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model training](../capabilities/machine-learning/model-training.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md) |

# Related frameworks

- [DCAM v3](framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.
- [ISO 8000 (data quality)](framework-iso-8000.md): A series of international standards on data quality, covering concepts, quality management processes, profiling, rules, master data exchange and sensor data.
- [CDMC (Cloud Data Management Capabilities)](framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.

# Applies to

- [Data architect](../personas/persona-data-architect.md) (persona): Designs the data platform and how data flows, is modelled and is governed across the organisation.
- [Chief data officer](../personas/persona-cdo.md) (persona): Accountable for the organisation's data strategy, value, risk and governance.
- [Data steward](../personas/persona-data-steward.md) (persona): Looks after the definition, quality and proper use of data in a business domain.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md) (use case): Produce trusted, consistent KPIs and management reports across the organisation.
- [Customer 360](../use-cases/usecase-customer-360.md) (use case): Give every channel a single, trusted view of each customer.
