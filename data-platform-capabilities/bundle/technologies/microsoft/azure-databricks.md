---
type: Technology
id: azure-databricks
title: Azure Databricks
description: The Databricks Data Intelligence Platform delivered as a first-party Azure service, billed through Azure and integrated with Entra ID and ADLS.
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [distributed-processing]
distribution_of: platform-databricks
resource: https://learn.microsoft.com/en-us/azure/databricks/introduction/
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runs the [Databricks platform](../../platforms/platform-databricks.md), including Unity Catalog, Lakeflow and Agent Bricks, as a first-party Azure service: it is bought and billed through Azure, uses Microsoft Entra ID for sign-in and stores data in Azure Data Lake Storage. Interoperates with Fabric through the [mirrored Azure Databricks catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md) and OneLake shortcuts.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Distribution of:** [Databricks](../../platforms/platform-databricks.md). It is not counted in Microsoft Azure and Fabric's coverage.
