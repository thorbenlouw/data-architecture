---
type: Capability
id: data-trust-indicators
title: Data trust indicators
description: Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents.
aliases: [trust signals, data health indicators, data quality warnings, health badges, reliability status]
broader: [data-catalogue, analytics-bi]
related:
- data-certification
- data-issue-management
- data-quality-scorecards
- data-consumer-portal
- data-slas
depends_on: [freshness-monitoring, data-quality-rules, table-lineage]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A trust indicator combines several signals about an asset into a status a consumer can read at a glance, in the tool they are using rather than only in the catalogue. A sales dashboard might carry a banner saying the orders data was last updated at 06:10, two of its 40 checks failed overnight and an incident is open, with a link to the owner. The same status can sit beside a table in a SQL editor, on a spreadsheet connection or under an AI assistant's answer. It is drawn from certification, freshness, quality results, open issues and upstream failures found through lineage.

Without it, consumers find stale or broken data by acting on it. Certification differs: an owner sets it against criteria and it changes rarely, while trust indicators are computed from live results and can change by the hour. Delivery ranges from warnings built into BI tools, through browser extensions that overlay catalogue status, to status fields that applications and agents read through APIs.

# Key considerations

- Keep the indicator simple, such as three states with a one-line reason. A composite score nobody can explain is soon ignored.
- Carry status through lineage to the dashboards and reports people actually open, or warnings stay on tables consumers never see.
- Decide who may suppress a warning and record it, so one known false alarm does not teach people to ignore every warning.
- Check which consumption tools can show status natively and which need an extension or API, and whether AI assistants receive it with their context.

# Questions to ask

- How do report users find out today that data is late or wrong?
- Which tools do consumers open most, and can they display status from the catalogue or observability tools?
- Should a failing check hide a dashboard, warn on it, or only notify its owner?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data catalogue](data-catalogue.md), [Analytics and BI](../analytics-bi/analytics-bi.md) |
| Related | [Data certification](data-certification.md), [Data consumer portal](../analytics-bi/data-consumer-portal.md), [Data issue management](../data-quality/data-issue-management.md), [Data quality scorecards](../data-quality/data-quality-scorecards.md), [Data service levels](../data-products/data-slas.md) |
| Depends on | [Freshness monitoring](../data-quality/freshness-monitoring.md), [Data quality rules](../data-quality/data-quality-rules.md), [Table-level lineage](table-lineage.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 4, Measured)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 9 – Clarity and usefulness · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 3 Authoritative Data Sources and Provisioning Points (Governance and accountability); 11 Data Quality Measurement (Data lifecycle) · [Data mesh principles](../../frameworks/framework-data-mesh.md): Data as a product · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Management Ports

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Catalog](../../technologies/aws/aws-sagemaker-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [OneLake catalog](../../technologies/microsoft/fabric-onelake-catalog.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data quality](../../technologies/google-cloud/gcp-knowledge-catalog-data-quality.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Catalog Explorer](../../technologies/databricks/databricks-catalog-explorer.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alation Intelligence Operating System (AIOS)](../../technologies/independent/alation-aios.md), [Atlan](../../technologies/independent/atlan.md), [Collibra Data Catalog](../../technologies/independent/collibra-data-catalog.md), [Secoda](../../technologies/independent/secoda.md), [Tableau Cloud](../../technologies/independent/tableau-cloud.md) |
