# Cadence

**A 32-key Colemak-DH layout for the Ferris Sweep, designed around per-key Tap Dance Home Row Mods, frequency-ranked symbols, and a Dead Key Hub for German + US-International completeness.**

Cadence is a daily-driver keyboard layout for [Ferris Sweep](https://github.com/davidphilipbarr/Sweep) hardware running [Vial](https://get.vial.today/) firmware. It is the descendant of [Cadenza](https://github.com/one7two99/cadenza) (36-key Corne) — adapted to the Sweep's four-thumb form by encoding layer access as Tap Dance triggers on the alpha keys rather than dedicated thumb keys.

The full design specification with per-layer rationale lives in [`docs/index.html`](docs/index.html). The version history is in [`CHANGELOG.md`](CHANGELOG.md).

---

## Quick start

1. **Build the Vial-QMK firmware** with `TAP_DANCE_ENTRIES = 64`. The default Vial-Sweep build ships with 48; Cadence uses 51 of 64 slots so a custom build is required.

   In `keyboards/ferris/sweep/keymaps/vial/config.h`:
   ```c
   #define TAP_DANCE_ENTRIES 64
   ```

2. **Flash the firmware** to your Sweep via QMK Toolbox or `qmk flash`.

3. **Load the layout** from [`configuration/Cadence-FerrisSweep_v1_12_2.vil`](configuration/) into Vial.

4. **Set your OS keyboard layout to US International** (with dead keys). Cadence's German and other accent support relies on US-International dead-key behaviour at the OS level.

---

## Layer overview

| # | Layer | Access | Purpose |
|---|---|---|---|
| L0 | Base | always active | Colemak-DH alphas with Tap Dance Home Row Mods |
| L1 | Overflow + International | Hold **Tab** | The Dead Key Hub — direct ä/ö/ü, all five US-Intl dead keys, ß, €, Esc |
| L2 | Symbols | Hold **Bsp** | Frequency-ranked operator and bracket layout |
| L3 | Numbers | Hold **Ent** | Numpad on left, ASCII operators on right, Tab on Tab-thumb |
| L4 | Navigation | Hold **Spc** | Arrows, word-skip, page-nav, CapsLock, Insert, Delete, ScrollLock, Pause |
| L5 | Mouse | Spc **tap+hold** | Pointer (NEIO), scroll, mouse buttons on thumbs |
| L6 | Fn + Media | Hold **F** *or* **U** | F1–F12 numpad-spatial, media controls, PrintScreen |
| L7 | Code & CLI | Hold **W** *or* **Y** | Shell operators, path navigation, expansions, comparisons, arrows |
| L8 | Tiling WM | Hold **Z** *or* **/** | Workspaces 1–10, focus, window-move, Kill / Float / Fullscreen |
| L9 | Brackets | Hold **X** *or* **.** | Tap-open / hold-close pairs, bilateral mirror |
| L11 | Firmware Control | Long-hold (500 ms) **Q** *or* **'** | `QK_BOOT` and `QK_REBOOT` only — safety-gated |

L10 (Clipboard) is in firmware without a trigger by user choice. L12 is empty (Vial format placeholder).

For the per-layer design rationale, the Tap Dance and Macro tables, and the cross-cutting design principles, see [`docs/index.html`](docs/index.html).

---

## Highlights

- **Per-key HRM tipping terms via Tap Dance** — 250 ms on pinky/ring (A, O), 200 ms on index/middle. Departs from Miryoku's single global term.
- **Spc Tap-Hold-TapHold** — `tap = Space`, `hold = Navigation`, `tap + hold = Mouse`. Three layer functions on a single thumb position.
- **Tab Tap-Hold** — `tap = Tab`, `hold = International`. Tab remains a normal character; umlauts via thumb hold.
- **Bilateral layer access** — Fn+Media (F+U), Code & CLI (W+Y), Tiling WM (Z+/), Brackets (X+.). Same finger on both hands, same row — symmetric muscle memory.
- **L1 Dead Key Hub** — all five US-International dead keys (`` ` ``, `'`, `"`, `^`, `~`) plus direct umlaut Tap Dances, plus ß and €, all centralised on one layer.
- **L7 Code & CLI** — Tap Dances for path navigation (`/` / `~/` / `../`), pipe with optional spaces, shell expansion, comparison, arrows; macros for `||`, `&&`, `2>&1`, `$?`.

---

## Why not standard Miryoku?

Cadence keeps Miryoku's core insight (layers via thumb holds, HRM on home row) and replaces parts that don't serve the use case:

- Miryoku's `MT()` HRM has one global tipping term; Cadence's per-key Tap Dance terms reduce false-trigger pressure on weaker fingers.
- Miryoku's symbol layer mirrors numpad positions for mnemonic value; Cadence's L2 ranks symbols by frequency × finger strength so the most-typed operators land on the strongest fingers.
- Miryoku has no native German or US-International support; Cadence's L1 covers it natively.
- Miryoku has no dedicated Code & CLI, Tiling WM, or Brackets layer; Cadence has all three with workflow-specific Tap Dances.

The trade-off: Cadence has more layers (11 reachable vs. ~6) and a higher learning curve. The bet is that the additional structure pays off after muscle memory is established.

A more thorough comparison lives in [`docs/index.html`](docs/index.html#vs-miryoku).

---

## Resource budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance | 51 | 64 |
| Macros | 19 | 32 |
| Layers (firmware) | 12 | 16 |
| Layers (reachable) | 11 | — |
| Combos | 0 | 32 |
| Key Overrides | 0 | 32 |

Combos and Key Overrides are unallocated — reserve capacity for future iteration.

---

## Documentation

- [`docs/index.html`](docs/index.html) — full design specification with per-layer rationale, TD/macro tables, design principles, appendices
- [`CHANGELOG.md`](CHANGELOG.md) — version history and design-process record
- [`ROADMAP.md`](ROADMAP.md) — open items and planned work
- [`VERSIONING.md`](VERSIONING.md) — semantic versioning policy and release workflow
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution guidelines

## Layout family

Cadence is one of four related layouts maintained by the same author:

- **Cadence** (32 keys, Ferris Sweep) — this layout, the daily driver
- **Cadenza** (36 keys, Corne) — the parent layout, frozen at v1.0
- **Sonata** (28 keys, no inner column) — sister project, shares the L2 Symbols specification
- **Coda** (22 keys, three columns per hand) — minimal concept

## License

[MIT](LICENSE)
