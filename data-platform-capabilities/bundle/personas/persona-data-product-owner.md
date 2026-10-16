---
type: Persona
id: persona-data-product-owner
title: Data product owner
description: Owns the value, roadmap and consumers of one or more data products.
cares_about:
- data-product-specification
- data-contracts
- data-slas
- data-product-lifecycle
- usage-metadata
- data-catalogue
- data-marketplace
- internal-data-sharing
- access-requests
- data-ownership
- freshness-monitoring
- data-quality-scorecards
- cost-attribution
- impact-analysis
- external-data-sharing
- data-usage-rights
- data-certification
- data-domains
patterns: [data-mesh, shift-left]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data product owners are accountable for datasets, models or APIs published for others to use, such as a customer master, a sales performance product or a pricing feed. They sit in a business domain or a domain-aligned data team and decide what the product contains, who it serves, which service levels it promises and what is built next. The role is often new and borrows from software product management.

Success is a product with known consumers who use it instead of building their own copies, published service levels that are met, and changes released with notice rather than surprises. They need usage and cost figures to justify continued investment.

# Goals

- Grow use of the product among the consumers it is meant for.
- Meet the freshness, quality and availability the product promises.
- Change the product without breaking its consumers.
- Show what the product costs and what value it supports.

# Jobs

- Write the product's specification, contract and service levels.
- Prioritise the backlog with consumers and engineers.
- Review usage, quality and service-level reports.
- Approve consumer access and terms of use.
- Plan new versions and deprecations, and notify consumers.
- Report product cost and value to domain leadership.

# Pain points

- It is unclear who consumes the product and how.
- Consumers build their own copies instead of using the product.
- Upstream sources introduce breaking changes.
- Cost allocation does not reflect how the product is used.

# Questions they ask

- What must a dataset publish before it counts as a data product here?
- How do we measure and publish service levels automatically?
- How do we version and deprecate without breaking consumers?
- Can we share the product with other domains or external partners without making copies?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Data product specification](../capabilities/data-products/data-product-specification.md) | [Data products](../capabilities/data-products/data-products.md) | Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | [Data products](../capabilities/data-products/data-products.md) | Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers. |
| [Data service levels](../capabilities/data-products/data-slas.md) | [Data products](../capabilities/data-products/data-products.md) | Set and track service levels for data products, such as freshness, availability and quality. |
| [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) | [Data products](../capabilities/data-products/data-products.md) | Version, publish, deprecate and retire data products with notice to their consumers. |
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Show who uses which data, how often and how, to guide discovery and clean-up. |
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Provide a searchable inventory of data assets with descriptions, owners, quality and usage. |
| [Data marketplace](../capabilities/data-sharing/data-marketplace.md) | [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | Publish, find and subscribe to data products and datasets, internally or commercially. |
| [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md) | [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | Share live data between teams, accounts and workspaces without copying it. |
| [Access requests and reviews](../capabilities/security/access-requests.md) | [Security and access](../capabilities/security/security.md) | Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle. |
| [Ownership and stewardship](../capabilities/governance/data-ownership.md) | [Governance and compliance](../capabilities/governance/governance.md) | Assign accountable owners and stewards to data and record their responsibilities. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Detect when data arrives later than expected or misses its freshness target. |
| [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Track quality results over time and report them by dataset, domain and quality dimension. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Attribute spend to teams, products and workloads using tags and usage data. |
| [Impact analysis](../capabilities/metadata/impact-analysis.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Use lineage to find everything affected by a proposed change or a data incident. |
| [External data sharing](../capabilities/data-sharing/external-data-sharing.md) | [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | Share live data with customers, partners and suppliers under agreed terms. |
| [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) | [Governance and compliance](../capabilities/governance/governance.md) | Record licence terms and permitted uses of datasets and check use against them, including for model training. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Mark assets as trusted, deprecated or under review so consumers know what to rely on. |
| [Data domains](../capabilities/governance/data-domains.md) | [Governance and compliance](../capabilities/governance/governance.md) | Group data assets, products and owners into business domains with their own stewardship and policies. |

# Patterns

- [Data mesh](../patterns/data-mesh.md)
- [Shift-left data quality and governance](../patterns/shift-left.md)

# Use cases they take part in

- [Application data publishing](../use-cases/usecase-application-data-publishing.md): Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
- [Churn prediction](../use-cases/usecase-churn-prediction.md): Score customers regularly by likelihood to leave so teams can act before they do.
- [Customer 360](../use-cases/usecase-customer-360.md): Give every channel a single, trusted view of each customer.
- [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md): Give external customers fast, secure analytics inside a product.
- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md): Share or sell data products to partners and customers under agreed terms.
- [Personalised recommendations](../use-cases/usecase-recommendations.md): Recommend products or content to each user in real time.
- [Platform cost management and chargeback](../use-cases/usecase-platform-cost-management.md): Attribute, forecast and control what the data platform costs, and recover it from the teams and products that use it.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.

# Frameworks they work with

- [Data mesh principles](../frameworks/framework-data-mesh.md): Four principles for decentralising analytical data ownership to business domains while keeping data interoperable and governed.
- [EU Data Act](../frameworks/framework-eu-data-act.md): Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.
- [Open Data Contract Standard (ODCS)](../frameworks/framework-bitol-odcs.md): An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.
- [Open Data Product Standard (ODPS)](../frameworks/framework-bitol-odps.md): An open YAML standard for describing a data product, its input and output ports, management interfaces, team and support.
