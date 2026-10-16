---
type: Technology
id: palantir-foundry
title: Palantir Foundry
description: Integrated data platform that combines connectors, pipelines, storage, the Ontology, analytics, application building, model integration and governance in one environment with shared lineage and security.
platform: platform-palantir
kind: saas
availability: ga
realises: [multi-tenancy, decoupled-storage-compute, managed-storage, data-versioning]
resource: https://www.palantir.com/docs/foundry/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Usually Palantir-hosted on its Kubernetes-based infrastructure in AWS, Azure, Google Cloud or Oracle Cloud, and also deployable on premises or in accredited government regions through [Palantir Apollo](palantir-apollo.md). Datasets are stored as versioned Parquet files with a transaction history, so earlier versions can be read; Spark and lighter engines run transforms. It is a closed, opinionated platform, so plan exports and open-format access deliberately.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations) (primary): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Platform-managed storage](../../capabilities/storage/managed-storage.md) (Storage and table management): Let the platform manage table storage layout, compression and durability internally.
- [Data versioning](../../capabilities/storage/data-versioning.md) (Storage and table management): Keep and reference past versions of data so you can reproduce results, compare changes or roll back.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspaces](../microsoft/fabric-workspaces.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Resource Manager](../google-cloud/gcp-resource-manager.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake organisations](../snowflake/snowflake-organizations.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [SharedMergeTree](../clickhouse/clickhouse-sharedmergetree.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Kyuubi](../open-source/apache-kyuubi.md), [Apache Polaris](../open-source/apache-polaris.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
