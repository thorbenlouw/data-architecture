---
type: Framework
id: framework-eu-ai-act
title: EU AI Act
description: Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
aliases: [AI Act, Artificial Intelligence Act, Regulation (EU) 2024/1689, EU AIA]
kind: regulation
publisher: European Union
resource: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
related: [framework-iso-iec-42001, framework-nist-ai-rmf, framework-gdpr]
applies_to:
- usecase-credit-decisioning
- usecase-agentic-automation
- usecase-rag-assistant
- usecase-document-extraction
- persona-risk-compliance
- persona-ai-engineer
- persona-ml-engineer
- persona-cdo
mappings:
- ref: Article 4 – AI literacy
  summary: Providers and deployers support adequate AI literacy among staff who operate or use AI, a duty the Omnibus softened so that no specific level must be guaranteed.
  capabilities: [ai-governance]
- ref: Article 4a – Special categories of personal data for bias detection
  summary: The Omnibus moved the permission to process sensitive personal data, under conditions such as pseudonymisation, strict access control, deletion after use and a recorded justification, to detect and correct bias from Article 10(5) into a new article.
  capabilities:
  - fairness-assessment
  - privacy-enhancing-technologies
  - deidentification
  - access-control
  - data-retention
  - records-of-processing
  - data-classification
- ref: Article 5 – Prohibited AI practices
  summary: Bans practices such as social scoring and workplace emotion recognition, with a ninth ban on non-consensual intimate and abusive content generation from 2 December 2026.
  capabilities: [ai-governance, ai-system-discovery, ai-guardrails]
- ref: Article 6 and Annex III – Classification as high-risk
  summary: Organisations must find the AI systems they use or provide and identify which fall into high-risk categories such as credit scoring or recruitment.
  capabilities: [ai-system-discovery, agent-registry, model-governance, ai-governance]
- ref: Article 9 – Risk management system
  summary: Providers of high-risk systems run a continuous process to identify, assess, test and reduce risks to health, safety and fundamental rights throughout the system's life.
  capabilities: [ai-governance, model-governance, ai-impact-assessment, model-evaluation, ai-red-teaming]
- ref: Article 10 – Data and data governance
  summary: Training, validation and test data must be governed for origin, preparation, assumptions, gaps and bias, and be relevant, representative and as error-free as possible.
  capabilities:
  - training-dataset-management
  - data-lineage
  - data-profiling
  - data-quality-rules
  - data-labelling
  - data-cleansing
  - fairness-assessment
- ref: Article 11 and Annex IV – Technical documentation
  summary: Providers keep up-to-date documentation that shows how the system was built, trained and tested, including the datasets used.
  capabilities: [model-governance, model-lineage, training-dataset-management, experiment-tracking, model-registry]
- ref: Article 12 – Record-keeping
  summary: High-risk systems must log events automatically over their lifetime to support traceability and monitoring.
  capabilities: [inference-logging, audit-logging, genai-observability]
- ref: Article 13 – Transparency and information to deployers
  summary: Providers give deployers clear instructions, including capabilities, limits and how to interpret outputs.
  capabilities: [model-governance, model-explainability]
- ref: Article 14 – Human oversight
  summary: High-risk systems must be designed so that people can understand, monitor, override and stop them.
  capabilities: [human-oversight, model-explainability, model-monitoring, ai-guardrails]
- ref: Article 15 – Accuracy, robustness and cybersecurity
  summary: High-risk systems must perform consistently, declare their accuracy levels and resist errors and attacks such as data poisoning, model poisoning and adversarial inputs.
  capabilities:
  - model-evaluation
  - model-performance-monitoring
  - ai-red-teaming
  - ai-supply-chain-security
  - ai-guardrails
  - drift-detection
- ref: Article 17 – Quality management system
  summary: Providers run a documented quality management system covering design, testing, data management, post-market monitoring and serious incident reporting.
  capabilities: [ai-governance, compliance-evidence, ml-cicd, training-dataset-management, ai-incident-management]
- ref: Articles 19 and 26(6) – Log retention
  summary: Providers and deployers keep the logs they control for a period suited to the purpose and for at least six months.
  capabilities: [inference-logging, data-retention, audit-logging]
- ref: Article 26 – Obligations of deployers
  summary: Deployers use systems as instructed, assign human oversight, make sure input data they control is relevant and representative, monitor operation and report serious incidents.
  capabilities:
  - human-oversight
  - model-monitoring
  - data-quality-rules
  - ai-incident-management
  - inference-logging
  - ai-governance
- ref: Article 27 – Fundamental rights impact assessment
  summary: Certain deployers of high-risk systems, such as public bodies and credit or insurance providers, assess the impact on people's rights and the oversight measures in place before first use, alongside any data protection impact assessment.
  capabilities:
  - ai-impact-assessment
  - fairness-assessment
  - human-oversight
  - privacy-impact-assessment
  - compliance-evidence
- ref: Article 49 – Registration
  summary: High-risk systems, and systems claimed to be exempt, are registered in the EU database, a duty the Omnibus simplified for exempt systems.
  capabilities: [ai-governance, model-governance, ai-system-discovery]
- ref: Article 50 – Transparency obligations
  summary: People must be told when they deal with AI, synthetic content must be marked so that machines can detect it and deepfakes must be disclosed.
  capabilities: [ai-content-provenance, ai-governance, ai-guardrails]
- ref: Article 53 – Obligations of general-purpose AI model providers
  summary: Model providers keep technical documentation, inform downstream integrators, follow a copyright policy that respects rights reservations and publish a summary of training content.
  capabilities:
  - model-governance
  - training-dataset-management
  - data-usage-rights
  - model-lineage
  - unstructured-lineage
- ref: Article 72 – Post-market monitoring
  summary: Providers collect and analyse data on how high-risk systems perform once in use.
  capabilities:
  - model-monitoring
  - model-performance-monitoring
  - drift-detection
  - inference-logging
  - genai-observability
- ref: Article 73 – Reporting of serious incidents
  summary: Providers, and deployers through them, report serious incidents to market surveillance authorities within set deadlines and investigate their causes.
  capabilities: [ai-incident-management, model-monitoring, inference-logging]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The AI Act classifies AI by risk: banned practices, high-risk systems with strict obligations, transparency duties for systems such as chatbots and content generators, and rules for providers of general-purpose AI models; the Digital Omnibus on AI (Regulation (EU) 2026/1744, in force since 27 July 2026) amended it. As of October 2026 the prohibitions and AI literacy duties have applied since 2 February 2025, general-purpose AI obligations since 2 August 2025, and most other rules, including Article 50 transparency and enforcement, since 2 August 2026. Still to come are a ninth prohibition and the Article 50(2) deadline for content generators already on the market (2 December 2026), compliance for general-purpose models placed on the market before August 2025 (2 August 2027), high-risk rules for Annex III uses (2 December 2027, delayed from August 2026) and for Annex I products (2 August 2028). For platforms, the high-risk requirements on data governance, logging, documentation, oversight and monitoring translate most directly into capabilities.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Article 4 – AI literacy | Providers and deployers support adequate AI literacy among staff who operate or use AI, a duty the Omnibus softened so that no specific level must be guaranteed. | [AI governance](../capabilities/governance/ai-governance.md) |
| Article 4a – Special categories of personal data for bias detection | The Omnibus moved the permission to process sensitive personal data, under conditions such as pseudonymisation, strict access control, deletion after use and a recorded justification, to detect and correct bias from Article 10(5) into a new article. | [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [De-identification](../capabilities/governance/deidentification.md), [Access control](../capabilities/security/access-control.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Data classification](../capabilities/governance/data-classification.md) |
| Article 5 – Prohibited AI practices | Bans practices such as social scoring and workplace emotion recognition, with a ninth ban on non-consensual intimate and abusive content generation from 2 December 2026. | [AI governance](../capabilities/governance/ai-governance.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| Article 6 and Annex III – Classification as high-risk | Organisations must find the AI systems they use or provide and identify which fall into high-risk categories such as credit scoring or recruitment. | [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Model governance](../capabilities/mlops/model-governance.md), [AI governance](../capabilities/governance/ai-governance.md) |
| Article 9 – Risk management system | Providers of high-risk systems run a continuous process to identify, assess, test and reduce risks to health, safety and fundamental rights throughout the system's life. | [AI governance](../capabilities/governance/ai-governance.md), [Model governance](../capabilities/mlops/model-governance.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md) |
| Article 10 – Data and data governance | Training, validation and test data must be governed for origin, preparation, assumptions, gaps and bias, and be relevant, representative and as error-free as possible. | [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md) |
| Article 11 and Annex IV – Technical documentation | Providers keep up-to-date documentation that shows how the system was built, trained and tested, including the datasets used. | [Model governance](../capabilities/mlops/model-governance.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model registry](../capabilities/machine-learning/model-registry.md) |
| Article 12 – Record-keeping | High-risk systems must log events automatically over their lifetime to support traceability and monitoring. | [Inference logging](../capabilities/mlops/inference-logging.md), [Audit logging](../capabilities/security/audit-logging.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| Article 13 – Transparency and information to deployers | Providers give deployers clear instructions, including capabilities, limits and how to interpret outputs. | [Model governance](../capabilities/mlops/model-governance.md), [Model explainability](../capabilities/machine-learning/model-explainability.md) |
| Article 14 – Human oversight | High-risk systems must be designed so that people can understand, monitor, override and stop them. | [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| Article 15 – Accuracy, robustness and cybersecurity | High-risk systems must perform consistently, declare their accuracy levels and resist errors and attacks such as data poisoning, model poisoning and adversarial inputs. | [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Drift detection](../capabilities/mlops/drift-detection.md) |
| Article 17 – Quality management system | Providers run a documented quality management system covering design, testing, data management, post-market monitoring and serious incident reporting. | [AI governance](../capabilities/governance/ai-governance.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [AI incident management](../capabilities/governance/ai-incident-management.md) |
| Articles 19 and 26(6) – Log retention | Providers and deployers keep the logs they control for a period suited to the purpose and for at least six months. | [Inference logging](../capabilities/mlops/inference-logging.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Audit logging](../capabilities/security/audit-logging.md) |
| Article 26 – Obligations of deployers | Deployers use systems as instructed, assign human oversight, make sure input data they control is relevant and representative, monitor operation and report serious incidents. | [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [Inference logging](../capabilities/mlops/inference-logging.md), [AI governance](../capabilities/governance/ai-governance.md) |
| Article 27 – Fundamental rights impact assessment | Certain deployers of high-risk systems, such as public bodies and credit or insurance providers, assess the impact on people's rights and the oversight measures in place before first use, alongside any data protection impact assessment. | [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| Article 49 – Registration | High-risk systems, and systems claimed to be exempt, are registered in the EU database, a duty the Omnibus simplified for exempt systems. | [AI governance](../capabilities/governance/ai-governance.md), [Model governance](../capabilities/mlops/model-governance.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md) |
| Article 50 – Transparency obligations | People must be told when they deal with AI, synthetic content must be marked so that machines can detect it and deepfakes must be disclosed. | [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI governance](../capabilities/governance/ai-governance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| Article 53 – Obligations of general-purpose AI model providers | Model providers keep technical documentation, inform downstream integrators, follow a copyright policy that respects rights reservations and publish a summary of training content. | [Model governance](../capabilities/mlops/model-governance.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| Article 72 – Post-market monitoring | Providers collect and analyse data on how high-risk systems perform once in use. | [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| Article 73 – Reporting of serious incidents | Providers, and deployers through them, report serious incidents to market surveillance authorities within set deadlines and investigate their causes. | [AI incident management](../capabilities/governance/ai-incident-management.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Inference logging](../capabilities/mlops/inference-logging.md) |

# Related frameworks

- [ISO/IEC 42001:2023](framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
- [NIST AI Risk Management Framework (AI RMF 1.0)](framework-nist-ai-rmf.md): A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.
- [GDPR](framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.

# Applies to

- [Credit decisioning](../use-cases/usecase-credit-decisioning.md) (use case): Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
- [Agentic process automation](../use-cases/usecase-agentic-automation.md) (use case): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md) (use case): A generative AI assistant that answers questions from internal documents, with citations.
- [Document data extraction](../use-cases/usecase-document-extraction.md) (use case): Extract fields and tables from invoices, claims, contracts and forms into business systems, with people reviewing uncertain results.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [AI engineer](../personas/persona-ai-engineer.md) (persona): Builds applications and agents on foundation models and enterprise data.
- [ML engineer](../personas/persona-ml-engineer.md) (persona): Takes models to production and keeps them running reliably.
- [Chief data officer](../personas/persona-cdo.md) (persona): Accountable for the organisation's data strategy, value, risk and governance.
