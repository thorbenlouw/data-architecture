---
type: Technology
id: dataiku-govern
title: Dataiku Govern
description: Separate governance node that keeps registries of projects, bundles, models and agents, with sign-off workflows, deployment policies and custom governance templates.
platform: platform-dataiku
kind: software
availability: ga
realises: [model-governance, ai-governance, model-registry, agent-registry]
resource: https://doc.dataiku.com/dss/latest/governance/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

The Standard licence covers the core features; the Advanced licence adds governance of agents and an agent registry page, custom actions, custom governance templates, custom pages and scripted governance settings. The Deployer checks the final sign-off status in Govern, so deployment policies can block releases that lack approval.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations) (primary): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [AI governance](../../capabilities/governance/ai-governance.md) (Governance and compliance): Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Model Registry](../aws/aws-sagemaker-model-registry.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Registry](../snowflake/snowflake-model-registry.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Models in Unity Catalog](../databricks/databricks-models-in-unity-catalog.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata ModelOps](../teradata/teradata-modelops.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Model Manager](../sas/sas-model-manager.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md), [OneTrust AI Governance](../independent/onetrust-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
