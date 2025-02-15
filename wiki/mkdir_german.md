# [리눅스] Bash mkdir 사용법

## Übersicht
Der Befehl `mkdir` (make directory) wird in Bash verwendet, um neue Verzeichnisse (Ordner) im Dateisystem zu erstellen. Dies ist eine grundlegende Funktion in der Dateiverwaltung, die es Entwicklern und Ingenieuren ermöglicht, ihre Projekte und Dateien strukturiert zu organisieren.

## Verwendung
Die grundlegende Syntax des `mkdir`-Befehls lautet:

```bash
mkdir [OPTIONEN] VERZEICHNISNAME
```

### Häufige Optionen
- `-p`: Erstellt das Verzeichnis und alle übergeordneten Verzeichnisse, die möglicherweise nicht existieren.
- `-v`: Gibt eine detaillierte Ausgabe, die anzeigt, welche Verzeichnisse erstellt wurden.
- `-m`: Setzt die Berechtigungen für das neu erstellte Verzeichnis, z.B. `-m 755`.

## Beispiele
### Beispiel 1: Einfaches Verzeichnis erstellen
Um ein einfaches Verzeichnis namens `projekt` zu erstellen, verwenden Sie den folgenden Befehl:

```bash
mkdir projekt
```

### Beispiel 2: Verzeichnis mit übergeordneten Verzeichnissen erstellen
Um ein Verzeichnis `2023/projekt` zu erstellen, auch wenn das Verzeichnis `2023` noch nicht existiert, verwenden Sie die `-p`-Option:

```bash
mkdir -p 2023/projekt
```

## Tipps
- Verwenden Sie die `-v`-Option, um eine Bestätigung zu erhalten, dass das Verzeichnis erfolgreich erstellt wurde. Dies kann besonders nützlich sein, wenn Sie mehrere Verzeichnisse auf einmal erstellen.
- Achten Sie darauf, dass Sie die richtigen Berechtigungen für Ihre Verzeichnisse festlegen, insbesondere wenn Sie mit sensiblen Daten arbeiten. Nutzen Sie die `-m`-Option, um die Berechtigungen direkt beim Erstellen festzulegen.
- Überprüfen Sie immer, ob das Verzeichnis bereits existiert, um Fehler zu vermeiden. Sie können dies mit dem Befehl `ls` tun, bevor Sie `mkdir` verwenden.