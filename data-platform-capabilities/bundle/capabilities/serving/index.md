# Serving and activation

* [Serving and activation](serving.md) - Deliver data to the applications, people and processes that use it, at the latency and volume they need.
  * [Change feeds](change-feeds.md) - Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
  * [Data APIs](data-apis.md) - Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
  * [Data export](data-export.md) - Unload query results or tables to files and external systems in bulk.
  * [Decision management](decision-management.md) - Combine business rules, model scores and policies into automated decisions that are consistent, explainable and audited.
  * [Low-latency serving](low-latency-serving.md) - Serve individual records or small result sets to applications in milliseconds.
  * [Operational data store](operational-data-store.md) - Hold a current, integrated view of data from several operational systems for operational reporting and lookups.
  * [Operational database integration](operational-database.md) - Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
  * [Read-optimised views](read-optimised-views.md) - Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.
  * [Regulatory submission](regulatory-submission.md) - Produce returns in regulator-defined formats and templates, validate them against the regulator's rules and track filing.
  * [Reverse ETL](reverse-etl.md) - Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
    * [Audience building and activation](audience-activation.md) - Build customer audiences from platform data and deliver them to marketing, advertising and service channels.
  * [SQL and programmatic access](sql-access.md) - Connect tools and code to the platform through standard drivers and protocols.

# Also part of this domain

* [Data application hosting](../development-lifecycle/data-applications.md) (main home: Development and DataOps) - Build and host interactive data applications next to the data, under platform security.
* [Online feature store](../machine-learning/online-feature-store.md) (main home: Machine learning development) - Serve the latest feature values to models in milliseconds.
* [Real-time analytical database](../compute/real-time-analytics.md) (main home: Query and compute) - Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
