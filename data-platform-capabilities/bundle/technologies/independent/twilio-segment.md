---
type: Technology
id: twilio-segment
title: Twilio Segment
description: Customer data platform that collects behavioural events through SDKs, validates them against tracking plans, unifies profiles and sends data to destinations, including from the warehouse.
aliases: [Segment]
platform: platform-independent
vendor: Twilio
kind: saas
availability: ga
realises: [behavioural-event-collection, data-contracts, entity-resolution, reverse-etl, audience-activation]
resource: https://www.twilio.com/docs/segment
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The products are Connections (collection and routing), Protocols (tracking-plan validation and transforms), Unify (identity and profiles), Engage (audiences) and Reverse ETL. Data Graph and Linked Audiences join profiles to warehouse entities on BigQuery, Databricks, Redshift or Snowflake (Business plans).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Behavioural event collection](../../capabilities/ingestion-integration/behavioural-event-collection.md) (Ingestion and integration) (primary): Collect clickstream and product events from web, mobile and server SDKs and validate them against a tracking plan.
- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
- [Audience building and activation](../../capabilities/serving/audience-activation.md) (Serving and activation): Build customer audiences from platform data and deliver them to marketing, advertising and service channels.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga
