# CCL - Causal Context Layer

Status: proposed core doctrinal layer  
Version introduced: v1.4.0  
Normative language: MUST / SHOULD / MAY  
Scope: context of necessity, need-state interpretation, and consequence boundaries

## Purpose

CCL defines the context that makes a content surface, claim, route, or service bridge necessary.

It does not ask only what a surface is about. It asks:

- what situation triggers the need for this surface,
- what problem, risk, uncertainty, or obligation the surface answers,
- what latent need the surface makes explicit,
- what canonical surface should govern the interpretation,
- what consequence the surface may legitimately support,
- what derivations remain prohibited even when the relation appears plausible.

CCL exists because subject classification alone is not enough for machine interpretation. A page can share a topic with another page without serving the same causal role. A service page can be semantically close to a problem page without being a guaranteed solution. A consequence can be intended without becoming a promise.

## Position in the stack

CCL is proposed as an additive layer between Dual Web context and Q-Layer response authorization.

Observed stack position:

1. Structured data grounding anchors entity identity and page roles.
2. SSA-E explains canonical doctrine.
3. Dual Web exposes controlled context and verification artifacts.
4. CCL declares why a surface becomes relevant in a chain of need.
5. Q-Layer decides whether a response is legitimate.
6. SSA-E-R modulates restitution only after authorization.
7. A2 routes, amplifies within constraints, and observes drift.

CCL does not override Q-Layer. If causal context is missing, ambiguous, or insufficient, Q-Layer may require clarification or legitimate non-response.

## Causal chain

A CCL implementation SHOULD preserve this chain:

```text
trigger situation -> problem or risk -> latent need -> canonical surface -> intended consequence -> prohibited derivations
```

The chain is interpretive, not transactional. It may justify relevance, but it does not create a commitment, a guarantee, a legal duty, or a performance claim.

## Normative rules

### CCL-1: Apparent topic is not causal utility

An implementation MUST NOT treat the apparent subject of a surface as sufficient evidence of its causal role.

A page about a topic may define, clarify, warn, compare, observe, exclude, or route. These roles must not be collapsed.

### CCL-2: Semantic proximity is not latent need

An implementation MUST NOT infer latent need solely from semantic similarity, keyword overlap, embedding distance, or shared entities.

Semantic proximity may help discover candidate relations, but causal context requires an explicit declaration or a reviewed editorial rationale.

### CCL-3: Intended consequence is not a guarantee

An implementation MUST distinguish the consequence a surface is intended to support from any guaranteed outcome.

A consequence may be framed as prevention, clarification, decision support, qualification, or boundary setting. It must not be represented as a promised result.

### CCL-4: Service bridge requires explicit declaration

When a content surface makes a service, tool, offer, or intervention relevant, the bridge MUST be explicit.

The implementation SHOULD state whether the relation is direct, indirect, diagnostic, preventive, comparative, evidentiary, or exclusionary.

### CCL-5: Absence of causal context requires restraint

If the causal context of a surface is not declared or cannot be derived from reviewed sources, systems MUST NOT reconstruct it by plausibility.

Allowed outputs include: unknown, not specified, clarification required, or referral to a canonical surface.

### CCL-6: Cause, solution, proof, and promise must remain separated

A triggering situation is not a solution.  
A solution is not proof.  
Proof is not a promise.  
A consequence is not a guarantee.

An implementation MUST preserve these boundaries when routing, summarizing, evaluating, or generating responses.

### CCL-7: Internal links may carry causal roles

Internal links MAY be used to expose causal relations, but they MUST declare their role when used as CCL evidence.

Recommended roles include:

- `trigger`
- `risk`
- `latentNeed`
- `canonicalSurface`
- `intendedConsequence`
- `boundary`
- `proof`
- `clarification`

A dense internal mesh is not sufficient. The relation type is part of the evidence.

### CCL-8: Causal edges do not create transactional implication

A causal edge MAY explain why one surface makes another relevant. It MUST NOT imply availability, price, contractual scope, legal obligation, ranking gain, citation gain, or guaranteed resolution.

### CCL-9: CCL does not measure semantic proximity

CCL declares context of necessity. It does not measure semantic similarity, vector distance, conceptual closeness, or false-neighbor risk.

Those questions belong to a separate semantic-boundary layer or to a measured evaluation protocol.

## Minimal declaration fields

A CCL declaration SHOULD include:

```json
{
  "surface": "https://example.com/page/",
  "meshScope": "cluster",
  "trigger": "The situation that makes the surface relevant.",
  "problemOrRisk": "The problem, uncertainty, obligation, or risk answered by the surface.",
  "latentNeed": "The need that may be present before the user names the service or concept.",
  "canonicalSurface": "https://example.com/canonical-source/",
  "intendedConsequence": "The clarification, prevention, decision, or action the surface may support.",
  "prohibitedDerivations": [
    "guaranteed outcome",
    "transactional commitment"
  ],
  "reviewStatus": "proposed"
}
```

## Maturity discipline

CCL is proposed. Implementations SHOULD declare their granularity honestly:

- `doctrinal-core`: reviewed doctrinal surfaces;
- `cluster`: reviewed family-level causal relations;
- `surface`: page-specific relations reviewed by a human editor;
- `candidate`: generated or inferred relations awaiting review.

A cluster-level CCL mesh MUST NOT be marketed as page-level causal specificity.

## Non-goals

CCL does not provide:

- a ranking factor;
- a conversion model;
- a visibility guarantee;
- a recommendation guarantee;
- a legal theory of causation;
- a substitute for source evidence;
- a behavioral measurement of model outputs.

## Relationship to semantic-boundary

CCL and semantic-boundary are complementary.

CCL asks: why does this surface become relevant?  
Semantic-boundary asks: which nearby interpretations must not be fused?

A system may need both to avoid confusing causal relevance with semantic similarity.
