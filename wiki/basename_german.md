# [리눅스] Bash basename 사용법

## Übersicht
Der Befehl `basename` wird in Bash verwendet, um den Basisnamen einer Datei oder eines Verzeichnisses zu extrahieren. Dies bedeutet, dass der Befehl den Pfad einer Datei oder eines Verzeichnisses entfernt und nur den letzten Teil des Pfades zurückgibt, der den Dateinamen oder das Verzeichnis darstellt. Der Hauptzweck von `basename` ist es, den Dateinamen aus einem vollständigen Pfad zu isolieren, was in Skripten und Automatisierungsaufgaben nützlich sein kann.

## Verwendung
Die grundlegende Syntax des `basename`-Befehls lautet:

```bash
basename [OPTIONEN] NAME [SUFFIX]
```

### Optionen
- `NAME`: Der vollständige Pfad oder der Dateiname, von dem der Basisname extrahiert werden soll.
- `SUFFIX`: (Optional) Ein Suffix, das vom Basisnamen entfernt werden soll. Dies ist nützlich, um Dateiendungen zu entfernen.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des `basename`-Befehls:

### Beispiel 1: Basisnamen extrahieren
```bash
basename /usr/local/bin/script.sh
```
**Ausgabe:**
```
script.sh
```
In diesem Beispiel wird der vollständige Pfad `/usr/local/bin/script.sh` übergeben, und `basename` gibt nur `script.sh` zurück.

### Beispiel 2: Suffix entfernen
```bash
basename /usr/local/bin/script.sh .sh
```
**Ausgabe:**
```
script
```
Hier wird das Suffix `.sh` entfernt, sodass nur der Basisname `script` zurückgegeben wird.

## Tipps
- Verwenden Sie `basename` in Skripten, um die Lesbarkeit zu verbessern, indem Sie nur den Dateinamen anzeigen, anstatt den gesamten Pfad.
- Kombinieren Sie `basename` mit anderen Befehlen wie `find` oder `ls`, um dynamisch Basisnamen von mehreren Dateien zu extrahieren.
- Achten Sie darauf, dass das Suffix genau mit dem Ende des Basisnamens übereinstimmt, da `basename` nur dann das Suffix entfernt, wenn es exakt übereinstimmt.