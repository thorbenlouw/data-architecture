---
type: Technology
id: informatica-data-masking-transformation
title: Informatica Data Masking transformation
description: Mapping transformation that replaces sensitive values with realistic masked values per column while keeping referential integrity across tables, for non-production copies.
aliases: [Cloud Data Masking]
platform: platform-informatica
kind: feature
availability: ga
realises: [deidentification, test-data-management]
resource: https://docs.informatica.com/integration-cloud/data-integration/current-version/transformations/data-masking-transformation.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This is persistent, in-pipeline masking, separate from CDAM's policy-driven controls. Masking runs in Data Integration mappings and is billed in IPUs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance) (primary): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps): Provide realistic, safe data for development and testing through subsetting, masking or generation.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Guardrails](../aws/aws-bedrock-guardrails.md), [Amazon Comprehend](../aws/aws-comprehend.md), [AWS Glue DataBrew](../aws/aws-glue-databrew.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Language PII detection](../microsoft/azure-ai-language-pii.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data masking](../google-cloud/gcp-bigquery-data-masking.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake masking policies](../snowflake/snowflake-masking-policies.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [De-identification](../../capabilities/governance/deidentification.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM InfoSphere Optim](../ibm/ibm-optim.md) | [De-identification](../../capabilities/governance/deidentification.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Microsoft Presidio](../open-source/presidio.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tonic Structural](../independent/tonic-structural.md), [Perforce Delphix](../independent/perforce-delphix.md), [Tonic Textual](../independent/tonic-textual.md) | [De-identification](../../capabilities/governance/deidentification.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
