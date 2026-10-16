# ML operations

* [ML operations](mlops.md) - Deploy, run, monitor and improve models in production reliably.
  * [CI/CD for machine learning](ml-cicd.md) - Test and promote model code, pipelines and models through environments automatically.
  * [Continuous training](continuous-training.md) - Retrain and redeploy models automatically when data, drift or schedules call for it.
  * [Model deployment](model-deployment.md) - Package and release models into production for batch, real-time or streaming use.
    * [Batch inference](batch-inference.md) - Score large datasets with a model on a schedule.
    * [Edge inference](edge-inference.md) - Run models on devices or local sites close to where data is produced, with updates managed centrally.
    * [Generative model serving](generative-model-serving.md) - Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.
    * [Real-time inference](real-time-inference.md) - Serve predictions through low-latency endpoints.
    * [Streaming inference](streaming-inference.md) - Apply models to events as they flow through a stream.
  * [Model governance](model-governance.md) - Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
  * [Model monitoring](model-monitoring.md) - Track the health of production models, including inputs, outputs, quality and service metrics.
    * [Drift detection](drift-detection.md) - Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
    * [Inference logging](inference-logging.md) - Capture model inputs, outputs and metadata for monitoring, audit and retraining.
    * [Model performance monitoring](model-performance-monitoring.md) - Measure prediction quality over time against ground truth as it arrives.
  * [Model release strategies](model-release-strategies.md) - Reduce release risk by exposing new models, prompts or agent versions gradually, or running them in parallel with the current version.
    * [Canary and A/B testing](canary-ab-testing.md) - Route a share of live traffic to a new model and compare outcomes before full rollout.
    * [Champion-challenger](champion-challenger.md) - Run challenger models alongside the champion and promote a challenger when it proves better.
    * [Shadow deployment](shadow-deployment.md) - Run a new model on live traffic without acting on its outputs, to compare it with the production model.

# Also part of this domain

* [Bias and fairness assessment](../machine-learning/fairness-assessment.md) (main home: Machine learning development) - Measure whether a model's outcomes differ unfairly across groups of people.
* [Model lineage](../metadata/model-lineage.md) (main home: Metadata and discovery) - Track the data, features, code and runs behind each model and its predictions.
