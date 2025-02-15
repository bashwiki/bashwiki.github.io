# [리눅스] Bash timeout 사용법

## Übersicht
Der `timeout` Befehl in Bash wird verwendet, um einen bestimmten Prozess oder Befehl nach einer festgelegten Zeitspanne zu beenden. Dies ist besonders nützlich, wenn Sie sicherstellen möchten, dass ein Skript oder ein Befehl nicht unbegrenzt läuft und Ressourcen verbraucht. Mit `timeout` können Sie die Ausführungszeit eines Befehls kontrollieren und gegebenenfalls beenden, wenn dieser zu lange dauert.

## Verwendung
Die grundlegende Syntax des `timeout` Befehls lautet:

```bash
timeout [OPTIONEN] DURATION COMMAND [ARGUMENTE...]
```

Hierbei sind die wichtigsten Komponenten:
- `DURATION`: Die Zeitspanne, nach der der Befehl beendet werden soll. Dies kann in Sekunden (z.B. `10s`), Minuten (z.B. `5m`) oder Stunden (z.B. `1h`) angegeben werden.
- `COMMAND`: Der auszuführende Befehl, der möglicherweise zeitlich begrenzt werden soll.
- `ARGUMENTE`: Optionale Argumente, die an den Befehl übergeben werden.

### Häufige Optionen
- `-s`, `--signal`: Gibt das Signal an, das an den Befehl gesendet werden soll, wenn die Zeit abläuft. Standardmäßig wird das `SIGTERM` Signal verwendet.
- `-k`, `--kill-after`: Gibt eine zusätzliche Zeitspanne an, nach der ein `SIGKILL` Signal gesendet wird, falls der Befehl nicht bereits beendet wurde.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des `timeout` Befehls:

1. Beenden eines Befehls nach 5 Sekunden:
   ```bash
   timeout 5s sleep 10
   ```
   In diesem Beispiel wird der `sleep` Befehl, der normalerweise 10 Sekunden dauert, nach 5 Sekunden beendet.

2. Verwendung eines spezifischen Signals:
   ```bash
   timeout -s SIGINT 3s ping google.com
   ```
   Hier wird der `ping` Befehl nach 3 Sekunden mit dem `SIGINT` Signal beendet.

## Tipps
- Verwenden Sie `timeout` in Skripten, um sicherzustellen, dass lang laufende Prozesse nicht unbeaufsichtigt bleiben.
- Testen Sie die Zeitüberschreitungen in einer sicheren Umgebung, um sicherzustellen, dass wichtige Prozesse nicht versehentlich beendet werden.
- Nutzen Sie die `--kill-after` Option, um sicherzustellen, dass Prozesse, die nicht auf das erste Signal reagieren, nach einer bestimmten Zeit endgültig beendet werden.