# [Linux] Bash sed Verwendung: Textverarbeitung und -manipulation

## Übersicht
Der `sed`-Befehl, kurz für "stream editor", ist ein leistungsfähiges Tool in der Bash, das zur Bearbeitung und Manipulation von Textströmen verwendet wird. Er ermöglicht es Benutzern, Textdateien zu durchsuchen, zu ersetzen, zu löschen und zu formatieren, ohne die Originaldatei direkt zu verändern.

## Verwendung
Die grundlegende Syntax des `sed`-Befehls lautet:

```bash
sed [Optionen] [Argumente]
```

## Häufige Optionen
- `-e`: Ermöglicht die Angabe mehrerer Bearbeitungsanweisungen.
- `-i`: Führt die Bearbeitung direkt in der Datei durch (in-place).
- `-n`: Unterdrückt die Standardausgabe, nur explizit angegebene Ausgaben werden angezeigt.
- `s`: Steht für "substitute" und wird verwendet, um Text zu ersetzen.

## Häufige Beispiele

### 1. Text ersetzen
Um in einer Datei "alt" durch "neu" zu ersetzen, verwenden Sie:

```bash
sed 's/alt/neu/g' datei.txt
```

### 2. In-place Bearbeitung
Um "alt" durch "neu" in der Datei direkt zu ersetzen, verwenden Sie:

```bash
sed -i 's/alt/neu/g' datei.txt
```

### 3. Zeilen löschen
Um alle Zeilen, die "entfernen" enthalten, aus einer Datei zu löschen:

```bash
sed '/entfernen/d' datei.txt
```

### 4. Nur bestimmte Zeilen anzeigen
Um nur die Zeilen 2 bis 4 einer Datei anzuzeigen:

```bash
sed -n '2,4p' datei.txt
```

### 5. Mehrere Ersetzungen
Um mehrere Ersetzungen in einer Datei durchzuführen:

```bash
sed -e 's/alt1/neu1/g' -e 's/alt2/neu2/g' datei.txt
```

## Tipps
- Testen Sie Ihre `sed`-Befehle zuerst ohne die `-i`-Option, um sicherzustellen, dass die Ergebnisse wie gewünscht sind.
- Verwenden Sie reguläre Ausdrücke für komplexere Suchmuster.
- Nutzen Sie die `-n`-Option, um die Ausgabe zu kontrollieren und nur die gewünschten Zeilen anzuzeigen.