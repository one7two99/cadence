<div align="center">
  <h1>Cadence</h1>
  <p>
    <img src="https://img.shields.io/badge/version-1.11.0-brightgreen?style=flat-square" alt="Version">
    <img src="https://img.shields.io/badge/keyboard-Ferris%20Sweep-blue?style=flat-square" alt="Keyboard">
    <img src="https://img.shields.io/badge/firmware-Vial%20%2F%20QMK-orange?style=flat-square" alt="Firmware">
    <img src="https://img.shields.io/badge/base-Colemak--DH-purple?style=flat-square" alt="Base">
    <img src="https://img.shields.io/badge/tap%20dances-54%20%2F%2064-yellow?style=flat-square" alt="Tap Dances">
    <img src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square" alt="License">
  </p>
</div>

---

> *Cadence (n.): the rhythm of a movement, the measured fall of a phrase — the same musical lineage as Cadenza, condensed.*

**Cadence** is a 34-key split keyboard layout for the [Ferris Sweep](https://github.com/davidphilipbarr/Sweep), built on [Colemak-DH](https://colemakmods.github.io/mod-dh/) and configured in [Vial](https://get.vial.today/). It is the Sweep adaptation of the [Cadenza](https://github.com/one7two99/cadenza) layout (36-key Corne Choc) — same design philosophy, same muscle memory, two thumb keys less.

> *Cadenza without compromise — minus two thumbs.*

---

## ✦ Heritage

Cadence inherits the entire Cadenza design philosophy:

- **Per-finger Home Row Mods** via Tap Dance (200 ms index/middle, 250 ms ring/pinky)
- **Frequency + Strength symbol layer** — high-frequency operators on strongest fingers
- **Bilateral layer access** — most modal layers reachable from either hand
- **No inner column for layer content** — G/M never carry layer content
- **Vertical movement only** for layer access — no lateral stretches
- **NEIO = ←↓↑→** convention on every directional layer

Cadence diverges only where the Sweep's reduced key count requires it.

---

## ✦ What is different from Cadenza

The Ferris Sweep has **34 keys** (30 alpha + 4 thumb) versus the Corne Choc's 36 (30 alpha + 6 thumb). The two missing thumb keys force several structural decisions, which Cadence solves through Tap-Dance triggers and bilateral layer access:

| Cadenza (36) | Cadence (34) | Rationale |
|---|---|---|
| Esc on left thumb outer | Esc on Bsp-thumb (L1, L7) | Reachable via thumb-position layer holds |
| Del on right thumb outer | Del relocated within layers | Reassigned to layers that need it |
| L6 F-Keys via Hold Del | L6 F-Keys via **Hold F or Hold U** bilateral | Middle Top — strong fingers, low-frequency letters |
| L1 RGB & Media | merged into **L6 Fn + Media** | Sweep has no RGB; F-Keys + media combined into single layer |
| L11 (WS Quick) + L12 (WS Full) | **L8 Tiling WM** (consolidated) | Single unified WM layer |
| (no firmware control layer) | **L11 Firmware Control** | Bootloader + reboot via long pinky-top hold (500 ms) |
| (separate International layer) | **L1 Overflow + International** via Hold Tab | Tab on the inner left thumb makes umlauts maximally accessible |
| (separate Symbol layer) | **L12 Symbols** (NEW in v1.11) via Hold Bsp | Redesigned with right-thumb access asymmetry |

Everything else — Colemak-DH base, Tap Dance HRM, frequency-driven symbol placement, bilateral layer access, the Code & CLI macros, the dead-key fallbacks — is identical or preserved.

The Sweep adaptation is **not a downgrade**: it removes redundant features (RGB on a non-RGB board, two near-identical WM layers) and replaces dedicated thumb keys with Tap-Dance triggers that cost nothing in muscle memory.

---

## ✦ Highlights

- **Home Row Mods via Tap Dance** — per-key tipping terms (250 ms ring/pinky · 200 ms index/middle)
- **11 reachable layers** (13 in firmware) — Base, International, Numbers, Navigation, Mouse, Fn+Media, Code & CLI, Tiling WM, Brackets, Firmware Control, Symbols
- **Spc Tap-Hold-TapHold (TD(21))** — `tap = Space`, `hold = Navigation`, `tap+hold = Mouse` — three layer functions on a single thumb position
- **Tab Tap-Hold (TD(10))** — `tap = Tab`, `hold = International` — Tab remains a normal character; umlauts via thumb hold
- **Bilateral layer access** — Fn+Media (F+U), Code & CLI (W+Y), Tiling WM (Z+/), Brackets (X+.) — same finger on both hands, same row
- **L7 Code & CLI** — `||` · `2>&1` · `&&` · `|` (tap) / ` | ` (hold) · `/` / `~/` / `../` · `$()` / `${}` · `!=` / `==` · `=>` / `->` · `$?` · `` ` `` · `~` · `\`
- **L1 Overflow + International** — direct umlaut TDs (ä/ö/ü on A/O/U positions, hold = capital), `"` dead key fallback, ß (`RAlt+S`), € (`RAlt+5`), `'` literal
- **L8 Tiling WM** — WS 1–10 tap=go / hold=move (numpad memory) · focus and window-move on right hand · Kill / Float / Fullscreen on thumbs
- **L11 Firmware Control** — `QK_BOOT` and `QK_REBOOT` symmetrically placed, accessible only via deliberate long-hold (500 ms) pinky-top combination
- **L12 Symbols (NEW in v1.11)** — redesigned symbol layer with right-thumb access asymmetry, sharing the design specification with Sonata v3.x
- **Mouse settings tuned** — QMK mouse acceleration / scroll behaviour configured in the `.vil`

---

## ✦ Layer Overview

| # | Layer | Access | Purpose |
|---|---|---|---|
| L0 | Base | — | Colemak-DH + Tap Dance HRM |
| L1 | Overflow + International | Hold **Tab** | direct **ä/ö/ü** TDs (tap=lower, hold=capital) · `"` dead key · ß · € · `'` |
| L2 | (Symbols, deprecated) | — | replaced by L12 — kept in firmware for cleanup later |
| L3 | Numbers | Hold **Ent** | Numpad on left · operators · `0` on Spc-thumb · `-` on Tab-thumb |
| L4 | Navigation | Hold **Spc** | Arrows · Home/End/PgUp/PgDn · Word-skip · Tab on Ent-thumb for repeated Tab |
| L5 | Mouse | **Spc tap + hold** | Pointer · Scroll · Buttons — tap then hold Spc to activate |
| L6 | Function Keys + Media | Hold **F** *or* Hold **U** | F1–F12 (left, numpad-spatial) · media controls (right hand) |
| L7 | Code & CLI | Hold **W** *or* Hold **Y** | Shell operators · path navigation TD · `\|` (tap) / ` \| ` (hold) · `` ` `` · `~` · `\` · Tab/Esc on thumbs |
| L8 | Tiling WM | Hold **Z** *or* Hold **/** | WS 1–10 (numpad memory) · focus · window move · Kill / Float / Fullscreen |
| L9 | Brackets | Hold **X** *or* Hold **.** | `(` `)` `[` `]` `<` `>` `{` `}` — bilateral mirror |
| L10 | Clipboard | — | layer present, no trigger by user choice |
| L11 | Firmware Control | **Long-hold (500 ms) Q** *or* Long-hold **'** | `QK_BOOT` (bootloader) · `QK_REBOOT` |
| L12 | Symbols (NEW) | Hold **Bsp** | redesigned symbol layout — see [`L4-Symbol-Layer.html`](docs/L4-Symbol-Layer.html) |

### Access key principle

Access keys in v1.11 are assigned by **usage frequency × ergonomic quality × hold-detection safety**, with one critical refinement learnt from v1.9: layers used heavily during HRM-required workflows (especially Mouse) must not block the active hand's Home Row Mods. This is solved by putting Mouse on a Tap-Dance carrier (Spc tap+hold) instead of a bilateral letter trigger.

The remaining bilateral letter pairs use **finger-symmetric** triggers — same finger on both hands, same row — placed on letters whose frequency is low enough for clean hold-detection: F+U (Middle Top), W+Y (Ring Top), Z+/ (Pinky Bottom), X+. (Ring Bottom). G and M never carry layer content. The **outer pinky-top positions (Q and `'`)** are deliberately reserved for the rarely-used Firmware Control layer — uncomfortable enough to prevent accidental activation, paired with an unusually long 500 ms hold term.

---

## ✦ Design Decisions

**Spc as Tap-Dance carrier (TD(21)):** `tap = Space, hold = Navigation, tap+hold = Mouse`. The tap+hold pattern triggers when Spc is tapped, then immediately pressed again and held. This three-way differentiation eliminates v1.9's HRM-blocking issue: on Mouse, both hands are free to use Home Row Mods (Ctrl for multi-select, Shift for range-select). The same key carries the two most-used cursor-related layers, semantically related ("Spc = cursor work").

**Tab as Tap-Dance carrier (TD(10)):** `tap = Tab, hold = International`. International is one of the most frequently used layers when writing German prose; placing it on a single thumb hold makes it maximally accessible. Tab as a character remains directly available (tap), and inside L4 Navigation and L7 Code & CLI it is also placed on the Ent-thumb for repeated Tab sequences (form navigation, shell auto-complete, code indentation).

**Frequency + Strength (L12 Symbols):** Symbols ranked by daily usage frequency in German IT writing, then assigned to fingers in strength order, weighted by the position-quality penalty for the right-thumb-anchored hand. `=` and `-` on thumbs (most-frequent operators on strongest positions). Bracket pairs as Tap Dance on right top. Identical specification shared with Sonata v3.x.

**F/U for Fn+Media (L6):** Middle fingers, top row. Strong fingers, low-frequency letters for safe hold-detection. F1–F12 in numpad-spatial layout on the left (matches L_NUM and L_WM positions for muscle-memory transfer); media controls on the right.

**X/. for Brackets (L9):** Ring Bottom. Moved from D+H in v1.9.0 — D and H are common letters (~5%), which made the Brackets layer prone to false-positive hold-detection during normal typing. X and . are far less frequent — cleaner hold-detection without per-key tapping-term tuning.

**Z// for Tiling WM (L8):** Pinky Bottom. Both letters very rare in DE+EN — safest hold-detection of all bilateral pairs. WS 1–10 in numpad spatial layout on the left (matches L_NUM positions for muscle-memory transfer).

**L11 Firmware Control — deliberate exception to "no pinky-top hold":** The Bootloader and Reboot functions need to be reachable but must never trigger by accident. They sit on Q (left pinky top) and `'` (right pinky top) with a **500 ms hold term** (more than double the standard 200 ms). The combination of an uncomfortable position and an unusually long hold serves as a safety mechanism. Within L11, both `QK_BOOT` and `QK_REBOOT` are placed on home-row middle positions, mirrored on both hands — requiring two deliberate steps (hold to enter the layer, then a separate key press) before the firmware command fires.

**Path-navigation TD on L7 (TD29):** Tap = `/`, hold = `~/`, double-tap = `../`. A complete filesystem path can be typed without leaving the layer.

**Pipe TD on L7 (TD45):** Tap = `|`, hold = ` | ` (with surrounding spaces). Both pipe variants on the strongest left index position.

**Direct umlaut TDs on L1 (TD48/49/50):** Tap = `ä` / `ü` / `ö`, hold = `Ä` / `Ü` / `Ö`. Mnemonically placed on the A / U / O positions. The `"` dead key (TD33) remains available as a fallback for typing systems where the AltGr-shortcut is not desired (e.g. text fields that consume AltGr modifiers). The hold is implemented as a macro (M16/M17/M18) because Tap Dance hold slots accept only a single Vial keycode, while a capital umlaut requires `RShift+RAlt+letter`.

**Backtick reachability:** Backtick is reachable on L12 (right ring top via TD) and within L7 Code & CLI. Sufficient access for Markdown code-fences, JS template literals, and shell command substitution.

**No inner column for layer content:** G and M require a lateral inward index stretch — the same problem Colemak-DH solves for B and H. Cadence preserves Cadenza's extension: G/M only carry their letters and `App/Menu` on hold, never layer content.

---

## ✦ Installation

### Requirements

- Ferris Sweep (any RP2040-compatible variant)
- Vial-compatible firmware **with `TAP_DANCE_ENTRIES = 64`** (Cadence v1.11 uses TD(57); the default Vial-Sweep build ships with 48)
- OS keyboard layout set to **US International** (required for dead keys and `RAlt` combinations)

### Step 1 — Flash Vial firmware

Cadence v1.11 uses 54 Tap Dance slots and requires a firmware build with at least 58 entries. The default Vial-Sweep firmware ships with 48 slots, so a custom build with `TAP_DANCE_ENTRIES = 64` is required:

```bash
# Clone Vial-QMK
git clone https://github.com/vial-kb/vial-qmk.git
cd vial-qmk
make git-submodule

# Verify keyboards/ferris/sweep/keymaps/vial/config.h
# Should contain: #define TAP_DANCE_ENTRIES 64

# Build
qmk compile -kb ferris/sweep -km vial
```

Flash via RP2040 drag-and-drop:
1. Double-tap the reset button → `RPI-RP2` drive appears
2. Copy the generated `.uf2` file to the drive
3. Repeat for the other half

### Step 2 — Load the layout

1. Open Vial desktop app, connect keyboard via USB
2. **File → Load saved layout** → select `configuration/Cadence-FerrisSweep_v1_11_0.vil`
3. Confirm all layers loaded correctly

### Step 3 — Verify OS layout

Set your OS keyboard layout to **US International**. This is required for:

- `RAlt+S` → ß
- `RAlt+5` → €
- `RAlt+Q/Y/P` → ä/ü/ö (and `Shift+RAlt+Q/Y/P` → Ä/Ü/Ö, used by L1 hold-macros)
- Dead key `"` (Shift+Quote) → ä, ö, ü when followed by a vowel

---

## ✦ Resource Budget

| Resource | Used | Available | Free |
|---|---|---|---|
| Tap Dance slots | 54 | 64 | 10 |
| Macro slots | 19 | 32 | 13 |
| Key Overrides | 0 | 32 | 32 |
| Combos | 0 | 32 | 32 |
| Layers | 13 in firmware (11 reachable) | 16 | 3 |

---

## ✦ Documentation

| Document | Description |
|---|---|
| **[docs/index.html](docs/index.html)** | Full design documentation and layer reference — keyboard visualisations for all 13 layers, design decisions, design principles, complete Tap Dance and Macro tables, firmware notes |
| **[docs/L4-Symbol-Layer.html](docs/L4-Symbol-Layer.html)** | Dedicated specification for the L12 Symbol layer — design rationale, position assignments, shared with Sonata v3.x |
| **[VERSIONING.md](VERSIONING.md)** | Semantic versioning policy and version history |
| **[CHANGELOG.md](CHANGELOG.md)** | Detailed change log including the Cadenza heritage |
| **[ROADMAP.md](ROADMAP.md)** | Planned milestones — patches, features, QMK migration |

---

## ✦ Versioning

Cadence follows [Semantic Versioning](https://semver.org/) — `vMAJOR.MINOR.PATCH`.

| Increment | When |
|---|---|
| **PATCH** | Bug fix — no key moves, no new features |
| **MINOR** | New layer, macro, or Tap Dance added |
| **MAJOR** | Existing key behaviour changes — muscle memory impact |

Cadence's version numbers track the underlying Ferris Sweep configuration version 1:1 — `v1.11.0` of the layout corresponds to Vial config `Cadence-FerrisSweep_v1_11_0.vil`.

Full versioning policy and change log: [VERSIONING.md](VERSIONING.md)

---

## ✦ Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Ports, language variants, and usage reports are welcome. Open a Discussion to suggest future features.

---

## ✦ License

Designed by **one7two99** · [MIT](LICENSE) · 2026

> *Based on [Cadenza](https://github.com/one7two99/cadenza) by one7two99 · [Colemak-DH](https://colemakmods.github.io/mod-dh/) by stevep99 · Inspired by [Miryoku](https://github.com/manna-harbour/miryoku)*

> *34 keys. Two thumbs less. Same rhythm.*
