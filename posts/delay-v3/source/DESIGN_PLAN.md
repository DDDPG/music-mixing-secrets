# V3 design plan — ready for production

## Decision

Use **Apple**, after reading the pinned Apple, IBM and Linear guides. Apple’s product-first presentation best connects the real orange H-Delay interface with neutral technical explanations. IBM’s light display type and enterprise grid would make this read like a technical brochure; Linear’s almost-black canvas and lavender framing would make the interface compete with the diagrams. We borrow neither system.

Reference repository: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md), commit `13be5c05c63be24b57581162364167028020f043`.

Read candidates:
- `design-md/apple/DESIGN.md` — selected; actual tokens: white `#ffffff`, light gray `#f5f5f7`, ink `#1d1d1f`, blue `#0066cc`; quiet 600-weight headings, genuine product imagery, flat surfaces, no decorative gradients.
- `design-md/ibm/DESIGN.md` — white/gray, square geometry, blue `#0f62fe`, IBM Plex Sans 300 display.
- `design-md/linear.app/DESIGN.md` — near-black `#010102`, lavender `#5e6ad2`, layered charcoal screenshot panels.

These are third-party website analyses, not official brand standards. No Apple logos, SF Pro redistribution, copied website chrome, navigation, fake controls or endorsement cues.

## Production contract

**`production_spec.json` is authoritative.** It contains exact final copy, all element rectangles, every line/circle/arrow, image paths and dimensions, diagram coordinates and page-level prohibitions. Implement from it; do not embed the full landscape SVG assets at reduced size. Keep original diagram assets as checked factual references, then rebuild their geometry at final size. Do not run `write_design_spec.py`, which precedes the final fit corrections.

1080 × 1440; preview at 360 × 480. Text safe area x=72…1008. Page 1’s full image extends to x=48…1032 intentionally; text remains inside the safe area. Body 36–40 px; essential diagram labels 30–34 px; caveats 26–28 px; title 58 px, 56 px for the long page-5 title, 68 px on the cover. All headings use 600 weight, body 400. Copy the verified Noto Sans SC 400/600 files and OFL license into the package. Chinese tracking remains zero. No automatic shrinking.

White is dominant; only page 7 uses a light-gray canvas. Gray grouping surfaces appear only where they clarify the send comparison or settings. Blue marks selected information and Delay paths; this is a static teaching adaptation, not Apple’s original interaction rule. Secondary data use dark slate `#697887`, reinforced by position and labels. No warm paper, giant colored panels, gradients, drop shadows, card grid repetition or faux DAW windows.

## Eight compositions

1. **Identify the real object.** Full A01 at `[48,528,984,357.759]`, original ratio/colors. Four external numbered pointers. Use `DELAY R` because that is the actual screenshot label. Two rows of control definitions below. Adjacent disclaimer explicitly says DUAL/BPM and not tutorial settings.
2. **See the insert route.** Large H-Delay boundary `[208,402,640,470]`; the dry split stays inside it. Delay path and Feedback loop in blue; feedback taps before Dry/Wet. Keep the send alternative as a readable prose comparison, not a second tiny diagram.
3. **Compare time, then notice D.** Four horizontal duration bars share x=282…798 for 0…250 ms. Four exact millisecond values stay readable. Real A02 is 300 × 210 at y=1030; beside it, ordinary 1/8 = 187.5 ms and 1/8D = 281.25 ms at 160 BPM. The manual-default warning and the screenshot’s 120 BPM/BPM-state disclaimer remain distinct and adjacent. No second miniature chart.
4. **Follow the alternating events.** A large L/R timeline maps 0…750 ms to x=234…936. Dry sits on a separate row at t=0. A bracket shows the 375 ms same-side interval; body states the 187.5 ms adjacent interval. A03 locates PING PONG. The `Feedback > 1` requirement is identified as a display value, not model g.
5. **Separate two controls.** A04 and A05 sit above the explanation at matched displayed height, never stretched. One grouped chart replaces the two landscape charts: shared 0…100 relative-amplitude axis, four repeat groups, slate g=0.3 and blue g=0.6. The 8× claim is explicitly amplitude, and all model limitations remain near it.
6. **Hear filter direction.** A06 is a large 660 × 288 crop, unchanged. Below, a log-frequency ruler spans 20 Hz…20 kHz, with exact 200 Hz and 6 kHz positions. Arrows show affected sides, not a fictional response curve. Trial adjustments and “one cutoff at a time” remain readable.
7. **Use a reference sheet.** White settings surface on light gray. Five generous rows, followed by reduced-variable settings and three audition steps. No screenshot with invented settings, simulated knob or fake preset panel.
8. **Diagnose in the song.** Four problem-to-control rows lead into accompaniment, matched-loudness and L+R fold-down checks. End with the musical stopping point. No fabricated width, waveform, correlation or loudness measurements.

## Checks and rights

Before export, validate font metrics, arrow destinations and all numeric scales. Then inspect every 1080 px page and 360 px preview. Reflow instead of reducing type if any label or caveat is hard to read. The genuine PNG and crops must remain pixel-identical to the recorded sources.

Waves imagery is attributed, limited product-specific educational quotation. Public republication permission remains **unverified**. Preserve `assets.json`, source links and this limitation in delivery; do not describe it as copyright-cleared or externally publish it. This plan contains no audio measurements or promised sonic outcomes.
