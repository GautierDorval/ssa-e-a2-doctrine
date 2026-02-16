# Reading guide

This repository is doctrinal: it explains **why** SSA-E + A2 + Dual Web + Q-Layer + SSA-E-R exist.
It is **not** a product, a framework, or a certification.

If you are looking for the canonical machine-first standard, start at:
- https://interpretive-governance.org

---

## Minimal path (10–15 minutes)

1) `doctrine.md`  
   The full stack and the intended deployment order.

2) `layers/q-layer.md`  
   The legitimacy discipline: answering is not the default state.

3) `patterns/source-hierarchy.md`  
   The normative hierarchy that prevents inference from becoming “fact”.

---

## Deeper path (30–60 minutes)

1) `terminology.md`  
   Vocabulary and scope boundaries.

2) Layer docs (pick what you need):
   - `layers/ssa-e.md`
   - `layers/dual-web.md`
   - `layers/a2.md`
   - `layers/q-layer.md`
   - `layers/ssa-e-r.md` (RFC)

3) Constraints and safety posture:
   - `LIMITATIONS.md`
   - `non-goals.md`
   - `principles.md`

4) Structured data grounding:
   - `layers/structured-data-grounding.md`
   - `schema-rules/README.md`
   - `schema-templates/README.md`

---

## By persona

### CTO / architect (systems)
- Read: `doctrine.md` → `layers/q-layer.md` → `patterns/source-hierarchy.md` → `LIMITATIONS.md`
- Goal: understand why legitimacy and authoritative silence are first-class constraints.

### Engineer / implementer
- Read: `layers/q-layer.md` → `schema-rules/README.md` → `schema-templates/README.md`
- Then: reference the non-normative runtime proof in `interpretive-agentic-reference`.

### Auditor / governance / compliance
- Read: `LIMITATIONS.md` → `layers/q-layer.md` → `patterns/response-authorization.md` → `OBSERVABILITY.md`
- Goal: understand what the doctrine claims, and explicitly does **not** claim.

### Publisher / SEO / structured data lead
- Read: `layers/structured-data-grounding.md` → `schema-rules/README.md` → `patterns/source-hierarchy.md`
- Then: see `implementations/better-robots-txt.md` (informational surface).

---

## Machine-readable map

- Doctrinal entity graph (JSON-LD): `ssa-e-a2-dual-web-doctrine.jsonld`
- Link registry: `links.json`
