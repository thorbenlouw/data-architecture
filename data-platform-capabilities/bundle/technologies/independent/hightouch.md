---
type: Technology
id: hightouch
title: Hightouch
description: Warehouse-native activation platform that syncs modelled data to business tools and adds audience building, identity resolution and event collection on top of the warehouse.
platform: platform-independent
vendor: Hightouch
kind: saas
availability: ga
realises:
- reverse-etl
- entity-resolution
- audience-activation
- behavioural-event-collection
- decision-management
resource: https://hightouch.com/docs
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Syncs is the reverse ETL core. Customer Studio adds audiences, Journeys and a built-in agent. Hightouch Events collects behavioural data, and Match Booster improves ad match rates. AI Decisioning chooses message, channel and timing per customer using reinforcement learning.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation) (primary): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Audience building and activation](../../capabilities/serving/audience-activation.md) (Serving and activation): Build customer audiences from platform data and deliver them to marketing, advertising and service channels.
- [Behavioural event collection](../../capabilities/ingestion-integration/behavioural-event-collection.md) (Ingestion and integration): Collect clickstream and product events from web, mobile and server SDKs and validate them against a tracking plan.
- [Decision management](../../capabilities/serving/decision-management.md) (Serving and activation): Combine business rules, model scores and policies into automated decisions that are consistent, explainable and audited.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery EXPORT DATA](../google-cloud/gcp-bigquery-export-data.md), [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md) |
