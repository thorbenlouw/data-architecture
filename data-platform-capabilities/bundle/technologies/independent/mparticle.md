---
type: Technology
id: mparticle
title: mParticle
description: Customer data platform for real-time event collection, identity resolution, audience segmentation and predictions, with a hybrid architecture that can use the customer's warehouse.
aliases: [mParticle by Rokt]
platform: platform-independent
vendor: Rokt
kind: saas
availability: ga
realises: [behavioural-event-collection, entity-resolution, reverse-etl, audience-activation]
resource: https://www.mparticle.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

mParticle has merged with Rokt and is now sold as mParticle by Rokt. The hybrid architecture lets profiles and audiences be built from data in the customer's warehouse as well as from events collected by mParticle's SDKs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Behavioural event collection](../../capabilities/ingestion-integration/behavioural-event-collection.md) (Ingestion and integration) (primary): Collect clickstream and product events from web, mobile and server SDKs and validate them against a tracking plan.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
- [Audience building and activation](../../capabilities/serving/audience-activation.md) (Serving and activation): Build customer audiences from platform data and deliver them to marketing, advertising and service channels.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga
