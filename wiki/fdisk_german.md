# [리눅스] Bash fdisk 사용법

## Übersicht
Der Befehl `fdisk` ist ein leistungsstarkes Tool zur Partitionierung von Festplatten unter Linux. Es ermöglicht Benutzern, Partitionen auf Festplatten zu erstellen, zu löschen und zu verwalten. `fdisk` unterstützt hauptsächlich MBR (Master Boot Record) Partitionstabellen, ist jedoch auch in der Lage, GPT (GUID Partition Table) Partitionen zu verwalten, wenn die richtige Option verwendet wird.

## Verwendung
Die grundlegende Syntax des `fdisk`-Befehls lautet:

```bash
fdisk [OPTIONEN] [GERÄT]
```

Hierbei ist `[GERÄT]` das zu bearbeitende Blockgerät, z. B. `/dev/sda`. Einige häufig verwendete Optionen sind:

- `-l`: Listet alle Partitionen auf den verfügbaren Festplatten auf.
- `-u`: Zeigt die Größe der Partitionen in Sektoren an, anstatt in Blöcken.
- `-n`: Erstellt eine neue Partition.
- `-d`: Löscht eine bestehende Partition.
- `-t`: Ändert den Partitionstyp.

## Beispiele
### Beispiel 1: Auflisten der Partitionen
Um alle Partitionen auf der Festplatte `/dev/sda` aufzulisten, verwenden Sie den folgenden Befehl:

```bash
fdisk -l /dev/sda
```

Dieser Befehl zeigt eine Übersicht über alle Partitionen, deren Größe und Typ auf der angegebenen Festplatte.

### Beispiel 2: Erstellen einer neuen Partition
Um eine neue Partition auf der Festplatte `/dev/sda` zu erstellen, führen Sie `fdisk` ohne Optionen aus:

```bash
fdisk /dev/sda
```

Sie gelangen in die interaktive `fdisk`-Sitzung. Verwenden Sie die folgenden Schritte:
1. Geben Sie `n` ein, um eine neue Partition zu erstellen.
2. Wählen Sie den Partitionstyp (primär oder logisch).
3. Geben Sie die Start- und Endsektoren oder die Größe der Partition an.
4. Speichern Sie die Änderungen mit `w`.

## Tipps
- **Sichern Sie Ihre Daten**: Vor der Verwendung von `fdisk` sollten Sie immer ein Backup Ihrer wichtigen Daten erstellen, da Partitionierungsänderungen zu Datenverlust führen können.
- **Verwenden Sie `parted` für GPT**: Wenn Sie mit GPT-Partitionen arbeiten, ziehen Sie in Betracht, das Tool `parted` zu verwenden, da es eine bessere Unterstützung für GPT bietet.
- **Vorsicht bei der Auswahl des Geräts**: Stellen Sie sicher, dass Sie das richtige Gerät auswählen, um versehentliche Änderungen an der falschen Festplatte zu vermeiden.

Mit diesen Informationen sind Sie gut gerüstet, um den `fdisk`-Befehl effektiv zu nutzen und Ihre Festplattenpartitionen zu verwalten.