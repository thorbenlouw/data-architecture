---
type: Capability
id: metadata-harvesting
title: Metadata harvesting
description: Collect technical metadata automatically from databases, pipelines, BI tools and files.
aliases: [scanners, crawlers, connectors]
broader: [data-catalogue]
related: [table-catalogue, data-profiling, metadata-interoperability, table-lineage, system-telemetry]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Connectors, sometimes called scanners or crawlers, read the system tables and APIs of source tools: database information schemas, table catalogues, pipeline definitions, BI tool APIs and file headers. They load what they find into the catalogue, including schemas, types, locations, owners, row counts and query history. For example, a nightly scan of a warehouse picks up a new column in the customers table and updates its catalogue page, while a BI connector links each dashboard to the tables it queries.

Without harvesting, the catalogue depends on manual entry and drifts from reality. It works in two ways. Pull connectors scan on a schedule; push integrations have tools send events when something changes, for example OpenLineage events from jobs or webhooks from a catalogue, which keeps metadata fresher. Harvesting often also profiles sample data, gathers query logs for usage metadata and extracts lineage. It collects technical facts; business meaning still comes from glossaries and people.

# Key considerations

- Connector depth varies widely. For each source, check which objects and fields are captured, not just that a connector exists.
- Scanners need credentials. Keep them to metadata read access, and allow reading data values only where profiling is intended.
- Large estates produce huge numbers of objects. Filter out temporary and staging objects so the catalogue stays usable.
- Event-based capture gives near real-time updates but needs each tool to emit events.

# Questions to ask

- Which sources must be scanned, and does a connector exist for each?
- How soon after a change must the catalogue reflect it?
- May the harvester read sample data, or only metadata?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data catalogue](data-catalogue.md) |
| Related | [Data profiling](../data-quality/data-profiling.md), [Metadata interoperability](metadata-interoperability.md), [Table catalogue](../storage/table-catalogue.md), [Table-level lineage](table-lineage.md), [Usage and system telemetry](../platform-operations/system-telemetry.md) |
| Needed by | [AI-generated documentation](ai-generated-documentation.md), [Column-level lineage](column-lineage.md), [Data classification](../governance/data-classification.md), [Data lineage](data-lineage.md), [Data observability](../data-quality/data-observability.md), [Data security posture management](../security/data-security-posture.md), [End-to-end lineage](cross-system-lineage.md), [Table-level lineage](table-lineage.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 3) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 3)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md) · [Data lake](../../patterns/data-lake.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 5 Cataloguing (Cataloguing and classification) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Metadata Management · [DCAM v3](../../frameworks/framework-edm-dcam.md): 4 Business Data Knowledge

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3 Metadata](../../technologies/aws/aws-s3-metadata.md), [AWS Glue Data Catalog](../../technologies/aws/aws-glue-data-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Data Map](../../technologies/microsoft/purview-data-map.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Knowledge Catalog automatic discovery and metadata import | [Knowledge Catalog](../../technologies/google-cloud/gcp-knowledge-catalog.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Horizon Catalog](../../technologies/snowflake/snowflake-horizon-catalog.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Catalog Explorer](../../technologies/databricks/databricks-catalog-explorer.md) |
| [Informatica](../../platforms/platform-informatica.md) | catalog sources and scanners in Metadata Command Center | [Informatica Data 360 Connector and Scanner](../../technologies/informatica/informatica-data-360-connector-and-scanner.md), [Informatica Metadata Command Center (MCC)](../../technologies/informatica/informatica-metadata-command-center.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Lineage](../../technologies/cloudera/cloudera-data-lineage.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Catalog](../../technologies/oracle/oracle-oci-data-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Data Intelligence Cloud](../../technologies/sap/sap-data-intelligence-cloud.md) (deprecated) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Manta Data Lineage](../../technologies/ibm/ibm-manta-data-lineage.md), [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [SAS](../../platforms/platform-sas.md) | Discovery agents | [SAS Data Governance](../../technologies/sas/sas-data-governance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DataHub](../../technologies/open-source/datahub.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Catalog](../../technologies/independent/collibra-data-catalog.md) |
