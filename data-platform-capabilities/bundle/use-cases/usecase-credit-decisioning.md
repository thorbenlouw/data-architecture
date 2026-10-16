---
type: Use Case
id: usecase-credit-decisioning
title: Credit decisioning
description: Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
requires:
- {capability: feature-engineering, level: 2, why: 'Application, bureau and account data become consistent applicant-level features.'}
- {capability: point-in-time-joins, level: 3, why: Development samples use bureau and account data as known on each application date.}
- {capability: model-training, level: 2, why: Scorecards and models are redeveloped as portfolios and economic conditions change.}
- capability: model-evaluation
  level: 3
  why: Discrimination, calibration and stability are tested by segment against the current model on an out-of-time sample.
- {capability: model-explainability, level: 3, why: 'Every decline needs reasons the applicant can understand, and validators need to see what drives the model.'}
- {capability: fairness-assessment, level: 3, why: Approval and error rates are compared across protected groups before release and in production.}
- {capability: model-registry, level: 3, why: The approved version used for decisions must be controlled and quick to roll back.}
- {capability: model-governance, level: 3, why: 'Each model has a risk tier, independent validation, committee approval and a review date.'}
- {capability: model-lineage, level: 3, why: 'Validators and regulators trace each version to its sample, features, code and parameters.'}
- capability: decision-management
  level: 3
  why: Policy rules, cut-offs and scores combine into approve, decline or refer outcomes through versioned strategies.
- capability: inference-logging
  level: 3
  why: Each decision is stored with its inputs, versions and reasons for the life of the agreement and the retention period after it.
- {capability: model-performance-monitoring, level: 3, why: Arrears and default rates are tracked by application cohort as outcomes mature over months.}
- {capability: drift-detection, level: 2, why: 'Population stability of applicants and scores is checked monthly, the standard early warning in credit risk.'}
- {capability: human-oversight, level: 2, why: Referred applications go to underwriters whose decisions and overrides are recorded.}
- capability: ai-impact-assessment
  level: 2
  why: Lenders using AI to assess individuals' creditworthiness must assess its impact on applicants' rights before first use.
- {capability: data-usage-rights, level: 2, why: Bureau and open banking data may be used only for the purposes their terms permit.}
benefits_from:
- {capability: champion-challenger, why: 'Challenger models and strategies run on a random share of applications, long-standing practice in credit risk.'}
- {capability: training-dataset-management, why: 'Frozen, documented development and validation samples let validators reproduce results.'}
- {capability: shadow-deployment, why: Tests a new model on live applications before it affects any decision.}
- {capability: real-time-inference, why: Digital applications are scored within seconds while the applicant waits.}
- {capability: entity-resolution, why: Links an applicant's existing products and previous applications.}
- {capability: compliance-evidence, why: 'Assembles validation, monitoring and approval records for supervisors.'}
personas:
- persona-data-scientist
- persona-ml-engineer
- persona-risk-compliance
- persona-data-engineer
- persona-business-user
patterns: [fti-pipelines]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lenders decide on loan, card and overdraft applications many thousands of times a day, and each decision must be fast, consistent, explainable to the applicant and fair. A decision service gathers application data and bureau and account history as known at that moment, runs a scorecard or machine learning model, applies policy rules and cut-offs, and returns approve, decline or refer with reason codes. Data scientists develop models on frozen development samples, independent validators review them, and the risk function approves each version before release.

Good looks like decisions that can be reproduced years later, reasons every declined applicant can understand, outcomes checked across protected groups before release and in production, and new models or strategies proven on a random share of applications before they replace the current ones. In the EU, creditworthiness assessment of individuals is a high-risk use under the AI Act, which adds duties for documentation, logging, human oversight and impact assessment.

# Non-functional requirements

- Online applications are decided within a few seconds, including bureau calls.
- Every decision can be reproduced with its inputs and its model, rule and policy versions for as long as records must be kept.
- A decline reason is produced for every declined applicant.
- Each model is validated independently before release and reviewed at least once a year.

# Risks

- Features such as postcode act as proxies for protected characteristics.
- Outcomes are seen only for approved applicants, so monitoring and retraining inherit the old model's choices.
- Underwriter overrides are not recorded, so the policy applied drifts from the policy written.
- A retrained model is released as a minor change without revalidation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Feature engineering](../capabilities/machine-learning/feature-engineering.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Application, bureau and account data become consistent applicant-level features. |
| [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Development samples use bureau and account data as known on each application date. |
| [Model training](../capabilities/machine-learning/model-training.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Scorecards and models are redeveloped as portfolios and economic conditions change. |
| [Model evaluation](../capabilities/machine-learning/model-evaluation.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Discrimination, calibration and stability are tested by segment against the current model on an out-of-time sample. |
| [Model explainability](../capabilities/machine-learning/model-explainability.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Every decline needs reasons the applicant can understand, and validators need to see what drives the model. |
| [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Approval and error rates are compared across protected groups before release and in production. |
| [Model registry](../capabilities/machine-learning/model-registry.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | The approved version used for decisions must be controlled and quick to roll back. |
| [Model governance](../capabilities/mlops/model-governance.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Each model has a risk tier, independent validation, committee approval and a review date. |
| [Model lineage](../capabilities/metadata/model-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Validators and regulators trace each version to its sample, features, code and parameters. |
| [Decision management](../capabilities/serving/decision-management.md) | [Serving and activation](../capabilities/serving/serving.md) | 3 (Defined) | Policy rules, cut-offs and scores combine into approve, decline or refer outcomes through versioned strategies. |
| [Inference logging](../capabilities/mlops/inference-logging.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Each decision is stored with its inputs, versions and reasons for the life of the agreement and the retention period after it. |
| [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Arrears and default rates are tracked by application cohort as outcomes mature over months. |
| [Drift detection](../capabilities/mlops/drift-detection.md) | [ML operations](../capabilities/mlops/mlops.md) | 2 (Managed) | Population stability of applicants and scores is checked monthly, the standard early warning in credit risk. |
| [Human oversight of AI](../capabilities/governance/human-oversight.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Referred applications go to underwriters whose decisions and overrides are recorded. |
| [AI impact assessment](../capabilities/governance/ai-impact-assessment.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Lenders using AI to assess individuals' creditworthiness must assess its impact on applicants' rights before first use. |
| [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Bureau and open banking data may be used only for the purposes their terms permit. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Champion-challenger](../capabilities/mlops/champion-challenger.md) | Challenger models and strategies run on a random share of applications, long-standing practice in credit risk. |
| [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) | Frozen, documented development and validation samples let validators reproduce results. |
| [Shadow deployment](../capabilities/mlops/shadow-deployment.md) | Tests a new model on live applications before it affects any decision. |
| [Real-time inference](../capabilities/mlops/real-time-inference.md) | Digital applications are scored within seconds while the applicant waits. |
| [Entity resolution](../capabilities/master-data/entity-resolution.md) | Links an applicant's existing products and previous applications. |
| [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) | Assembles validation, monitoring and approval records for supervisors. |

# Personas

- [Data scientist](../personas/persona-data-scientist.md): Explores data and builds statistical and machine learning models.
- [ML engineer](../personas/persona-ml-engineer.md): Takes models to production and keeps them running reliably.
- [Risk and compliance officer](../personas/persona-risk-compliance.md): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.

# Patterns

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md)

# Frameworks that apply

- [EU AI Act](../frameworks/framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [ISO/IEC 42001:2023](../frameworks/framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
- [NIST AI Risk Management Framework (AI RMF 1.0)](../frameworks/framework-nist-ai-rmf.md): A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 7 of 16 | [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 13 of 16 | [Decision management](../capabilities/serving/decision-management.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 11 of 16 | [Decision management](../capabilities/serving/decision-management.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 11 of 16 | [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Decision management](../capabilities/serving/decision-management.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Databricks](../platforms/platform-databricks.md) | 11 of 16 | [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Decision management](../capabilities/serving/decision-management.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 0 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Model governance](../capabilities/mlops/model-governance.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Informatica](../platforms/platform-informatica.md) | 2 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 4 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Oracle](../platforms/platform-oracle.md) | 4 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model governance](../capabilities/mlops/model-governance.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [SAP](../platforms/platform-sap.md) | 1 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Model governance](../capabilities/mlops/model-governance.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Teradata](../platforms/platform-teradata.md) | 6 of 16 (+1 in preview) | [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) (preview only) |
| [IBM](../platforms/platform-ibm.md) | 7 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Palantir](../platforms/platform-palantir.md) | 6 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Decision management](../capabilities/serving/decision-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 8 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model governance](../capabilities/mlops/model-governance.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Decision management](../capabilities/serving/decision-management.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
| [Independent vendors](../platforms/platform-independent.md) | 12 of 16 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |
