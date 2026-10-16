---
type: Technology
id: aws-glue-schema-registry
title: AWS Glue Schema Registry
description: Registry of versioned Avro, JSON Schema and Protobuf schemas that Kafka, Kinesis and Flink clients use to serialise data and check compatibility.
platform: platform-aws
kind: feature
availability: ga
realises: [schema-registry]
resource: https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Free to use; works with MSK, self-managed Kafka, Kinesis Data Streams and Managed Service for Apache Flink through serialiser libraries. Not wire-compatible with Confluent Schema Registry.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Schema registry](../../capabilities/metadata/schema-registry.md) (Metadata and discovery) (primary): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** AWS Glue

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Schema Registry in Event Hubs](../microsoft/azure-event-hubs-schema-registry.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Platform](../ibm/confluent-platform.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apicurio Registry](../open-source/apicurio-registry.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
