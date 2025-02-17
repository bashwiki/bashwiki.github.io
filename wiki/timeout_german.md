# [Linux] Bash timeout Verwendung: Begrenzt die Ausführungszeit eines Befehls

## Übersicht
Der `timeout` Befehl in Bash wird verwendet, um die Ausführungszeit eines anderen Befehls zu begrenzen. Wenn der angegebene Befehl die festgelegte Zeit überschreitet, wird er automatisch beendet. Dies ist besonders nützlich, um sicherzustellen, dass Skripte oder Prozesse nicht unendlich lange laufen.

## Verwendung
Die grundlegende Syntax des `timeout` Befehls lautet:

```bash
timeout [Optionen] Dauer Befehl [Argumente]
```

## Häufige Optionen
- `-s, --signal SIGNAL`: Gibt das Signal an, das gesendet werden soll, wenn der Timeout erreicht ist (Standard ist `SIGTERM`).
- `--preserve-status`: Beibehaltung des Exit-Status des Befehls, auch wenn er durch `timeout` beendet wurde.
- `-v, --verbose`: Gibt eine Meldung aus, wenn der Timeout erreicht wird.

## Häufige Beispiele

1. **Ein einfacher Timeout von 5 Sekunden für einen Befehl:**
   ```bash
   timeout 5s sleep 10
   ```
   In diesem Beispiel wird der `sleep` Befehl nach 5 Sekunden abgebrochen, obwohl er 10 Sekunden dauern würde.

2. **Verwendung eines anderen Signals:**
   ```bash
   timeout -s SIGKILL 5s sleep 10
   ```
   Hier wird der `sleep` Befehl nach 5 Sekunden mit dem `SIGKILL` Signal beendet.

3. **Beibehaltung des Exit-Status:**
   ```bash
   timeout --preserve-status 5s false
   echo $?
   ```
   In diesem Fall wird der Befehl `false` nach 5 Sekunden beendet, und der Exit-Status bleibt erhalten, sodass der Wert von `$?` den Status von `false` anzeigt.

4. **Verbose Ausgabe aktivieren:**
   ```bash
   timeout -v 5s sleep 10
   ```
   Dies gibt eine Meldung aus, wenn der Timeout erreicht wird.

## Tipps
- Verwenden Sie `--preserve-status`, wenn Sie den Exit-Status des Befehls nach dem Timeout benötigen.
- Experimentieren Sie mit verschiedenen Signalen, um zu sehen, welches Verhalten für Ihre Anwendung am besten geeignet ist.
- Nutzen Sie `timeout` in Skripten, um sicherzustellen, dass Prozesse nicht hängen bleiben und Ressourcen blockieren.