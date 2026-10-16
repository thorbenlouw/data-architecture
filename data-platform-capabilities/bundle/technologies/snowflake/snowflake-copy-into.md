---
type: Technology
id: snowflake-copy-into
title: Snowflake bulk loading (COPY INTO <table>)
description: Loads staged files in bulk into tables on a warehouse, tracking which files were loaded so they are not loaded twice.
aliases: [COPY INTO <table>]
platform: platform-snowflake
kind: feature
availability: ga
realises: [batch-ingestion, file-ingestion]
resource: https://docs.snowflake.com/en/user-guide/data-load-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports CSV, JSON, Avro, ORC, Parquet and XML, with transformations during the load, schema detection and error handling (ON_ERROR, VALIDATION_MODE). Load metadata is kept for 64 days.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) (Ingestion and integration) (primary): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration): Detect and load files arriving in landing storage, processing each file exactly once.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift auto-copy](../aws/aws-redshift-auto-copy.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Copy job](../microsoft/fabric-copy-job.md), [Azure Data Factory](../microsoft/azure-data-factory.md), [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica File Ingestion and Replication](../informatica/informatica-file-ingestion-and-replication.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
