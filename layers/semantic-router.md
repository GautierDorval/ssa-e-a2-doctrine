# Semantic router (A2 routing constraints)

This layer defines an ultralight intent → canonical routing artifact.

It exists to prevent misrouting, avoid crawl traps, and enforce authoritative silence on transactional domains when sources are not explicit.

## Artifact : semantic-router.json

Hard rules (examples) :
- Prefer canonical URLs without query parameters.
- Treat parameterized inventory filters as non-canonical crawl traps.
- For pricing, availability, promotions, diagnostics : require explicit source or respond as unspecified.
