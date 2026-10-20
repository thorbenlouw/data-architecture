---
type: Capability
id: data-applications
title: Data application hosting
description: Build and host interactive data applications next to the data, under platform security.
aliases: [data apps]
broader: [development-lifecycle, serving]
related: [container-services, data-writeback, embedded-analytics, notebooks, data-consumer-portal]
depends_on: [identity-authentication, access-control]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data applications are small interactive web apps, such as a pricing simulator, a data-entry form, a model explorer or an internal tool over a table. They are built with frameworks such as Streamlit, Dash or Gradio and hosted by the platform. The platform runs the app's code on its own compute, signs users in through the organisation's identity provider, and lets the app query data with either the viewer's permissions or a service identity. Users open a link; nothing is installed and no data is copied to a separate server.

Hosting next to the data avoids exporting it to a separate server that needs its own security review, credentials and infrastructure. It suits internal tools and prototypes that need input, custom logic or model calls that dashboards cannot provide. It is not a general application platform, so check scaling limits, uptime commitments and support for external users before building customer-facing products on it. Embedded analytics puts dashboards into other applications; this capability runs custom applications on the platform.

# Key considerations

- Decide whether apps query as the viewing user or as a shared service identity. The second is simpler but can show viewers data they should not see.
- Apps that write data need validation, audit trails and the same change control as pipelines.
- Version, review and promote apps through environments like other code rather than editing them in place.
- Check idle and scaling behaviour. Always-on app compute can cost more than an app's usage justifies.

# Questions to ask

- What do users need that dashboards cannot give them: input, workflow, simulation or model calls?
- Will apps be used only by staff, or also by customers and partners?
- Who will own and support each app after the person who built it moves on?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md), [Serving and activation](../serving/serving.md) |
| Related | [Container services](../compute/container-services.md), [Data application distribution](../data-sharing/application-sharing.md), [Data consumer portal](../analytics-bi/data-consumer-portal.md), [Data entry and write-back](../analytics-bi/data-writeback.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [Notebooks](notebooks.md), [Operational database integration](../serving/operational-database.md) |
| Depends on | [Identity and authentication](../security/identity-authentication.md), [Access control](../security/access-control.md) |

# Where it appears

- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Quick](../../technologies/aws/aws-quick.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric user data functions](../../technologies/microsoft/fabric-user-data-functions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Cloud Run](../../technologies/google-cloud/gcp-cloud-run.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Streamlit in Snowflake and Snowflake Native Apps | [Snowflake Native App Framework](../../technologies/snowflake/snowflake-native-app-framework.md), [Snowpark Container Services](../../technologies/snowflake/snowflake-snowpark-container-services.md), [Streamlit in Snowflake](../../technologies/snowflake/snowflake-streamlit.md) |
| [Databricks](../../platforms/platform-databricks.md) | Databricks Apps | [Databricks Apps](../../technologies/databricks/databricks-apps.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Applications (AI Workbench) | [Cloudera AI Workbench](../../technologies/cloudera/cloudera-ai-workbench.md) |
| [Palantir](../../platforms/platform-palantir.md) | Workshop | [Palantir Workshop](../../technologies/palantir/palantir-workshop.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Webapps and Dataiku Applications | [Dataiku webapps and Dataiku Applications](../../technologies/dataiku/dataiku-webapps.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [marimo](../../technologies/open-source/marimo.md), [Streamlit](../../technologies/open-source/streamlit.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Domo](../../technologies/independent/domo.md), [Hex](../../technologies/independent/hex.md), [Sigma Computing](../../technologies/independent/sigma.md), [Sisense](../../technologies/independent/sisense.md) |
