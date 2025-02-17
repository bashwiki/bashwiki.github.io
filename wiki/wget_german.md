# [Linux] Bash wget Verwendung: Dateien herunterladen

## Übersicht
Der Befehl `wget` ist ein leistungsstarkes Tool zum Herunterladen von Dateien aus dem Internet. Es unterstützt verschiedene Protokolle wie HTTP, HTTPS und FTP und ermöglicht das Herunterladen von einzelnen Dateien oder ganzen Webseiten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
wget [Optionen] [Argumente]
```

## Häufige Optionen
- `-O [Dateiname]`: Speichert die heruntergeladene Datei unter dem angegebenen Namen.
- `-c`: Setzt einen abgebrochenen Download fort.
- `-r`: Aktiviert den rekursiven Download, um ganze Webseiten herunterzuladen.
- `-p`: Lädt alle notwendigen Dateien herunter, um eine Webseite korrekt anzuzeigen (z. B. Bilder, CSS).
- `--limit-rate=[Rate]`: Begrenzt die Downloadgeschwindigkeit auf die angegebene Rate.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `wget`:

1. **Einzelne Datei herunterladen:**
   ```bash
   wget https://example.com/datei.zip
   ```

2. **Datei unter einem bestimmten Namen speichern:**
   ```bash
   wget -O mein_download.zip https://example.com/datei.zip
   ```

3. **Abgebrochenen Download fortsetzen:**
   ```bash
   wget -c https://example.com/datei.zip
   ```

4. **Rekursiven Download einer Webseite:**
   ```bash
   wget -r https://example.com
   ```

5. **Download mit begrenzter Geschwindigkeit:**
   ```bash
   wget --limit-rate=200k https://example.com/datei.zip
   ```

## Tipps
- Verwenden Sie die Option `-q`, um den Download im "stillen" Modus durchzuführen, ohne Ausgaben im Terminal anzuzeigen.
- Kombinieren Sie `-r` mit `-np` (no parent), um nur die Dateien der aktuellen Webseite herunterzuladen und nicht die übergeordneten Verzeichnisse.
- Überprüfen Sie die heruntergeladenen Dateien regelmäßig, um sicherzustellen, dass sie vollständig und nicht beschädigt sind.