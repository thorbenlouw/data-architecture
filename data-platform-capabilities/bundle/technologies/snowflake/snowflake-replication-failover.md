---
type: Technology
id: snowflake-replication-failover
title: Snowflake replication and failover groups
description: Replicate databases, users, roles, warehouses, policies and integrations to accounts in other regions or clouds, with promotion on failover and client redirect through connection objects.
platform: platform-snowflake
kind: feature
availability: ga
realises: [cross-region-failover, cross-region-sharing]
resource: https://docs.snowflake.com/en/user-guide/account-replication-intro
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Failover needs Business Critical Edition. Optimized Refresh and RPO Assurance became GA in September 2026. Some objects, such as MCP servers, budgets and archived COOL or COLD data, are not replicated.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations) (primary): Replicate data and configuration to another region and fail over when needed.
- [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md) (Data sharing and collaboration): Share data with consumers on other clouds or regions, replicating it where needed.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake disaster recovery](../microsoft/fabric-onelake-disaster-recovery.md), [Azure SQL Database](../microsoft/azure-sql.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed disaster recovery](../google-cloud/gcp-bigquery-managed-disaster-recovery.md), [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed disaster recovery](../databricks/databricks-managed-disaster-recovery.md) (preview) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md), [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
