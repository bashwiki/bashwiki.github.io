# [Linux] Bash trap Verwendung: Behandeln von Signalen und Fehlern

## Übersicht
Der `trap` Befehl in Bash wird verwendet, um bestimmte Aktionen auszuführen, wenn ein Skript ein Signal empfängt oder einen Fehler auftritt. Dies ist besonders nützlich, um Ressourcen freizugeben oder um sicherzustellen, dass bestimmte Bereinigungsaktionen durchgeführt werden, bevor das Skript beendet wird.

## Verwendung
Die grundlegende Syntax des `trap` Befehls lautet:

```bash
trap [Aktion] [Signal]
```

## Häufige Optionen
- `EXIT`: Führt die angegebene Aktion aus, wenn das Skript beendet wird.
- `SIGINT`: Reagiert auf das Interrupt-Signal (z. B. Ctrl+C).
- `SIGTERM`: Reagiert auf das Terminationssignal.
- `ERR`: Führt die angegebene Aktion aus, wenn ein Fehler auftritt.

## Häufige Beispiele

### Beispiel 1: Aufräumarbeiten bei Skriptbeendigung
```bash
trap 'echo "Skript wird beendet"; rm -f temp.txt' EXIT
```
In diesem Beispiel wird eine Nachricht ausgegeben und die Datei `temp.txt` gelöscht, wenn das Skript beendet wird.

### Beispiel 2: Abfangen von Interrupt-Signalen
```bash
trap 'echo "Interrupt empfangen, Skript wird abgebrochen"; exit' SIGINT
```
Hier wird eine Nachricht angezeigt und das Skript beendet, wenn ein Interrupt-Signal empfangen wird.

### Beispiel 3: Fehlerbehandlung
```bash
trap 'echo "Ein Fehler ist aufgetreten"; exit 1' ERR
```
In diesem Fall wird eine Fehlermeldung ausgegeben und das Skript mit einem Fehlerstatus beendet, wenn ein Fehler auftritt.

## Tipps
- Verwenden Sie `trap` in Kombination mit `EXIT`, um sicherzustellen, dass Aufräumarbeiten immer durchgeführt werden, unabhängig davon, wie das Skript beendet wird.
- Testen Sie Ihre `trap`-Befehle gründlich, um sicherzustellen, dass sie wie gewünscht funktionieren, insbesondere bei der Fehlerbehandlung.
- Seien Sie vorsichtig mit der Verwendung von `trap` in langen Skripten, da es zu unerwartetem Verhalten führen kann, wenn Signale nicht richtig behandelt werden.