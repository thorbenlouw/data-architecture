# Machine learning development

* [Machine learning development](machine-learning.md) - Develop, train and evaluate machine learning models on platform data.
  * [Data labelling](data-labelling.md) - Create and manage labelled examples for supervised learning, using people, rules or models.
  * [Experiment tracking](experiment-tracking.md) - Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
  * [Feature engineering](feature-engineering.md) - Turn raw data into model inputs in reusable, consistent pipelines.
  * [Feature store](feature-store.md) - Manage features centrally so they are reused, documented and served consistently for training and inference.
    * [Offline feature store](offline-feature-store.md) - Store historical feature values for model training and batch scoring.
    * [Online feature store](online-feature-store.md) - Serve the latest feature values to models in milliseconds.
    * [Point-in-time correct joins](point-in-time-joins.md) - Join features as they were known at each training example's timestamp, preventing leakage of future data.
  * [In-database machine learning](in-database-ml.md) - Train and run models using SQL inside the data platform.
  * [ML pipelines](ml-pipelines.md) - Automate the steps from data preparation to training and evaluation as repeatable pipelines.
  * [Model evaluation](model-evaluation.md) - Assess models against holdout data, baselines and business criteria before release.
    * [Bias and fairness assessment](fairness-assessment.md) - Measure whether a model's outcomes differ unfairly across groups of people.
    * [Model explainability](model-explainability.md) - Explain which inputs drive a model's predictions, overall and for individual predictions.
  * [Model registry](model-registry.md) - Version, document and manage the lifecycle of trained models from candidate to production.
  * [Model training](model-training.md) - Train models on platform data at the scale required, from single machines to GPU clusters.
    * [AutoML](automl.md) - Try features, algorithms and settings automatically to produce a good baseline model with little code.
    * [Distributed training](distributed-training.md) - Split training across many machines or GPUs to handle large models or datasets.
    * [Hyperparameter tuning](hyperparameter-tuning.md) - Search automatically for the model settings that perform best.
  * [Pretrained predictive models](pretrained-predictive-models.md) - Forecast, classify or detect anomalies on business tables with pretrained models, without training a model for each use case.
  * [Training and evaluation dataset management](training-dataset-management.md) - Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

# Also part of this domain

* [Runtime and environment management](../development-lifecycle/runtime-management.md) (main home: Development and DataOps) - Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.
