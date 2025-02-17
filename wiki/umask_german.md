# [Linux] Bash umask Verwendung: Steuerung der Standardberechtigungen für neue Dateien und Verzeichnisse

## Übersicht
Der `umask`-Befehl in Bash wird verwendet, um die Standardberechtigungen für neu erstellte Dateien und Verzeichnisse festzulegen. Er bestimmt, welche Berechtigungen beim Erstellen von Dateien und Verzeichnissen standardmäßig eingeschränkt werden.

## Verwendung
Die grundlegende Syntax des `umask`-Befehls lautet:

```bash
umask [Optionen] [Argumente]
```

## Häufige Optionen
- `-S`: Zeigt die aktuelle Umask in symbolischer Form an.
- `-p`: Zeigt die aktuelle Umask für den aktuellen Benutzer an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `umask`-Befehls:

1. **Aktuelle Umask anzeigen:**
   ```bash
   umask
   ```

2. **Umask in symbolischer Form anzeigen:**
   ```bash
   umask -S
   ```

3. **Umask auf 027 setzen (lesen und ausführen für Gruppe, keine Berechtigungen für andere):**
   ```bash
   umask 027
   ```

4. **Umask auf 002 setzen (lesen und schreiben für Gruppe, keine Berechtigungen für andere):**
   ```bash
   umask 002
   ```

5. **Umask zurücksetzen auf Standardwert (typischerweise 022):**
   ```bash
   umask 022
   ```

## Tipps
- Überprüfen Sie regelmäßig Ihre Umask-Einstellungen, um sicherzustellen, dass neue Dateien und Verzeichnisse die gewünschten Berechtigungen haben.
- Setzen Sie die Umask in Ihrer Shell-Konfigurationsdatei (z.B. `.bashrc`), um sicherzustellen, dass sie bei jeder Sitzung angewendet wird.
- Seien Sie vorsichtig beim Setzen von Umask-Werten, da zu restriktive Berechtigungen den Zugriff auf Dateien und Verzeichnisse für andere Benutzer einschränken können.