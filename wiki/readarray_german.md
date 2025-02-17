# [Linux] Bash readarray Verwendung: Liest Zeilen in ein Array ein

## Übersicht
Der Befehl `readarray` (auch bekannt als `mapfile`) in Bash wird verwendet, um Zeilen aus einer Eingabe (z. B. einer Datei oder einer Standardausgabe) in ein Array zu lesen. Jede Zeile wird zu einem Element des Arrays, was die Verarbeitung von Daten erleichtert.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
readarray [Optionen] [Arrayname]
```

## Häufige Optionen
- `-n N`: Liest nur die ersten N Zeilen ein.
- `-s N`: Überspringt die ersten N Zeilen der Eingabe.
- `-t`: Entfernt das Zeilenende von jeder Zeile, die in das Array eingelesen wird.

## Häufige Beispiele

### Beispiel 1: Einfache Verwendung
Lese alle Zeilen aus einer Datei in ein Array namens `mein_array` ein.

```bash
readarray mein_array < datei.txt
```

### Beispiel 2: Nur die ersten 3 Zeilen einlesen
Lese nur die ersten 3 Zeilen aus einer Datei in ein Array.

```bash
readarray -n 3 mein_array < datei.txt
```

### Beispiel 3: Zeilen ohne Zeilenende einlesen
Lese Zeilen aus einer Datei ein und entferne das Zeilenende.

```bash
readarray -t mein_array < datei.txt
```

### Beispiel 4: Zeilen überspringen
Überspringe die ersten 2 Zeilen und lese den Rest in ein Array ein.

```bash
readarray -s 2 mein_array < datei.txt
```

## Tipps
- Verwenden Sie die Option `-t`, um unerwünschte Zeilenenden zu vermeiden, wenn Sie die Daten weiterverarbeiten möchten.
- Achten Sie darauf, dass das Array in Bash eine Null-basierte Indizierung hat. Das erste Element ist also `mein_array[0]`.
- Nutzen Sie `printf` oder `echo`, um die Inhalte des Arrays anzuzeigen, z. B. `printf '%s\n' "${mein_array[@]}"`.