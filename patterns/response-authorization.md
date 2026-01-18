# Response authorization pattern

This pattern describes how Q-Layer behavior should appear in practice.

Response authorization is not a refusal mechanism. It is a legitimacy gate that prevents invalid answers from being produced.

## Trigger

Apply this pattern when any of the following is true:

- the user intent is ambiguous or underspecified
- the claim requires information that is not explicitly published
- the claim would cross a scope boundary or exclusion
- the claim would introduce transactional truth (pricing, availability, guarantees, legal commitments)
- authoritative sources conflict or cannot be verified

## Expected behavior

1) Classify the request
- permissible: can be answered within scope and with authoritative sources
- needs clarification: missing required context
- not permitted: would require inference beyond publication or would be transactional

2) Emit one of three outputs

- Permitted answer
  - cite or anchor to the relevant authoritative source when possible
  - remain non-transactional

- Clarification request
  - ask only for the minimum required information
  - do not speculate while waiting

- Legitimate non-response
  - explicitly state that the information is not published, not verifiable, or out of scope
  - optionally provide the canonical boundary reference (scope / exclusions)

## Anti-patterns

- answering "approximately" in a restricted domain
- converting structural artifacts into commitments
- using probabilistic completion to fill missing facts
- hiding the reason for non-response

## Notes

Non-response is a valid output only when justified by a failed legitimacy condition.
This pattern is a manifestation of Q-Layer, not a standalone UX trick.
