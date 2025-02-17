# [Linux] Bash rev: Zeichen in Zeilen umkehren

## Overview
Der `rev` Befehl in Bash wird verwendet, um die Zeichen in jeder Zeile einer Datei oder von der Standardeingabe umzukehren. Dies kann nützlich sein, wenn man beispielsweise die Reihenfolge der Zeichen in Textzeilen ändern möchte.

## Usage
Die grundlegende Syntax des `rev` Befehls lautet:

```bash
rev [optionen] [argumente]
```

## Common Options
- `-o, --output=DATEI`: Gibt die umgekehrten Zeilen in die angegebene Datei aus.
- `-h, --help`: Zeigt eine Hilfe-Seite mit Informationen zur Verwendung des Befehls an.
- `-V, --version`: Gibt die Versionsnummer des Befehls aus.

## Common Examples
Hier sind einige praktische Beispiele zur Verwendung des `rev` Befehls:

1. **Umkehren von Text aus einer Datei**:
   ```bash
   rev datei.txt
   ```

2. **Umkehren von Text aus der Standardeingabe**:
   ```bash
   echo "Hallo Welt" | rev
   ```

3. **Umkehren und in eine neue Datei schreiben**:
   ```bash
   rev datei.txt > umgekehrte_datei.txt
   ```

4. **Umkehren mehrerer Zeilen**:
   ```bash
   printf "Zeile 1\nZeile 2\nZeile 3\n" | rev
   ```

## Tips
- Verwenden Sie `rev` in Kombination mit anderen Befehlen, um komplexe Textbearbeitungen durchzuführen.
- Achten Sie darauf, dass `rev` nur die Zeichen in jeder Zeile umkehrt, nicht die Zeilen selbst.
- Nutzen Sie die `-o` Option, um die Ausgabe direkt in eine Datei zu speichern, anstatt sie auf dem Bildschirm anzuzeigen.