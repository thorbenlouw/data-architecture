# Ingestion and integration

* [Ingestion and integration](ingestion-integration.md) - Bring data from source systems into the platform and keep it in step with them.
  * [Application integration](application-integration.md) - Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
  * [B2B and EDI integration](b2b-edi-integration.md) - Exchange structured business documents such as orders and invoices with trading partners using EDI standards.
  * [Batch ingestion](batch-ingestion.md) - Load data from sources on a schedule or on demand, in bulk or incrementally.
    * [API ingestion](api-ingestion.md) - Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.
    * [Bulk and offline transfer](bulk-data-transfer.md) - Move very large datasets into the platform over high-throughput links or physical transfer devices.
    * [Database extraction](database-extraction.md) - Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
    * [File ingestion](file-ingestion.md) - Detect and load files arriving in landing storage, processing each file exactly once.
    * [SaaS application connectors](saas-connectors.md) - Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
  * [Change data capture](change-data-capture.md) - Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
  * [Custom connector development](custom-connectors.md) - Build and run connectors for sources with no prebuilt option, using an SDK or framework.
  * [Database replication and mirroring](database-replication.md) - Replicate operational databases continuously into the analytical platform without building pipelines.
  * [Deduplication and idempotent loading](idempotent-loading.md) - Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.
  * [Event streaming](event-streaming.md) - Publish and subscribe to durable, ordered and replayable streams of events between systems.
  * [Mainframe data integration](mainframe-integration.md) - Capture and offload data from mainframe databases and files with minimal load on the host.
  * [Managed file transfer](managed-file-transfer.md) - Exchange files securely with partners over SFTP, FTPS or AS2, with tracking and retries.
  * [Message queuing](message-queuing.md) - Distribute messages to competing consumers with per-message acknowledgement and redelivery.
  * [Streaming ingestion](streaming-ingestion.md) - Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
    * [Behavioural event collection](behavioural-event-collection.md) - Collect clickstream and product events from web, mobile and server SDKs and validate them against a tracking plan.
    * [IoT and telemetry ingestion](iot-ingestion.md) - Collect high-volume telemetry securely from devices and edge gateways.
    * [Stream-to-table materialisation](stream-to-table.md) - Expose event-stream topics directly as open-format tables, with schema mapping, compaction and catalogue registration handled for you.
  * [Unstructured data ingestion](unstructured-ingestion.md) - Bring documents, images, audio and other unstructured content into the platform together with their metadata.

# Also part of this domain

* [Edge data processing](../processing/edge-data-processing.md) (main home: Processing and transformation) - Filter, transform and buffer data on devices or sites before it reaches the platform, tolerating disconnection.
