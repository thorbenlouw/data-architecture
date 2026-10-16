---
type: Technology
id: gcp-bigquery-managed-disaster-recovery
title: BigQuery managed disaster recovery
description: Cross-region dataset replication paired with failover reservations so compute and storage can be switched to a secondary region in a hard or soft failover.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [cross-region-failover]
resource: https://docs.cloud.google.com/bigquery/docs/managed-disaster-recovery
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Plus. Turbo replication targets a 15-minute RPO and 5-minute RTO. Scheduled queries do not move automatically after failover. Cross-region table copy also went GA in October 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations) (primary): Replicate data and configuration to another region and fail over when needed.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake disaster recovery](../microsoft/fabric-onelake-disaster-recovery.md), [Azure SQL Database](../microsoft/azure-sql.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake replication and failover groups](../snowflake/snowflake-replication-failover.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed disaster recovery](../databricks/databricks-managed-disaster-recovery.md) (preview) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md), [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
