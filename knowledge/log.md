# Bundle log

- 2026-08-12 — Bundle seeded from step-0 recon of the ontology alignment pass
  (metasalmon roadmap S9). Five cards: domain, context, and three
  InformationObject cards carrying the verified builds/imports facts, the
  F1–F8 conventions findings, and the cross-vocabulary alignment state.
  All cards `status: draft`; sources cited inline as file:line against the
  commits named in each card. Validation: `psc-okf check --tier capture`.
- 2026-08-13 — Codex review fixes: corrected the module-02 card (class-level
  property assertions are legal OWL 2 DL punning, not OWL Full; remedy is a
  targeted SPARQL report plus axiom rewrite, not the DL gate) and registered
  the bundle in docs/entrypoints.md.
- 2026-08-13 — Portability pass: removed all absolute filesystem paths (new
  hub rule); validation command is now relative to a sibling psc-data-systems
  checkout. Cross-repo references updated for metasalmon's notes/ -> knowledge/
  migration.
- 2026-08-13 — S9 step 1 (alignment semantics): F1-F7 fixed, F8 property-side
  fixed; conventions cards updated to reflect the landed state.
- 2026-08-13 — S9 steps 2+5: methods-as-SKOS migration (smn:MethodScheme) and
  smn:StatisticalModifierScheme landed; cross-repo pun resolved; cards updated.
