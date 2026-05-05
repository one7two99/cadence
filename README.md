<div align="center">
  <h1>Cadence</h1>
  <p>
    <img src="https://img.shields.io/badge/version-1.12.2-brightgreen?style=flat-square" alt="Version">
    <img src="https://img.shields.io/badge/keyboard-Ferris%20Sweep-blue?style=flat-square" alt="Keyboard">
    <img src="https://img.shields.io/badge/firmware-Vial%20%2F%20QMK-orange?style=flat-square" alt="Firmware">
    <img src="https://img.shields.io/badge/base-Colemak--DH-purple?style=flat-square" alt="Base">
    <img src="https://img.shields.io/badge/tap%20dances-51%20%2F%2064-yellow?style=flat-square" alt="Tap Dances">
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
| (separate Symbol layer) | **L2 Symbols** (NEW in v1.11 as L12, consolidated to L2 in v1.12.1) via Hold Bsp | Redesigned with right-thumb access asymmetry |

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
- **L1 Overflow + International — *Dead Key Hub*** — direct umlaut TDs (ä/ö/ü on A/O/U positions, hold = capital), plus all five US-International dead keys centralised: `` ` `` (P, L bilateral), `'` (D, H), `"` (T, N), `^` (.), `~` (,). Also: ß (`RAlt+S`), € (`RAlt+5`), Esc on Bsp-thumb. Q and X mirrored from Base for forward-compatibility with Sonata.
- **L8 Tiling WM** — WS 1–10 tap=go / hold=move (numpad memory) · focus and window-move on right hand · Kill / Float / Fullscreen on thumbs
- **L11 Firmware Control** — `QK_BOOT` and `QK_REBOOT` symmetrically placed, accessible only via deliberate long-hold (500 ms) pinky-top combination
- **L2 Symbols (NEW in v1.11 as L12, consolidated to L2 in v1.12.1)** — redesigned symbol layer with right-thumb access asymmetry, sharing the design specification with Sonata v3.x
- **Mouse settings tuned** — QMK mouse acceleration / scroll behaviour configured in the `.vil`

---

## ✦ Layer Overview

| # | Layer | Access | Purpose |
|---|---|---|---|
| L0 | Base | — | Colemak-DH + Tap Dance HRM |
| L1 | Overflow + International (*Dead Key Hub*) | Hold **Tab** | direct **ä/ö/ü** TDs (tap=lower, hold=capital) · all five dead keys (`` ` ``, `'`, `"`, `^`, `~`) · ß · € · Q/X overflow for Sonata-compat |
| L2 | Symbols | Hold **Bsp** | redesigned symbol layout — see [`L4-Symbol-Layer.html`](docs/L4-Symbol-Layer.html). Slot reused in v1.12.1 (was the redesigned L12 slot in v1.11–v1.12.0) |
| L3 | Numbers | Hold **Ent** | Numpad on left (1–9, 0 on Spc-thumb) · ASCII operators on right (`+ - * = , . /`) · brackets `(` Q · `)` Z · Tab on Tab-thumb (Excel cell navigation) |
| L4 | Navigation | Hold **Spc** | Arrows · Home/End/PgUp/PgDn · Word-skip · Tab on Ent-thumb for repeated Tab · ScrollLock (Q) · Pause/Break (X) |
| L5 | Mouse | **Spc tap + hold** | Pointer (NEIO) · Scroll (right bot) · BTN1/BTN2 on right thumbs · BTN3 on U · `DF(5)` on F (persistent mode) · `DF(0)` on Spc-thumb (exit persistent) |
| L6 | Function Keys + Media | Hold **F** *or* Hold **U** | F1–F12 (left, numpad-spatial) · media controls (right hand) · **PrintScreen** on left Spc-thumb |
| L7 | Code & CLI | Hold **W** *or* Hold **Y** | Shell operators · path navigation TD · `\|` (tap) / ` \| ` (hold) · `` ` `` · `~` · `\` · `'` / `"` / `` ` `` on thumbs (literal) · Tab on Ent-thumb |
| L8 | Tiling WM | Hold **Z** *or* Hold **/** | WS 1–10 (numpad memory) · focus · window move · Kill / Float / Fullscreen |
| L9 | Brackets | Hold **X** *or* Hold **.** | `(` `)` `[` `]` `<` `>` `{` `}` — bilateral mirror · `App/Menu` on Spc/Bsp thumbs |
| L10 | Clipboard | — | layer present, no trigger by user choice |
| L11 | Firmware Control | **Long-hold (500 ms) Q** *or* Long-hold **'** | `QK_BOOT` (bootloader) · `QK_REBOOT` |
| L12 | (empty) | — | retained as empty firmware slot (was the Symbols layer in v1.11–v1.12.0; consolidated to L2 in v1.12.1) |

### Access key principle

Access keys in v1.11 are assigned by **usage frequency × ergonomic quality × hold-detection safety**, with one critical refinement learnt from v1.9: layers used heavily during HRM-required workflows (especially Mouse) must not block the active hand's Home Row Mods. This is solved by putting Mouse on a Tap-Dance carrier (Spc tap+hold) instead of a bilateral letter trigger.

The remaining bilateral letter pairs use **finger-symmetric** triggers — same finger on both hands, same row — placed on letters whose frequency is low enough for clean hold-detection: F+U (Middle Top), W+Y (Ring Top), Z+/ (Pinky Bottom), X+. (Ring Bottom). G and M never carry layer content. The **outer pinky-top positions (Q and `'`)** are deliberately reserved for the rarely-used Firmware Control layer — uncomfortable enough to prevent accidental activation, paired with an unusually long 500 ms hold term.

---

## ✦ Design Decisions

**Spc as Tap-Dance carrier (TD(21)):** `tap = Space, hold = Navigation, tap+hold = Mouse`. The tap+hold pattern triggers when Spc is tapped, then immediately pressed again and held. This three-way differentiation eliminates v1.9's HRM-blocking issue: on Mouse, both hands are free to use Home Row Mods (Ctrl for multi-select, Shift for range-select). The same key carries the two most-used cursor-related layers, semantically related ("Spc = cursor work").

**Tab as Tap-Dance carrier (TD(10)):** `tap = Tab, hold = International`. International is one of the most frequently used layers when writing German prose; placing it on a single thumb hold makes it maximally accessible. Tab as a character remains directly available (tap), and inside L4 Navigation and L7 Code & CLI it is also placed on the Ent-thumb for repeated Tab sequences (form navigation, shell auto-complete, code indentation).

**Frequency + Strength (L2 Symbols):** Symbols ranked by daily usage frequency in German IT writing, then assigned to fingers in strength order, weighted by the position-quality penalty for the right-thumb-anchored hand. `=` and `-` on thumbs (most-frequent operators on strongest positions). Bracket pairs as Tap Dance on right top. Identical specification shared with Sonata v3.x.

**F/U for Fn+Media (L6):** Middle fingers, top row. Strong fingers, low-frequency letters for safe hold-detection. F1–F12 in numpad-spatial layout on the left (matches L_NUM and L_WM positions for muscle-memory transfer); media controls on the right.

**X/. for Brackets (L9):** Ring Bottom. Moved from D+H in v1.9.0 — D and H are common letters (~5%), which made the Brackets layer prone to false-positive hold-detection during normal typing. X and . are far less frequent — cleaner hold-detection without per-key tapping-term tuning.

**Z// for Tiling WM (L8):** Pinky Bottom. Both letters very rare in DE+EN — safest hold-detection of all bilateral pairs. WS 1–10 in numpad spatial layout on the left (matches L_NUM positions for muscle-memory transfer).

**L11 Firmware Control — deliberate exception to "no pinky-top hold":** The Bootloader and Reboot functions need to be reachable but must never trigger by accident. They sit on Q (left pinky top) and `'` (right pinky top) with a **500 ms hold term** (more than double the standard 200 ms). The combination of an uncomfortable position and an unusually long hold serves as a safety mechanism. Within L11, both `QK_BOOT` and `QK_REBOOT` are placed on home-row middle positions, mirrored on both hands — requiring two deliberate steps (hold to enter the layer, then a separate key press) before the firmware command fires.

**Path-navigation TD on L7 (TD29):** Tap = `/`, hold = `~/`, double-tap = `../`. A complete filesystem path can be typed without leaving the layer.

**Pipe TD on L7 (TD45):** Tap = `|`, hold = ` | ` (with surrounding spaces). Both pipe variants on the strongest left index position.

**Direct umlaut TDs on L1 (TD48/49/50):** Tap = `ä` / `ü` / `ö`, hold = `Ä` / `Ü` / `Ö`. Mnemonically placed on the A / U / O positions. The `"` dead key (TD33) remains available as a fallback for typing systems where the AltGr-shortcut is not desired (e.g. text fields that consume AltGr modifiers). The hold is implemented as a macro (M16/M17/M18) because Tap Dance hold slots accept only a single Vial keycode, while a capital umlaut requires `RShift+RAlt+letter`.

**Backtick reachability:** Backtick is reachable on L1 (P and L positions, bilateral — as grave-accent dead key feeding into vowels), on L7 Code & CLI (C-position and right Bsp-thumb — for literal use in shell, Markdown, JS template literals), and on the L7 thumb cluster as part of the `'` / `"` / `` ` `` quote group introduced in v1.12. Five access points across two layers — single-point-of-failure eliminated.

**No inner column for layer content:** G and M require a lateral inward index stretch — the same problem Colemak-DH solves for B and H. Cadence preserves Cadenza's extension: G/M only carry their letters, never layer content. The Application Menu key (formerly on G/M hold in v1.11.0 and earlier) was never used in daily work and was relocated to L9 Brackets in v1.11.1 — see Design Decisions below.

**App/Menu on L9 Brackets thumbs (v1.11.1):** Application Menu is reachable on the L9 Spc-thumb and Bsp-thumb, available from either hand while holding X or . to access Brackets. The Tab and Ent thumb positions remain unallocated on L9. Rationale: G and M hold-actions for App/Menu were inherited from Cadenza but never used in practice; freeing them simplifies the base layer to plain letters and reclaims two TD slots without any functional loss.

**Dead Key Hub on L1 (v1.12):** L1 Overflow + International is treated as the centralised access point for *all five* US-International dead keys. ä/ö/ü retain their direct Tap Dances (TD48/49/50). The five raw dead-key glyphs sit on positions chosen for finger-symmetry and minimum interference with the Q/X overflow letters: `` ` `` on P and L (bilateral), `'` on D and H (bilateral, via TD34), `"` on T and N (bilateral, via TD33), `^` on the dot position, `~` on the comma position. The dead keys feed into vowels typed afterwards on L0 Base — L1 does not need to remain held during the second keystroke. This consolidation gives the user a single mental model: *if I want a diacritic, I go to L1*. Mixing dead-key access between L1 and the Symbols layer (which had been the case before v1.12 with `^` and `~` on the Symbols layer) is eliminated.

**Sonata-overflow letters on L1 (Q, X) — design rationale:** Sonata, the 28-key sister project, drops the inner column entirely on its base layer. To make muscle-memory transferable between Cadence and Sonata without retraining, Q (left pinky-top) and X (left ring-bottom) — both already on Cadence Base — are *also* placed on L1 (right home E-position and I-position respectively). On Cadence the L1 placement is redundant; on Sonata it will be the only access point for those letters. Typing Q or X via L1 on Cadence requires Hold-Tab → tap E or I, which produces the letter without releasing L1. The placement does not interfere with the Dead Key Hub additions because dead-key-then-vowel always involves an L1 release between the two keystrokes.

**ScrollLock and Pause/Break on L4 (v1.12):** Two completeness-driven additions on the Navigation top-row left side. ScrollLock on Q (left pinky-top), Pause/Break on X (left ring-bottom) — Pause and Break are the same physical PC key (`KC_PAUSE` produces Pause; `Ctrl+KC_PAUSE` produces Break interrupt). Both are rarely used in daily driver work but belong in a complete keyboard layout. Q and X were chosen because they are otherwise unused on L4 and stay out of the way of frequently-used Navigation keys; X also visually parallels P (CapsLock) on the same row.

**PrintScreen on L6 left Spc-thumb (v1.12):** PrintScreen is conceptually a media/system-output function (capture screen → output buffer), grouping it with Mute, Volume, and Brightness on L6 Fn+Media. The left Spc-thumb position is reachable from both bilateral access modes (Hold F or Hold U) without finger conflict, since the left thumb is unanchored in both cases. Single prominent access point matches the user's frequent-use pattern.

**L7 thumb quote cluster (v1.12):** The four L7 thumb positions previously held `KC_NO`. v1.12 fills three of them with `'`, `"`, `` ` `` for direct access during code and shell work, plus `Tab` on the right Ent-thumb (mirroring the L4 convention for repeated-Tab workflows like shell auto-complete). Mnemonic: *thumbs = quoting* during Code & CLI. Note that in US-International (Dead Keys) OS mode, these characters remain dead keys at the OS level — what makes them feel literal during code writing is that code identifiers usually start with consonants, which the OS treats as non-combining and emits as two literal characters. The C-position `` ` `` from earlier versions is retained as a redundant access point and as muscle-memory continuity.

**Symbols layer slot consolidation L12 → L2 (v1.12.1):** v1.11 introduced the redesigned Symbols layer on L12, leaving the deprecated former Symbols layout in L2 as an empty placeholder. v1.12.0 cleared L2's residual content. v1.12.1 takes the natural next step and moves the Symbols content from L12 down into the now-empty L2 slot, so the active reachable layers occupy a contiguous L0–L9, L11 range with L10 (Clipboard, no trigger by user choice) and L12 (now empty) as the only non-active slots in firmware. From the user's perspective nothing changes: Hold Bsp still activates the Symbols layer with the identical layout. The change is implemented purely via the layer-tap encoding on the Bsp-thumb (`LT12(KC_BSPACE)` → `LT2(KC_BSPACE)`) and the array swap. This consolidation also prepares the layout for the planned Layer Indicator feature, where each non-base layer will surface a single-digit identifier on the inner-column B-position for diagnostic and UAT use.

**L5 Mouse Mode — momentary plus persistent (v1.12.2):** L5 Mouse is reachable two ways. The momentary path is unchanged: Spc tap+hold activates L5 for as long as Spc is held, releasing returns to Base. The new persistent path uses `DF()` (set default layer) to make L5 the base for sustained mouse work without keeping a thumb anchored. Workflow: Spc tap+hold to enter L5 momentary → tap **F** which fires `DF(5)` → release Spc → L5 remains active because it is now the default layer → both hands free, Tab-thumb works as a third BTN3 surface, U remains the primary BTN3 click → tap Spc which fires `DF(0)` to return to Base. The mechanism uses `DF()` rather than a Tap-Dance double-tap on Spc (which would collide with double-spaces in normal text) and rather than `TG()` toggle (whose direction is implicit and confusing) — `DF()` makes the intent explicit and the Spc thumb works symmetrically as both entry and exit. `DF()` does not persist across reboots, so a fresh power-cycle always returns to Base regardless of mode at shutdown. Mouse Button 3 is reachable on three surfaces: U (primary, available in both modes), left Tab-thumb (only useful in persistent mode where the left thumb is free), and as drag-friendly via Hold-U for click-and-hold operations.

**L3 Numbers — calculator-friendly redesign (v1.12.2):** Three coordinated changes turn L3 from a strict numpad replica into a self-contained calculator workflow. First, the numpad-namespace operators (`KC_KP_PLUS`, `KC_KP_MINUS`, `KC_KP_ASTERISK`, `KC_KP_EQUAL`, `KC_KP_COMMA`, `KC_KP_DOT`, `KC_KP_SLASH`) are replaced by their plain ASCII counterparts (`+`, `-`, `*`, `=`, `,`, `.`, `/`). This removes a real-world friction point: numpad keycodes require a Num-Lock state which is unreliable across laptop hardware, macOS does not have a Num-Lock concept, `KC_KP_COMMA` produces locale-dependent output (decimal separator on German systems, thousands separator on others) when crossing app boundaries. ASCII operators are universally compatible. Second, round brackets are added on Q and Z (left pinky vertical pair) — `(` on Q, `)` on Z — so calculations like `(2+3)*4` complete on L3 without escaping to L9 Brackets. Third, Tab is placed on the Tab-thumb (was `-`) — minus is now reachable on U, and Tab-thumb regains its mnemonic identity for fast cell navigation in spreadsheets while staying inside the Numbers layer.

---

## ✦ Installation

### Requirements

- Ferris Sweep (any RP2040-compatible variant)
- Vial-compatible firmware **with `TAP_DANCE_ENTRIES = 64`** (Cadence v1.12.2 uses TD(57); the default Vial-Sweep build ships with 48)
- OS keyboard layout set to **US International** (required for dead keys and `RAlt` combinations)

### Step 1 — Flash Vial firmware

Cadence v1.12.2 uses 51 Tap Dance slots and requires a firmware build with at least 58 entries. The default Vial-Sweep firmware ships with 48 slots, so a custom build with `TAP_DANCE_ENTRIES = 64` is required:

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
2. **File → Load saved layout** → select `configuration/Cadence-FerrisSweep_v1_12_2.vil`
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
| Tap Dance slots | 51 | 64 | 13 |
| Macro slots | 19 | 32 | 13 |
| Key Overrides | 0 | 32 | 32 |
| Combos | 0 | 32 | 32 |
| Layers | 13 in firmware (11 reachable) | 16 | 3 |

---

## ✦ Documentation

| Document | Description |
|---|---|
| **[docs/index.html](docs/index.html)** | Full design documentation and layer reference — keyboard visualisations for all 13 layers, design decisions, design principles, complete Tap Dance and Macro tables, firmware notes |
| **[docs/L4-Symbol-Layer.html](docs/L4-Symbol-Layer.html)** | Dedicated specification for the Symbol layer (L2 in v1.12.1+, was L12 in v1.11–v1.12.0) — design rationale, position assignments, shared with Sonata v3.x |
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

Cadence's version numbers track the underlying Ferris Sweep configuration version 1:1 — `v1.12.2` of the layout corresponds to Vial config `Cadence-FerrisSweep_v1_12_2.vil`.

Full versioning policy and change log: [VERSIONING.md](VERSIONING.md)

---

## ✦ Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Ports, language variants, and usage reports are welcome. Open a Discussion to suggest future features.

---

## ✦ License

Designed by **one7two99** · [MIT](LICENSE) · 2026

> *Based on [Cadenza](https://github.com/one7two99/cadenza) by one7two99 · [Colemak-DH](https://colemakmods.github.io/mod-dh/) by stevep99 · Inspired by [Miryoku](https://github.com/manna-harbour/miryoku)*

> *34 keys. Two thumbs less. Same rhythm.*
