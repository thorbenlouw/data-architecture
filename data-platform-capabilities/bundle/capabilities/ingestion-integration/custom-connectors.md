---
type: Capability
id: custom-connectors
title: Custom connector development
description: Build and run connectors for sources with no prebuilt option, using an SDK or framework.
broader: [ingestion-integration]
related: [api-ingestion, saas-connectors, ci-cd, data-testing]
depends_on: [secrets-management]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When no prebuilt connector exists, for example for an in-house system or a niche industry application, a team writes one with a connector SDK or framework. The framework supplies the common parts: scheduling, storage of cursors and other state, retries, schema declaration, logging and writing to the destination. The developer writes only the source-specific code, such as how to authenticate, list available streams and read a page of records. Some frameworks are declarative, so a simple REST source can be described in a configuration file rather than code.

Every estate has a long tail of sources no vendor will support, and ad hoc scripts for them end up unowned and unmonitored. Building on a framework means custom connectors run, log and fail like prebuilt ones and can be shared between teams. The open Singer and Airbyte protocols are examples of a common contract between sources and destinations. The ongoing cost is maintenance: the team owns every change to the source's API.

# Key considerations

- Treat connectors as software, with version control, tests against recorded responses and release through CI.
- Support incremental reads and saved state from the start. Retrofitting them onto a full-load design is costly.
- Name an owner for each connector. Source API changes break connectors without warning.
- Check that the framework's runtime meets security needs, such as running inside your network and reading credentials from a secrets store.

# Questions to ask

- How many sources have no prebuilt connector, and how much data do they hold?
- Who would build and maintain custom connectors, and with what skills?
- Could the source owner provide a stable API or regular export instead?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [API ingestion](api-ingestion.md), [CI/CD](../development-lifecycle/ci-cd.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [SaaS application connectors](saas-connectors.md) |
| Depends on | [Secrets management](../security/secrets-management.md) |

# Where it appears

- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon AppFlow](../../technologies/aws/aws-appflow.md), [Amazon Managed Streaming for Apache Kafka](../../technologies/aws/aws-msk.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric open mirroring](../../technologies/microsoft/fabric-open-mirroring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Cloud Data Fusion](../../technologies/google-cloud/gcp-data-fusion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../../technologies/snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../../technologies/snowflake/snowflake-openflow.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Connect](../../technologies/databricks/databricks-lakeflow-connect.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM StreamSets](../../technologies/ibm/ibm-streamsets.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku connections](../../technologies/dataiku/dataiku-connections.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Airbyte](../../technologies/open-source/airbyte.md), [dlt (data load tool)](../../technologies/open-source/dlt.md), [Kafka Connect](../../technologies/open-source/apache-kafka-connect.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Airbyte Cloud](../../technologies/independent/airbyte-cloud.md), [Fivetran](../../technologies/independent/fivetran.md) |
