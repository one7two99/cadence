# Changelog

All notable changes to Cadence are documented here.

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
