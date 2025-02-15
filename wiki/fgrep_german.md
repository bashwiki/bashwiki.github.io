# [리눅스] Bash fgrep 사용법

## Übersicht
Der Befehl `fgrep` (fixed grep) ist ein Tool in der Bash, das verwendet wird, um nach festen Zeichenfolgen in Dateien zu suchen. Im Gegensatz zu `grep`, das reguläre Ausdrücke unterstützt, sucht `fgrep` nur nach genauen Übereinstimmungen. Dies macht `fgrep` besonders nützlich, wenn Sie nach speziellen Zeichenfolgen suchen, die möglicherweise reguläre Ausdrücke enthalten, da es diese nicht interpretiert.

## Verwendung
Die grundlegende Syntax des Befehls `fgrep` lautet:

```bash
fgrep [OPTIONEN] SUCHBEGRIFF [DATEIEN...]
```

### Häufig verwendete Optionen:
- `-i`: Ignoriere die Groß- und Kleinschreibung bei der Suche.
- `-v`: Invertiere die Suche, um Zeilen anzuzeigen, die **nicht** den Suchbegriff enthalten.
- `-c`: Zähle die Anzahl der Übereinstimmungen und gib diese aus.
- `-n`: Zeige die Zeilennummern der Übereinstimmungen an.
- `-r`: Durchsuche Verzeichnisse rekursiv.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `fgrep`:

1. **Einfaches Suchen in einer Datei**:
   Um nach der genauen Zeichenfolge "Fehler" in der Datei `log.txt` zu suchen, verwenden Sie den folgenden Befehl:
   ```bash
   fgrep "Fehler" log.txt
   ```

2. **Rekursive Suche in einem Verzeichnis**:
   Um alle Vorkommen der Zeichenfolge "TODO" in allen `.txt`-Dateien innerhalb eines Verzeichnisses und seiner Unterverzeichnisse zu finden, verwenden Sie:
   ```bash
   fgrep -r "TODO" *.txt
   ```

## Tipps
- Verwenden Sie `fgrep` anstelle von `grep`, wenn Sie sicher sind, dass Ihre Suchzeichenfolge keine regulären Ausdrücke enthält, um die Leistung zu verbessern.
- Kombinieren Sie `fgrep` mit anderen Befehlen wie `less`, um die Ausgabe besser zu durchsuchen:
  ```bash
  fgrep "Fehler" log.txt | less
  ```
- Nutzen Sie die Option `-i`, wenn Sie eine Suche durchführen möchten, die nicht zwischen Groß- und Kleinschreibung unterscheidet, um umfassendere Ergebnisse zu erhalten.

Mit diesen Informationen sind Sie gut gerüstet, um den Befehl `fgrep` effektiv in Ihren Bash-Skripten und -Befehlen zu verwenden.