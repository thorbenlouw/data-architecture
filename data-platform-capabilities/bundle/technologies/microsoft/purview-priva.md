---
type: Technology
id: purview-priva
title: Microsoft Priva
description: Privacy tooling that finds personal data, flags privacy risks such as overexposure and transfers, and manages subject rights requests.
platform: platform-microsoft
kind: saas
availability: ga
realises: [privacy-management, data-subject-requests, privacy-impact-assessment]
resource: https://learn.microsoft.com/en-us/privacy/priva/priva-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Strongest for Microsoft 365 content; analytical stores registered in Purview are covered more thinly.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Privacy management](../../capabilities/governance/privacy-management.md) (Governance and compliance) (primary): Meet privacy obligations such as purpose limitation, consent and individuals' rights over their data.
- [Data subject requests](../../capabilities/governance/data-subject-requests.md) (Governance and compliance): Find, export or erase a person's data across the platform when they ask.
- [Privacy impact assessment](../../capabilities/governance/privacy-impact-assessment.md) (Governance and compliance): Trigger, carry out and record data protection impact assessments for high-risk processing, linked to the data and pipelines concerned.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Privacy management](../../capabilities/governance/privacy-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [OneTrust Privacy Automation](../independent/onetrust-privacy-automation.md) | [Data subject requests](../../capabilities/governance/data-subject-requests.md), [Privacy impact assessment](../../capabilities/governance/privacy-impact-assessment.md), [Privacy management](../../capabilities/governance/privacy-management.md) |
