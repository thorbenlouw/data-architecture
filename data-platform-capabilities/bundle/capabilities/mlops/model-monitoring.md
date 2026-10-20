---
type: Capability
id: model-monitoring
title: Model monitoring
description: Track the health of production models, including inputs, outputs, quality and service metrics.
aliases: [ML observability, model observability]
broader: [mlops]
related:
- data-observability
- genai-observability
- platform-observability
- ai-incident-management
- continuous-training
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Monitoring works on several layers. Service metrics cover request rate, latency and errors. Input metrics cover missing values, out-of-range values and changes in distribution. Output metrics cover the predictions themselves, such as the share of loans approved or the average fraud score. Quality metrics compare predictions with actual outcomes once these are known. Dashboards show each layer over time per model version, and alerts fire when thresholds or statistical tests are breached.

Models fail quietly. An upstream change that switches a currency field from pounds to pence leaves the service healthy while its predictions become nonsense, and monitoring is how teams find out before customers or finance do. It builds on inference logs and feeds continuous training and incident handling. It overlaps with data observability, which watches tables and pipelines, and with generative AI observability, which traces prompts and responses. Model monitoring adds the link between features, predictions and outcomes for one model version.

# Key considerations

- Monitor inputs and outputs from the first release. Quality metrics may take weeks to become available.
- Set and review thresholds per model and feature. Default thresholds across hundreds of features cause alert fatigue.
- Break metrics down by key segments such as region or product, since problems often start in one segment.
- Send alerts to a named owner with a runbook that says what to check and when to roll back.

# Questions to ask

- How would you know today if a production model's predictions became wrong?
- When do true outcomes become known, and are they captured in the platform?
- Who responds to a model alert outside working hours?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [ML operations](mlops.md) |
| Narrower | [Bias and fairness assessment](../machine-learning/fairness-assessment.md), [Drift detection](drift-detection.md), [Inference logging](inference-logging.md), [Model performance monitoring](model-performance-monitoring.md) |
| Related | [AI incident management](../governance/ai-incident-management.md), [Continuous training](continuous-training.md), [Data observability](../data-quality/data-observability.md), [Edge inference](edge-inference.md), [Generative AI observability](../generative-ai/genai-observability.md), [Platform observability](../platform-operations/platform-observability.md) |

# Where it appears

- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 14 – Human oversight; Article 26 – Obligations of deployers; Article 72 – Post-market monitoring; Article 73 – Reporting of serious incidents · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Model monitoring · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 9 – Performance evaluation; Annex A.6 – AI system life cycle; Annex A.9 – Use of AI systems · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 4 – Full MLOps automated operations · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MEASURE 3 – Tracking risks over time; MANAGE 3 – Third-party risk monitoring; MANAGE 4 – Response, recovery and communication

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Model Monitor](../../technologies/aws/aws-sagemaker-model-monitor.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning model monitoring](../../technologies/microsoft/azure-ml-model-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Model Monitoring on Agent Platform](../../technologies/google-cloud/gcp-model-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | ML Observability (model monitors) | [Snowflake ML Observability (model monitors)](../../technologies/snowflake/snowflake-ml-observability.md) |

Narrower capabilities are realised by a further 24 technologies; see their pages.
