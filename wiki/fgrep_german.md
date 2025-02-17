# [Linux] Bash fgrep Verwendung: Sucht nach festen Zeichenfolgen in Dateien

## Übersicht
Der Befehl `fgrep` ist ein Tool in der Bash, das verwendet wird, um nach festen Zeichenfolgen in Dateien zu suchen. Im Gegensatz zu `grep` interpretiert `fgrep` keine regulären Ausdrücke, sondern sucht nach exakten Übereinstimmungen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
fgrep [Optionen] [Argumente]
```

## Häufige Optionen
- `-i`: Ignoriere Groß- und Kleinschreibung bei der Suche.
- `-v`: Zeige nur die Zeilen an, die **nicht** mit der angegebenen Zeichenfolge übereinstimmen.
- `-c`: Zähle die Anzahl der Übereinstimmungen und gib diese aus.
- `-n`: Zeige die Zeilennummern der Übereinstimmungen an.
- `-r`: Durchsuche Verzeichnisse rekursiv.

## Häufige Beispiele

1. **Einfaches Suchen nach einer Zeichenfolge in einer Datei:**
   ```bash
   fgrep "Suchbegriff" datei.txt
   ```

2. **Suchen ohne Berücksichtigung der Groß- und Kleinschreibung:**
   ```bash
   fgrep -i "suchbegriff" datei.txt
   ```

3. **Zählen der Übereinstimmungen:**
   ```bash
   fgrep -c "Suchbegriff" datei.txt
   ```

4. **Zeilen ausgeben, die nicht mit der Zeichenfolge übereinstimmen:**
   ```bash
   fgrep -v "Suchbegriff" datei.txt
   ```

5. **Rekursive Suche in einem Verzeichnis:**
   ```bash
   fgrep -r "Suchbegriff" /pfad/zum/verzeichnis
   ```

## Tipps
- Verwenden Sie `fgrep`, wenn Sie sicher sind, dass Sie nach einer exakten Zeichenfolge suchen möchten, um die Leistung zu verbessern.
- Kombinieren Sie Optionen, um spezifischere Suchergebnisse zu erhalten, z. B. `fgrep -n -i "Suchbegriff" datei.txt`.
- Nutzen Sie die Möglichkeit der rekursiven Suche, um in mehreren Dateien oder Verzeichnissen effizient nach Inhalten zu suchen.