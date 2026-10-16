---
type: Capability
id: development-lifecycle
title: Development and DataOps
description: Build, test and release data and AI workloads safely and repeatably, from first commit to production.
aliases: [path to live, DataOps]
broader: []
related: [platform-operations, transformation-as-code, ml-cicd, data-contracts, data-observability]
order: 18
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This domain covers how data and AI work moves from an idea in a notebook to a job that runs in production and that other people depend on. Its parts follow the path to live. People write code in notebooks or their own editor, keep it in version control, test it against safe data, and release it through automated pipelines that promote the same artefact through development, test and production. DataOps is the name for applying these software delivery habits to data, with the added problem that the data changes underneath the code.

Data work differs from application development in three ways that shape the capabilities. Tests must check data as well as logic, so data pipeline testing sits beside unit tests. Developers need realistic data without exposing personal records, which is the job of test data management, synthetic data and zero-copy cloning. And table structures outlive any one release, so schema change management and data modelling keep the physical design under control as it changes.

AI-assisted development and data engineering agents change who writes code and how fast, which makes review, testing and promotion controls more important, not less. Data application hosting extends the lifecycle to interactive apps built on the data. Platform operations provides and runs the environments this domain deploys into; this domain decides what goes into them and how.

# Key considerations

- Agree one path to live for every kind of code: SQL models, notebooks, pipelines, ML and infrastructure. Otherwise each team invents its own and audit evidence is scattered.
- Separate environments by more than name. Development must not be able to write to production tables, and production jobs should run as service identities, not as people.
- Decide early how developers get data: production copies, masked subsets, clones or synthetic data. This choice drives privacy risk, cost and how realistic tests are.
- Treat notebooks and visual tools as code. If they cannot be versioned, reviewed and promoted like other code, they become an unmanaged route to production.
- Measure delivery with lead time from commit to production, change failure rate and time to restore. These show whether controls help or only slow people down.

# Questions to ask

- How does a change reach production today, and how long does it take?
- Who may change production pipelines and data, and how is each change approved and recorded?
- What data do developers and testers use, and does it contain personal or regulated information?
- How often do releases break downstream reports, models or consumers?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [AI-assisted development](ai-assisted-development.md), [CI/CD](ci-cd.md), [Data application hosting](data-applications.md), [Data modelling and design](data-modelling.md), [Data pipeline testing](data-testing.md), [Environment promotion](environment-promotion.md), [Ephemeral development environments](ephemeral-environments.md), [IDE and local development](local-development.md), [Notebooks](notebooks.md), [Runtime and environment management](runtime-management.md), [Schema change management](schema-change-management.md), [Test data management](test-data-management.md), [Version control integration](version-control.md), [Zero-copy cloning](../storage/zero-copy-cloning.md) |
| Related | [Platform operations](../platform-operations/platform-operations.md), [CI/CD for machine learning](../mlops/ml-cicd.md), [Data contracts](../data-products/data-contracts.md), [Data observability](../data-quality/data-observability.md), [Transformation as code](../processing/transformation-as-code.md) |

# Where it appears

- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 142 technologies; see their pages.
