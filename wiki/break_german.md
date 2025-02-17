# [Linux] Bash break Verwendung: Beendet Schleifen

## Übersicht
Der `break` Befehl in Bash wird verwendet, um eine Schleife vorzeitig zu beenden. Dies ist besonders nützlich, wenn eine bestimmte Bedingung erfüllt ist und man nicht die gesamte Schleife durchlaufen möchte.

## Verwendung
Die grundlegende Syntax des `break` Befehls ist wie folgt:

```bash
break [n]
```

Hierbei steht `n` für die Anzahl der Schleifen, die beendet werden sollen. Wenn `n` nicht angegeben ist, wird die innere Schleife beendet.

## Häufige Optionen
- `n`: Gibt an, wie viele Schleifen beendet werden sollen. Standardmäßig wird nur die innerste Schleife beendet.

## Häufige Beispiele

### Beispiel 1: Beenden einer `for` Schleife
```bash
for i in {1..10}; do
  if [ $i -eq 5 ]; then
    break
  fi
  echo $i
done
```
In diesem Beispiel wird die Schleife beendet, wenn `i` den Wert 5 erreicht.

### Beispiel 2: Beenden einer `while` Schleife
```bash
count=1
while true; do
  echo $count
  if [ $count -ge 3 ]; then
    break
  fi
  ((count++))
done
```
Hier wird die `while` Schleife beendet, wenn `count` den Wert 3 erreicht.

### Beispiel 3: Beenden einer verschachtelten Schleife
```bash
for i in {1..3}; do
  for j in {1..3}; do
    if [ $j -eq 2 ]; then
      break 2
    fi
    echo "i: $i, j: $j"
  done
done
```
In diesem Beispiel wird die äußere Schleife ebenfalls beendet, wenn `j` den Wert 2 erreicht.

## Tipps
- Verwenden Sie `break` in Kombination mit Bedingungen, um die Kontrolle über Schleifen zu behalten.
- Achten Sie darauf, wie viele Schleifen Sie mit `break n` beenden, um unerwartete Ergebnisse zu vermeiden.
- Nutzen Sie `break` in Skripten, um die Effizienz zu steigern, indem Sie unnötige Iterationen vermeiden.