---
type: Technology
id: apicurio-registry
title: Apicurio Registry
description: Schema and API registry that stores and versions Avro, Protobuf, JSON Schema, OpenAPI and AsyncAPI artefacts and checks compatibility rules.
aliases: [Apicurio]
platform: platform-open-source
kind: open-source
availability: ga
realises: [schema-registry, event-api-catalogue]
resource: https://www.apicur.io/registry/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, Red Hat-led. Provides a Confluent-compatible API, so Kafka clients and serialisers can use it in place of Confluent Schema Registry, which is not open source.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Schema registry](../../capabilities/metadata/schema-registry.md) (Metadata and discovery) (primary): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
- [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) (Metadata and discovery): List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Schema Registry](../aws/aws-glue-schema-registry.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Schema Registry in Event Hubs](../microsoft/azure-event-hubs-schema-registry.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md), [Schema registry](../../capabilities/metadata/schema-registry.md) |
