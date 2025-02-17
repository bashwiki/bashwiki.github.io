# [Linux] Bash mount Verwendung: Einbinden von Dateisystemen

## Übersicht
Der Befehl `mount` wird verwendet, um Dateisysteme in das Verzeichnisbaum des Linux-Systems einzubinden. Dies ermöglicht den Zugriff auf Dateien und Verzeichnisse, die sich auf anderen Speichermedien befinden, wie z.B. Festplatten, USB-Sticks oder Netzwerkfreigaben.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
mount [Optionen] [Gerät] [Zielverzeichnis]
```

## Häufige Optionen
- `-t`: Gibt den Typ des Dateisystems an (z.B. ext4, ntfs).
- `-o`: Ermöglicht das Festlegen von Optionen wie `ro` (nur lesen) oder `rw` (lesen und schreiben).
- `-a`: Bindet alle in der Datei `/etc/fstab` aufgeführten Dateisysteme ein.
- `-r`: Bindet das Dateisystem nur im Lesemodus ein.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `mount`-Befehls:

1. **Einbinden eines USB-Sticks**:
   ```bash
   mount /dev/sdb1 /mnt/usb
   ```

2. **Einbinden eines ext4-Dateisystems mit spezifischen Optionen**:
   ```bash
   mount -t ext4 -o rw /dev/sda1 /mnt/data
   ```

3. **Einbinden aller in fstab definierten Dateisysteme**:
   ```bash
   mount -a
   ```

4. **Einbinden eines Netzwerkfreigabe (NFS)**:
   ```bash
   mount -t nfs 192.168.1.100:/freigabe /mnt/nfs
   ```

## Tipps
- Stellen Sie sicher, dass das Zielverzeichnis existiert, bevor Sie das Dateisystem einbinden.
- Verwenden Sie `umount`, um ein eingebundenes Dateisystem sicher zu trennen.
- Überprüfen Sie mit `df -h`, welche Dateisysteme derzeit eingebunden sind und deren Nutzung.