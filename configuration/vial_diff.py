#!/usr/bin/env python3
"""
vil_diff.py — Diff two Vial keymap (.vil) configurations and generate a
Markdown report describing what changed between them.

Usage
-----
    python3 vil_diff.py OLD.vil NEW.vil [options]

Options
-------
    -o, --output FILE         Write Markdown to FILE (default: stdout).
    --names OLD NEW           Display names for the two configs
                              (default: filename stems).
    --title TITLE             Override the report title.
    --base {colemak-dh,qwerty}
                              Base-layer letter mapping for position labels
                              (default: colemak-dh).

Design notes
------------
- Compares all top-level sections of the .vil JSON: layout, tap_dance,
  macro, combo, key_override, settings, encoder_layout, plus metadata.
- Layout cells are reported per-layer. Position labels follow Colemak-DH
  by default (Q W F P B / A R S T G / Z X C D V on the left half,
  J L U Y ' / M N E I O / K H , . / on the right half). Thumb positions
  use Spc/Tab/Ent/Bsp regardless of base.
- Each layout change is classified as `filled` (empty → assigned),
  `cleared` (assigned → empty), or `reassigned` (assigned → assigned).
- A small keycode translator adds human-readable glyphs in parentheses
  for common symbol/modifier keycodes (e.g. `KC_GRAVE` → `` ` ``).
  Unknown keycodes are shown as raw QMK identifiers.
- Tap-dance, macro, combo, key-override sections are only listed when
  they actually differ; otherwise the report records them as identical.

This tool is layout-agnostic: it works on any Vial config, not just
Cadence. It does not assume any particular layer naming or count.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Position label maps
# ---------------------------------------------------------------------------

# Vial layout structure for Ferris Sweep / Corne-class boards:
#   8 sub-arrays per layer.
#   sub 0..3 = left half (top, home, bot, thumbs)
#   sub 4..7 = right half (top, home, bot, thumbs)
#   each sub-array has 5 slots (slots 2..4 of thumb arrays are -1).

POS_BY_BASE = {
    'colemak-dh': {
        0: ['Q', 'W', 'F', 'P', 'B'],
        1: ['A', 'R', 'S', 'T', 'G'],
        2: ['Z', 'X', 'C', 'D', 'V'],
        3: ['Spc', 'Tab', '-', '-', '-'],
        4: ['J', 'L', 'U', 'Y', "'"],
        5: ['M', 'N', 'E', 'I', 'O'],
        6: ['K', 'H', ',', '.', '/'],
        7: ['Ent', 'Bsp', '-', '-', '-'],
    },
    'qwerty': {
        0: ['Q', 'W', 'E', 'R', 'T'],
        1: ['A', 'S', 'D', 'F', 'G'],
        2: ['Z', 'X', 'C', 'V', 'B'],
        3: ['Spc', 'Tab', '-', '-', '-'],
        4: ['Y', 'U', 'I', 'O', 'P'],
        5: ['H', 'J', 'K', 'L', ';'],
        6: ['N', 'M', ',', '.', '/'],
        7: ['Ent', 'Bsp', '-', '-', '-'],
    },
}

ROW_NAME = {0: 'top', 1: 'home', 2: 'bot', 3: 'thumb',
            4: 'top', 5: 'home', 6: 'bot', 7: 'thumb'}
SIDE_NAME = {0: 'L', 1: 'L', 2: 'L', 3: 'L',
             4: 'R', 5: 'R', 6: 'R', 7: 'R'}


# ---------------------------------------------------------------------------
# Keycode → human-readable glyph translator
# ---------------------------------------------------------------------------

_DIRECT = {
    'KC_NO': '(empty)',
    'KC_TRNS': '(transparent)',
    'KC_GRAVE': '`',
    'KC_QUOTE': "'",
    'KC_BSLASH': '\\',
    'KC_BACKSLASH': '\\',
    'KC_COMMA': ',',
    'KC_DOT': '.',
    'KC_SLASH': '/',
    'KC_SCOLON': ';',
    'KC_SEMICOLON': ';',
    'KC_MINUS': '-',
    'KC_EQUAL': '=',
    'KC_LBRACKET': '[',
    'KC_RBRACKET': ']',
    'KC_TAB': 'Tab',
    'KC_SPACE': 'Space',
    'KC_SPC': 'Space',
    'KC_ENTER': 'Enter',
    'KC_ENT': 'Enter',
    'KC_BSPACE': 'Bsp',
    'KC_BSPC': 'Bsp',
    'KC_ESCAPE': 'Esc',
    'KC_ESC': 'Esc',
    'KC_DELETE': 'Del',
    'KC_DEL': 'Del',
    'KC_INSERT': 'Ins',
    'KC_INS': 'Ins',
    'KC_HOME': 'Home',
    'KC_END': 'End',
    'KC_PGUP': 'PgUp',
    'KC_PGDOWN': 'PgDn',
    'KC_PGDN': 'PgDn',
    'KC_LEFT': '←',
    'KC_RIGHT': '→',
    'KC_UP': '↑',
    'KC_DOWN': '↓',
    'KC_CAPSLOCK': 'CapsLock',
    'KC_CAPS': 'CapsLock',
    'KC_SCROLLLOCK': 'ScrollLock',
    'KC_SCRL': 'ScrollLock',
    'KC_PAUSE': 'Pause/Break',
    'KC_BRK': 'Pause/Break',
    'KC_BREAK': 'Pause/Break',
    'KC_PRINTSCREEN': 'PrintScreen',
    'KC_PSCR': 'PrintScreen',
    'KC_APPLICATION': 'App/Menu',
    'KC_APP': 'App/Menu',
    'KC_LSHIFT': 'LShift',
    'KC_LSFT': 'LShift',
    'KC_RSHIFT': 'RShift',
    'KC_RSFT': 'RShift',
    'KC_LCTRL': 'LCtrl',
    'KC_LCTL': 'LCtrl',
    'KC_RCTRL': 'RCtrl',
    'KC_RCTL': 'RCtrl',
    'KC_LALT': 'LAlt',
    'KC_RALT': 'AltGr',
    'KC_LGUI': '⌘ (left)',
    'KC_RGUI': '⌘ (right)',
    'KC_MUTE': 'Mute',
    'KC_VOLD': 'Vol−',
    'KC_VOLU': 'Vol+',
    'KC_MNXT': 'Next',
    'KC_MPRV': 'Prev',
    'KC_MPLY': 'Play',
    'KC_MSTP': 'Stop',
    'KC_BRID': 'Bri−',
    'KC_BRIU': 'Bri+',
    'QK_BOOT': '→ Bootloader',
    'QK_REBOOT': '→ Reboot',
}

# Shifted digits (US layout) and other LSFT(...) wrappers we want to translate.
_SHIFTED_DIGIT = {
    '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
    '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
}
_SHIFTED_KEY = {
    'KC_GRAVE': '~',
    'KC_QUOTE': '"',
    'KC_MINUS': '_',
    'KC_EQUAL': '+',
    'KC_LBRACKET': '{',
    'KC_RBRACKET': '}',
    'KC_BSLASH': '|',
    'KC_BACKSLASH': '|',
    'KC_COMMA': '<',
    'KC_DOT': '>',
    'KC_SLASH': '?',
    'KC_SCOLON': ':',
    'KC_SEMICOLON': ':',
}


def translate_keycode(kc: Any) -> str:
    """Return a Markdown-friendly description of a Vial keycode.

    Examples
    --------
    KC_GRAVE          → ``KC_GRAVE`` (`` ` ``)
    LSFT(KC_GRAVE)    → ``LSFT(KC_GRAVE)`` (`~`)
    LSFT(KC_2)        → ``LSFT(KC_2)`` (`@`)
    RALT(KC_5)        → ``RALT(KC_5)`` (AltGr+5)
    TD(33)            → ``TD(33)``
    MO(4)             → ``MO(4)`` (→ Layer 4)
    -1                → (slot unused)
    """
    if kc == -1 or kc is None:
        return '(slot unused)'
    if not isinstance(kc, str):
        return f'`{kc!r}`'

    code = '`' + kc + '`'

    # Direct lookup
    if kc in _DIRECT:
        glyph = _DIRECT[kc]
        if glyph.startswith('('):
            return glyph
        # Special-case: literal backtick char needs double-backtick fence in MD
        if glyph == '`':
            return f'{code} (`` ` ``)'
        return f'{code} (`{glyph}`)' if len(glyph) == 1 else f'{code} ({glyph})'

    # Shifted digit
    m = re.match(r'^LSFT\(KC_(\d)\)$', kc)
    if m and m.group(1) in _SHIFTED_DIGIT:
        g = _SHIFTED_DIGIT[m.group(1)]
        if g == '`':
            return f'{code} (`` ` ``)'
        return f'{code} (`{g}`)'

    # Shifted other-key
    m = re.match(r'^LSFT\((KC_\w+)\)$', kc)
    if m and m.group(1) in _SHIFTED_KEY:
        g = _SHIFTED_KEY[m.group(1)]
        if g == '`':
            return f'{code} (`` ` ``)'
        return f'{code} (`{g}`)'

    # AltGr (RALT)
    m = re.match(r'^RALT\(KC_(\w+)\)$', kc)
    if m:
        return f'{code} (AltGr+{m.group(1)})'

    # Layer-tap LT(N, KC)
    m = re.match(r'^LT(\d+)\((\w+)\)$', kc)
    if m:
        return f'{code} (tap=`{m.group(2)}`, hold=→ Layer {m.group(1)})'

    # MO(N) momentary layer
    m = re.match(r'^MO\((\d+)\)$', kc)
    if m:
        return f'{code} (→ Layer {m.group(1)})'

    # Plain digits
    m = re.match(r'^KC_(\d)$', kc)
    if m:
        return f'{code} (`{m.group(1)}`)'

    # Plain letters
    m = re.match(r'^KC_([A-Z])$', kc)
    if m:
        return f'{code} (`{m.group(1).lower()}`)'

    # F-keys, keypad
    if kc.startswith('KC_F') and kc[4:].isdigit():
        return f'{code} (F{kc[4:]})'
    if kc.startswith('KC_KP_'):
        return f'{code} (numpad {kc[6:]})'

    return code


def short_keycode(kc: Any) -> str:
    """Compact form for table cells: just `KC_NAME` or '(empty)'."""
    if kc == -1 or kc is None:
        return '—'
    if kc == 'KC_NO':
        return '(empty)'
    if kc == 'KC_TRNS':
        return '(transparent)'
    return translate_keycode(kc)


# ---------------------------------------------------------------------------
# Diff data structures
# ---------------------------------------------------------------------------

@dataclass
class LayoutDiff:
    layer: int
    sub: int
    key: int
    old: Any
    new: Any

    def position_label(self, base: str) -> str:
        labels = POS_BY_BASE[base][self.sub]
        pos = labels[self.key]
        # Annotate with side+row context for clarity
        side = SIDE_NAME[self.sub]
        row = ROW_NAME[self.sub]
        return f'{pos} ({side}-{row})'

    def kind(self) -> str:
        empty = ('KC_NO',)
        old_empty = self.old in empty or self.old == -1
        new_empty = self.new in empty or self.new == -1
        if old_empty and not new_empty:
            return 'filled'
        if not old_empty and new_empty:
            return 'cleared'
        return 'reassigned'


@dataclass
class TapDanceDiff:
    index: int
    old: list
    new: list

    def kind(self) -> str:
        old_active = self.old and self.old[0] not in ('KC_NO',)
        new_active = self.new and self.new[0] not in ('KC_NO',)
        if not old_active and new_active:
            return 'added'
        if old_active and not new_active:
            return 'cleared'
        return 'modified'


# ---------------------------------------------------------------------------
# Diff computation
# ---------------------------------------------------------------------------

def diff_layout(old_layout, new_layout):
    diffs = []
    n_layers = max(len(old_layout), len(new_layout))
    for L in range(n_layers):
        if L >= len(old_layout) or L >= len(new_layout):
            # Layer only present on one side — would be a structural change
            continue
        for sub_idx in range(len(old_layout[L])):
            for key_idx in range(len(old_layout[L][sub_idx])):
                old = old_layout[L][sub_idx][key_idx]
                new = new_layout[L][sub_idx][key_idx]
                if old != new:
                    diffs.append(LayoutDiff(L, sub_idx, key_idx, old, new))
    return diffs


def diff_tap_dance(old_td, new_td):
    diffs = []
    for i in range(min(len(old_td), len(new_td))):
        if old_td[i] != new_td[i]:
            diffs.append(TapDanceDiff(i, old_td[i], new_td[i]))
    return diffs


def count_used_tds(td_list):
    return sum(1 for td in td_list if td and td[0] not in ('KC_NO',))


def count_used_macros(macro_list):
    return sum(1 for m in macro_list if m)


def count_layers_with_content(layout):
    """A layer counts as 'with content' if any keycode in any sub-array
    is non-trivial (not KC_NO and not the -1 unused-slot placeholder)."""
    n = 0
    for layer in layout:
        has_content = False
        for sub in layer:
            for k in sub:
                if k not in ('KC_NO', -1, None):
                    has_content = True
                    break
            if has_content:
                break
        if has_content:
            n += 1
    return n


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_markdown(old_path, new_path, old_data, new_data,
                    old_name, new_name, title, base):
    layout_diffs = diff_layout(old_data['layout'], new_data['layout'])
    td_diffs = diff_tap_dance(old_data.get('tap_dance', []),
                              new_data.get('tap_dance', []))

    macro_changed = old_data.get('macro') != new_data.get('macro')
    combo_changed = old_data.get('combo') != new_data.get('combo')
    keyov_changed = old_data.get('key_override') != new_data.get('key_override')
    settings_changed = old_data.get('settings') != new_data.get('settings')
    encoder_changed = old_data.get('encoder_layout') != new_data.get('encoder_layout')

    # Resource counts
    old_td_used = count_used_tds(old_data.get('tap_dance', []))
    new_td_used = count_used_tds(new_data.get('tap_dance', []))
    old_td_max = len(old_data.get('tap_dance', []))
    new_td_max = len(new_data.get('tap_dance', []))
    old_m_used = count_used_macros(old_data.get('macro', []))
    new_m_used = count_used_macros(new_data.get('macro', []))
    old_m_max = len(old_data.get('macro', []))
    new_m_max = len(new_data.get('macro', []))
    old_layers_filled = count_layers_with_content(old_data['layout'])
    new_layers_filled = count_layers_with_content(new_data['layout'])
    old_layers_total = len(old_data['layout'])
    new_layers_total = len(new_data['layout'])

    out = []
    out.append(f'# {title}')
    out.append('')
    out.append('| | |')
    out.append('|---|---|')
    out.append(f'| **Old** | `{old_path.name}` (label: *{old_name}*) |')
    out.append(f'| **New** | `{new_path.name}` (label: *{new_name}*) |')
    out.append(f'| **Generated** | {date.today().isoformat()} |')
    out.append(f'| **Position labels** | {base} |')
    out.append('')

    # ---- Summary ----
    out.append('## Summary')
    out.append('')
    out.append('| Section | Changes | Status |')
    out.append('|---|---:|---|')
    out.append(f'| Layout cells | {len(layout_diffs)} | {"identical" if not layout_diffs else "modified"} |')
    out.append(f'| Tap Dance entries | {len(td_diffs)} | {"identical" if not td_diffs else "modified"} |')
    out.append(f'| Macros | — | {"modified" if macro_changed else "identical"} |')
    out.append(f'| Combos | — | {"modified" if combo_changed else "identical"} |')
    out.append(f'| Key Overrides | — | {"modified" if keyov_changed else "identical"} |')
    out.append(f'| Settings | — | {"modified" if settings_changed else "identical"} |')
    out.append(f'| Encoder layout | — | {"modified" if encoder_changed else "identical"} |')
    out.append('')

    # ---- Resource counts ----
    out.append('## Resource Budget')
    out.append('')
    out.append('| Resource | Old | New | Δ |')
    out.append('|---|---:|---:|---:|')
    delta_td = new_td_used - old_td_used
    out.append(f'| Tap Dance slots used | {old_td_used} / {old_td_max} | {new_td_used} / {new_td_max} | {delta_td:+d} |')
    delta_m = new_m_used - old_m_used
    out.append(f'| Macro slots used | {old_m_used} / {old_m_max} | {new_m_used} / {new_m_max} | {delta_m:+d} |')
    delta_l = new_layers_filled - old_layers_filled
    out.append(f'| Layers with content | {old_layers_filled} / {old_layers_total} | {new_layers_filled} / {new_layers_total} | {delta_l:+d} |')
    out.append('')

    # ---- Layout changes by layer ----
    out.append('## Layout Changes')
    out.append('')
    if not layout_diffs:
        out.append('*No layout cells changed.*')
        out.append('')
    else:
        # Group by layer
        by_layer = {}
        for d in layout_diffs:
            by_layer.setdefault(d.layer, []).append(d)
        for L in sorted(by_layer.keys()):
            ds = by_layer[L]
            kinds = {'filled': 0, 'cleared': 0, 'reassigned': 0}
            for d in ds:
                kinds[d.kind()] += 1
            kind_summary = ', '.join(f'{v} {k}' for k, v in kinds.items() if v)
            out.append(f'### Layer {L} — {len(ds)} change(s) ({kind_summary})')
            out.append('')
            out.append('| Position | Old | New | Type |')
            out.append('|---|---|---|---|')
            for d in ds:
                out.append(f'| {d.position_label(base)} | {short_keycode(d.old)} | {short_keycode(d.new)} | {d.kind()} |')
            out.append('')

    # ---- Tap Dance changes ----
    out.append('## Tap Dance Changes')
    out.append('')
    if not td_diffs:
        out.append('*No tap-dance entries changed.*')
        out.append('')
    else:
        for d in td_diffs:
            out.append(f'### TD({d.index}) — {d.kind()}')
            out.append('')
            out.append('| Field | Old | New |')
            out.append('|---|---|---|')
            field_names = ['Tap', 'Hold', 'Double', 'Tap-Hold', 'Term (ms)']
            for i, name in enumerate(field_names):
                old_v = d.old[i] if i < len(d.old) else '—'
                new_v = d.new[i] if i < len(d.new) else '—'
                if name == 'Term (ms)':
                    out.append(f'| {name} | {old_v} | {new_v} |')
                else:
                    out.append(f'| {name} | {short_keycode(old_v)} | {short_keycode(new_v)} |')
            out.append('')

    # ---- Other sections (macro / combo / etc.) ----
    out.append('## Other Sections')
    out.append('')
    if macro_changed:
        out.append('### Macros')
        old_m = old_data.get('macro', [])
        new_m = new_data.get('macro', [])
        out.append('')
        out.append('| Slot | Old | New |')
        out.append('|---:|---|---|')
        for i in range(max(len(old_m), len(new_m))):
            a = old_m[i] if i < len(old_m) else None
            b = new_m[i] if i < len(new_m) else None
            if a != b:
                out.append(f'| M{i} | `{a}` | `{b}` |')
        out.append('')
    else:
        out.append('- **Macros:** identical')
    if combo_changed:
        out.append('- **Combos:** modified (see raw JSON for details)')
    else:
        out.append('- **Combos:** identical')
    if keyov_changed:
        out.append('- **Key Overrides:** modified (see raw JSON for details)')
    else:
        out.append('- **Key Overrides:** identical')
    if settings_changed:
        out.append('- **Settings:** modified — note that Vial settings are stored as numeric IDs whose semantics depend on the firmware build')
    else:
        out.append('- **Settings:** identical')
    if encoder_changed:
        out.append('- **Encoder layout:** modified')
    else:
        out.append('- **Encoder layout:** identical')
    out.append('')

    # ---- Metadata ----
    out.append('## Metadata')
    out.append('')
    out.append('| Field | Old | New |')
    out.append('|---|---|---|')
    for k in ('version', 'vial_protocol', 'via_protocol', 'uid', 'layout_options'):
        a = old_data.get(k, '—')
        b = new_data.get(k, '—')
        marker = '' if a == b else ' ⚠'
        out.append(f'| `{k}` | `{a}` | `{b}`{marker} |')
    out.append('')

    out.append('---')
    out.append('')
    out.append(f'*Generated by `vil_diff.py` — '
               f'{len(layout_diffs)} layout cells + '
               f'{len(td_diffs)} tap dance changes detected.*')

    return '\n'.join(out)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Diff two Vial .vil keymap configurations and produce a Markdown report.',
        epilog='Position labels default to Colemak-DH; pass --base qwerty for QWERTY layouts.',
    )
    parser.add_argument('old', type=Path, help='Older .vil file')
    parser.add_argument('new', type=Path, help='Newer .vil file')
    parser.add_argument('-o', '--output', type=Path, default=None,
                        help='Output Markdown file (default: stdout)')
    parser.add_argument('--names', nargs=2, metavar=('OLD', 'NEW'),
                        help='Display labels for the two configs')
    parser.add_argument('--title', default=None,
                        help='Report title (default: derived from filenames)')
    parser.add_argument('--base', choices=['colemak-dh', 'qwerty'],
                        default='colemak-dh',
                        help='Base-layer letter mapping for position labels')
    args = parser.parse_args()

    if not args.old.exists():
        parser.error(f'Old file not found: {args.old}')
    if not args.new.exists():
        parser.error(f'New file not found: {args.new}')

    with open(args.old) as f:
        old_data = json.load(f)
    with open(args.new) as f:
        new_data = json.load(f)

    if args.names:
        old_name, new_name = args.names
    else:
        old_name = args.old.stem
        new_name = args.new.stem

    title = args.title or f'Vial Configuration Diff — {old_name} → {new_name}'

    md = render_markdown(args.old, args.new, old_data, new_data,
                         old_name, new_name, title, args.base)

    if args.output:
        args.output.write_text(md, encoding='utf-8')
        print(f'Wrote {args.output} ({len(md):,} chars)', file=sys.stderr)
    else:
        sys.stdout.write(md)


if __name__ == '__main__':
    main()
