# False-neighbor boundary pattern

Status: proposed pattern  
Related layer: `layers/semantic-boundary.md`

## Problem

Machine systems often collapse nearby concepts into a single interpretation when the concepts share vocabulary, entities, documents, or retrieval neighborhoods.

This creates false interpretive continuity. The output sounds plausible because the concepts are close, but the reconstruction is wrong because the boundary is missing.

## Pattern

Declare false neighbors explicitly:

```text
source concept -> nearby concept -> relation type -> fusion risk -> prohibited inference -> required behavior
```

## Requirements

A useful false-neighbor record SHOULD include:

- the two terms or surfaces;
- the reason they are likely to be confused;
- the relation type;
- the prohibited fusion;
- the correct distinction;
- the canonical source that governs the distinction;
- optional behavioral prompts for testing.

## Examples

- `llms.txt` is related to AI governance but is not a complete governance system.
- Visibility is related to recommendation but does not imply endorsement.
- Citation readiness is related to answer fidelity but does not guarantee citation or correctness.
- Intended consequence is related to outcome but is not a guaranteed result.

## Boundary rule

If the boundary is not explicit, a system MUST NOT manufacture equivalence from proximity.
