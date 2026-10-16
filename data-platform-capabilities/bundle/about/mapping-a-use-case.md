---
type: Reference
id: mapping-a-use-case
title: Mapping a use case to capabilities
description: A practical method for turning a business use case into required capabilities with minimum maturity levels, checking platform fit and recording the result.
order: 7
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The aim is a short list of the capabilities a use case cannot do without, each with the minimum maturity level it needs and one sentence on why, plus those that help. The list drives platform choices, maturity gap analysis and delivery planning, so it should be specific enough that someone else could check it. Before starting, look for the closest existing use case in [use cases](../use-cases/index.md) and adapt it rather than start from nothing.

# 1. Clarify the outcome and non-functional needs

Write the outcome in one sentence that names who acts, on what, how soon, and how success is measured. "Reduce churn" is not an outcome; "retention advisers call customers showing a strong leaving signal on the same day, and retention improves against a control group" is.

Then pin down the non-functional needs as numbers, because they decide between capabilities that look alike.

| Need | Ask | Example answer |
|---|---|---|
| Latency and freshness | How old can data be when someone acts on it? | Signal to action within 15 minutes |
| Volume and concurrency | How much data, how many requests or users at peak? | 3 million events a day, 200 advisers |
| Availability | What happens if it is down for an hour, and when must it run? | Contact-centre hours; degrade to the daily list |
| Accuracy and reproducibility | Must results be explained, reproduced or audited? | Reasons on every task; retraining reproducible |
| Regulation and policy | Which purposes, consents, residency and retention rules apply? | Profiling only with consent; UK data stays in the UK |
| People | Who builds it, who runs it, who uses it? | Data scientists, ML engineers, CRM team, advisers |

# 2. Walk the domains

Ask one question per domain and note anything that applies. Each domain page has more *Questions to ask* and lists its capabilities.

| Domain | Ask |
|---|---|
| [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Which sources hold the data, how fresh must it be, and can the sources take extra load? |
| [Storage and table management](../capabilities/storage/storage.md) | Which engines must read or write the same data, and what retention or residency rules apply? |
| [Processing and transformation](../capabilities/processing/processing.md) | What latency does each dataset need, and who will write the logic? |
| [Orchestration](../capabilities/orchestration/orchestration.md) | What must run in what order, and what happens when a step fails or data arrives late? |
| [Query and compute](../capabilities/compute/compute.md) | What latency and concurrency do the workloads need, and how predictable is demand? |
| [Serving and activation](../capabilities/serving/serving.md) | Who consumes the results (people, applications, business tools or partners), and how fast? |
| [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | How will people see, explore or act on results, and must the numbers match other reports? |
| [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Will models be trained, and must training be reproducible or explainable? |
| [ML operations](../capabilities/mlops/mlops.md) | How are predictions delivered, and how will anyone know when a model stops working? |
| [Generative AI](../capabilities/generative-ai/generative-ai.md) | Will language models read, generate or act, and on which data? |
| [Metadata and discovery](../capabilities/metadata/metadata.md) | How will people and agents find, understand and trust the data involved? |
| [Data quality and observability](../capabilities/data-quality/data-quality.md) | What goes wrong if the data is late, incomplete or wrong, and who would notice? |
| [Master and reference data](../capabilities/master-data/master-data.md) | Must records about the same customer, product or supplier be matched across systems? |
| [Governance and compliance](../capabilities/governance/governance.md) | Which regulations, policies, permitted purposes and retention rules apply? |
| [Security and access](../capabilities/security/security.md) | Who may see which data, and which data would cause most harm if exposed? |
| [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | Does data cross team, organisation, region or cloud boundaries? |
| [Data products](../capabilities/data-products/data-products.md) | Will other teams depend on the outputs, and who owns them? |
| [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | How will changes be tested and released, and on what test data? |
| [Platform operations](../capabilities/platform-operations/platform-operations.md) | What availability, recovery and cost targets apply, and who is on call? |
| [Specialised data types](../capabilities/specialised-data/specialised-data.md) | Are there time series, locations, graphs, free text, documents, images or audio? |

# 3. Pick capabilities and minimum levels

For each domain that applies, open its page and choose capabilities.

- **Required or helpful.** A capability is required if the use case fails, or becomes unsafe or unlawful, without it. Everything else goes in *benefits from*. Most use cases need 8 to 16 required capabilities; a much longer list usually means helpful ones have crept in.
- **Narrowest fit.** Choose the most specific capability that states the need, such as [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) rather than [Feature store](../capabilities/machine-learning/feature-store.md). A parent hides which part matters.
- **Similar names.** Where two capabilities look alike, [Choosing between similar capabilities](similar-capabilities.md) shows how they differ. For applications reading from the platform, see [Read paths for applications](application-read-paths.md).
- **Why.** Write one sentence linking the capability to the outcome or a non-functional need. If you cannot, it is probably not required.
- **Dependencies.** Check the *Depends on* row in each capability's relationships table. [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), for example, needs [Inference logging](../capabilities/mlops/inference-logging.md).

Set the minimum level on the [maturity scale](../maturity/maturity-scale.md) for each required capability:

| Level | Set it when the use case needs |
|---|---|
| 1 Initial | Rarely a requirement. Acceptable only for a one-off or a proof of concept. |
| 2 Managed | One team doing it repeatably with basic tooling. Enough for most first releases that one team owns. |
| 3 Defined | A shared, documented platform standard. Needed when several teams rely on the capability, or when mistakes would be silent and costly. |
| 4 Measured | Automated monitoring against explicit targets, so the platform catches problems before consumers do. Typical for customer-facing, money-moving or regulated paths. |
| 5 Optimising | Continuous tuning from measurements. Usually a goal, rarely a minimum. |

# 4. Check platform fit

- Run `python tools/dpc.py usecase <use-case-id> --platform <platform-id>` to list, for each capability, the technologies that realise it on that platform. `python tools/dpc.py coverage <platform-id>` shows the platform's coverage by domain.
- After the use case is recorded and built, its *Platform fit* table counts how many required capabilities each platform covers.
- Treat gaps as questions, not verdicts. A gap can mean the platform lacks the capability, that it comes from a separate product, or that nobody has mapped it yet. Preview-only coverage is listed separately and should not carry a production commitment.
- Compare the minimum levels with how mature the organisation is today. [Running a maturity assessment](assessing-maturity.md) explains how to find the gaps that matter.

# 5. Check for common omissions

First drafts tend to cover the data and the model and miss how the work is released, run and controlled.

| Area | Question that is often skipped | Capabilities to check |
|---|---|---|
| Path to live | How does a change reach production, and how is it tested and rolled back? | [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md) |
| Observability | Who finds out when data is late or wrong, or a model degrades, and how quickly? | [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Data observability](../capabilities/data-quality/data-observability.md), [Model monitoring](../capabilities/mlops/model-monitoring.md) |
| Governance | Who owns the outputs, which data is personal, and which purposes and retention rules apply? | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data classification](../capabilities/governance/data-classification.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Retention and disposal](../capabilities/governance/data-retention.md) |
| Security | Which identities read and write, and who can see sensitive fields? | [Access control](../capabilities/security/access-control.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Secrets management](../capabilities/security/secrets-management.md), [Audit logging](../capabilities/security/audit-logging.md) |
| Last mile | Where do results reach the people or systems that act on them? | [Reverse ETL](../capabilities/serving/reverse-etl.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Data APIs](../capabilities/serving/data-apis.md) |
| Proof of value | How will anyone know the use case caused the improvement? | [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| Rework and recovery | How is history rebuilt after a bug, and what if data is lost? | [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| Cost | Who pays, and what stops runaway spend? | [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) |

# 6. Record it as a use case file

Create the file with the command-line tool, then fill it in:

```
python tools/dpc.py new use-case usecase-churn-early-warning \
  --title "Churn early warning" \
  --description "Rescore customers within minutes of a strong leaving signal and give the retention team a task with reasons."
```

This writes `use-cases/usecase-churn-early-warning.md` with draft frontmatter and empty *Non-functional requirements* and *Risks* sections. Add the relationships to the frontmatter. Quote any `why` that contains a comma or a colon.

```yaml
requires:
- {capability: streaming-inference, level: 2, why: Each qualifying event is scored within seconds of arriving.}
- {capability: point-in-time-joins, level: 3, why: 'Training must use features as known at each past signal, or the model learns from the future.'}
benefits_from:
- {capability: drift-detection, why: Warns when customer behaviour shifts before outcomes are known.}
personas: [persona-data-scientist, persona-ml-engineer, persona-software-engineer]
patterns: [fti-pipelines]
```

In the body, write two short paragraphs (what happens, and what good looks like), then list the non-functional needs from step 1 and the main risks. Run `python tools/dpc.py build` to generate the requirement tables, platform fit and links from each capability back to the use case, and `python tools/dpc.py validate` to check ids and links.

# Worked example: near-real-time churn early warning

**Outcome.** When a customer shows a strong sign of leaving, such as visiting the cancellation page, making a second complaint in a week or failing a payment, the retention team gets a task in the CRM within 15 minutes, with the main reasons, so an adviser can call the same day. Success is retention uplift against a randomly held-out control group.

**Non-functional needs.** 95% of tasks within 15 minutes of the signal during contact-centre hours. About 3 million web and app events and 50,000 service and payment events a day, of which a few thousand qualify for scoring. No customer who has opted out of profiling or retention contact is scored or called, and nobody is contacted more than once in 30 days.

**Starting point.** The existing [Churn prediction](../use-cases/usecase-churn-prediction.md) use case scores everyone daily and lists streaming scoring only as a benefit. Latency, the trigger and the delivery path differ enough to record a separate use case.

**Domain walk.** Ingestion (events from web, app, service and billing), processing (rolling counts per customer), ML development and operations (training, event-triggered scoring, monitoring), serving (a decision and a CRM task), analytics (the control group) and governance (consent) all apply. Master data helps but is not required if the customer id is consistent; specialised data and sharing do not apply.

| Capability | Minimum level | Why |
|---|---|---|
| [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md) | 2 | Cancellation-page visits are the earliest signal and must follow a tracking plan. |
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) | 3 | Complaints, payment failures and web events arrive on shared topics that other teams also read. |
| [Stream processing](../capabilities/processing/stream-processing.md) | 2 | Rolling counts per customer, such as failed payments in seven days, stay current. |
| [Online feature store](../capabilities/machine-learning/online-feature-store.md) | 2 | The scorer reads each customer's latest batch and streaming features in milliseconds. |
| [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) | 3 | Training must use features as known at each past signal, or the model learns from the future. |
| [Streaming inference](../capabilities/mlops/streaming-inference.md) | 2 | Each qualifying event is scored within seconds of arriving. |
| [Model explainability](../capabilities/machine-learning/model-explainability.md) | 2 | Advisers need the main reasons behind each score to choose what to say. |
| [Model registry](../capabilities/machine-learning/model-registry.md) | 2 | The version scoring live events is known and can be rolled back. |
| [Decision management](../capabilities/serving/decision-management.md) | 2 | Thresholds and the 30-day contact rule combine into a logged decision with reasons. |
| [Application integration](../capabilities/ingestion-integration/application-integration.md) | 2 | Tasks are created through the CRM's API within minutes. |
| [Inference logging](../capabilities/mlops/inference-logging.md) | 2 | Each score is kept with its features and model version so outcomes can be joined later. |
| [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | 2 | Actual churn is compared with past scores as it arrives. |
| [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) | 2 | A random holdout shows whether the calls cause retention, not only predict churn. |
| [Consent and purpose management](../capabilities/governance/consent-management.md) | 2 | Opted-out customers are excluded before scoring. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | 2 | A topic that stops flowing means no warnings, which looks the same as good news. |
| [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md) | 2 | Model and pipeline changes reach production through tested, repeatable releases. |

Most levels are 2 because one team owns the first release. Event streaming is 3 because other teams share the topics, and point-in-time joins are 3 because leakage fails silently: the model looks accurate offline and then fails in use.

Three choices in the table come from checking needs against capabilities. [Reverse ETL](../capabilities/serving/reverse-etl.md) was the first idea for reaching the CRM, but a 15-minute sync would use the whole latency budget, so the CRM task is created per event through application integration. Model explainability is required, not helpful, because the outcome says each task carries reasons. The last three rows (consent, freshness monitoring, and CI/CD for ML) came from the omissions check in step 5.

*Benefits from* includes [Drift detection](../capabilities/mlops/drift-detection.md) (warns before outcomes arrive), [Master data management](../capabilities/master-data/master-data-management.md) (avoids scoring duplicate customer records separately) and [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md) (a daily summary for team leaders).

**Platform fit.** Behavioural event collection, decision management, consent management and experimentation often come from separate products rather than from the data platform, such as an event collection tool, a rules engine or the CRM's own rules, a consent platform and an experimentation tool. Decide early who owns each integration, and check the remaining rows with `python tools/dpc.py usecase usecase-churn-early-warning --platform <platform-id>`.
