# [Linux] Bash pkill Verwendung: Prozesse nach Namen beenden

## Übersicht
Der `pkill` Befehl wird verwendet, um Prozesse basierend auf ihrem Namen oder anderen Attributen zu beenden. Er ist besonders nützlich, wenn Sie mehrere Instanzen eines Programms gleichzeitig schließen möchten, ohne die Prozess-ID (PID) manuell suchen zu müssen.

## Verwendung
Die grundlegende Syntax des `pkill` Befehls lautet:

```bash
pkill [Optionen] [Argumente]
```

## Häufige Optionen
- `-f`: Sucht nach dem vollständigen Befehl, nicht nur nach dem Prozessnamen.
- `-n`: Beendet nur den neuesten Prozess, der dem angegebenen Namen entspricht.
- `-o`: Beendet nur den ältesten Prozess, der dem angegebenen Namen entspricht.
- `-signal`: Gibt an, welches Signal an den Prozess gesendet werden soll (z. B. `-9` für SIGKILL).

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `pkill`:

1. Beenden eines Prozesses mit dem Namen "firefox":
   ```bash
   pkill firefox
   ```

2. Beenden aller Prozesse, die mit "python" beginnen:
   ```bash
   pkill python
   ```

3. Beenden des neuesten Prozesses mit dem Namen "myapp":
   ```bash
   pkill -n myapp
   ```

4. Beenden eines Prozesses mit einem bestimmten Signal (z. B. SIGKILL):
   ```bash
   pkill -9 firefox
   ```

5. Beenden von Prozessen basierend auf dem vollständigen Befehl:
   ```bash
   pkill -f "python script.py"
   ```

## Tipps
- Verwenden Sie `pkill -l`, um eine Liste der verfügbaren Signale zu erhalten, die Sie an Prozesse senden können.
- Seien Sie vorsichtig beim Einsatz von `pkill`, insbesondere mit dem `-9` Signal, da dies Prozesse sofort beendet, ohne ihnen die Möglichkeit zu geben, ihre Arbeit zu speichern.
- Testen Sie den Befehl zuerst mit `pgrep`, um sicherzustellen, dass Sie die richtigen Prozesse anvisieren, bevor Sie sie mit `pkill` beenden.