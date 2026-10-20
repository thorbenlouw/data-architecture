---
type: Capability
id: edge-inference
title: Edge inference
description: Run models on devices or local sites close to where data is produced, with updates managed centrally.
aliases: [on-device inference]
broader: [model-deployment]
related:
- edge-data-processing
- iot-ingestion
- streaming-inference
- model-monitoring
- model-release-strategies
depends_on: [model-registry]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The model is packaged for the target hardware, often converted to a compact format such as ONNX or TensorFlow Lite and quantised to fit limited memory, then installed on a camera, vehicle, phone, factory gateway or in-store server. Predictions are made locally, so a camera on a production line can reject a faulty part in milliseconds even when the site's internet link is down. A central service records which model version runs on which device, rolls out updates in stages and collects summaries of inputs and predictions for monitoring.

Edge inference matters when a round trip to the cloud is too slow, sending raw data such as video costs too much bandwidth, connectivity is unreliable, or data must not leave the site. Deployments range from small models on microcontrollers and phones to compact clusters at a local site. It differs from edge data processing, which filters and transforms data before sending it on; edge inference acts on the data where it is produced.

# Key considerations

- Plan for a fleet with mixed hardware and model versions. Track which version runs on each device, and be able to roll back a bad update remotely.
- Compressing a model through quantisation or pruning lowers its accuracy. Evaluate the compressed model on the target hardware, not only the original in the cloud.
- Monitoring is harder when devices are offline or bandwidth is scarce. Decide which inputs, outputs and samples are sent back, how often, and how they are buffered meanwhile.
- Models on devices can be copied or tampered with. Sign model packages, encrypt them at rest and check their integrity before loading.
- Decide what the device does when the model fails or its confidence is low: fall back to a rule, defer to a central service, or ask a person.

# Questions to ask

- What latency, connectivity and bandwidth limits apply where the predictions are needed?
- How many devices and hardware types must be supported and kept up to date?
- Must raw data stay on the device or site for privacy, safety or cost reasons?
- How will outcomes observed at the edge reach the platform so model quality can be measured?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model deployment](model-deployment.md) |
| Related | [Edge data processing](../processing/edge-data-processing.md), [IoT and telemetry ingestion](../ingestion-integration/iot-ingestion.md), [Model monitoring](model-monitoring.md), [Model release strategies](model-release-strategies.md), [Streaming inference](streaming-inference.md) |
| Depends on | [Model registry](../machine-learning/model-registry.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (benefits from)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning online and batch endpoints](../../technologies/microsoft/azure-ml-endpoints.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Container Runtime](../../technologies/sas/sas-container-runtime.md) |
