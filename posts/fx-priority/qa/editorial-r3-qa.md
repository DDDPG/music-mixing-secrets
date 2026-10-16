# Editorial R3 QA · FX priority

Date: 2026-10-16. Scope: current carousel, report, captions, editable HTML/CSS/SVG and compact-source reproducibility. Independent final review is recorded separately.

## Changes checked

- The cover's visible provenance label and its CSS rule were removed. The R2 hero image and all cover composition settings remain unchanged.
- Removed per-page source footnotes and repetitive non-test/non-preset commentary. Final-page technical references and FabFilter attribution remain, with detailed sources and rights grouped at the end of the report.
- Replaced screenshot-state warnings with the actionable instruction to switch Internal to External and connect the FX send in the host. Screenshot controls and parameter values are unchanged.
- The Pro-C 3 asset contains a previously appended 100 px editorial strip. The carousel uses top-aligned cropping. The report uses a proportional SVG viewport to display exactly the complete original 1680 × 1386 screenshot, with no dependency on page/body margins; neither changes the software interface.
- Mathematical and timing SVGs now use positive descriptions: ideal steady-state compression and an Automation gain-envelope example. Hard Knee, Auto Threshold off, signal-above-threshold assumptions, Release response, timing points and arithmetic remain intact.
- Report Markdown, report HTML, full story and platform caption have matching editorial changes.
- A short orphan on page 5 was fixed with a deliberate sentence break.

## Render and integrity checks

- Carousel: 9 pages, 1080 × 1440 PNG and PDF. Phone previews: 360 × 480. Report: 9 pages; source entries stay together across page boundaries.
- All current HTML image/style references resolve locally. Render script creates output, phone-preview and QA-preview directories, including when run from a compact source package without generated folders.
- Both bundled body-font weights contain 723 glyphs and cover every visible character in the current HTML, report and SVGs. SVGs use the bundled Noto family. No system CJK fallback is required for the authored text.
- PDF text is within page bounds, with no replacement characters. Current reading surfaces contain no targeted AI-label, non-test, non-preset or screenshot-disclaimer phrases, and no empty label boxes remain.
- R2 hero SHA-256: `6c4b2fdf86883ed08c42cfeeb4095a95e1b854c8c64f4f1533078aea6d8a5d6f`.

## Visual inspection

Inspected both contact sheets, affected full-size carousel pages, 360 px phone previews and the final report resources page. The cover remains dominant, screenshot controls are complete, and page 5 calculations, page 6 timing and page 7 instructions are legible. No overlap, clipped copy or orphaned caption boxes were found. Older QA Markdown is explicitly marked historical.

## Remaining considerations

No unresolved editorial or rendering blocker. FabFilter's image rights remain as recorded in RIGHTS.md; this revision does not expand the usage license. The original source asset and generation provenance are retained for traceability.

## Independent-review correction · 2026-10-16

The reviewer identified a clipped attribution line below the report screenshot on page 5. The fixed-height display crop had assumed a wider content area than the actual body. It was replaced by `assets/derived/pro-c3-display.svg`, a 1680 × 1386 clipping viewport over the unchanged 1680 × 1486 source asset. The report was rerendered and page 5 inspected at 1.5×: no strip pixels remain, the entire bottom status bar is visible, and all article text is unchanged. Report length remains 9 pages; all report previews and the contact sheet were refreshed.
