# [리눅스] Bash wget 사용법

## Übersicht
Der Befehl `wget` ist ein leistungsstarkes Kommandozeilen-Tool, das zum Herunterladen von Dateien aus dem Internet verwendet wird. Es unterstützt verschiedene Protokolle wie HTTP, HTTPS und FTP. `wget` ist besonders nützlich für das Herunterladen von Inhalten von Webseiten, das Abrufen von Dateien in Skripten und das Erstellen von Backups von Webinhalten.

## Verwendung
Die grundlegende Syntax des `wget`-Befehls lautet:

```bash
wget [Optionen] [URL]
```

### Häufige Optionen:
- `-O [Dateiname]`: Speichert die heruntergeladene Datei unter dem angegebenen Namen.
- `-c`: Setzt einen abgebrochenen Download fort.
- `-r`: Aktiviert den rekursiven Download, um alle verlinkten Seiten und Dateien herunterzuladen.
- `-p`: Lädt alle notwendigen Dateien (z.B. Bilder, CSS) herunter, um eine Webseite lokal anzuzeigen.
- `--limit-rate=[Rate]`: Begrenzung der Downloadgeschwindigkeit, um Bandbreite zu sparen.

## Beispiele
### Beispiel 1: Einfaches Herunterladen einer Datei
Um eine Datei von einer URL herunterzuladen, verwenden Sie den folgenden Befehl:

```bash
wget https://example.com/datei.zip
```

### Beispiel 2: Fortsetzen eines abgebrochenen Downloads
Wenn ein Download unterbrochen wurde, können Sie ihn mit der `-c`-Option fortsetzen:

```bash
wget -c https://example.com/datei.zip
```

## Tipps
- Verwenden Sie die `-q`-Option für einen stillen Modus, um die Ausgabe zu minimieren, wenn Sie Skripte automatisieren.
- Nutzen Sie die `-r`-Option mit Bedacht, da rekursive Downloads große Datenmengen erzeugen können.
- Überprüfen Sie die `--limit-rate`-Option, um sicherzustellen, dass Ihre Downloads die Netzwerkbandbreite nicht überlasten.
- Stellen Sie sicher, dass Sie die Erlaubnis haben, Inhalte von Webseiten herunterzuladen, um rechtliche Probleme zu vermeiden.