---
type: Capability
id: privacy-enhancing-technologies
title: Privacy-enhancing technologies
description: Analyse data while limiting what is revealed, using techniques such as differential privacy, aggregation thresholds and secure computation.
aliases: [PETs]
broader: [privacy-management]
related: [data-clean-rooms, deidentification, synthetic-data, external-data-sharing]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Privacy-enhancing technologies (PETs) let people learn from data while limiting what results reveal about any individual or about another party's raw records. Aggregation thresholds refuse to return groups below a set size, so a count of customers by postcode never shows a group of three. Differential privacy adds calibrated random noise to results and tracks a privacy budget, which puts a mathematical limit on how much one person's data can change any answer. Secure multi-party computation, homomorphic encryption and trusted execution environments compute over data that stays split between parties, encrypted, or inside hardware-protected memory.

PETs matter when data must be analysed or shared but raw records cannot be exposed: joint analysis with partners, published statistics, or model training on sensitive data. Each trades accuracy, speed or flexibility for protection, and the right choice depends on whom the data is being protected from. They are building blocks of data clean rooms and some federated learning set-ups. They differ from de-identification, which changes stored data, because they control what computations reveal.

# Key considerations

- Differential privacy needs decisions on the privacy budget and how it is spent across queries and users. Too small a budget makes results useless; too large gives little protection.
- Aggregation thresholds alone can be defeated by differencing: comparing two queries whose groups differ by one person. Combine them with query restrictions or noise.
- Cryptographic techniques such as homomorphic encryption remain slow for general analytics. Test them on realistic workloads before committing.
- Be clear about the threat. An untrusted analyst, an untrusted partner and an untrusted infrastructure operator each call for different techniques.

# Questions to ask

- Who must not see the raw data: internal analysts, partners, the platform operator or the public?
- How much loss of accuracy can the use case accept?
- Are results published or shared outside the organisation?
- Does the work involve several organisations combining data they cannot share directly?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Privacy management](privacy-management.md) |
| Related | [Data sharing and collaboration](../data-sharing/data-sharing.md), [Data clean rooms](../data-sharing/data-clean-rooms.md), [De-identification](deidentification.md), [Entity resolution](../master-data/entity-resolution.md), [External data sharing](../data-sharing/external-data-sharing.md), [Synthetic data generation](../development-lifecycle/synthetic-data.md) |
| Needed by | [Data clean rooms](../data-sharing/data-clean-rooms.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (benefits from)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md) (from level 4, Measured)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 4a – Special categories of personal data for bias detection · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(c) – Data minimisation; Article 25 – Data protection by design and by default

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Clean Rooms](../../technologies/aws/aws-clean-rooms.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Confidential Clean Rooms](../../technologies/microsoft/azure-confidential-clean-rooms.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | analysis rules (aggregation threshold, differential privacy, list overlap) | [BigQuery data clean rooms](../../technologies/google-cloud/gcp-bigquery-data-clean-rooms.md), [Google Cloud Sensitive Data Protection](../../technologies/google-cloud/gcp-sensitive-data-protection.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | aggregation, projection, join and privacy (differential privacy) policies | [Snowflake aggregation policies](../../technologies/snowflake/snowflake-aggregation-policies.md), [Snowflake Data Clean Rooms](../../technologies/snowflake/snowflake-data-clean-rooms.md), [Snowflake differential privacy](../../technologies/snowflake/snowflake-differential-privacy.md), [Snowflake projection policies](../../technologies/snowflake/snowflake-projection-policies.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Clean Rooms](../../technologies/databricks/databricks-clean-rooms.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [MOSTLY AI Data Intelligence Platform](../../technologies/independent/mostly-ai-data-intelligence-platform.md) |
