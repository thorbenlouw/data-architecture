---
type: Technology
id: presidio
title: Microsoft Presidio
description: Toolkit that detects personal data in text, images and structured data and masks, replaces or encrypts it.
aliases: [Presidio]
platform: platform-open-source
kind: open-source
availability: ga
realises: [deidentification, data-classification, ai-guardrails]
resource: https://microsoft.github.io/presidio/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

MIT licence, Microsoft-led. Combines named-entity recognition, patterns and context rules with customisable recognisers. Often used to filter prompts and documents before they reach language models.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance) (primary): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Guardrails](../aws/aws-bedrock-guardrails.md), [Amazon Comprehend](../aws/aws-comprehend.md), [AWS Glue DataBrew](../aws/aws-glue-databrew.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [De-identification](../../capabilities/governance/deidentification.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Language PII detection](../microsoft/azure-ai-language-pii.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md), [BigQuery data masking](../google-cloud/gcp-bigquery-data-masking.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake masking policies](../snowflake/snowflake-masking-policies.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Data Masking transformation](../informatica/informatica-data-masking-transformation.md), [Informatica Test Data Management (TDM)](../informatica/informatica-test-data-management.md), [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM InfoSphere Optim](../ibm/ibm-optim.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md), [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md), [Tonic Textual](../independent/tonic-textual.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
