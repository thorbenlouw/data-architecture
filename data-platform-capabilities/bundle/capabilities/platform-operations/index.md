# Platform operations

* [Platform operations](platform-operations.md) - Run the data platform itself, including provisioning, tenancy, cost, monitoring and resilience.
  * [Backup and disaster recovery](business-continuity.md) - Protect against data loss and outages with backups, replication and failover.
    * [Backup and restore](backup-restore.md) - Take point-in-time backups of data and metadata and restore them when needed.
      * [Immutable backups](immutable-backups.md) - Keep backups that nobody can delete or change before they expire, with legal holds, to protect against ransomware.
    * [Cross-region replication and failover](cross-region-failover.md) - Replicate data and configuration to another region and fail over when needed.
    * [Resilience and recovery testing](resilience-testing.md) - Test backup, recovery and failover regularly and record the results as evidence.
  * [Cost management](cost-management.md) - Understand, allocate and control what the platform costs.
    * [AI usage and spend controls](ai-spend-controls.md) - Limit, prioritise and attribute model and agent consumption per user, team or application.
    * [Budgets and spend controls](spend-controls.md) - Set budgets, quotas and alerts, and stop runaway spend automatically.
    * [Cost attribution and chargeback](cost-attribution.md) - Attribute spend to teams, products and workloads using tags and usage data.
    * [Cost optimisation](cost-optimisation.md) - Find and act on savings such as idle compute, oversized clusters and unused data.
    * [Spend forecasting and anomaly detection](cost-forecasting.md) - Project future platform spend from usage trends, commitments and planned workloads, and flag spend that departs from its expected pattern.
  * [Hybrid and multi-cloud deployment](deployment-options.md) - Run the platform across clouds, regions or on-premises, or inside your own cloud account.
    * [Customer-hosted data plane](hybrid-data-plane.md) - Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
  * [Infrastructure as code](infrastructure-as-code.md) - Define platform resources, permissions and configuration as code and apply them automatically.
  * [Multi-tenancy and workspace isolation](multi-tenancy.md) - Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
  * [Platform migration](platform-migration.md) - Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.
    * [Code and SQL translation](code-translation.md) - Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.
    * [Database migration](database-migration.md) - Move databases to new engines or platforms, converting schemas and keeping data in sync until cut-over.
  * [Platform observability](platform-observability.md) - Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
    * [Pipeline monitoring and alerting](pipeline-monitoring.md) - Track pipeline runs, failures and durations, and alert the right people.
    * [Platform incident management](platform-incident-management.md) - Detect, escalate and resolve platform outages and degradations through on-call rotas, runbooks and post-incident reviews.
    * [Query and job performance analysis](query-performance-analysis.md) - Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.
    * [Usage and system telemetry](system-telemetry.md) - Expose platform usage, billing and operational data as queryable tables.
  * [Resource configuration guardrails](configuration-guardrails.md) - Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules.
  * [Self-service provisioning](self-service-provisioning.md) - Let teams create approved workspaces, pipelines and resources from templates without waiting for a central team.
  * [Sustainability and carbon management](sustainability-reporting.md) - Measure and reduce the carbon emissions and energy use of data workloads.

# Also part of this domain

* [Analytical sandboxes](../analytics-bi/analytical-sandboxes.md) (main home: Analytics and BI) - Give analysts and teams governed spaces on the platform where they can upload files, create tables and try out analyses, with quotas, expiry and the platform's access controls.
* [Reserved and committed capacity](../compute/reserved-capacity.md) (main home: Query and compute) - Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.
* [Runtime and environment management](../development-lifecycle/runtime-management.md) (main home: Development and DataOps) - Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.
* [Spot and interruptible compute](../compute/interruptible-compute.md) (main home: Query and compute) - Run fault-tolerant jobs on spare capacity at a large discount, accepting that the provider can reclaim it at short notice.
