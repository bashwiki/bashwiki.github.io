# [리눅스] Bash mount 사용법

## Übersicht
Der Befehl `mount` wird in Unix-ähnlichen Betriebssystemen verwendet, um Dateisysteme in das Verzeichnisbaum des Systems einzuhängen. Sein Hauptzweck besteht darin, physische oder virtuelle Speichergeräte (wie Festplatten, USB-Sticks oder Netzlaufwerke) für den Zugriff durch das Betriebssystem und die Benutzer verfügbar zu machen. Durch das Einhängen eines Dateisystems wird es möglich, auf die darin enthaltenen Dateien und Verzeichnisse zuzugreifen.

## Verwendung
Die grundlegende Syntax des `mount`-Befehls lautet:

```bash
mount [Optionen] <Gerät> <Zielverzeichnis>
```

### Häufige Optionen:
- `-t <Typ>`: Gibt den Typ des Dateisystems an (z.B. `ext4`, `ntfs`, `vfat`).
- `-o <Optionen>`: Ermöglicht die Angabe zusätzlicher Optionen, wie z.B. `ro` (read-only) oder `rw` (read-write).
- `-a`: Mountet alle in der Datei `/etc/fstab` aufgeführten Dateisysteme.
- `-r`: Mountet das Dateisystem im Nur-Lese-Modus.

## Beispiele
### Beispiel 1: Einhängen eines USB-Sticks
Angenommen, Ihr USB-Stick ist als `/dev/sdb1` erkannt worden und Sie möchten ihn im Verzeichnis `/mnt/usb` einhängen:

```bash
sudo mount -t vfat /dev/sdb1 /mnt/usb
```

### Beispiel 2: Einhängen eines Netzlaufwerks
Um ein Netzlaufwerk mit dem Typ `cifs` einzuhängen, können Sie den folgenden Befehl verwenden:

```bash
sudo mount -t cifs //192.168.1.100/freigabe /mnt/netzlaufwerk -o username=benutzername,password=passwort
```

## Tipps
- Stellen Sie sicher, dass das Zielverzeichnis existiert, bevor Sie den `mount`-Befehl ausführen. Sie können es mit `mkdir` erstellen, falls es nicht vorhanden ist.
- Überprüfen Sie nach dem Einhängen mit dem Befehl `df -h`, ob das Dateisystem erfolgreich eingehängt wurde.
- Verwenden Sie den `-o ro`-Schalter, wenn Sie ein Dateisystem nur im Lese-Modus einhängen möchten, um versehentliche Änderungen zu vermeiden.
- Denken Sie daran, das eingehängte Dateisystem mit dem Befehl `umount <Zielverzeichnis>` wieder auszuhängen, wenn Sie damit fertig sind.