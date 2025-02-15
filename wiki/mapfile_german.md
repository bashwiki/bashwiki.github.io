# [리눅스] Bash mapfile 사용법

## Übersicht
Der Befehl `mapfile` (auch bekannt als `readarray`) ist ein integrierter Bash-Befehl, der dazu verwendet wird, Zeilen aus einer Datei oder von der Standardeingabe in ein Array zu lesen. Der Hauptzweck von `mapfile` besteht darin, die Verarbeitung von Daten in Array-Form zu erleichtern, was insbesondere bei der Arbeit mit großen Datenmengen nützlich ist.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
mapfile [-n N] [-s S] [-t] [array]
```

### Optionen:
- `-n N`: Liest maximal N Zeilen.
- `-s S`: Überspringt die ersten S Zeilen.
- `-t`: Entfernt das abschließende Zeilenende von jeder Zeile.
- `array`: Der Name des Arrays, in das die Zeilen gespeichert werden sollen. Wenn kein Array angegeben wird, wird das Standardarray `MAPFILE` verwendet.

## Beispiele

### Beispiel 1: Einfache Verwendung
Angenommen, wir haben eine Datei namens `daten.txt`, die mehrere Zeilen enthält. Um diese Zeilen in ein Array namens `meine_daten` zu lesen, können wir den folgenden Befehl verwenden:

```bash
mapfile meine_daten < daten.txt
```

Nach der Ausführung dieses Befehls enthält das Array `meine_daten` jede Zeile der Datei `daten.txt` als ein Element.

### Beispiel 2: Zeilen überspringen und trimmen
Wenn wir nur die letzten 3 Zeilen einer Datei lesen und die Zeilenenden entfernen möchten, können wir dies wie folgt tun:

```bash
mapfile -n 3 -t meine_daten < daten.txt
```

Hier werden nur die letzten 3 Zeilen von `daten.txt` in das Array `meine_daten` gelesen, und die Zeilenenden werden entfernt.

## Tipps
- Verwenden Sie die Option `-t`, um unerwünschte Zeilenenden zu vermeiden, wenn Sie mit den Daten weiterarbeiten.
- Wenn Sie große Dateien verarbeiten, kann das Speichern der Daten in einem Array die Verarbeitungsgeschwindigkeit erhöhen, da Sie nicht wiederholt auf die Datei zugreifen müssen.
- Überprüfen Sie die Länge des Arrays mit `${#meine_daten[@]}`, um sicherzustellen, dass die Daten korrekt geladen wurden.
- Seien Sie vorsichtig mit der Größe des Arrays, da Bash-Arrays eine maximale Größe haben, die von der Systemkonfiguration abhängt.