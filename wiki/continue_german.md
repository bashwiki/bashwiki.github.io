# [Linux] Bash continue Verwendung: Fortsetzen einer Schleife

## Übersicht
Der Befehl `continue` wird in Bash verwendet, um den aktuellen Durchlauf einer Schleife zu beenden und mit dem nächsten Durchlauf fortzufahren. Dies ist nützlich, wenn bestimmte Bedingungen erfüllt sind und der Rest des Schleifeninhalts übersprungen werden soll.

## Verwendung
Die grundlegende Syntax des Befehls ist:

```bash
continue [option]
```

## Häufige Optionen
- `n`: Gibt an, in welcher Schleife das `continue` ausgeführt werden soll. Wenn `n` nicht angegeben wird, wird die nächste Iteration der innersten Schleife fortgesetzt.

## Häufige Beispiele

### Beispiel 1: Einfache Schleife mit continue
In diesem Beispiel wird die Schleife von 1 bis 5 durchlaufen, aber die Zahl 3 wird übersprungen.

```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    continue
  fi
  echo $i
done
```

**Ausgabe:**
```
1
2
4
5
```

### Beispiel 2: while-Schleife mit continue
Hier wird eine `while`-Schleife verwendet, um nur gerade Zahlen von 1 bis 10 auszugeben.

```bash
i=1
while [ $i -le 10 ]; do
  i=$((i + 1))
  if [ $((i % 2)) -ne 0 ]; then
    continue
  fi
  echo $i
done
```

**Ausgabe:**
```
2
4
6
8
10
```

### Beispiel 3: continue mit einer verschachtelten Schleife
In diesem Beispiel wird eine verschachtelte Schleife verwendet, um die Kombinationen von zwei Zahlen zu durchlaufen, wobei bestimmte Kombinationen übersprungen werden.

```bash
for i in {1..3}; do
  for j in {1..3}; do
    if [ $i -eq $j ]; then
      continue
    fi
    echo "i: $i, j: $j"
  done
done
```

**Ausgabe:**
```
i: 1, j: 2
i: 1, j: 3
i: 2, j: 1
i: 2, j: 3
i: 3, j: 1
i: 3, j: 2
```

## Tipps
- Verwenden Sie `continue`, um die Lesbarkeit Ihres Codes zu verbessern, indem Sie unnötige Verschachtelungen vermeiden.
- Achten Sie darauf, dass `continue` nur innerhalb von Schleifen verwendet werden kann; andernfalls führt es zu einem Fehler.
- Nutzen Sie die Option `n`, um gezielt in verschachtelten Schleifen zu steuern, welche Schleife fortgesetzt werden soll.