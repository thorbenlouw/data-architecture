# Storage and table management

* [Storage and table management](storage.md) - Store data durably and cheaply in formats that many tools can read and manage it as reliable tables.
  * [Data versioning](data-versioning.md) - Keep and reference past versions of data so you can reproduce results, compare changes or roll back.
    * [Data branching and tagging](data-branching.md) - Create isolated branches and named tags of data, Git-style, to develop and test changes before merging them.
    * [Time travel](time-travel.md) - Query or restore a table as it was at an earlier point in time or version.
    * [Zero-copy cloning](zero-copy-cloning.md) - Create an instant copy of a table, schema or database that shares storage with the original until either changes.
  * [Object storage](object-storage.md) - Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
    * [File-system access to object storage](object-file-access.md) - Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.
    * [Storage tiering and lifecycle](storage-tiering.md) - Move data between hot, cool and archive tiers automatically based on age or access patterns.
  * [Open file formats](file-formats.md) - Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.
    * [Columnar storage](columnar-storage.md) - Store data column by column with compression and statistics so analytical queries read only what they need.
    * [Multimodal data formats](multimodal-data-formats.md) - Store images, audio, video and embeddings together with tabular columns in formats built for fast random access.
  * [Open table formats](open-table-formats.md) - Manage collections of files as transactional tables with a defined schema, history and metadata.
    * [ACID transactions](acid-transactions.md) - Commit concurrent writes atomically so readers never see partial or conflicting results.
    * [Row-level updates and deletes](row-level-updates.md) - Update, delete and merge individual rows in large tables efficiently.
    * [Schema enforcement and evolution](schema-evolution.md) - Reject data that does not match a table's schema, and change schemas safely over time.
    * [Table format conversion](table-format-conversion.md) - Expose one copy of table data in several table formats by generating or translating metadata.
    * [Table maintenance and optimisation](table-maintenance.md) - Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
  * [Partitioning and clustering](partitioning-clustering.md) - Organise table data by key columns so queries can skip data they do not need.
  * [Platform-managed storage](managed-storage.md) - Let the platform manage table storage layout, compression and durability internally.
  * [Semi-structured data](semi-structured-data.md) - Store and query nested data such as JSON without flattening it first.
  * [Table catalogue](table-catalogue.md) - Register tables, their schemas and storage locations so engines can find, govern and share them.
    * [Catalogue federation](catalogue-federation.md) - Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.
    * [Storage credential vending](credential-vending.md) - Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.
