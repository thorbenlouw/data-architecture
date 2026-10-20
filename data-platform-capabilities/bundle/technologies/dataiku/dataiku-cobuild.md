---
type: Technology
id: dataiku-cobuild
title: Dataiku Cobuild
description: Agent inside a Dataiku project that builds and edits Flows, recipes, models, knowledge banks, agents, dashboards, notebooks and scenarios from natural-language requests.
platform: platform-dataiku
kind: feature
availability: ga
realises: [data-engineering-agents]
resource: https://doc.dataiku.com/dss/latest/ai-assistants/cobuild.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Generally available since 18 June 2026. It asks for confirmation before key actions and produces ordinary, editable Flow objects; a Plan mode, added in version 15.1, lets users review the proposed tasks first. Runs as one of the Dataiku AI services, which also include SQL Assistant, AI Explain, Generate Metadata and AI Search.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps) (primary): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Data Engineering Agent](../google-cloud/gcp-bigquery-data-engineering-agent.md), [Colab Enterprise](../google-cloud/gcp-colab-enterprise.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoCo](../snowflake/snowflake-coco.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Code](../databricks/databricks-genie-code.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Agents](../informatica/informatica-claire-agents.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Anywhere Cloud](../cloudera/cloudera-anywhere-cloud.md) (unconfirmed) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia](../independent/matillion-maia.md), [dbt Copilot](../independent/dbt-copilot.md), [Astronomer Astro](../independent/astronomer-astro.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
