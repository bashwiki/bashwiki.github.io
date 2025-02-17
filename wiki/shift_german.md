# [Linux] Bash shift Verwendung: Entfernen von Positionsparametern

## Übersicht
Der Befehl `shift` wird in Bash verwendet, um die Positionsparameter nach links zu verschieben. Das bedeutet, dass der erste Parameter ($1) entfernt wird und alle nachfolgenden Parameter um eine Position nach vorne rücken. Dies ist besonders nützlich in Skripten, um mit einer variablen Anzahl von Argumenten zu arbeiten.

## Verwendung
Die grundlegende Syntax des Befehls ist wie folgt:

```bash
shift [n]
```

Hierbei ist `n` die Anzahl der Positionen, um die die Parameter verschoben werden sollen. Wenn `n` nicht angegeben ist, wird standardmäßig um eins verschoben.

## Häufige Optionen
- `n`: Gibt an, um wie viele Positionen die Parameter verschoben werden sollen. Wenn `n` nicht angegeben ist, wird um eins verschoben.

## Häufige Beispiele

### Beispiel 1: Einfaches Verschieben
```bash
#!/bin/bash
echo "Erster Parameter: $1"
shift
echo "Neuer erster Parameter: $1"
```
In diesem Beispiel wird der erste Parameter entfernt und der zweite Parameter rückt an die erste Position.

### Beispiel 2: Verschieben um mehrere Positionen
```bash
#!/bin/bash
echo "Erster Parameter: $1"
echo "Zweiter Parameter: $2"
shift 2
echo "Neuer erster Parameter: $1"
```
Hier werden zwei Positionen verschoben, sodass der dritte Parameter nun der erste ist.

### Beispiel 3: Verwendung in einer Schleife
```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Verarbeite Parameter: $1"
    shift
done
```
In diesem Beispiel werden alle übergebenen Parameter nacheinander verarbeitet, bis keine mehr vorhanden sind.

## Tipps
- Verwenden Sie `shift` in Kombination mit Schleifen, um alle Argumente in einem Skript effizient zu verarbeiten.
- Achten Sie darauf, dass nach dem Verschieben von Parametern die Anzahl der verbleibenden Parameter überprüft wird, um Fehler zu vermeiden.
- Nutzen Sie `shift` in Skripten, die mit einer variablen Anzahl von Eingaben arbeiten, um die Lesbarkeit und Wartbarkeit zu verbessern.