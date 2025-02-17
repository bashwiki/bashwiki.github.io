# [Linux] Bash find Verwendung: Dateinamen finden

## Übersicht
Der Befehl `find` wird in Bash verwendet, um Dateien und Verzeichnisse im Dateisystem zu suchen. Er ermöglicht es Benutzern, gezielt nach Dateien zu suchen, die bestimmten Kriterien entsprechen, wie z.B. Name, Typ, Größe oder Änderungsdatum.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
find [Optionen] [Argumente]
```

## Häufige Optionen
- `-name`: Sucht nach Dateien mit einem bestimmten Namen.
- `-type`: Filtert nach Dateitypen (z.B. `f` für reguläre Dateien, `d` für Verzeichnisse).
- `-size`: Sucht nach Dateien, die eine bestimmte Größe haben.
- `-mtime`: Sucht nach Dateien, die in den letzten n Tagen geändert wurden.
- `-exec`: Führt einen Befehl für jede gefundene Datei aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `find`:

1. **Nach einer Datei mit einem bestimmten Namen suchen:**
   ```bash
   find /pfad/zum/verzeichnis -name "dateiname.txt"
   ```

2. **Nach allen Verzeichnissen suchen:**
   ```bash
   find /pfad/zum/verzeichnis -type d
   ```

3. **Nach Dateien mit einer bestimmten Größe suchen (z.B. größer als 1MB):**
   ```bash
   find /pfad/zum/verzeichnis -size +1M
   ```

4. **Nach Dateien suchen, die in den letzten 7 Tagen geändert wurden:**
   ```bash
   find /pfad/zum/verzeichnis -mtime -7
   ```

5. **Eine Aktion für jede gefundene Datei ausführen (z.B. löschen):**
   ```bash
   find /pfad/zum/verzeichnis -name "*.tmp" -exec rm {} \;
   ```

## Tipps
- Verwenden Sie `-iname` anstelle von `-name`, um die Suche nicht case-sensitiv zu gestalten.
- Kombinieren Sie Optionen, um präzisere Suchen durchzuführen, z.B. `find /pfad -type f -size +500k -mtime -30`.
- Nutzen Sie `-print` am Ende des Befehls, um die gefundenen Dateien anzuzeigen, wenn Sie `-exec` nicht verwenden.