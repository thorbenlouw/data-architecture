---
type: Reference
id: similar-capabilities
title: Choosing between similar capabilities
description: Groups of capabilities that are easily confused, with one line on what each is and when to choose it.
order: 5
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Many capabilities overlap or sound alike, and choosing the wrong one usually surfaces later as a latency, cost or governance problem. Each section below takes one group of easily confused capabilities, states the question that separates them, and gives one line on what each is and when to choose it. Some capabilities appear in more than one group. Each capability page explains the differences in more detail.

# Getting data out of operational databases

They differ in how changes are found and whether the copy is meant to last.

| Capability | What it is | Choose it when |
|---|---|---|
| [Database extraction](../capabilities/ingestion-integration/database-extraction.md) | Reads tables with queries or bulk export, in full or filtered by a timestamp. | Initial loads, small reference tables, or sources that refuse log access. It misses hard deletes. |
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) | Reads the transaction log and emits every insert, update and delete as an event. | You need current copies, deletes and change history with little load on the source, and want to choose where changes go. |
| [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md) | A managed service that captures and applies changes end to end into platform tables. | You want a current analytical copy quickly and can accept the service's target layout and supported sources. |
| [Database migration](../capabilities/platform-operations/database-migration.md) | Converts schemas and keeps source and target in sync until a one-off cut-over. | The source database is being replaced, not fed to analytics indefinitely. |
| [Operational database integration](../capabilities/serving/operational-database.md) | Runs the transactional database as part of the platform, so no copy pipeline is needed. | You are building or moving an application and can host its database on the platform. |

# Streaming into and through the platform

They sit at different points between a producer and a table. [Event streaming](../capabilities/ingestion-integration/event-streaming.md) is the transport under most of them.

| Capability | What it is | Choose it when |
|---|---|---|
| [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) | Lands events from a broker, endpoint or device in tables within seconds, with light mapping only. | Consumers need raw or lightly shaped events in tables quickly. |
| [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md) | The streaming platform or a managed service writes topics as open-format tables itself. | Topics should be queryable as tables with no reshaping and no loader jobs to run. |
| [Stream processing](../capabilities/processing/stream-processing.md) | Continuous, stateful logic, such as joins, windows and running totals, over events as they arrive. | Results must be computed in flight, such as rolling fraud features or operational alerts. |
| [Streaming SQL](../capabilities/processing/streaming-sql.md) | Stream processing written in SQL, often as views that update continuously. | The people writing the logic know SQL and the logic fits it. |
| [Change feeds](../capabilities/serving/change-feeds.md) | Row-level changes to platform tables, exposed as an ordered stream for incremental readers. | Downstream jobs, caches or applications need only what changed in a platform table. |

Change data capture brings changes from source databases into the platform; change feeds publish changes from platform tables outwards.

# Moving data between systems

They differ in what moves (events, jobs, transactions, records or files) and why.

| Capability | What it is | Choose it when |
|---|---|---|
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) | Durable, ordered, replayable topics that many consumers read independently. | Several consumers need the same events, now or by replaying history. |
| [Message queuing](../capabilities/ingestion-integration/message-queuing.md) | Hands each message to one of several workers, which acknowledges it, after which it is gone. | Distributing jobs or commands that must each be handled once. |
| [Application integration](../capabilities/ingestion-integration/application-integration.md) | Flows that carry individual transactions between operational systems to run a business process. | An order in one system must trigger work in others within seconds. |
| [Reverse ETL](../capabilities/serving/reverse-etl.md) | Syncs modelled platform tables into the objects of business tools such as a CRM. | Staff or automations act on platform data inside a SaaS tool. |
| [Data export](../capabilities/serving/data-export.md) | Unloads tables or query results in bulk to files or another system. | The consumer cannot connect to the platform, such as a regulator or a legacy system. |

# Building transformations

They differ in who writes the logic and how much the platform decides for you.

| Capability | What it is | Choose it when |
|---|---|---|
| [SQL transformation](../capabilities/processing/sql-transformation.md) | SQL that transforms data already loaded into the platform. | The default for most warehouse and lakehouse transformation. |
| [Transformation as code](../capabilities/processing/transformation-as-code.md) | A Git project of small SQL or Python models with tests, documentation and automatic ordering. | Several people maintain shared models and need review, tests and separate environments. |
| [Declarative pipelines](../capabilities/processing/declarative-pipelines.md) | You declare target tables; the platform works out order, incremental refresh and retries. | You want the engine to manage incremental and streaming refresh, and accept being tied to it. |
| [Low-code transformation](../capabilities/processing/low-code-transformation.md) | Pipelines assembled visually from configured components. | Integration developers build simple flows and prefer not to write code. |
| [Self-service data preparation](../capabilities/processing/data-preparation.md) | Interactive, recipe-based cleaning and reshaping by analysts, usually on samples. | An analyst needs data shaped for one analysis, not a production pipeline. |

# History, copies and recovery

They differ in whether you look back, make a separate copy, or recover from loss.

| Capability | What it is | Choose it when |
|---|---|---|
| [Time travel](../capabilities/storage/time-travel.md) | Query or restore a table's own earlier snapshots within a retention window. | Undoing a bad load or delete, or reproducing a recent result. |
| [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) | An instant, independent copy that shares files with the source until either side changes. | Full-size development or test environments, or freezing a dataset for audit or training. |
| [Data branching and tagging](../capabilities/storage/data-branching.md) | Git-style branches and tags of tables or whole catalogues, with merge. | Several tables must change in isolation and be published together after checks. |
| [Backup and restore](../capabilities/platform-operations/backup-restore.md) | Copies of data and metadata held apart from the source and restorable to a chosen point. | Mistakes found after the time travel window, or loss or compromise of the account itself. |
| [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md) | Data and configuration replicated to another region, ready to take over. | A regional outage must not stop critical workloads. |

# Making queries faster

They differ in whether they skip data, reuse earlier work or accept approximate answers.

| Capability | What it is | Choose it when |
|---|---|---|
| [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md) | Lays out table data by key columns so whole partitions or files can be skipped. | Queries filter on predictable columns such as date or region. |
| [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md) | Statistics, bloom filters and indexes that rule out data before it is read. | Selective queries on columns that layout alone does not help. |
| [Result caching](../capabilities/compute/result-caching.md) | Returns a stored result when an identical query runs again on unchanged data. | Many people open the same dashboards over slowly changing tables. |
| [Materialised views](../capabilities/compute/materialised-views.md) | The engine stores and refreshes a query's result, and may use it to answer other queries. | The same aggregation or join over large data runs repeatedly. |
| [Approximate query processing](../capabilities/compute/approximate-query-processing.md) | Sampling and sketches give fast answers within a known error. | Approximate counts or distinct counts are good enough, as in exploration and monitoring. |

# Fast and consistent analytical reads

Ask who owns the refresh, and whether results are precomputed or calculated at request time.

| Capability | What it is | Choose it when |
|---|---|---|
| [Read-optimised views](../capabilities/serving/read-optimised-views.md) | Tables built by pipelines in the exact shape consumers read: pre-joined, pre-aggregated, filtered. | Many consumers run similar queries, or response times must be predictable. |
| [Materialised views](../capabilities/compute/materialised-views.md) | A stored query result that the engine itself keeps current. | You want the engine, not a pipeline, to maintain an aggregation or join. |
| [Operational data store](../capabilities/serving/operational-data-store.md) | A current, integrated view of several operational systems, shaped for lookups and short queries. | Operational staff need minutes-old data across systems that cannot take the query load. |
| [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) | Definitions of entities, joins and measures that generate queries at request time. | Several tools must calculate the same measures identically. It describes tables; it does not build them. |
| [Real-time analytical database](../capabilities/compute/real-time-analytics.md) | A database that ingests streams and answers aggregations in milliseconds at high concurrency. | Analytics face customers or operations and need seconds-fresh data for thousands of concurrent queries. |

# Serving operational applications

They differ in whether the application writes, whether data is integrated across sources, and whether it feeds a model.

| Capability | What it is | Choose it when |
|---|---|---|
| [Operational database integration](../capabilities/serving/operational-database.md) | A transactional database run as part of the platform, with data flowing to analytical tables. | The application writes as well as reads, with transactions. |
| [Operational data store](../capabilities/serving/operational-data-store.md) | Current, integrated records from several operational systems for lookups and operational reports. | Users need one current view across systems, minutes old, at moderate request rates. |
| [Low-latency serving](../capabilities/serving/low-latency-serving.md) | Precomputed records loaded into a key-value, document or cache store for millisecond lookups. | Each request needs one record or a small set, at thousands of requests a second. |
| [Online feature store](../capabilities/machine-learning/online-feature-store.md) | Low-latency serving of the latest feature values, kept consistent with training history. | A model scores inside a request and needs its features in milliseconds. |

[Read paths for applications](application-read-paths.md) compares these with the other ways an application can read from the platform.

# Using data where it lives

All avoid copying data by hand. They differ in whether they move queries, metadata, access or data.

| Capability | What it is | Choose it when |
|---|---|---|
| [Query federation](../capabilities/compute/query-federation.md) | Runs queries against external databases or storage in place, pushing parts of each query down. | Exploration, data that may not be copied, or the period before a pipeline is worth building. |
| [Catalogue federation](../capabilities/storage/catalogue-federation.md) | Shows tables from other catalogues in one catalogue with one set of permissions. | Migrations, acquisitions or several platforms need one place to find and govern tables. |
| [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md) | Several engines read and write the same tables through open formats and a shared catalogue. | Different workloads need different engines on one copy of the data. |
| [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md) | Live access to curated tables across workspaces or accounts, without copies. | Teams in separate workspaces or accounts need each other's data. |
| [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md) | Continuously copies an operational database into platform tables. | Analytics use the data heavily and repeatedly, so federated queries would load the source or cost too much. |

# Sharing outside the organisation

They differ in what the recipient runs and what it can see.

| Capability | What it is | Choose it when |
|---|---|---|
| [External data sharing](../capabilities/data-sharing/external-data-sharing.md) | Live, revocable shares of tables or views to customers and partners. | Recipients use the same platform, or a reader account the provider supplies. |
| [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) | Live shares read through an open protocol by any compatible engine. | Recipients use a different platform or vendor. |
| [Data marketplace](../capabilities/data-sharing/data-marketplace.md) | Listings that consumers find and subscribe to, with terms, approval and possibly payment. | Many consumers should serve themselves, or the data is sold. |
| [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md) | Joint analysis in which each party controls what the others can see and only approved outputs leave. | Parties must combine data that neither may share with the other directly. |
| [Data application distribution](../capabilities/data-sharing/application-sharing.md) | Installable applications that run the provider's code and models on the consumer's data, in the consumer's account. | The value is in the logic, and the consumer's data may not leave. |
| [Data export](../capabilities/serving/data-export.md) | Bulk files or loads delivered outside the platform. | The recipient cannot read a live share. |

# Defining business meaning

They differ in who reads the definition (people, tools or models) and whether it is executed.

| Capability | What it is | Choose it when |
|---|---|---|
| [Business glossary](../capabilities/metadata/business-glossary.md) | Agreed definitions of business terms in words, with owners, linked to the data. | People disagree about what a term means or which data represents it. |
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | Certified, versioned calculation logic for key metrics, each with an owner. | Key figures must be calculated one approved way. |
| [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) | A queryable model of entities, joins and measures that generates SQL for tools. | Several tools must compute those metrics identically at query time. |
| [AI context layer](../capabilities/metadata/ai-context-layer.md) | Definitions, verified queries and usage guidance prepared for AI agents to retrieve. | Agents or conversational analytics must interpret local data correctly. |
| [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) | Entities and typed relationships under a formal ontology that machines can reason over. | Data from many sources must be linked by meaning, or AI needs verified entities and relationships. |

# Catalogues and inventories of data

They differ in who uses them and what they list.

| Capability | What it is | Choose it when |
|---|---|---|
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | A searchable inventory of data assets with owners, descriptions, quality and usage. | People and agents need to find data and judge whether to trust it. |
| [Table catalogue](../capabilities/storage/table-catalogue.md) | The technical registry engines use to resolve table names to schemas, locations, commits and permissions. | Engines must find, commit to and govern tables. Every lakehouse needs one. |
| [Business glossary](../capabilities/metadata/business-glossary.md) | Business terms and their agreed meanings, linked to the data. | The problem is meaning, not location. |
| [AI context layer](../capabilities/metadata/ai-context-layer.md) | Curated knowledge served to AI agents at question time. | Agents answer questions over data. |
| [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) | An inventory of topics and data APIs with owners, schemas, versions and consumers. | Many teams publish events and APIs and nobody can say who depends on what. |

A [Schema registry](../capabilities/metadata/schema-registry.md) enforces event schema compatibility but records little about ownership, meaning or consumers.

# Describing data products

They differ in scope: a whole product, one output, one promise or one label.

| Capability | What it is | Choose it when |
|---|---|---|
| [Data product specification](../capabilities/data-products/data-product-specification.md) | A machine-readable description of a whole product: purpose, owners, outputs and terms of use. | Products must be registered, provisioned and checked automatically. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | The enforced promise on one output: schema, meaning, quality and service levels, with a change process. | Data crosses a team boundary and consumers need protection from unannounced change. |
| [Data service levels](../capabilities/data-products/data-slas.md) | Targets for freshness, availability and quality, measured and published with their history. | Consumers need to judge reliability, and producers need a definition of success. |
| [Schema registry](../capabilities/metadata/schema-registry.md) | Versioned event schemas with enforced compatibility rules. | Event producers and consumers must not break each other. It covers structure only. |
| [Data certification](../capabilities/metadata/data-certification.md) | A trust label on an asset: certified, deprecated or under review. | Consumers must know which of several similar assets to rely on. |

# Checking data

They differ in when they run and who decides what correct means.

| Capability | What it is | Choose it when |
|---|---|---|
| [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) | Tests of pipeline logic and output on known inputs, before release. | Changing pipeline code, to catch errors before they reach production. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | Explicit checks that production data must pass, run in pipelines or on a schedule. | Requirements are known: business rules, regulatory checks, conditions consumers rely on. |
| [Data observability](../capabilities/data-quality/data-observability.md) | Broad monitoring of freshness, volume, schema and distributions across production tables. | Problems nobody anticipated must be caught across many tables without writing rules for each. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | A published, owned promise between producer and consumer, checked in the producer's build and runs. | Data crosses a team boundary and detection should move to the producer. |
| [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) | Counts, totals and record matching that prove data moved completely and correctly. | Finance, regulatory or migration work needs evidence that nothing was lost or altered. |

# Monitoring the platform and its data

They differ in whether they watch services, jobs or the data the jobs produce.

| Capability | What it is | Choose it when |
|---|---|---|
| [Platform observability](../capabilities/platform-operations/platform-observability.md) | Logs, metrics and traces for jobs, queries and services across the platform. | The platform team needs to know whether the platform is healthy. |
| [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) | Records of pipeline runs, failures and durations, with alerts to owners. | Teams must know when a job fails or runs late. |
| [Data observability](../capabilities/data-quality/data-observability.md) | Monitors the data produced: freshness, volume, schema and distributions. | Jobs can succeed while loading wrong or partial data. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | Checks that each dataset arrives by its expected time. | Consumers depend on a deadline. Usually the first data check to add. |
| [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) | Usage, billing and operational data exposed as queryable tables. | You want to analyse platform use and cost with SQL or build your own monitoring. |

# Monitoring models and AI

They differ in what they compare against: outcomes, training data, tables or traces. [Inference logging](../capabilities/mlops/inference-logging.md) supplies the records most of them need.

| Capability | What it is | Choose it when |
|---|---|---|
| [Model monitoring](../capabilities/mlops/model-monitoring.md) | The umbrella: service, input, output and quality metrics for each production model. | Any model is in production. |
| [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | Joins predictions to actual outcomes as they arrive and tracks quality over time. | Outcomes become known, even weeks later. It is the only direct measure that a model still works. |
| [Drift detection](../capabilities/mlops/drift-detection.md) | Compares live inputs and predictions with training data and alerts on change. | Outcomes arrive late or never, and an early warning is needed. |
| [Data observability](../capabilities/data-quality/data-observability.md) | Monitors tables and pipelines, not models. | The data feeding models, and every other consumer, needs watching. |
| [Generative AI observability](../capabilities/generative-ai/genai-observability.md) | Traces each prompt, retrieval, model call, tool call and response, with cost and feedback. | Applications and agents are built on language models. |

# Testing models in production

They differ in whether anyone acts on the new model's output, and for how long the comparison runs.

| Capability | What it is | Choose it when |
|---|---|---|
| [Shadow deployment](../capabilities/mlops/shadow-deployment.md) | The new model scores live traffic, but its outputs are not used. | A first live test. It is safe but cannot measure the effect of acting on predictions. |
| [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md) | A share of traffic acts on the new model. A canary checks safety; an A/B test measures which version is better. | Releasing a model version and measuring the business effect of acting on it. |
| [Champion-challenger](../capabilities/mlops/champion-challenger.md) | A standing process: challengers run beside the champion and are promoted on agreed evidence. | Decisioning models, such as credit and collections, where a continuing record is expected. |
| [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) | Randomised experiments with control groups that measure whether any action caused an outcome. | Product, pricing, marketing or policy changes, not only models. |

# Checking generative AI

They differ in timing (before release or on every request) and in whether they judge, block or only record.

| Capability | What it is | Choose it when |
|---|---|---|
| [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) | Scores outputs against test sets and rubrics, with human review and model judges. | Deciding whether a change is good enough to release, and sampling live quality. |
| [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md) | Deliberate attacks: jailbreaks, prompt injection, data extraction and tool misuse. | Before release and after significant changes, to find failures under hostile use. |
| [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) | Run-time checks on inputs, outputs and tool calls that block, redact or escalate. | Policies must be enforced on every request, outside the model. |
| [Generative AI observability](../capabilities/generative-ai/genai-observability.md) | Traces of what happened in each request. | Debugging, cost attribution and feeding evaluation. It records but does not judge. |
| [Human oversight of AI](../capabilities/governance/human-oversight.md) | Routes decisions to people for review, approval or override. | Actions are high-impact, or regulation requires a person in the loop. |

# Inventories of models and AI systems

They differ in what they list and who uses the list.

| Capability | What it is | Choose it when |
|---|---|---|
| [Model registry](../capabilities/machine-learning/model-registry.md) | Versions of trained models with metrics, approval state and aliases used by deployment. | Teams deploy, promote and roll back trained models. |
| [Model governance](../capabilities/mlops/model-governance.md) | An inventory of models with owners, risk tiers, validation evidence and approvals. | Models affect customers, money or safety, or model risk rules apply. |
| [AI governance](../capabilities/governance/ai-governance.md) | Governance of all AI systems, including purchased services, generative AI and agents. | AI regulation or policy applies across the organisation. |
| [Agent and tool registry](../capabilities/generative-ai/agent-registry.md) | The approved list of agents, tools and MCP servers that runtimes check against. | Agents and tool servers multiply, and access must be approved and controlled. |
| [AI system discovery](../capabilities/governance/ai-system-discovery.md) | Finds AI systems in use that were never registered. | The inventory must be complete, including unapproved use. |

# Search and retrieval

They differ in what counts as a match: words, meaning, relationships or permission.

| Capability | What it is | Choose it when |
|---|---|---|
| [Full-text search](../capabilities/specialised-data/full-text-search.md) | Inverted indexes that match words and rank results by relevance. | People search by terms, codes and names. |
| [Vector search](../capabilities/generative-ai/vector-search.md) | Finds the items whose embeddings are nearest, so it matches meaning. | Queries and content use different words for the same thing. Usually combined with keyword search. |
| [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) | Retrieves relevant passages at question time and gives them to a model to ground its answer. | A language model must answer from your own content. |
| [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) | Entities and typed relationships under an ontology. | Answers depend on relationships between entities rather than on similar passages. |
| [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md) | Filters retrieved content by each user's permissions in the source systems. | An assistant searches content with mixed access rights. |

# Natural-language access

They differ in whether the user asks, the tool volunteers, or the system acts.

| Capability | What it is | Choose it when |
|---|---|---|
| [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) | Natural-language questions answered from structured data, with the generated query shown. | Business users ask questions of governed data and metrics. |
| [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md) | The tool surfaces anomalies, drivers and insights without being asked. | Users need to be told what changed rather than ask. |
| [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md) | A ready-made assistant across documents, applications and data, under each user's permissions. | Staff need one general assistant, and building it would not set you apart. |
| [AI agents](../capabilities/generative-ai/ai-agents.md) | Systems in which models plan, call tools and act over several steps. | A task needs actions in systems, not only answers. |

# Protecting sensitive data in use

They differ in whether the stored data changes, and whom it is protected from.

| Capability | What it is | Choose it when |
|---|---|---|
| [Column security and dynamic masking](../capabilities/security/column-masking.md) | Hides or transforms column values at query time depending on who asks. Stored data is unchanged. | One table serves users with different rights. |
| [De-identification](../capabilities/governance/deidentification.md) | Pseudonymises, tokenises or anonymises the stored data itself, usually in a pipeline. | Data is used for analytics, testing, sharing or training where identities are not needed. |
| [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md) | Limits what results reveal, through aggregation thresholds, differential privacy or secure computation. | Results must not expose individuals, even to authorised analysts or partners. |
| [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md) | A collaboration space built on these techniques, with each party's rules on joins and outputs. | Two or more organisations analyse combined data that none may see in full. |
| [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md) | Artificial records generated to keep the useful properties of real data. | Even masked real data is too risky, or real examples are scarce. It is not automatically anonymous. |
