# Versioning

## Version intent

Versions reflect doctrinal evolution, not performance changes.

## Backward compatibility

New versions must not contradict prior definitions without an explicit deprecation note.

## Change discipline

Changes must:
- preserve layer roles
- preserve non-transactional constraints
- preserve authoritative silence rules
- preserve Q-Layer response authorization semantics (no implicit override)

## Optional integrity fingerprints (implementations)

Some reference implementations may publish SHA-256 fingerprints for critical machine-first artifacts
(e.g., entity graphs, manifests, governance entrypoints) to prevent silent drift and support auditability.

This mechanism is a versioning and change-control aid.
It does not imply enforcement over external systems, and it must not be interpreted as a guarantee,
certification, or authority proof.

## RFC modules (experimental doctrinal extensions)

Some doctrinal modules may be introduced with an explicit RFC status.

RFC modules:
- are doctrinal and conceptual, not operational guarantees,
- may evolve between minor versions,
- must be explicitly marked as RFC in canonical documents,
- must not be interpreted as enforcement over external systems.

SSA-E-R is an RFC module:
- it governs restitution only (form and depth of an already-legitimate answer),
- it is applied post Q-Layer authorization,
- it must not override Q-Layer outputs (clarificationRequired or legitimateNoAnswer),
- it must fall back to Q-Layer when compliant restitution would require invention.

## Recommended tagging

Tag releases as:
- v1.0, v1.1, v1.2…

Each tag should correspond to a coherent doctrinal state.

If an RFC module is introduced or materially revised, the release notes must:
- identify the module,
- state its RFC status,
- state its non-override and non-transactional constraints,
- state whether any canonical definitions or doctrinal entity graphs were updated.
