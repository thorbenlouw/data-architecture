---
type: Maturity Track
id: track-path-to-live
title: Path to live
description: How safely, quickly and repeatably changes to data and AI workloads move from a developer's first commit to production.
covers:
- development-lifecycle
- notebooks
- local-development
- version-control
- ci-cd
- environment-promotion
- data-testing
- test-data-management
- synthetic-data
- schema-change-management
- data-modelling
- ai-assisted-development
- data-engineering-agents
- data-applications
- zero-copy-cloning
- ml-cicd
- runtime-management
- ephemeral-environments
related_tracks: [track-mlops, track-transformation, track-platform-self-service]
levels:
- level: 1
  name: Initial
  summary: Changes are made and tested directly in production.
  criteria:
  - Changes are made in production through consoles, notebooks or SQL editors.
  - Code exists only in the platform workspace or on laptops, not in version control.
  - Testing, if any, means running the job and looking at the output.
  capabilities: [notebooks]
- level: 2
  name: Managed
  summary: Code is versioned and reviewed, and a separate development environment exists, but promotion is manual.
  criteria:
  - Pipeline and model code is in Git, and changes are reviewed through pull requests.
  - Developers work in their own editors and run code against a development environment.
  - Promotion from development to production is a manual copy or deployment step.
  - Schema changes are written as ordered migration scripts and checked against documented data models for the main subject areas.
  capabilities: [version-control, local-development, schema-change-management, data-modelling]
- level: 3
  name: Defined
  summary: A standard CI/CD route tests and promotes the same artefacts through environments, using safe test data.
  criteria:
  - CI runs unit tests, linting and data tests on every pull request for pipelines, models and infrastructure.
  - The same artefact moves through development, test and production, with configuration supplied per environment.
  - Test environments get data from masked subsets or zero-copy clones of production, never raw personal data.
  - Interactive data applications are deployed through the same pipeline and run under platform security.
  - Jobs and notebooks declare a pinned runtime version, and a runtime upgrade is tested in CI against the workloads that use it before it reaches production.
  capabilities:
  - ci-cd
  - environment-promotion
  - data-testing
  - test-data-management
  - zero-copy-cloning
  - data-applications
  - runtime-management
- level: 4
  name: Measured
  summary: Delivery is measured with DevOps delivery metrics, each change is tested in its own short-lived environment, and ML and AI-assisted changes go through the same gates.
  criteria:
  - Deployment frequency, lead time for changes, change failure rate and recovery time are measured for data and ML workloads.
  - Each change gets a short-lived environment built from clones or branches of production data, where it runs at production scale and its outputs are compared before release, and the environment is removed on merge.
  - Model and ML pipeline changes pass through CI/CD with automated evaluation gates.
  - Synthetic datasets are checked statistically against the data they imitate and scanned for copied real records.
  - AI coding assistants are available in development tools, and their output goes through the same review and tests as other code.
  capabilities: [ephemeral-environments, ml-cicd, synthetic-data, ai-assisted-development]
- level: 5
  name: Optimising
  summary: Releases are small, frequent and self-correcting, and the delivery process is tuned from its own metrics.
  criteria:
  - Failed post-deployment checks roll a release back automatically.
  - Data engineering agents propose, test and repair pipelines under the same review, permissions and audit as people, and their change failure rate is tracked.
  - Flaky or slow tests are identified from CI history and fixed.
  - Bottlenecks shown by the delivery metrics are reviewed quarterly, and the resulting changes are tracked.
  capabilities: [data-engineering-agents]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means every change to pipelines, models, schemas and infrastructure is versioned, tested against realistic but safe data and promoted through environments automatically, so releases become small, frequent and reversible. At level 4 the DevOps Research and Assessment (DORA) delivery metrics, such as deployment frequency, lead time for changes, change failure rate and recovery time, give measurable targets; this DORA is not the EU resilience regulation of the same name. Typical blockers are production data that cannot be copied to test, changes made directly in production consoles, and tests that check code but not data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Changes are made and tested directly in production.

- Changes are made in production through consoles, notebooks or SQL editors.
- Code exists only in the platform workspace or on laptops, not in version control.
- Testing, if any, means running the job and looking at the output.

**Capabilities first relied on:** [Notebooks](../capabilities/development-lifecycle/notebooks.md)

## Level 2: Managed

Code is versioned and reviewed, and a separate development environment exists, but promotion is manual.

- Pipeline and model code is in Git, and changes are reviewed through pull requests.
- Developers work in their own editors and run code against a development environment.
- Promotion from development to production is a manual copy or deployment step.
- Schema changes are written as ordered migration scripts and checked against documented data models for the main subject areas.

**Capabilities first relied on:** [Version control integration](../capabilities/development-lifecycle/version-control.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md)

## Level 3: Defined

A standard CI/CD route tests and promotes the same artefacts through environments, using safe test data.

- CI runs unit tests, linting and data tests on every pull request for pipelines, models and infrastructure.
- The same artefact moves through development, test and production, with configuration supplied per environment.
- Test environments get data from masked subsets or zero-copy clones of production, never raw personal data.
- Interactive data applications are deployed through the same pipeline and run under platform security.
- Jobs and notebooks declare a pinned runtime version, and a runtime upgrade is tested in CI against the workloads that use it before it reaches production.

**Capabilities first relied on:** [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md), [Data application hosting](../capabilities/development-lifecycle/data-applications.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md)

## Level 4: Measured

Delivery is measured with DevOps delivery metrics, each change is tested in its own short-lived environment, and ML and AI-assisted changes go through the same gates.

- Deployment frequency, lead time for changes, change failure rate and recovery time are measured for data and ML workloads.
- Each change gets a short-lived environment built from clones or branches of production data, where it runs at production scale and its outputs are compared before release, and the environment is removed on merge.
- Model and ML pipeline changes pass through CI/CD with automated evaluation gates.
- Synthetic datasets are checked statistically against the data they imitate and scanned for copied real records.
- AI coding assistants are available in development tools, and their output goes through the same review and tests as other code.

**Capabilities first relied on:** [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md), [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md)

## Level 5: Optimising

Releases are small, frequent and self-correcting, and the delivery process is tuned from its own metrics.

- Failed post-deployment checks roll a release back automatically.
- Data engineering agents propose, test and repair pipelines under the same review, permissions and audit as people, and their change failure rate is tracked.
- Flaky or slow tests are identified from CI history and fixed.
- Bottlenecks shown by the delivery metrics are reviewed quarterly, and the resulting changes are tracked.

**Capabilities first relied on:** [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md)

# Capabilities in scope

[Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md), [AI-assisted development](../capabilities/development-lifecycle/ai-assisted-development.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Data application hosting](../capabilities/development-lifecycle/data-applications.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md), [IDE and local development](../capabilities/development-lifecycle/local-development.md), [Notebooks](../capabilities/development-lifecycle/notebooks.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md), [Test data management](../capabilities/development-lifecycle/test-data-management.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md)

# Related tracks

- [MLOps](track-mlops.md): How automatically and safely models are released, run, monitored and improved in production.
- [Transformation engineering](track-transformation.md): How consistently transformation logic is written, tested, reused and run efficiently, from raw data to tables ready for use.
- [Platform self-service](track-platform-self-service.md): How far teams can obtain, run and observe what they need on the shared platform without waiting for a central team.

Levels follow the shared [maturity scale](maturity-scale.md).
