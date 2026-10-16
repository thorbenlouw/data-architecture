---
type: Capability
id: data-security-posture
title: Data security posture management
description: Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
aliases: [DSPM]
broader: [security]
related:
- data-classification
- governance-metrics
- ai-system-discovery
- usage-metadata
- data-threat-detection
depends_on: [data-classification, metadata-harvesting]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data security posture management (DSPM) scans the data estate continuously to answer three questions: where sensitive data is, who and what can reach it, and which configurations put it at risk. It discovers data stores, including unregistered ones, samples their contents to classify them, works out effective access from identities, roles, shares and public links, and flags problems. For example, it might find a copy of a customer table in a forgotten storage bucket readable by every employee, or a service account with write access to finance data it never uses.

Platforms and cloud accounts change faster than manual reviews can follow, and sensitive data spreads through copies, exports and test environments. DSPM gives security teams a current view of exposure and a way to track fixes. It uses classification, and overlaps with cloud security posture management, which checks infrastructure settings without knowing what data they protect. Threat detection differs: posture concerns what could happen given the set-up, threat detection what people are actually doing.

# Key considerations

- Scope discovery beyond the main platform to storage accounts, databases, SaaS tools and file shares where copies end up.
- Effective access means resolving nested groups, roles, shares and storage-level permissions. Check how completely a tool computes it.
- Prioritise findings by sensitivity, exposure and usage, or teams drown in alerts.
- Feed findings into ownership and ticketing so each one reaches someone who can fix it.

# Questions to ask

- Do you know every location holding copies of sensitive data, including outside the main platform?
- Can you say who can effectively reach a given sensitive table, including through groups and shares?
- How are misconfigurations found today, and how long do they stay open?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Related | [AI system discovery](../governance/ai-system-discovery.md), [Data breach response](data-breach-response.md), [Data classification](../governance/data-classification.md), [Data threat detection](data-threat-detection.md), [Enterprise AI assistant](../generative-ai/enterprise-ai-assistant.md), [Governance coverage metrics](../governance/governance-metrics.md), [Resource configuration guardrails](../platform-operations/configuration-guardrails.md), [Usage and popularity metadata](../metadata/usage-metadata.md) |
| Depends on | [Data classification](../governance/data-classification.md), [Metadata harvesting](../metadata/metadata-harvesting.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (benefits from) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 3)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 4, Measured)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 1 Data Control Compliance (Governance and accountability); 7 Entitlements and Access for Sensitive Data (Accessibility and usage) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Security · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter II – ICT risk management (Articles 5 to 16); Article 8 – Identification; Article 10 – Detection; Chapter IV – Digital operational resilience testing (Articles 24 to 27) · [GDPR](../../frameworks/framework-gdpr.md): Articles 33 and 34 – Personal data breach notification

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Macie](../../technologies/aws/aws-macie.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | DSPM | [Data security posture management in Microsoft Defender for Cloud](../../technologies/microsoft/azure-defender-for-cloud-dspm.md), [Microsoft Purview Data Security Posture Management](../../technologies/microsoft/purview-dspm.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Sensitive Data Protection discovery; Security Command Center | [Google Cloud Security Command Center](../../technologies/google-cloud/gcp-security-command-center.md), [Google Cloud Sensitive Data Protection](../../technologies/google-cloud/gcp-sensitive-data-protection.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Trust Center | [Snowflake sensitive data classification](../../technologies/snowflake/snowflake-sensitive-data-classification.md), [Snowflake Trust Center](../../technologies/snowflake/snowflake-trust-center.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Data Classification](../../technologies/databricks/databricks-data-classification.md), [Databricks Governance Hub](../../technologies/databricks/databricks-governance-hub.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) | Data Safe security assessment | [Oracle Data Safe](../../technologies/oracle/oracle-data-safe.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Guardium Data Security Center](../../technologies/ibm/ibm-guardium-data-security-center.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [BigID Next](../../technologies/independent/bigid-next.md), [Cyera DSPM](../../technologies/independent/cyera-dspm.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md), [Varonis Data Security Platform](../../technologies/independent/varonis-data-security-platform.md) |
