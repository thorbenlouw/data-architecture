---
type: Capability
id: analytics-bi
title: Analytics and BI
description: Help people explore, visualise and report on data to make decisions.
aliases: [business intelligence, visualisation]
broader: []
related: [ai-context-layer, query-acceleration, workload-isolation, row-level-security, data-certification]
depends_on: [sql-access]
order: 7
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Analytics and BI is where most people meet the data platform. It turns modelled tables into numbers people act on: a semantic layer fixes what each measure means, and a set of tools presents those measures as dashboards, formatted reports, spreadsheets, alerts or answers to typed questions.

The parts sit in tiers. The semantic layer and governed metrics sit closest to the data and give every tool the same definition of, say, an active customer. Above them, consumption tools serve different needs: dashboards for monitoring, paginated reports for operational and regulatory output, ad hoc analysis for one-off questions, and conversational and augmented analytics for people who do not write SQL. Embedded analytics and the consumer portal decide where results appear.

Some capabilities move data the other way. Write-back and planning let users enter figures, forecasts and corrections that flow back into governed tables. The main architectural question is where business logic lives: in one shared layer, or copied into each tool, where it drifts.

# Key considerations

- Decide where calculation logic lives before choosing tools. Logic held inside each BI tool's own model drifts apart and cannot be reused by spreadsheets or AI tools.
- BI workloads are many small concurrent queries with people waiting for them. Size and isolate compute for that pattern, and plan caching or pre-aggregation.
- Enforce access controls in the platform, not only in the BI tool, so a user who switches to SQL or a spreadsheet sees the same rows.
- Extracts copy data into the BI tool for speed but create a second copy to secure and refresh. Live queries avoid this but depend on platform performance.
- Self-service needs curation. Without certification and a clear home for trusted content, dashboard counts grow into thousands of near duplicates nobody owns.

# Questions to ask

- Who consumes data, and how: monitoring dashboards, regulatory reports, spreadsheets, embedded in products, or questions in natural language?
- How many users and concurrent queries are expected at peak, and what response time do they expect?
- Do key metrics give different answers in different tools today, and who settles which is right?
- Do any users need to enter data, plans or corrections, not only read?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Ad hoc analysis](ad-hoc-analysis.md), [Alerts and subscriptions](data-alerting.md), [Analytical sandboxes](analytical-sandboxes.md), [Augmented analytics](augmented-analytics.md), [Conversational analytics](conversational-analytics.md), [Dashboards and interactive reports](dashboards-reports.md), [Data consumer portal](data-consumer-portal.md), [Data entry and write-back](data-writeback.md), [Data trust indicators](../metadata/data-trust-indicators.md), [Embedded analytics](embedded-analytics.md), [Experimentation and causal measurement](experimentation.md), [Packaged analytics content](packaged-analytics.md), [Paginated reports](paginated-reports.md), [Planning and forecasting](enterprise-planning.md), [Self-service data preparation](../processing/data-preparation.md), [Semantic layer](semantic-layer.md), [Spreadsheet integration](spreadsheet-integration.md) |
| Related | [Serving and activation](../serving/serving.md), [AI context layer](../metadata/ai-context-layer.md), [Data certification](../metadata/data-certification.md), [Query acceleration](../compute/query-acceleration.md), [Row-level security](../security/row-level-security.md), [Workload isolation](../compute/workload-isolation.md) |
| Depends on | [SQL and programmatic access](../serving/sql-access.md) |

# Where it appears

- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 122 technologies; see their pages.
