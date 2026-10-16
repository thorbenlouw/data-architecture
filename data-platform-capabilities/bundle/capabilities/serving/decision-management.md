---
type: Capability
id: decision-management
title: Decision management
description: Combine business rules, model scores and policies into automated decisions that are consistent, explainable and audited.
aliases: [business rules engine, decisioning]
broader: [serving]
related:
- real-time-inference
- model-explainability
- human-oversight
- champion-challenger
- online-feature-store
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A decision service receives a request such as a loan application, gathers the data it needs, runs model scores and business rules, and returns an outcome with reasons. For a loan, a rule first excludes applicants under 18, a credit model produces a risk score, a policy table maps score bands to approve, refer or decline, and a final rule caps the limit by income. Rules and tables are versioned artefacts, often decision tables or models in a standard such as DMN, so analysts can change a threshold without a software release.

It suits decisions taken at volume that must be consistent, explainable to customers and regulators, and quick to change, as in credit, fraud, claims, pricing and eligibility. Each decision is logged with its inputs, versions and reasons so it can be reconstructed later. A model only predicts; decision management decides what to do with the prediction, and supports simulating rule changes against past cases and testing alternative strategies.

# Key considerations

- Keep rules, thresholds and models as separate versioned components so each can be changed and tested without redeploying the others.
- Log enough to replay a decision exactly: the input data as it was at the time, every rule and model version, and the reasons returned.
- Let business users change rules only through a controlled path with tests, simulation against past cases and approval. Direct edits in production cause incidents that are hard to trace.
- Decide which outcomes go to a person for review, and capture their overrides as data for improving rules and models.
- Data protection law can give people the right to an explanation of, or human review of, an automated decision about them. Design reason codes in from the start.

# Questions to ask

- Which decisions are made at volume today, and where do the rules live: in code, spreadsheets or people's heads?
- How quickly must the business be able to change a threshold or policy?
- What must be shown to a customer, auditor or regulator who asks why a decision was made?
- Are decisions needed in real time, in batch, or both?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Related | [Champion-challenger](../mlops/champion-challenger.md), [Human oversight of AI](../governance/human-oversight.md), [Model explainability](../machine-learning/model-explainability.md), [Online feature store](../machine-learning/online-feature-store.md), [Real-time inference](../mlops/real-time-inference.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 4, Measured)
- **Frameworks:** [GDPR](../../frameworks/framework-gdpr.md): Article 22 – Automated individual decision-making

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [Hightouch](../../technologies/independent/hightouch.md) |
