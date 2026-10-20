---
type: Reference
id: sources-and-method
title: Sources and method
description: How the first version of the bundle was researched and written, how it was checked, and its known limitations.
order: 3
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

# How it was built

The first version was produced on 16 October 2026 in six steps.

1. **Skeleton.** A vendor-neutral capability tree was drafted from established practice in data architecture, data management and MLOps.
2. **Platform research.** Separate research passes covered AWS, Microsoft (Azure, Fabric, Power BI, Purview), Google Cloud, Snowflake, Databricks, ClickHouse, Informatica, Cloudera, Oracle, SAP, Teradata, IBM, Palantir, SAS, Dataiku, the open-source ecosystem and independent vendors. Each pass read vendor documentation and product pages, recorded current product names, renames and availability, mapped each technology to capabilities, and listed capabilities the tree lacked. The page used for each technology is its `resource`.
3. **Framework mapping.** DAMA-DMBOK, DCAM, CDMC, Google's and Microsoft's MLOps maturity models, the Bitol data contract and data product standards, the data mesh principles, BCBS 239, the EU AI Act, GDPR, ISO/IEC 42001, the NIST AI RMF, ISO 8000, the EU Data Act and DORA were mapped onto capabilities.
4. **Gap rounds.** About 70 capabilities suggested by the research, the frameworks and the writers were added, and technologies were re-mapped to them.
5. **Persona review.** Independent reviewers walked the bundle as each of the 16 personas, and as an AI agent answering architects' questions. Their findings led to 14 more capabilities, 6 more use cases, a further pattern, two more maturity tracks, four guidance pages, product families, alias and title fixes, and changes to the tooling.
6. **Checks.** Technology entries were cleaned up platform by platform (names, renames, availability, duplicate and inflated mappings). An independent fact-check of 70 technologies, weighted towards renamed, acquired and preview products, found 62 correct and 8 needing correction, all minor; the corrections were applied.

# Known limitations

- **Unreviewed.** No person has yet checked the content. Every concept is `status: draft` with no `verified` entry.
- **Point in time.** Product names, ownership and availability change quickly. Several vendors renamed major products during 2025 and 2026. Technology entries have `stale_after: 2027-04-16`.
- **Coverage is uneven.** The five largest platforms have 90-140 technologies each; others have 18-50. A missing mapping can mean the platform lacks the capability or that nobody has mapped it yet.
- **Not every claim was checked against a live page.** Research passes ran into search limits, and the fact-check covered a sample. Where a vendor states no release stage, `availability` is `unconfirmed`.
- **Mapping is judgement.** Whether a feature "realises" a capability is a judgement call, made conservatively. Platform fit tables count mappings; they do not measure quality, cost or ease of use.
- **Not advice.** Regulatory content summarises obligations at a general level and is not legal advice.
