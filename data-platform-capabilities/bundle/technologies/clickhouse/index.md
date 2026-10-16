# ClickHouse

# Ingestion and integration

* [ClickHouse Kafka table engine](clickhouse-kafka-engine.md) - Table engine that consumes Kafka topics as a consumer group and, with a materialised view, writes messages continuously into MergeTree tables; RabbitMQ and NATS engines work the same way.
* [ClickPipes](clickhouse-clickpipes.md) - Managed ingestion service in ClickHouse Cloud that runs continuous or one-off pipes from streaming platforms and object storage into ClickHouse tables, with scaling separate from the database.
* [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](clickhouse-clickpipes-cdc.md) - ClickPipes connectors that take an initial snapshot of source tables and then replicate inserts, updates and deletes from Postgres, MySQL or MongoDB logs into ClickHouse, plus a BigQuery connector for bulk and incremental loads.
* [S3Queue and AzureQueue table engines](clickhouse-s3queue.md) - Table engines that watch an S3 or Azure Blob path and load new files in the background through a materialised view, tracking which files have been processed in Keeper.

# Storage and table management

* [ClickHouse DataLakeCatalog database engine](clickhouse-datalakecatalog.md) (preview) - Database engine that connects to an external lakehouse catalogue and exposes its tables as ClickHouse tables for querying and joining.
* [ClickHouse JSON, Dynamic and Variant data types](clickhouse-json-types.md) - Column types that store semi-structured JSON as typed sub-columns per path, and values whose type varies from row to row, without flattening them first.
* [ClickHouse lightweight updates and deletes](clickhouse-lightweight-updates-deletes.md) - Changes or removes individual rows in MergeTree tables by writing small patch parts or a deleted-row mask that queries apply at once, instead of rewriting whole parts.
* [MergeTree table engine family](clickhouse-mergetree.md) - Core storage engines that write sorted, compressed column parts, merge them in the background, and index them with a sparse primary index, with variants that deduplicate, sum, aggregate or collapse rows during merges.

# Processing and transformation

* [chDB](clickhouse-chdb.md) - In-process OLAP engine built on ClickHouse that runs inside Python, Go, Rust, Node.js or C/C++ programs, with a pandas-compatible DataStore API.
* [ClickHouse AI functions](clickhouse-ai-functions.md) (preview) - SQL functions such as aiGenerate, aiClassify, aiExtract, aiTranslate, aiRedact and aiEmbed that call an LLM or embedding endpoint for each row.
* [ClickHouse user-defined functions](clickhouse-udfs.md) - Extends ClickHouse with SQL lambda functions, executable functions that call external scripts such as Python over standard input and output, and experimental WebAssembly functions.
* [clickhouse-local](clickhouse-local.md) - Mode of the ClickHouse binary that runs SQL over local or remote files and piped data without starting a server.
* [dbt-clickhouse adapter](clickhouse-dbt.md) (preview) - ClickHouse-supported dbt adapter that builds views, tables, incremental and microbatch models, materialised views and dictionaries in ClickHouse.

# Query and compute

* [ClickHouse Cloud](clickhouse-cloud.md) - Fully managed ClickHouse on AWS, GCP and Azure that stores data in object storage and scales, idles and upgrades services automatically.
* [ClickHouse Cloud Warehouses (compute-compute separation)](clickhouse-warehouses.md) - Groups several Cloud services with their own replicas and endpoints over the same data, so ingestion, reporting and ad hoc workloads can run on separately sized compute.
* [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](clickhouse-data-lake.md) - Table functions and engines that query Apache Iceberg, Delta Lake, Apache Hudi and Apache Paimon tables in object storage, with Iceberg time travel and the ability to create and insert into Iceberg tables.
* [ClickHouse data skipping indexes](clickhouse-skipping-indexes.md) - Per-block minmax, set and Bloom filter indexes that let queries skip granules which cannot match a filter, after the primary index has pruned data.
* [ClickHouse dictionaries](clickhouse-dictionaries.md) - In-memory key-value lookups loaded from ClickHouse tables, external databases, HTTP or files, refreshed on a set lifetime and queried with dictGet functions or as tables.
* [ClickHouse incremental materialized views](clickhouse-materialized-views.md) - Insert triggers that run a query over each newly inserted block and write the results to a target table, usually an AggregatingMergeTree or SummingMergeTree that merges partial aggregates.
* [ClickHouse integration table engines and table functions](clickhouse-integration-engines.md) - Engines and functions such as postgresql, mysql, mongodb, s3, url, jdbc, odbc and arrowflight that read from and write to external databases and storage directly in SQL.
* [ClickHouse projections](clickhouse-projections.md) - Hidden, automatically maintained copies of a table with a different sort order or pre-aggregation that the optimiser picks when they reduce the data read.
* [ClickHouse query cache](clickhouse-query-cache.md) - Stores the results of SELECT queries in memory, or optionally on disk, and serves repeats until a time to live expires.
* [ClickHouse refreshable materialized views](clickhouse-refreshable-materialized-views.md) - Views that rerun a full query on a schedule and replace or append to a target table, with optional dependencies between views.
* [ClickHouse server](clickhouse-server.md) - Open-source column-oriented SQL database that runs analytical queries over very large tables with vectorised, parallel execution on single servers or sharded and replicated clusters.
* [ClickHouse workload scheduling](clickhouse-workload-scheduling.md) - Divides CPU, disk I/O, memory and query slots between a hierarchy of SQL-defined workloads using priorities, weights and limits.
* [SharedMergeTree](clickhouse-sharedmergetree.md) - Cloud-native counterpart of the MergeTree family that keeps table data and metadata in shared object storage and coordinates replicas through Keeper instead of copying data between them.

# Serving and activation

* [ClickHouse Cloud Query API Endpoints](clickhouse-query-api-endpoints.md) - Turns a saved, parameterised SQL query in the Cloud console into an authenticated HTTP endpoint that returns results in any ClickHouse format.
* [ClickHouse interfaces and client drivers](clickhouse-clients.md) - HTTP, native TCP, gRPC and Arrow Flight interfaces, MySQL and PostgreSQL wire-protocol compatibility, and official clients including JDBC, ODBC, ADBC, Python, Go, Node.js, Rust, C++ and .NET.
* [ClickHouse Managed Postgres](clickhouse-managed-postgres.md) (preview) - Managed PostgreSQL on local NVMe storage with high availability, read replicas and point-in-time recovery, wired to ClickHouse through built-in CDC and the pg_clickhouse extension.

# Analytics and BI

* [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](clickhouse-sql-console.md) - Browser workspace for writing and sharing queries, charting results, building parameterised dashboards from saved queries and asking an AI assistant to write SQL or explore data.
* [ClickHouse data source plugin for Grafana](clickhouse-grafana-plugin.md) - Signed Grafana data source with a query builder for building dashboards and exploring logs and traces stored in ClickHouse.

# Generative AI

* [ClickHouse Agents](clickhouse-agents.md) (preview) - Managed agent service in ClickHouse Cloud with a chat interface, no-code agent builder, skills, memory, sandboxed code execution and MCP tool access, using Claude models by default.
* [ClickHouse MCP server (open-source and Remote MCP in Cloud)](clickhouse-mcp-server.md) - Model Context Protocol servers that let AI assistants list ClickHouse databases and tables and run read-only queries, including a managed remote endpoint for ClickHouse Cloud.
* [ClickHouse vector similarity indexes](clickhouse-vector-search.md) - HNSW indexes on embedding columns for approximate nearest-neighbour search with L2, cosine or dot-product distance, alongside exact brute-force search and the QBit type.
* [Langfuse](clickhouse-langfuse.md) - LLM engineering platform that traces model and agent calls, runs evaluations and experiments on datasets, and versions prompts, available self-hosted or as Langfuse Cloud.

# Governance and compliance

* [ClickHouse TTL (time to live)](clickhouse-ttl.md) - Table and column rules that delete, roll up, recompress or move data once it reaches a given age, applied during background merges.

# Security and access

* [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](clickhouse-access-control.md) - SQL-managed access entities that grant privileges to roles, filter rows per user, mask column values per user, and cap settings and resource use per user or role.
* [ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)](clickhouse-private-link.md) - Connects ClickHouse Cloud services and ClickPipes to customer virtual networks over the cloud providers' private endpoint services, and restricts public access with IP filters.
* [ClickHouse Cloud TDE and customer-managed encryption keys (CMEK)](clickhouse-cmek.md) - Adds database-level encryption to Cloud services and lets the customer supply and rotate the wrapping key in AWS KMS, GCP KMS or Azure Key Vault.

# Platform operations

* [ClickHouse BYOC (Bring Your Own Cloud)](clickhouse-byoc.md) - Runs the ClickHouse Cloud data plane, including clusters, data and backups, inside the customer's own cloud account while ClickHouse operates the control plane.
* [ClickHouse Cloud backups and BACKUP/RESTORE](clickhouse-backups.md) - Scheduled Cloud backups restored to a new service, and SQL BACKUP and RESTORE statements that write full or incremental backups to disk, S3 or Azure in self-managed clusters.
* [ClickHouse Cloud usage breakdown and spend alerts](clickhouse-cost-controls.md) - Console usage breakdown by service and cost category, a usage cost API, and organisation spend alerts at set thresholds of committed or budgeted spend.
* [ClickHouse Keeper](clickhouse-keeper.md) - Raft-based coordination service, compatible with the ZooKeeper client protocol, that coordinates replication, distributed DDL and queue engines.
* [ClickHouse Query Insights and system tables](clickhouse-cloud-monitoring.md) - Console views of query volume, latency and errors built on system.query_log, alongside system tables, Cloud monitoring dashboards and Prometheus endpoints that expose server, query and ClickPipes metrics.
* [ClickHouse Terraform provider](clickhouse-terraform.md) - Official Terraform provider for ClickHouse Cloud services, scaling, private endpoints, organisation roles and API keys, ClickPipes, ClickStack resources and Managed Postgres.

# Specialised data types

* [ClickHouse geo data types and functions](clickhouse-geo.md) - Point, polygon and line types plus functions for great-circle distances, point-in-polygon tests, geohash, H3 and S2 indexing and Mapbox vector tile encoding.
* [ClickHouse text indexes (full-text search)](clickhouse-text-indexes.md) - Inverted indexes on string, array and map columns with configurable tokenisers that answer token, phrase and pattern searches without scanning.
* [ClickHouse TimeSeries table engine](clickhouse-timeseries.md) (preview) - Experimental engine that stores Prometheus-style metrics as samples, tags and metric tables and accepts Prometheus remote-write and remote-read traffic.
* [ClickStack](clickhouse-clickstack.md) - Observability stack that combines the HyperDX UI, a preconfigured OpenTelemetry collector and ClickHouse to store and search logs, traces, metrics and session replays, with dashboards and alerts.
