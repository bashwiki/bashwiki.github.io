# [Linux] Bash dd Verwendung: Daten kopieren und konvertieren

## Übersicht
Der `dd`-Befehl ist ein leistungsstarkes Werkzeug in Unix-ähnlichen Betriebssystemen, das zum Kopieren und Konvertieren von Daten verwendet wird. Er wird häufig für das Erstellen von Backups, das Klonen von Festplatten und das Konvertieren von Dateiformaten eingesetzt.

## Verwendung
Die grundlegende Syntax des `dd`-Befehls lautet:

```bash
dd [Optionen] [Argumente]
```

## Häufige Optionen
- `if=`: Gibt die Eingabedatei an (Input File).
- `of=`: Gibt die Ausgabedatei an (Output File).
- `bs=`: Legt die Blockgröße fest, die beim Lesen und Schreiben verwendet wird.
- `count=`: Gibt die Anzahl der zu kopierenden Blöcke an.
- `status=`: Steuert die Ausgabe von Fortschrittsinformationen (z.B. `none`, `noxfer`, `progress`).

## Häufige Beispiele

### 1. Erstellen eines Festplatten-Images
Um ein Abbild einer Festplatte zu erstellen, verwenden Sie den folgenden Befehl:

```bash
dd if=/dev/sda of=/path/to/backup.img bs=4M
```

### 2. Wiederherstellen eines Festplatten-Images
Um ein zuvor erstelltes Abbild wiederherzustellen, verwenden Sie:

```bash
dd if=/path/to/backup.img of=/dev/sda bs=4M
```

### 3. Kopieren einer Datei
Um eine Datei in eine andere zu kopieren, können Sie `dd` wie folgt verwenden:

```bash
dd if=/path/to/source.file of=/path/to/destination.file
```

### 4. Erstellen einer bootfähigen USB-Stick
Um ein ISO-Image auf einen USB-Stick zu schreiben, verwenden Sie:

```bash
dd if=/path/to/image.iso of=/dev/sdb bs=4M status=progress
```

## Tipps
- Seien Sie vorsichtig mit dem `of=`-Argument, da das Überschreiben von Festplatten zu Datenverlust führen kann.
- Verwenden Sie die Option `status=progress`, um den Fortschritt des Kopiervorgangs anzuzeigen.
- Testen Sie `dd` zuerst mit kleinen Dateien, um sicherzustellen, dass Sie die richtigen Optionen verwenden.