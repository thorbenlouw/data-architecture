---
type: Capability
id: multimodal-data-formats
title: Multimodal data formats
description: Store images, audio, video and embeddings together with tabular columns in formats built for fast random access.
aliases: [Lance, AI data formats]
broader: [file-formats, unstructured-data]
related: [vector-search, model-training, embedding-generation, data-labelling, data-versioning]
depends_on: [object-storage]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

These formats hold large binary values, such as images, audio clips, video frames and embedding vectors, in the same table as ordinary columns like labels, captions and timestamps. Parquet is tuned for scanning whole columns; multimodal formats are built for random access, such as fetching row 1,204,553 and its image quickly, which training data loaders need when they shuffle and sample. Some, such as the open-source Lance format, also allow columns to be added without rewriting existing data, keep versions, and store vector indexes next to the data.

They matter when ML and AI teams would otherwise keep media as millions of loose files plus a separate metadata table, which makes filtering, versioning and governing them hard. Blobs can be stored in standard columnar files, but random reads and wide binary columns perform poorly there. The area is young, so engine support needs checking. There is overlap with vector search: some formats index embeddings in place, but a dedicated vector store may still be needed for low-latency queries.

# Key considerations

- Tool support is narrower than for Parquet. Confirm which query engines, data loaders and catalogues can read the format before committing to it.
- Decide whether blobs live inside the files or as references to objects in storage. Inline blobs keep data and metadata consistent; references keep files small and allow reuse.
- Classification and access tools may not inspect binary content. Images and audio need their own approach to sensitive content.
- Plan deletion across versions: removing one person's images must remove them from older versions and derived indexes too.

# Questions to ask

- Do training or retrieval jobs need random access to individual records, or full sequential scans?
- How are images, audio and video stored and linked to their metadata today?
- Which tools must read the data: SQL engines, ML frameworks, vector search, or all three?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Open file formats](file-formats.md), [Unstructured data management](../specialised-data/unstructured-data.md) |
| Related | [Data labelling](../machine-learning/data-labelling.md), [Data versioning](data-versioning.md), [Embedding generation](../generative-ai/embedding-generation.md), [Model training](../machine-learning/model-training.md), [Vector search](../generative-ai/vector-search.md) |
| Depends on | [Object storage](object-storage.md) |

# Where it appears

- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Lance](../../technologies/open-source/lance.md), [Vortex](../../technologies/open-source/vortex.md) |
