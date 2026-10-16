---
type: Capability
id: active-metadata
title: Active metadata
description: Use metadata to trigger actions automatically, such as propagating tags, alerting owners or blocking bad data.
broader: [metadata]
related:
- data-policy-management
- attribute-based-access
- data-observability
- event-driven-triggering
- data-certification
depends_on: [data-catalogue, metadata-interoperability]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Rules and events act on metadata as it changes, instead of waiting for someone to read it. When a column is classified as personal data, a masking policy is applied and the tag flows to derived columns through lineage. When a quality check fails, the certified badge is removed and owners of affected dashboards are alerted. When a table has gone unused for a year, an archiving ticket is opened. This needs a feed of metadata change events, a rules or workflow engine, and integrations with the tools that take the action.

It lets governance keep pace with a growing estate without proportional manual effort, and keeps metadata in step across systems. It appears as automation features in catalogues, as event streams of metadata changes consumed by custom services, and as policy engines that read tags at query time. The risk is acting on wrong metadata, for example masking a column that a critical report needs. Data observability detects problems in data; active metadata acts on metadata signals across tools.

# Key considerations

- Start with low-risk actions such as notifications and tag suggestions before automating access changes or blocking pipelines.
- Tag propagation needs rules for where it stops, for example after aggregation or anonymisation.
- Log every automated change and make it reversible.
- Check that the catalogue publishes change events. Without them, automation falls back to slow polling.

# Questions to ask

- Which governance tasks are repeated by hand today?
- Which tools would need to receive automated actions?
- Who signs off rules that can block pipelines or change access?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Metadata and discovery](metadata.md) |
| Related | [Attribute- and tag-based access control](../security/attribute-based-access.md), [Data certification](data-certification.md), [Data classification](../governance/data-classification.md), [Data issue management](../data-quality/data-issue-management.md), [Data observability](../data-quality/data-observability.md), [Event-driven triggering](../orchestration/event-driven-triggering.md), [Policy management](../governance/data-policy-management.md), [Stewardship workflows](../governance/stewardship-workflows.md) |
| Depends on | [Data catalogue](data-catalogue.md), [Metadata interoperability](metadata-interoperability.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (benefits from) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md) · [Shift-left data quality and governance](../../patterns/shift-left.md)
- **Personas:** [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 4, Measured)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 1 Data Control Compliance (Governance and accountability); 6 Classification (Cataloguing and classification); 10 Data Privacy Impact Assessments (Protection and privacy) · [Data mesh principles](../../frameworks/framework-data-mesh.md): Federated computational governance · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Management Ports

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | Knowledge Catalog metadata change feeds | [Knowledge Catalog](../../technologies/google-cloud/gcp-knowledge-catalog.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Horizon Context](../../technologies/snowflake/snowflake-horizon-context.md) (preview), [Snowflake object tagging](../../technologies/snowflake/snowflake-object-tagging.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks governed tags](../../technologies/databricks/databricks-governed-tags.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DataHub](../../technologies/open-source/datahub.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Atlan](../../technologies/independent/atlan.md) |
