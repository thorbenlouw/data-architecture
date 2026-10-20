---
type: Capability
id: synthetic-data
title: Synthetic data generation
description: Generate artificial data that keeps the useful properties of real data without exposing real records.
broader: [test-data-management]
related: [privacy-enhancing-technologies, deidentification, model-training, genai-evaluation, data-sharing]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Synthetic records come from a generator rather than from real events. Rule-based generators produce random values within ranges, pick from lists and respect constraints such as "end date after start date". Statistical and machine learning generators learn the distributions and correlations of a real dataset and sample new records from that model, so a synthetic customer table keeps realistic patterns of age, region and spending while no row describes a real person. Language models are also used to generate realistic text, such as support conversations.

Uses include development and testing where even masked data is too risky, sharing data with vendors or researchers, training models when real examples are scarce or imbalanced, and testing AI systems on rare cases. Synthetic data is not automatically anonymous. Learned generators can memorise and reproduce real outliers, so privacy should be measured, for example with distance-to-nearest-record tests or by training with differential privacy. Utility should be measured too, by checking that analyses on synthetic data give answers close to those on real data.

# Key considerations

- Measure privacy and utility for each release of synthetic data, not once. A generator retrained on new data can start leaking.
- Rule-based generators are predictable and cheap. Learned generators are more realistic but need access to real data for training and careful privacy controls.
- Multi-table data is harder than single tables. Check that relationships, time sequences and business rules hold across generated tables.
- Label synthetic datasets clearly in the catalogue so nobody mistakes them for real data in analysis or reporting.

# Questions to ask

- What will the synthetic data be used for: functional tests, performance tests, sharing or model training?
- Does the use need realistic statistical patterns, or only valid formats and edge cases?
- What evidence would your privacy team need before synthetic data leaves the controlled environment?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Test data management](test-data-management.md) |
| Related | [Data sharing and collaboration](../data-sharing/data-sharing.md), [Data labelling](../machine-learning/data-labelling.md), [De-identification](../governance/deidentification.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Model customisation](../generative-ai/model-customisation.md), [Model training](../machine-learning/model-training.md), [Privacy-enhancing technologies](../governance/privacy-enhancing-technologies.md) |

# Where it appears

- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake synthetic data generation](../../technologies/snowflake/snowflake-synthetic-data.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Test Data Management (TDM)](../../technologies/informatica/informatica-test-data-management.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../../technologies/cloudera/cloudera-ai-studios.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Select AI](../../technologies/oracle/oracle-select-ai.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Data Maker](../../technologies/sas/sas-data-maker.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Synthetic Data Vault (SDV)](../../technologies/open-source/sdv.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [K2view Data Product Platform](../../technologies/independent/k2view-data-product-platform.md), [MOSTLY AI Data Intelligence Platform](../../technologies/independent/mostly-ai-data-intelligence-platform.md), [Perforce Delphix](../../technologies/independent/perforce-delphix.md), [Tonic Structural](../../technologies/independent/tonic-structural.md), [Tonic Textual](../../technologies/independent/tonic-textual.md), [Gretel](../../technologies/independent/gretel.md) (retired) |
