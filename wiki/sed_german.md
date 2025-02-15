# [리눅스] Bash sed 사용법

## Übersicht
`sed` (Stream Editor) ist ein leistungsfähiges Textverarbeitungswerkzeug in der Bash, das hauptsächlich verwendet wird, um Text in einer Datei oder einem Datenstrom zu bearbeiten. Es ermöglicht das Durchführen von grundlegenden Textoperationen wie Ersetzen, Löschen und Einfügen von Text. `sed` ist besonders nützlich für die Verarbeitung von großen Textdateien und kann in Skripten automatisiert werden, um wiederholbare Aufgaben zu erledigen.

## Verwendung
Die grundlegende Syntax des `sed`-Befehls lautet:

```bash
sed [Optionen] 'Befehl' Datei
```

### Häufige Optionen:
- `-e`: Ermöglicht die Angabe mehrerer Befehle.
- `-i`: Bearbeitet die Datei direkt (in-place) ohne eine separate Ausgabe zu erzeugen.
- `-n`: Unterdrückt die Standardausgabe; nützlich, wenn nur bestimmte Ausgaben angezeigt werden sollen.
- `s`: Der Ersetzungsbefehl, um Text zu suchen und zu ersetzen.

## Beispiele

### Beispiel 1: Text ersetzen
Um in einer Datei `datei.txt` das Wort "alt" durch "neu" zu ersetzen, verwenden Sie den folgenden Befehl:

```bash
sed 's/alt/neu/g' datei.txt
```
Hierbei steht `s` für "ersetzen", `alt` ist das zu suchende Wort, `neu` ist das Ersetzungwort, und `g` bedeutet, dass alle Vorkommen in der Zeile ersetzt werden sollen.

### Beispiel 2: In-place Bearbeitung
Um das Wort "alt" durch "neu" in der Datei `datei.txt` direkt zu ersetzen, verwenden Sie:

```bash
sed -i 's/alt/neu/g' datei.txt
```
Mit der Option `-i` wird die Datei direkt aktualisiert, ohne eine separate Ausgabedatei zu erstellen.

## Tipps
- Verwenden Sie die Option `-n` zusammen mit dem Befehl `p`, um nur bestimmte Zeilen anzuzeigen, die ein bestimmtes Muster enthalten. Zum Beispiel:

```bash
sed -n '/Muster/p' datei.txt
```

- Testen Sie Ihre `sed`-Befehle zuerst ohne die `-i`-Option, um sicherzustellen, dass die gewünschten Änderungen korrekt sind, bevor Sie die Datei dauerhaft ändern.
- Nutzen Sie reguläre Ausdrücke für komplexere Such- und Ersetzungsoperationen, um die Flexibilität von `sed` voll auszuschöpfen.