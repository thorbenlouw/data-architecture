# Contributing

Thank you for improving the map. The rules are in `bundle/about/conventions.md`; this page covers the workflow.

## Set up

```sh
pip install -r requirements.txt
python tools/dpc.py validate
```

## Common changes

| Change | How |
|---|---|
| Fix a fact or wording | Edit the file above the `dpc:generated` line, then `python tools/dpc.py build`. |
| Add a technology | `python tools/dpc.py new technology <id> --title "..." --platform <platform-id> --realises <capability-id>`, then fill in the description, `availability`, `resource` and notes. |
| Add a capability | Search first. Then `python tools/dpc.py new capability <id> --title "..." --broader <parent-id>` and write the explanation, *Key considerations* and *Questions to ask*. Add it to a maturity track's `covers` and, if it matters to one, to a use case or persona. |
| Add a use case | `python tools/dpc.py new use-case usecase-<name> --title "..."`. Follow `bundle/about/mapping-a-use-case.md`. |
| Rename a product | Change `title`, add the old name to `formerly`, keep the `id`. |
| Retire a product | Set `availability: retired` (or `deprecated`) and `status: deprecated`; say what replaced it in the notes. Keep the file so links still work. |
| Review a concept | Check it against its `resource`, fix it, add `verified: {by: human:<you>, at: <UTC timestamp>}` and set `status: stable`. |

## Before you open a pull request

```sh
python tools/dpc.py build
python tools/dpc.py validate --check-generated
python tools/test_dpc.py
```

CI runs the same checks and publishes `dist/` (including `explorer.html`) as a build artefact. Add a dated line to `bundle/log.md` for notable changes.

## Style

Plain, succinct UK English. Explain ideas in plain words before using the technical term. Concrete mechanisms, not adjectives. No marketing language. Write in your own words; do not paste vendor text.
