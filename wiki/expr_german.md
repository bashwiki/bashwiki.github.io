# [Linux] Bash expr Verwendung: Berechnungen und String-Manipulationen

## Übersicht
Der Befehl `expr` wird in Bash verwendet, um einfache mathematische Berechnungen durchzuführen und mit Zeichenfolgen zu arbeiten. Er kann sowohl arithmetische Operationen als auch logische Vergleiche und String-Operationen ausführen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
expr [Optionen] [Argumente]
```

## Häufige Optionen
- `+` : Addition von zwei Zahlen.
- `-` : Subtraktion von zwei Zahlen.
- `*` : Multiplikation von zwei Zahlen (muss mit Escape-Zeichen `\` verwendet werden).
- `/` : Division von zwei Zahlen.
- `%` : Modulo-Operation (Rest der Division).
- `=` : Vergleich, ob zwei Werte gleich sind.
- `!=` : Vergleich, ob zwei Werte ungleich sind.

## Häufige Beispiele

### 1. Einfache Addition
Um zwei Zahlen zu addieren, verwenden Sie:

```bash
expr 5 + 3
```

### 2. Subtraktion
Um eine Zahl von einer anderen zu subtrahieren:

```bash
expr 10 - 4
```

### 3. Multiplikation
Um zwei Zahlen zu multiplizieren:

```bash
expr 6 \* 7
```

### 4. Division
Um eine Zahl durch eine andere zu dividieren:

```bash
expr 20 / 4
```

### 5. Modulo
Um den Rest einer Division zu erhalten:

```bash
expr 10 % 3
```

### 6. String-Länge
Um die Länge einer Zeichenfolge zu ermitteln:

```bash
expr length "Hallo Welt"
```

### 7. String-Vergleich
Um zu überprüfen, ob zwei Zeichenfolgen gleich sind:

```bash
expr "abc" = "abc"
```

## Tipps
- Verwenden Sie Escape-Zeichen (`\`) für Operatoren wie `*`, um Missverständnisse mit Shell-Globbing zu vermeiden.
- `expr` gibt nur Ganzzahlen zurück; für Fließkommazahlen sollten Sie andere Werkzeuge wie `bc` verwenden.
- Nutzen Sie Klammern, um die Reihenfolge der Operationen zu steuern, z.B. `expr \( 2 + 3 \) \* 4`.

Mit diesen Informationen sind Sie gut gerüstet, um den `expr`-Befehl effektiv in Ihren Bash-Skripten zu verwenden!