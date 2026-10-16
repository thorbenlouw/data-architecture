# Patterns

* [Data fabric](data-fabric.md) - Integrate distributed data through a metadata-driven layer that automates discovery, integration and governance across sources.
* [Data lake](data-lake.md) - A store of raw data in open files of any structure, with schema applied when the data is read.
* [Data marts](data-marts.md) - Subject- or department-specific sets of data shaped for one group of users.
* [Data mesh](data-mesh.md) - Decentralise data ownership to business domains that publish data products on a shared self-service platform under federated governance.
* [Data Vault](data-vault.md) - Model integrated history with hubs, links and satellites so new sources can be added without rework.
* [Data warehouse](data-warehouse.md) - A central store of integrated, historical data, modelled for analysis and reporting.
* [Dimensional modelling](dimensional-modelling.md) - Model data as fact tables of measurements surrounded by dimension tables of context.
* [ELT](elt.md) - Extract and load raw data into the platform first, then transform it there.
* [ETL](etl.md) - Extract data, transform it in a separate engine, then load the result into the target.
* [Feature, training and inference pipelines](fti-pipelines.md) - Split an ML system into independent feature, training and inference pipelines that share a feature store and model registry.
* [Kappa architecture](kappa-architecture.md) - Treat all data as streams and rebuild state by replaying the log, using a single processing path.
* [Lakehouse](lakehouse.md) - Warehouse-style tables, transactions and governance on open formats in object storage, shared by many engines.
* [Lambda architecture](lambda-architecture.md) - Run a batch layer and a speed layer in parallel and merge their results for serving.
* [Medallion architecture](medallion-architecture.md) - Organise data in layers of increasing refinement, typically bronze (raw), silver (cleaned) and gold (business-ready).
* [Metadata-driven pipelines](metadata-driven-pipelines.md) - Run one generic ingestion or transformation pipeline driven by control tables that list hundreds of sources and how to load each.
* [One big table](one-big-table.md) - Denormalise data into wide tables to simplify and speed up analytical queries.
* [Separate read models](cqrs-read-models.md) - Separate the models used to write data from models shaped for reading, and keep the read models in sync.
* [Shift-left data quality and governance](shift-left.md) - Move quality checks, contracts and governance controls upstream to where data is produced.
* [Slowly changing dimensions](slowly-changing-dimensions.md) - Track changes to descriptive attributes over time, for example by overwriting values or versioning rows.
* [Transactional outbox](transactional-outbox.md) - Write events to an outbox table in the same transaction as the business change, then publish them reliably.
* [Write-audit-publish](write-audit-publish.md) - Write new data to an isolated location, check it, and only then publish it to consumers.
