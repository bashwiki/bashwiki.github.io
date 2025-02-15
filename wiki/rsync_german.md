# [리눅스] Bash rsync 사용법

## Übersicht

`rsync` ist ein leistungsstarkes Kommandozeilenwerkzeug in Linux und Unix-ähnlichen Betriebssystemen, das hauptsächlich zum Synchronisieren von Dateien und Verzeichnissen zwischen zwei Standorten verwendet wird. Es kann sowohl lokal als auch über ein Netzwerk verwendet werden. Der Hauptvorteil von `rsync` liegt in seiner Effizienz, da es nur die Änderungen an Dateien überträgt, anstatt die gesamten Dateien zu kopieren. Dies spart sowohl Bandbreite als auch Zeit.

## Verwendung

Die grundlegende Syntax des `rsync`-Befehls lautet:

```bash
rsync [OPTIONEN] QUELLE ZIEL
```

Hierbei sind die wichtigsten Optionen:

- `-a`: Aktiviert den Archivmodus, der rekursive Übertragungen und die Erhaltung von Symbolischen Links, Berechtigungen, Zeitstempeln und Gruppen-/Benutzereigentum ermöglicht.
- `-v`: Aktiviert den ausführlichen Modus, der detaillierte Informationen über den Übertragungsprozess anzeigt.
- `-z`: Komprimiert die Daten während der Übertragung, um die Bandbreite zu sparen.
- `-r`: Rekursive Übertragung von Verzeichnissen.
- `--delete`: Löscht Dateien im Zielverzeichnis, die nicht mehr im Quellverzeichnis vorhanden sind.

## Beispiele

### Beispiel 1: Lokale Synchronisation

Um ein Verzeichnis lokal zu synchronisieren, verwenden Sie den folgenden Befehl:

```bash
rsync -av /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
```

In diesem Beispiel werden alle Dateien und Unterverzeichnisse aus dem Quellverzeichnis in das Zielverzeichnis kopiert, wobei alle Attribute beibehalten werden.

### Beispiel 2: Synchronisation über SSH

Um Dateien von einem lokalen System auf einen Remote-Server zu übertragen, können Sie `rsync` über SSH verwenden:

```bash
rsync -avz /pfad/zum/quellverzeichnis/ benutzername@remote-server:/pfad/zum/zielverzeichnis/
```

Hierbei wird die Datenübertragung komprimiert, was besonders nützlich ist, wenn Sie große Datenmengen über das Internet übertragen.

## Tipps

- Verwenden Sie die Option `--dry-run` (oder `-n`), um eine Simulation des Befehls auszuführen, bevor Sie die tatsächliche Übertragung durchführen. Dies hilft, unerwartete Ergebnisse zu vermeiden.
  
  ```bash
  rsync -av --dry-run /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
  ```

- Achten Sie darauf, einen Schrägstrich (`/`) am Ende des Quellverzeichnisses zu verwenden, um sicherzustellen, dass nur der Inhalt und nicht das Verzeichnis selbst kopiert wird.
  
- Nutzen Sie `rsync` in Kombination mit Cron-Jobs, um regelmäßige Backups oder Synchronisationen zu automatisieren.

Mit diesen Informationen sind Sie gut gerüstet, um `rsync` effektiv zu nutzen und Ihre Dateiübertragungen zu optimieren.