---
type: Capability
id: data-quality-rules
title: Data quality rules
description: Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
aliases: [expectations, validation rules, DQ checks]
broader: [data-quality]
related: [data-contracts, data-testing, bad-data-quarantine, critical-data-elements, transformation-as-code]
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Typical rules: order ID is never null and is unique; order date is not in the future; every order's customer ID exists in the customer table; line amounts add up to the order total. Rules are written in SQL, a declarative configuration file or a rules interface. Each has a severity and an action on failure, and runs at a set point in a pipeline, on a schedule or on each new batch, with results stored for reporting.

Rules capture known requirements, so they suit business logic, regulatory checks and conditions consumers depend on. They are usually grouped by quality dimension: completeness, validity, uniqueness, consistency, accuracy and timeliness. Approaches range from tests in transformation code to standalone rule engines and open-source check libraries such as Great Expectations and Soda Core. Rules complement learned anomaly detection, which catches problems nobody anticipated but cannot express business requirements.

# Key considerations

- Give every rule an owner and an action on failure. Rules that only log results are soon ignored.
- Run rules close to where data enters or changes, and before publishing, so bad data does not reach consumers.
- Keep rules in version control with the pipelines they test, and review them as part of each change.
- Large rule sets cost compute on every run. Prioritise critical fields and check only new data where possible.

# Questions to ask

- Which business rules must data meet before it is used?
- Who writes rules: engineers in code, or business stewards through an interface?
- What should happen when a rule fails: stop, quarantine or warn?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md) |
| Related | [Master and reference data](../master-data/master-data.md), [Bad-data quarantine](bad-data-quarantine.md), [Critical data elements](../governance/critical-data-elements.md), [Data anomaly detection](data-anomaly-detection.md), [Data branching and tagging](../storage/data-branching.md), [Data contracts](../data-products/data-contracts.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Data reconciliation](data-reconciliation.md), [Declarative pipelines](../processing/declarative-pipelines.md), [Feature engineering](../machine-learning/feature-engineering.md), [Merge and survivorship](../master-data/survivorship.md), [ML pipelines](../machine-learning/ml-pipelines.md), [Reference data management](../master-data/reference-data-management.md), [Transformation as code](../processing/transformation-as-code.md) |
| Needed by | [Bad-data quarantine](bad-data-quarantine.md), [Critical data elements](../governance/critical-data-elements.md), [Data quality scorecards](data-quality-scorecards.md), [Data trust indicators](../metadata/data-trust-indicators.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 2) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 3) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 3) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Patterns:** [Data warehouse](../../patterns/data-warehouse.md) · [Medallion architecture](../../patterns/medallion-architecture.md) · [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md) · [Shift-left data quality and governance](../../patterns/shift-left.md) · [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 3 – Accuracy and integrity; Principle 4 – Completeness; Principle 7 – Accuracy (reporting) · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 11 Data Quality Measurement (Data lifecycle) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Quality · [DCAM v3](../../frameworks/framework-edm-dcam.md): 5 Data Quality Management · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 10 – Data and data governance; Article 26 – Obligations of deployers · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(d) – Accuracy · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Data validation · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-8 – Concepts and measuring; ISO 8000-61 – Data quality management process reference model; ISO/TS 8000-82 – Creating data rules; ISO 8000-130 and 8000-140 – Accuracy and completeness; ISO/CD TR 8000-320 – AI training data quality (in development) · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.7 – Data for AI systems · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Data Quality

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | DQDL rulesets (Glue Data Quality) | [AWS Glue Data Quality](../../technologies/aws/aws-glue-data-quality.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric materialized lake views](../../technologies/microsoft/fabric-materialized-lake-views.md), [Microsoft Purview Data Quality](../../technologies/microsoft/purview-data-quality.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data quality](../../technologies/google-cloud/gcp-knowledge-catalog-data-quality.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | data metric functions (DMFs) with expectations | [Snowflake data quality monitoring (data metric functions)](../../technologies/snowflake/snowflake-data-quality-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | Expectations | [Lakeflow pipelines expectations](../../technologies/databricks/databricks-pipeline-expectations.md) |
| [Informatica](../../platforms/platform-informatica.md) | rule specifications | [CLAIRE Data Quality Agent](../../technologies/informatica/informatica-claire-data-quality-agent.md), [Informatica Cloud Data Quality (CDQ)](../../technologies/informatica/informatica-cloud-data-quality.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Master Data Governance](../../technologies/sap/sap-master-data-governance.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Data quality in IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence-quality.md) |
| [Palantir](../../platforms/platform-palantir.md) | Data expectations | [Palantir Data Health and data expectations](../../technologies/palantir/palantir-data-health.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Dagster](../../technologies/open-source/dagster.md), [GX Core (Great Expectations)](../../technologies/open-source/great-expectations.md), [OpenMetadata](../../technologies/open-source/openmetadata.md), [Soda Core](../../technologies/open-source/soda-core.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Anomalo](../../technologies/independent/anomalo.md), [Ataccama ONE](../../technologies/independent/ataccama-one.md), [Collibra Data Quality & Observability](../../technologies/independent/collibra-data-quality-observability.md), [Experian Aperture Data Studio](../../technologies/independent/experian-aperture-data-studio.md), [GX Cloud](../../technologies/independent/gx-cloud.md), [Precisely Data Integrity Suite](../../technologies/independent/precisely-data-integrity-suite.md), [Semarchy Data Platform](../../technologies/independent/semarchy-data-platform.md), [Soda Cloud](../../technologies/independent/soda-cloud.md), [Stibo Systems STEP](../../technologies/independent/stibo-systems-step.md), [Syndigo MDM](../../technologies/independent/syndigo-mdm.md) |
