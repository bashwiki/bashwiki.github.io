# [Linux] Bash resize2fs Verwendung: Dateisystemgröße anpassen

## Übersicht
Der Befehl `resize2fs` wird verwendet, um die Größe eines ext2-, ext3- oder ext4-Dateisystems anzupassen. Dies kann nützlich sein, wenn Sie den verfügbaren Speicherplatz auf einer Partition erhöhen oder verringern möchten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
resize2fs [Optionen] [Argumente]
```

## Häufige Optionen
- `-f`: Erzwingt die Größenänderung, auch wenn das Dateisystem nicht als "sauber" markiert ist.
- `-p`: Zeigt den Fortschritt der Größenänderung an.
- `-s`: Passt die Größe des Dateisystems an die Größe der Partition an.
- `-M`: Reduziert das Dateisystem auf die minimal mögliche Größe.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `resize2fs`:

1. **Anpassen der Dateisystemgröße auf die gesamte Partition:**
   ```bash
   resize2fs /dev/sda1
   ```

2. **Erzwingen der Größenänderung eines nicht sauberen Dateisystems:**
   ```bash
   resize2fs -f /dev/sda1
   ```

3. **Anpassen der Größe des Dateisystems auf eine spezifische Größe (z.B. 20G):**
   ```bash
   resize2fs 20G /dev/sda1
   ```

4. **Fortschritt der Größenänderung anzeigen:**
   ```bash
   resize2fs -p /dev/sda1
   ```

## Tipps
- Stellen Sie sicher, dass das Dateisystem vor der Größenänderung ungemountet ist, um Datenverluste zu vermeiden.
- Führen Sie vor der Verwendung von `resize2fs` ein Backup wichtiger Daten durch.
- Verwenden Sie `df -h`, um den verfügbaren Speicherplatz vor und nach der Größenänderung zu überprüfen.