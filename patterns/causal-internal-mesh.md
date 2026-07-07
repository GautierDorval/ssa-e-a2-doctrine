# Causal internal mesh pattern

Status: proposed pattern  
Related layer: `layers/causal-context-layer.md`

## Purpose

A causal internal mesh uses typed internal links to expose the need-state role of pages and clusters.

It is not ordinary internal linking. It is a role-aware graph that tells a machine whether a link points to a trigger, risk, latent need, canonical surface, consequence, proof, or boundary.

## Required discipline

A causal mesh MUST declare its granularity.

Recommended values:

- `doctrinal-core`: canonical doctrine pages;
- `cluster`: editorial family or theme-level relations;
- `surface`: reviewed page-specific relations;
- `candidate`: generated relations awaiting review.

A generated mesh MUST NOT be represented as reviewed surface-level causality.

## Minimal record

```json
{
  "from": "https://example.com/problem-page/",
  "to": "https://example.com/canonical-service/",
  "role": "latentNeed",
  "meshScope": "cluster",
  "reviewStatus": "cluster-level-reviewed"
}
```

## Audit requirements

A useful audit SHOULD detect:

- broken targets;
- duplicated relation signatures beyond declared bilingual pairs;
- excessive templating;
- surface-level claims without review;
- missing canonical surfaces;
- prohibited transactional implications.
