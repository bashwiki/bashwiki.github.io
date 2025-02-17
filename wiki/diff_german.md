# [Linux] Bash diff Verwendung: Vergleiche Dateien und Verzeichnisse

## Übersicht
Der `diff`-Befehl wird verwendet, um Unterschiede zwischen zwei Dateien oder Verzeichnissen zu vergleichen. Er zeigt an, welche Zeilen in einer Datei hinzugefügt, entfernt oder geändert wurden, was besonders nützlich ist, um Änderungen in Quellcode-Dateien oder Textdokumenten nachzuvollziehen.

## Verwendung
Die grundlegende Syntax des `diff`-Befehls lautet:

```bash
diff [Optionen] [Argumente]
```

## Häufige Optionen
- `-u`: Zeigt die Unterschiede im unified Format an, das kontextbezogene Informationen bietet.
- `-c`: Gibt die Unterschiede im kontextuellen Format aus, das mehr Kontext um die Änderungen herum zeigt.
- `-i`: Ignoriert Groß- und Kleinschreibung bei der Vergleichung.
- `-w`: Ignoriert Leerzeichen und Tabulatoren bei der Vergleichung.
- `-r`: Vergleicht rekursiv alle Dateien in zwei Verzeichnissen.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `diff`:

1. **Einfacher Vergleich zweier Dateien:**
   ```bash
   diff datei1.txt datei2.txt
   ```

2. **Vergleich im unified Format:**
   ```bash
   diff -u datei1.txt datei2.txt
   ```

3. **Vergleich von zwei Verzeichnissen:**
   ```bash
   diff -r verzeichnis1/ verzeichnis2/
   ```

4. **Ignorieren von Leerzeichen:**
   ```bash
   diff -w datei1.txt datei2.txt
   ```

5. **Vergleich mit kontextuellem Format:**
   ```bash
   diff -c datei1.txt datei2.txt
   ```

## Tipps
- Verwenden Sie die `-u`-Option, um die Ausgabe besser lesbar zu machen, insbesondere bei größeren Änderungen.
- Nutzen Sie `diff` in Kombination mit `patch`, um Änderungen an Dateien anzuwenden.
- Speichern Sie die Ausgabe von `diff` in einer Datei, um später darauf zurückzugreifen:
  ```bash
  diff datei1.txt datei2.txt > unterschiede.txt
  ```