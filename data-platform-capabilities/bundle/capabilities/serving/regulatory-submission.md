---
type: Capability
id: regulatory-submission
title: Regulatory submission
description: Produce returns in regulator-defined formats and templates, validate them against the regulator's rules and track filing.
aliases: [XBRL filing, regulatory returns, COREP, FINREP, regulatory filing]
broader: [serving, governance]
related: [critical-data-elements, data-reconciliation, manual-adjustments, paginated-reports, column-lineage]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Regulators define what they want to receive, usually as a reporting framework of templates, data point definitions and validation rules, delivered in a format such as XBRL or XML. A submission process maps governed platform data to each template cell or data point, runs the regulator's validation rules, such as checks that totals agree across templates, and generates the file. It then records sign-off, sends the file through the regulator's portal or API, and tracks acknowledgements, rejections and resubmissions.

It applies to periodic returns in banking, insurance, pharmaceuticals, energy and other regulated sectors, and to tax and statistical reporting. Errors bring fines and closer supervision, so firms must show how each reported figure was derived. Approaches range from specialist reporting software whose templates are updated as rules change, to in-house pipelines that produce the files. Unlike paginated reports, which are laid out for people to read, submissions are machine-readable and checked by the receiving authority.

# Key considerations

- Regulators revise templates and validation rules often, sometimes several times a year. Decide who tracks the changes and how quickly mappings and rules are updated.
- Trace each reported value to source data through lineage and reconciliation, so regulator questions can be answered without rebuilding the figure.
- Keep every submitted version with its inputs, sign-off and any resubmissions. You may need to reproduce a return years later.
- Run the regulator's validation rules early in the reporting cycle, not at submission. Failed checks found on deadline day are a common cause of late filing.
- Manual adjustments are routine in regulatory returns. Capture them in a controlled process, not in the final file or a spreadsheet.

# Questions to ask

- Which returns are filed, to which authorities, in which formats and how often?
- How much of each return is assembled by hand in spreadsheets today?
- How are template and rule changes from regulators tracked and put into effect?
- Can you show, for any figure in a past return, where it came from and who approved it?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md), [Governance and compliance](../governance/governance.md) |
| Related | [Approved manual adjustments](../analytics-bi/manual-adjustments.md), [Column-level lineage](../metadata/column-lineage.md), [Critical data elements](../governance/critical-data-elements.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Paginated reports](../analytics-bi/paginated-reports.md) |

# Where it appears

- **Use cases:** [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 4, Measured)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 7 – Accuracy (reporting)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [Workiva](../../technologies/independent/workiva.md) |
