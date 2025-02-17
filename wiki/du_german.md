# [Linux] Bash du Verwendung: Speicherplatznutzung anzeigen

## Übersicht
Der `du` (Disk Usage) Befehl wird verwendet, um die Speichernutzung von Dateien und Verzeichnissen anzuzeigen. Er gibt an, wie viel Speicherplatz von Dateien und Verzeichnissen auf der Festplatte belegt wird.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
du [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`: Gibt die Größe in menschenlesbarem Format aus (z.B. KB, MB).
- `-s`: Zeigt nur die Gesamtsumme der angegebenen Verzeichnisse an.
- `-a`: Listet die Größe aller Dateien und Verzeichnisse auf, nicht nur der Verzeichnisse.
- `-c`: Gibt eine Gesamtsumme für alle angegebenen Argumente aus.

## Häufige Beispiele
1. **Speicherplatz für das aktuelle Verzeichnis anzeigen**:
   ```bash
   du -h
   ```

2. **Gesamtspeicherplatz eines bestimmten Verzeichnisses anzeigen**:
   ```bash
   du -sh /pfad/zum/verzeichnis
   ```

3. **Speicherplatz für alle Dateien und Verzeichnisse im aktuellen Verzeichnis auflisten**:
   ```bash
   du -ah
   ```

4. **Gesamtspeicherplatz mehrerer Verzeichnisse anzeigen**:
   ```bash
   du -ch /pfad/zum/verzeichnis1 /pfad/zum/verzeichnis2
   ```

## Tipps
- Verwenden Sie die `-h` Option, um die Ausgabe leichter lesbar zu machen.
- Kombinieren Sie `-s` mit spezifischen Verzeichnissen, um schnell die Gesamtnutzung zu überprüfen.
- Nutzen Sie `-a`, wenn Sie auch die Größen einzelner Dateien benötigen, nicht nur die der Verzeichnisse.