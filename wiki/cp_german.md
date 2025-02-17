# [Linux] Bash cp Verwendung: Dateien und Verzeichnisse kopieren

## Übersicht
Der `cp`-Befehl wird in Bash verwendet, um Dateien und Verzeichnisse von einem Ort zu einem anderen zu kopieren. Er ist ein grundlegendes Werkzeug für die Dateiverwaltung in Unix-ähnlichen Betriebssystemen.

## Verwendung
Die grundlegende Syntax des `cp`-Befehls lautet:

```bash
cp [Optionen] [Quell] [Ziel]
```

## Häufige Optionen
- `-r`: Kopiert Verzeichnisse rekursiv.
- `-i`: Fragt vor dem Überschreiben von Dateien nach.
- `-u`: Kopiert nur, wenn die Quell-Datei neuer ist als die Ziel-Datei oder wenn die Ziel-Datei nicht existiert.
- `-v`: Zeigt die Dateien an, die kopiert werden, während der Befehl ausgeführt wird.

## Häufige Beispiele

1. **Kopieren einer Datei:**
   ```bash
   cp datei.txt kopie_datei.txt
   ```

2. **Kopieren eines Verzeichnisses rekursiv:**
   ```bash
   cp -r verzeichnis1/ verzeichnis2/
   ```

3. **Kopieren mit Bestätigung vor dem Überschreiben:**
   ```bash
   cp -i datei.txt kopie_datei.txt
   ```

4. **Kopieren nur neuerer Dateien:**
   ```bash
   cp -u datei.txt zielverzeichnis/
   ```

5. **Kopieren mit detaillierter Ausgabe:**
   ```bash
   cp -v datei.txt kopie_datei.txt
   ```

## Tipps
- Verwenden Sie die `-i`-Option, um versehentliches Überschreiben von Dateien zu vermeiden.
- Bei der Arbeit mit Verzeichnissen ist die `-r`-Option unerlässlich, um sicherzustellen, dass alle Unterverzeichnisse und Dateien kopiert werden.
- Nutzen Sie die `-v`-Option, um den Fortschritt beim Kopieren zu überwachen, besonders bei großen Datenmengen.