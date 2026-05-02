# Cadence v1.5.0 → v1.8.0 Update Guide

This package contains everything needed to update the Cadence repository
from v1.5.0 to v1.8.0. Every file in this ZIP is a **drop-in replacement** —
no patches, no scripts.

## What's in this ZIP

```
cadence-v1.8.0/
├── README.md                                  ← drop-in replacement
├── CHANGELOG.md                               ← drop-in replacement
├── VERSIONING.md                              ← drop-in replacement
├── ROADMAP.md                                 ← drop-in replacement
├── docs/
│   └── index.html                             ← drop-in replacement (full v1.8.0 rebuild)
├── configuration/
│   └── Cadence-FerrisSweep_v1_8_0.vil         ← new file (alongside the old v1.5.0)
└── UPDATE_GUIDE.md                            ← this file
```

## How to apply

### 1. Copy files into the repository

From the unpacked ZIP, copy each file to the matching location in your
local Cadence checkout:

```bash
cp README.md CHANGELOG.md VERSIONING.md ROADMAP.md /path/to/cadence/
cp docs/index.html                              /path/to/cadence/docs/
cp configuration/Cadence-FerrisSweep_v1_8_0.vil /path/to/cadence/configuration/
```

### 2. Remove the old interactive viewer

Cadence v1.8.0 consolidates the design documentation and the interactive
layer reference into a single `docs/index.html`. The standalone
`cadence-viewer-v1.5.0.html` is no longer maintained:

```bash
rm /path/to/cadence/docs/cadence-viewer-v1.5.0.html
```

The new `docs/index.html` contains keyboard visualisations for all 13
layers (auto-generated from the v1.8.0 `.vil`), the full Tap Dance and
Macro tables, the design philosophy, the layer access map, and firmware
notes — everything that used to live in the viewer plus everything from
the old `index.html`, on one page.

### 3. Keep the old configuration file

The previous `configuration/Cadence-FerrisSweep_v1_5_0.vil` stays in
place as version history — do not delete it. Each release ships its own
`.vil` next to the older ones; this gives every prior version a stable
reference point.

### 4. Verify

```bash
cd /path/to/cadence
git status        # see exactly what changed
git diff          # review every modification
```

Sanity checks:

- `grep -r "v1.5.0" .` should return only intentional historical
  references (CHANGELOG / VERSIONING entries describing the v1.5.0
  release, the "unchanged from v1.5.0" mention in firmware notes).
- `grep -r "Cadence-FerrisSweep_v1_5_0" .` likewise.
- `grep -r "cadence-viewer" .` should return zero results — the link
  is removed from README.md and the file is gone.
- The badge in README.md should read v1.8.0 / 49/64 TDs.
- Open `docs/index.html` in a browser: hero says v1.8.0, the green
  "What's new in v1.8.0" callout sits above the TOC, the L10 layer
  card has a "v1.8.0 · 3 new TDs" pill and shows ä/ü/ö marked on the
  A/U/O positions.

### 5. Commit, tag, release

```bash
git add -A
git commit -m "feat(l10): direct umlaut access via TD(48/49/50)

Adds TD(48/49/50) for ä/ü/ö (tap) and Ä/Ü/Ö (hold) on the A/U/O
positions of L10. Macros M16/17/18 carry the Shift+RAlt sequences.
TAP_DANCE_ENTRIES raised from 48 to 64.

The version jump from v1.5.0 to v1.8.0 reflects three internal
configuration revisions (v1.6, v1.7, v1.8) used to test the umlaut
work. v1.6 and v1.7 surfaced false-trigger and modifier-stickiness
issues during daily use and were not published. v1.8 is the first
revision that resolves all known issues.

Documentation consolidated: docs/index.html now contains the full
design reference plus keyboard visualisations for all layers. The
separate cadence-viewer-v1.5.0.html is removed.

The previous \`\"\` dead key path on L10 remains unchanged.
"

git tag v1.8.0
git push origin main
git push origin v1.8.0

gh release create v1.8.0 \
  "configuration/Cadence-FerrisSweep_v1_8_0.vil#Cadence-v1.8.0.vil" \
  --title "v1.8.0 — Direct umlaut access on L10" \
  --notes-file CHANGELOG.md
```

## Rebuilding docs/index.html later

`docs/index.html` was generated programmatically from the `.vil`. If you
make further `.vil` changes that affect layer content (key positions,
new TDs, new macros) and want the keyboard visualisations to reflect
those changes, hand-edit the HTML or request an updated rebuild for the
next release.
