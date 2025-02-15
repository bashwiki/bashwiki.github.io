# [리눅스] Bash trap 사용법

## Überblick
Der `trap`-Befehl in Bash wird verwendet, um bestimmte Aktionen auszuführen, wenn das Skript ein Signal empfängt oder wenn es auf bestimmte Ereignisse stößt, wie z.B. das Beenden des Skripts. Dies ist besonders nützlich, um Ressourcen freizugeben, temporäre Dateien zu löschen oder eine saubere Beendigung des Skripts zu gewährleisten.

## Verwendung
Die grundlegende Syntax des `trap`-Befehls lautet:

```bash
trap 'Befehle' SIGNAL
```

Hierbei steht `Befehle` für die Aktionen, die ausgeführt werden sollen, und `SIGNAL` für das Signal, das den `trap`-Befehl auslöst. Zu den häufigsten Signalen gehören:

- `SIGINT` (Interrupt, z.B. durch Drücken von Ctrl+C)
- `SIGTERM` (Termination, z.B. durch den Befehl `kill`)
- `EXIT` (wird ausgeführt, wenn das Skript beendet wird)

## Beispiele

### Beispiel 1: Aufräumen bei Skriptbeendigung
In diesem Beispiel wird ein temporäres Verzeichnis erstellt und beim Beenden des Skripts gelöscht.

```bash
#!/bin/bash

temp_dir=$(mktemp -d)

trap 'rm -rf "$temp_dir"' EXIT

echo "Temporäres Verzeichnis erstellt: $temp_dir"
# Hier können weitere Befehle ausgeführt werden

# Skript läuft weiter...
sleep 10
```

### Beispiel 2: Abfangen von Interrupt-Signalen
In diesem Beispiel wird ein Signal abgefangen, wenn das Skript durch Ctrl+C unterbrochen wird.

```bash
#!/bin/bash

trap 'echo "Skript wurde unterbrochen!"; exit' SIGINT

echo "Drücken Sie Ctrl+C, um das Skript zu unterbrechen."
while true; do
    sleep 1
done
```

## Tipps
- Verwenden Sie `trap` mit dem `EXIT`-Signal, um sicherzustellen, dass Aufräumarbeiten immer durchgeführt werden, unabhängig davon, wie das Skript beendet wird.
- Testen Sie Ihr Skript gründlich, um sicherzustellen, dass alle Ressourcen korrekt freigegeben werden, insbesondere wenn Sie mit temporären Dateien oder Netzwerkanfragen arbeiten.
- Seien Sie vorsichtig bei der Verwendung von `trap` in komplexen Skripten, da es zu unerwartetem Verhalten führen kann, wenn mehrere `trap`-Befehle für verschiedene Signale definiert sind.