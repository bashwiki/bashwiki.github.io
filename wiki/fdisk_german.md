# [Linux] Bash fdisk Verwendung: Partitionierung von Festplatten

## Übersicht
Der `fdisk`-Befehl ist ein leistungsstarkes Tool zur Partitionierung von Festplatten unter Linux. Mit `fdisk` können Benutzer Partitionen erstellen, löschen und verwalten, um den Speicherplatz auf ihren Laufwerken effizient zu nutzen.

## Verwendung
Die grundlegende Syntax des `fdisk`-Befehls lautet:

```bash
fdisk [Optionen] [Gerät]
```

## Häufige Optionen
- `-l`: Listet alle Partitionen auf allen Festplatten auf.
- `-u`: Verwendet Sektoren anstelle von Zylindern zur Anzeige der Partitionierung.
- `-n`: Erstellt eine neue Partition.
- `-d`: Löscht eine bestehende Partition.
- `-t`: Ändert den Typ einer Partition.

## Häufige Beispiele

### 1. Auflisten der Partitionen
Um alle Partitionen auf dem System anzuzeigen, verwenden Sie:

```bash
fdisk -l
```

### 2. Neue Partition erstellen
Um eine neue Partition auf `/dev/sda` zu erstellen, starten Sie `fdisk` mit dem Gerät:

```bash
fdisk /dev/sda
```
Dann folgen Sie den Anweisungen, um eine neue Partition zu erstellen.

### 3. Partition löschen
Um eine Partition zu löschen, starten Sie `fdisk` und wählen Sie die entsprechende Partition aus:

```bash
fdisk /dev/sda
```
Geben Sie dann den Befehl `d` ein, um die Partition zu löschen.

### 4. Partitionstyp ändern
Um den Typ einer Partition zu ändern, verwenden Sie:

```bash
fdisk /dev/sda
```
Geben Sie dann den Befehl `t` ein und wählen Sie die Partition sowie den neuen Typ aus.

## Tipps
- Stellen Sie sicher, dass Sie ein Backup Ihrer Daten haben, bevor Sie Partitionen ändern oder löschen.
- Verwenden Sie `fdisk` mit Bedacht, da falsche Befehle zu Datenverlust führen können.
- Überprüfen Sie nach Änderungen die Partitionstabelle mit `fdisk -l`, um sicherzustellen, dass alles korrekt ist.