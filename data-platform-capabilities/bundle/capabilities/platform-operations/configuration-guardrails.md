---
type: Capability
id: configuration-guardrails
title: Resource configuration guardrails
description: Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules.
aliases:
- compute policies
- cluster policies
- organisation policies
- service control policies
- platform guardrails
- preventive controls
broader: [platform-operations]
related:
- infrastructure-as-code
- self-service-provisioning
- spend-controls
- data-security-posture
- compliance-evidence
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Guardrails are rules checked when someone creates or changes a resource, and again afterwards. A compute policy might allow three cluster sizes, require auto-termination after 30 minutes and force a cost-centre tag. An organisation policy might block storage outside approved regions, or any workspace without private networking. Preventive rules reject a request that breaks them. Detective rules scan existing resources and report or fix those that do not comply, which catches changes made outside templates and infrastructure code.

Templates set good defaults, but anyone with console or API access can still create something else. Guardrails make the rules hold whichever route was used, so security, cost and residency settings stay consistent across hundreds of workspaces. They sit at several levels: cloud organisation policies, data platform account and workspace policies, and checks on infrastructure plans in CI. Data policy management governs use of data; guardrails govern how the platform is configured. Posture management finds risky settings after the fact; guardrails stop many being created.

# Key considerations

- Set each rule at the highest level that can enforce it, such as the cloud organisation or platform account, so new workspaces inherit it automatically.
- Run new rules in audit mode and report violations before enforcing them, or a rule can block production deployments overnight.
- Provide an exception process with an owner and an expiry date. Permanent exceptions granted by hand become the next source of drift.
- Keep rules in version control and test them against sample requests, like any other code.

# Questions to ask

- Which settings must hold everywhere, such as regions, encryption, private networking and cost tags?
- Can anyone create compute or storage outside approved templates today, and how would you find out?
- Who may grant an exception to a rule, and for how long?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Related | [Budgets and spend controls](spend-controls.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Data security posture management](../security/data-security-posture.md), [Infrastructure as code](infrastructure-as-code.md), [Self-service provisioning](self-service-provisioning.md) |

# Where it appears

- **Use cases:** [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 2) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 4, Measured)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter II – ICT risk management (Articles 5 to 16); Article 9 – Protection and prevention

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Config](../../technologies/aws/aws-config.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Policy](../../technologies/microsoft/azure-policy.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Assured Workloads](../../technologies/google-cloud/gcp-assured-workloads.md), [Google Cloud Resource Manager](../../technologies/google-cloud/gcp-resource-manager.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks classic compute (Databricks Runtime clusters)](../../technologies/databricks/databricks-classic-compute.md), [Databricks compliance security profile](../../technologies/databricks/databricks-compliance-security-profile.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Open Policy Agent (OPA)](../../technologies/open-source/open-policy-agent.md) |
