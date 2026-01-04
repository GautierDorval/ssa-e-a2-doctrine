# gsc-priority.json — specification

## Nature

- non-transactional
- observational
- relative to a defined time window

## Purpose

To prioritize stabilization and amplification effort based on Google Search Console signals.

This artifact does NOT:
- define semantic truth
- guarantee performance
- predict outcomes

## Required fields

- version
- scope
- nature
- source
- rule
- generated_on
- window
- scoring_model
- priorities[]

## Interpretation rules

- Scores are relative within a single export window.
- Scores are not comparable across windows without recalibration.
- Metrics may be redacted or bucketed for public publication.

## Constraints

- Must not be used to infer business success.
- Must not be used as a ranking promise.
- Serves orchestration, not explanation.
