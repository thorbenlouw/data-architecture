---
type: Use Case
id: usecase-iot-predictive-maintenance
title: IoT predictive maintenance
description: Analyse sensor telemetry to predict equipment failures before they happen.
aliases: [condition monitoring, asset health]
requires:
- {capability: iot-ingestion, level: 3, why: Telemetry from thousands of devices must be collected securely at high frequency.}
- {capability: edge-data-processing, level: 2, why: Sites with poor connectivity must filter and buffer data locally and send it when links return.}
- {capability: network-security, level: 3, why: Traffic from operational technology networks into the platform must be tightly controlled.}
- {capability: time-series-data, level: 3, why: Large volumes of time-stamped measurements are stored and queried by asset and time range.}
- {capability: event-time-windowing, level: 3, why: Readings arrive late and out of order and must be aggregated by when they were measured.}
- {capability: stream-processing, level: 2, why: Features and simple threshold alerts are computed continuously from telemetry.}
- {capability: storage-tiering, level: 2, why: Years of raw high-frequency data must be kept affordably for training.}
- {capability: data-quality-rules, level: 2, why: 'Flat-lining, out-of-range and drifting sensors must be detected so they do not look like equipment faults.'}
- {capability: hierarchy-management, level: 2, why: 'Readings must be tied to the right asset in the site, line, asset and component hierarchy.'}
- {capability: data-labelling, level: 2, why: Failure events from maintenance records must be turned into reliable labels.}
- {capability: feature-engineering, level: 2, why: 'Raw signals are turned into features such as trends, frequency bands and operating states.'}
- {capability: model-training, level: 2, why: Models are trained per equipment type on telemetry and failure history.}
- {capability: streaming-inference, level: 2, why: Equipment is scored as telemetry arrives so fast-developing faults are caught.}
- {capability: drift-detection, level: 2, why: 'Sensor replacement, recalibration and new operating conditions change the inputs.'}
- {capability: application-integration, level: 2, why: Predictions must raise work orders in the maintenance system to be acted on.}
benefits_from:
- {capability: pretrained-predictive-models, why: Pretrained anomaly and forecasting models help where failure history is scarce.}
- {capability: data-anomaly-detection, why: Spots unexpected changes in telemetry without hand-written rules.}
- {capability: real-time-analytics, why: Lets engineers explore recent telemetry interactively.}
- {capability: geospatial-data, why: Adds location for fleets and distributed networks.}
- {capability: model-explainability, why: Shows engineers which signals drove an alert.}
- {capability: knowledge-graphs, why: Models asset structure and dependencies for root-cause analysis.}
- {capability: model-performance-monitoring, why: Compares predictions with actual failures as they occur.}
- {capability: edge-inference, why: Scores equipment on site where links are unreliable or a fault must stop a machine within milliseconds.}
personas:
- persona-data-scientist
- persona-ml-engineer
- persona-data-engineer
- persona-platform-engineer
- persona-business-user
patterns: [lambda-architecture, kappa-architecture, medallion-architecture, fti-pipelines]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Unplanned failures of machines, vehicles, turbines or network equipment are expensive, and fixed maintenance schedules replace parts that still had life in them. Predictive maintenance uses sensor telemetry such as vibration, temperature, pressure and current to spot signs of wear and predict failure early enough to plan an intervention. Data is collected from devices and site gateways, often over unreliable links, stored as time series, combined with maintenance records that provide failure labels, and fed to models that score equipment continuously or in frequent batches and raise work orders.

Good looks like failures predicted with enough lead time to schedule repair, false alarms low enough that engineers keep trusting the alerts, predictions arriving in the maintenance system rather than on a separate dashboard, and sensor faults told apart from equipment faults.

# Non-functional requirements

- Ingestion from thousands to millions of sensors at intervals from sub-second to minutes.
- Edge buffering covers connectivity loss of hours to days without data loss.
- Alerts for fast-developing faults within minutes, and predictions days or weeks ahead for planned repair.
- Raw data kept for months and downsampled data for years.

# Risks

- Too few recorded failures to train on, especially for reliable equipment.
- False alarms from sensor faults cause alert fatigue and engineers stop responding.
- Predictions stay on a dashboard and never reach the maintenance workflow.
- Models trained on one site do not transfer to others with different operating conditions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Telemetry from thousands of devices must be collected securely at high frequency. |
| [Edge data processing](../capabilities/processing/edge-data-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 2 (Managed) | Sites with poor connectivity must filter and buffer data locally and send it when links return. |
| [Network security](../capabilities/security/network-security.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Traffic from operational technology networks into the platform must be tightly controlled. |
| [Time-series data](../capabilities/specialised-data/time-series-data.md) | [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 3 (Defined) | Large volumes of time-stamped measurements are stored and queried by asset and time range. |
| [Event-time windowing](../capabilities/processing/event-time-windowing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 3 (Defined) | Readings arrive late and out of order and must be aggregated by when they were measured. |
| [Stream processing](../capabilities/processing/stream-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 2 (Managed) | Features and simple threshold alerts are computed continuously from telemetry. |
| [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) | [Storage and table management](../capabilities/storage/storage.md) | 2 (Managed) | Years of raw high-frequency data must be kept affordably for training. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 2 (Managed) | Flat-lining, out-of-range and drifting sensors must be detected so they do not look like equipment faults. |
| [Hierarchy management](../capabilities/master-data/hierarchy-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 2 (Managed) | Readings must be tied to the right asset in the site, line, asset and component hierarchy. |
| [Data labelling](../capabilities/machine-learning/data-labelling.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Failure events from maintenance records must be turned into reliable labels. |
| [Feature engineering](../capabilities/machine-learning/feature-engineering.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Raw signals are turned into features such as trends, frequency bands and operating states. |
| [Model training](../capabilities/machine-learning/model-training.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Models are trained per equipment type on telemetry and failure history. |
| [Streaming inference](../capabilities/mlops/streaming-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | 2 (Managed) | Equipment is scored as telemetry arrives so fast-developing faults are caught. |
| [Drift detection](../capabilities/mlops/drift-detection.md) | [ML operations](../capabilities/mlops/mlops.md) | 2 (Managed) | Sensor replacement, recalibration and new operating conditions change the inputs. |
| [Application integration](../capabilities/ingestion-integration/application-integration.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Predictions must raise work orders in the maintenance system to be acted on. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md) | Pretrained anomaly and forecasting models help where failure history is scarce. |
| [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md) | Spots unexpected changes in telemetry without hand-written rules. |
| [Real-time analytical database](../capabilities/compute/real-time-analytics.md) | Lets engineers explore recent telemetry interactively. |
| [Geospatial data](../capabilities/specialised-data/geospatial-data.md) | Adds location for fleets and distributed networks. |
| [Model explainability](../capabilities/machine-learning/model-explainability.md) | Shows engineers which signals drove an alert. |
| [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) | Models asset structure and dependencies for root-cause analysis. |
| [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | Compares predictions with actual failures as they occur. |
| [Edge inference](../capabilities/mlops/edge-inference.md) | Scores equipment on site where links are unreliable or a fault must stop a machine within milliseconds. |

# Personas

- [Data scientist](../personas/persona-data-scientist.md): Explores data and builds statistical and machine learning models.
- [ML engineer](../personas/persona-ml-engineer.md): Takes models to production and keeps them running reliably.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.

# Patterns

- [Lambda architecture](../patterns/lambda-architecture.md)
- [Kappa architecture](../patterns/kappa-architecture.md)
- [Medallion architecture](../patterns/medallion-architecture.md)
- [Feature, training and inference pipelines](../patterns/fti-pipelines.md)

# Frameworks that apply

- [EU Data Act](../frameworks/framework-eu-data-act.md): Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.
- [ISO 8000 (data quality)](../frameworks/framework-iso-8000.md): A series of international standards on data quality, covering concepts, quality management processes, profiling, rules, master data exchange and sensor data.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 12 of 15 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Drift detection](../capabilities/mlops/drift-detection.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 14 of 15 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 12 of 15 | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 9 of 15 | [Edge data processing](../capabilities/processing/edge-data-processing.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Stream processing](../capabilities/processing/stream-processing.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
| [Databricks](../platforms/platform-databricks.md) | 9 of 15 | [Edge data processing](../capabilities/processing/edge-data-processing.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 4 of 15 | [Edge data processing](../capabilities/processing/edge-data-processing.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Stream processing](../capabilities/processing/stream-processing.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model training](../capabilities/machine-learning/model-training.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Informatica](../platforms/platform-informatica.md) | 4 of 15 | [Edge data processing](../capabilities/processing/edge-data-processing.md), [Network security](../capabilities/security/network-security.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Stream processing](../capabilities/processing/stream-processing.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model training](../capabilities/machine-learning/model-training.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Drift detection](../capabilities/mlops/drift-detection.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 5 of 15 | [Network security](../capabilities/security/network-security.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Oracle](../platforms/platform-oracle.md) | 3 of 15 | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [SAP](../platforms/platform-sap.md) | 4 of 15 | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Network security](../capabilities/security/network-security.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Stream processing](../capabilities/processing/stream-processing.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model training](../capabilities/machine-learning/model-training.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Drift detection](../capabilities/mlops/drift-detection.md) |
| [Teradata](../platforms/platform-teradata.md) | 4 of 15 | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Network security](../capabilities/security/network-security.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Stream processing](../capabilities/processing/stream-processing.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [IBM](../platforms/platform-ibm.md) | 5 of 15 (+1 in preview) | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Network security](../capabilities/security/network-security.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) (preview only) |
| [Palantir](../platforms/platform-palantir.md) | 4 of 15 | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Network security](../capabilities/security/network-security.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [SAS](../platforms/platform-sas.md) | 7 of 15 | [Network security](../capabilities/security/network-security.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Dataiku](../platforms/platform-dataiku.md) | 4 of 15 | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Network security](../capabilities/security/network-security.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Stream processing](../capabilities/processing/stream-processing.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 9 of 15 | [Network security](../capabilities/security/network-security.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Independent vendors](../platforms/platform-independent.md) | 7 of 15 | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Network security](../capabilities/security/network-security.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Streaming inference](../capabilities/mlops/streaming-inference.md) |
