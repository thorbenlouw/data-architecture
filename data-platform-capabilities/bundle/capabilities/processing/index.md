# Processing and transformation

* [Processing and transformation](processing.md) - Transform, clean, join and aggregate data into forms ready for use.
  * [AI functions in SQL](ai-functions.md) - Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
  * [Data enrichment](data-enrichment.md) - Add attributes to records from lookup tables or curated third-party reference data.
  * [DataFrame APIs](dataframe-apis.md) - Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
  * [Declarative pipelines](declarative-pipelines.md) - Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
  * [Distributed processing](distributed-processing.md) - Process large datasets in parallel across a cluster of machines.
  * [Document processing](document-processing.md) - Extract text, tables and fields from documents such as PDFs, scans and images.
  * [Edge data processing](edge-data-processing.md) - Filter, transform and buffer data on devices or sites before it reaches the platform, tolerating disconnection.
  * [Incremental processing](incremental-processing.md) - Process only new or changed data instead of recomputing everything each run.
  * [Low-code transformation](low-code-transformation.md) - Build transformation logic visually from configurable components rather than writing code.
  * [Self-service data preparation](data-preparation.md) - Let analysts profile, clean and reshape data interactively without engineering help.
  * [Single-node processing](single-node-processing.md) - Process small to medium datasets quickly on one machine using in-process engines.
  * [SQL transformation](sql-transformation.md) - Transform data inside the platform using SQL, typically after it has been loaded.
    * [Transformation as code](transformation-as-code.md) - Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
  * [Stream processing](stream-processing.md) - Transform, join and aggregate events continuously as they arrive, keeping state across events.
    * [Event-time windowing](event-time-windowing.md) - Group events into time windows by when they happened, handling late and out-of-order data.
    * [Streaming SQL](streaming-sql.md) - Express continuous transformations and incrementally maintained views over streams in SQL.
  * [User-defined functions and procedures](user-defined-functions.md) - Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.
