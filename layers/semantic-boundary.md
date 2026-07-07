# Semantic-boundary layer

Status: proposed boundary layer  
Version introduced: v1.4.0  
Normative language: MUST / SHOULD / MAY  
Scope: non-equivalence, false-neighbor separation, and proximity-risk declarations

## Purpose

Semantic-boundary defines how implementations should declare concepts, claims, entities, or surfaces that are close enough to be confused but not equivalent.

It exists to prevent a common machine interpretation failure: proximity becomes fusion.

A system may identify two elements as lexically, semantically, or conceptually close. That closeness does not authorize equivalence, substitution, derivation, or causal inference.

## Position in the stack

Semantic-boundary is proposed as an additive boundary layer. It does not replace SSA-E, Dual Web, CCL, Q-Layer, SSA-E-R, or A2.

Its role is narrower:

- identify proximity risks;
- declare false neighbors;
- separate similarity from causality;
- separate consequence from guarantee;
- define behavioral tests for fusion risk when measurement exists.

## Normative rules

### SB-1: Proximity is not equivalence

An implementation MUST NOT treat semantic, lexical, vector, topical, or entity proximity as equivalence unless an authoritative source declares equivalence.

### SB-2: Neighboring concepts require explicit relation types

When two concepts are close but not identical, the implementation SHOULD declare the relation type.

Recommended relation types include:

- `related_not_equivalent`
- `broader_than`
- `narrower_than`
- `supports_but_does_not_prove`
- `causally_related_not_semantically_equivalent`
- `semantically_close_not_causally_related`
- `evidence_not_guarantee`
- `visibility_not_recommendation`

### SB-3: False neighbors must declare prohibited fusions

A false-neighbor declaration MUST identify the fusion or substitution that is prohibited.

A pair is not useful if it only says that two things differ. It must state how a system is likely to merge them and why that merge is invalid.

### SB-4: Boundary tests must not pretend to be measurements

A behavioral testset is a proposed instrument until model runs, judge criteria, prompts, dates, and outputs are published.

Declaring prompts is not the same as measuring behavior.

### SB-5: Semantic-boundary does not define causal relevance

Semantic-boundary may identify proximity risks, but it MUST NOT infer the need-state, trigger, or consequence chain of a surface. That belongs to CCL or to a reviewed CCL implementation.

## Minimal false-neighbor declaration

```json
{
  "source": "llms.txt",
  "neighbor": "AI governance",
  "relation": "related_not_equivalent",
  "risk": "reduction_of_governance_to_discovery_file",
  "prohibitedFusion": "Treating the existence of llms.txt as equivalent to a complete governance system.",
  "requiredBehavior": "Preserve the distinction between discovery, policy, routing, legitimacy, authority control, and context governance."
}
```

## Non-goals

Semantic-boundary does not provide:

- embedding computation;
- a universal similarity threshold;
- a taxonomy of all possible relations;
- proof that a model will respect a boundary;
- a replacement for behavioral evaluation.
