# R3 editorial QA — 2026-10-16

## Scope and results
- Current carousel: 10 pages, 1080 × 1440 PNG and PDF, plus 360 × 480 phone previews. Text-bounds warnings: 0.
- Current research report: 7 A4 pages, HTML/Markdown/PDF synchronized. The formerly sparse eighth page was removed by consolidating source attribution.
- Creator checked all phone previews, the full-resolution contact sheet, detailed diagram/interface pages, and all seven report-page renders. No visible label placeholders, clipped text or missing glyphs found. Independent review remains pending.
- R2 hero file and cover composition retained; the visible provenance caption and its CSS rule were removed. The generated-image provenance records remain intact.
- Repetitive non-test/non-preset disclaimers removed from rendered slides, report, diagrams and public caption. Technical conditions remain close to formulas/results as normal prose.
- FabFilter attribution is consolidated on carousel page 10 and in report sources. The original Saturn overview includes a prior editorial caption; its presentation now uses an SVG viewBox crop, leaving interface pixels and controls intact.
- Numerical values, formula assumptions, relative dB scale, Peak/RMS distinctions, phase/polarity distinctions and Saturn quality-mode scope were retained.

## Reproduction and fonts
- source/build.py reconstructs the current R2 cover plus R3 editorial copy. It no longer reverts to the pre-R2 cover.
- Static 400/600 fonts cover all current carousel, diagram and report characters. No variable font is required at runtime. The unused full variable font can be omitted from the compact source archive.
- Existing source scripts create output, phone-preview and QA directories as needed. Rendering uses local files.

Prior cover/layout QA documents are marked historical. Current machine checks are in editorial-revision.json and layout-report.json. Original third-party image rights remain reserved; this edit grants no additional image rights.
