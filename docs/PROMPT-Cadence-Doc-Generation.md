# Prompt: Cadence/Sonata/Coda Dokumentation aus Vial-Konfiguration generieren

Du erhältst eine Vial-Konfigurationsdatei (`.vil`) und eine bestehende HTML-Dokumentation einer früheren Version. Erstelle daraus eine neue Versions-Dokumentation. Diese Anweisungen sind verbindlich; weiche nicht ab und liefere nicht zwischendrin.

## Quelle der Wahrheit

Die Vial-Datei ist die **einzige** Quelle für Tastenbelegungen, Tap Dances, Macros, Layer-Inhalte. Die alte HTML-Doku liefert nur das **Layout-Template** (CSS, Sektionsstruktur, Hero-Bereich) — keine Inhalts-Annahmen. Übernimm niemals Inhalts-Beschreibungen aus der alten Doku ohne sie gegen die Vial-Datei zu verifizieren.

## Pflicht-Inputs vor dem Start

Bevor du Code schreibst, kläre per Rückfrage falls nicht aus der Konversation eindeutig:

1. **Layer-Namen** — die Vial-Datei kennt nur Layer-Nummern. Layer-Namen kommen aus der Konversation oder der alten Doku.
2. **Visuelle Konvention für Tasten-Anordnung**:
   - Linke Hand Reihenfolge auf dem Bildschirm (links nach rechts): `Q W F P B` / `A R S T G` / `Z X C D V` (für Cadence) — pinky außen links, inner außen rechts
   - Rechte Hand Reihenfolge auf dem Bildschirm (links nach rechts): `J L U Y '` / `M N E I O` / `K H , . /` — **NICHT gespiegelt**, also inner-Spalte (M/J/K) auf Bildschirm links, pinky-Spalte (O/Y/'/) auf Bildschirm rechts
   - Linke Daumen: `Spc Tab` (von Bildschirm links nach rechts)
   - Rechte Daumen: `Ent Bsp` (von Bildschirm links nach rechts, Ent unter K)
3. **Trigger-Map und Layer-Zuordnung** für die aktuelle Version — nicht aus der alten Doku übernehmen, sondern aus der Vial-Datei extrahieren und gegen die User-Aussage verifizieren.

## Vial-Daten-Extraktions-Konventionen

```
Sweep-Layout in Vial-Array:
  Layer = layout[L] mit 8 rows × 5 cols
  
  Linke Hand (rows 0-3):
    row 0 = top, row 1 = home, row 2 = bot, row 3 = thumbs
    Spalten 0-4 = pinky, ring, middle, index, inner
  
  Rechte Hand (rows 4-7):
    row 4 = top, row 5 = home, row 6 = bot, row 7 = thumbs
    Spalten 0-4 = inner, index, middle, ring, pinky
  
  Daumen-Zeilen haben nur cols 0-1 (rest -1):
    Linke row 3: col 0 = Spc, col 1 = Tab (in Cadence v1.9 Konvention)
    Rechte row 7: col 0 = Ent, col 1 = Bsp
```

**Beim Rendering:** Verwende die Vial-Spaltenreihenfolge **direkt ohne Reverse** für beide Hände. Das ergibt:
- Links: Vial col 0 → screen leftmost (pinky außen links)
- Rechts: Vial col 0 → screen leftmost (inner außen links, pinky außen rechts)

Das ist die Konvention die der User erwartet. Spiegele die rechte Seite NICHT visuell.

## Tasten-Resolver

Schreibe einen Resolver, der jede Vial-Zelle in ein lesbares Display-Label umwandelt. Berücksichtige:

| Vial-Wert | Display |
|---|---|
| `KC_X` (Buchstabe/Ziffer) | `X` |
| `KC_SPACE`, `KC_BSPACE`, `KC_ENTER`, `KC_TAB`, `KC_ESCAPE`, `KC_DELETE` | `Spc`, `Bsp`, `Ent`, `Tab`, `Esc`, `Del` |
| `KC_LSHIFT`, `KC_LCTRL`, `KC_LALT`, `KC_LGUI`, `KC_RALT`, `KC_APPLICATION` | `⇧`, `⌃`, `⌥`, `⌘`, `AltGr`, `App` |
| `KC_LEFT`, `KC_DOWN`, `KC_UP`, `KC_RIGHT` | `←`, `↓`, `↑`, `→` |
| `LSFT(KC_3)` und alle Shift-Symbole | das **produzierte Zeichen** (`#`), nicht `S+3` |
| `RALT(KC_Q)`, `RALT(KC_Y)`, `RALT(KC_P)`, `RALT(KC_S)`, `RALT(KC_5)` | `ä`, `ü`, `ö`, `ß`, `€` (deutsche Sonderzeichen) |
| `LGUI(KC_1)`, `SGUI(KC_1)` | `⌘+1`, `⌘⇧+1` |
| `TD(n)` — wenn hold = `MO(L)` | nur den Tap-Buchstaben (Layer-Trigger) |
| `TD(n)` — sonst | `tap · hold` oder `tap · double` mit Mittelpunkt-Trenner |
| `TD(n)` — wenn Tap oder Hold ein Pipe enthält | ` / ` als Trenner statt ` · ` (Kollisionsvermeidung) |
| `Mn` (Macro) | das produzierte Zeichen, falls bekannt; sonst `Mn` |
| `LTn(KC_X)` | nur den Tap-Buchstaben |

**Macros mit Text-Output** (`[["text", "$?"]]`) lassen sich direkt zum Text auflösen. **Komplexe Tap-Sequenz-Macros** (z.B. M8 = `[tap LSFT(4) LSFT(9) LSFT(0) LEFT]` für `$()` mit Cursor in Mitte) brauchen eine manuelle Mapping-Tabelle:

```python
COMPLEX_MACRO_LABELS = {
    2: "' ", 3: "''' ", 4: '" ',
    8: '$()', 9: '${}',
    16: 'Ä', 17: 'Ü', 18: 'Ö',
}
```

Diese Tabelle muss du beim Lesen der Vial-Datei **gegen die echten Macro-Inhalte verifizieren** — die Indizes können sich zwischen Versionen verschieben.

## Pflicht-Sektionen der neuen Doku

In dieser Reihenfolge:

1. **Hero**: Title (`Cadence v[VERSION] — Layout Documentation`), Sub-title (`v[VERSION] — Layout Documentation · Ferris Sweep · Colemak-DH · Vial / QMK`), Hero-Badges (Version, "[N] reachable layers", "[X]/64 TD · [Y]/32 Macros", weitere Tags)
2. **Changelog [PREV] → [NEW]** — ausführlicher Block mit drei Tabellen (Layer Renumbering, Access Key Reassignment, Other Changes) und Migration Notes
3. **What is different from Cadenza** (für Cadence) bzw. analoge Vergleichssektion
4. **Why Cadence over standard Miryoku** (für Cadence)
5. **Design Principles**
6. **Layer Access Map** — Tabelle aller Layer mit Trigger und Position
7. **Layer Reference** — eine Karte pro Layer, jede mit:
   - Header (Layer-ID, Name, Trigger)
   - Beschreibung (1-3 Sätze, **inhaltlich aus Vial verifiziert**)
   - Visualisierung der 34 Tasten in der oben spezifizierten Reihenfolge
   - Activator-Markierung (★ am Position-Label, blauer Hintergrund) für die Tasten, die diesen Layer triggern
   - Auf Base-Layer: Access-Key-Markierung (orange Border, L-Badge oben links) für Tasten, die andere Layer triggern
8. **Tap Dance Reference** — Summary-Tabelle (Gruppen + Counts) und Detail-Tabelle (alle verwendeten TDs gruppiert nach Funktion: HRMs, Layer-Access, Action-TDs pro Layer)
9. **Macro Reference** — gruppiert nach Kategorie (Shell-Helpers, Code-Operators, Umlaut-Capitals, Apostroph-Helpers)
10. **Firmware Notes** — TAP_DANCE_ENTRIES Anforderung, Settings-Block-Hinweis

## CSS-Anforderungen für Layer-Karten

```
.kb { display:flex; gap:60px; align-items:flex-start; justify-content:center; padding:10px }
.kb-half { display:flex; flex-direction:column; flex:0 0 300px; gap:3px }
.key-row { display:flex; gap:3px }
.key-thumbs { margin-top:6px }

/* Linke Daumen-Cluster sitzt unter D/V */
.key-thumbs-l { margin-left:171px }   /* = 3 × (54px Tasten-Breite + 3px gap) */
/* Rechte Daumen-Cluster sitzt unter K/H */
.key-thumbs-r { margin-left:0 }

/* Tasten: 54×48px, Daumen 54×42px */
.key { width:54px; height:48px; ... }
.key-thumbs .key { height:42px }

/* Sichtbarkeit: inaktive Tasten MÜSSEN voll sichtbar sein */
.key-empty { 
    border-color:#D8D2C0; background:#F0ECE0; color:#888; 
    opacity:1;       /* NIEMALS opacity < 1 */
    box-shadow:0 1px 0 #BFB8A4 
}

/* Aktive Tasten (Activators): klar erkennbar, deutlich blau */
.key-active { 
    border-color:#1A2870; background:#3B4BA8; color:#FFFFFF; 
    border-width:2px; box-shadow:0 2px 0 #0A1855 
}

/* Access-Keys (auf Base): orange */
.key-access { 
    border-color:#C77A12; background:#FDE9C8; color:#3A2810; 
    border-width:2px; box-shadow:0 2px 0 #A06200 
}
```

## Pflicht-Audit VOR Lieferung

Bevor du die fertige Datei lieferst, lasse einen automatisierten Verifikations-Check über die generierte HTML laufen, der **explizit** prüft:

### Check-1: Hero-Bereich
- Title enthält `v[NEW_VERSION]`
- `<div class="subtitle">` enthält `v[NEW_VERSION]` (nicht die alte Version!)
- Hero-Badges zeigen `[N] reachable layers` und `[X]/64 TD` mit den **tatsächlichen** Werten aus der Vial-Datei (selbst zählen, nicht aus der alten Doku übernehmen)

### Check-2: Layer-Karten Position-Reihenfolge
Für **jeden** der 12 Layer extrahiere die Reihenfolge der Position-Labels (`<span class="key-pos">X</span>`) und vergleiche **exakt** gegen:
```python
expected = ['Q','W','F','P','B', 'A','R','S','T','G', 'Z','X','C','D','V',
            'Spc','Tab',
            'J','L','U','Y',"'", 'M','N','E','I','O', 'K','H',',','.','/',
            'Ent','Bsp']
```

### Check-3: Activator-Markierungen
Für jeden Modal-Layer (L1-L11 außer L10) prüfe, dass die ★-markierten Position(en) den erwarteten Triggern entsprechen.

### Check-4: Access-Key-Markierungen auf Base
Zähle `key-access` auf Base-Layer. Muss **exakt** der Anzahl unique Layer-Trigger entsprechen — typischerweise 16 (bilateral × 5 + 4 Daumen + 2 Long-Hold pinky-top).

### Check-5: Inaktive Tasten Sichtbarkeit
CSS `.key-empty` muss `opacity:1` haben (oder kein opacity-Property). NIE `opacity: 0.5` oder ähnlich — das war ein Fehler in einer früheren Iteration.

### Check-6: Versions-Mentions
Liste alle `v[OLD_VERSION]`-Erwähnungen in der HTML auf. **Jede** Erwähnung muss klassifiziert werden:
- ✓ historisch (in Changelog-Tabelle, "Migration notes for users coming from", "Both were ... in v[OLD]", "unchanged from v[X]–v[OLD]") → behalten
- ✗ stale (Hero, "What's new in v[OLD]" Callout, Design Principles "rule holds in v[OLD]", Vergleichstabellen-Pills) → **fixen**

Liefere nicht, solange noch eine v[OLD]-Erwähnung außerhalb historischer Kontexte existiert.

### Check-7: Inhaltliche Vial-Realität
Für mindestens 3 Layer (vorzugsweise die mit Symbol-/Macro-Inhalten) verifiziere stichprobenartig:
- Was die Layer-Description verspricht (z.B. "Backtick TD on R_idx_bot")
- Mit dem was an dieser Position in der Vial-Datei tatsächlich steht

Wenn die Description nicht zur Vial-Datei passt: Description anpassen (oder User fragen falls Vial die Absicht nicht erfüllt).

### Check-8: Inner-Column-Regel
Für L1–L11 prüfe, ob G (row 1 col 4) und M (row 5 col 0) auf KC_NO oder KC_TRNS stehen. Falls Verstöße existieren, dokumentiere sie als Anmerkung — fixe sie nicht selbst, frage den User.

## Anti-Pattern: Was NICHT tun

- **Nicht** TD(n)-Hold-Werte als reine `MO(L)`-Targets bei Long-Hold-Triggern (Q, ') übersehen — diese 500ms-TDs sind ebenfalls Layer-Trigger und müssen als Access-Key markiert werden
- **Nicht** den 47/49/50/64-TD-Count aus der alten Doku übernehmen — neu zählen aus der Vial-Datei (Slot ist "verwendet" wenn mindestens einer der ersten 4 Slots != KC_NO ist; ein Slot mit nur Tap-Wert (z.B. TD(15)/X nach v1.9 ohne MO) zählt als verwendet, nicht als frei)
- **Nicht** die rechte Hand visuell spiegeln (das ist ein häufiger Fehler bei Split-KB-Docs, aber der User will Vial-Spaltenreihenfolge direkt)
- **Nicht** Layer-Beschreibungen aus der alten Doku 1:1 übernehmen, wenn der Layer-Inhalt in der neuen Version geändert wurde
- **Nicht** "fertig" sagen ohne den vollständigen Audit Check 1-8 durchgelaufen zu haben — auch nicht bei Zeitdruck
- **Nicht** mehrere kleine Patches hintereinander liefern — sammle Befunde, fixe alles, liefere einmal

## Wenn du unsicher bist

Wenn die Vial-Datei und die User-Aussage einander widersprechen (z.B. Vial sagt `Spc-thumb=KC_MINUS, Tab-thumb=KC_EQUAL` aber User sagte einmal "= auf Spc, - auf Tab"): **frage den User**, welche der beiden Versionen die Absicht ist. Nimm nicht eine Seite an. Solche Konflikte als "Inhaltliche Inkonsistenz vor Klärung" auflisten, nicht stillschweigend auf eine Seite entscheiden.

## Lieferformat

Eine einzige HTML-Datei in `/mnt/user-data/outputs/Cadence-v[VERSION]-Documentation.html`, gefolgt von einer `present_files`-Aktion und einer kurzen, knappen Zusammenfassung (max. 10 Zeilen):

- Was geändert wurde gegenüber der alten Version
- Was verifiziert wurde (Audit-Punkte 1-8 als Liste)
- Bekannte Limitierungen oder bewusst nicht gefixte Stellen mit Begründung

**Nicht** mehr als das. Kein "ich hoffe, das hilft", keine Werbe-Sprache. Knapp, faktisch, vollständig.
