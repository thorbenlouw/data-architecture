---
type: Technology
id: sas-intelligent-decisioning
title: SAS Intelligent Decisioning
description: Application in SAS Viya for building decision flows that combine business rules, model scores, code and calls to external APIs such as LLMs, then testing them and publishing them as batch, API or real-time services.
platform: platform-sas
kind: feature
availability: ga
realises: [decision-management, ai-agents]
resource: https://www.sas.com/en_us/software/intelligent-decisioning.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

SAS presents it as the base for agentic AI workflows, combining models, AI agents and deterministic rules in one governed flow. REST API definitions let a decision call external services such as LLMs, and the [SAS Agentic AI Accelerator](sas-agentic-ai-accelerator.md) adds a node for LLM calls. Decisions can start custom workflows that involve people, are versioned and audited, and run in [SAS Container Runtime](sas-container-runtime.md), the SAS Micro Analytic Service or [SAS Event Stream Processing](sas-event-stream-processing.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Decision management](../../capabilities/serving/decision-management.md) (Serving and activation) (primary): Combine business rules, model scores and policies into automated decisions that are consistent, explainable and audited.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hightouch](../independent/hightouch.md) | [Decision management](../../capabilities/serving/decision-management.md) |
