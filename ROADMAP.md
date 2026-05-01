# Cadence Roadmap

## v1.5.0 — Completed ✓

- [x] **Sweep adaptation of Cadenza** — Colemak-DH base, Tap Dance HRM,
  Frequency+Strength symbol layout, bilateral layer access, all preserved
  from Cadenza v1.0.0
- [x] **Thumb-cluster reduction** — Esc/Del relocated into layers, L6 via
  Bsp+Spc chord activation
- [x] **L11 Workspaces** — single unified WM layer with full WS 1–10
  numpad map, focus switching, window movement, Kill / Float / Fullscreen
- [x] **L12 Firmware Control** — `QK_BOOT` and `QK_REBOOT` with deliberate
  safety design: long-hold (500 ms) on outer pinky-top, then a separate
  home-row key press required
- [x] **L1 Media simplified** — RGB controls dropped (Sweep has no RGB),
  layer renamed from "RGB & Media" to "Media"
- [x] **Backtick at three positions** — L4 BotL pinky, L9 BotL middle, L9
  BotR middle (`~`)
- [x] **€ on L10** — replaces duplicated ß slot
- [x] **Pipe TD on L9** — TD45 tap=`|` / hold=` | `
- [x] **L2 Ctrl+Arrow ordering** — corrected to match NEIO convention
  on the row directly below
- [x] **L5 inner column cleanup** — `=` removed from G-position; "no
  inner column for layer content" now holds without exception
- [x] **QMK mouse settings tuned** — mouse / scroll behaviour configured
  in the `.vil` settings section
- [x] **Documentation suite** — README, VERSIONING, CHANGELOG, ROADMAP,
  CONTRIBUTING, design documentation HTML, interactive layer viewer

---

## v1.x — Active / Planned

### v1.5.x — Stabilisation (PATCH)

- [ ] **Real-world tipping term data** — validate 200 / 250 ms defaults
  for HRM and the 500 ms terms on TD46 / TD47 (L12 access). Adjust if
  false triggers or missed holds appear during extended daily use.

- [ ] **L6 chord activation feel** — verify the Bsp+Spc chord triggers
  reliably without false Backspace events when typing fast. Adjust LT4
  tipping term if needed.

- [ ] **L12 Firmware Control safety review** — after extended use,
  confirm that the 500 ms hold on Q / `'` plus a separate home-row press
  has never produced an accidental `QK_BOOT` or `QK_REBOOT`. If any false
  trigger occurs, consider adding combo-based confirmation (e.g. require
  L+R simultaneous press of the two `QK_REBOOT` positions).

- [ ] **WM keybind validation** — confirm that `⌘+←/↓/↑/→` for focus
  switching, `⌘⇧+←/↓/↑/→` for window movement, `⌘⇧+Q` for Kill,
  `⌘+Spc` for Float, and `⌘+F` for Fullscreen match the actual
  i3 / Sway / macOS configuration in use.

- [ ] **QMK mouse settings — document semantic intent** — the v1.5
  settings section uses numeric Vial setting IDs (1, 2, 3 … 27) that
  are not self-documenting in the `.vil` format. Document the mapping
  from numeric ID to QMK setting name (acceleration enable, base speed,
  scroll speed, etc.) for future reference and easier review.

### v1.6.0 — New features (MINOR)

- [ ] **Key Overrides** — 32 slots completely free. Low-hanging fruit:
  `Shift + Bsp → Del` (standard ergonomic habit), `Shift + Esc → ~`
  (common in vim). Does not consume any TD slot. Evaluate after v1.5.x
  stabilisation.

- [ ] **Combos** — 31 slots free (1 used: `M-Btn1 + M-Btn2 → M-Btn3` on
  L7 thumb cluster, useful for Linux paste-on-middle-click). Natural
  candidates for additional combos: simultaneous `J + K` → Esc (vim
  pattern), `S + D` → `Ctrl+S` (save). Requires careful testing to avoid
  false triggers with Colemak-DH bigrams.

- [ ] **TD slot 10 / 21** — only two free TD slots remaining (TD10, TD21).
  Reserve for future high-value action keys; do not allocate without
  clear use-case.

- [ ] **Macro slots 16–31** — 16 free macro slots available. Candidates:
  common email signatures, frequent file paths, project-specific snippets.
  Define on demand rather than pre-allocating.

- [ ] **L13–L15 future layers** — three layer slots remain. Possible uses:
  a second international set (Cyrillic / French / Spanish), an
  app-launcher layer, a date / time / unit-conversion macro layer.
  Decide based on actual usage gaps after v1.5.x stabilisation.

---

## v2.0.0 — QMK migration (MAJOR)

The most significant planned evolution. Cadence v1.5.0 is fully specified
and verified — the natural moment to port from Vial's EEPROM-based config
to a proper `keymap.c` source file.

**Benefits gained:**
- Full git history of every key change
- Leader key sequences (macros without using macro slots)
- Combo definitions in code (no timing risk from Vial UI)
- Key override logic in C (conditional, layer-aware)
- Reproducibility: one `.uf2` = complete keyboard, no EEPROM dependency
- Unlimited macro content (not limited to Vial macro slots)
- Self-documenting QMK settings — no opaque numeric IDs

**Migration approach:**
- Use `Cadence-FerrisSweep_v1_5_0.vil` as the authoritative source of truth
- Generate `keymap.c` systematically from the JSON rather than by hand
- Keep Vial support enabled (via `vial_enable = true` in `rules.mk`) so
  the Vial UI can still be used for live experimentation — changes that
  survive testing get committed back to `keymap.c`
- Tag `v2.0.0` once `keymap.c` is the canonical source and the `.vil`
  file is demoted to a convenience export

**Classification as MAJOR:** the migration itself changes no key
behaviour, but the source-of-truth moves from EEPROM to firmware — any
`.vil` file from v1.x will no longer be the canonical config. This
warrants a MAJOR bump as a clear signal to users.

---

## Cross-family considerations

Cadence is part of a layout family:

- [Cadenza](https://github.com/one7two99/cadenza) — 36-key Corne Choc, the daily driver
- **Cadence** — 34-key Ferris Sweep, this project
- *Sonata* — 28-key sister project, currently in v2.0 redesign
- *Coda* — 22-key minimal concept

When a design decision is taken in one project that has implications for
muscle memory across the family (e.g. moving an HRM, reassigning a layer
access key), the change should be evaluated against the other family
members. This is especially relevant for Cadence ↔ Cadenza: anyone using
both keyboards should not have to relearn anything when switching.

The current v1.5.0 state is fully consistent with Cadenza on every shared
position — Bottom Row layer access, Home Row HRMs, Frequency+Strength
symbols, Path TD, Bracket pairs.

---

## Community Wishlist

Open a Discussion tagged `roadmap` to add yours.

| Idea | Raised by | Status |
|---|---|---|
| *(be the first)* | — | — |
