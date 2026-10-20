---
type: Capability
id: test-data-management
title: Test data management
description: Provide realistic, safe data for development and testing through subsetting, masking or generation.
aliases: [TDM]
broader: [development-lifecycle]
related: [deidentification, zero-copy-cloning, column-masking, environment-promotion, data-subject-requests]
depends_on: [data-classification]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tests are only meaningful on data that behaves like production, with similar volumes, edge cases and relationships. Three techniques provide it without exposing real customers. Subsetting extracts a consistent slice, such as 1% of customers with all their orders, keeping foreign keys intact. Masking replaces sensitive values with realistic substitutes, ideally consistently, so the same real name always becomes the same fake name across tables and systems. Generation creates artificial records from rules or models. Environments are then refreshed on a schedule or on request.

This matters wherever production holds personal, financial or health data, because copying it into development usually breaks privacy rules and widens who can see it. Small consistent subsets also build and test faster than full copies. Zero-copy cloning gives an environment data quickly, but a clone of production is still production data unless it is masked. Synthetic data generation is the specialised form of the generation technique.

# Key considerations

- Masking must keep referential integrity and formats across tables and systems, or joins and validation tests fail.
- Free-text fields, logs and semi-structured columns often hide personal data that column-level masking misses.
- Treat masked data as lower risk, not zero risk. Combinations of retained attributes can still identify people.
- Automate refreshes. Test data that is months old misses new edge cases and schema changes.

# Questions to ask

- Does any non-production environment hold unmasked personal or regulated data today?
- What volume and variety of data do tests need to be meaningful?
- How often must test environments be refreshed, and who asks for it?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Narrower | [Synthetic data generation](synthetic-data.md) |
| Related | [Analytical sandboxes](../analytics-bi/analytical-sandboxes.md), [Column security and dynamic masking](../security/column-masking.md), [Data subject requests](../governance/data-subject-requests.md), [De-identification](../governance/deidentification.md), [Environment promotion](environment-promotion.md), [Zero-copy cloning](../storage/zero-copy-cloning.md) |
| Depends on | [Data classification](../governance/data-classification.md) |
| Needed by | [Data pipeline testing](data-testing.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (benefits from)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery table clones](../../technologies/google-cloud/gcp-bigquery-table-clones.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake zero-copy cloning](../../technologies/snowflake/snowflake-zero-copy-cloning.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks table clone (shallow and deep clone)](../../technologies/databricks/databricks-table-clone.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Data Masking transformation](../../technologies/informatica/informatica-data-masking-transformation.md), [Informatica Test Data Management (TDM)](../../technologies/informatica/informatica-test-data-management.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Data Safe](../../technologies/oracle/oracle-data-safe.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Backup, Archive and Restore and Data Mover](../../technologies/teradata/teradata-bar-data-mover.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM InfoSphere Optim](../../technologies/ibm/ibm-optim.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [lakeFS](../../technologies/open-source/lakefs.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [K2view Data Product Platform](../../technologies/independent/k2view-data-product-platform.md), [Perforce Delphix](../../technologies/independent/perforce-delphix.md), [Tonic Structural](../../technologies/independent/tonic-structural.md) |

Narrower capabilities are realised by a further 12 technologies; see their pages.
