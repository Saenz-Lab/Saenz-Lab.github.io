# Changes Summary

## Files to UPDATE (replace in your repo)

### `index.md` — Redesigned homepage
- Hero banner with "From *lipids* to *life*" tagline
- Research outlook section with membrane animation video (placeholder until you upload `membrane.mp4` to `assets/img/`)
- Bluesky feed embed (@jamessaenz.bsky.social) replacing old Twitter widget
- Lab photo carousel (placeholder — add images later)
- "What we do" pillar cards linking to research page sections
- Fixed UTF-8 encoding (em-dashes render correctly)

### `research.md` — Refined text
- Fixed `RNA–lipid` encoding artifacts
- Tightened wording (removed redundancies)
- Added anchor IDs (`#composition`, `#minimal`, `#regulation`, `#rna-lipid`) so homepage cards link directly to each section

### `_layouts/default.html` — Encoding fix
- Replaced `Â·` and `Â©` with proper HTML entities (`&middot;`, `&copy;`)
- Title no longer shows "Home ·" prefix on the homepage

### `assets/css/style.css` — Full redesign
- Clean white academic aesthetic with serif body text (Palatino/Georgia)
- Sans-serif for headings and navigation (system fonts)
- New styles for: hero banner, intro row, video embed, Bluesky feed, photo carousel, pillar cards with images
- Responsive layout for all new sections

### `scripts/orcid_sync_publications.py` — Deduplication fix
- Added `deduplicate()` function that merges entries sharing the same DOI
- Keeps the entry with the best metadata (prefers DOI links over institutional repository URLs)

## Files to DELETE from your repo

### `index.html`
- This bare placeholder file (`<h1>Welcome to the Laboratory...</h1>`) may override `index.md` in Jekyll builds
- **Delete it** — `index.md` is your real homepage

## Files to ADD to your repo

### `assets/img/membrane-placeholder.svg`
- Temporary SVG shown until you upload the real animation

### `assets/img/membrane.mp4`
- Upload your membrane animation here (convert from .mov if needed)

### Lab photos
- Add to `assets/img/` and update the carousel `<div>` elements in `index.md`
