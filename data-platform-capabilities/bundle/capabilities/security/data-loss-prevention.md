---
type: Capability
id: data-loss-prevention
title: Data loss prevention
description: Detect and block sensitive data leaving approved boundaries.
aliases: [DLP, exfiltration protection]
broader: [security]
related: [data-classification, network-security, ai-guardrails, data-export, external-data-sharing]
depends_on: [data-classification]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data loss prevention (DLP) watches the routes by which data can leave approved boundaries and stops or flags sensitive content. On a data platform those routes include downloads and exports of query results, copies to external storage, shares with other accounts, reports sent by email or chat, calls from code to external APIs, and prompts sent to AI services. Controls look at content and context: a policy might block downloads of more than 10,000 rows tagged `personal` to unmanaged devices, or redact card numbers in prompts before they reach an external model.

DLP is a last line of defence after access control. It deals with people who legitimately have access but move data where it should not go, by mistake or on purpose. Platform settings such as disabling export, restricting external sharing and limiting egress are usually more reliable than content inspection, which raises false positives and misses data in unusual formats. Threat detection differs: it looks for abnormal behaviour rather than specific content leaving.

# Key considerations

- List every exit route first, including APIs, connectors, notebooks, BI downloads and AI assistants, then decide which to block, restrict or monitor.
- Base policies on classification tags where possible, and use content inspection for unstructured data and free text.
- Tune for false positives. Policies that block legitimate work too often get switched off or worked around.
- Treat AI prompts and agent tool calls as an exit route that needs the same policies as exports.

# Questions to ask

- Which routes out of the platform exist, and which are monitored today?
- Should exports and downloads of sensitive data be blocked, limited or only logged?
- Are users allowed to paste platform data into external AI services?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Related | [AI guardrails](../generative-ai/ai-guardrails.md), [Data classification](../governance/data-classification.md), [Data export](../serving/data-export.md), [Data threat detection](data-threat-detection.md), [External data sharing](../data-sharing/external-data-sharing.md), [Network security](network-security.md), [Spreadsheet integration](../analytics-bi/spreadsheet-integration.md) |
| Depends on | [Data classification](../governance/data-classification.md) |

# Where it appears

- **Use cases:** [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 4, Measured)
- **Frameworks:** [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(f) – Integrity and confidentiality; Articles 33 and 34 – Personal data breach notification

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock Guardrails](../../technologies/aws/aws-bedrock-guardrails.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric workspace outbound access protection](../../technologies/microsoft/fabric-outbound-access-protection.md), [Microsoft Purview Data Loss Prevention](../../technologies/microsoft/purview-data-loss-prevention.md), [Microsoft Purview Insider Risk Management](../../technologies/microsoft/purview-insider-risk-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | VPC Service Controls perimeters | [Model Armor](../../technologies/google-cloud/gcp-model-armor.md), [VPC Service Controls](../../technologies/google-cloud/gcp-vpc-service-controls.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks serverless egress control](../../technologies/databricks/databricks-serverless-egress-control.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Cyera DSPM](../../technologies/independent/cyera-dspm.md) |
