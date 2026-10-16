---
type: Technology
id: gcp-carbon-footprint
title: Google Cloud Carbon Footprint
description: Console dashboard and export that estimate location- and market-based greenhouse gas emissions from Google Cloud usage by project, region and product.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [sustainability-reporting]
resource: https://docs.cloud.google.com/carbon-footprint/docs
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Covers Scopes 1, 2 and 3 for Google Cloud services; monthly data can take up to 21 days to arrive and can be exported to BigQuery for reporting.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Sustainability and carbon management](../../capabilities/platform-operations/sustainability-reporting.md) (Platform operations) (primary): Measure and reduce the carbon emissions and energy use of data workloads.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exports](../aws/aws-data-exports.md) | [Sustainability and carbon management](../../capabilities/platform-operations/sustainability-reporting.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure carbon optimization](../microsoft/azure-carbon-optimization.md) | [Sustainability and carbon management](../../capabilities/platform-operations/sustainability-reporting.md) |
