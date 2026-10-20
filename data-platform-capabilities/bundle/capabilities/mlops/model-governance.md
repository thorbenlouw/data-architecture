---
type: Capability
id: model-governance
title: Model governance
description: Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
aliases: [model risk management, model cards]
broader: [mlops, governance]
related: [ai-governance, fairness-assessment, model-explainability, ai-system-discovery, compliance-evidence]
depends_on: [model-registry]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A bank's credit scoring model carries an independent validation report, sign-off from a model risk committee, documented limitations and an annual review date. A low-risk internal forecasting model may need only a named owner and brief documentation. Model governance keeps such records for every model in one inventory: purpose, owner, risk tier, decisions affected, data sources, validation evidence, approvals and review dates. The platform helps by linking the inventory to the registry, lineage, evaluation results and monitoring, so evidence is collected as work happens rather than assembled by hand.

Regulated industries have long had supervisory expectations for model risk management, and AI regulation is extending similar duties to other sectors. Elsewhere it matters wherever models affect customers, money or safety. Tiering by risk keeps controls in proportion. Model governance covers predictive models; AI governance is wider, taking in generative AI, agents and third-party AI services, and usually contains model governance as one part. Model cards are a common format for documenting each model.

# Key considerations

- Tier models by risk and scale controls to the tier. Applying the strictest process to every model slows low-risk work for no benefit.
- Collect documentation, lineage and approvals automatically from the platform where possible. Hand-kept records go out of date.
- Include vendor-supplied and embedded models in the inventory, not only those built in-house.
- Define which changes are material and need revalidation, such as new features or a retrained version.

# Questions to ask

- Do regulations or internal policies require model validation, an inventory or periodic review?
- How many models are in production today, and could you list them with their owners?
- Who has authority to approve a model for use, and how is that recorded?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [ML operations](mlops.md), [Governance and compliance](../governance/governance.md) |
| Narrower | [Model lineage](../metadata/model-lineage.md) |
| Related | [AI governance](../governance/ai-governance.md), [AI impact assessment](../governance/ai-impact-assessment.md), [AI supply chain security](../security/ai-supply-chain-security.md), [AI system discovery](../governance/ai-system-discovery.md), [Bias and fairness assessment](../machine-learning/fairness-assessment.md), [Champion-challenger](champion-challenger.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Model deployment](model-deployment.md), [Model explainability](../machine-learning/model-explainability.md) |
| Depends on | [Model registry](../machine-learning/model-registry.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 2, Managed) · [MLOps](../../maturity/track-mlops.md) (from level 3, Defined)
- **Frameworks:** [DCAM v3](../../frameworks/framework-edm-dcam.md): 8 Analytics Management · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 6 and Annex III – Classification as high-risk; Article 9 – Risk management system; Article 11 and Annex IV – Technical documentation; Article 13 – Transparency and information to deployers; Article 49 – Registration; Article 53 – Obligations of general-purpose AI model providers · [GDPR](../../frameworks/framework-gdpr.md): Article 22 – Automated individual decision-making · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 5 – Leadership; Clause 6 – Planning; Clause 7 – Support; Clause 8 – Operation; Annex A.3 – Internal organisation; Annex A.4 – Resources for AI systems; Annex A.8 – Information for interested parties · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 2 – Accountability structures; GOVERN 6 – Third-party risk; MAP 1 – Context; MAP 2 – Categorisation; MANAGE 1 – Risk response

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Model Registry](../../technologies/aws/aws-sagemaker-model-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Foundry Control Plane](../../technologies/microsoft/azure-foundry-control-plane.md) (preview) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Model Registry](../../technologies/snowflake/snowflake-model-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Models in Unity Catalog](../../technologies/databricks/databricks-models-in-unity-catalog.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica CDGC AI governance](../../technologies/informatica/informatica-cdgc-ai-governance.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata ModelOps](../../technologies/teradata/teradata-modelops.md) |
| [IBM](../../platforms/platform-ibm.md) | AI factsheets / watsonx.governance | [IBM watsonx.governance](../../technologies/ibm/ibm-watsonx-governance.md) |
| [SAS](../../platforms/platform-sas.md) | Model cards | [SAS Model Manager](../../technologies/sas/sas-model-manager.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Govern](../../technologies/dataiku/dataiku-govern.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra AI Command Center](../../technologies/independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../../technologies/independent/credo-ai-governance-platform.md), [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md), [Domino Enterprise AI Platform](../../technologies/independent/domino-enterprise-ai-platform.md), [OneTrust AI Governance](../../technologies/independent/onetrust-ai-governance.md) |

Narrower capabilities are realised by a further 10 technologies; see their pages.
