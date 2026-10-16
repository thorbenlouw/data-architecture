---
type: Capability
id: enterprise-planning
title: Planning and forecasting
description: Build budgets, forecasts and plans over governed data, with versions, allocations and approval workflows.
aliases: [FP&A planning, xP&A]
broader: [analytics-bi]
related:
- data-writeback
- master-data-management
- hierarchy-management
- packaged-analytics
- spreadsheet-integration
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A planner loads last year's actuals from the platform, applies growth drivers by product and region, allocates central costs to departments by headcount, and compares the result with a pessimistic scenario. Plans are held as named versions, such as the annual budget or a second-quarter reforecast, and move through submission and approval workflows. Many planning tools use multidimensional models, in which a figure entered at a total can be spread down to lower levels automatically.

Planning differs from reporting because users create and change numbers, and because the model needs time hierarchies, versions and allocation logic. It matters when plans live in disconnected spreadsheets that are slow to consolidate and cannot be compared with actuals automatically. Integration with the platform runs both ways: actuals and master data flow in, and approved plans flow back so they can be reported alongside actuals.

# Key considerations

- Share dimensions such as accounts, cost centres and products with master data, or plans and actuals will not line up.
- Approved plans must flow back to the platform for variance reporting. Check how often and at what level of detail.
- Allocation and spreading engines behave differently from SQL. Test performance with realistic model sizes.
- Plans hold sensitive forward-looking figures, so access often needs to vary by version and department.

# Questions to ask

- How are budgets and forecasts built today, and how long does consolidation take?
- Which drivers and allocations must the model support?
- How often are plans revised, and must every version be kept?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Approved manual adjustments](manual-adjustments.md), [Data entry and write-back](data-writeback.md), [Hierarchy management](../master-data/hierarchy-management.md), [Master data management](../master-data/master-data-management.md), [Packaged analytics content](packaged-analytics.md), [Pretrained predictive models](../machine-learning/pretrained-predictive-models.md), [Spreadsheet integration](spreadsheet-integration.md) |

# Where it appears

- **Use cases:** [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (benefits from) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from)
- **Personas:** [Business user](../../personas/persona-business-user.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Planning in Fabric IQ](../../technologies/microsoft/fabric-iq-planning.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Analytics Cloud](../../technologies/sap/sap-analytics-cloud.md) |
