# [리눅스] Bash xz 사용법

## Übersicht
Der Befehl `xz` ist ein Komprimierungstool, das das LZMA-Algorithmus verwendet, um Dateien zu komprimieren. Es bietet eine hohe Kompressionsrate und ist besonders nützlich für die Reduzierung der Dateigröße von großen Datenmengen. `xz` wird häufig in der Softwareverteilung und für die Archivierung von Daten eingesetzt.

## Verwendung
Die grundlegende Syntax des `xz`-Befehls lautet:

```bash
xz [OPTIONEN] [DATEI...]
```

### Häufige Optionen:
- `-d`, `--decompress`: Dekomprimiert eine komprimierte Datei.
- `-k`, `--keep`: Behalte die Originaldatei nach der Komprimierung oder Dekomprimierung.
- `-f`, `--force`: Überschreibe vorhandene Dateien ohne Nachfrage.
- `-9`: Setzt die Kompressionsstufe auf maximal (1-9, wobei 9 die höchste Kompression bietet).
- `-z`: Komprimiert die Datei (Standardverhalten).

## Beispiele
### Beispiel 1: Komprimieren einer Datei
Um eine Datei namens `beispiel.txt` zu komprimieren, verwenden Sie den folgenden Befehl:

```bash
xz beispiel.txt
```

Dies erstellt eine komprimierte Datei namens `beispiel.txt.xz` und entfernt die ursprüngliche Datei.

### Beispiel 2: Dekomprimieren einer Datei
Um eine komprimierte Datei `beispiel.txt.xz` zu dekomprimieren, verwenden Sie:

```bash
xz -d beispiel.txt.xz
```

Dies stellt die ursprüngliche Datei `beispiel.txt` wieder her.

## Tipps
- Verwenden Sie die Option `-k`, wenn Sie die Originaldatei behalten möchten, während Sie die komprimierte Version erstellen.
- Experimentieren Sie mit verschiedenen Kompressionsstufen (z.B. `-1` bis `-9`), um ein Gleichgewicht zwischen Kompressionsrate und Verarbeitungszeit zu finden.
- Für die Verarbeitung mehrerer Dateien können Sie Platzhalter verwenden, z.B. `xz *.txt`, um alle `.txt`-Dateien im aktuellen Verzeichnis zu komprimieren.