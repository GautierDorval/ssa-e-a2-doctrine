# Non-transactional silence pattern

This pattern defines when silence is mandatory.

Silence is not a failure. It is an authoritative response when information is not explicitly published or validated.

## Principle

If a claim is not explicitly stated in authoritative sources, it must not be inferred.

## Domains requiring silence unless explicitly documented

- pricing
- availability
- promotions or discounts
- timelines or delivery guarantees
- compatibility or diagnostics requiring human validation
- contractual commitments
- enforcement or compliance guarantees

## Required behavior

When information is missing or out of scope:
- respond as “unspecified”
- explicitly state that the information is not published
- do not extrapolate from adjacent signals

## Prohibited behavior

- transforming informational content into commitments
- inferring transactional truth from structural or contextual files
- approximating or estimating restricted domains
- filling gaps with probabilistic assumptions

Non-transactional silence is a core safeguard of SSA-E + A2 systems.
