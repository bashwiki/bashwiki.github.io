# [Linux] Bash head Verwendung: Zeilen am Anfang anzeigen

## Übersicht
Der Befehl `head` wird in der Bash verwendet, um die ersten Zeilen einer Datei anzuzeigen. Standardmäßig zeigt `head` die ersten 10 Zeilen an, kann jedoch angepasst werden, um eine beliebige Anzahl von Zeilen anzuzeigen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
head [Optionen] [Argumente]
```

## Häufige Optionen
- `-n [Anzahl]`: Gibt die ersten `[Anzahl]` Zeilen der Datei aus.
- `-c [Anzahl]`: Gibt die ersten `[Anzahl]` Bytes der Datei aus.
- `-q`: Unterdrückt die Ausgabe der Dateinamen bei mehreren Eingabedateien.
- `-v`: Zeigt die Dateinamen immer an, auch wenn nur eine Datei angegeben ist.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `head`-Befehls:

1. **Standardverwendung**: Zeigt die ersten 10 Zeilen einer Datei an.
   ```bash
   head datei.txt
   ```

2. **Anpassen der Zeilenanzahl**: Zeigt die ersten 5 Zeilen einer Datei an.
   ```bash
   head -n 5 datei.txt
   ```

3. **Anzeigen von Bytes**: Zeigt die ersten 20 Bytes einer Datei an.
   ```bash
   head -c 20 datei.txt
   ```

4. **Mehrere Dateien**: Zeigt die ersten 10 Zeilen von mehreren Dateien an.
   ```bash
   head datei1.txt datei2.txt
   ```

5. **Dateinamen immer anzeigen**: Zeigt die ersten 10 Zeilen einer Datei an und zeigt den Dateinamen an.
   ```bash
   head -v datei.txt
   ```

## Tipps
- Verwenden Sie die `-n`-Option, um die Anzahl der angezeigten Zeilen schnell anzupassen, je nach Bedarf.
- Kombinieren Sie `head` mit anderen Befehlen wie `grep`, um die ersten Zeilen von gefilterten Ergebnissen anzuzeigen.
- Nutzen Sie `head` in Skripten, um schnell einen Überblick über große Dateien zu erhalten, ohne sie vollständig zu laden.