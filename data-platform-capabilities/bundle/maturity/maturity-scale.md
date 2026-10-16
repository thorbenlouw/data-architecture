---
type: Reference
id: maturity-scale
title: Maturity scale
description: The five maturity levels used by every maturity track and every use case requirement in the bundle.
order: 4
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

All maturity tracks use the same five levels, based on the familiar capability maturity model. Use cases use the same numbers for the minimum level they need in each capability.

| Level | Name | What it looks like |
|---|---|---|
| 1 | Initial | Done ad hoc by individuals. Manual, undocumented, hard to repeat. Success depends on who is around. |
| 2 | Managed | Repeatable within a team. Basic tooling and documentation exist, but each team does it its own way. |
| 3 | Defined | Standardised across the platform. A shared, documented, self-service way of doing it that most teams use. |
| 4 | Measured | Automated and monitored against explicit targets. Problems are detected by the platform, not by consumers. |
| 5 | Optimising | Continuously improved from the measurements, often predictive or self-tuning. |

# How to assess

- Assess against each track's **criteria**, which are written to be observable (you can check the platform, its configuration or its processes), not against the level names.
- An area is at the highest level whose criteria are mostly met **and** all lower levels are met. Note the gaps rather than averaging them away.
- Assess per domain or business area if practice varies. A single platform-wide score hides the teams that need help.
- Higher is not always better. Match the level to what the use cases need: most use cases need level 2 or 3, and the *Minimum level* column in each use case says which.

# Relationship to other models

The scale lines up with the five-level models in DCAM, CMMI and Microsoft's MLOps maturity model, and with Google's three MLOps levels at levels 1, 3 and 4. The MLOps track explains the mapping in detail.
