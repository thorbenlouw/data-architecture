---
type: Technology
id: gcp-bigquery-data-engineering-agent
title: BigQuery Data Engineering Agent
description: Gemini agent in BigQuery pipelines and Dataform that writes or changes pipeline code (SQLX) from natural-language requests and investigates failed runs.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [data-engineering-agents, agent-interoperability]
resource: https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA April 2026. It proposes changes for review but does not run pipelines, and it reads persistent rules from a GEMINI.MD file. It is also exposed through an Agent2Agent (A2A) API. Failed-run investigation is in preview. A companion Data Science Agent in Colab Enterprise went GA in May 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps) (primary): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.
- [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) (Generative AI): Let agents built on different platforms discover, delegate to and call each other through open protocols.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoCo](../snowflake/snowflake-coco.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Code](../databricks/databricks-genie-code.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Agents](../informatica/informatica-claire-agents.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Anywhere Cloud](../cloudera/cloudera-anywhere-cloud.md) (unconfirmed) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Agent2Agent (A2A) protocol](../open-source/agent2agent-protocol.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia](../independent/matillion-maia.md), [dbt Copilot](../independent/dbt-copilot.md), [Astronomer Astro](../independent/astronomer-astro.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
