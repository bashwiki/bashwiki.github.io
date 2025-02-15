# [리눅스] Bash tune2fs 사용법

## Übersicht
Der Befehl `tune2fs` wird in Linux-Systemen verwendet, um die Parameter eines ext2-, ext3- oder ext4-Dateisystems zu ändern. Mit diesem Befehl können Administratoren verschiedene Aspekte des Dateisystems anpassen, wie z.B. die Anzahl der maximalen Mounts, die Zeit bis zur Überprüfung des Dateisystems und andere Optionen, die die Leistung und Integrität des Dateisystems beeinflussen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
tune2fs [Optionen] <Gerät>
```

Hierbei ist `<Gerät>` das zu bearbeitende Dateisystem, typischerweise in der Form `/dev/sdXn`, wobei `X` der Laufwerksbuchstabe und `n` die Partitionsnummer ist.

### Häufige Optionen
- `-c <anzahl>`: Setzt die maximale Anzahl der Mounts, nach denen das Dateisystem überprüft werden soll.
- `-i <Zeitspanne>`: Legt die Zeitspanne (in Tagen) fest, nach der das Dateisystem überprüft werden soll.
- `-m <Prozentsatz>`: Setzt den Prozentsatz des Speicherplatzes, der für den Superuser reserviert ist.
- `-O <Option>`: Aktiviert bestimmte Dateisystem-Features.
- `-L <Label>`: Ändert das Label des Dateisystems.

## Beispiele
### Beispiel 1: Maximale Mounts festlegen
Um die maximale Anzahl der Mounts auf 20 festzulegen, verwenden Sie den folgenden Befehl:

```bash
sudo tune2fs -c 20 /dev/sda1
```

### Beispiel 2: Überprüfungsintervall festlegen
Um das Überprüfungsintervall auf 30 Tage zu setzen, verwenden Sie diesen Befehl:

```bash
sudo tune2fs -i 30d /dev/sda1
```

## Tipps
- **Sichern Sie Ihre Daten**: Bevor Sie Änderungen an einem Dateisystem vornehmen, sollten Sie immer eine Sicherung Ihrer Daten erstellen.
- **Verwenden Sie mit Bedacht**: Änderungen an den Dateisystemparametern können die Leistung und Stabilität Ihres Systems beeinflussen. Stellen Sie sicher, dass Sie die Auswirkungen verstehen, bevor Sie Änderungen vornehmen.
- **Überprüfen Sie die aktuellen Einstellungen**: Mit dem Befehl `tune2fs -l <Gerät>` können Sie die aktuellen Einstellungen des Dateisystems anzeigen, bevor Sie Änderungen vornehmen.