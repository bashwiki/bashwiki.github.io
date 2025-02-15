# [리눅스] Bash at 사용법

## Übersicht
Der Befehl `at` wird in Unix-ähnlichen Betriebssystemen verwendet, um Aufgaben zu einem bestimmten Zeitpunkt in der Zukunft zu planen. Mit `at` können Benutzer Befehle oder Skripte zu einem festgelegten Zeitpunkt ausführen, was besonders nützlich ist, um wiederkehrende Aufgaben oder einmalige Jobs zu automatisieren.

## Verwendung
Die grundlegende Syntax des `at`-Befehls lautet:

```bash
at [OPTIONEN] ZEIT
```

Hierbei sind die wichtigsten Optionen:

- `-f DATEI`: Gibt eine Datei an, die die Befehle enthält, die zu dem angegebenen Zeitpunkt ausgeführt werden sollen.
- `-l`: Listet die geplanten Aufträge auf.
- `-d JOB_ID`: Löscht einen bestimmten geplanten Auftrag.
- `-m`: Sendet eine E-Mail-Benachrichtigung, wenn der Job abgeschlossen ist.

Die Zeit kann in verschiedenen Formaten angegeben werden, z. B. `now + 1 hour`, `tomorrow`, oder ein spezifisches Datum und Uhrzeit wie `2023-10-15 14:00`.

## Beispiele
### Beispiel 1: Einfache Aufgabe planen
Um einen einfachen Befehl zu einem bestimmten Zeitpunkt auszuführen, können Sie Folgendes tun:

```bash
echo "echo 'Hallo, Welt!'" | at now + 1 minute
```
Dieser Befehl plant, dass in einer Minute der Text "Hallo, Welt!" in die Konsole ausgegeben wird.

### Beispiel 2: Skript zu einem späteren Zeitpunkt ausführen
Um ein Skript zu einem bestimmten Zeitpunkt auszuführen, verwenden Sie die `-f` Option:

```bash
at 14:00 -f /path/to/script.sh
```
Dieser Befehl plant die Ausführung des Skripts `script.sh` um 14:00 Uhr.

## Tipps
- Stellen Sie sicher, dass der `atd`-Dienst (At Daemon) auf Ihrem System läuft, da `at` ohne diesen Dienst nicht funktionieren kann.
- Verwenden Sie die `-l` Option, um Ihre geplanten Aufträge zu überprüfen und sicherzustellen, dass sie korrekt eingeplant wurden.
- Nutzen Sie die `-m` Option, um Benachrichtigungen zu erhalten, wenn Ihre Aufgaben abgeschlossen sind, insbesondere bei längeren oder kritischen Jobs.
- Achten Sie darauf, dass die Zeitzone Ihres Systems korrekt eingestellt ist, um unerwartete Ausführungszeiten zu vermeiden.