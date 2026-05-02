<div align="center">
  <h1>Cadence</h1>
  <p>
    <img src="https://img.shields.io/badge/version-1.8.0-brightgreen?style=flat-square" alt="Version">
    <img src="https://img.shields.io/badge/keyboard-Ferris%20Sweep-blue?style=flat-square" alt="Keyboard">
    <img src="https://img.shields.io/badge/firmware-Vial%20%2F%20QMK-orange?style=flat-square" alt="Firmware">
    <img src="https://img.shields.io/badge/base-Colemak--DH-purple?style=flat-square" alt="Base">
    <img src="https://img.shields.io/badge/tap%20dances-49%20%2F%2064-yellow?style=flat-square" alt="Tap Dances">
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
- **Frequency + Strength symbol layer** — `=` on T (strongest left index), `$` on N (strongest right index)
- **Bilateral layer access** — L7/L8/L9/L10/L11 reachable from either hand
- **No inner column for layer content** — G/M never carry layer content
- **Vertical movement only** for layer access — no lateral stretches
- **NEIO = ←↓↑→** convention on every directional layer

Cadence diverges only where the Sweep's reduced key count requires it.

---

## ✦ What is different from Cadenza

The Ferris Sweep has **34 keys** (30 alpha + 4 thumb) versus the Corne Choc's 36 (30 alpha + 6 thumb). The two missing thumb keys force three structural decisions:

| Cadenza (36) | Cadence (34) | Rationale |
|---|---|---|
| Esc on left thumb outer | Esc on D-position (L2/L3 bottom row) | Index-finger-down during Hold-Space — reachable without leaving home |
| Del on right thumb outer | Del on right thumb inner (L2 / L6) | Reassigned within the layers that need it |
| L6 F-Keys via Hold Del | L6 F-Keys via **Bsp + Spc chord** | Hold Bsp → L4 active → Hold Spc-position → `MO(6)` → L6 |
| L1 RGB & Media | L1 **Media only** | Sweep has no RGB — feature dropped |
| L11 (WS Quick) + L12 (WS Full) | L11 **Workspaces** (consolidated) | Single unified WM layer, F/U → L11 |
| L hold → L12 | L is a plain key | No pinky-top hold — outside the Cadence philosophy (with one deliberate exception, see L12 below) |
| (no firmware control layer) | L12 **Firmware Control** | Bootloader + reboot, accessible only via long pinky-top hold (500 ms) — deliberately uncomfortable to prevent accidental triggering |

Everything else — Colemak-DH base, Tap Dance HRM, all 13 documented layers, Frequency+Strength symbols, bilateral layer access, the Code & CLI macros, the International dead-key layer — is identical or preserved.

The Sweep adaptation is **not a downgrade**: it removes redundant features (RGB on a non-RGB board, two near-identical WM layers) and replaces dedicated thumb keys with chord-based access that costs nothing in muscle memory.

---

## ✦ Highlights

- **Home Row Mods via Tap Dance** — per-key tipping terms (250 ms ring/pinky · 200 ms index/middle)
- **13 active layers** — alpha, media, navigation, mouse, symbols, numbers, F-keys, clipboard, brackets, code/CLI, international, workspaces, firmware control
- **Frequency + Strength symbols** — most-used symbol on strongest finger, identical ranking to Cadenza
- **Bilateral layer access** — L7/L8/L9/L10/L11 reachable from either hand
- **Code & CLI layer (L9)** — `||` · `2>&1` · `&&` · `|` (tap) / ` | ` (hold) · `/` / `~/` / `../` · `$()` / `${}` · `!=` / `==` · `=>` / `->` · `$?` · `` ` `` · `~` · `\`
- **International layer (L10)** — direct umlaut TDs (ä/ö/ü on A/O/U positions, hold = capital), `"` dead key fallback, ß (`RAlt+S`), € (`RAlt+5`), `'` literal — bilateral access
- **Tiling WM (L11)** — WS 1–10 tap=go / hold=move (numpad memory) · focus and window-move on right hand · Kill / Float / Fullscreen on thumbs
- **Firmware Control (L12)** — `QK_BOOT` and `QK_REBOOT` symmetrically placed, accessible only via deliberate long-hold pinky-top combination
- **Layer-6 chord activation** — Bsp + Spc → F-Keys, no pinky-top hold required
- **Mouse settings tuned** — QMK mouse acceleration / scroll behaviour configured in the `.vil`

---

## ✦ Layer Overview

| # | Layer | Access | Purpose |
|---|---|---|---|
| L0 | Base | — | Colemak-DH + Tap Dance HRM |
| L1 | Media | Hold **W** or Hold **Y** | Volume · Brightness · Play/Stop · CapsLock · PrtSc |
| L2 | Navigation | Hold **Space** | Arrows · Home/End/PgUp/PgDn · Word-skip · Esc · Del |
| L3 | Mouse | Hold **Tab** | Pointer · Scroll · Buttons |
| L4 | Symbols | Hold **Bsp** | Frequency+Strength symbol layout · `` ` `` · `/` |
| L5 | Numbers | Hold **Ent** | Numpad · operators · `0` on thumb |
| L6 | Function Keys | Hold **Bsp + Spc** chord | F1–F12 · Del |
| L7 | Clipboard | Hold **Z** *or* Hold **/** | Undo/Cut/Copy/Paste/Redo — symmetric, both hands |
| L8 | Brackets | Hold **C** *or* Hold **,** | `(` `)` `[` `]` `<` `>` `{` `}` — tap/hold, both hands · `\` |
| L9 | Code & CLI | Hold **X** *or* Hold **.** | Shell operators · path navigation TD · `\|` (tap) / ` \| ` (hold) · `` ` `` · `~` · `\` |
| L10 | International | Hold **D** *or* Hold **H** | direct **ä/ö/ü** TDs (tap=lower, hold=capital) · `"` dead key · ß · € · `'` |
| L11 | Workspaces | Hold **F** *or* Hold **U** | WS 1–10 (numpad memory) · focus · window move · Kill / Float / Fullscreen |
| L12 | Firmware Control | **Long-hold (500 ms) Q** *or* Long-hold **'** | `QK_BOOT` (bootloader) · `QK_REBOOT` |

### Access key principle

Access keys are assigned by **usage frequency × ergonomic quality**. The right thumb middle (Bsp) earns L4 Symbols because it requires no lateral movement. D/H (strongest index pair) earn L10 International because German umlauts appear in every sentence. F/U (middle fingers, top row) earn L11 because workspaces are reflex-frequency. G and M never carry layer content. The **outer pinky-top positions (Q and `'`)** are deliberately reserved for the rarely-used Firmware Control layer — a position that is uncomfortable enough to prevent accidental activation, paired with an unusually long 500 ms hold term.

---

## ✦ Design Decisions

**Layer-6 via thumb chord:** The Sweep adaptation has no spare thumb for L6 access. Holding `'` (right pinky top) was rejected as outside the Cadence philosophy — pinky-top holds are uncomfortable. Instead: Hold Bsp (→ L4 active) then hold Spc-position (which on L4 is `MO(6)`) → L6. The order matters: Bsp first, then Spc. The reverse order produces a literal Backspace, which is acceptable.

**Frequency + Strength (L4 Symbols):** Symbols are ranked by daily usage frequency in German IT writing, then assigned to fingers in strength order. `=` (rank 1) sits on T (strongest left index). `&` (rank 8) sits on O (weakest right pinky). Identical to Cadenza.

**W/Y for Media (L1):** Ring fingers, top row. Leaves both thumbs free for `PrtSc` (left) and `Mute / Play-Stop` (right). The full Cadenza rationale (no thumb conflict on the access layer) holds.

**D/H for International (L10):** Index fingers, bottom row. Bilateral pattern — `"` dead key on both T (left, hold via H) and N (right, hold via D) for umlaut input regardless of which hand triggers the layer. ß and € use direct `RAlt` keycodes — no macros.

**F/U for Workspaces (L11):** Middle fingers, top row. Replaces the Cadenza split between L11 (Quick) and L12 (Full). Cadence merges them: F/U give the full WS 1–10 numpad map. The L key carries no hold function — it is a plain letter.

**L12 Firmware Control — deliberate exception to "no pinky-top hold":** The Bootloader and Reboot functions need to be reachable but must never trigger by accident. They sit on Q (left pinky top) and `'` (right pinky top) with a **500 ms hold term** (more than double the standard 200 ms). The combination of an uncomfortable position and an unusually long hold serves as a safety mechanism. Within L12, both `QK_BOOT` and `QK_REBOOT` are placed on home-row middle positions, mirrored on both hands — requiring two deliberate steps (hold to enter the layer, then a separate key press) before the firmware command fires.

**Path-navigation TD on L9 (TD29):** Tap = `/`, hold = `~/`, double-tap = `../`. A complete filesystem path can be typed without leaving the layer.

**Pipe TD on L9 (TD45):** Tap = `|`, hold = ` | ` (with surrounding spaces). Both pipe variants on the strongest left index position.

**Direct umlaut TDs on L10 (TD48/49/50):** Tap = `ä` / `ü` / `ö`, hold = `Ä` / `Ü` / `Ö`. Mnemonically placed on the A / U / O positions. The `"` dead key (TD33) remains available as a fallback for typing systems where the AltGr-shortcut is not desired (e.g. text fields that consume AltGr modifiers). The hold is implemented as a macro (M16/M17/M18) because Tap Dance hold slots accept only a single Vial keycode, while a capital umlaut requires `RShift+RAlt+letter`.

**Backtick on L4 and L9:** Backtick is reachable on L4 (left pinky bottom) and on L9 (left middle bottom), with `~` on the same row right side. Sufficient access for Markdown code-fences, JS template literals, and shell command substitution.

**No inner column for layer content:** G and M require a lateral inward index stretch — the same problem Colemak-DH solves for B and H. Cadence preserves Cadenza's extension: G/M only carry their letters and `App/Menu` on hold, never layer content. *No exceptions in v1.8.0.*

---

## ✦ Installation

### Requirements

- Ferris Sweep (any RP2040-compatible variant)
- Vial-compatible firmware **with `TAP_DANCE_ENTRIES = 64`** (Cadence v1.8 uses TD(50); the default Vial-Sweep build ships with 48)
- OS keyboard layout set to **US International** (required for dead keys and `RAlt` combinations)

### Step 1 — Flash Vial firmware

Cadence v1.8 uses 49 Tap Dance slots and requires a firmware build with at least 50 entries. The default Vial-Sweep firmware ships with 48 slots, so a custom build with `TAP_DANCE_ENTRIES = 64` is required:

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
2. **File → Load saved layout** → select `configuration/Cadence-FerrisSweep_v1_8_0.vil`
3. Confirm all layers loaded correctly

### Step 3 — Verify OS layout

Set your OS keyboard layout to **US International**. This is required for:

- `RAlt+S` → ß
- `RAlt+5` → €
- `RAlt+Q/Y/P` → ä/ü/ö (and `Shift+RAlt+Q/Y/P` → Ä/Ü/Ö, used by L10 hold-macros)
- Dead key `"` (Shift+Quote) → ä, ö, ü when followed by a vowel

---

## ✦ Resource Budget

| Resource | Used | Available | Free |
|---|---|---|---|
| Tap Dance slots | 49 | 64 | 15 (incl. TD10, TD21) |
| Macro slots | 19 | 32 | 13 |
| Key Overrides | 0 | 32 | 32 |
| Combos | 1 | 32 | 31 *(M-Btn1+M-Btn2 → M-Btn3 on L7)* |
| Layers | 13 active | 16 | 3 |

---

## ✦ Documentation

| Document | Description |
|---|---|
| **[docs/index.html](docs/index.html)** | Full design documentation and layer reference — keyboard visualisations for all 13 layers, design decisions, design principles, complete Tap Dance and Macro tables, firmware notes |
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

Cadence's version numbers track the underlying Ferris Sweep configuration version 1:1 — `v1.8.0` of the layout corresponds to Vial config `Cadence-FerrisSweep_v1_8_0.vil`.

Full versioning policy and change log: [VERSIONING.md](VERSIONING.md)

---

## ✦ Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Ports, language variants, and usage reports are welcome. Open a Discussion to suggest future features.

---

## ✦ License

Designed by **one7two99** · [MIT](LICENSE) · 2026

> *Based on [Cadenza](https://github.com/one7two99/cadenza) by one7two99 · [Colemak-DH](https://colemakmods.github.io/mod-dh/) by stevep99 · Inspired by [Miryoku](https://github.com/manna-harbour/miryoku)*

> *34 keys. Two thumbs less. Same rhythm.*
