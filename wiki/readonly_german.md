# [Linux] Bash readonly Verwendung: Variablen als schreibgeschützt festlegen

## Übersicht
Der `readonly` Befehl in Bash wird verwendet, um Variablen als schreibgeschützt zu deklarieren. Das bedeutet, dass einmal gesetzte Werte nicht mehr verändert werden können, was hilfreich ist, um versehentliche Änderungen zu vermeiden.

## Verwendung
Die grundlegende Syntax des `readonly` Befehls lautet:

```bash
readonly [options] [arguments]
```

## Häufige Optionen
- `-p`: Gibt eine Liste aller schreibgeschützten Variablen und deren Werte aus.

## Häufige Beispiele

### Beispiel 1: Eine schreibgeschützte Variable erstellen
```bash
readonly MEINE_VARIABLE="Hallo Welt"
```
In diesem Beispiel wird die Variable `MEINE_VARIABLE` auf "Hallo Welt" gesetzt und als schreibgeschützt markiert.

### Beispiel 2: Versuch, eine schreibgeschützte Variable zu ändern
```bash
MEINE_VARIABLE="Neue Werte"  # Dies wird einen Fehler auslösen
```
Wenn Sie versuchen, den Wert von `MEINE_VARIABLE` zu ändern, wird Bash einen Fehler ausgeben, da die Variable schreibgeschützt ist.

### Beispiel 3: Auflisten schreibgeschützter Variablen
```bash
readonly -p
```
Dieser Befehl listet alle schreibgeschützten Variablen und deren Werte auf.

## Tipps
- Verwenden Sie `readonly`, um wichtige Variablen zu schützen, die nicht versehentlich geändert werden sollten.
- Überprüfen Sie regelmäßig schreibgeschützte Variablen mit `readonly -p`, um sicherzustellen, dass sie korrekt gesetzt sind.
- Seien Sie vorsichtig, wenn Sie `readonly` verwenden, da es nicht möglich ist, den schreibgeschützten Status einer Variablen zu entfernen, ohne die Shell neu zu starten oder eine neue Shell-Instanz zu öffnen.