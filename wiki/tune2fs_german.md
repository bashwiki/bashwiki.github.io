# [Linux] Bash tune2fs Verwendung: Anpassen von ext2/ext3/ext4-Dateisystemen

## Übersicht
Der Befehl `tune2fs` wird verwendet, um verschiedene Parameter eines ext2-, ext3- oder ext4-Dateisystems zu ändern. Mit diesem Befehl können Administratoren die Leistung und das Verhalten des Dateisystems anpassen, ohne es neu zu formatieren.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
tune2fs [Optionen] [Argumente]
```

## Häufige Optionen
- `-c <anzahl>`: Setzt die maximale Anzahl an Mounts, nach denen das Dateisystem überprüft werden soll.
- `-i <intervall>`: Legt das Zeitintervall (in Tagen) fest, nach dem das Dateisystem überprüft werden soll.
- `-m <prozent>`: Setzt den Prozentsatz des Speicherplatzes, der für den Root-Benutzer reserviert ist.
- `-L <label>`: Ändert das Label des Dateisystems.
- `-O <option>`: Aktiviert eine bestimmte Funktion im Dateisystem.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `tune2fs`:

1. **Maximale Anzahl an Mounts setzen**:
   ```bash
   tune2fs -c 20 /dev/sda1
   ```
   Dieser Befehl setzt die maximale Anzahl an Mounts auf 20 für das Dateisystem auf `/dev/sda1`.

2. **Überprüfungsintervall in Tagen festlegen**:
   ```bash
   tune2fs -i 30 /dev/sda1
   ```
   Hiermit wird das Dateisystem alle 30 Tage überprüft.

3. **Reservierten Speicherplatz für Root-Benutzer ändern**:
   ```bash
   tune2fs -m 5 /dev/sda1
   ```
   Dieser Befehl reserviert 5% des Speicherplatzes für den Root-Benutzer auf dem Dateisystem.

4. **Label des Dateisystems ändern**:
   ```bash
   tune2fs -L MeinLabel /dev/sda1
   ```
   Damit wird das Label des Dateisystems auf `/dev/sda1` in "MeinLabel" geändert.

5. **Aktivieren einer Dateisystemfunktion**:
   ```bash
   tune2fs -O dir_index /dev/sda1
   ```
   Dieser Befehl aktiviert die `dir_index`-Funktion für das Dateisystem, was die Leistung bei Verzeichnissen mit vielen Dateien verbessern kann.

## Tipps
- Verwenden Sie `tune2fs` nur auf unmontierten Dateisystemen, um Datenverlust zu vermeiden.
- Überprüfen Sie die aktuellen Einstellungen mit `tune2fs -l /dev/sda1`, bevor Sie Änderungen vornehmen.
- Seien Sie vorsichtig beim Ändern von Optionen, die das Verhalten des Dateisystems beeinflussen, insbesondere bei Produktionssystemen.