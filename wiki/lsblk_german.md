# [Linux] Bash lsblk Verwendung: Zeigt Informationen über Blockgeräte an

## Übersicht
Der Befehl `lsblk` wird verwendet, um Informationen über Blockgeräte im Linux-System anzuzeigen. Dazu gehören Festplatten, Partitionen und andere Speichermedien. Der Befehl zeigt eine hierarchische Ansicht der Geräte und deren Mount-Punkte.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
lsblk [Optionen] [Argumente]
```

## Häufige Optionen
- `-a`, `--all`: Zeigt alle Geräte an, einschließlich leerer Geräte.
- `-f`, `--fs`: Zeigt Dateisysteminformationen an.
- `-l`, `--list`: Listet die Geräte in einer flachen Liste auf.
- `-o`, `--output`: Bestimmt, welche Spalten angezeigt werden sollen.
- `-p`, `--paths`: Zeigt die vollständigen Pfade der Geräte an.
- `-t`, `--tree`: Zeigt die Geräte in einer baumartigen Struktur an.

## Häufige Beispiele

1. **Einfaches Auflisten von Blockgeräten:**
   ```bash
   lsblk
   ```

2. **Anzeigen aller Geräte, einschließlich leerer:**
   ```bash
   lsblk -a
   ```

3. **Anzeigen von Blockgeräten mit Dateisysteminformationen:**
   ```bash
   lsblk -f
   ```

4. **Ausgabe in einer flachen Liste:**
   ```bash
   lsblk -l
   ```

5. **Anzeigen spezifischer Spalten (z.B. NAME, SIZE, TYPE):**
   ```bash
   lsblk -o NAME,SIZE,TYPE
   ```

6. **Baumstruktur der Geräte anzeigen:**
   ```bash
   lsblk -t
   ```

## Tipps
- Verwenden Sie die Option `-f`, um schnell Informationen über das Dateisystem zu erhalten, was besonders nützlich ist, wenn Sie mehrere Partitionen verwalten.
- Kombinieren Sie `lsblk` mit anderen Befehlen wie `grep`, um gezielt nach bestimmten Geräten zu suchen.
- Nutzen Sie die Option `-p`, um die vollständigen Pfade der Geräte zu sehen, was hilfreich ist, wenn Sie Skripte schreiben oder Geräte identifizieren müssen.