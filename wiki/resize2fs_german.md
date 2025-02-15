# [리눅스] Bash resize2fs 사용법

## Übersicht
Der Befehl `resize2fs` wird verwendet, um die Größe von ext2-, ext3- und ext4-Dateisystemen zu ändern. Sein Hauptzweck besteht darin, ein Dateisystem an die Größe der zugrunde liegenden Partition anzupassen, sei es durch Vergrößerung oder Verkleinerung. Dies ist besonders nützlich, wenn Speicherplatz neu zugewiesen oder Partitionen angepasst werden müssen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
resize2fs [Optionen] <Gerät>
```

### Häufige Optionen:
- `-f`: Erzwingt die Größenänderung des Dateisystems, auch wenn es nicht erforderlich ist.
- `-p`: Zeigt den Fortschritt der Größenänderung an.
- `<Größe>`: Gibt die neue Größe des Dateisystems an. Dies kann in Blöcken, Kilobytes (K), Megabytes (M) oder Gigabytes (G) angegeben werden.

## Beispiele
### Beispiel 1: Vergrößerung eines Dateisystems
Um ein ext4-Dateisystem auf `/dev/sda1` auf die maximale Größe zu vergrößern, verwenden Sie den folgenden Befehl:

```bash
resize2fs /dev/sda1
```

### Beispiel 2: Verkleinerung eines Dateisystems
Um ein ext4-Dateisystem auf `/dev/sda1` auf eine Größe von 20 GB zu verkleinern, verwenden Sie:

```bash
resize2fs /dev/sda1 20G
```

## Tipps
- Stellen Sie sicher, dass das Dateisystem nicht gemountet ist, bevor Sie `resize2fs` verwenden, insbesondere bei der Verkleinerung, um Datenverlust zu vermeiden.
- Führen Sie vor der Größenänderung eine Sicherung Ihrer Daten durch, um sicherzustellen, dass keine wichtigen Informationen verloren gehen.
- Verwenden Sie die Option `-p`, um den Fortschritt der Operation zu überwachen, insbesondere bei großen Dateisystemen.