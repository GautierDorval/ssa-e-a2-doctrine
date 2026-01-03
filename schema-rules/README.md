# Schema rules and constraints

This directory defines the normative constraints governing the use of structured data within the SSA-E + A2 + Dual Web doctrine.

These rules exist to limit interpretation space, not to expand it.

## Role of schema rules

Schema rules define what structured data is allowed to assert and, more importantly, what it must refuse to assert.

They operate as a negative capability layer:
preventing inference, speculation, and semantic drift caused by over-assertive markup.

## Core principle

If a fact is not explicitly published and verifiable in authoritative sources, it must not be encoded in structured data.

Omission is the correct action when certainty cannot be established.

## Mandatory constraints

Implementations must comply with the following constraints:

- Structured data must never introduce information absent from the visible or authoritative content.
- Schema properties must not contradict or extend editorial content.
- Identifiers (`@id`) must be stable, canonical, and consistently reused.
- Relationships must reflect real, published connections, not assumed hierarchies.
- Optional properties remain optional and must not be populated for completeness or perceived benefit.

## Explicitly forbidden practices

The following practices are incompatible with this doctrine:

- Inventing ratings, reviews, popularity metrics, or engagement signals.
- Declaring transactional facts (pricing, availability, delivery promises) unless formally published and maintained.
- Using `sameAs` links without clear editorial or ownership control.
- Encoding legal, medical, or financial claims not explicitly stated.
- Treating structured data as an optimization or persuasion mechanism.

## Authority and precedence

Structured data is subordinate to:

1. Published editorial content.
2. SSA-E explanatory resources.
3. Explicit source hierarchy definitions.

If a conflict exists, structured data must yield and be corrected or removed.

## Relationship to other layers

Schema rules do not interpret meaning.

- They do not route intents (A2).
- They do not define explanatory truth (SSA-E).
- They do not establish verification context (Dual Web).

They exist solely to constrain what can be asserted at the grounding level.

## Consequences of violation

Improper or speculative schema usage increases ambiguity and interpretation cost.

Such violations directly undermine disambiguation objectives and invalidate claims of doctrinal compliance.
