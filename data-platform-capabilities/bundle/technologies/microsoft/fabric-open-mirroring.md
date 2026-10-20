---
type: Technology
id: fabric-open-mirroring
title: Fabric open mirroring
description: Lets any application or partner write change data into a landing zone in OneLake, which Fabric merges into mirrored Delta tables.
platform: platform-microsoft
kind: feature
availability: ga
realises: [custom-connectors, database-replication]
resource: https://learn.microsoft.com/en-us/fabric/mirroring/open-mirroring
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The extension point used by third-party replication vendors to target Fabric.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration) (primary): Build and run connectors for sources with no prebuilt option, using an SDK or framework.
- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration): Replicate operational databases continuously into the analytical platform without building pipelines.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Databases

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md), [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM StreamSets](../ibm/ibm-streamsets.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md), [dlt (data load tool)](../open-source/dlt.md), [Airbyte](../open-source/airbyte.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
