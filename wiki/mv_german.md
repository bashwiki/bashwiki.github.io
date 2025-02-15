# [리눅스] Bash mv 사용법

## Übersicht
Der `mv`-Befehl in Bash wird verwendet, um Dateien und Verzeichnisse zu verschieben oder umzubenennen. Der Hauptzweck dieses Befehls besteht darin, die Position von Dateien im Dateisystem zu ändern oder ihnen einen neuen Namen zu geben, ohne den Inhalt der Datei zu verändern.

## Verwendung
Die grundlegende Syntax des `mv`-Befehls lautet:

```bash
mv [Optionen] Quelle Ziel
```

Hierbei steht `Quelle` für die Datei oder das Verzeichnis, das verschoben oder umbenannt werden soll, und `Ziel` für den neuen Speicherort oder den neuen Namen.

### Häufige Optionen
- `-i`: Interaktive Eingabe. Fragt vor dem Überschreiben einer bestehenden Datei nach.
- `-u`: Verschiebt nur, wenn die Quelle neuer ist als die Ziel-Datei oder wenn die Ziel-Datei nicht existiert.
- `-v`: Ausführliche Ausgabe. Zeigt an, welche Dateien verschoben oder umbenannt werden.

## Beispiele
### Beispiel 1: Datei umbenennen
Um eine Datei von `alte_datei.txt` in `neue_datei.txt` umzubenennen, verwenden Sie den folgenden Befehl:

```bash
mv alte_datei.txt neue_datei.txt
```

### Beispiel 2: Datei verschieben
Um eine Datei namens `dokument.txt` in ein Verzeichnis namens `archive` zu verschieben, verwenden Sie:

```bash
mv dokument.txt archive/
```

## Tipps
- Verwenden Sie die `-i`-Option, um versehentliches Überschreiben von Dateien zu vermeiden, insbesondere wenn Sie mit wichtigen Daten arbeiten.
- Nutzen Sie die `-v`-Option, um den Fortschritt Ihrer Dateioperationen zu überwachen, besonders wenn Sie mehrere Dateien gleichzeitig verschieben oder umbenennen.
- Achten Sie darauf, den vollständigen Pfad anzugeben, wenn Sie Dateien zwischen verschiedenen Verzeichnissen verschieben, um Verwirrung zu vermeiden.