---
type: Capability
id: ai-content-provenance
title: AI content marking and provenance
description: Mark AI-generated content in machine-readable form and detect such marks so synthetic content can be identified.
aliases: [watermarking, C2PA]
broader: [generative-ai, ai-governance]
related: [compliance-evidence, unstructured-lineage]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Two mechanisms work together. Watermarking embeds a signal in the content itself, such as a statistical pattern in word choice or an imperceptible change to pixels or audio, which a detector can recognise later. Provenance metadata attaches a signed record to a file describing how it was created and edited; the C2PA standard, shown to users as Content Credentials, is the main open format. For example, a marketing team's generated product images carry C2PA records naming the model used, and a news organisation's verification tool reads them before publication.

It matters for transparency obligations, such as the EU AI Act's requirement that providers of generative systems mark synthetic output in a machine-readable, detectable way, and for trust in published media. Both mechanisms have limits. Metadata is stripped by screenshots and re-encoding; image and audio watermarks survive some edits but not all; text watermarks are weak. Detecting unmarked synthetic content relies on unreliable classifiers. Lineage traces how outputs were produced inside your systems; marking travels with the content once it leaves.

# Key considerations

- Marks are easily lost. Combine signed metadata with watermarks where durability matters.
- Decide which outputs to mark. Images, audio and video are well supported; text is harder and often handled with visible disclosure instead.
- Check whether your model providers already watermark output and whether you can verify their marks.
- Signing provenance records needs managed signing keys and a list of trusted signers.

# Questions to ask

- Which generated content is published externally or used as evidence?
- Do regulations in your markets require marking or disclosure of AI-generated content?
- Do you need to check incoming content, such as claim photos or identity documents, for synthetic origin?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md), [AI governance](../governance/ai-governance.md) |
| Related | [Compliance controls and evidence](../governance/compliance-evidence.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md) |

# Where it appears

- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 4, Measured) · [Generative AI](../../maturity/track-genai.md) (from level 4, Measured)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 50 – Transparency obligations · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): Generative AI Profile (NIST AI 600-1)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock](../../technologies/aws/aws-bedrock.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure OpenAI in Foundry Models](../../technologies/microsoft/azure-openai.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Gemini models on Agent Platform](../../technologies/google-cloud/gcp-gemini-models.md) |
