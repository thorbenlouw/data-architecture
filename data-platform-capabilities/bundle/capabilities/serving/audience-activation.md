---
type: Capability
id: audience-activation
title: Audience building and activation
description: Build customer audiences from platform data and deliver them to marketing, advertising and service channels.
aliases: [CDP, composable CDP]
broader: [reverse-etl]
related: [behavioural-event-collection, data-clean-rooms, master-data-management, deidentification]
depends_on: [entity-resolution, consent-management]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Marketers define groups of customers from platform data, such as "bought twice in the last 90 days, opened an email this month and not flagged as likely to churn", and send them to channels like email platforms, advertising networks, mobile push and contact centres. A visual builder turns the conditions into SQL against modelled customer tables, estimates the audience size and syncs membership changes to each destination on a schedule. People are matched by email address, phone number or device identifier, often hashed first.

This is the composable alternative to copying all customer data into a separate customer data platform: audience logic runs where the data already is, and only membership is sent out. It needs a modelled customer table with resolved identities and consent flags. Compared with general reverse ETL it adds a builder marketers can use, audience sizing and overlap analysis, identity matching specific to each destination, and often holdout groups to measure effect.

# Key considerations

- Check consent and purpose for each channel before every sync. Advertising destinations usually need explicit consent.
- Hashing identifiers is not anonymisation. Treat audience uploads as transfers of personal data, with contracts and records to match.
- Match rates in advertising networks vary widely. Measure them, because a low match rate wastes the effort of building an audience.
- Version audience definitions so results can be traced to the exact rules used.

# Questions to ask

- Which channels need audiences, and how does each identify people?
- Is there a modelled customer table with resolved identities and consent?
- Who builds audiences today, and how long does a new one take?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Reverse ETL](reverse-etl.md) |
| Related | [Behavioural event collection](../ingestion-integration/behavioural-event-collection.md), [Consent and purpose management](../governance/consent-management.md), [Data clean rooms](../data-sharing/data-clean-rooms.md), [De-identification](../governance/deidentification.md), [Experimentation and causal measurement](../analytics-bi/experimentation.md), [Master data management](../master-data/master-data-management.md) |
| Depends on | [Entity resolution](../master-data/entity-resolution.md), [Consent and purpose management](../governance/consent-management.md) |

# Where it appears

- **Use cases:** [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 3)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fivetran Activations](../../technologies/independent/fivetran-activations.md), [Hightouch](../../technologies/independent/hightouch.md), [mParticle](../../technologies/independent/mparticle.md), [Twilio Segment](../../technologies/independent/twilio-segment.md) |
