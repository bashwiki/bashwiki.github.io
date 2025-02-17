# [Linux] Bash local Verwendung: Lokale Variablen definieren

## Übersicht
Der Befehl `local` wird in Bash-Skripten verwendet, um lokale Variablen innerhalb einer Funktion zu definieren. Diese Variablen sind nur innerhalb der Funktion sichtbar und beeinflussen nicht die globalen Variablen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
local [Optionen] [Variablenname]=[Wert]
```

## Häufige Optionen
- **-n**: Weist die Variable als Namensreferenz zu, sodass sie auf eine andere Variable verweist.
- **-i**: Setzt die Variable als Ganzzahl, was bedeutet, dass alle Zuweisungen als Ganzzahlen behandelt werden.

## Häufige Beispiele

### Beispiel 1: Einfache lokale Variable
```bash
function meine_funktion {
    local meine_variable="Hallo Welt"
    echo $meine_variable
}
meine_funktion
# Ausgabe: Hallo Welt
```

### Beispiel 2: Lokale Variable mit einer Berechnung
```bash
function berechnung {
    local zahl1=5
    local zahl2=10
    local summe=$((zahl1 + zahl2))
    echo $summe
}
berechnung
# Ausgabe: 15
```

### Beispiel 3: Verwendung von Namensreferenzen
```bash
function referenz {
    local -n referenz_variable=$1
    referenz_variable="Neuer Wert"
}
meine_variable="Alter Wert"
referenz meine_variable
echo $meine_variable
# Ausgabe: Neuer Wert
```

## Tipps
- Verwenden Sie `local`, um die Sichtbarkeit von Variablen zu steuern und Konflikte mit globalen Variablen zu vermeiden.
- Es ist eine gute Praxis, `local` am Anfang einer Funktion zu verwenden, um alle lokalen Variablen zu definieren.
- Denken Sie daran, dass lokale Variablen nach dem Verlassen der Funktion nicht mehr verfügbar sind.