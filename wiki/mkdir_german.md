# [Linux] Bash mkdir Verwendung: Verzeichnisse erstellen

## Übersicht
Der `mkdir`-Befehl wird verwendet, um neue Verzeichnisse (Ordner) im Dateisystem zu erstellen. Er ermöglicht es Benutzern, die Struktur ihrer Dateien zu organisieren, indem sie neue Ordner anlegen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
mkdir [Optionen] [Argumente]
```

## Häufige Optionen
- `-p`: Erstellt auch alle übergeordneten Verzeichnisse, falls sie nicht existieren.
- `-v`: Gibt eine ausführliche Ausgabe aus, die anzeigt, welche Verzeichnisse erstellt wurden.
- `-m`: Setzt die Berechtigungen für das neu erstellte Verzeichnis.

## Häufige Beispiele
1. **Ein einfaches Verzeichnis erstellen:**

   ```bash
   mkdir meinOrdner
   ```

2. **Mehrere Verzeichnisse gleichzeitig erstellen:**

   ```bash
   mkdir ordner1 ordner2 ordner3
   ```

3. **Ein Verzeichnis mit übergeordneten Verzeichnissen erstellen:**

   ```bash
   mkdir -p /home/benutzer/neuerOrdner/unterordner
   ```

4. **Ein Verzeichnis mit spezifischen Berechtigungen erstellen:**

   ```bash
   mkdir -m 755 meinSichererOrdner
   ```

5. **Ausführliche Ausgabe beim Erstellen eines Verzeichnisses:**

   ```bash
   mkdir -v meinNeuerOrdner
   ```

## Tipps
- Verwenden Sie die `-p`-Option, um sicherzustellen, dass alle erforderlichen übergeordneten Verzeichnisse gleichzeitig erstellt werden.
- Überprüfen Sie die Berechtigungen des Verzeichnisses mit `ls -l`, um sicherzustellen, dass sie Ihren Anforderungen entsprechen.
- Nutzen Sie die `-v`-Option, um Feedback zu erhalten, insbesondere wenn Sie mehrere Verzeichnisse auf einmal erstellen.