# Changelog

All notable changes to Cadence are documented here.

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
