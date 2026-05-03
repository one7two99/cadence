# Cadence Roadmap

## v1.11.0 — Completed ✓

- [x] **Mouse-on-thumb redesign** — L5 Mouse moved from F+U bilateral
  to `Spc tap+hold` (TD(21)). Solves the v1.9 ergonomic issue where
  bilateral letter-pair triggers blocked the active hand's Home Row
  Mods, making `Ctrl+Click` multi-select impossible to perform with
  one hand on the keyboard.
- [x] **Tab as Tap-Dance carrier** — TD(10) `tap = Tab, hold = MO(1)`.
  Tab remains a normal character; International layer moved from
  Spc-hold to Tab-hold for maximum thumb-accessibility.
- [x] **Spc as three-way Tap-Dance** — TD(21) `tap = Space,
  hold = Navigation, tap+hold = Mouse`. Three layer functions on
  a single thumb position.
- [x] **L12 Symbols (NEW)** — completely redesigned symbol layer
  replacing the deprecated L2. Right-thumb access asymmetry: the
  layer is activated by Bsp-hold, so high-frequency symbols are
  placed on the freer left hand and on right-top rows. Specification
  shared with Sonata v3.x via dedicated `L4-Symbol-Layer.html`.
- [x] **L9 Brackets relocated to X+.** — moved from D+H bilateral
  (Index Bottom) to X+. (Ring Bottom). D and H are common letters
  (~5%); X and . are far less frequent. Cleaner hold-detection
  without per-key tapping-term tuning.
- [x] **L6 Fn+Media access moved to F+U** — replaces v1.9's C+,
  bilateral. Since F and U are no longer the Mouse trigger, they
  take over L6 access. C and , become plain letter keys.

---

## v1.9.0 — Completed ✓

- [x] **Sonata-aligned layer system** — L1–L9 reorganised to mirror
  Sonata v3.0's numbering. Future migration to Sonata hardware
  becomes a "learn the new alpha grid" exercise rather than a
  complete relearning of the layer architecture.
- [x] **L1 Media + L6 F-Keys merged** — single "L6 Fn + Media" layer
  with bilateral C+, access. Eliminates the v1.8 Bsp+Spc chord
  trigger for F-Keys.
- [x] **L10 Clipboard intentionally without trigger** — layer remains
  in firmware for future activation; user opts out for now.
- [x] **X and . MO-holds removed** — both were L9 Code & CLI triggers
  in v1.8.0; now plain letter keys.
- [x] **Inner column rule verified** — all 12 modal layers leave the
  inner column (G/M positions) empty.

---

## v1.8.0 — Completed ✓

- [x] **Direct umlaut access on L10** — TD(48/49/50) for ä/ü/ö (tap)
  and Ä/Ü/Ö (hold) on the A/U/O positions; macros M16/17/18 carry
  the Shift+RAlt key sequences. The `"` dead key path remains
  unchanged.
- [x] **Firmware capacity expanded** — `TAP_DANCE_ENTRIES` raised
  from 48 to 64. 15 TD slots remain free for future high-value
  action keys.

---

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
  CONTRIBUTING, design documentation HTML with interactive layer reference

---

## v1.x — Active / Planned

### v1.11.x — Stabilisation (PATCH)

- [ ] **Spc Tap+Hold pattern feel** — verify the `tap+hold` Mouse
  trigger works reliably without false activations during normal
  typing. The two-step pattern (tap then hold) should be distinct
  enough from a normal Space tap, but extended daily use will tell.
  Adjust TD(21) tapping term if needed.

- [ ] **Tab Tap-Hold for International** — verify TD(10) hold for
  L1 activation feels natural during German prose typing. If
  occasional unintended Tab insertion appears (Tab tap when L1 hold
  was intended), increase tapping term.

- [ ] **L9 Brackets on X+. — hold-detection in code** — confirm that
  the new Ring Bottom trigger pair has cleaner hold-detection than
  v1.9's D+H. X and . are low-frequency letters in DE+EN; this should
  hold true in practice. If false-triggers appear during code editing,
  reconsider per-key tipping terms.

- [ ] **L12 Symbol layer in daily use** — the new layer is shared with
  Sonata v3.x; first extended use will reveal whether the access
  asymmetry (high-frequency symbols on left hand and right-top) feels
  natural in real coding sessions. Watch for: bracket pair access
  speed, frequency of returning to L7 Code & CLI for missing operators,
  ergonomic comfort during long symbol-heavy sessions.

- [ ] **L2 cleanup** — the deprecated L2 still contains the v1.9 Symbol
  layer content. After verifying L12 covers all needed symbols,
  L2 should be cleared in a v1.11.x patch. Currently kept in firmware
  to avoid premature deletion.

- [ ] **Real-world tipping term data** — validate 200 / 250 ms defaults
  for HRM and the 500 ms terms on TD46 / TD47 (L11 access). Adjust if
  false triggers or missed holds appear during extended daily use.

- [ ] **L11 Firmware Control safety review** — after extended use,
  confirm that the 500 ms hold on Q / `'` plus a separate home-row
  press has never produced an accidental `QK_BOOT` or `QK_REBOOT`. If
  any false trigger occurs, consider adding combo-based confirmation
  (e.g. require L+R simultaneous press of the two `QK_REBOOT`
  positions).

- [ ] **WM keybind validation** — confirm that `⌘+←/↓/↑/→` for focus
  switching, `⌘⇧+←/↓/↑/→` for window movement, `⌘⇧+Q` for Kill,
  `⌘+Spc` for Float, and `⌘+F` for Fullscreen match the actual
  i3 / Sway / macOS configuration in use.

- [ ] **L1 umlaut TD validation** — confirm that TD(48/49/50) trigger
  reliably under fast typing without the modifier-stickiness or false-
  trigger issues that surfaced in v1.6 / v1.7. If problems re-appear,
  re-evaluate the macro encoding (currently `down`/`tap`/`up` sequence)
  or consider per-TD tipping term adjustment.

- [ ] **QMK mouse settings — document semantic intent** — the settings
  section uses numeric Vial setting IDs (1, 2, 3 … 27) that are not
  self-documenting in the `.vil` format. Document the mapping from
  numeric ID to QMK setting name (acceleration enable, base speed,
  scroll speed, etc.) for future reference and easier review.

### v1.12.0 — New features (MINOR)

- [ ] **Key Overrides** — 32 slots completely free. Low-hanging fruit:
  `Shift + Bsp → Del` (standard ergonomic habit), `Shift + Esc → ~`
  (common in vim). Does not consume any TD slot. Evaluate after
  v1.11.x stabilisation.

- [ ] **Combos** — 32 slots free (the v1.5 M-Btn combo for middle-click
  was retired in v1.11; MB3 is now placed directly on the Spc-thumb of
  L5 Mouse instead). Natural candidates for re-adding combos:
  simultaneous `J + K` → Esc (vim pattern), `S + D` → `Ctrl+S` (save).
  Requires careful testing to avoid false triggers with Colemak-DH
  bigrams.

- [ ] **TD slot allocation** — 10 free slots remain (TD58–TD63 plus any
  retired TDs). Reserve for future high-value action keys; do not
  allocate without clear use-case.

- [ ] **Macro slots 19–31** — 13 free macro slots available. Candidates:
  common email signatures, frequent file paths, project-specific
  snippets. Define on demand rather than pre-allocating.

- [ ] **L13–L15 future layers** — three layer slots remain (or four if
  L2 is retired). Possible uses: a second international set (Cyrillic
  / French / Spanish), an app-launcher layer, a date / time / unit-
  conversion macro layer. Decide based on actual usage gaps after
  v1.11.x stabilisation.

---

## v2.0.0 — QMK migration (MAJOR)

The most significant planned evolution. Cadence v1.11.0 is fully
specified and verified — the natural moment to port from Vial's
EEPROM-based config to a proper `keymap.c` source file.

**Benefits gained:**
- Full git history of every key change
- Leader key sequences (macros without using macro slots)
- Combo definitions in code (no timing risk from Vial UI)
- Key override logic in C (conditional, layer-aware)
- Reproducibility: one `.uf2` = complete keyboard, no EEPROM dependency
- Unlimited macro content (not limited to Vial macro slots)
- Self-documenting QMK settings — no opaque numeric IDs
- Per-key `PERMISSIVE_HOLD` and `HOLD_ON_OTHER_KEY_PRESS` — currently
  only available globally in Vial. Per-key control would let Spc/Tab
  thumbs use aggressive hold-detection while HRMs keep conservative
  defaults.

**Migration approach:**
- Use `Cadence-FerrisSweep_v1_11_0.vil` as the authoritative source of truth
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
- *Sonata* — 28-key sister project (v3.0 released; L_SYM specification shared with Cadence v1.11)
- *Coda* — 22-key minimal concept

When a design decision is taken in one project that has implications for
muscle memory across the family (e.g. moving an HRM, reassigning a layer
access key), the change should be evaluated against the other family
members. This is especially relevant for Cadence ↔ Cadenza: anyone using
both keyboards should not have to relearn anything when switching.

The current v1.11.0 state diverges from Cadenza in the thumb-trigger
mechanics: Cadenza's six-thumb cluster does not need the Tap-Dance-
carrier patterns that Cadence v1.11 introduced for Mouse and
International. The Mouse-on-thumb solution is Sweep-specific and not
applicable to Cadenza. The L12 Symbol layer specification is, however,
fully shared with Sonata v3.x — these two projects can be treated as
specification-compatible at the symbol layer.

The L1 direct-umlaut TDs (TD48/49/50) introduced in v1.8 remain a
Cadence-specific addition; whether to backport them to Cadenza is a
decision for that project.

---

## Community Wishlist

Open a Discussion tagged `roadmap` to add yours.

| Idea | Raised by | Status |
|---|---|---|
| *(be the first)* | — | — |
