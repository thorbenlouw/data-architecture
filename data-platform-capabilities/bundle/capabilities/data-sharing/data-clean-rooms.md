---
type: Capability
id: data-clean-rooms
title: Data clean rooms
description: Let organisations combine and analyse data jointly while each keeps control over what the others can see.
aliases: [DCR, clean room, data collaboration, privacy-safe collaboration]
broader: [data-sharing]
related: [deidentification, consent-management, entity-resolution, audience-activation, data-usage-rights]
depends_on: [privacy-enhancing-technologies]
tags: [data-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An advertiser and a publisher want to know how many of the publisher's readers bought the advertiser's product, without handing each other customer lists. In a clean room, each contributes records keyed by a hashed email address. They can count the overlap and measure conversions, but the room only returns aggregates above a minimum group size, so no individual can be singled out. Each party sets rules on which columns may be joined, which queries or templates may run and what output may leave.

Clean rooms are used in advertising measurement, retail media, financial crime collaboration and health research, where combined data is valuable but direct sharing would breach privacy law or commercial confidence. Controls range from approved query templates and aggregation thresholds to differential privacy and confidential computing hardware. A clean room packages privacy-enhancing techniques with a collaboration workflow. It differs from ordinary sharing, where the consumer can read every shared row.

# Key considerations

- Aggregation thresholds alone can be defeated by repeated, overlapping queries. Check for limits on query patterns, privacy budgets or added noise.
- Agree matching keys and how they are prepared, such as normalising and hashing emails, before onboarding. Poor match rates make results useless.
- Clean rooms are simplest when all parties use the same platform. Cross-platform options exist but add latency and set-up work.
- Personal data still crosses organisational boundaries, so a legal basis and an agreement are needed even when outputs are aggregated.

# Questions to ask

- Which partners want to combine data with you, and to answer which questions?
- What must each party be prevented from learning?
- Are partners on the same platform, and can they agree common matching keys?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data sharing and collaboration](data-sharing.md) |
| Broader | [Data sharing and collaboration](data-sharing.md) |
| Related | [Audience building and activation](../serving/audience-activation.md), [Consent and purpose management](../governance/consent-management.md), [Data application distribution](application-sharing.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [De-identification](../governance/deidentification.md), [Entity resolution](../master-data/entity-resolution.md), [Privacy-enhancing technologies](../governance/privacy-enhancing-technologies.md) |
| Depends on | [Privacy-enhancing technologies](../governance/privacy-enhancing-technologies.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (benefits from)
- **Maturity tracks:** [Data sharing](../../maturity/track-data-sharing.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS Clean Rooms collaborations | [AWS Clean Rooms](../../technologies/aws/aws-clean-rooms.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Confidential Clean Rooms](../../technologies/microsoft/azure-confidential-clean-rooms.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery data clean rooms | [BigQuery data clean rooms](../../technologies/google-cloud/gcp-bigquery-data-clean-rooms.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Data Clean Rooms](../../technologies/snowflake/snowflake-data-clean-rooms.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Clean Rooms](../../technologies/databricks/databricks-clean-rooms.md) |
