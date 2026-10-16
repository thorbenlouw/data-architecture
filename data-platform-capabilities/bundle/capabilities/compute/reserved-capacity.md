---
type: Capability
id: reserved-capacity
title: Reserved and committed capacity
description: Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.
aliases: [commitments, slots, provisioned throughput, savings plans]
broader: [compute-options, cost-management]
related: [cost-optimisation, spend-controls, gpu-compute, ai-spend-controls, cost-attribution]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Providers offer lower unit prices, guaranteed availability, or both, in return for an advance commitment. Forms include reserved instances or slots for a fixed term, prepaid credits drawn down over a year, committed-spend agreements across services, and provisioned throughput for model inference, where a set number of tokens per minute is held for you. A team that knows it will run a warehouse all day, or a block of GPUs for a planned training run, can pay well below on-demand rates or be sure the capacity exists when needed.

It suits steady base load, critical work that cannot risk a capacity shortage, and finance teams that prefer fixed costs. It is a financial instrument as much as a technical one. Commit too much and you pay for capacity nobody uses; commit too little and peak use is billed at on-demand rates. The usual approach is to reserve the stable base and leave peaks to on-demand or serverless capacity.

# Key considerations

- Base commitments on several months of measured use, not on project plans, which tend to be optimistic.
- Check flexibility: whether reservations can move between regions, instance families, services or teams, and what happens to unused credit.
- Reservations do not cap use. Spend controls are still needed to stop on-demand overruns.
- Line commitments up with planned architecture changes. A migration or new engine can leave a reservation unused.

# Questions to ask

- What is the stable minimum level of use across the year?
- Do any workloads need guaranteed capacity, such as GPU training or high-volume inference?
- Who makes commitment decisions, and how are they reviewed?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Compute provisioning options](compute-options.md), [Cost management](../platform-operations/cost-management.md) |
| Related | [AI usage and spend controls](../platform-operations/ai-spend-controls.md), [Budgets and spend controls](../platform-operations/spend-controls.md), [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Cost optimisation](../platform-operations/cost-optimisation.md), [Distributed training](../machine-learning/distributed-training.md), [Foundation model access](../generative-ai/foundation-model-access.md), [Generative model serving](../mlops/generative-model-serving.md), [GPU and accelerated compute](gpu-compute.md), [Model training](../machine-learning/model-training.md), [Provisioned compute](provisioned-compute.md), [Spend forecasting and anomaly detection](../platform-operations/cost-forecasting.md), [Spot and interruptible compute](interruptible-compute.md) |

# Where it appears

- **Use cases:** [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 2)
- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 4, Measured) · [FinOps](../../maturity/track-finops.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Athena](../../technologies/aws/aws-athena.md), [Amazon Bedrock](../../technologies/aws/aws-bedrock.md), [Amazon Kinesis Data Streams](../../technologies/aws/aws-kinesis-data-streams.md), [Amazon Redshift](../../technologies/aws/aws-redshift.md), [Amazon SageMaker AI training jobs](../../technologies/aws/aws-sagemaker-training.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure OpenAI in Foundry Models](../../technologies/microsoft/azure-openai.md), [Microsoft Fabric capacities (F SKUs)](../../technologies/microsoft/fabric-capacities.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Managed Training](../../technologies/google-cloud/gcp-agent-platform-managed-training.md), [BigQuery editions](../../technologies/google-cloud/gcp-bigquery-editions.md), [Gemini models on Agent Platform](../../technologies/google-cloud/gcp-gemini-models.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Foundation Model APIs](../../technologies/databricks/databricks-foundation-model-apis.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Processing Unit (IPU) consumption pricing](../../technologies/informatica/informatica-ipu-pricing.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Generative AI (OCI Enterprise AI)](../../technologies/oracle/oracle-oci-generative-ai.md) |
