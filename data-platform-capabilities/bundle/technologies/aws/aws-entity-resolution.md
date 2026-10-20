---
type: Technology
id: aws-entity-resolution
title: AWS Entity Resolution
description: Matches and links records that describe the same person or business using rules, machine learning or licensed provider data, and maintains match IDs.
platform: platform-aws
kind: managed-service
availability: ga
realises: [entity-resolution]
resource: https://docs.aws.amazon.com/entityresolution/latest/userguide/what-is-service.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports batch, incremental and near real-time lookups and ID mapping between namespaces. It does not build golden records or manage survivorship, so it is not a full MDM product.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data) (primary): Find and link records that refer to the same real-world entity, even when they do not match exactly.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Customer 360 SaaS](../informatica/informatica-customer-360.md), [Informatica Multidomain MDM SaaS](../informatica/informatica-multidomain-mdm-saas.md), [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Accelerator](../sas/sas-data-accelerator.md), [SAS Data Engineering](../sas/sas-data-engineering.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [mParticle](../independent/mparticle.md), [Ataccama ONE Master Data Management](../independent/ataccama-one-mdm.md), [Hightouch](../independent/hightouch.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
