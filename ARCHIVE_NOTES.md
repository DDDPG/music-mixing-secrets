# Archive scope and preservation

Three post topics are archived. The main Delay entry uses approved V3. Earlier revisions are indexed separately when recovered; the main index never silently substitutes a historical revision for the approved baseline.

Final HTML, PNGs and PDFs are preserved byte-for-byte; checksums are in [PRESERVED_FINALS.json](PRESERVED_FINALS.json). The archive is a curated public source tree rather than a full working-directory mirror. Publicly readable reports reconstruct the research rationale from the retained production artifacts and are explicitly labelled as reconstructions.

Excluded materials: full vendor media ZIPs, unrelated vendor logos/press releases, duplicated delivery bundles, complete cached manuals/webpages, operational delivery manifests and non-public provenance. Product illustrations actually used in the teaching material remain with ownership and source notices.

Portability changes: renderer scripts use installed dependencies instead of a machine-specific import directory. Packaging uses relative paths. The drum/bass facts and research generator contain only public content. Source project READMEs are replaced by per-post navigation and reproducibility notes; final artwork is unchanged.

## Modified support files

- `posts/delay-v3/source/render.py`
- `posts/delay-v3/source/package.py`
- `posts/ms-return/source/render.py`
- `posts/ms-return/source/package.py`
- `posts/drums-bass/source/render.py`
- `posts/drums-bass/source/build_research.py`
- `posts/drums-bass/source/facts.json`
- `posts/drums-bass/source/package.py`

## Historical recovery

Delay V2 was recovered with eight PNGs, PDF, contact sheet, HTML, caption, diagram sources, fonts, and licenses. Its support scripts receive the same relative-path portability edits. Original V2 workflow text is replaced by the repository-level public workflow. V1 recovery and inclusion are tracked in history/README.md.

Delay V1 is also included unchanged as historical artwork, including its benign original mixing-note narrative and date. The historical caption and technical source note remain intact. No raw note extraction is included.

## Upstream template references

The seed-editorial.html files preserve the upstream template for source/license provenance and use by build scripts. They are not final standalone posts; unused placeholder references (for example cover.jpg or template screenshot backgrounds) are not bundled. The active page assets resolve locally, and index.html files are the viewing entrypoints. Historical V1/V2 HTML also retains unused upstream CSS texture references; these absent placeholder textures are not applied to the rendered pages. Both historical render smoke tests passed without them.

Unused reference-image entries remain in assets.json for provenance, explicitly marked as not bundled. They are not dependencies of the final pages.

Rebuild smoke tests succeeded for the three current posts and both historical versions in temporary copies using the retained rendering dependencies: current posts 8 / 7 / 8 pages, historical V1 / V2 7 / 8 pages, all at 1080 × 1440, with zero text-bound warnings. This was not a fresh dependency-install test, and the published original final artifacts were not overwritten. Python syntax, local references and final-artifact checksums were also checked.

Support scripts also create their QA/preview output directories when absent, allowing a clean checkout to rebuild without archived operational QA files.

Project-level workflow text is consolidated into the public root WORKFLOW.md; the Delay source keeps a link to it instead of redundant process notes.

The create_research.py / build_research.py scripts are preserved early-stage authoring generators, not the final rebuild entrypoints. Running them may overwrite later editorial data. Use build.py and render.py to rebuild current pages; use a separate copy when studying an earlier authoring generator. Optional omitted reference images are skipped.
