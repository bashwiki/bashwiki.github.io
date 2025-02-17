# [Linux] Bash cat Verwendung: Dateien anzeigen und zusammenführen

## Übersicht
Der `cat`-Befehl (kurz für "concatenate") wird in der Bash verwendet, um den Inhalt von Dateien anzuzeigen, mehrere Dateien zusammenzuführen oder neue Dateien zu erstellen. Er ist ein einfaches, aber leistungsstarkes Werkzeug für die Arbeit mit Textdateien.

## Verwendung
Die grundlegende Syntax des `cat`-Befehls lautet:

```bash
cat [Optionen] [Argumente]
```

## Häufige Optionen
- `-n`: Nummeriert die Ausgaben der Zeilen.
- `-E`: Zeigt ein Dollarzeichen (`$`) am Ende jeder Zeile an.
- `-b`: Nummeriert nur nicht-leere Zeilen.
- `-s`: Unterdrückt aufeinanderfolgende leere Zeilen.

## Häufige Beispiele
1. **Inhalt einer Datei anzeigen:**
   ```bash
   cat datei.txt
   ```

2. **Inhalt mehrerer Dateien anzeigen:**
   ```bash
   cat datei1.txt datei2.txt
   ```

3. **Inhalt einer Datei in eine neue Datei kopieren:**
   ```bash
   cat datei.txt > neue_datei.txt
   ```

4. **Inhalt mehrerer Dateien in eine neue Datei zusammenführen:**
   ```bash
   cat datei1.txt datei2.txt > zusammengefuehrt.txt
   ```

5. **Nummerierte Ausgabe der Zeilen anzeigen:**
   ```bash
   cat -n datei.txt
   ```

## Tipps
- Verwenden Sie `cat` in Kombination mit anderen Befehlen, wie `grep`, um gezielt nach Inhalten in Dateien zu suchen.
- Seien Sie vorsichtig beim Überschreiben von Dateien mit `>`, um versehentliches Verlieren von Daten zu vermeiden.
- Nutzen Sie die Option `-s`, um die Lesbarkeit zu erhöhen, wenn Sie mit Dateien arbeiten, die viele leere Zeilen enthalten.