# [리눅스] Bash mkfifo 사용법

## Übersicht
Der Befehl `mkfifo` wird in Unix-ähnlichen Betriebssystemen verwendet, um benannte Pipes (FIFO - First In, First Out) zu erstellen. Eine benannte Pipe ist ein spezieller Typ von Datei, der es Prozessen ermöglicht, Daten miteinander zu kommunizieren. Im Gegensatz zu normalen Dateien, die Daten speichern, ermöglichen benannte Pipes eine direkte Kommunikation zwischen Prozessen, indem sie Daten in der Reihenfolge, in der sie gesendet werden, empfangen und weitergeben.

## Verwendung
Die grundlegende Syntax des Befehls `mkfifo` lautet:

```bash
mkfifo [OPTIONEN] NAME
```

### Häufige Optionen
- `-m, --mode=MODE`: Setzt die Berechtigungen der erstellten FIFO-Datei. Der Modus kann in oktaler Form angegeben werden (z.B. `0666`).
- `--help`: Zeigt eine Hilfe-Seite mit Informationen zur Verwendung des Befehls an.
- `--version`: Gibt die Versionsnummer des Befehls aus.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `mkfifo`:

### Beispiel 1: Erstellen einer einfachen benannten Pipe
Um eine benannte Pipe mit dem Namen `meine_pipe` zu erstellen, verwenden Sie den folgenden Befehl:

```bash
mkfifo meine_pipe
```

### Beispiel 2: Erstellen einer benannten Pipe mit spezifischen Berechtigungen
Um eine benannte Pipe mit benutzerdefinierten Berechtigungen zu erstellen, verwenden Sie die `-m` Option. Zum Beispiel:

```bash
mkfifo -m 0666 meine_pipe
```

In diesem Beispiel wird die benannte Pipe `meine_pipe` mit Lese- und Schreibberechtigungen für alle Benutzer erstellt.

## Tipps
- Stellen Sie sicher, dass die benannte Pipe vor der Verwendung von Prozessen erstellt wird, die darauf zugreifen möchten. Andernfalls kann es zu Fehlern kommen.
- Verwenden Sie `ls -l`, um die Berechtigungen der erstellten FIFO-Datei zu überprüfen.
- Denken Sie daran, dass Daten, die in eine benannte Pipe geschrieben werden, von einem anderen Prozess gelesen werden müssen, da sie nicht gespeichert werden. Wenn kein Prozess zum Lesen bereit ist, blockiert der schreibende Prozess.
- Benannte Pipes sind nützlich für die Interprozesskommunikation in Skripten und Anwendungen, die Daten in Echtzeit austauschen müssen.