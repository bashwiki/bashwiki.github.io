# [Linux] Bash rsync Verwendung: Dateien synchronisieren und übertragen

## Übersicht
Der `rsync`-Befehl ist ein leistungsstarkes Tool zur Dateiübertragung und -synchronisation. Es ermöglicht Benutzern, Dateien und Verzeichnisse zwischen verschiedenen Orten zu kopieren, während nur die Änderungen übertragen werden, was die Effizienz erhöht.

## Verwendung
Die grundlegende Syntax des `rsync`-Befehls lautet:

```bash
rsync [Optionen] [Quell] [Ziel]
```

## Häufige Optionen
- `-a`: Archivmodus; kopiert Dateien rekursiv und bewahrt die Dateiberechtigungen.
- `-v`: Verbose; zeigt detaillierte Informationen über den Kopiervorgang an.
- `-z`: Komprimierung; komprimiert die Daten während der Übertragung.
- `-r`: Rekursiv; kopiert Verzeichnisse und deren Inhalte.
- `--delete`: Löscht Dateien im Zielverzeichnis, die nicht mehr im Quellverzeichnis vorhanden sind.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `rsync`:

1. **Ein einfaches Kopieren von Dateien:**
   ```bash
   rsync -av /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
   ```

2. **Kopieren von Dateien über SSH:**
   ```bash
   rsync -avz -e ssh /lokaler/pfad/ benutzer@remote:/remote/pfad/
   ```

3. **Synchronisieren und Löschen nicht mehr vorhandener Dateien:**
   ```bash
   rsync -av --delete /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
   ```

4. **Kopieren von Dateien mit Fortschrittsanzeige:**
   ```bash
   rsync -av --progress /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
   ```

## Tipps
- Verwenden Sie den `--dry-run`-Schalter, um zu sehen, welche Änderungen vorgenommen werden, ohne tatsächlich zu kopieren:
  ```bash
  rsync -av --dry-run /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
  ```
- Achten Sie darauf, einen Schrägstrich (`/`) am Ende des Quellverzeichnisses zu verwenden, um nur den Inhalt zu kopieren und nicht das Verzeichnis selbst.
- Nutzen Sie `rsync` regelmäßig für Backups, um sicherzustellen, dass Ihre Daten immer aktuell sind.