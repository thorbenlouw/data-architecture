---
type: Technology
id: azure-api-management
title: Azure API Management
description: An API gateway for publishing, securing and rate-limiting APIs, including AI gateway policies for model token limits, load balancing and logging.
aliases: [APIM]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [ai-gateway, data-apis, application-integration, ai-spend-controls, event-api-catalogue]
resource: https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Foundry AI Gateway (preview) is built on API Management. Can also expose MCP servers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI) (primary): Route, secure, rate-limit and track model calls across providers from one place.
- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.
- [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) (Metadata and discovery): List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Apigee](../google-cloud/gcp-apigee.md), [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Data APIs](../../capabilities/serving/data-apis.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica API Center](../informatica/informatica-api-center.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Data APIs](../../capabilities/serving/data-apis.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku LLM Mesh](../dataiku/dataiku-llm-mesh.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LiteLLM](../open-source/litellm.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Kong Konnect](../independent/kong-konnect.md), [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [LangSmith](../independent/langsmith.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
