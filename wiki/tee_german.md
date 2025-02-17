# [Linux] Bash tee Verwendung: Daten in Dateien und Standardausgabe umleiten

## Übersicht
Der `tee` Befehl in Bash wird verwendet, um die Eingabe sowohl in eine Datei zu schreiben als auch an die Standardausgabe (in der Regel das Terminal) weiterzuleiten. Dies ist besonders nützlich, wenn Sie den Output eines Befehls sowohl speichern als auch anzeigen möchten.

## Verwendung
Die grundlegende Syntax des `tee` Befehls lautet:

```bash
tee [Optionen] [Datei(en)]
```

## Häufige Optionen
- `-a`: Fügt die Ausgabe an die angegebene Datei an, anstatt sie zu überschreiben.
- `-i`: Ignoriert Interrupt-Signale.
- `--help`: Zeigt eine Hilfeseite mit Informationen zur Verwendung von tee an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `tee`:

1. **Einfaches Schreiben in eine Datei:**
   ```bash
   echo "Hallo Welt" | tee datei.txt
   ```
   Dies schreibt "Hallo Welt" in die Datei `datei.txt` und zeigt es gleichzeitig im Terminal an.

2. **An eine bestehende Datei anhängen:**
   ```bash
   echo "Neue Zeile" | tee -a datei.txt
   ```
   Hier wird "Neue Zeile" an die Datei `datei.txt` angehängt, ohne den bestehenden Inhalt zu überschreiben.

3. **Ausgabe eines Befehls speichern:**
   ```bash
   ls -l | tee dateiliste.txt
   ```
   Dies listet die Dateien im aktuellen Verzeichnis auf und speichert die Ausgabe in `dateiliste.txt`.

4. **Mehrere Dateien gleichzeitig beschreiben:**
   ```bash
   echo "Daten für mehrere Dateien" | tee datei1.txt datei2.txt
   ```
   In diesem Beispiel wird der Text in sowohl `datei1.txt` als auch `datei2.txt` geschrieben.

## Tipps
- Verwenden Sie die `-a` Option, wenn Sie sicherstellen möchten, dass bestehende Daten in einer Datei nicht verloren gehen.
- Kombinieren Sie `tee` mit anderen Befehlen in einer Pipeline, um die Ausgabe zu speichern und gleichzeitig anzuzeigen.
- Nutzen Sie `tee` in Skripten, um Protokolle zu erstellen, während Sie die Ausführungsergebnisse im Terminal sehen.