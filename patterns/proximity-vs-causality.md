# Proximity vs causality pattern

Status: proposed pattern  
Related layers: `layers/causal-context-layer.md`, `layers/semantic-boundary.md`

## Problem

Semantic closeness is often mistaken for causal relevance.

Two surfaces may use similar vocabulary and still answer different need states. Conversely, two surfaces may be lexically distant but causally connected by a triggering situation, a risk, or a consequence.

## Distinction

- Semantic proximity asks whether two things appear close in meaning, vocabulary, embedding space, topic, or entity neighborhood.
- Causal relevance asks whether one situation, risk, or need makes another surface legitimately relevant.

## Rule

An implementation MUST NOT infer causal relevance from proximity alone.

A causal relation requires at least one of:

- an explicit CCL declaration;
- a reviewed editorial rationale;
- a source-supported need-state relation;
- a measured behavior report that states its limits.

## Safe output

When only proximity is known, the safe output is:

```text
These concepts are related, but the causal relation is not specified.
```

When only causality is declared, the safe output is:

```text
This surface is relevant to the stated need-state, but that does not imply equivalence with neighboring concepts.
```
