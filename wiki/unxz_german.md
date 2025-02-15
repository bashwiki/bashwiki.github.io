# [리눅스] Bash unxz 사용법

## Übersicht
Der Befehl `unxz` wird in der Bash verwendet, um Dateien zu dekomprimieren, die im XZ-Format komprimiert sind. XZ ist ein weit verbreitetes Komprimierungsformat, das eine hohe Komprimierungsrate bietet. Der Hauptzweck von `unxz` besteht darin, komprimierte Dateien zu entpacken und in ihr ursprüngliches Format zurückzuführen.

## Verwendung
Die grundlegende Syntax des Befehls `unxz` lautet:

```bash
unxz [Optionen] [Datei]
```

### Häufige Optionen:
- `-k`, `--keep`: Behalte die komprimierte Datei nach dem Dekomprimieren.
- `-f`, `--force`: Überschreibe die Ausgabedatei, wenn sie bereits existiert.
- `-v`, `--verbose`: Zeige detaillierte Informationen über den Dekomprimierungsprozess an.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `unxz`:

1. **Dekomprimieren einer Datei**:
   Um eine Datei namens `beispiel.xz` zu dekomprimieren, verwenden Sie den folgenden Befehl:

   ```bash
   unxz beispiel.xz
   ```

   Nach der Ausführung dieses Befehls wird die Datei `beispiel.xz` entfernt und die dekomprimierte Datei `beispiel` wird im aktuellen Verzeichnis erstellt.

2. **Dekomprimieren und Behalten der Originaldatei**:
   Wenn Sie die komprimierte Datei nach dem Dekomprimieren behalten möchten, können Sie die `-k` Option verwenden:

   ```bash
   unxz -k beispiel.xz
   ```

   In diesem Fall bleibt die Datei `beispiel.xz` erhalten, und die dekomprimierte Datei `beispiel` wird ebenfalls erstellt.

## Tipps
- Verwenden Sie die `-v` Option, um den Fortschritt der Dekomprimierung zu überwachen, besonders bei großen Dateien.
- Achten Sie darauf, dass Sie genügend Speicherplatz auf Ihrem Laufwerk haben, um die dekomprimierte Datei zu speichern, da sie in der Regel größer ist als die komprimierte Version.
- Wenn Sie mehrere Dateien gleichzeitig dekomprimieren möchten, können Sie Wildcards verwenden, z.B. `unxz *.xz`, um alle XZ-Dateien im aktuellen Verzeichnis zu dekomprimieren.