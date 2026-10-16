---
type: Technology
id: kong-konnect
title: Kong Konnect
description: API platform whose AI Gateway governs and meters LLM traffic and whose Event Gateway applies policies to Kafka traffic, such as virtual clusters and access control.
aliases: [Kong AI Gateway, Kong Event Gateway]
platform: platform-independent
vendor: Kong
kind: saas
availability: ga
realises: [ai-gateway, agent-tool-access, agent-registry, ai-spend-controls, event-api-catalogue]
resource: https://konghq.com/products/kong-konnect
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Konnect is a broader API management platform. Its AI Gateway, Event Gateway, Dev Portal and Service Catalog are the parts that matter for data and AI platforms. The MCP Registry is a tech preview. The Event Gateway sits in front of existing Kafka clusters and does not replace them.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI) (primary): Route, secure, rate-limit and track model calls across providers from one place.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.
- [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) (Metadata and discovery): List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure API Management](../microsoft/azure-api-management.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md), [Apigee](../google-cloud/gcp-apigee.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md), [Databricks managed MCP servers](../databricks/databricks-managed-mcp-servers.md) (preview) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LiteLLM](../open-source/litellm.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
