# [Linux] Bash df Verwendung: Zeigt den verfügbaren Speicherplatz auf Dateisystemen an

## Übersicht
Der Befehl `df` (disk free) wird verwendet, um Informationen über den verfügbaren und verwendeten Speicherplatz auf Dateisystemen anzuzeigen. Er gibt eine Übersicht über die Speicherkapazität und die Nutzung der verschiedenen Dateisysteme auf einem Linux- oder Unix-basierten System.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
df [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`: Gibt die Größen in menschenlesbarem Format aus (z. B. KB, MB, GB).
- `-T`: Zeigt den Typ des Dateisystems an.
- `-a`: Zeigt auch die Dateisysteme an, die 0 Blöcke haben.
- `-i`: Zeigt die Anzahl der inodes anstelle der Blocknutzung an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `df`-Befehls:

1. **Einfacher Befehl ohne Optionen:**
   ```bash
   df
   ```

2. **Menschenlesbare Ausgabe:**
   ```bash
   df -h
   ```

3. **Anzeige des Dateisystemtyps:**
   ```bash
   df -T
   ```

4. **Anzeige aller Dateisysteme, einschließlich leerer:**
   ```bash
   df -a
   ```

5. **Anzeige der inodes:**
   ```bash
   df -i
   ```

## Tipps
- Verwenden Sie die `-h`-Option, um die Ausgabe leichter lesbar zu machen, insbesondere wenn Sie mit großen Speichermengen arbeiten.
- Kombinieren Sie Optionen, um spezifischere Informationen zu erhalten, z. B. `df -hT`, um sowohl die Größe als auch den Typ des Dateisystems anzuzeigen.
- Überprüfen Sie regelmäßig den Speicherplatz, um sicherzustellen, dass Ihr System nicht überlastet wird, was zu Leistungseinbußen führen kann.