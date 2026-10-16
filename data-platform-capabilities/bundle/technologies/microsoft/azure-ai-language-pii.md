---
type: Technology
id: azure-ai-language-pii
title: Azure AI Language PII detection
description: Detects and redacts personal and health information in text and conversations.
platform: platform-microsoft
kind: feature
availability: ga
realises: [deidentification]
resource: https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Part of Foundry Tools; useful for redacting data before it reaches analytics or LLM prompts.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance) (primary): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Foundry Tools

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Guardrails](../aws/aws-bedrock-guardrails.md), [Amazon Comprehend](../aws/aws-comprehend.md), [AWS Glue DataBrew](../aws/aws-glue-databrew.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data masking](../google-cloud/gcp-bigquery-data-masking.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake masking policies](../snowflake/snowflake-masking-policies.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Data Masking transformation](../informatica/informatica-data-masking-transformation.md), [Informatica Test Data Management (TDM)](../informatica/informatica-test-data-management.md), [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM InfoSphere Optim](../ibm/ibm-optim.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Microsoft Presidio](../open-source/presidio.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tonic Textual](../independent/tonic-textual.md), [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md), [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md) | [De-identification](../../capabilities/governance/deidentification.md) |
