# Platform variability pattern

This pattern addresses the non-deterministic nature of external platforms.

## Principle

Outcomes are not guaranteed because platforms evolve.

Changes may occur in:
- parsers
- renderers
- crawlers
- caches
- CDNs
- security layers
- indexing behavior
- UI or API behavior

## Implications

- Identical inputs may produce different outputs over time.
- False positives and false negatives are inherent.
- Observations are temporal, not absolute.

## Required interpretation rule

No claim of:
- permanence
- universality
- guaranteed behavior

may be made unless explicitly documented by the platform itself.

Platform variability is an irreducible constraint and must be acknowledged.
