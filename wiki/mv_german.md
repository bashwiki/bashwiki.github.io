# [Linux] Bash mv Verwendung: Dateien und Verzeichnisse verschieben oder umbenennen

## Übersicht
Der `mv`-Befehl in Bash wird verwendet, um Dateien und Verzeichnisse zu verschieben oder umzubenennen. Er ist ein grundlegendes Werkzeug in der Kommandozeilenumgebung, das es Benutzern ermöglicht, ihre Dateien effizient zu organisieren.

## Verwendung
Die grundlegende Syntax des `mv`-Befehls lautet:

```bash
mv [Optionen] [Quellargumente] [Zielargument]
```

## Häufige Optionen
- `-i`: Fragt vor dem Überschreiben einer bestehenden Datei nach.
- `-u`: Verschiebt nur, wenn die Quelldatei neuer ist als die Zieldatei oder wenn die Zieldatei nicht existiert.
- `-v`: Zeigt detaillierte Informationen über die durchgeführten Aktionen an.
- `-n`: Verhindert das Überschreiben von Dateien.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `mv`-Befehls:

1. **Datei umbenennen**:
   ```bash
   mv alte_datei.txt neue_datei.txt
   ```

2. **Datei verschieben**:
   ```bash
   mv datei.txt /pfad/zum/neuen/ordner/
   ```

3. **Mehrere Dateien verschieben**:
   ```bash
   mv datei1.txt datei2.txt /pfad/zum/neuen/ordner/
   ```

4. **Datei mit Bestätigung verschieben**:
   ```bash
   mv -i datei.txt /pfad/zum/neuen/ordner/
   ```

5. **Datei nur verschieben, wenn sie neuer ist**:
   ```bash
   mv -u datei.txt /pfad/zum/neuen/ordner/
   ```

## Tipps
- Verwenden Sie die `-i`-Option, um versehentliches Überschreiben wichtiger Dateien zu vermeiden.
- Nutzen Sie die `-v`-Option, um zu sehen, was der Befehl tatsächlich tut, insbesondere wenn Sie mehrere Dateien verschieben.
- Überprüfen Sie den Zielpfad, um sicherzustellen, dass Sie die Dateien an den richtigen Ort verschieben.