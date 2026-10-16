---
type: Capability
id: compute-user-isolation
title: Shared compute isolation
description: Sandbox each user's code on shared compute so nobody can bypass access controls or affect other users.
broader: [security, compute]
related: [workload-isolation, row-level-security, column-masking, user-defined-functions, credential-vending]
depends_on: [access-control]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

On shared clusters, several users run their own Python, Scala or SQL functions in the same engine. Without isolation, one user's code could read another user's data from memory or disk, use the cluster's storage credentials directly, or skip row filters and masks by reading the underlying files. Shared compute isolation runs each user's code in a sandbox, such as a separate process, container or lightweight virtual machine, with no direct access to storage credentials or other users' work, while the engine applies access policies to the data it passes to that code.

Row filters, column masks and other fine-grained controls can only be trusted on shared compute if user code cannot get around them. Without isolation, platforms force a choice between single-user clusters, which cost more and start slowly, and shared clusters with coarse permissions. Isolation lets many users share running compute safely. It differs from workload isolation, which separates workloads so they do not slow each other down, not to stop them reaching each other's data.

# Key considerations

- Check which languages and features run inside the sandbox. Some platforms restrict libraries, file-system access or network calls on shared compute.
- Confirm that user code cannot reach storage credentials, instance metadata endpoints or cluster-wide temporary storage.
- Sandboxing adds overhead to user-defined functions. Test performance for Python-heavy workloads.
- Decide which workloads still need dedicated compute, such as jobs needing privileged libraries or GPUs, and how those are secured.

# Questions to ask

- Do many users share clusters, and do they run their own code on them?
- Must row filters and column masks hold for notebook and DataFrame users, not only SQL users?
- Which libraries or system access do users need on shared compute?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md), [Query and compute](../compute/compute.md) |
| Related | [Agent hosting and runtime](../generative-ai/agent-runtime.md), [Column security and dynamic masking](column-masking.md), [Row-level security](row-level-security.md), [Storage credential vending](../storage/credential-vending.md), [User-defined functions and procedures](../processing/user-defined-functions.md), [Workload isolation](../compute/workload-isolation.md) |
| Depends on | [Access control](access-control.md) |

# Where it appears

- **Use cases:** [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 3, Defined) · [Security and access control](../../maturity/track-security.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeguard](../../technologies/databricks/databricks-lakeguard.md) |
