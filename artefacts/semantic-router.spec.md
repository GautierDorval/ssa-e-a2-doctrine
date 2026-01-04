# semantic-router.json — specification

## Nature

- non-transactional
- interpretive constraint layer

## Purpose

To route frequent intents to canonical URLs while preventing misrouting and unsafe inference.

## Core rules

- Prefer canonical URLs without parameters.
- Explicitly define crawl traps and non-canonical patterns.
- Prevent routing to filtered or parameterized inventory URLs.

## Hard constraints

Unless explicitly published:
- no pricing inference
- no availability inference
- no diagnostic inference
- no contractual commitment inference

## Typical fields

- version
- scope
- purpose
- rules[]
- crawl_traps
- routes[]

The semantic router exists to reduce interpretive error, not to automate decisions.
