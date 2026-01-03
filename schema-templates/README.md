# Schema templates usage guidelines

This directory contains illustrative JSON-LD templates intended to support the structured data grounding layer of the SSA-E + A2 + Dual Web doctrine.

These templates are not optimization recipes and must not be treated as performance levers.

## Purpose

Schema templates provided here serve one primary function:
to anchor stable identifiers and explicit relations so that meaning becomes cheaper to verify and harder to infer incorrectly.

They exist to reduce ambiguity, not to increase exposure.

## Non-goals

These templates must not be used to:
- claim ranking, visibility, or rich result eligibility,
- introduce unverifiable attributes or inferred facts,
- compensate for missing or unclear content,
- override the explanatory authority of SSA-E resources.

## Usage constraints (mandatory)

When using these templates:

- Every property must be grounded in explicitly published content.
- If a value cannot be verified, the property must be omitted.
- Empty placeholders must never be left in production markup.
- Schema types must reflect the actual role of the page or entity, not its intended positioning.
- Optional properties are optional by design and should not be “filled for completeness”.

## Anti-patterns (forbidden)

The following practices are explicitly incompatible with this doctrine:

- Invented ratings, reviews, or aggregate metrics.
- Fake or speculative `sameAs` links.
- Transactional claims (pricing, availability, delivery) unless formally published.
- Using schema to contradict or overrule page content.
- Treating schema as a substitute for clear editorial structure.

## Relationship to SSA-E, Dual Web, and A2

Structured data grounding is a precondition layer.

- It does not replace SSA-E explanatory authority.
- It does not act as Dual Web verification context.
- It must not be modified by A2 routing or observation logic.

Each layer has a distinct role. Schema exists to anchor identity and relations, not to interpret or optimize.

## Responsibility

Implementers remain responsible for ensuring that structured data reflects published reality.

Incorrect or speculative schema usage increases ambiguity and interpretation cost, directly violating the objectives of this doctrine.
