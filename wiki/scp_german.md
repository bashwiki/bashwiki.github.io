# [Linux] Bash scp Verwendung: Dateien sicher kopieren

## Übersicht
Der `scp`-Befehl (Secure Copy Protocol) wird verwendet, um Dateien sicher zwischen einem lokalen und einem entfernten System oder zwischen zwei entfernten Systemen zu kopieren. Er nutzt SSH zur Datenübertragung und bietet somit eine sichere Verbindung.

## Verwendung
Die grundlegende Syntax des `scp`-Befehls lautet:

```bash
scp [Optionen] [Quell] [Ziel]
```

## Häufige Optionen
- `-r`: Kopiert Verzeichnisse rekursiv.
- `-P`: Gibt den Port an, der für die Verbindung verwendet werden soll (beachten Sie, dass es ein großes "P" ist).
- `-i`: Gibt den Pfad zur privaten Schlüsseldatei an, die für die Authentifizierung verwendet wird.
- `-v`: Aktiviert den ausführlichen Modus, um mehr Informationen über den Kopiervorgang anzuzeigen.

## Häufige Beispiele

1. **Eine Datei von lokal nach remote kopieren:**
   ```bash
   scp /pfad/zur/datei.txt benutzer@remote-server:/pfad/zum/ziel/
   ```

2. **Eine Datei von remote nach lokal kopieren:**
   ```bash
   scp benutzer@remote-server:/pfad/zur/datei.txt /pfad/zum/lokalen/ziel/
   ```

3. **Ein Verzeichnis rekursiv kopieren:**
   ```bash
   scp -r /pfad/zum/verzeichnis benutzer@remote-server:/pfad/zum/ziel/
   ```

4. **Eine Datei über einen bestimmten Port kopieren:**
   ```bash
   scp -P 2222 /pfad/zur/datei.txt benutzer@remote-server:/pfad/zum/ziel/
   ```

5. **Eine Datei mit einer spezifischen Schlüsseldatei kopieren:**
   ```bash
   scp -i /pfad/zur/schluesseldatei.pem /pfad/zur/datei.txt benutzer@remote-server:/pfad/zum/ziel/
   ```

## Tipps
- Stellen Sie sicher, dass der SSH-Dienst auf dem Remote-Server läuft, um Verbindungsprobleme zu vermeiden.
- Verwenden Sie den `-v`-Schalter, um bei Problemen detaillierte Fehlermeldungen zu erhalten.
- Überprüfen Sie die Berechtigungen der Dateien und Verzeichnisse, um sicherzustellen, dass Sie die erforderlichen Zugriffsrechte haben.
- Nutzen Sie `scp` für schnelle Übertragungen, aber für große Datenmengen oder langsame Verbindungen kann `rsync` eine bessere Wahl sein.