---
type: Capability
id: secrets-management
title: Secrets management
description: Store and rotate the credentials and keys used by pipelines and tools without putting them in code.
broader: [security]
related: [identity-authentication, encryption, ci-cd, customer-managed-keys, credential-vending]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Pipelines, connectors and tools need credentials to reach sources and targets: database passwords, API keys, tokens and certificates. A secrets manager stores them encrypted, releases them at run time only to authorised identities, logs every read and rotates them on a schedule or after a suspected leak. Code refers to a secret by name, such as `crm/api_key`, and never contains the value. Some managers issue dynamic secrets, creating a short-lived database account for each job and removing it afterwards.

Credentials in code, notebooks, configuration files and environment variables are a frequent cause of breaches, because they spread through Git history, logs and copies. Central management limits who can see them and makes rotation possible without editing every pipeline. The better long-term step is to avoid stored secrets where possible, using workload identity federation so services authenticate with identities issued by their runtime, and to keep secrets management for systems that still need them, such as third-party APIs.

# Key considerations

- Scan repositories, notebooks and logs for leaked credentials, and block commits that contain them.
- Scope secrets to the identities and environments that need them, so a development job cannot read a production key.
- Automate rotation and test that pipelines pick up new values without failing.
- Watch for secrets printed in job logs or notebook output, and redact them automatically.

# Questions to ask

- Where are credentials for sources and targets kept today?
- When were the most sensitive credentials last rotated, and could you rotate them today without breaking pipelines?
- Which systems could use federated workload identity instead of stored secrets?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Related | [Agent identity and authorisation](../generative-ai/agent-identity.md), [AI gateway](../generative-ai/ai-gateway.md), [CI/CD](../development-lifecycle/ci-cd.md), [Cryptographic agility](cryptographic-agility.md), [Customer-managed keys](customer-managed-keys.md), [Encryption](encryption.md), [IDE and local development](../development-lifecycle/local-development.md), [Identity and authentication](identity-authentication.md), [Privileged access management](privileged-access.md), [Storage credential vending](../storage/credential-vending.md), [User-defined functions and procedures](../processing/user-defined-functions.md) |
| Needed by | [Ingestion and integration](../ingestion-integration/ingestion-integration.md), [Orchestration](../orchestration/orchestration.md), [API ingestion](../ingestion-integration/api-ingestion.md), [CI/CD](../development-lifecycle/ci-cd.md), [Custom connector development](../ingestion-integration/custom-connectors.md), [De-identification](../governance/deidentification.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [SaaS application connectors](../ingestion-integration/saas-connectors.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 2)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md) · [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 2, Managed)
- **Frameworks:** [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Variables · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Variables

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Secrets Manager](../../technologies/aws/aws-secrets-manager.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Key Vault](../../technologies/microsoft/azure-key-vault.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Secret Manager](../../technologies/google-cloud/gcp-secret-manager.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake secrets](../../technologies/snowflake/snowflake-secrets.md) |
| [Databricks](../../platforms/platform-databricks.md) | Secrets in Unity Catalog | [Secrets in Unity Catalog](../../technologies/databricks/databricks-secrets-in-unity-catalog.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenBao](../../technologies/open-source/openbao.md) |
