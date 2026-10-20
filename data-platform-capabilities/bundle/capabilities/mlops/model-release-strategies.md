---
type: Capability
id: model-release-strategies
title: Model release strategies
description: Reduce release risk by exposing new models, prompts or agent versions gradually, or running them in parallel with the current version.
broader: [mlops, generative-ai]
related: [model-evaluation, environment-promotion, model-registry, model-performance-monitoring]
depends_on: [model-deployment, inference-logging]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Instead of switching all traffic to a new version at once, a release proceeds in stages. The new version may first run in parallel without effect (shadow), then take a small share of traffic (canary), or compete with the current version on a split of traffic (A/B or champion-challenger). Each stage has exit criteria, such as no rise in errors and quality at least as good as before, and a defined way back. Generative AI changes are released the same way: a new model version, prompt, retrieval setting or agent runs in shadow on live questions, is scored by online evaluators, then serves a growing share of users.

Offline evaluation cannot fully predict live behaviour. Shadow is safe but measures only what can be judged without acting; traffic splits measure real outcomes but expose some users to the new version. For generative AI, quality comes from evaluators and user feedback rather than ground truth, and agents in shadow need their tool calls stubbed so they take no actions.

# Key considerations

- Set promotion and rollback criteria before the release starts, including how long to wait and how much data is enough.
- Traffic splitting needs routing in the serving layer and logs recording which version served each request.
- If outcomes take weeks, a canary cannot judge quality quickly. Combine shadow comparison with service metrics.
- Running two models doubles serving cost while the comparison lasts. Give every comparison an end date.

# Questions to ask

- What would it cost if a worse model reached all users for a day?
- How soon after a prediction is the true outcome known?
- Can the serving layer split traffic and record which version handled each request?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [ML operations](mlops.md), [Generative AI](../generative-ai/generative-ai.md) |
| Narrower | [Canary and A/B testing](canary-ab-testing.md), [Champion-challenger](champion-challenger.md), [Shadow deployment](shadow-deployment.md) |
| Related | [Edge inference](edge-inference.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Model evaluation](../machine-learning/model-evaluation.md), [Model performance monitoring](model-performance-monitoring.md), [Model registry](../machine-learning/model-registry.md) |
| Depends on | [Model deployment](model-deployment.md), [Inference logging](inference-logging.md) |

# Where it appears

- **Use cases:** [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 4, Measured) · [MLOps](../../maturity/track-mlops.md) (from level 4, Measured)
- **Frameworks:** [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MANAGE 2 – Maximising benefit and minimising harm

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 11 technologies; see their pages.
