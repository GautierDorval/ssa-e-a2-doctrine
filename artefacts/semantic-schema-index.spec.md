# semantic-schema-index.jsonld — specification

## Nature

- declarative
- non-transactional

## Purpose

To provide a machine-readable inventory of critical pages and their declared schema roles.

This artifact:
- describes what is asserted
- does not define what must be inferred

## Recommended structure

- Schema.org JSON-LD
- WebSite node with hasPart references
- WebPage nodes with about/@type roles

## Constraints

- No pricing, availability, or guarantee claims.
- No duplication of transactional truth.
- Complements SSA-E and A2 without overriding them.

The schema index is an interpretive map, not a source of authority.
