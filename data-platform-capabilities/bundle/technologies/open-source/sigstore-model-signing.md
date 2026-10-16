---
type: Technology
id: sigstore-model-signing
title: OpenSSF Model Signing
description: Open specification and library for signing machine learning model files with Sigstore so consumers can check who produced a model and that it has not been altered.
aliases: [model-transparency, OMS, Sigstore model signing]
platform: platform-open-source
kind: open-standard
availability: ga
realises: [ai-supply-chain-security]
resource: https://github.com/sigstore/model-transparency
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Developed under the Open Source Security Foundation (OpenSSF) with Sigstore, and released as version 1.0 in 2025. A signature covers every file in a model directory, so a changed weight or configuration file fails verification. A Kubernetes operator can refuse to load models whose signatures do not verify.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI supply chain security](../../capabilities/security/ai-supply-chain-security.md) (Security and access) (primary): Check third-party models, model files, libraries and tool servers for tampering and malicious code before use, and record what each AI system is built from.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga
