---
type: Capability
id: reverse-etl
title: Reverse ETL
description: Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
aliases: [data activation, operational analytics]
broader: [serving]
related: [saas-connectors, change-feeds, consent-management, application-integration, data-contracts]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Reverse ETL writes tables modelled on the platform, such as customer lifetime value, product usage scores or churn risk, into the business tools where staff and automated processes act on them. A sync might run every 15 minutes, work out which account rows have changed since the last run, map columns to CRM fields and call the CRM's API to update only those records, respecting rate limits and logging rejected rows. Sales staff then see a usage score on each account without opening a dashboard.

It connects analysis to action, using the platform's integrated, modelled data as the source instead of rebuilding the same logic in each tool. Application integration differs by moving individual transactions between operational systems; data export differs by delivering bulk files without mapping them to a destination's objects. Once a table feeds reverse ETL, the platform is effectively a source system for business tools, so that table needs the reliability and ownership of any production feed.

# Key considerations

- Sync only changed records. Full syncs use up destination API quotas and can overwrite edits made in the tool.
- Decide which system owns each field. Writing to fields that users also edit causes their changes to be quietly reverted.
- Monitor rejected records and failed syncs, and make sure the owners of source tables know they now feed operational processes.
- Check that personal data pushed to tools respects consent and purpose limits.

# Questions to ask

- Which teams need platform data inside their tools, and which decisions will they make with it?
- How fresh must synced values be?
- Who owns each destination field, and can users edit it in the tool?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Narrower | [Audience building and activation](audience-activation.md) |
| Related | [Alerts and subscriptions](../analytics-bi/data-alerting.md), [Application integration](../ingestion-integration/application-integration.md), [Batch inference](../mlops/batch-inference.md), [Change feeds](change-feeds.md), [Consent and purpose management](../governance/consent-management.md), [Data contracts](../data-products/data-contracts.md), [End-to-end lineage](../metadata/cross-system-lineage.md), [Master data management](../master-data/master-data-management.md), [SaaS application connectors](../ingestion-integration/saas-connectors.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 2) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 3)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon AppFlow](../../technologies/aws/aws-appflow.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery continuous queries](../../technologies/google-cloud/gcp-bigquery-continuous-queries.md), [BigQuery EXPORT DATA](../../technologies/google-cloud/gcp-bigquery-export-data.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Data 360 Connector and Scanner](../../technologies/informatica/informatica-data-360-connector-and-scanner.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Boomi Data Integration](../../technologies/independent/boomi-data-integration.md), [Fivetran Activations](../../technologies/independent/fivetran-activations.md), [Hightouch](../../technologies/independent/hightouch.md), [mParticle](../../technologies/independent/mparticle.md), [Twilio Segment](../../technologies/independent/twilio-segment.md) |

Narrower capabilities are realised by a further 4 technologies; see their pages.
