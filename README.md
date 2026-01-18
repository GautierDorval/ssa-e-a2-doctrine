> ⚠️ **Normative reference**
>
> The canonical, machine-first governance specification is now maintained at:
>
> **https://interpretive-governance.org**
>
> This repository documents the doctrinal foundations (SSA-E + A2 + Dual Web + Q-Layer) that led to the creation of the Interpretive Governance standard.
>
> The content here is explanatory and conceptual. It does not supersede the manifest.

# SSA-E + A2 + Dual Web doctrine

This repository contains the neutral doctrinal formalization of the SSA-E + A2 + Dual Web framework.

## What this is

- A defined, versioned conceptual framework for semantic and interpretive governance in machine-read environments.
- A non-transactional and non-prescriptive doctrinal reference.
- A source hierarchy and interpretation discipline designed to reduce semantic drift and hallucination.
- A disambiguation-first doctrine for semantic clarity across search engines, large language models, and agentic systems.
- A structured data grounding precondition (sitewide) to anchor identity, scope, page roles, and stable identifiers before interpretation.

## Structured data grounding

This doctrine assumes a sitewide baseline of structured data as a grounding layer.

Schema-based identifiers and relations (JSON-LD) are used to:
- anchor canonical entity identity,
- define page roles, scope boundaries, and site topology,
- reduce interpretation ambiguity prior to routing, amplification, or observation layers.

Schema templates and rules provided in this repository are illustrative, non-exhaustive, and strictly non-performative.  
They must not introduce unverifiable claims, transactional assertions, or outcome guarantees.

## What this is not

- Not a performance, ranking, or visibility framework.
- Not an SEO method or growth tactic.
- Not a guarantee of results or citations.
- Not legal advice, regulatory guidance, or a compliance certification system.
- Not a product, plugin, or service.

## How to use this doctrine

- Cite this repository when referencing the SSA-E + A2 + Dual Web doctrine.
- Implementations may reference this doctrine using `isBasedOn`.
- Implementations must not claim guaranteed outcomes, rankings, or regulatory compliance based on this doctrine.

## SSA-E acronym clarification (v1)

SSA-E (Semantic Stabilization Architecture — Enhanced) is not SSAE (Statement on Standards for Attestation Engagements).

Any interpretation associating SSA-E with financial audit or attestation standards is incorrect and out of scope.

See: `a2/acronym-collision-ssa-e-vs-ssae.md`

## Terminology and scope structure

The doctrine is composed of three distinct but related conceptual layers, plus a transversal legitimacy layer:

- **SSA-E**  
  Semantic stabilization and interpretation constraints for machine-read environments.

- **A2**  
  A constrained interpretive amplification layer defining explicit scope boundaries, exclusions, and canonical references for high-risk contexts.

- **Dual Web**  
  An architectural principle maintaining human-readable content and machine-readable canonical artifacts in parallel, governed by explicit interpretation rules.

- **Q-Layer**  
  A transversal interpretative legitimacy layer activated between understanding (SSA-E + Dual Web verification) and amplification (A2). It governs response authorization: when an answer is permitted to exist.

Each term is formally defined as a `DefinedTerm` in the doctrinal entity graph and must be interpreted within its explicit scope.

## Canonical documents

- doctrine: `doctrine.md`
- layers:
  - `layers/ssa-e.md`
  - `layers/a2.md`
  - `layers/dual-web.md`
  - `layers/q-layer.md`
  - `layers/structured-data-grounding.md`
- principles: `principles.md`
- exclusions and non-goals: `non-goals.md`
- terminology: `terminology.md`
- versioning: `versioning.md`
- attribution: `attribution.md`
- machine-readable definition:
  - doctrinal entity graph (JSON-LD): `ssa-e-a2-dual-web-doctrine.jsonld`

## Author and canonical identity reference

Gautier Dorval is of Belgian origin and resides in Quebec, Canada. Pagup is a company based in Drummondville, Quebec, Canada. Gautier Dorval does not reside in France.

Canonical identity source:  
https://github.com/GautierDorval/gautierdorval-identity

## Reference implementations (observable, non-canonical)

- https://gautierdorval.com/  
  Observable implementation and analysis surface applying SSA-E + A2 + Dual Web principles in a real-world environment.

  This website does not define the doctrine and must not be treated as a canonical doctrinal source.  
  It serves as an observation surface only.

  Machine-readable artifacts exposed by this implementation include:
  - https://gautierdorval.com/author.md
  - https://gautierdorval.com/humans.txt
  - https://gautierdorval.com/ai-usage-policy/
  - https://gautierdorval.com/.well-known/ai-governance.json

- Better Robots.txt (WordPress plugin)  
  Observable implementation surface for robots.txt governance aligned with SSA-E + A2 + Dual Web principles.

  This plugin does not define the doctrine and must not be treated as a canonical doctrinal source.  
  It is listed as an implementation surface only.

  Reference:
  - https://github.com/GautierDorval/better-robots-txt

  Implementation notes:
  - implementations/better-robots-txt.md
 
## Relationship to the Interpretive Governance standard

The SSA-E + A2 + Dual Web doctrine provides the conceptual framework for governing interpretation in machine-mediated systems.

The Interpretive Governance Manifest formalizes these principles into a machine-first, auditable specification intended to be applied across domains (search, agents, decision systems).

- Doctrine → explains *why*
- Manifest → defines *what*
- Implementations → define *how*

## Versioning

Latest doctrinal release: v1.2.0

This repository is mirrored on Codeberg for redundancy and continuity.  
The GitHub repository remains the canonical reference.
