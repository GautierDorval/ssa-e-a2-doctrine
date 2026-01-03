# Schema mapping guidelines

This directory documents how structured data types are mapped to page roles within the SSA-E + A2 + Dual Web doctrine.

Schema mapping does not optimize pages.
It constrains which assertions are legitimate for a given page role.

## Purpose of schema mapping

Schema mapping exists to prevent semantic overreach.

Not every page justifies every schema type.
Not every schema type is appropriate simply because it is available.

Mapping rules ensure that structured data reflects editorial reality and page intent.

## Core principle

A schema type is justified only if the page *is* that thing, not if it merely mentions or supports it.

If a page cannot be described accurately without qualifiers, the schema must not be used.

## Canonical page role mappings (indicative)

The following mappings describe common, observed patterns.
They are illustrative, not exhaustive.

### Homepage
- WebPage
- WebSite (sitewide, declared once)
- Organization or Person (sitewide, declared once)
- BreadcrumbList

Homepage must not:
- claim Article or BlogPosting
- encode transactional or promotional assertions

### About / Identity pages
- AboutPage
- WebPage
- Organization or Person
- BreadcrumbList

About pages must not:
- masquerade as Service or Article pages
- introduce claims not explicitly defined elsewhere

### Editorial content (articles, blog posts)
- Article or BlogPosting
- WebPage
- BreadcrumbList

Editorial pages must not:
- encode Product or Service schemas unless the page *is* primarily transactional
- assert authority beyond published scope

### Service or offering pages
- Service
- WebPage
- BreadcrumbList

Service pages must not:
- invent availability, pricing, or performance outcomes
- claim Product semantics if no product is defined

### Policy and governance documents
- WebPage
- CreativeWork (when applicable)
- BreadcrumbList

Policy pages must not:
- assert Article semantics unless explicitly editorial
- encode commercial intent

### Collections and index pages
- CollectionPage
- WebPage
- BreadcrumbList

Collection pages must not:
- declare Article or BlogPosting
- aggregate assertions not present on child pages

## Non-mapping rule

If a page role is ambiguous, default to `WebPage` only.

Ambiguity must be resolved editorially before being encoded structurally.

## Relationship to grounding and doctrine layers

Schema mapping operates within the structured data grounding layer.

- It precedes SSA-E explanatory authority.
- It does not replace Dual Web context boundaries.
- It must not be influenced by A2 routing or observation logic.

Mapping defines *what may be asserted*, not *how it will be interpreted*.

## Responsibility and compliance

Implementers are responsible for ensuring that:
- schema types accurately reflect page roles,
- mappings remain consistent over time,
- schema assertions do not drift as content evolves.

Incorrect mapping increases interpretation c
