---
type: Capability
id: interruptible-compute
title: Spot and interruptible compute
description: Run fault-tolerant jobs on spare capacity at a large discount, accepting that the provider can reclaim it at short notice.
aliases: [spot instances, spot VMs, preemptible VMs, low-priority VMs]
broader: [compute-options, cost-management]
related: [reserved-capacity, distributed-processing, model-training, backfill-replay, cost-optimisation]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cloud providers sell unused capacity at a deep discount, often 60 to 90 per cent below on-demand prices, on condition that they can take it back with a short warning of between thirty seconds and two minutes. Data and ML services expose this as spot worker nodes in Spark clusters, managed spot training jobs that checkpoint and resume, or low-priority node pools. A typical design keeps the driver and a few core nodes on on-demand capacity and runs most workers on spot, so a reclaimed node costs some recomputed tasks rather than the whole job.

It suits work that can be retried or resumed: batch transformation, backfills, model training with checkpoints and test runs. It suits poorly anything with a deadline that cannot slip, long tasks that cannot checkpoint, and interactive or streaming services. Savings depend on how often capacity is reclaimed, which varies by instance type, region and time of day. Reserved capacity lowers cost by committing in advance; interruptible capacity lowers it by giving up guaranteed availability.

# Key considerations

- Keep coordinating processes, such as the Spark driver and any shuffle storage on local disks, on on-demand capacity. Losing them loses the whole job.
- Allow several instance types and zones, and fall back to on-demand automatically when spot capacity runs out, or jobs wait indefinitely.
- Measure the cost of reruns and delays caused by reclaimed nodes against the discount, per workload.
- Training jobs need regular checkpoints to durable storage, or a reclaim near the end repeats hours of work.

# Questions to ask

- Which batch and training workloads can tolerate restarts or a later finish?
- What share of cluster compute spend runs on on-demand capacity today?
- Do the managed services you use support spot capacity with automatic fallback to on-demand?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Compute provisioning options](compute-options.md), [Cost management](../platform-operations/cost-management.md) |
| Related | [Backfill and reprocessing](../orchestration/backfill-replay.md), [Cost optimisation](../platform-operations/cost-optimisation.md), [Distributed processing](../processing/distributed-processing.md), [Model training](../machine-learning/model-training.md), [Reserved and committed capacity](reserved-capacity.md) |

# Where it appears

- **Use cases:** [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (benefits from)
- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 5, Optimising) · [FinOps](../../maturity/track-finops.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon EMR on EC2](../../technologies/aws/aws-emr-on-ec2.md), [Amazon SageMaker AI training jobs](../../technologies/aws/aws-sagemaker-training.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning](../../technologies/microsoft/azure-machine-learning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Managed Training](../../technologies/google-cloud/gcp-agent-platform-managed-training.md), [Google Cloud Dataflow](../../technologies/google-cloud/gcp-dataflow.md), [Google Cloud Managed Service for Apache Spark on clusters](../../technologies/google-cloud/gcp-managed-spark-clusters.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks classic compute (Databricks Runtime clusters)](../../technologies/databricks/databricks-classic-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Engineering](../../technologies/cloudera/cloudera-data-engineering.md) |
