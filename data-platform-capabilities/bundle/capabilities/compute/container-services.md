---
type: Capability
id: container-services
title: Container services
description: Run custom containerised applications and services next to the data, inside the platform's security boundary.
broader: [compute-options]
related: [data-applications, agent-runtime, real-time-inference, network-security, application-sharing]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Container services run images you build, such as a web application, an API, a custom model server or a third-party tool, on compute that the data platform manages. The containers run inside the platform's network and identity boundary, so they can query tables and read files with a service's or the caller's permissions without data leaving the platform. Typical offerings support long-running services, scheduled jobs, GPUs, endpoints for users and autoscaling, on an orchestrator such as Kubernetes that the platform operates for you.

They cover what SQL and notebooks cannot: open-source tools with no managed version, custom inference servers, data applications and agents. The alternative is to run such services in a separate cloud environment and move data out to them, which adds copies, network paths and security reviews. In return you own the images, their vulnerabilities and their upgrades, as you would anywhere else.

# Key considerations

- Image security is your responsibility. Scan images, pin base images and keep a patching process.
- Decide which identity a container uses to reach data, and whether it acts as itself or on behalf of the calling user.
- Check network controls: whether containers can call external services, and how outbound traffic is restricted so data cannot leave.
- Containers are priced and scaled differently from query compute. Include idle running time in cost estimates.

# Questions to ask

- Which applications or tools must run close to the data, and why can they not run as SQL or notebooks?
- Must data stay inside the platform's security boundary for these workloads?
- Who will build, patch and support the container images?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Compute provisioning options](compute-options.md) |
| Related | [Agent hosting and runtime](../generative-ai/agent-runtime.md), [Data application distribution](../data-sharing/application-sharing.md), [Data application hosting](../development-lifecycle/data-applications.md), [Model deployment](../mlops/model-deployment.md), [Model training](../machine-learning/model-training.md), [Network security](../security/network-security.md), [Real-time inference](../mlops/real-time-inference.md), [Runtime and environment management](../development-lifecycle/runtime-management.md) |

# Where it appears

- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon EMR on EKS](../../technologies/aws/aws-emr-on-eks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Cloud Run](../../technologies/google-cloud/gcp-cloud-run.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Snowpark Container Services (SPCS), compute pools | [Snowpark Container Services](../../technologies/snowflake/snowflake-snowpark-container-services.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Apps](../../technologies/databricks/databricks-apps.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Services on premises](../../technologies/cloudera/cloudera-data-services-on-premises.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Elastic AI computation | [Dataiku DSS](../../technologies/dataiku/dataiku.md) |
