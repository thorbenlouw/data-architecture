---
type: Capability
id: resilience-testing
title: Resilience and recovery testing
description: Test backup, recovery and failover regularly and record the results as evidence.
aliases: [DR testing, operational resilience testing]
broader: [business-continuity]
related: [compliance-evidence, infrastructure-as-code, platform-observability, data-reconciliation]
depends_on: [backup-restore]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tests range from restoring a sample table from backup each month, through rebuilding a whole environment from code in an empty account, to a full exercise in which production runs from the secondary region for a day. Each test records what was done, how long recovery took, how much data was lost compared with the RPO and RTO, what went wrong and what was fixed. Chaos engineering adds deliberate faults, such as stopping workers or blocking a dependency, to see how pipelines behave.

Recovery that has never been tested often fails: backups turn out incomplete, runbooks are out of date or permissions are missing in the secondary region. Regular tests find these gaps while there is time to fix them. Operational resilience rules in financial services, such as the EU Digital Operational Resilience Act and UK operational resilience requirements, expect firms to test recovery of important services and keep evidence. Automated tests are cheaper to repeat and produce consistent records that auditors can review.

# Key considerations

- Start with frequent small tests, such as automated table restores, before attempting full failover exercises.
- Test with realistic volumes. Restoring a small sample says little about how long the largest datasets take.
- Include people and process: who is contacted, who decides, and whether runbooks match the current platform.
- Keep the evidence, including timings, gaps found and fixes made, in a form auditors and risk teams can use.

# Questions to ask

- When were backup restore and regional failover last tested, and what did the tests find?
- Which regulators or customers expect evidence of recovery testing, and how often?
- Can recovery tests run without disrupting production?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Backup and disaster recovery](business-continuity.md) |
| Related | [Compliance controls and evidence](../governance/compliance-evidence.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Infrastructure as code](infrastructure-as-code.md), [Platform observability](platform-observability.md) |
| Depends on | [Backup and restore](backup-restore.md) |

# Where it appears

- **Use cases:** [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (benefits from)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Resilience and recovery](../../maturity/track-resilience.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 10 – Frequency · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Articles 11 and 12 – Response and recovery; backup, restoration and recovery; Chapter IV – Digital operational resilience testing (Articles 24 to 27) · [GDPR](../../frameworks/framework-gdpr.md): Article 32 – Security of processing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Backup](../../technologies/aws/aws-backup.md) |
