---
type: Technology
id: lance
title: Lance
description: Columnar data format and table format for AI and multimodal data, with fast random access, versioning and built-in vector indexes.
aliases: [Lance format]
platform: platform-open-source
kind: open-source
availability: ga
realises: [multimodal-data-formats, vector-search, data-versioning, columnar-storage]
resource: https://github.com/lancedb/lance
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, led by LanceDB. Stores images, video and embeddings with tabular columns. Used for ML training and retrieval datasets where Parquet's random access is too slow.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multimodal data formats](../../capabilities/storage/multimodal-data-formats.md) (Storage and table management) (primary): Store images, audio, video and embeddings together with tabular columns in formats built for fast random access.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Data versioning](../../capabilities/storage/data-versioning.md) (Storage and table management): Keep and reference past versions of data so you can reproduce results, compare changes or roll back.
- [Columnar storage](../../capabilities/storage/columnar-storage.md) (Storage and table management): Store data column by column with compression and statistics so analytical queries read only what they need.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga
