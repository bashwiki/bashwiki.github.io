# [리눅스] Bash test 사용법

## Übersicht
Der `test` Befehl in Bash ist ein grundlegendes Werkzeug, das verwendet wird, um Bedingungen zu überprüfen. Es wird häufig in Skripten eingesetzt, um Entscheidungen zu treffen, basierend auf dem Ergebnis der Überprüfung. Der Hauptzweck von `test` besteht darin, verschiedene Arten von Bedingungen zu evaluieren, wie z.B. Dateieigenschaften, numerische Vergleiche und Zeichenfolgenvergleiche.

## Verwendung
Die grundlegende Syntax des `test` Befehls lautet:

```bash
test EXPRESSION
```

Alternativ kann `test` auch durch die Verwendung von eckigen Klammern `[` und `]` aufgerufen werden:

```bash
[ EXPRESSION ]
```

### Häufige Optionen
- `-e FILE`: Überprüft, ob die angegebene Datei existiert.
- `-d FILE`: Überprüft, ob die angegebene Datei ein Verzeichnis ist.
- `-f FILE`: Überprüft, ob die angegebene Datei eine reguläre Datei ist.
- `-z STRING`: Überprüft, ob die angegebene Zeichenfolge leer ist.
- `-n STRING`: Überprüft, ob die angegebene Zeichenfolge nicht leer ist.
- `NUM1 -eq NUM2`: Überprüft, ob zwei Zahlen gleich sind.
- `NUM1 -ne NUM2`: Überprüft, ob zwei Zahlen ungleich sind.
- `NUM1 -lt NUM2`: Überprüft, ob NUM1 kleiner als NUM2 ist.
- `NUM1 -gt NUM2`: Überprüft, ob NUM1 größer als NUM2 ist.

## Beispiele
### Beispiel 1: Überprüfen, ob eine Datei existiert
```bash
if test -e /path/to/file.txt; then
    echo "Die Datei existiert."
else
    echo "Die Datei existiert nicht."
fi
```

### Beispiel 2: Überprüfen, ob eine Zahl größer ist als eine andere
```bash
NUM1=10
NUM2=5

if test $NUM1 -gt $NUM2; then
    echo "$NUM1 ist größer als $NUM2."
else
    echo "$NUM1 ist nicht größer als $NUM2."
fi
```

## Tipps
- Verwenden Sie die eckigen Klammern `[` und `]` für eine lesbarere Syntax, da dies in vielen Skripten üblich ist.
- Achten Sie darauf, dass zwischen den eckigen Klammern und den Bedingungen Leerzeichen stehen müssen.
- Nutzen Sie die `&&` und `||` Operatoren, um mehrere Bedingungen in einer Zeile zu kombinieren, z.B. `test -e file.txt && echo "Datei existiert."`.
- Für komplexere Bedingungen kann der `[[` Befehl verwendet werden, der erweiterte Funktionen bietet, wie z.B. reguläre Ausdrücke.

Mit diesen Informationen sind Sie gut gerüstet, um den `test` Befehl effektiv in Ihren Bash-Skripten zu verwenden.