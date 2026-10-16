---
type: Pattern
id: shift-left
title: Shift-left data quality and governance
description: Move quality checks, contracts and governance controls upstream to where data is produced.
aliases: [shift left, quality at source]
uses:
- data-contracts
- schema-registry
- schema-change-management
- data-quality-rules
- data-testing
- ci-cd
- data-classification
- data-ownership
- active-metadata
related: [data-mesh, write-audit-publish, transactional-outbox]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In many organisations quality and governance work happens far downstream: engineers clean data after it lands, stewards classify tables after they are in use, and problems surface in dashboards. Shifting left moves these controls to the producer. Application teams publish data against a contract that defines schema, meaning and quality expectations; schema compatibility checks and data tests run in the producer's CI pipeline; classification and ownership are set when a dataset is created rather than afterwards. The term is borrowed from software testing, where shift-left means testing earlier in the development cycle.

Fixing a problem at the source costs less than fixing it in every consumer, and it removes the defensive cleansing that each downstream team repeats. It requires producers to take responsibility for data they previously treated as a by-product, which is an organisational change as much as a technical one. It complements downstream observability rather than replacing it, because some problems only appear in real production data. It is closely tied to data contracts and to the data mesh idea of data as a product.

# When to use

- The same quality problems are fixed repeatedly downstream, often by several consumers.
- Breaking schema changes in source applications regularly cause pipeline failures.
- Producers and consumers can agree contracts, and producer teams have CI pipelines where checks can run.

# Watch out for

- Producers resist extra work unless contracts and checks are cheap to adopt and the benefits are visible to them.
- Contracts that exist only as documents, without enforcement in CI or at run time, do not change behaviour.
- Downstream monitoring is still needed for problems that only show up in production data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Data contracts](../capabilities/data-products/data-contracts.md): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Schema registry](../capabilities/metadata/schema-registry.md): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
- [Schema change management](../capabilities/development-lifecycle/schema-change-management.md): Version and apply database schema changes through controlled migrations.
- [Data quality rules](../capabilities/data-quality/data-quality-rules.md): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md): Test transformation logic and data with unit, integration and regression tests before release.
- [CI/CD](../capabilities/development-lifecycle/ci-cd.md): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Data classification](../capabilities/governance/data-classification.md): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Ownership and stewardship](../capabilities/governance/data-ownership.md): Assign accountable owners and stewards to data and record their responsibilities.
- [Active metadata](../capabilities/metadata/active-metadata.md): Use metadata to trigger actions automatically, such as propagating tags, alerting owners or blocking bad data.

# Related patterns

- [Data mesh](data-mesh.md)
- [Write-audit-publish](write-audit-publish.md)
- [Transactional outbox](transactional-outbox.md)

# Where it appears

- **Use cases:** [Application data publishing](../use-cases/usecase-application-data-publishing.md) · [Privacy rights handling](../use-cases/usecase-privacy-rights.md) · [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md) · [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md)
- **Personas:** [Chief data officer](../personas/persona-cdo.md) · [Data engineer](../personas/persona-data-engineer.md) · [Data product owner](../personas/persona-data-product-owner.md) · [Data steward](../personas/persona-data-steward.md) · [Risk and compliance officer](../personas/persona-risk-compliance.md) · [Security and privacy officer](../personas/persona-security-officer.md) · [Software engineer](../personas/persona-software-engineer.md)
