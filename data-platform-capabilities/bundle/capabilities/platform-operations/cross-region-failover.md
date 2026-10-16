---
type: Capability
id: cross-region-failover
title: Cross-region replication and failover
description: Replicate data and configuration to another region and fail over when needed.
broader: [business-continuity]
related: [cross-region-sharing, data-residency, infrastructure-as-code, deployment-options, backup-restore]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Storage replication copies table files and metadata from the primary region to a secondary one, continuously or on a schedule, and platform-level replication can also copy accounts, users, grants and pipeline definitions. When the primary becomes unavailable, operators or automation promote the secondary and redirect users, pipelines and applications to it, often by switching a connection endpoint or DNS name, and later fail back. Designs range from replicating only storage and building compute when needed, through a configured warm standby, to running active in both regions.

Regional outages are rare but can last hours, and some sectors must show they can keep critical services running through one. The cost is real: duplicate storage, transfer charges, standby compute and the work of keeping two environments identical. Replication is usually asynchronous, so changes not yet copied are lost on failover; that gap is the effective RPO. Cross-region sharing makes data available to consumers elsewhere; failover recovers your own service.

# Key considerations

- Replicate configuration, permissions and pipelines as well as data, preferably by deploying them from code to both regions.
- Decide who declares a disaster and who triggers failover. Automatic failover on brief faults can do more harm than the outage.
- Monitor replication lag continuously, since it is the data you would lose in a failover.
- Check data residency rules before choosing a secondary region. Some data may not leave its jurisdiction.
- Plan failback. Returning to the primary and reconciling changes made in the secondary is often harder than failing over.

# Questions to ask

- Which workloads must survive the loss of a whole region, and how long can they be unavailable?
- Are there jurisdictional limits on where replicas may be stored?
- What do standby capacity and cross-region transfer cost, and is that justified for each workload?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Backup and disaster recovery](business-continuity.md) |
| Related | [Backup and restore](backup-restore.md), [Cross-region and cross-cloud sharing](../data-sharing/cross-region-sharing.md), [Data residency and sovereignty](../governance/data-residency.md), [Hybrid and multi-cloud deployment](deployment-options.md), [Infrastructure as code](infrastructure-as-code.md), [Platform incident management](platform-incident-management.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from)
- **Maturity tracks:** [Resilience and recovery](../../maturity/track-resilience.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Storage and Operations · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Articles 11 and 12 – Response and recovery; backup, restoration and recovery; Chapter IV – Digital operational resilience testing (Articles 24 to 27)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Aurora](../../technologies/aws/aws-aurora.md), [Amazon DynamoDB](../../technologies/aws/aws-dynamodb.md), [Amazon Managed Streaming for Apache Kafka](../../technologies/aws/aws-msk.md), [Amazon S3](../../technologies/aws/aws-s3.md), [AWS Backup](../../technologies/aws/aws-backup.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Cosmos DB](../../technologies/microsoft/azure-cosmos-db.md), [Azure SQL Database](../../technologies/microsoft/azure-sql.md), [OneLake disaster recovery](../../technologies/microsoft/fabric-onelake-disaster-recovery.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery managed disaster recovery | [BigQuery managed disaster recovery](../../technologies/google-cloud/gcp-bigquery-managed-disaster-recovery.md), [Google Cloud Storage](../../technologies/google-cloud/gcp-cloud-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | replication and failover groups | [Snowflake replication and failover groups](../../technologies/snowflake/snowflake-replication-failover.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks managed disaster recovery](../../technologies/databricks/databricks-managed-disaster-recovery.md) (preview) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Replication Manager](../../technologies/cloudera/cloudera-replication-manager.md), [Cloudera Streams Messaging](../../technologies/cloudera/cloudera-streams-messaging.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Database](../../technologies/oracle/oracle-autonomous-ai-database.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Backup, Archive and Restore and Data Mover](../../technologies/teradata/teradata-bar-data-mover.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud](../../technologies/ibm/confluent-cloud.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Pulsar](../../technologies/open-source/apache-pulsar.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Redis Cloud](../../technologies/independent/redis-cloud.md) |
