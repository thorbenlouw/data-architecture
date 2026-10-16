# Query and compute

* [Query and compute](compute.md) - Provide the query engines and processing power that run workloads, sized and isolated appropriately.
  * [Compute provisioning options](compute-options.md) - Choose how compute is supplied, from serverless capacity to clusters you size and control.
    * [Container services](container-services.md) - Run custom containerised applications and services next to the data, inside the platform's security boundary.
    * [GPU and accelerated compute](gpu-compute.md) - Use GPUs or other accelerators for model training, inference and accelerated data processing.
    * [Provisioned compute](provisioned-compute.md) - Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
    * [Reserved and committed capacity](reserved-capacity.md) - Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.
    * [Serverless compute](serverless-compute.md) - Run workloads without managing servers, with capacity allocated on demand and billed by use.
    * [Spot and interruptible compute](interruptible-compute.md) - Run fault-tolerant jobs on spare capacity at a large discount, accepting that the provider can reclaim it at short notice.
  * [Decoupled storage and compute](decoupled-storage-compute.md) - Scale storage and compute independently and let several compute clusters work on the same data.
  * [Elastic scaling](elastic-scaling.md) - Add and remove compute automatically as load changes, including for bursts of concurrent users.
  * [Multi-engine interoperability](engine-interoperability.md) - Let several engines read and write the same tables through open formats and shared catalogues.
  * [Query acceleration](query-acceleration.md) - Speed up repeated or selective queries using caches, precomputed results and indexes.
    * [Approximate query processing](approximate-query-processing.md) - Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.
    * [Indexes and data skipping](data-skipping-indexes.md) - Use indexes, statistics and filters to avoid scanning data that cannot match a query.
    * [Materialised views](materialised-views.md) - Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
    * [Result caching](result-caching.md) - Return results of repeated queries from a cache without recomputing them.
    * [Vectorised native execution](native-execution-acceleration.md) - Speed up engines by running operators in native, vectorised code without changing user code.
  * [Query federation](query-federation.md) - Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
  * [Real-time analytical database](real-time-analytics.md) - Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
  * [SQL query engine](sql-query-engine.md) - Run analytical SQL over large datasets with parallel, optimised execution.
  * [Workload isolation](workload-isolation.md) - Run different workloads on separate compute so one cannot slow or starve another.
  * [Workload management](workload-management.md) - Prioritise, queue and limit queries and jobs so the most important work meets its service levels.

# Also part of this domain

* [Shared compute isolation](../security/compute-user-isolation.md) (main home: Security and access) - Sandbox each user's code on shared compute so nobody can bypass access controls or affect other users.
