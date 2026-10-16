---
type: Persona
id: persona-platform-engineer
title: Data platform engineer
description: Builds and runs the shared data platform and its self-service tooling.
cares_about:
- infrastructure-as-code
- self-service-provisioning
- multi-tenancy
- configuration-guardrails
- identity-authentication
- access-control
- network-security
- platform-observability
- platform-incident-management
- system-telemetry
- compute-options
- workload-isolation
- workload-management
- elastic-scaling
- runtime-management
- cost-attribution
- spend-controls
- secrets-management
- encryption
- customer-managed-keys
- audit-logging
- table-catalogue
- credential-vending
- ci-cd
- environment-promotion
- business-continuity
- resilience-testing
- compute-user-isolation
- hybrid-data-plane
patterns: [lakehouse, data-mesh]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data platform engineers usually work in a central platform team and treat the platform as an internal product whose customers are data engineers, analysts, data scientists and AI engineers. They look after accounts and workspaces, storage, catalogues, compute policies, identity and network integration, deployment templates and monitoring. Most of their work is code: infrastructure definitions, automation and templates that replace tickets.

Success means a team can get a governed workspace, pipeline or compute environment from a template in hours rather than weeks, the platform meets its availability and recovery targets, every cost has an owner, and security settings are the same everywhere because they come from code rather than from a console.

# Goals

- Give teams self-service access to approved resources without raising tickets.
- Keep the platform secure, available and recoverable, with all configuration held as code.
- Make every unit of spend attributable to a team, product or workload.
- Upgrade and change platform components without breaking user workloads.

# Jobs

- Provision accounts, workspaces, catalogues, compute policies and networking through infrastructure as code.
- Integrate the platform with the identity provider, secrets store and key management service.
- Build and maintain standard templates for pipelines, CI/CD and environments.
- Monitor platform health, job failures, quotas and capacity, and lead incident response.
- Apply tagging, budgets and compute policies, and tune the platform for cost.
- Plan and test backup, failover and version upgrades.
- Roll out runtime, library and orchestrator upgrades across tenants, testing representative workloads first.
- Define and enforce resource policies, such as allowed compute sizes, mandatory tags and private networking, at organisation and workspace level.

# Pain points

- Requests arrive as tickets for things that should be self-service, and the team becomes a bottleneck.
- Environments drift apart because of changes made by hand in consoles.
- One heavy workload on shared compute slows everyone else.
- Vendor features change quickly, and preview features become dependencies before they are supported.
- Gaps in telemetry make incidents and bills hard to explain.
- Hundreds of jobs pin old runtime versions, so security patches and upgrades stall.

# Questions they ask

- Should each domain get its own workspace and catalogue, or share them with finer-grained permissions?
- Which parts of the platform can be defined entirely in code, and which still need manual steps?
- Serverless or provisioned compute for each workload type, given its cost and performance targets?
- Which recovery time and recovery point objectives must we meet, and how do we prove them?
- How do we run processing inside our own network or cloud account for regulated data?
- Which configuration rules must hold everywhere, and are they enforced when resources are created or only reported afterwards?
- How many runtime versions will we support at once, and how do we move teams off old ones?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Define platform resources, permissions and configuration as code and apply them automatically. |
| [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Let teams create approved workspaces, pipelines and resources from templates without waiting for a central team. |
| [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations. |
| [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | Authenticate people and services through central identity, single sign-on and short-lived credentials. |
| [Access control](../capabilities/security/access-control.md) | [Security and access](../capabilities/security/security.md) | Decide who can see and change which data, at every level from account down to individual values. |
| [Network security](../capabilities/security/network-security.md) | [Security and access](../capabilities/security/security.md) | Keep data traffic on private networks and restrict where the platform can be reached from. |
| [Platform observability](../capabilities/platform-operations/platform-observability.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Monitor jobs, queries, services and usage across the platform with logs, metrics and traces. |
| [Platform incident management](../capabilities/platform-operations/platform-incident-management.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Detect, escalate and resolve platform outages and degradations through on-call rotas, runbooks and post-incident reviews. |
| [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Expose platform usage, billing and operational data as queryable tables. |
| [Compute provisioning options](../capabilities/compute/compute-options.md) | [Query and compute](../capabilities/compute/compute.md) | Choose how compute is supplied, from serverless capacity to clusters you size and control. |
| [Workload isolation](../capabilities/compute/workload-isolation.md) | [Query and compute](../capabilities/compute/compute.md) | Run different workloads on separate compute so one cannot slow or starve another. |
| [Workload management](../capabilities/compute/workload-management.md) | [Query and compute](../capabilities/compute/compute.md) | Prioritise, queue and limit queries and jobs so the most important work meets its service levels. |
| [Elastic scaling](../capabilities/compute/elastic-scaling.md) | [Query and compute](../capabilities/compute/compute.md) | Add and remove compute automatically as load changes, including for bursts of concurrent users. |
| [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Attribute spend to teams, products and workloads using tags and usage data. |
| [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Set budgets, quotas and alerts, and stop runaway spend automatically. |
| [Secrets management](../capabilities/security/secrets-management.md) | [Security and access](../capabilities/security/security.md) | Store and rotate the credentials and keys used by pipelines and tools without putting them in code. |
| [Encryption](../capabilities/security/encryption.md) | [Security and access](../capabilities/security/security.md) | Encrypt data at rest and in transit, with keys managed securely. |
| [Customer-managed keys](../capabilities/security/customer-managed-keys.md) | [Security and access](../capabilities/security/security.md) | Encrypt platform data with keys you control, so you can rotate or revoke them. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | Record who accessed or changed what, when and from where, and keep the records tamper-evident. |
| [Table catalogue](../capabilities/storage/table-catalogue.md) | [Storage and table management](../capabilities/storage/storage.md) | Register tables, their schemas and storage locations so engines can find, govern and share them. |
| [Storage credential vending](../capabilities/storage/credential-vending.md) | [Storage and table management](../capabilities/storage/storage.md) | Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access. |
| [CI/CD](../capabilities/development-lifecycle/ci-cd.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Build, test and deploy pipelines, models and infrastructure automatically on every change. |
| [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Promote the same artefacts through development, test and production with environment-specific configuration. |
| [Backup and disaster recovery](../capabilities/platform-operations/business-continuity.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Protect against data loss and outages with backups, replication and failover. |
| [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Test backup, recovery and failover regularly and record the results as evidence. |
| [Shared compute isolation](../capabilities/security/compute-user-isolation.md) | [Security and access](../capabilities/security/security.md) | Sandbox each user's code on shared compute so nobody can bypass access controls or affect other users. |
| [Customer-hosted data plane](../capabilities/platform-operations/hybrid-data-plane.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Run processing inside your own network or cloud account while the vendor operates the control plane as a service. |

# Patterns

- [Lakehouse](../patterns/lakehouse.md)
- [Data mesh](../patterns/data-mesh.md)

# Use cases they take part in

- [Agentic process automation](../use-cases/usecase-agentic-automation.md): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Application data publishing](../use-cases/usecase-application-data-publishing.md): Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
- [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md): Give external customers fast, secure analytics inside a product.
- [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md): Analyse sensor telemetry to predict equipment failures before they happen.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md): A generative AI assistant that answers questions from internal documents, with citations.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Operational reporting](../use-cases/usecase-operational-reporting.md): Report on current operations within minutes of events happening.
- [Platform cost management and chargeback](../use-cases/usecase-platform-cost-management.md): Attribute, forecast and control what the data platform costs, and recover it from the teams and products that use it.
- [Privacy rights handling](../use-cases/usecase-privacy-rights.md): Find, report and erase an individual's data across the estate within legal deadlines.
- [Real-time fraud detection](../use-cases/usecase-fraud-detection.md): Score transactions in milliseconds and block or flag suspicious ones.
- [Security and log analytics](../use-cases/usecase-security-log-analytics.md): Collect and analyse large volumes of logs to detect threats and investigate incidents.
- [Self-service BI](../use-cases/usecase-self-service-bi.md): Analysts and business users explore governed data and build their own reports with trusted metrics.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
- [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md): Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.

# Frameworks they work with

- [DORA (Digital Operational Resilience Act)](../frameworks/framework-eu-dora.md): Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.
- [Data mesh principles](../frameworks/framework-data-mesh.md): Four principles for decentralising analytical data ownership to business domains while keeping data interoperable and governed.
- [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md): A five-level model from Microsoft that describes MLOps maturity across people, model creation, model release and application integration.
