---
type: Technology
id: azure-event-hubs-schema-registry
title: Azure Schema Registry in Event Hubs
description: Stores and versions Avro and JSON schemas for event producers and consumers with compatibility checks.
platform: platform-microsoft
kind: feature
availability: ga
realises: [schema-registry]
resource: https://learn.microsoft.com/en-us/azure/event-hubs/schema-registry-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Schema registry](../../capabilities/metadata/schema-registry.md) (Metadata and discovery) (primary): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Schema Registry](../aws/aws-glue-schema-registry.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Platform](../ibm/confluent-platform.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apicurio Registry](../open-source/apicurio-registry.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
