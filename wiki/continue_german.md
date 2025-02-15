# [리눅스] Bash continue 사용법

## Übersicht
Der Befehl `continue` in Bash wird innerhalb von Schleifen verwendet, um die aktuelle Iteration der Schleife zu beenden und mit der nächsten Iteration fortzufahren. Dies ist besonders nützlich, wenn bestimmte Bedingungen erfüllt sind und der Rest des Schleifenblocks übersprungen werden soll.

## Verwendung
Die grundlegende Syntax des `continue`-Befehls ist einfach:

```bash
continue [N]
```

- `N`: Optional. Gibt an, wie viele Schleifenebenen übersprungen werden sollen. Wenn `N` nicht angegeben ist, wird die nächste Iteration der innersten Schleife fortgesetzt.

## Beispiele

### Beispiel 1: Einfache Schleife
In diesem Beispiel wird eine `for`-Schleife verwendet, um die Zahlen von 1 bis 5 zu durchlaufen. Wenn die Zahl 3 erreicht wird, wird die Iteration übersprungen.

```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    continue
  fi
  echo "Zahl: $i"
done
```
**Ausgabe:**
```
Zahl: 1
Zahl: 2
Zahl: 4
Zahl: 5
```

### Beispiel 2: Mit `while`-Schleife
In diesem Beispiel wird eine `while`-Schleife verwendet, um die Zahlen von 1 bis 5 zu durchlaufen. Wenn die Zahl gerade ist, wird die Iteration übersprungen.

```bash
i=1
while [ $i -le 5 ]; do
  if [ $((i % 2)) -eq 0 ]; then
    ((i++))
    continue
  fi
  echo "Ungerade Zahl: $i"
  ((i++))
done
```
**Ausgabe:**
```
Ungerade Zahl: 1
Ungerade Zahl: 3
Ungerade Zahl: 5
```

## Tipps
- Verwenden Sie `continue`, um den Code lesbarer zu gestalten, indem Sie unnötige Verschachtelungen vermeiden.
- Achten Sie darauf, dass `continue` nur innerhalb von Schleifen verwendet werden kann. Andernfalls führt es zu einem Fehler.
- Nutzen Sie die optionale Zahl `N`, um gezielt mehrere Schleifenebenen zu überspringen, wenn Sie in verschachtelten Schleifen arbeiten.