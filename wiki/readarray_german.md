# [리눅스] Bash readarray 사용법

## Übersicht
Der Befehl `readarray` (auch bekannt als `mapfile`) wird in Bash verwendet, um eine Datei oder die Standardausgabe in ein Array zu lesen. Die Hauptfunktion von `readarray` besteht darin, jede Zeile der Eingabe in ein Element des Arrays zu speichern. Dies ist besonders nützlich, wenn Sie mit Zeilen von Daten arbeiten und diese in einem Skript weiterverarbeiten möchten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
readarray [Optionen] ARRAY_NAME
```

### Häufige Optionen:
- `-n N`: Liest nur die ersten N Zeilen der Eingabe.
- `-s N`: Überspringt die ersten N Zeilen der Eingabe.
- `-t`: Entfernt das Zeilenende (newline) von jeder Zeile, die in das Array gelesen wird.
- `-d DELIMITER`: Setzt ein benutzerdefiniertes Trennzeichen anstelle des Standard-Zeilenumbruchs.

## Beispiele

### Beispiel 1: Einfache Verwendung
Angenommen, Sie haben eine Datei namens `daten.txt`, die mehrere Zeilen enthält. Sie können diese Datei in ein Array einlesen, wie folgt:

```bash
readarray zeilen < daten.txt
```

Nach dem Ausführen dieses Befehls sind die Zeilen der Datei `daten.txt` in dem Array `zeilen` gespeichert. Sie können dann auf die Elemente des Arrays zugreifen, z.B.:

```bash
echo "${zeilen[0]}"  # Gibt die erste Zeile der Datei aus
```

### Beispiel 2: Mit Optionen
Wenn Sie nur die ersten 3 Zeilen einer Datei lesen möchten und die Zeilenenden entfernen wollen, können Sie den Befehl wie folgt verwenden:

```bash
readarray -n 3 -t erste_drei < daten.txt
```

Jetzt enthält das Array `erste_drei` die ersten drei Zeilen der Datei ohne Zeilenenden.

## Tipps
- Verwenden Sie die Option `-t`, um unerwünschte Zeilenenden zu vermeiden, wenn Sie die Daten weiterverarbeiten möchten.
- Wenn Sie mit großen Dateien arbeiten, denken Sie daran, die Optionen `-n` und `-s` zu verwenden, um die Menge der gelesenen Daten zu steuern und die Leistung zu optimieren.
- Testen Sie den Inhalt des Arrays mit einer Schleife, um sicherzustellen, dass die Daten korrekt eingelesen wurden:

```bash
for zeile in "${zeilen[@]}"; do
    echo "$zeile"
done
```

Mit diesen Informationen sind Sie gut gerüstet, um den Befehl `readarray` effektiv in Ihren Bash-Skripten zu verwenden.