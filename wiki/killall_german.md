# [리눅스] Bash killall 사용법

## Übersicht
Der Befehl `killall` wird in der Bash verwendet, um Prozesse anhand ihres Namens zu beenden. Im Gegensatz zu anderen Befehlen wie `kill`, der eine Prozess-ID benötigt, ermöglicht `killall` das gezielte Beenden mehrerer Prozesse, die denselben Namen haben. Dies ist besonders nützlich, wenn mehrere Instanzen eines Programms ausgeführt werden und Sie alle gleichzeitig schließen möchten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
killall [OPTIONEN] PROZESSNAME
```

### Häufige Optionen:
- `-u, --user`: Beendet nur die Prozesse, die von einem bestimmten Benutzer gestartet wurden.
- `-q, --quiet`: Unterdrückt die Ausgabe von Fehlermeldungen, wenn kein Prozess gefunden wird.
- `-I, --ignore-case`: Ignoriert die Groß- und Kleinschreibung bei der Angabe des Prozessnamens.
- `-s, --signal`: Gibt das Signal an, das an die Prozesse gesendet werden soll (z.B. `SIGTERM`, `SIGKILL`).

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `killall`:

1. Beenden aller Instanzen des Programms `firefox`:

   ```bash
   killall firefox
   ```

   Dieser Befehl sendet das Standard-Signal `SIGTERM` an alle laufenden `firefox`-Prozesse, um sie zu beenden.

2. Beenden aller `python`-Prozesse, die von einem bestimmten Benutzer gestartet wurden:

   ```bash
   killall -u benutzername python
   ```

   Hierbei wird nur die `python`-Instanz beendet, die vom Benutzer `benutzername` ausgeführt wird.

## Tipps
- Seien Sie vorsichtig beim Einsatz von `killall`, da es alle Prozesse mit dem angegebenen Namen beendet. Dies kann zu Datenverlust führen, wenn Sie nicht gespeicherte Arbeiten in einer Anwendung haben.
- Verwenden Sie die Option `-q`, um die Ausgabe zu minimieren, wenn Sie nicht sicher sind, ob der Prozess läuft.
- Testen Sie den Befehl zunächst mit einem weniger kritischen Prozess, um sich mit der Funktionsweise vertraut zu machen.
- Nutzen Sie `killall -I`, wenn Sie nicht sicher sind, ob der Prozessname in Groß- oder Kleinschreibung eingegeben wurde.

Mit diesen Informationen sind Sie gut gerüstet, um den Befehl `killall` effektiv in Ihrer Bash-Umgebung zu verwenden.