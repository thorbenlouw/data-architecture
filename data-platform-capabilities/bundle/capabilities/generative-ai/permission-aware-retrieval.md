---
type: Capability
id: permission-aware-retrieval
title: Permission-aware retrieval
description: Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.
aliases: [ACL-aware retrieval, document-level security]
broader: [retrieval-augmented-generation, access-control]
related: [row-level-security, attribute-based-access, agent-identity, data-classification]
depends_on: [identity-authentication, retrieval-pipelines]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When content is indexed, the access list of each source document, meaning the users and groups allowed to open it, is stored with its chunks. At query time the system resolves the user's identity and group memberships and searches only chunks that user may see, before anything reaches the model. For example, two employees ask an assistant the same question about a reorganisation; only the one in the HR group gets the confidential plan included in the retrieved context.

Without it, anything indexed becomes visible to anyone who can use the assistant. There are three main approaches. Copying access lists into the index and filtering there is fast but can lag behind changes. Checking with the source system at query time is accurate but slower. Querying sources directly with the user's delegated credentials avoids a central index altogether. Expanding nested groups and mapping identities across systems are usually the hardest parts. Row-level security protects tables inside the platform; this capability protects content copied out of other systems into an index.

# Key considerations

- Revoked access in the source must take effect in the index quickly. Agree an acceptable delay and measure it.
- Filter before or during the search. Removing content after the model has read it can still leak information in the answer.
- Sources model permissions differently, with sharing links, inherited folders and external guests. Mapping them to one model loses detail, so check the edge cases.
- Caches, agent memory and conversation history can carry content across users unless they are scoped to the user.
- Include tests with users of different access levels in every release.

# Questions to ask

- Which sources have access rules that must be respected, and can their access lists be read?
- How quickly must a revoked permission take effect in AI answers?
- Is there one identity provider that maps users consistently across all sources?
- Will the assistant ever answer for people outside the organisation?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Retrieval-augmented generation](retrieval-augmented-generation.md), [Access control](../security/access-control.md) |
| Related | [Agent identity and authorisation](agent-identity.md), [Agent memory](agent-memory.md), [Attribute- and tag-based access control](../security/attribute-based-access.md), [Data classification](../governance/data-classification.md), [Full-text search](../specialised-data/full-text-search.md), [Row-level security](../security/row-level-security.md), [Unstructured data ingestion](../ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../specialised-data/unstructured-data.md) |
| Depends on | [Identity and authentication](../security/identity-authentication.md), [Retrieval pipelines](retrieval-pipelines.md) |
| Needed by | [Enterprise AI assistant](enterprise-ai-assistant.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 3, Defined) · [Security and access control](../../maturity/track-security.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock Knowledge Bases](../../technologies/aws/aws-bedrock-knowledge-bases.md), [Amazon Quick](../../technologies/aws/aws-quick.md), [Amazon Kendra](../../technologies/aws/aws-kendra.md) (deprecated), [Amazon Q Business](../../technologies/aws/aws-q-business.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure AI Search](../../technologies/microsoft/azure-ai-search.md), [Foundry IQ](../../technologies/microsoft/azure-foundry-iq.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Gemini Enterprise](../../technologies/google-cloud/gcp-gemini-enterprise.md), [Google Cloud Agent Search](../../technologies/google-cloud/gcp-agent-search.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Chatbot Studio](../../technologies/palantir/palantir-aip-chatbot-studio.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Elastic Cloud](../../technologies/independent/elastic-cloud.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md) |
