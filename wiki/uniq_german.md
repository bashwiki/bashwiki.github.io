# [리눅스] Bash uniq 사용법

## Übersicht
Der Befehl `uniq` wird in der Bash verwendet, um aufeinanderfolgende, doppelte Zeilen in einer Datei oder von der Standardeingabe zu entfernen. Der Hauptzweck von `uniq` besteht darin, die Ausgabe zu bereinigen, indem nur einzigartige Zeilen angezeigt werden. Es ist wichtig zu beachten, dass `uniq` nur auf aufeinanderfolgende Duplikate reagiert. Daher wird es häufig in Kombination mit dem Befehl `sort` verwendet, um sicherzustellen, dass alle Duplikate zusammenstehen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
uniq [OPTIONEN] [EINGABE] [AUSGABE]
```

### Häufige Optionen:
- `-c`: Zählt die Anzahl der Vorkommen jeder einzigartigen Zeile und gibt diese Anzahl vor der Zeile aus.
- `-d`: Gibt nur die Zeilen aus, die mehr als einmal vorkommen.
- `-u`: Gibt nur die einzigartigen Zeilen aus, die nur einmal vorkommen.
- `-i`: Ignoriert die Groß- und Kleinschreibung beim Vergleich der Zeilen.

## Beispiele
### Beispiel 1: Grundlegende Verwendung
Angenommen, Sie haben eine Datei namens `beispiel.txt` mit folgendem Inhalt:

```
Apfel
Apfel
Banane
Banane
Kirsche
```

Um die doppelten Zeilen zu entfernen, verwenden Sie den Befehl:

```bash
uniq beispiel.txt
```

Die Ausgabe wird sein:

```
Apfel
Banane
Kirsche
```

### Beispiel 2: Zählen der Vorkommen
Wenn Sie die Anzahl der Vorkommen jeder einzigartigen Zeile sehen möchten, können Sie die `-c` Option verwenden:

```bash
uniq -c beispiel.txt
```

Die Ausgabe wird sein:

```
      2 Apfel
      2 Banane
      1 Kirsche
```

## Tipps
- Um sicherzustellen, dass `uniq` korrekt funktioniert, sortieren Sie die Datei zuerst mit dem Befehl `sort`, insbesondere wenn die Duplikate nicht aufeinanderfolgend sind. Beispiel:

```bash
sort beispiel.txt | uniq
```

- Verwenden Sie die `-d` Option, wenn Sie nur die doppelten Zeilen sehen möchten, um schnell herauszufinden, welche Zeilen mehrmals in Ihrer Datei vorkommen.
- Die `-u` Option ist nützlich, wenn Sie nur die einzigartigen Zeilen extrahieren möchten, die nicht wiederholt werden.

Mit diesen Informationen sind Sie gut gerüstet, um den `uniq` Befehl effektiv in Ihren Bash-Skripten und -Befehlen zu verwenden.