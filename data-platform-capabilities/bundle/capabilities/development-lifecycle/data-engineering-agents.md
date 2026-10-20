---
type: Capability
id: data-engineering-agents
title: Data engineering agents
description: Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.
aliases: [agentic data engineering]
broader: [ai-assisted-development, ai-agents]
related: [agent-identity, human-oversight, data-testing, ai-spend-controls, ci-cd]
depends_on: [foundation-model-access, agent-tool-access, version-control]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An agent is given a goal, such as "ingest this API daily into the sales schema" or "find out why yesterday's revenue job failed and fix it", and works through the steps itself. It reads catalogue metadata and existing code, writes or edits pipelines, runs them in a development environment, inspects errors and test results, and tries again. It then opens a pull request or asks a person for approval. Agents call platform tools through APIs or protocols such as MCP, and run under an identity whose permissions limit what they can touch.

Agents can take on repetitive engineering: standard ingestion, tests and documentation, library upgrades, SQL migration and failure triage. The architectural questions are control and accountability. An agent that can deploy or change data needs guard rails at least as tight as a new engineer's: least-privilege access, development environments by default, mandatory review and a record of what it did and why. Unlike an assistant, it acts over many steps without waiting for each prompt.

# Key considerations

- Run agents in development environments and require human approval for promotion. Do not give them standing write access to production.
- Give each agent its own identity so its actions can be told apart in audit logs from those of the person who started it.
- Agents need fast, safe feedback from tests, data comparisons and clones. Without it they produce plausible changes that nobody can verify quickly.
- Budget for model and compute use. An agent retrying a failing job in a loop can run up costs quickly.

# Questions to ask

- Which engineering tasks are repetitive and well tested enough to hand to an agent?
- What, if anything, may an agent change without a person reviewing it?
- Can you reconstruct afterwards what an agent did, with which data and permissions?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [AI-assisted development](ai-assisted-development.md), [AI agents](../generative-ai/ai-agents.md) |
| Related | [Agent identity and authorisation](../generative-ai/agent-identity.md), [AI usage and spend controls](../platform-operations/ai-spend-controls.md), [CI/CD](ci-cd.md), [Data pipeline testing](data-testing.md), [Human oversight of AI](../governance/human-oversight.md) |
| Depends on | [Foundation model access](../generative-ai/foundation-model-access.md), [Agent tool and data access](../generative-ai/agent-tool-access.md), [Version control integration](version-control.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 5, Optimising) · [Path to live](../../maturity/track-path-to-live.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Data Agent](../../technologies/aws/aws-sagemaker-data-agent.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Data Engineering Agent](../../technologies/google-cloud/gcp-bigquery-data-engineering-agent.md), [Colab Enterprise](../../technologies/google-cloud/gcp-colab-enterprise.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake CoCo](../../technologies/snowflake/snowflake-coco.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Genie Code](../../technologies/databricks/databricks-genie-code.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [CLAIRE Agents](../../technologies/informatica/informatica-claire-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Anywhere Cloud](../../technologies/cloudera/cloudera-anywhere-cloud.md) (unconfirmed) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Tera](../../technologies/teradata/teradata-tera.md) (preview) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data integration](../../technologies/ibm/ibm-watsonx-data-integration.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Cobuild | [Dataiku Cobuild](../../technologies/dataiku/dataiku-cobuild.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Astronomer Astro](../../technologies/independent/astronomer-astro.md), [dbt Copilot](../../technologies/independent/dbt-copilot.md), [Matillion Maia](../../technologies/independent/matillion-maia.md) |
