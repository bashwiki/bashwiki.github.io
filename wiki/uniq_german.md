# [Linux] Bash uniq Verwendung: Entfernen von aufeinanderfolgenden Duplikaten

## Übersicht
Der Befehl `uniq` wird in Bash verwendet, um aufeinanderfolgende doppelte Zeilen aus einer Datei oder von der Standardeingabe zu entfernen. Er ist besonders nützlich, um Daten zu bereinigen und die Ausgabe zu vereinfachen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
uniq [Optionen] [Argumente]
```

## Häufige Optionen
- `-c`: Zählt die Anzahl der Vorkommen jeder Zeile und gibt diese zusammen mit der Zeile aus.
- `-d`: Gibt nur die Zeilen aus, die mehr als einmal vorkommen.
- `-u`: Gibt nur die Zeilen aus, die einzigartig sind (d.h. nur einmal vorkommen).
- `-i`: Ignoriert die Groß- und Kleinschreibung beim Vergleich der Zeilen.

## Häufige Beispiele

1. **Einfaches Entfernen von Duplikaten:**
   ```bash
   uniq datei.txt
   ```

2. **Zählen der Vorkommen jeder Zeile:**
   ```bash
   uniq -c datei.txt
   ```

3. **Anzeigen nur der doppelten Zeilen:**
   ```bash
   uniq -d datei.txt
   ```

4. **Anzeigen nur der einzigartigen Zeilen:**
   ```bash
   uniq -u datei.txt
   ```

5. **Ignorieren der Groß- und Kleinschreibung:**
   ```bash
   uniq -i datei.txt
   ```

## Tipps
- Stellen Sie sicher, dass die Eingabedatei sortiert ist, bevor Sie `uniq` verwenden, da der Befehl nur aufeinanderfolgende Duplikate entfernt.
- Kombinieren Sie `uniq` mit dem `sort`-Befehl, um eine vollständige Liste eindeutiger Zeilen zu erhalten:
  ```bash
  sort datei.txt | uniq
  ```
- Verwenden Sie `uniq` in Skripten, um die Ausgabe von anderen Befehlen zu filtern und zu bereinigen.