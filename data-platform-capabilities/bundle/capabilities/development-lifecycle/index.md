# Development and DataOps

* [Development and DataOps](development-lifecycle.md) - Build, test and release data and AI workloads safely and repeatably, from first commit to production.
  * [AI-assisted development](ai-assisted-development.md) - Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
    * [Data engineering agents](data-engineering-agents.md) - Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.
  * [CI/CD](ci-cd.md) - Build, test and deploy pipelines, models and infrastructure automatically on every change.
  * [Data application hosting](data-applications.md) - Build and host interactive data applications next to the data, under platform security.
  * [Data modelling and design](data-modelling.md) - Design and document conceptual, logical and physical data models, and keep them in step with what is deployed.
  * [Data pipeline testing](data-testing.md) - Test transformation logic and data with unit, integration and regression tests before release.
  * [Environment promotion](environment-promotion.md) - Promote the same artefacts through development, test and production with environment-specific configuration.
  * [Ephemeral development environments](ephemeral-environments.md) - Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.
  * [IDE and local development](local-development.md) - Develop in your own editor and run against the platform, with debugging and local tests.
  * [Notebooks](notebooks.md) - Develop interactively with code, results and narrative together, with collaboration and scheduling.
  * [Runtime and environment management](runtime-management.md) - Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.
  * [Schema change management](schema-change-management.md) - Version and apply database schema changes through controlled migrations.
  * [Test data management](test-data-management.md) - Provide realistic, safe data for development and testing through subsetting, masking or generation.
    * [Synthetic data generation](synthetic-data.md) - Generate artificial data that keeps the useful properties of real data without exposing real records.
  * [Version control integration](version-control.md) - Keep code and configuration in Git and work with branches from inside the platform.

# Also part of this domain

* [CI/CD for machine learning](../mlops/ml-cicd.md) (main home: ML operations) - Test and promote model code, pipelines and models through environments automatically.
* [Zero-copy cloning](../storage/zero-copy-cloning.md) (main home: Storage and table management) - Create an instant copy of a table, schema or database that shares storage with the original until either changes.
