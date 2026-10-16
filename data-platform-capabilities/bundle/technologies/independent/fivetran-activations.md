---
type: Technology
id: fivetran-activations
title: Fivetran Activations
description: Syncs modelled data from a warehouse or lake back into operational tools such as CRM, advertising and marketing platforms.
formerly: [Census]
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: saas
availability: ga
realises: [reverse-etl, audience-activation]
resource: https://fivetran.com/docs/activations/census-migration-faq
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This is the former Census product, now being folded into the Fivetran platform. Census month-to-month plans ended in March 2026. Census Store, CSV uploads and Mesh datasets were withdrawn on 1 August 2026. Activations is priced by MAR like the rest of Fivetran.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation) (primary): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
- [Audience building and activation](../../capabilities/serving/audience-activation.md) (Serving and activation): Build customer audiences from platform data and deliver them to marketing, advertising and service channels.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery EXPORT DATA](../google-cloud/gcp-bigquery-export-data.md), [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md) |
