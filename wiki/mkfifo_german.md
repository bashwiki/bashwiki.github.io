# [Linux] Bash mkfifo Verwendung: Erstellen von benannten Pipes

## Übersicht
Der Befehl `mkfifo` wird verwendet, um benannte Pipes (FIFO - First In First Out) in Linux zu erstellen. Diese speziellen Dateien ermöglichen die Kommunikation zwischen verschiedenen Prozessen, indem sie Daten in einer sequenziellen Reihenfolge übertragen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
mkfifo [Optionen] [Argumente]
```

## Häufige Optionen
- `-m, --mode=MODE`: Setzt die Berechtigungen für die erstellte Pipe. `MODE` kann in oktaler Form angegeben werden, z.B. `0666`.
- `--help`: Zeigt eine Hilfemeldung mit einer Übersicht über die Optionen an.
- `--version`: Gibt die Versionsnummer des Befehls aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `mkfifo`:

### Beispiel 1: Erstellen einer einfachen benannten Pipe
```bash
mkfifo meine_pipe
```
Dieses Kommando erstellt eine benannte Pipe mit dem Namen `meine_pipe`.

### Beispiel 2: Erstellen einer benannten Pipe mit spezifischen Berechtigungen
```bash
mkfifo -m 0644 meine_pipe
```
Hier wird eine benannte Pipe mit den Berechtigungen `0644` erstellt, was bedeutet, dass der Besitzer lesen und schreiben kann, während andere nur lesen können.

### Beispiel 3: Verwendung der Pipe zur Kommunikation zwischen Prozessen
In einem Terminal:
```bash
cat < meine_pipe
```
In einem anderen Terminal:
```bash
echo "Hallo, Welt!" > meine_pipe
```
Das erste Terminal wartet auf Eingaben aus der Pipe, während das zweite Terminal die Nachricht "Hallo, Welt!" in die Pipe schreibt.

## Tipps
- Stellen Sie sicher, dass Sie die Pipe löschen, wenn Sie sie nicht mehr benötigen, um Speicherplatz zu sparen. Verwenden Sie dazu `rm meine_pipe`.
- Nutzen Sie `mkfifo` in Skripten, um einfache Interprozesskommunikation zu ermöglichen.
- Testen Sie die Berechtigungen der Pipe, um sicherzustellen, dass die richtigen Prozesse darauf zugreifen können.