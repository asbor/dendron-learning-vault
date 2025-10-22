---
id: dendron-refactoring-summary
title: Dendron Refactoring Summary
desc: "Snapshot of the vault reorganization, schema updates, and navigation improvements"
updated: 1761162000000
created: 1698001200000
---

# Dendron Refactoring Summary

This document captures the most recent restructuring of the vault. The focus was on simplifying navigation, aligning notes with long-term domains, and ensuring schema coverage for every active area.

## Key Changes

- **New top-level domains** – Introduced `about` and `education` to separate personal orientation from structured learning.
- **Education namespace** – Migrated all data engineering and data science notes under `education.orange-business` and `education.academic`.
- **Professional focus** – Trimmed the professional tree to emphasize experience and skills, moving onboarding material into the education space.
- **Updated indexes** – Added fresh summaries for each domain (`about`, `education`, `education.orange-business`, `education.academic`, etc.) so every branch has an entry point.
- **Schema refresh** – Replaced legacy `data-engineering`/`data-science` schema files with `education.*` equivalents while keeping `learning`, `knowledge`, and `professional` consistent.

## Schema Overview

| Schema File | Purpose |
| --- | --- |
| `root.schema.yml` | Declares `about`, `education`, `learning`, `knowledge`, `professional`, and `tutorial`. |
| `education.schema.yml` | Defines the education namespace (`orange-business`, `academic`). |
| `education.orange-business.schema.yml` | Details the data engineering curriculum and onboarding guides. |
| `education.academic.data-science.schema.yml` | Maps university modules (IU + STU) with lecture/exercise breakdowns. |
| `learning.schema.yml` | Covers conferences and tooling resources. |
| `knowledge.schema.yml` | Groups setup guides and SQL references. |
| `professional.schema.yml` | Tracks experience and skills assessments. |

## Navigation Improvements

- Every major domain now has an introductory note with clear next steps.
- Cross-links connect related material (e.g., professional reflections ↔️ education tracks).
- README and root landing page highlight the simplified structure for quick entry.

## Maintenance Tips

1. **Create index notes first** – New learning programs or roles should start with a short index inside the appropriate namespace.
2. **Reuse schema patterns** – Extend `education.orange-business.schema.yml` and `education.academic.data-science.schema.yml` when adding new modules.
3. **Keep wikilinks current** – Use the new prefixes (`education.orange-business.*`, `education.academic.*`) for any fresh notes or migrations.
4. **Document external assets** – Large notebooks or datasets stay in their original repositories; reference them instead of duplicating.

---

*This summary is a living log—update it whenever the vault’s structure shifts again.*
