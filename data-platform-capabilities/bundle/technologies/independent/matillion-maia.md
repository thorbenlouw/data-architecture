---
type: Technology
id: matillion-maia
title: Matillion Maia
description: Team of AI agents that plans, builds, tests, deploys and repairs Matillion pipelines from natural-language requests, with human review before execution.
aliases: [Maia]
platform: platform-independent
vendor: Matillion
kind: saas
availability: ga
realises: [data-engineering-agents, human-oversight]
resource: https://www.matillion.com/news/matillion-unveils-agentic-data-team-maia
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Launched by invitation in June 2025. It includes Maia Team (the agents), Context Engine (which applies house standards and business rules) and Mission Control (where people review plans). It runs on top of [Matillion Maia Foundation](../independent/matillion-maia-foundation.md) and does not replace it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps) (primary): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.
- [Human oversight of AI](../../capabilities/governance/human-oversight.md) (Governance and compliance): Route model and agent decisions to people for review, approval or override, and let them pause or stop a system.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

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
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
