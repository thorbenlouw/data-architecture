---
type: Technology
id: sap-snowflake
title: SAP Snowflake
description: SAP-sold and SAP-operated Snowflake offering added to BDC as a solution extension, sharing SAP data products with Snowflake in both directions without copying.
platform: platform-sap
kind: managed-service
availability: unconfirmed
realises: [sql-query-engine, internal-data-sharing, engine-interoperability]
distribution_of: platform-snowflake
resource: https://www.sap.com/products/data-cloud/snowflake.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Announced at SAP TechEd on 5 November 2025, with general availability planned for the first quarter of 2026. SAP sells and operates it inside BDC; customers with their own Snowflake accounts use SAP BDC Connect for Snowflake instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** unconfirmed  
**Product family:** SAP Business Data Cloud  
**Distribution of:** [Snowflake](../../platforms/platform-snowflake.md). It is not counted in SAP's coverage.
