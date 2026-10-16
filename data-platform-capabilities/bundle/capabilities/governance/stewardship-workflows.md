---
type: Capability
id: stewardship-workflows
title: Stewardship workflows
description: Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.
aliases:
- governance workflows
- steward task queue
- approval workflows
- stewardship console
- governance tasks
broader: [governance]
related: [access-requests, business-glossary, data-issue-management, data-classification, active-metadata]
depends_on: [data-ownership]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Much of a steward's platform time goes on approving and reviewing: a drafted glossary term, a column a scanner thinks holds national insurance numbers, an access request, a disputed customer merge, a quarterly check that a domain's descriptions are still right. A stewardship workflow turns each into a task with an assignee taken from the ownership record, a due date, escalation when it is missed, and an outcome stored against the asset. Stewards work from one queue, approve similar items in bulk, delegate when away and act from email or chat.

Without it, requests arrive by message, wait for whoever is remembered as responsible and leave no evidence of who decided what. With it, governance teams see backlogs and decision times per domain and can show auditors that reviews happened. Workflow engines come inside governance catalogues and master data tools, or as ticketing platforms connected to them. Data issue management tracks fixing data problems; the access request workflow is one flow that can run on the same engine.

# Key considerations

- Take assignees from ownership records by domain and asset, so tasks reach a person without a central triage step.
- Design for stewards with little time. Bulk approval, the evidence shown on each task and actions from tools they already use matter more than features.
- Set deadlines and escalation for tasks with legal or audit weight, such as access to restricted data or confirming personal-data labels.
- Keep the number of workflows small and standard. Each custom flow has to be reworked when the operating model changes.
- Report backlog and time to decision per domain, so overloaded stewards are visible before the backlog becomes a risk.

# Questions to ask

- Which governance decisions do stewards make each week, and how do the requests reach them today?
- Can anyone show who approved a glossary term, a classification or an access grant, and when?
- Should governance tasks live in the governance tool, the IT service management tool or both?
- How much time each week do stewards actually have for this work?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Related | [Access requests and reviews](../security/access-requests.md), [Active metadata](../metadata/active-metadata.md), [Business glossary](../metadata/business-glossary.md), [Data classification](data-classification.md), [Data issue management](../data-quality/data-issue-management.md) |
| Depends on | [Ownership and stewardship](data-ownership.md) |

# Where it appears

- **Personas:** [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 7 Entitlements and Access for Sensitive Data (Accessibility and usage) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Governance · [DCAM v3](../../frameworks/framework-edm-dcam.md): 4 Business Data Knowledge; 6 Govern Data & DMP · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-150 – Roles and responsibilities · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Roles

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-unified-catalog.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Governance and Catalog (CDGC)](../../technologies/informatica/informatica-cloud-data-governance-and-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Master Data Governance](../../technologies/sap/sap-master-data-governance.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alation Intelligence Operating System (AIOS)](../../technologies/independent/alation-aios.md), [Ataccama ONE Master Data Management](../../technologies/independent/ataccama-one-mdm.md), [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [DataHub Cloud](../../technologies/independent/datahub-cloud.md), [Profisee MDM](../../technologies/independent/profisee-mdm.md), [Reltio Multidomain MDM](../../technologies/independent/reltio-multidomain-mdm.md), [Semarchy Data Platform](../../technologies/independent/semarchy-data-platform.md) |
