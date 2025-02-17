# [Linux] Bash killall Verwendung: Beenden von Prozessen nach Namen

## Übersicht
Der Befehl `killall` wird verwendet, um Prozesse zu beenden, die einen bestimmten Namen haben. Im Gegensatz zu `kill`, das eine spezifische Prozess-ID benötigt, ermöglicht `killall` das Beenden aller Instanzen eines Programms anhand seines Namens.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
killall [Optionen] [Argumente]
```

## Häufige Optionen
- `-u <Benutzer>`: Beendet nur die Prozesse, die von einem bestimmten Benutzer gestartet wurden.
- `-i`: Fragt vor dem Beenden jedes Prozesses nach Bestätigung.
- `-q`: Unterdrückt die Ausgabe von Fehlern, wenn kein Prozess gefunden wird.
- `-s <Signal>`: Sendet ein bestimmtes Signal an die Prozesse (Standard ist `TERM`).

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `killall`:

1. Beenden aller Instanzen von Firefox:
   ```bash
   killall firefox
   ```

2. Beenden aller Prozesse eines bestimmten Benutzers:
   ```bash
   killall -u benutzername
   ```

3. Beenden von Prozessen mit Bestätigungsaufforderung:
   ```bash
   killall -i firefox
   ```

4. Senden eines bestimmten Signals (z.B. `KILL`) an alle Instanzen von `gedit`:
   ```bash
   killall -s KILL gedit
   ```

5. Unterdrücken von Fehlermeldungen, wenn kein Prozess gefunden wird:
   ```bash
   killall -q gnome-terminal
   ```

## Tipps
- Verwenden Sie die Option `-i`, um versehentliche Beendigungen zu vermeiden, insbesondere bei kritischen Anwendungen.
- Seien Sie vorsichtig beim Einsatz von `killall`, da es alle Prozesse mit dem angegebenen Namen beendet, was zu Datenverlust führen kann, wenn ungespeicherte Arbeiten vorhanden sind.
- Nutzen Sie `killall -l`, um eine Liste der verfügbaren Signale anzuzeigen, die Sie mit der `-s` Option verwenden können.