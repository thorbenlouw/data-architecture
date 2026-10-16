---
type: Use Case
id: usecase-platform-modernisation
title: Legacy warehouse migration
description: Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
aliases: [Hadoop migration, Teradata migration, warehouse modernisation]
requires:
- {capability: platform-migration, level: 3, why: 'Inventory, assessment and wave planning must follow a repeatable method across hundreds of workloads.'}
- {capability: code-translation, level: 3, why: 'Thousands of SQL scripts, stored procedures and ETL jobs must be converted with as much automation as possible.'}
- {capability: database-migration, level: 2, why: Schemas and data types must be converted to the target platform.}
- {capability: bulk-data-transfer, level: 2, why: 'Years of history, often hundreds of terabytes, must be moved within the plan.'}
- {capability: change-data-capture, level: 2, why: Old and new platforms must stay in step during parallel running.}
- {capability: data-reconciliation, level: 3, why: Outputs on the new platform must be proven to match the old before cut-over.}
- {capability: data-testing, level: 3, why: Regression tests compare reports and tables between old and new on every wave.}
- {capability: workflow-orchestration, level: 3, why: Legacy schedules and dependencies must be rebuilt and run reliably.}
- {capability: table-lineage, level: 2, why: 'Migration waves are planned from dependencies between tables, jobs and reports.'}
- {capability: role-based-access, level: 3, why: Permissions must be rebuilt on the new platform without widening access.}
- {capability: identity-authentication, level: 3, why: Users and service accounts must authenticate through central identity on the new platform.}
- {capability: network-security, level: 2, why: Private connectivity between on-premises sources and the cloud platform must be in place before data moves.}
- capability: environment-promotion
  level: 2
  why: Hundreds of migrated workloads must reach production through one tested, repeatable route rather than hand deployment.
benefits_from:
- {capability: usage-metadata, why: Finds unused tables and reports that can be retired rather than migrated.}
- {capability: infrastructure-as-code, why: Builds the new platform consistently across environments.}
- {capability: spend-controls, why: Catches unexpected consumption costs early.}
- {capability: cost-attribution, why: Shows each team its cost on the new platform.}
- {capability: open-table-formats, why: Reduces lock-in on the target platform.}
- {capability: query-federation, why: Lets users query data still on the legacy platform during the transition.}
- {capability: data-engineering-agents, why: 'Speeds up conversion, testing and fixing of translated code.'}
- {capability: mainframe-integration, why: Covers sources that feed the legacy warehouse from mainframes.}
- {capability: cost-forecasting, why: Forecasts running and dual-running costs per wave against the business case.}
- capability: compute-options
  why: Choosing serverless, provisioned, single-node or cluster compute per migrated workload decides whether running costs meet the business case.
personas:
- persona-data-architect
- persona-platform-engineer
- persona-data-engineer
- persona-analytics-engineer
- persona-finops-practitioner
- persona-cdo
- persona-security-officer
patterns: [lakehouse, data-warehouse, elt, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Many organisations still run on-premises warehouses or Hadoop clusters that are costly to licence and support, slow to change, and poorly suited to streaming, machine learning and AI. Migration moves data, code, schedules, permissions and users to a cloud platform. It normally runs in waves: inventory and assess what exists, translate SQL and ETL code, transfer history, keep the new platform in step with the old during a parallel run, reconcile outputs, cut over consumers and switch off the old system.

Good looks like each wave cut over on schedule with outputs proven to match, unused objects retired rather than moved, report service levels no worse than before, and cloud running costs within the business case. A migration that only copies the old design keeps its problems and adds a new bill.

# Non-functional requirements

- Outputs match the legacy platform within agreed tolerances over a parallel-run period before cut-over.
- Cut-over downtime for each wave fits an agreed window, often a weekend.
- Report and pipeline service levels are no worse than on the legacy platform.
- The migration finishes before legacy licence or support contracts end.
- Running costs after migration fall within the business case.

# Risks

- Lift-and-shift moves unused objects and poor designs, keeping old problems on a new bill.
- Reconciliation starts late and differences undermine trust in the new platform.
- Stored procedures and ETL logic turn out more complex than estimated and the plan slips.
- Dual running lasts far longer than planned and doubles costs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Platform migration](../capabilities/platform-operations/platform-migration.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Inventory, assessment and wave planning must follow a repeatable method across hundreds of workloads. |
| [Code and SQL translation](../capabilities/platform-operations/code-translation.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Thousands of SQL scripts, stored procedures and ETL jobs must be converted with as much automation as possible. |
| [Database migration](../capabilities/platform-operations/database-migration.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Schemas and data types must be converted to the target platform. |
| [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Years of history, often hundreds of terabytes, must be moved within the plan. |
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Old and new platforms must stay in step during parallel running. |
| [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Outputs on the new platform must be proven to match the old before cut-over. |
| [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 3 (Defined) | Regression tests compare reports and tables between old and new on every wave. |
| [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | 3 (Defined) | Legacy schedules and dependencies must be rebuilt and run reliably. |
| [Table-level lineage](../capabilities/metadata/table-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | Migration waves are planned from dependencies between tables, jobs and reports. |
| [Role-based access control](../capabilities/security/role-based-access.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Permissions must be rebuilt on the new platform without widening access. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Users and service accounts must authenticate through central identity on the new platform. |
| [Network security](../capabilities/security/network-security.md) | [Security and access](../capabilities/security/security.md) | 2 (Managed) | Private connectivity between on-premises sources and the cloud platform must be in place before data moves. |
| [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 2 (Managed) | Hundreds of migrated workloads must reach production through one tested, repeatable route rather than hand deployment. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | Finds unused tables and reports that can be retired rather than migrated. |
| [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md) | Builds the new platform consistently across environments. |
| [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) | Catches unexpected consumption costs early. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | Shows each team its cost on the new platform. |
| [Open table formats](../capabilities/storage/open-table-formats.md) | Reduces lock-in on the target platform. |
| [Query federation](../capabilities/compute/query-federation.md) | Lets users query data still on the legacy platform during the transition. |
| [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md) | Speeds up conversion, testing and fixing of translated code. |
| [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md) | Covers sources that feed the legacy warehouse from mainframes. |
| [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md) | Forecasts running and dual-running costs per wave against the business case. |
| [Compute provisioning options](../capabilities/compute/compute-options.md) | Choosing serverless, provisioned, single-node or cluster compute per migrated workload decides whether running costs meet the business case. |

# Personas

- [Data architect](../personas/persona-data-architect.md): Designs the data platform and how data flows, is modelled and is governed across the organisation.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [FinOps practitioner](../personas/persona-finops-practitioner.md): Tracks, allocates and optimises what the data platform costs.
- [Chief data officer](../personas/persona-cdo.md): Accountable for the organisation's data strategy, value, risk and governance.
- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.

# Patterns

- [Lakehouse](../patterns/lakehouse.md)
- [Data warehouse](../patterns/data-warehouse.md)
- [ELT](../patterns/elt.md)
- [Medallion architecture](../patterns/medallion-architecture.md)

# Frameworks that apply

- [CDMC (Cloud Data Management Capabilities)](../frameworks/framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [DORA (Digital Operational Resilience Act)](../frameworks/framework-eu-dora.md): Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.
- [EU Data Act](../frameworks/framework-eu-data-act.md): Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 12 of 13 | [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 10 of 13 (+1 in preview) | [Database migration](../capabilities/platform-operations/database-migration.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) (preview only) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 13 of 13 |  |
| [Snowflake](../platforms/platform-snowflake.md) | 10 of 13 | [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) |
| [Databricks](../platforms/platform-databricks.md) | 10 of 13 | [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 6 of 13 (+1 in preview) | [Platform migration](../capabilities/platform-operations/platform-migration.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Table-level lineage](../capabilities/metadata/table-lineage.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) (preview only) |
| [Informatica](../platforms/platform-informatica.md) | 9 of 13 | [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Network security](../capabilities/security/network-security.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 5 of 13 | [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) |
| [Oracle](../platforms/platform-oracle.md) | 5 of 13 | [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Table-level lineage](../capabilities/metadata/table-lineage.md), [Role-based access control](../capabilities/security/role-based-access.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) |
| [SAP](../platforms/platform-sap.md) | 4 of 13 | [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Role-based access control](../capabilities/security/role-based-access.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) |
| [Teradata](../platforms/platform-teradata.md) | 1 of 13 | [Platform migration](../capabilities/platform-operations/platform-migration.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Table-level lineage](../capabilities/metadata/table-lineage.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) |
| [IBM](../platforms/platform-ibm.md) | 1 of 13 | [Platform migration](../capabilities/platform-operations/platform-migration.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Table-level lineage](../capabilities/metadata/table-lineage.md), [Role-based access control](../capabilities/security/role-based-access.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) |
| [Palantir](../platforms/platform-palantir.md) | 5 of 13 | [Platform migration](../capabilities/platform-operations/platform-migration.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 9 of 13 | [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Network security](../capabilities/security/network-security.md) |
| [Independent vendors](../platforms/platform-independent.md) | 5 of 13 | [Platform migration](../capabilities/platform-operations/platform-migration.md), [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Role-based access control](../capabilities/security/role-based-access.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md) |
