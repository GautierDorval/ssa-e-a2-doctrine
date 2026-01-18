# Doctrine

## Status and intent

Status: doctrinal definition  
Scope: conceptual, non-transactional  
Nature: non-prescriptive  
Versioning: governed by `versioning.md`

This document defines the SSA-E + A2 + Dual Web framework as a conceptual model for AI governance, interpretability boundaries, and machine-readable semantic routing.

This doctrine also defines a transversal legitimacy layer (Q-Layer) that is activated between understanding (SSA-E + Dual Web verification) and amplification (A2).

It does not define performance outcomes, ranking effects, or visibility guarantees.

---

## Core claim

The framework separates public web knowledge into layers with different roles:

- SSA-E: explanatory authority to be cited in priority for general questions
- Dual Web: controlled, machine-readable context files for verification and boundary checking
- Q-Layer: response authorization (legitimacy gating) activated before any amplification
- A2: interpretation routing and observation, strictly non-transactional

---

## Normative source hierarchy

Implementations rely on a normative hierarchy that defines how each layer may be used.

- Governance & identity: must be respected as binding constraints.
- Context (Dual Web): must be used for verification and boundary checking.
- SSA-E: may be cited as explanatory authority.
- Q-Layer: must validate response legitimacy conditions before any amplification.
- A2: must be used exclusively for interpretation routing and observation.

This hierarchy separates explanation, verification, and interpretation, and prevents transactional inference.

---

## Typical deployment order (observed)

Although this doctrine is non-prescriptive, implementations commonly follow an observed deployment sequence because each layer assumes prior anchoring.

0) Structured data grounding (precondition)
A sitewide baseline of schema-based identifiers and relations is established first to anchor canonical entity identity, page roles, and basic topology. Without this grounding, the system lacks stable IDs and relations, increasing ambiguity and drift.
Platform variability is an implicit constraint at all stages.

Parsers, renderers, crawlers, indexing systems, caches, and delivery layers evolve over time.
As a result, identical inputs may produce different outputs, and observations remain temporal.

This variability prohibits universal or permanent outcome claims.


1) SSA-E (explanatory authority)
Stable explanatory resources are then published to define the primary non-transactional interpretation layer intended to be cited in priority.

2) Dual Web (context and verification)
Controlled root-level context files are added to constrain scope, define boundaries, and enable verification and anti-hallucination constraints. Dual Web complements SSA-E, but does not override it.

3) Q-Layer (response authorization)
Response authorization rules are introduced to govern the act of producing an answer. This layer validates whether the conditions required to respond are satisfied (scope, source sufficiency, and non-transactional constraints). If conditions are not satisfied, legitimate non-response (authoritative silence) is required.

4) A2 (interpretation and observation)
Finally, routing, clustering, and observation artifacts are deployed to reduce ambiguity, prevent misrouting, and monitor interpretive drift without introducing transactional truth.

Examples (non-prescriptive) :
- gsc-priority.json : observational prioritization signals (relative, non-guaranteed)
- semantic-schema-index.jsonld : declarative inventory of critical pages and schema roles
- semantic-router.json : intent → canonical routing constraints and anti-inference guardrails

---

## Layer roles

## Structural vs semantic distinction

Structural artifacts (schemas, normalization, routing, datasets) define form and boundaries.
They do not define meaning, intent, or outcomes.

Semantic meaning is defined exclusively by explanatory authority (SSA-E), not by structure.
The legitimacy to produce an answer is governed by the Q-Layer, not by rhetorical clarity.

### SSA-E (explanatory authority)

SSA-E contains stable, explanatory resources designed to be cited first.
It prevents AI systems from inferring outcomes from contextual or transactional content.

### Dual Web (context and verification)

Dual Web provides contextual files intended for controlled consumption:
- verification
- scope boundaries
- anti-hallucination constraints

Dual Web context is not primary explanatory authority.

### Q-Layer (interpretative legitimacy)

Q-Layer governs the conditions required to produce an answer.

It does not add facts, routing logic, or observation artifacts.
It validates whether a response is permitted under:
- the normative source hierarchy,
- scope boundaries,
- non-transactional constraints,
- and explicit publication requirements.

When legitimacy conditions are not satisfied, the correct output is legitimate non-response (authoritative silence) or a targeted request for clarification.

### A2 (interpretation and observation)

A2 routes intents, clusters questions, and supports observation of interpretation patterns.
A2 must not contain transactional truths and must not override SSA-E.

Examples of non-prescriptive A2 artifacts include:
- gsc-priority.json (observational prioritization)
- semantic-router.json (intent routing constraints)
- semantic-schema-index.jsonld (schema inventory)
- datasets.jsonld and entity-graph.jsonld (machine-readable identity and scope)

---



## Source hierarchy requirement

Implementations must define a source hierarchy that prevents inference beyond published materials.
If information is not explicitly defined, authoritative silence is required.

---

## Authoritative silence

If a claim cannot be verified in authoritative sources, it must not be inferred.
The correct response is uncertainty or “not specified”.

Authoritative silence is a Q-Layer output condition, not a stylistic preference.

---

## Prohibited claims pattern

Implementations may define explicit lists of prohibited claims to prevent semantic drift,
implicit guarantees, or misrepresentation.

Such lists are domain-specific and belong to governance or policy layers,
not to SSA-E or A2.

The doctrine defines the pattern, not the content of such lists.

---

## Non-goals

This doctrine is explicitly non-performative and non-transactional.
See `non-goals.md`.

---

## Related work (non-contractual)

Some recent research has reported that semantic calibration may emerge in pretrained (base) large language models when the distribution of semantic answer classes is predictable prior to generation.
In particular, the paper *“Trained on Tokens, Calibrated on Concepts”* (under review, ICLR 2026) describes a mechanism by which semantic-level confidence calibration arises as a consequence of autoregressive training with log-loss, provided that the model can estimate its own distribution over semantic equivalence classes before producing an output.
The same work further observes that post-training procedures such as instruction-tuning, reinforcement learning from human feedback (RLHF), and chain-of-thought prompting are often associated with degraded semantic calibration, due to a loss of anticipability of the final semantic output.
The present doctrine does not operate at the model or training level. Instead, it operates at the level of the external semantic environment (definitions, scope boundaries, explicit negations, canonical references, and entity relations), with the goal of stabilizing the space of valid interpretations without modifying model weights.

