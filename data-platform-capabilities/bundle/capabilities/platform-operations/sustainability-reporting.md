---
type: Capability
id: sustainability-reporting
title: Sustainability and carbon management
description: Measure and reduce the carbon emissions and energy use of data workloads.
broader: [platform-operations]
related: [cost-optimisation, cost-attribution, gpu-compute, data-residency]
depends_on: [system-telemetry]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Emissions from data workloads are estimated rather than measured directly. The usual method takes usage records, such as compute hours by instance type, stored volume and data transferred, and multiplies them by energy and carbon factors for each provider region and period. Cloud providers publish emissions estimates for their customers, often weeks or months in arrears, and open methods such as the Green Software Foundation's Software Carbon Intensity specification standardise the calculation. Results are reported by team, workload or product alongside cost.

Organisations need these figures for reporting indirect (scope 3) emissions and for internal targets. Many reduction levers are the same as for cost: run less, run smaller and keep less. Others are specific to carbon: move flexible batch jobs to times or regions where electricity has lower carbon intensity, and choose more efficient hardware. Methods and provider data differ, so trends and comparisons are more reliable than absolute figures.

# Key considerations

- State the method and data source with every figure. Provider-reported, location-based and market-based numbers can differ widely.
- Reuse cost attribution tags and usage data so emissions are allocated the same way as spend.
- Moving jobs to lower-carbon regions can conflict with data residency, latency and transfer costs.
- Include hardware manufacturing emissions and the effect of model training and inference, which can dominate for AI workloads.

# Questions to ask

- Does the organisation report scope 3 emissions, and does it need figures for the data platform?
- Are there internal targets that require emissions per team or product?
- Which batch workloads could run at other times or in other regions without harm?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Related | [Cost attribution and chargeback](cost-attribution.md), [Cost management](cost-management.md), [Cost optimisation](cost-optimisation.md), [Data residency and sovereignty](../governance/data-residency.md), [GPU and accelerated compute](../compute/gpu-compute.md) |
| Depends on | [Usage and system telemetry](system-telemetry.md) |

# Where it appears

- **Use cases:** [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (benefits from)
- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [FinOps](../../maturity/track-finops.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Data Exports](../../technologies/aws/aws-data-exports.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure carbon optimization](../../technologies/microsoft/azure-carbon-optimization.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Carbon Footprint](../../technologies/google-cloud/gcp-carbon-footprint.md) |
