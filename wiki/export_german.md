# [Linux] Bash export Verwendung: Umgebungsvariablen setzen

## Übersicht
Der Befehl `export` wird in Bash verwendet, um Umgebungsvariablen zu setzen und sie für untergeordnete Prozesse verfügbar zu machen. Wenn eine Variable mit `export` deklariert wird, wird sie für alle nachfolgenden Shell-Sitzungen und Prozesse, die von der aktuellen Shell gestartet werden, sichtbar.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
export [Optionen] [Argumente]
```

## Häufige Optionen
- `-p`: Zeigt alle exportierten Variablen an.
- `-n`: Entfernt die Exportmarkierung von einer Variablen, sodass sie nicht mehr für untergeordnete Prozesse verfügbar ist.

## Häufige Beispiele

### Beispiel 1: Eine neue Umgebungsvariable setzen
Um eine neue Umgebungsvariable namens `MEINE_VAR` zu setzen, verwenden Sie:

```bash
export MEINE_VAR="Hallo Welt"
```

### Beispiel 2: Eine bestehende Variable ändern
Um den Wert einer bereits existierenden Umgebungsvariable zu ändern, führen Sie Folgendes aus:

```bash
export MEINE_VAR="Neuer Wert"
```

### Beispiel 3: Alle exportierten Variablen anzeigen
Um alle aktuell exportierten Variablen anzuzeigen, verwenden Sie:

```bash
export -p
```

### Beispiel 4: Export einer Variablen ohne Wert
Um eine Variable zu exportieren, ohne ihr einen Wert zuzuweisen, verwenden Sie:

```bash
export MEINE_VAR
```

## Tipps
- Verwenden Sie `export` immer, wenn Sie sicherstellen möchten, dass eine Variable für untergeordnete Prozesse verfügbar ist.
- Überprüfen Sie regelmäßig Ihre exportierten Variablen mit `export -p`, um sicherzustellen, dass keine unnötigen Variablen gesetzt sind.
- Seien Sie vorsichtig beim Überschreiben von bestehenden Variablen, da dies zu unerwartetem Verhalten führen kann.