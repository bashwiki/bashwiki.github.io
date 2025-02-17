# [Linux] Bash mapfile Verwendung: Liest Zeilen in ein Array

## Übersicht
Der `mapfile`-Befehl in Bash wird verwendet, um Zeilen aus einer Datei oder von der Standardeingabe in ein Array zu lesen. Dies ist besonders nützlich, wenn Sie mehrere Zeilen verarbeiten und in einer strukturierten Form speichern möchten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
mapfile [Optionen] [Argumente]
```

## Häufige Optionen
- `-t`: Entfernt das Zeilenende von jeder Zeile, die in das Array gelesen wird.
- `-n N`: Liest maximal N Zeilen.
- `-O N`: Setzt den Index des Arrays auf N, anstatt bei 0 zu beginnen.

## Häufige Beispiele

### Beispiel 1: Einfache Verwendung
Liest alle Zeilen aus einer Datei in ein Array.

```bash
mapfile zeilen < datei.txt
```

### Beispiel 2: Zeilen ohne Zeilenenden
Liest die Zeilen aus einer Datei und entfernt die Zeilenenden.

```bash
mapfile -t zeilen < datei.txt
```

### Beispiel 3: Nur die ersten 5 Zeilen lesen
Liest nur die ersten 5 Zeilen einer Datei in ein Array.

```bash
mapfile -n 5 zeilen < datei.txt
```

### Beispiel 4: Array-Index anpassen
Setzt den Index des Arrays auf 1 und liest die Zeilen.

```bash
mapfile -O 1 zeilen < datei.txt
```

## Tipps
- Verwenden Sie die `-t`-Option, um unerwünschte Zeilenenden zu vermeiden, wenn Sie mit den Zeilen arbeiten.
- Überprüfen Sie den Inhalt des Arrays nach dem Lesen, indem Sie `echo "${zeilen[@]}"` verwenden.
- Kombinieren Sie `mapfile` mit anderen Bash-Befehlen, um komplexe Datenverarbeitungsaufgaben zu automatisieren.