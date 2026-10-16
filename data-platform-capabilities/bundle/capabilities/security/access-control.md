---
type: Capability
id: access-control
title: Access control
description: Decide who can see and change which data, at every level from account down to individual values.
aliases: [authorisation, permissions, entitlements, least privilege, fine-grained access control]
broader: [security]
related:
- data-policy-management
- data-classification
- identity-authentication
- audit-logging
- table-catalogue
depends_on: [identity-authentication]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Access control decides, for every request, whether an identity may perform an action on an object. Platforms check permissions at several levels: account and workspace, catalogue and schema, table and view, and within a table by row and column. For example, an analyst may query the `sales` schema, see only rows for her region and see customer emails masked. Permissions come from role grants, from attribute- and tag-based policies, and from filters and masks attached to tables, and the engine or catalogue evaluates them at query time.

The aim is to give each person only what they need without making access so slow that people copy data elsewhere. Role-based grants are simple and supported everywhere; attribute-based policies scale better across many datasets and user groups. Row and column controls let one table serve many audiences instead of maintaining filtered copies. Where enforcement lives matters: controls defined in one engine do not protect the same files when another engine reads them straight from storage.

# Key considerations

- Define permissions once in a shared catalogue or policy layer that every engine uses, and block direct storage access that bypasses it.
- Grant to groups, not individuals, and keep grants in code so they can be reviewed and reproduced.
- Apply least privilege to administrative and service roles too. They often hold far wider access than any analyst.
- Check how row and column controls behave in caches, materialised views, extracts, exports and shared data, where they are easily lost.
- Review access periodically and remove unused grants, using usage metadata to see which are actually exercised.

# Questions to ask

- Who needs access to which data, and how often does that change?
- How many engines and tools read the same data, and do they all enforce the same permissions?
- How long does it take to get access today, and do people work around delays by copying data?
- When were privileged and service accounts last reviewed?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Narrower | [Access requests and reviews](access-requests.md), [Agent identity and authorisation](../generative-ai/agent-identity.md), [Attribute- and tag-based access control](attribute-based-access.md), [Column security and dynamic masking](column-masking.md), [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md), [Privileged access management](privileged-access.md), [Role-based access control](role-based-access.md), [Row-level security](row-level-security.md), [Storage credential vending](../storage/credential-vending.md) |
| Related | [Serving and activation](../serving/serving.md), [Governance and compliance](../governance/governance.md), [Audit logging](audit-logging.md), [Data APIs](../serving/data-apis.md), [Data classification](../governance/data-classification.md), [File-system access to object storage](../storage/object-file-access.md), [Identity and authentication](identity-authentication.md), [Policy management](../governance/data-policy-management.md), [Privacy management](../governance/privacy-management.md), [Table catalogue](../storage/table-catalogue.md) |
| Depends on | [Identity and authentication](identity-authentication.md) |
| Needed by | [Generative AI](../generative-ai/generative-ai.md), [Data sharing and collaboration](../data-sharing/data-sharing.md), [Agent tool and data access](../generative-ai/agent-tool-access.md), [Analytical sandboxes](../analytics-bi/analytical-sandboxes.md), [Data application hosting](../development-lifecycle/data-applications.md), [External data sharing](../data-sharing/external-data-sharing.md), [Internal data sharing](../data-sharing/internal-data-sharing.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Policy management](../governance/data-policy-management.md), [Shared compute isolation](compute-user-isolation.md) |

# Where it appears

- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Data platform engineer](../../personas/persona-platform-engineer.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Security · [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve platform – infrastructure provisioning plane · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 9 – Protection and prevention · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 4a – Special categories of personal data for bias detection · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(f) – Integrity and confidentiality; Article 32 – Security of processing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3](../../technologies/aws/aws-s3.md), [AWS Lake Formation](../../technologies/aws/aws-lake-formation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [OneLake security](../../technologies/microsoft/fabric-onelake-security.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Apache Ranger (SDX) |  |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Gravitino](../../technologies/open-source/apache-gravitino.md), [Apache Ranger](../../technologies/open-source/apache-ranger.md), [Unity Catalog (open source)](../../technologies/open-source/unity-catalog.md) |

Narrower capabilities are realised by a further 76 technologies; see their pages.
