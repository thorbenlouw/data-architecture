---
type: Technology
id: purview-data-loss-prevention
title: Microsoft Purview Data Loss Prevention
description: Detects sensitive information in Microsoft 365, endpoints and Fabric items and raises policy tips, alerts or access restrictions.
platform: platform-microsoft
kind: saas
availability: ga
realises: [data-loss-prevention]
resource: https://learn.microsoft.com/en-us/fabric/governance/data-loss-prevention-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

For Fabric it covers semantic models, lakehouses, warehouses, KQL, SQL, mirrored and Cosmos databases; the restrict-access action for Fabric is preview. Advanced classifiers are not supported for Fabric.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data loss prevention](../../capabilities/security/data-loss-prevention.md) (Security and access) (primary): Detect and block sensitive data leaving approved boundaries.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Guardrails](../aws/aws-bedrock-guardrails.md) | [Data loss prevention](../../capabilities/security/data-loss-prevention.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Armor](../google-cloud/gcp-model-armor.md), [VPC Service Controls](../google-cloud/gcp-vpc-service-controls.md) | [Data loss prevention](../../capabilities/security/data-loss-prevention.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks serverless egress control](../databricks/databricks-serverless-egress-control.md) | [Data loss prevention](../../capabilities/security/data-loss-prevention.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Cyera DSPM](../independent/cyera-dspm.md) | [Data loss prevention](../../capabilities/security/data-loss-prevention.md) |
