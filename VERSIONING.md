# Versioning

Cadence follows [Semantic Versioning](https://semver.org/) — `vMAJOR.MINOR.PATCH`.

---

## The three numbers

```
v MAJOR . MINOR . PATCH
  │        │       └── bug fix — no key moves, no behaviour change
  │        └────────── new feature — new layer, new macro, new TD
  └─────────────────── breaking change — existing key behaviour changes
```

### PATCH

Something was wrong and is now corrected. No key moved, no new feature added.
The layout feels identical except the broken thing works.

*Example: removing an accidentally placed `KC_KP_6` from L6.*

### MINOR

Something new was added that did not exist before: a new layer, a new macro,
a new Tap Dance slot. All existing keys and layers are completely untouched.
A user on the previous version can upgrade without relearning anything.

*Example: adding a new Firmware Control layer for `QK_BOOT` / `QK_REBOOT`
without touching any existing key behaviour.*

### MAJOR

An existing key on an existing layer changed its behaviour. Muscle memory
built on the previous version no longer applies. Upgrading requires
conscious retraining.

*Examples: moving an HRM to a different finger, changing the base layout,
reordering the numpad grid, swapping a thumb cluster assignment.*

---

## Version alignment with the Ferris Sweep configuration

Cadence's version numbers map **1:1** to the underlying Vial configuration
file. `Cadence v1.8.0` corresponds to `Cadence-FerrisSweep_v1_8_0.vil`.

This intentional alignment means: the version number on a release page is
also the version number stamped into the configuration file name. There is
no translation step, no "config version vs. release version" ambiguity.

---

## Initial release at v1.5.0 — why not v1.0.0?

Cadence is the Sweep adaptation of Cadenza and is published in lockstep with
the underlying Vial configuration revisions. The first five configuration
revisions (v1.0 through v1.5) were the Sweep adaptation itself: identifying
gaps, adding the Bsp+Spc chord for L6, restoring the backtick, replacing the
duplicated ß with €, removing accidental key assignments, consolidating the
two WM layers, and finally adding a Firmware Control layer with deliberate
safety design. Cadence v1.5.0 is the first state stable enough to publish
— and rather than renumber to v1.0.0, the configuration version is preserved
for traceability with the Sweep adaptation history.

From v1.5.0 onwards, all three semver numbers follow their full conventional
meaning as described above.

---

## Decision rules

### Increment PATCH when
- A macro produces wrong output and is corrected
- A tipping term is adjusted because it caused false triggers
- A key that should be empty was accidentally assigned something
- Documentation corrected, no `.vil` changes
- Mouse / scroll settings tuning that does not change keymap behaviour

### Increment MINOR when
- A new layer is added
- A new macro slot is filled
- A new Tap Dance is defined
- An empty key position gets a new assignment for the first time

### Increment MAJOR when
- Any home row mod finger assignment changes
- A thumb cluster key moves to a different layer
- An existing layer changes its purpose or structure
- The base layout changes
- A layer access key for an existing layer changes
- A layer's *number* changes (e.g. moving Workspaces from L11 to L12 or back)

---

## Version history

### v1.8.0 — 2026-05-02 — direct umlaut access on L10

MINOR — three new Tap Dances and three new macros add direct AltGr-based
ä/ü/ö (and capital Ä/Ü/Ö) access on L10, mnemonically placed on the
A / U / O positions. The existing `"` dead key path remains unchanged.

The version jump from v1.5.0 to v1.8.0 reflects three internal Vial
configuration revisions (v1.6, v1.7, v1.8) used to test different
combinations of Tap Dance placements, hold encodings, and macro timings
for the umlaut work. v1.6 and v1.7 surfaced issues during daily use
(false triggers, modifier-stickiness on capital holds, HRM interaction
edge cases) and were never published. v1.8.0 is the first revision in
this series that resolves all known issues and is stable in extended use.

The 1:1 alignment between version number and configuration file name is
preserved — analogous to v1.5.0 itself being the first public release
rather than v1.0.0.

Firmware change: `TAP_DANCE_ENTRIES` increased from 48 to 64 to
accommodate TD(50). 15 TD slots remain free.

### v1.5.0 — 2026-05-01 — initial public release

**Stability declaration.** First public release of Cadence as a standalone
project. All planned core layers are complete and verified. Future breaking
changes will be communicated via a MAJOR increment.

The relationship to Cadenza:

- Cadence inherits the Cadenza design philosophy in full
- Diverges only where the Sweep's 4-thumb-key constraint requires (see CHANGELOG.md)
- Cadence and Cadenza version numbers are independent — Cadence is not
  required to track Cadenza version increments

Detailed changes from the pre-release Sweep adaptation revisions: see
[CHANGELOG.md](CHANGELOG.md).

---

## Git workflow

```bash
# PATCH
git commit -m "fix(l9): correct TD(45) tipping term"
git tag v1.8.1
git push origin v1.8.1
gh release create v1.8.1 \
  "configuration/Cadence-FerrisSweep_v1_8_1.vil#Cadence-v1.8.1.vil" \
  --title "v1.8.1 — <short description>" \
  --notes-file release-notes.md

# MINOR
git commit -m "feat: add international preset for French"
git tag v1.9.0
git push origin v1.9.0
gh release create v1.9.0 \
  "configuration/Cadence-FerrisSweep_v1_9_0.vil#Cadence-v1.9.0.vil" \
  --title "v1.9.0 — <short description>" \
  --notes-file release-notes.md

# MAJOR
git commit -m "feat!: reassign thumb cluster positions"
git tag v2.0.0
git push origin v2.0.0
gh release create v2.0.0 \
  "configuration/Cadence-FerrisSweep_v2_0_0.vil#Cadence-v2.0.0.vil" \
  --title "v2.0.0 — BREAKING: <short description>" \
  --notes-file release-notes.md
```

The `!` after the type token (`feat!`, `fix!`) is the
[Conventional Commits](https://www.conventionalcommits.org/) convention for
signalling a breaking change — it pairs naturally with MAJOR semver increments.

---

## Configuration file naming convention

Configuration files follow the version number directly, for example:

```
Cadence-FerrisSweep_v1_5_0.vil
Cadence-FerrisSweep_v1_8_0.vil
Cadence-FerrisSweep_v1_8_1.vil
Cadence-FerrisSweep_v1_9_0.vil
Cadence-FerrisSweep_v2_0_0.vil
```

Dots replaced with underscores for filesystem compatibility. All configuration
files are kept in `configuration/` and attached as assets to their corresponding
GitHub release.
