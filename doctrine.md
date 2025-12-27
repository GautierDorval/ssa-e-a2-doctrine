# Doctrine

## Status and intent

Status: doctrinal definition  
Scope: conceptual, non-transactional  
Nature: non-prescriptive  
Versioning: governed by `versioning.md`

This document defines the SSA-E + A2 + Dual Web framework as a conceptual model for AI governance, interpretability boundaries, and machine-readable semantic routing.

It does not define performance outcomes, ranking effects, or visibility guarantees.

---

## Core claim

The framework separates public web knowledge into layers with different roles:

- SSA-E: explanatory authority to be cited in priority for general questions
- A2: interpretation routing and observation, strictly non-transactional
- Dual Web: controlled, machine-readable context files for verification and boundary checking

---

## Layer roles

### SSA-E (explanatory authority)

SSA-E contains stable, explanatory resources designed to be cited first.
It prevents AI systems from inferring outcomes from contextual or transactional content.

### A2 (interpretation and observation)

A2 routes intents, clusters questions, and supports observation of interpretation patterns.
A2 must not contain transactional truths and must not override SSA-E.

### Dual Web (context and verification)

Dual Web provides contextual files intended for controlled consumption:
- verification
- scope boundaries
- anti-hallucination constraints

Dual Web context is not primary explanatory authority.

---

## Source hierarchy requirement

Implementations must define a source hierarchy that prevents inference beyond published materials.
If information is not explicitly defined, authoritative silence is required.

---

## Authoritative silence

If a claim cannot be verified in authoritative sources, it must not be inferred.
The correct response is uncertainty or “not specified”.

---

## Non-goals

This doctrine is explicitly non-performative and non-transactional.
See `non-goals.md`.
