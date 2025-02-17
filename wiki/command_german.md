# [Linux] Bash-Befehl cp: Dateien und Verzeichnisse kopieren

## Übersicht
Der Befehl `cp` wird verwendet, um Dateien und Verzeichnisse in Linux zu kopieren. Er ermöglicht es Benutzern, eine oder mehrere Quelldateien an einen Zielort zu kopieren, wobei verschiedene Optionen zur Verfügung stehen, um das Verhalten des Kopiervorgangs anzupassen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
cp [Optionen] [Quell-Datei(en)] [Ziel]
```

## Häufige Optionen
- `-r`: Kopiert Verzeichnisse rekursiv.
- `-i`: Fragt vor dem Überschreiben von Dateien nach.
- `-u`: Kopiert nur, wenn die Quell-Datei neuer ist als die Ziel-Datei oder wenn die Ziel-Datei nicht existiert.
- `-v`: Gibt detaillierte Informationen über den Kopiervorgang aus (verbose).
- `-a`: Archivmodus; kopiert Dateien und Verzeichnisse rekursiv und bewahrt alle Attribute.

## Häufige Beispiele
1. **Eine Datei kopieren:**
   ```bash
   cp datei.txt kopie_datei.txt
   ```

2. **Ein Verzeichnis rekursiv kopieren:**
   ```bash
   cp -r mein_verzeichnis/ kopie_verzeichnis/
   ```

3. **Datei mit Bestätigung vor dem Überschreiben kopieren:**
   ```bash
   cp -i datei.txt kopie_datei.txt
   ```

4. **Nur neuere Dateien kopieren:**
   ```bash
   cp -u datei.txt ziel_verzeichnis/
   ```

5. **Detaillierte Ausgabe beim Kopieren aktivieren:**
   ```bash
   cp -v datei.txt kopie_datei.txt
   ```

## Tipps
- Verwenden Sie die Option `-i`, um versehentliches Überschreiben wichtiger Dateien zu vermeiden.
- Nutzen Sie den Archivmodus `-a`, wenn Sie komplette Verzeichnisse mit ihren Attributen und Berechtigungen kopieren möchten.
- Überprüfen Sie die Zielverzeichnisse vor dem Kopieren, um sicherzustellen, dass Sie die Dateien am richtigen Ort ablegen.