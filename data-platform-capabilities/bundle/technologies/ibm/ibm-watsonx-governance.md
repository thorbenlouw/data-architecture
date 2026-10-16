---
type: Technology
id: ibm-watsonx-governance
title: IBM watsonx.governance
description: AI governance product that inventories AI use cases and models, including detected unapproved use, maps them to regulations, monitors them and records evidence and decisions.
platform: platform-ibm
kind: managed-service
availability: ga
realises:
- ai-governance
- model-governance
- compliance-evidence
- drift-detection
- fairness-assessment
- ai-system-discovery
- ai-impact-assessment
- genai-evaluation
- model-performance-monitoring
resource: https://www.ibm.com/products/watsonx-governance
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Includes regulatory content for the EU AI Act, NIST AI RMF and ISO 42001. Monitoring of fairness, drift and generative AI quality metrics comes from the former Watson OpenScale; factsheets record model lineage. Governs models built outside IBM, such as on AWS and Azure.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI governance](../../capabilities/governance/ai-governance.md) (Governance and compliance) (primary): Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance): Map regulatory requirements to platform controls and produce evidence for auditors.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
- [Bias and fairness assessment](../../capabilities/machine-learning/fairness-assessment.md) (Machine learning development): Measure whether a model's outcomes differ unfairly across groups of people.
- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.
- [AI impact assessment](../../capabilities/governance/ai-impact-assessment.md) (Governance and compliance): Assess and record an AI system's effects on people and society before release and whenever it changes.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations): Measure prediction quality over time against ground truth as it arrives.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview), [Microsoft Purview Compliance Manager](../microsoft/purview-compliance-manager.md) | [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [AI governance](../../capabilities/governance/ai-governance.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [AI governance](../../capabilities/governance/ai-governance.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md), [Holistic AI Governance Platform](../independent/holistic-ai-governance-platform.md), [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed) | [AI governance](../../capabilities/governance/ai-governance.md), [AI impact assessment](../../capabilities/governance/ai-impact-assessment.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
