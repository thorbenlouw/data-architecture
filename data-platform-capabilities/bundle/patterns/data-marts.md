---
type: Pattern
id: data-marts
title: Data marts
description: Subject- or department-specific sets of data shaped for one group of users.
uses:
- data-modelling
- sql-transformation
- semantic-layer
- metric-definitions
- materialised-views
- row-level-security
- workload-isolation
- data-certification
related: [data-warehouse, dimensional-modelling, one-big-table, data-mesh]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Marts come in three kinds, depending on where their data comes from. In Bill Inmon's approach, dependent marts are fed from a central enterprise warehouse and reshape its normalised data for one department. In Ralph Kimball's bus architecture, each mart is a dimensional model of one business process, such as orders or inventory, and marts share conformed dimensions so that together they form the warehouse. Independent marts are built straight from sources by one department and are the least controlled.

Marts give users a smaller, faster and simpler view, and let a department move without waiting for enterprise-wide agreement. Today they are often logical rather than physical: a schema, a set of views or a semantic model over shared tables, which avoids copies. Independent marts tend to produce conflicting numbers for the same measure, so the main design question is how marts share definitions. In a data mesh, domain data products play a similar role but are owned by the producing domain rather than the consuming department.

# When to use

- A department or function needs a simplified, purpose-built view of data in its own terms.
- Performance tuning or access control is easier to manage on a focused subset.
- You are building a warehouse incrementally, one business process at a time.

# Watch out for

- Independent marts built from sources duplicate logic and produce conflicting figures.
- Physical copies multiply storage, refresh jobs and access rules; prefer views or semantic models where performance allows.
- Mart sprawl makes it hard to know which version is authoritative, so certify and retire marts deliberately.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md): Design and document conceptual, logical and physical data models, and keep them in step with what is deployed.
- [SQL transformation](../capabilities/processing/sql-transformation.md): Transform data inside the platform using SQL, typically after it has been loaded.
- [Semantic layer](../capabilities/analytics-bi/semantic-layer.md): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md): Define, certify and version key business metrics with owners and calculation logic.
- [Materialised views](../capabilities/compute/materialised-views.md): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Row-level security](../capabilities/security/row-level-security.md): Restrict which rows each user sees based on who they are.
- [Workload isolation](../capabilities/compute/workload-isolation.md): Run different workloads on separate compute so one cannot slow or starve another.
- [Data certification](../capabilities/metadata/data-certification.md): Mark assets as trusted, deprecated or under review so consumers know what to rely on.

# Related patterns

- [Data warehouse](data-warehouse.md)
- [Dimensional modelling](dimensional-modelling.md)
- [One big table](one-big-table.md)
- [Data mesh](data-mesh.md)

# Where it appears

- **Use cases:** [Conversational analytics for business users](../use-cases/usecase-conversational-bi.md) · [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md) · [Self-service BI](../use-cases/usecase-self-service-bi.md)
- **Personas:** [Business user](../personas/persona-business-user.md) · [Data analyst](../personas/persona-data-analyst.md)
