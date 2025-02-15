# [리눅스] Bash shift 사용법

## Übersicht
Der Befehl `shift` in Bash wird verwendet, um die Position der Positionsparameter in einem Skript zu verschieben. Dies bedeutet, dass der erste Parameter `$1` auf den Wert von `$2` gesetzt wird, `$2` auf `$3` und so weiter. Der Hauptzweck von `shift` besteht darin, die Argumente, die an ein Skript oder eine Funktion übergeben werden, schrittweise zu verarbeiten, indem man die bereits verarbeiteten Argumente "verschiebt".

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
shift [n]
```

Hierbei ist `n` eine optionale Zahl, die angibt, um wie viele Positionen die Parameter verschoben werden sollen. Wenn `n` nicht angegeben wird, wird standardmäßig um 1 verschoben.

### Optionen
- `n`: Gibt die Anzahl der Positionen an, um die die Parameter verschoben werden sollen. Wenn `n` größer ist als die Anzahl der übergebenen Parameter, werden alle Parameter gelöscht.

## Beispiele

### Beispiel 1: Einfaches Verschieben der Parameter
Angenommen, wir haben ein Skript namens `example.sh`, das mehrere Argumente akzeptiert:

```bash
#!/bin/bash
echo "Vor Shift: $1 $2 $3"
shift
echo "Nach Shift: $1 $2 $3"
```

Wenn Sie das Skript mit den Argumenten `arg1 arg2 arg3` ausführen:

```bash
bash example.sh arg1 arg2 arg3
```

Die Ausgabe wird sein:

```
Vor Shift: arg1 arg2 arg3
Nach Shift: arg2 arg3 
```

### Beispiel 2: Verschieben um mehrere Positionen
Sie können auch mehrere Positionen verschieben. Hier ist ein weiteres Beispiel:

```bash
#!/bin/bash
echo "Vor Shift: $1 $2 $3 $4"
shift 2
echo "Nach Shift: $1 $2 $3 $4"
```

Wenn Sie das Skript mit den Argumenten `arg1 arg2 arg3 arg4` ausführen:

```bash
bash example.sh arg1 arg2 arg3 arg4
```

Die Ausgabe wird sein:

```
Vor Shift: arg1 arg2 arg3 arg4
Nach Shift: arg3 arg4 
```

## Tipps
- Verwenden Sie `shift` in Schleifen, um alle übergebenen Argumente nacheinander zu verarbeiten. Dies ist besonders nützlich, wenn Sie eine unbekannte Anzahl von Argumenten haben.
- Achten Sie darauf, dass nach dem Verschieben von Parametern die nicht mehr benötigten Parameter nicht mehr zugänglich sind. Planen Sie Ihre Argumentverarbeitung entsprechend.
- Überprüfen Sie die Anzahl der verbleibenden Argumente mit `$#`, bevor Sie `shift` verwenden, um Fehler zu vermeiden, wenn Sie versuchen, über die Anzahl der übergebenen Argumente hinaus zu verschieben.