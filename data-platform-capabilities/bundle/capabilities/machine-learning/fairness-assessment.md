---
type: Capability
id: fairness-assessment
title: Bias and fairness assessment
description: Measure whether a model's outcomes differ unfairly across groups of people.
broader: [model-evaluation, model-monitoring]
related:
- model-governance
- ai-impact-assessment
- data-classification
- drift-detection
- privacy-impact-assessment
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The usual method is to define groups, such as sex, age band or ethnicity, and compare outcomes and error rates between them. Common measures ask whether groups are approved at similar rates (demographic parity), whether qualified people in each group are equally likely to be approved (equal opportunity), and whether false positive rates differ. A hiring screen that rejects equally qualified older applicants twice as often as younger ones would show a gap in true positive rates.

It matters for any model that affects access to credit, jobs, housing, insurance or services, and anti-discrimination and AI rules increasingly expect it to be done and recorded. When base rates differ between groups, the common measures cannot all be met at once, so choosing one is a policy decision. Assessment needs data on protected characteristics, which may be sensitive or not collected; inferred proxies carry their own errors. Mitigation can change the training data, the training objective or the decision thresholds.

# Key considerations

- Agree with legal and business owners which fairness measure applies before testing. The choice changes the result.
- Removing protected characteristics from the inputs does not remove bias, because other features act as proxies for them.
- Holding protected characteristics for testing is sensitive processing in its own right. Restrict access and record the purpose.
- Repeat the assessment in production, since a model that was fair at release can drift as the population changes.

# Questions to ask

- Does the model affect people's access to credit, employment, insurance, housing or public services?
- Is data on protected characteristics available, lawful to use for testing and of good quality?
- Who decides what level of difference between groups is acceptable?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Model evaluation](model-evaluation.md), [Model monitoring](../mlops/model-monitoring.md) |
| Related | [AI impact assessment](../governance/ai-impact-assessment.md), [Data classification](../governance/data-classification.md), [Drift detection](../mlops/drift-detection.md), [Model explainability](model-explainability.md), [Model governance](../mlops/model-governance.md), [Privacy impact assessment](../governance/privacy-impact-assessment.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 3, Defined) · [ML development](../../maturity/track-ml-development.md) (from level 4, Measured)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Handling Ethics · [DCAM v3](../../frameworks/framework-edm-dcam.md): 8 Analytics Management · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 4a – Special categories of personal data for bias detection; Article 10 – Data and data governance; Article 27 – Fundamental rights impact assessment · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 6 – Planning; Annex A.5 – Assessing impacts of AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MAP 5 – Impacts; MEASURE 2 – Evaluation for trustworthy characteristics

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Clarify](../../technologies/aws/aws-sagemaker-clarify.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning Responsible AI dashboard](../../technologies/microsoft/azure-ml-responsible-ai-dashboard.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Model Evaluation](../../technologies/google-cloud/gcp-agent-platform-model-evaluation.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.governance](../../technologies/ibm/ibm-watsonx-governance.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Holistic AI Governance Platform](../../technologies/independent/holistic-ai-governance-platform.md) |
