---
type: Capability
id: analytical-sandboxes
title: Analytical sandboxes
description: Give analysts and teams governed spaces on the platform where they can upload files, create tables and try out analyses, with quotas, expiry and the platform's access controls.
aliases: [user sandboxes, personal schemas, data lab, scratch space, team analysis space, file upload]
broader: [analytics-bi, self-service-provisioning]
related: [data-preparation, ad-hoc-analysis, data-classification, data-retention, test-data-management]
depends_on: [access-control, spend-controls]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A sandbox is a schema, workspace or folder where an analyst or a small team may write as well as read. A pricing analyst uploads a competitor price list from a spreadsheet, joins it to certified sales tables, saves intermediate results and shares them with two colleagues, all inside the platform. The platform creates the space on request, limits its storage and compute, keeps masking and row policies on anything copied from governed data, scans uploaded files for sensitive content and removes what has not been used for an agreed period.

Analysts will combine data whatever the platform offers. Without a sandbox they do it on laptops, in exported spreadsheets or in unmanaged cloud storage, out of reach of access control, classification and retention. A sandbox keeps that work where it can be governed and later promoted: a table that proves useful moves into the curated layer with an owner and tests. Data preparation concerns tools for reshaping data; engineering environments are templated for building pipelines.

# Key considerations

- Set expiry and quotas by default with an easy way to extend them, or sandboxes grow into an unmanaged second warehouse.
- Stop sandboxes becoming a route around controls. Masked values must stay masked when copied, and sharing beyond the team should need the data owner's approval.
- Classify uploaded files and new tables as they are created, since uploads are a common way for personal data to enter the platform.
- Provide a route to promote a sandbox table into governed data, and flag sandbox tables that dashboards or other teams start to depend on.

# Questions to ask

- Where do analysts combine their own files with platform data today?
- How much personal or confidential data sits in personal copies outside the platform?
- What should happen to a sandbox when its owner leaves or it has not been used for months?
- Should sandbox results be shareable, and with whom?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md), [Self-service provisioning](../platform-operations/self-service-provisioning.md) |
| Related | [Ad hoc analysis](ad-hoc-analysis.md), [Data classification](../governance/data-classification.md), [Retention and disposal](../governance/data-retention.md), [Self-service data preparation](../processing/data-preparation.md), [Test data management](../development-lifecycle/test-data-management.md) |
| Depends on | [Access control](../security/access-control.md), [Budgets and spend controls](../platform-operations/spend-controls.md) |

# Where it appears

- **Use cases:** [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [Data analyst](../../personas/persona-data-analyst.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 6 – Adaptability · [DCAM v3](../../frameworks/framework-edm-dcam.md): 8 Analytics Management

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Unified Studio](../../technologies/aws/aws-sagemaker-unified-studio.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric workspaces](../../technologies/microsoft/fabric-workspaces.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog volumes](../../technologies/databricks/databricks-volumes.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Sigma Computing](../../technologies/independent/sigma.md) |
