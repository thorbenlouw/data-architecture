---
type: Capability
id: data-slas
title: Data service levels
description: Set and track service levels for data products, such as freshness, availability and quality.
aliases: [data SLOs, data SLAs]
broader: [data-products]
related:
- data-contracts
- data-quality-scorecards
- data-observability
- pipeline-monitoring
- data-issue-management
depends_on: [freshness-monitoring]
tags: [data-products]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Typical targets are freshness, such as the orders table updated by 06:00 UTC on business days; availability of the serving endpoint; completeness; and the share of quality checks passed. They come with support terms such as response time to incidents. The vocabulary comes from site reliability practice: an indicator is the measurement, an objective is the internal target, and an agreement is the promise made to consumers, with agreed consequences if it is missed.

Service levels let consumers judge whether a product is reliable enough for their use, and give producers a clear definition of success. They also set priorities: a product feeding a regulatory return needs tighter targets and on-call support than one used for monthly exploration. Targets are declared in contracts or specifications, measured by freshness monitoring and observability, and published with their history so consumers can see a product's track record.

# Key considerations

- Set targets from consumer needs, not from what pipelines happen to achieve. Ask when the data is actually used.
- Each target needs an automatic measurement. A service level nobody measures is a wish.
- Tighter targets cost more in compute, redundancy and on-call staff. Agree who funds them.
- Upstream dependencies cap what a product can promise. Follow service levels through lineage to find the weak links.

# Questions to ask

- When do consumers need the data, and what happens to them if it is late?
- Which products support regulatory, financial or customer-facing processes?
- Who is on call when a service level is missed, and how are consumers told?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data products](data-products.md) |
| Broader | [Data products](data-products.md) |
| Related | [Cross-region and cross-cloud sharing](../data-sharing/cross-region-sharing.md), [Data contracts](data-contracts.md), [Data issue management](../data-quality/data-issue-management.md), [Data observability](../data-quality/data-observability.md), [Data quality scorecards](../data-quality/data-quality-scorecards.md), [Data trust indicators](../metadata/data-trust-indicators.md), [Data-aware orchestration](../orchestration/asset-based-orchestration.md), [Freshness monitoring](../data-quality/freshness-monitoring.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md), [Platform incident management](../platform-operations/platform-incident-management.md), [Workload management](../compute/workload-management.md) |
| Depends on | [Freshness monitoring](../data-quality/freshness-monitoring.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from) · [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Data product owner](../../personas/persona-data-product-owner.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data products](../../maturity/track-data-products.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 5 – Timeliness; Principle 10 – Frequency · [Data mesh principles](../../frameworks/framework-data-mesh.md): Data as a product · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Service-Level Agreement

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data products](../../technologies/google-cloud/gcp-knowledge-catalog-data-products.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Open Data Contract Standard (ODCS)](../../technologies/open-source/open-data-contract-standard.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Astronomer Astro](../../technologies/independent/astronomer-astro.md) |
