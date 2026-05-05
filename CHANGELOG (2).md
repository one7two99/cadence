# Changelog

All notable changes to Cadence are documented here.

## [1.12.2] — 2026-05-05

Two unrelated layer refinements bundled into one PATCH release. **L5 Mouse**
gains a persistent mode via `DF()` while keeping the existing momentary
trigger; Mouse Button 3 (middle-click for Linux paste) is now properly
reachable. **L3 Numbers** is restructured for self-contained calculator
work: numpad-namespace operators are replaced by their ASCII counterparts,
round brackets land on the left pinky pair, and Tab takes over the Tab-thumb
for spreadsheet workflows.

### Changed — L5 Mouse Mode

| Position | v1.12.1 | v1.12.2 |
|---|---|---|
| L5 U-pos (right middle top) | `KC_NO` | `KC_BTN3` (middle click — primary) |
| L5 F-pos (left middle top) | `KC_NO` | `DF(5)` (set L5 as default — enter persistent) |
| L5 Spc-thumb (left) | `KC_BTN3` (unreachable dead code) | `DF(0)` (set L0 as default — exit persistent) |
| L5 Tab-thumb (left) | `KC_TRNS` | `KC_TAB` (explicit Tab — works in both modes) |

The momentary path is unchanged: Spc tap+hold → L5 active for the duration
of the hold. The new persistent path goes Spc tap+hold → tap F → release
Spc — L5 stays active because `DF(5)` made it the default layer. Tap Spc
to fire `DF(0)` and return to Base. `DF()` does not persist across reboots;
a fresh power-cycle always returns to L0.

`DF()` was chosen over `TG()` (toggle direction implicit) and over a
Tap-Dance double-tap on Spc (would collide with sentence-end double-spaces).

The previous `KC_BTN3` on the L5 Spc-thumb was dead code: while Spc is
held to keep the layer active, pressing Spc cannot also produce BTN3.

### Changed — L3 Numbers

| Position | v1.12.1 | v1.12.2 |
|---|---|---|
| L3 L-pos | `KC_KP_PLUS` (numpad +) | `LSFT(KC_EQUAL)` (`+`) |
| L3 U-pos | `KC_KP_MINUS` (numpad −) | `KC_MINUS` (`-`) |
| L3 Y-pos | `KC_KP_ASTERISK` (numpad *) | `LSFT(KC_8)` (`*`) |
| L3 H-pos | `KC_KP_EQUAL` (numpad =) | `KC_EQUAL` (`=`) |
| L3 ,-pos | `KC_KP_COMMA` | `KC_COMMA` (`,`) |
| L3 .-pos | `KC_KP_DOT` | `KC_DOT` (`.`) |
| L3 /-pos | `KC_KP_SLASH` | `KC_SLASH` (`/`) |
| L3 Q-pos | `KC_NO` | `LSFT(KC_9)` (`(`) |
| L3 Z-pos | `KC_NO` | `LSFT(KC_0)` (`)`) |
| L3 Tab-thumb | `KC_MINUS` | `KC_TAB` |

Numpad-namespace keycodes (`KC_KP_*`) require a Num-Lock state that is
unreliable on laptop hardware and absent on macOS, and `KC_KP_COMMA`
produces locale-dependent output. ASCII operators are universally
compatible across operating systems and applications.

Round brackets on Q (left pinky top) and Z (left pinky bot) form a vertical
pair on the same finger and let calculations like `(2+3)*4` complete on L3
without escaping to L9 Brackets.

Tab on the Tab-thumb makes the position match its name during Numbers mode
and supports fast cell navigation in spreadsheets without leaving the
layer; minus is reached on U-pos in the operator block.

### Resource Budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance | 51 | 64 |
| Macro | 19 | 32 |
| Layers with content | 12 in firmware (11 reachable) | 16 |
| Combos | 0 | 32 |
| Key Overrides | 0 | 32 |

Counts unchanged from v1.12.1.

### Classification

PATCH per Cadence's versioning policy. Both changes either fill previously
empty slots or refactor positions in ways that improve daily-driver
behaviour without invalidating muscle memory. The L3 numpad-to-ASCII change
is a behavioural improvement (more compatible output) on existing positions
— the same finger types the same operator, but the emitted character is now
universally compatible. The L3 Tab-thumb repurposing from `KC_MINUS` to
`KC_TAB` is the only cell where the typed character changes for the same
physical key, but it occurs in a layer mode the user controls deliberately,
and minus remains immediately reachable on the right hand.

### Configuration file

`Cadence-FerrisSweep_v1_12_2.vil` — preserves the 1:1 alignment between
published version number and configuration file name.

---

## [1.12.1] — 2026-05-05

Layer slot housekeeping. The Symbols layer that was redesigned and placed
on L12 in v1.11.0 is consolidated into the L2 slot, which has been an
empty placeholder since v1.9.0. From the user's perspective nothing
changes: Hold Bsp still activates the Symbols layer with identical
content. The change is purely an internal renumbering — every other
aspect of the layout, all Tap Dances, all macros, all settings remain
untouched.

### Changed

**Symbols layer slot consolidated L12 → L2.** Three coordinated changes
to the `.vil`:

| Change | v1.12.0 | v1.12.1 |
|---|---|---|
| L0 Base Bsp-thumb keycode | `LT12(KC_BSPACE)` | `LT2(KC_BSPACE)` |
| L2 array | empty (cleared in v1.12.0) | full Symbols content |
| L12 array | full Symbols content | empty |

The slot consolidation gives the layout a contiguous L0–L9 + L11 range
of active reachable layers, with L10 (Clipboard, no trigger by user
choice) and L12 (now empty) as the only non-active slots in firmware.

### Verified

The configuration was verified against v1.12.0 with `tools/vial-diff.py`:
exactly 45 layout-cell changes (1 reassigned on L0, 22 filled on L2, 22
cleared on L12). Tap Dance, Macro, Combo, Key Override, Settings, and
Encoder sections are bit-identical to v1.12.0. No reference to MO(12) or
LT12 remains anywhere in the configuration.

### Resource Budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance | 51 | 64 |
| Macro | 19 | 32 |
| Layers with content | 12 in firmware (11 reachable) | 16 |
| Combos | 0 | 32 |
| Key Overrides | 0 | 32 |

Counts are unchanged from v1.12.0; only the layer slot indices shifted.

### Classification

PATCH per Cadence's versioning policy: no behavioural change for the
user, no new functionality, no removed functionality. The change is a
pure refactoring of the firmware layer numbering. No muscle memory from
v1.12.0 is invalidated; the Symbols layer is reached identically via
Hold Bsp.

### Configuration file

`Cadence-FerrisSweep_v1_12_1.vil` — preserves the 1:1 alignment between
published version number and configuration file name.

### Motivation

Beyond the cosmetic improvement of consolidating layer numbering, this
change prepares the layout for the planned Layer Indicator feature. The
indicator strategy assigns a single-digit glyph to the inner-column
B-position of each non-base layer, allowing the user to verify which
layer is active by tapping B in the editor — a useful diagnostic for
both daily-driver troubleshooting and UAT runs. With Symbols on L2 the
layer numbering becomes a contiguous run that single-digit indicators
1–9 can cover cleanly.

---

## [1.12.0] — 2026-05-05

Layout completeness release. Three orthogonal additions: a Dead Key Hub on
L1 collecting all five US-International dead keys in one place, ScrollLock
and Pause/Break on L4 Navigation for keyboard completeness, and PrintScreen
on L6 Fn+Media for daily-driver use. L7 Code & CLI gains a literal-quote
thumb cluster (`'`, `"`, `` ` ``). Housekeeping: TD(51) deleted, deprecated
L2 layer cleared.

### Added

**L1 Overflow + International — Dead Key Hub**

L1 is consolidated as the single mental model for diacritic input. The
five US-International dead keys are now all reachable from L1:

| Position | Keycode | Dead key for |
|---|---|---|
| L1 P-pos (left index outer top) | `KC_GRAVE` | grave: à è ì ò ù |
| L1 L-pos (right index outer top) | `KC_GRAVE` | grave (bilateral mirror) |
| L1 ,-pos (right middle bot) | `LSFT(KC_GRAVE)` | tilde: ã ñ õ |
| L1 .-pos (right ring bot) | `LSFT(KC_6)` | circumflex: â ê î ô û |

The `'` (TD34, D + H bilateral) and `"` (TD33, T + N bilateral) dead keys
were already present from v1.5.0 — combined with the four new positions
above, the Dead Key Hub now covers the complete US-International set.
Dead-key-then-vowel always uses an L1 release between the two keystrokes
(L1 dead key tap → release Tab → L0 vowel tap), so the Q/X Sonata-overflow
slots on L1 right home (E and I positions) do not interfere.

**L4 Navigation — ScrollLock and Pause/Break**

| Position | Keycode | Function |
|---|---|---|
| L4 Q-pos (left pinky top) | `KC_SCRL` | ScrollLock |
| L4 X-pos (left ring bot) | `KC_PAUSE` | Pause; `Ctrl+KC_PAUSE` produces Break |

PC keyboards group PrintScreen / ScrollLock / Pause/Break together, but
Cadence v1.12 separates them by usage frequency: PrintScreen lives on L6
Fn+Media (frequent), ScrollLock and Pause on L4 Navigation (rare, but
required for layout completeness). `Pause` and `Break` share a single
physical key on a PC keyboard and the same QMK keycode (`KC_PAUSE` /
`KC_BRK` / `KC_BREAK` are aliases).

**L6 Fn+Media — PrintScreen on left Spc-thumb**

| Position | Keycode | Function |
|---|---|---|
| L6 Spc-thumb (left) | `KC_PSCR` | PrintScreen |

PrintScreen is grouped with Mute / Volume / Brightness on L6 because it
captures screen output (a system-output function). The left Spc-thumb is
reachable from both L6 access modes (Hold F or Hold U) without
finger-conflict.

**L7 Code & CLI — literal quote thumb cluster**

| Position | Keycode | Function |
|---|---|---|
| L7 Spc-thumb (left) | `KC_QUOTE` | `'` |
| L7 Tab-thumb (left) | `LSFT(KC_QUOTE)` | `"` |
| L7 Bsp-thumb (right) | `KC_GRAVE` | `` ` `` (also retained on C) |
| L7 Ent-thumb (right) | `KC_TAB` | Tab — for shell auto-complete sequences |

Mnemonic: *thumbs = quoting* while in Code & CLI. The C-position `` ` ``
from earlier versions is retained as redundancy and muscle-memory
continuity. Note: in US-International (Dead Keys) OS mode these
characters remain dead keys at the OS level — they feel literal in code
writing because identifiers usually start with consonants, which the
OS emits as two non-combining literals.

### Changed

**Documentation — Backtick reachability paragraph corrected.** Previous
README claimed backtick was reachable on L12 right ring top; this never
matched the `.vil` (which has the `<` / `>` Tap Dance there). The
paragraph now states the actual reachability: L1 (P, L bilateral), L7
(C-position and right Bsp-thumb), and L7 thumb cluster from v1.12.

### Removed

**TD(51) cleared.** TD(51) was defined as `tap = '`, `hold = "` but was
only placed on the deprecated L2 layer. Redundant with the existing
TD(33) (`"` dead key) and TD(34) (`'` dead key) on L1, which already
provide bilateral access. Cleared to all `KC_NO`.

**L2 deprecated layer — content cleared.** L2 (former Symbols layer
from v1.5–v1.9) was unreachable since v1.11.0. The 23 occupied
positions are cleared to `KC_NO`. The slot remains in the firmware
keymap (Vial format requires all 16 layer slots) but carries no content.

### Documented

**L1 Q/X Sonata-overflow rationale.** Q on L1 right home E-position and X
on L1 right home I-position are intentional, not a bug from earlier
iterations. Sonata (28-key sister project) drops the inner column on its
base layer; placing Q and X on L1 in Cadence preserves Sonata muscle
memory for users who later migrate hardware. The Cadence base layer
keeps Q and X in their natural Colemak-DH positions, so the L1 placement
is redundant on Cadence and primary on Sonata.

### Resource Budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance | 51 | 64 |
| Macro | 19 | 32 |
| Layers | 12 in firmware (11 reachable) | 16 |
| Combos | 0 | 32 |
| Key Overrides | 0 | 32 |

### Classification

MINOR per Cadence's versioning policy: new keys assigned to previously
empty positions; no change to the behaviour of any actively-used key. The
L7 right Bsp-thumb gaining `KC_GRAVE` does not conflict with the L0 Base
LT12 trigger on the same physical key — the Bsp-thumb on L0 is the L12
trigger, on L7 it is `KC_GRAVE`; layer-specific behaviour is independent.

### Configuration file

`Cadence-FerrisSweep_v1_12_0.vil` — preserves the 1:1 alignment between
published version number and configuration file name.

---

## [1.11.1] — 2026-05-03

App/Menu relocation. No layout structure changes, no muscle memory impact
for the user — the App/Menu hold-action on G and M was never used in
practice and is reassigned to L9 Brackets thumbs where it occupies
otherwise-transparent slots.

### Changed

**App/Menu moved from Base-layer G/M hold to L9 Brackets thumbs**

- TD(4) (G → App on hold) deleted — G is now a plain `KC_G`
- TD(5) (M → App on hold) deleted — M is now a plain `KC_M`
- L9 Brackets left-thumb outer (Spc-position): `KC_APPLICATION`
- L9 Brackets right-thumb outer (Bsp-position): `KC_APPLICATION`
- The two inner thumb positions on L9 (Tab-position, Ent-position)
  remain `KC_NO` (unallocated)

Rationale: the Base-layer G/M hold-action for Application Menu was
inherited from Cadenza but never used in daily work. Removing it
simplifies G and M to plain letters and frees two TD slots. L9
Brackets had four unallocated thumb positions; placing App/Menu on
the two outer positions makes it reachable from either hand while
on the Brackets layer, where modifier-like utility keys fit
contextually (App/Menu is conceptually similar to bracket-pair
operations: punctuation around a selection or word).

### Classification

PATCH per Cadence's versioning policy: no key behaviour changes for
any function the user actively uses. The G/M tap action is unchanged
(plain letters). The App/Menu function is preserved, only relocated
to a slot that wasn't carrying any other meaning.

### Resource Budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance | 52 | 64 |
| Macro | 19 | 32 |
| Layers | 13 in firmware (11 reachable) | 16 |
| Combos | 0 | 32 |
| Key Overrides | 0 | 32 |

### Configuration file

`Cadence-FerrisSweep_v1_11_1.vil` — preserves the 1:1 alignment between
published version number and configuration file name.

---

## [1.11.0] — 2026-05-03

Mouse-on-thumb redesign solves the v1.9.0 HRM-blocking issue, plus a
fully redesigned Symbol layer (L12). Tab and Spc become Tap-Dance
carriers handling multiple layer functions on single thumb positions.

### Why v1.11.0 and not v1.10.0?

A v1.10.0 internal Vial revision was created during the redesign of
the Mouse and Symbol layers. v1.10 surfaced configuration anomalies
during verification (a dead `MO(14)` trigger on F, three concurrent
L1 triggers, single-handed L6 access) that did not justify a public
release. v1.11 is the first revision in this series that resolves all
of these issues and matches the user's intended design cleanly.

Publishing only v1.11 (and not the intermediate v1.10 test revision)
preserves the 1:1 alignment between the published version number and
the configuration file name — analogous to v1.8 itself being the
first public release in its series rather than v1.6.

### Changed

**Thumb trigger redesign — Spc and Tab become Tap-Dance carriers**

| Thumb | v1.9 behaviour | v1.11 behaviour |
|---|---|---|
| Spc (L outer) | tap = Space, hold = L1 International | tap = Space, hold = L4 Navigation, **tap+hold = L5 Mouse** (TD(21)) |
| Tab (L inner) | tap = Tab, hold = L4 Navigation | tap = Tab, **hold = L1 International** (TD(10)) |
| Bsp (R outer) | tap = Bsp, hold = L2 Symbols | tap = Bsp, **hold = L12 Symbols** (LT(12)) |
| Ent (R inner) | tap = Ent, hold = L3 Numbers | unchanged |

The Spc tap+hold pattern is the central innovation: tap Spc, then
immediately press Spc again and hold to activate L5 Mouse. This
two-step trigger differentiates Mouse from Navigation while keeping
both layers on the same thumb position — and crucially, it frees both
hands for Home Row Mods during mouse use, which solves the v1.9
problem where the bilateral F+U trigger blocked Ctrl on the active
hand during multi-select operations.

**L5 Mouse — moved from F+U bilateral to Spc tap+hold**

The most important ergonomic fix. In v1.9, holding F to activate
Mouse made the left middle finger unavailable, so the Ctrl HRM on S
could not be tapped — making `Ctrl+Click` for multi-select impossible
to perform with one hand on the keyboard. Symmetrical problem on the
right with U blocking E (Ctrl). Spc tap+hold puts Mouse on the left
thumb only, leaving every finger HRM available.

**L9 Brackets — moved from D+H to X+. bilateral**

D and H are common letters (~5% frequency each in DE+EN), which made
the Brackets layer prone to false-positive hold-detection during
normal typing. X and . are far less frequent — cleaner hold-detection
without per-key tapping-term tuning. The bracket pairs and behaviour
inside the layer are unchanged.

**L1 International — access moved from Spc-hold to Tab-hold**

Tab is now a Tap-Dance with `tap = Tab, hold = MO(1)` (TD(10)). This
frees Spc for the Navigation+Mouse combined role described above.
Tab as a regular character is now reachable inside L4 Navigation and
L7 Code & CLI on the Ent-thumb position, so repeated Tab sequences
(form navigation, shell auto-complete, code indentation) work without
leaving the active layer.

**L6 Function Keys + Media — access moved from C/, to F+U bilateral**

Since F and U are no longer the Mouse trigger, they take over L6 Fn
+Media access. C and , become plain letter keys with no Tap Dance.
Layer content is unchanged from v1.9.

### Added

**L12 Symbols (NEW) — completely redesigned symbol layer**

Replaces the deprecated L2 Symbols. Activated by holding Bsp
(`LT(12, KC_BSPACE)`). Designed under the principle of access
asymmetry: since the right thumb anchors the layer trigger, high-
frequency symbols are placed on the freer left hand and on the top
rows of the right hand; the right bottom row is intentionally left
transparent (worst region during right-thumb anchoring).

The full design rationale and position assignments are documented in
the dedicated `L4-Symbol-Layer.html` specification, which is shared
across the Cadence (Sweep) and Sonata (28-key) sister projects. The
"L4" in the filename refers to the abstract Symbol-Layer concept; in
Cadence v1.11 it is implemented as L12.

Key positions:

- **Left home (high-frequency operators)** — `%` on A, `+` on R,
  `! / &` TD on S, `* / @` TD on T
- **Right top (bracket pairs)** — `( / )` TD on L, `[ / ]` TD on U,
  `< / >` TD on Y, `{ / }` TD on '
- **Right home (prose punctuation)** — `, / (` TD on N,
  `. / }` TD on E, `' / ^` TD on I, `;` on O
- **Thumbs** — `-` on Spc-thumb, `=` on Tab-thumb (most-frequent
  operators on strongest positions)
- **Various** — `~`, `?`, `#`, `$` on left top; `:`, `_`,
  `/ \` TD on left bottom

**New Tap Dances on L12** — TD(52)–TD(57) implement the symbol pairs
listed above.

### Deprecated

**L2 Symbols** — retained in firmware for cleanup later, no longer
reachable. The Bsp-thumb now triggers L12 instead. Users with v1.9
muscle memory for L2 symbols should retrain on the L12 layout, which
is intentionally different.

### Removed

**Tap Dance MO holds on C, D, H, and ,** — these positions are now
plain letter keys. C and , no longer trigger L6 (replaced by F+U); D
and H no longer trigger L9 Brackets (replaced by X+.).

### Firmware

`TAP_DANCE_ENTRIES` remains 64 (unchanged from v1.8). v1.11 uses 54
of 64 TD slots — 4 more than v1.9.0 due to the L12 Symbols layer
additions and the new Spc/Tab Tap Dances.

### Resource Budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance | 54 | 64 |
| Macro | 19 | 32 |
| Layers | 13 in firmware (11 reachable) | 16 |
| Combos | 0 | 32 |
| Key Overrides | 0 | 32 |

---

## [1.9.0] — 2026-05-02

Sonata-aligned release. Cadence's layer system is reorganised so that
L1–L9 mirror Sonata v3.0's numbering, simplifying any future migration
to Sonata hardware.

### Changed

**Layer renumbering** — twelve layers re-mapped:

| v1.8.0 layer | v1.9.0 layer | Note |
|---|---|---|
| L1 Media | merged into L6 | Combined with F-Keys |
| L2 Navigation | L4 Navigation | Sonata position |
| L3 Mouse | L5 Mouse | Renumbered |
| L4 Symbols | L2 Symbols | Renumbered |
| L5 Numbers | L3 Numbers | Renumbered |
| L6 F-Keys | merged into L6 | Combined with Media; chord trigger eliminated |
| L7 Clipboard | L10 Clipboard | Cadence-extra range; trigger removed |
| L8 Brackets | L9 Brackets | Cadence-extra range |
| L9 Code & CLI | L7 Code & CLI | Sonata position |
| L10 International | L1 Overflow + International | Renumbered + renamed |
| L11 Workspaces | L8 Tiling WM | Renumbered + renamed |
| L12 Firmware Control | L11 Firmware Control | Cadence-extra range |

**Access key reassignment by frequency × ergonomic strength** — the
Bsp+Spc chord trigger for F-Keys is eliminated; L6 Fn+Media gets
direct bilateral access via C+, instead. All access keys remain
configured as Tap Dance for per-key tapping-term control.

**L6 Fn+Media merged from former L1 + L6** — F1–F12 on left in
numpad-spatial layout, media controls on right hand. Single layer,
single bilateral access pair.

**L10 Clipboard intentionally has no access key** — user opts out;
layer remains in firmware for future activation.

### Removed

**X and . MO holds** — both were L9 Code & CLI triggers in v1.8.0;
in v1.9 they become pure letter keys.

### Resource Budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance | 50 | 64 |
| Macro | 19 | 32 |
| Layers | 13 in firmware (11 reachable) | 16 |
| Combos | 1 | 32 |
| Key Overrides | 0 | 32 |

---

## [1.8.0] — 2026-05-02

Direct AltGr-based umlaut access on L10 International. The previous
`"` dead key path remains available unchanged.

### Why v1.8.0 and not v1.6.0?

Three internal Vial configuration revisions (v1.6, v1.7, v1.8) were
created during the development of direct umlaut access on L10. Each
revision tested a different combination of Tap Dance placements, hold
behaviours, and macro encodings. v1.6 and v1.7 surfaced issues during
daily-driver use that did not justify a public release — false triggers,
modifier-stickiness on capital-letter holds, and edge cases in the
interaction between L10 hold-macros and HRM. v1.8 is the first revision
in this series that resolves all of these issues and behaves cleanly in
extended use.

Publishing only v1.8 (and not the intermediate test revisions) preserves
the 1:1 alignment between the published version number and the
configuration file name — analogous to v1.5.0 itself being the first
public release rather than v1.0.0.

### Added

**L10 International — direct umlaut Tap Dances**
- TD(48) on left A-position: tap = `RAlt+Q` → ä, hold = M16 (`Shift+RAlt+Q` → Ä)
- TD(49) on right U-position: tap = `RAlt+Y` → ü, hold = M17 (`Shift+RAlt+Y` → Ü)
- TD(50) on right O-position: tap = `RAlt+P` → ö, hold = M18 (`Shift+RAlt+P` → Ö)

The mnemonic placement (ä on A, ü on U, ö on O) means the lookup is
direct rather than positional. Bilateral access is preserved: holding
D or H activates L10, the umlaut TDs are reachable from either hand
depending on which layer-access key is held.

**Why hold = macro, not `Shift+RAlt+letter` keycode?** Tap Dance hold
slots accept a single Vial keycode, but the capital umlaut requires
two simultaneous modifiers (`RShift`+`RAlt`) plus the letter. Macros
are the cleanest expression of this sequence and produce identical USB
HID output.

### Firmware

`TAP_DANCE_ENTRIES` increased to 64 (default Vial-Sweep ships with 48).
Required because v1.8 uses TD(50). 15 TD slots remain free.

### Unchanged from v1.5.0

L0–L9, L11, L12 layers, all HRMs and tipping terms, all M0–M15 macros,
the M-Btn combo, and all Vial settings remain untouched.

### Resource Budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance | 49 | 64 |
| Macro | 19 | 32 |
| Layers | 13 active | 16 |
| Combos | 1 | 32 |
| Key Overrides | 0 | 32 |

---

## [1.5.0] — 2026-05-01

Initial public release. Cadence is the Ferris Sweep adaptation of
[Cadenza v1.0.0](https://github.com/one7two99/cadenza). The release
consolidates five pre-release Sweep adaptation revisions (v1.0 through v1.5).

### Inherited from Cadenza v1.0.0

These elements transfer unchanged from the Cadenza design:

**Base layout & HRM**
- Colemak-DH base layout
- Home Row Mods via Tap Dance: A=⌘, R=⌥, S=⌃, T=⇧ (left); N=⇧, E=⌃, I=AltGr, O=⌘ (right)
- G/M = `App/Menu` on hold (TD4 / TD5)
- Tipping terms: 250 ms ring/pinky (A, O), 200 ms index/middle (all others)

**Layer architecture**
- L0 Base, L2 Navigation, L3 Mouse, L4 Symbols, L5 Numbers, L6 F-Keys,
  L7 Clipboard, L8 Brackets, L9 Code & CLI, L10 International preserved
- Bottom-row layer access (Z, X, C, D, H, comma, period, slash) unchanged
- Top-row layer access (W, Y) for L1 unchanged
- Frequency+Strength symbol layout on L4 — `=` on T, `$` on N

**Action keys**
- L8 Brackets: TD25–TD28 tap=open / hold=close pairs (`(`/`)`, `[`/`]`, `<`/`>`, `{`/`}`)
- L9 Code & CLI: M0=`$?`, M5=` | `, M6=`../`, M7=`2>&1`, M8=`$()`, M9=`${}`,
  M10=`&&`, M11=`||`, M12=`!=`, M13=`==`, M14=`=>`, M15=`->`
- L9 Path TD: TD29 tap=`/`, hold=`~/`, double=`../`
- L10 International: `"` dead key (TD33), ß (`RAlt+S`), `'` macros (TD34)

### Diverged from Cadenza for the Sweep adaptation

These changes are required by the Sweep's 34-key form (4 thumb keys instead of 6):

**Thumb cluster — reduced**
- Cadenza: Esc / Spc / Tab on left thumb, Ent / Bsp / Del on right thumb (6 keys)
- Cadence: Spc(LT2) / Tab(LT3) on left thumb, Ent(LT5) / Bsp(LT4) on right thumb (4 keys)
- Esc removed from thumb — relocated to L2 / L3 bottom-row D-position
- Del removed from thumb — relocated to L2 right thumb inner and L6 right thumb middle
- L6 access key removed from thumb — replaced by Bsp+Spc chord

**L1 RGB & Media → L1 Media**
- RGB control functions removed (Sweep has no RGB)
- Layer renamed from "RGB & Media" to "Media"
- Left thumb (Spc-position) → `PrtSc`
- Right thumb: `Mute` (Ent-position), `Play / Stop` TD (Bsp-position)
- Left home row T-position → `CapsLock`
- Right home row → media controls (Prev / Vol- / Vol+ / Next)
- Right bottom row → screen brightness (Bri- / Bri+)

**L11 Tiling WM Quick + L12 Tiling WM Full → L11 Workspaces (consolidated)**
- Cadenza's two WM layers merged into a single layer
- Access via Hold F or Hold U (middle fingers, top row) — the previous L11 access pair
- L key (right index top row) is no longer a hold key — it is a plain `KC_L`
- Workspace 1–10 in numpad layout (left half, top-down 7-8-9 / 4-5-6 / 1-2-3 / 0)
- TD35–TD43 = WS 1–9 (tap=`⌘+N`, hold=`⌘⇧+N` to move window)
- TD44 = WS 10 (tap=`⌘+0`, hold=`⌘⇧+0`)
- Right hand: focus switch (`⌘+←/↓/↑/→`) home row, window move (`⌘⇧+←/↓/↑/→`) bottom row
- Left thumb: WS10 (Spc-position), Kill `⌘⇧+Q` (Tab-position)
- Right thumb: Float `⌘+Spc` (Ent-position), Fullscreen `⌘+F` (Bsp-position)

**L12 Firmware Control (new)**
- New layer not present in Cadenza
- Contains `QK_BOOT` (jump to bootloader for firmware updates) and `QK_REBOOT`
- Both functions placed symmetrically: `QK_BOOT` on left S-position and right E-position,
  `QK_REBOOT` on left T-position and right R-position (home row, middle columns)
- Access via long-hold (500 ms) on Q (left pinky top, TD46) or `'` (right pinky top, TD47)
- The 500 ms term is more than double the standard 200 ms — deliberately uncomfortable
  to prevent accidental triggering
- This is the only intentional pinky-top hold in the entire layout — the safety
  argument outweighs the philosophical preference

**L6 access — chord activation**
- Cadenza: Hold Del (right thumb outer)
- Cadence pre-release v1.0: Hold `'` (right pinky top, TD10 hold)
- Cadence v1.5: Hold Bsp + Hold Spc-position chord
- Mechanism: Bsp first → L4 active → Spc-position is now `MO(6)` → L6 active
- The order matters: Bsp first, then Spc; reverse order produces a literal Backspace

**Pipe TD on L9 (new vs Cadenza)**
- TD45: tap = `|`, hold = ` | ` (pipe with surrounding spaces)
- Replaces the standalone M5 placement on L9 left index home position
- Both pipe variants on the strongest left index — improves on Cadenza

**Backtick reachability (Sweep-specific addition)**
- Cadenza-original v1.0.0 placed backtick on L10 only
- Pre-release Sweep v1.0 lost backtick access entirely (genuine gap)
- Cadence v1.5 places backtick on three positions:
  - L4 BotL pinky (Z-position): plain `` ` ``
  - L9 BotL middle (C-position): plain `` ` ``
  - L9 BotR middle (`,`-position): `~` (LSft+`)
- Sufficient access for Markdown code-fences, JS template literals, shell command substitution

**€ on L10 (Sweep-specific addition)**
- Cadenza-original L10: `€` reachable on left half
- Pre-release Sweep v1.0 had ß placed twice and lost € access
- Cadence v1.5 L10 HomeL R-position: `RAlt+5` → € (replaces the duplicate ß)
- ß remains on L10 HomeL S-position (single placement)

**L4 `/` on Symbols**
- L4 BotR pinky position: `KC_SLASH` (allows typing `/` without leaving L4 for `*/`, `//` patterns)

**QMK Mouse settings**
- v1.5 includes tuned QMK mouse / scroll settings in the Vial `settings`
  section. The settings are stored as numeric Vial setting IDs and are
  preserved by the `.vil` import. Specific values: see the configuration
  file. Behaviour changes vs. defaults are not interpreted in this changelog
  because the numeric IDs are firmware-version-dependent and not
  self-documenting in the `.vil` format.

### Pre-release Sweep adaptation history (informal)

For traceability — the work leading up to v1.5.0:

- **v1.0** (early Sweep adaptation): initial port from Cadenza. Identified
  gaps: no backtick, doubled ß, L6 access via uncomfortable pinky-top hold.
- **v1.2** (consolidation): backtick added at three positions; doubled ß
  replaced with €; L6 chord activation via Bsp+Spc; L11/L12 merged into a
  single L12 Workspaces; TD45 pipe-TD added; L11 emptied as reserve slot.
- **v1.3** (cleanup): an accidentally placed `KC_KP_6` on L6 inner column
  removed; `TD(44)` WS10 verified.
- **v1.5** (this release): two ROADMAP items resolved (L2 Top-Row Ctrl+Arrow
  ordering corrected to NEIO; `=` removed from L5 G-inner-column).
  Workspaces moved from L12 to L11 to make room for a new L12 Firmware
  Control layer (`QK_BOOT` + `QK_REBOOT`), accessible via deliberately
  uncomfortable long-hold pinky-top combination. Mouse/scroll QMK settings
  tuned. (No v1.4 was released.)

### Resource budget

| Resource | Used | Available |
|---|---|---|
| Tap Dance slots | 46 | 48 |
| Macro slots | 16 | 32 |
| Combos | 1 | 32 |
| Key Overrides | 0 | 32 |
| Layers | 13 active | 16 |
