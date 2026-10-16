---
type: Capability
id: behavioural-event-collection
title: Behavioural event collection
description: Collect clickstream and product events from web, mobile and server SDKs and validate them against a tracking plan.
aliases: [clickstream, event tracking]
broader: [streaming-ingestion]
related: [data-contracts, consent-management, schema-registry, audience-activation, entity-resolution]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Small tracking libraries in web pages, mobile apps and back-end services record what users do, such as page views, searches and items added to a basket, and send each as an event with a user or device identifier, a timestamp and context such as device type and page. A collector receives the events and checks each against a tracking plan, which lists the allowed event names and their properties and types. It enriches valid events and forwards them to the platform, and routes invalid ones aside for inspection.

Product analytics, experimentation, personalisation and attribution all depend on this data, and it breaks easily: renamed events, missing properties and double tracking distort funnels without anyone noticing. A tracking plan acts as a data contract between product teams and analysts. Client-side collection sees user interaction but is affected by ad blockers and browser privacy limits; server-side collection is more reliable but sees less. Where privacy law requires it, consent is checked before tracking.

# Key considerations

- Version the tracking plan and validate events against it during development and in the collector, not only during analysis.
- Apply consent at collection time. Events gathered without valid consent may have to be found and deleted later at greater cost.
- Expect duplicate and out-of-order events from mobile clients that retry. Include an event id for deduplication.
- Linking one person's activity across devices and logins is a separate problem. Decide where it happens and which identifiers are collected.

# Questions to ask

- Which products and platforms need tracking, and who owns the tracking plan?
- What consent and privacy rules apply in the markets served?
- Which decisions depend on this data: reporting, experiments or real-time personalisation?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Streaming ingestion](streaming-ingestion.md) |
| Related | [Approximate query processing](../compute/approximate-query-processing.md), [Audience building and activation](../serving/audience-activation.md), [Consent and purpose management](../governance/consent-management.md), [Data contracts](../data-products/data-contracts.md), [Entity resolution](../master-data/entity-resolution.md), [Event-time windowing](../processing/event-time-windowing.md), [Experimentation and causal measurement](../analytics-bi/experimentation.md), [Schema registry](../metadata/schema-registry.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from) · [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (benefits from) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 3)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [Hightouch](../../technologies/independent/hightouch.md), [mParticle](../../technologies/independent/mparticle.md), [Twilio Segment](../../technologies/independent/twilio-segment.md) |
