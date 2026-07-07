# Consequence vs guarantee pattern

Status: proposed pattern  
Related layer: `layers/causal-context-layer.md`

## Problem

A surface may be designed to support a consequence: clarification, prevention, qualification, decision support, risk reduction, or abstention.

Systems may inflate that intended consequence into a guarantee.

## Pattern

Preserve the distinction:

```text
intended consequence != guaranteed outcome
```

## Examples

- A migration SEO guide may support prevention of organic visibility loss. It does not guarantee retained rankings.
- A governance policy may support answer fidelity. It does not guarantee that every AI system will obey it.
- A false-neighbor testset may support evaluation. It does not prove model behavior until runs are published.

## Rule

If a consequence is declared without measured evidence, the system MUST phrase it as intention, support, constraint, or risk reduction. It MUST NOT phrase it as certainty.
