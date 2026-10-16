---
type: Persona
id: persona-business-user
title: Business user
description: Uses data, reports and AI assistants to make decisions, without deep technical skills.
cares_about:
- dashboards-reports
- data-consumer-portal
- data-trust-indicators
- conversational-analytics
- enterprise-ai-assistant
- data-alerting
- spreadsheet-integration
- data-certification
- metric-definitions
- business-glossary
- enterprise-planning
- data-writeback
- manual-adjustments
- paginated-reports
- embedded-analytics
- access-requests
- row-level-security
- augmented-analytics
patterns: [data-marts]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Business users are managers and staff in sales, finance, operations, HR, supply chain and other functions. They read dashboards, receive scheduled reports, enter plans and forecasts, and increasingly ask AI assistants questions in plain language. Their tools are the BI portal, spreadsheets, email, chat and the business applications they work in all day.

Success for them is a reliable answer when they need it, in a tool they already use, without having to understand how the data was produced. They experience data problems as wrong numbers, slow pages and different answers from different people, and they are by far the largest group of platform users.

# Goals

- Get answers they can trust within minutes, in familiar tools.
- See exceptions and changes without having to go looking for them.
- Enter plans, forecasts and corrections without asking IT.
- Know whether a figure or an AI answer can be relied on.

# Jobs

- Review the dashboards and scheduled reports for their area.
- Ask questions of data in plain language or through an assistant.
- Export data to spreadsheets or work with it there.
- Enter budgets, forecasts, targets or corrections.
- Act on alerts, such as stock falling below a threshold or a customer at risk of leaving.
- Check that a report is current and trusted before using it in a decision.
- Request access to a report or dataset that a colleague has shared.

# Pain points

- There are too many dashboards and it is unclear which one is official.
- Different teams and tools give different answers to the same question.
- AI answers sound confident but cannot be checked.
- Small changes to a report mean waiting for an analyst.
- Reports do not show when the data was last updated or whether it passed its checks.

# Questions they ask

- Which report should I use for this decision, and is it up to date?
- Can I trust what the AI assistant tells me about our numbers?
- Can I have this data in my spreadsheet and keep it current?
- Why can a colleague see data that I cannot?
- Who do I tell when a number looks wrong, and will the report say so while it is being fixed?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Build and share visual, interactive dashboards with filters and drill-down. |
| [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Give business users one place to find the dashboards, apps and AI agents shared with them, without engineering tools. |
| [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents. |
| [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Ask questions of data in natural language and get answers, charts or SQL back. |
| [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Give staff a governed, ready-made assistant that answers questions and completes tasks across structured and unstructured enterprise data. |
| [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Notify people when data crosses thresholds, or deliver reports to them on a schedule. |
| [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Work with governed platform data directly from spreadsheet tools. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Mark assets as trusted, deprecated or under review so consumers know what to rely on. |
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define, certify and version key business metrics with owners and calculation logic. |
| [Business glossary](../capabilities/metadata/business-glossary.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Define business terms and link them to the data that represents them. |
| [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Build budgets, forecasts and plans over governed data, with versions, allocations and approval workflows. |
| [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Let users enter or correct data in analytics tools and write it back to governed tables with an audit trail. |
| [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Record manual adjustments to reported figures with approval steps, reasons and a full audit trail. |
| [Paginated reports](../capabilities/analytics-bi/paginated-reports.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Produce formatted, printable reports with precise layout for operational and regulatory use. |
| [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Put dashboards and analytics inside other applications and portals, often for external customers. |
| [Access requests and reviews](../capabilities/security/access-requests.md) | [Security and access](../capabilities/security/security.md) | Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | Restrict which rows each user sees based on who they are. |
| [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Use automation and machine learning to surface insights, anomalies and explanations without being asked. |

# Patterns

- [Data marts](../patterns/data-marts.md)

# Use cases they take part in

- [Agentic process automation](../use-cases/usecase-agentic-automation.md): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Churn prediction](../use-cases/usecase-churn-prediction.md): Score customers regularly by likelihood to leave so teams can act before they do.
- [Conversational analytics for business users](../use-cases/usecase-conversational-bi.md): Business users ask questions of governed data in plain language and get trustworthy answers.
- [Credit decisioning](../use-cases/usecase-credit-decisioning.md): Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
- [Customer 360](../use-cases/usecase-customer-360.md): Give every channel a single, trusted view of each customer.
- [Demand forecasting](../use-cases/usecase-demand-forecasting.md): Forecast demand by product, location and time to plan stock, staff and supply.
- [Document data extraction](../use-cases/usecase-document-extraction.md): Extract fields and tables from invoices, claims, contracts and forms into business systems, with people reviewing uncertain results.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md): Produce trusted, consistent KPIs and management reports across the organisation.
- [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md): Analyse sensor telemetry to predict equipment failures before they happen.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md): A generative AI assistant that answers questions from internal documents, with citations.
- [Marketing audience activation](../use-cases/usecase-marketing-activation.md): Build audiences from platform data and sync them to marketing and advertising tools.
- [Operational reporting](../use-cases/usecase-operational-reporting.md): Report on current operations within minutes of events happening.
- [Self-service BI](../use-cases/usecase-self-service-bi.md): Analysts and business users explore governed data and build their own reports with trusted metrics.
