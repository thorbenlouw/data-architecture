---
type: Capability
id: inference-logging
title: Inference logging
description: Capture model inputs, outputs and metadata for monitoring, audit and retraining.
aliases: [payload logging, inference tables]
broader: [model-monitoring]
related: [audit-logging, data-retention, event-streaming, genai-observability, model-lineage]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each prediction is recorded with a request id, timestamp, model name and version, the input features as the model received them, the output, and context such as the calling application and which release variant served it. The serving layer writes these records asynchronously to a stream or table, so logging adds no delay to the response. A batch job records the same details as columns alongside its scores.

Almost everything after deployment depends on these logs. Drift detection reads the inputs, performance monitoring joins outputs to outcomes, release strategies compare versions, auditors reconstruct why a decision was made, and later training sets reuse features exactly as served, which avoids skew. Logging every request of a high-volume model is costly, so some teams sample, but sampling weakens audit and rare-event analysis. Logs often hold personal data and need the same retention and access rules as their sources. Unlike general audit logs of user access, they record model decisions.

# Key considerations

- Log features as served, not recomputed later. Recomputed values hide the very skew you want to find.
- Decide per model between full logging and sampling, based on audit needs and volume.
- Apply retention, access control and de-identification to the logs, which can hold sensitive inputs.
- Use a stable request id that downstream systems can attach outcomes to.

# Questions to ask

- Must individual automated decisions be reconstructable for customers, auditors or regulators?
- How many predictions are made per day, and how long must records be kept?
- Do logged inputs contain personal or confidential data?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model monitoring](model-monitoring.md) |
| Related | [Audit logging](../security/audit-logging.md), [Event streaming](../ingestion-integration/event-streaming.md), [Generative AI observability](../generative-ai/genai-observability.md), [Model explainability](../machine-learning/model-explainability.md), [Model lineage](../metadata/model-lineage.md), [Retention and disposal](../governance/data-retention.md) |
| Needed by | [AI incident management](../governance/ai-incident-management.md), [Canary and A/B testing](canary-ab-testing.md), [Champion-challenger](champion-challenger.md), [Drift detection](drift-detection.md), [Model performance monitoring](model-performance-monitoring.md), [Model release strategies](model-release-strategies.md), [Shadow deployment](shadow-deployment.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 2, Managed)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 12 – Record-keeping; Articles 19 and 26(6) – Log retention; Article 26 – Obligations of deployers; Article 72 – Post-market monitoring; Article 73 – Reporting of serious incidents · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Model monitoring · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.6 – AI system life cycle · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 4 – Full MLOps automated operations

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Model Monitor](../../technologies/aws/aws-sagemaker-model-monitor.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning model monitoring](../../technologies/microsoft/azure-ml-model-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Endpoints](../../technologies/google-cloud/gcp-agent-platform-endpoints.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Observability (model monitors)](../../technologies/snowflake/snowflake-ml-observability.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks inference tables](../../technologies/databricks/databricks-inference-tables.md), [MLflow Tracing on Databricks](../../technologies/databricks/databricks-mlflow-tracing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [KServe](../../technologies/open-source/kserve.md), [OpenTelemetry semantic conventions for generative AI](../../technologies/open-source/opentelemetry-genai-semantic-conventions.md) (preview) |
