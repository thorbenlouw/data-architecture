---
type: Capability
id: data-consumer-portal
title: Data consumer portal
description: Give business users one place to find the dashboards, apps and AI agents shared with them, without engineering tools.
aliases: [business user portal]
broader: [analytics-bi]
related: [data-catalogue, data-marketplace, data-certification, access-requests, usage-metadata]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A data consumer portal is a single front door for business users. Instead of moving between a BI tool, a catalogue and an AI assistant, a sales manager opens one page listing the dashboards, data apps, reports and agents shared with them, organised by topic, with search, favourites, short descriptions and a mark showing which items are certified. Access requests and feedback can be raised from the same page.

It matters when content is spread across several tools and workspaces and people cannot find, or do not trust, what already exists. It differs from a data catalogue, which is built for people who work with datasets and shows tables, columns and lineage; the portal shows finished content and hides technical detail. It also differs from a data marketplace, which focuses on publishing and subscribing to data products. Portals may come with BI suites, as platform app hubs, or as intranet pages built on catalogue APIs.

# Key considerations

- A portal only helps if it covers the tools people actually use. Check which content types it can list from which tools.
- Curation matters more than completeness. Show certified items first and keep experiments and stale content out.
- Respect source permissions so users see only what they can open, and offer an access request when they cannot.
- Portal usage data shows what is valuable and what can be retired.

# Questions to ask

- How do business users find dashboards and reports today?
- How many tools publish content to business users?
- Do users need to request access or give feedback from the same place?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Access requests and reviews](../security/access-requests.md), [Data application hosting](../development-lifecycle/data-applications.md), [Data catalogue](../metadata/data-catalogue.md), [Data certification](../metadata/data-certification.md), [Data marketplace](../data-sharing/data-marketplace.md), [Data trust indicators](../metadata/data-trust-indicators.md), [Enterprise AI assistant](../generative-ai/enterprise-ai-assistant.md), [Usage and popularity metadata](../metadata/usage-metadata.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from)
- **Personas:** [Business user](../../personas/persona-business-user.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 11 – Distribution

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Quick](../../technologies/aws/aws-quick.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Power BI reports and dashboards](../../technologies/microsoft/powerbi-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Data Studio](../../technologies/google-cloud/gcp-data-studio.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Genie One](../../technologies/databricks/databricks-genie-one.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Workspaces | [Dataiku DSS](../../technologies/dataiku/dataiku.md) |
