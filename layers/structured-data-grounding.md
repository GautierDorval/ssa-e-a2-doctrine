# Structured data grounding (precondition)

This layer formalizes the minimum structured data grounding required before deploying SSA-E, A2, or Dual Web artifacts.

## Role
Structured data grounding establishes stable identifiers and machine-readable relations for:
- entity identity (who / what),
- scope (what is included and excluded),
- page roles (what a page represents),
- site topology (how content is connected).

It reduces interpretation ambiguity across search engines, LLMs, and agents.

## Non-goals
- Not a ranking or visibility mechanism.
- Not a guarantee of rich results.
- Not a license to invent attributes (no fake ratings, reviews, GTINs, claims, or availability).

## Minimum contract (sitewide)
Implementations typically provide a sitewide baseline including:
- Organization or Person (canonical @id),
- WebSite,
- WebPage,
- BreadcrumbList,
- content type schemas (Article / BlogPosting, Service, etc.) when applicable.

This layer is considered a precondition: SSA-E + A2 + Dual Web should not be claimed as deployed if structured data grounding is absent.
