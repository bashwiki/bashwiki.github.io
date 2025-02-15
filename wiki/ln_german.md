# [리눅스] Bash ln 사용법

## Übersicht
Der Befehl `ln` in Bash wird verwendet, um Links zu Dateien zu erstellen. Es gibt zwei Hauptarten von Links: harte Links und symbolische Links (symlinks). Harte Links verweisen direkt auf die Inode einer Datei, während symbolische Links einen Verweis auf den Pfad einer Datei erstellen. Der Hauptzweck des `ln`-Befehls besteht darin, mehrere Verweise auf dieselbe Datei zu erstellen, was die Dateiverwaltung und den Zugriff erleichtert.

## Verwendung
Die grundlegende Syntax des `ln`-Befehls lautet:

```bash
ln [OPTIONEN] QUELLE [ZIEL]
```

### Häufige Optionen:
- `-s`: Erstellt einen symbolischen Link anstelle eines harten Links.
- `-f`: Erzwingt das Erstellen des Links, indem vorhandene Dateien ohne Rückfrage überschrieben werden.
- `-n`: Verhindert das Dereferenzieren von symbolischen Links, wenn das Ziel bereits existiert.
- `-v`: Gibt detaillierte Informationen über die durchgeführten Aktionen aus (verbose).

## Beispiele
### Beispiel 1: Erstellen eines harten Links
Um einen harten Link zu einer Datei namens `datei.txt` zu erstellen, verwenden Sie den folgenden Befehl:

```bash
ln datei.txt link_zu_datei.txt
```

### Beispiel 2: Erstellen eines symbolischen Links
Um einen symbolischen Link zu einer Datei namens `datei.txt` zu erstellen, verwenden Sie den `-s`-Schalter:

```bash
ln -s datei.txt symlink_zu_datei.txt
```

## Tipps
- Verwenden Sie symbolische Links, wenn Sie auf Dateien in verschiedenen Verzeichnissen verweisen möchten, da harte Links nur innerhalb desselben Dateisystems funktionieren.
- Überprüfen Sie mit dem Befehl `ls -l`, ob Ihre Links korrekt erstellt wurden. Symbolische Links werden mit einem `->` angezeigt, das auf das Ziel verweist.
- Seien Sie vorsichtig beim Verwenden der `-f`-Option, da dies vorhandene Dateien ohne Warnung überschreibt.