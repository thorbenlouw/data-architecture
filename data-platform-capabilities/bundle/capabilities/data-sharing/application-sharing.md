---
type: Capability
id: application-sharing
title: Data application distribution
description: Package code, models, interfaces and data as installable applications that run in the consumer's environment.
aliases: [native apps]
broader: [data-sharing]
related: [data-applications, container-services, data-marketplace, data-clean-rooms, model-deployment]
tags: [data-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A vendor distributes a fraud-scoring application through the platform. The consumer installs it in its own account and grants it access to its transaction tables; the model runs inside the consumer's environment, so the consumer's data never leaves and the provider's code and model stay hidden. The provider pushes updates as new versions, and the package can also carry reference data, a user interface and stored procedures.

It matters when the value lies in logic as much as data, and sending data to the provider is ruled out for privacy, cost or regulatory reasons. It reverses ordinary sharing: instead of bringing data to the consumer, it brings processing to the consumer's data. Both sides need to settle which permissions the application requests, how its compute is paid for, how the provider's intellectual property is protected and how upgrades are controlled.

# Key considerations

- Review the permissions an installed application asks for, as you would for any third-party software, and grant the minimum.
- Check where compute runs and who pays, especially for applications with continuous processing or GPU needs.
- Providers need telemetry to support the application. Agree which logs and usage data flow back to them.
- Plan upgrades and rollback, since provider updates can change results in your environment.

# Questions to ask

- Does a provider's logic need to run on data you cannot send them?
- Who reviews and approves third-party applications installed on the platform?
- Do you distribute models or logic to customers who would rather keep their data?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data sharing and collaboration](data-sharing.md) |
| Broader | [Data sharing and collaboration](data-sharing.md) |
| Related | [Container services](../compute/container-services.md), [Data application hosting](../development-lifecycle/data-applications.md), [Data clean rooms](data-clean-rooms.md), [Data marketplace](data-marketplace.md), [Model deployment](../mlops/model-deployment.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (benefits from)
- **Maturity tracks:** [Data sharing](../../maturity/track-data-sharing.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Native App Framework](../../technologies/snowflake/snowflake-native-app-framework.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Marketplace](../../technologies/databricks/databricks-marketplace.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir DevOps and Marketplace](../../technologies/palantir/palantir-devops-marketplace.md) |
