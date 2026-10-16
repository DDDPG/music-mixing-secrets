# Editorial R3 cleanup

## Completed changes
- Removed the cover provenance label element and its unused CSS; kept the R2 hero and cover fonts byte-identical.
- Consolidated inner-page source/vendor notes onto the final resources page and report sources. Removed the redundant non-test/non-preset statements from the carousel, diagrams, report and caption.
- Kept explanatory assumptions beside the relevant claims: already-open gate state, descending detector envelope, 6 dB threshold difference, no retrigger, product-dependent timing and maximum attenuation.
- Rephrased Pro-G discussion around control functions and natural “以…为例” examples. Preserved the real product images without edits.
- Rebuilt both editable SVG explanations and standalone diagram PNGs, all eight carousel PNGs, eight mobile previews, carousel PDF, report PDF and contact sheets.
- Completed the bundled 400/600 body font subsets from the original Noto Sans SC source (SHA-256 a3041811a78c361b1de50f953c805e0244951c21c5bd412f7232ef0d899af0da). Current coverage is 624 characters, zero missing. Registered the local font for SVG rendering and removed dependence on system fallback.
- Updated reproducibility instructions and directory creation in render.py. Added check_fonts.py.

## Checks
- 8 carousel pages at 1080 × 1440; 8 previews at 360 × 480; 5 illustrated report pages.
- Zero page-bounds warnings, zero replacement glyphs and no removed disclaimer labels in either PDF's extracted text.
- Cover artwork, both product images and both cover font subsets match R2 hashes.
- Current contact sheets and selected full-size/mobile pages reviewed: no empty labels, clipped text, crowded footers or damaged UI.
- Source attribution and image-use records remain in the final resource/source sections and RIGHTS.md. Existing image rights remain subject to the documented bounded editorial-use basis.

Independent review is pending. No Library or GitHub operation was performed.
