---
type: Technology
id: snowflake-snowpark-container-services
title: Snowpark Container Services
description: Runs OCI container images as long-running services or finite jobs on Snowflake-managed compute pools, including GPU nodes, inside the account's security boundary.
aliases: [SPCS]
platform: platform-snowflake
kind: managed-service
availability: ga
realises: [container-services, gpu-compute, data-applications, object-file-access]
resource: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Snowpark Container Services underpins model serving, ML Jobs, Notebooks in Workspaces, Openflow Snowflake deployments and container-based Native Apps. Compute pools are billed while running, whatever the load.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Container services](../../capabilities/compute/container-services.md) (Query and compute) (primary): Run custom containerised applications and services next to the data, inside the platform's security boundary.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps): Build and host interactive data applications next to the data, under platform security.
- [File-system access to object storage](../../capabilities/storage/object-file-access.md) (Storage and table management): Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowpark

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EKS](../aws/aws-emr-on-eks.md) | [Container services](../../capabilities/compute/container-services.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Run](../google-cloud/gcp-cloud-run.md) | [Container services](../../capabilities/compute/container-services.md), [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Apps](../databricks/databricks-apps.md) | [Container services](../../capabilities/compute/container-services.md), [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Services on premises](../cloudera/cloudera-data-services-on-premises.md) | [Container services](../../capabilities/compute/container-services.md) |
