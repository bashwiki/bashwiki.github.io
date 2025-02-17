# [Linux] Bash useradd Verwendung: Benutzer erstellen

## Übersicht
Der Befehl `useradd` wird verwendet, um neue Benutzerkonten auf einem Linux-System zu erstellen. Mit diesem Befehl können Administratoren Benutzer hinzufügen und verschiedene Optionen zur Konfiguration der Benutzerkonten festlegen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
useradd [Optionen] [Argumente]
```

## Häufige Optionen
- `-m`: Erstellt das Home-Verzeichnis des Benutzers.
- `-s`: Legt die Standard-Shell für den Benutzer fest.
- `-G`: Fügt den Benutzer zu einer oder mehreren Gruppen hinzu.
- `-c`: Fügt einen Kommentar oder eine Beschreibung für den Benutzer hinzu.
- `-e`: Legt das Ablaufdatum des Benutzerkontos fest.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `useradd`:

1. **Einen neuen Benutzer mit Home-Verzeichnis erstellen:**
   ```bash
   useradd -m neuerbenutzer
   ```

2. **Einen Benutzer mit einer bestimmten Shell erstellen:**
   ```bash
   useradd -m -s /bin/bash neuerbenutzer
   ```

3. **Einen Benutzer zu mehreren Gruppen hinzufügen:**
   ```bash
   useradd -m -G gruppe1,gruppe2 neuerbenutzer
   ```

4. **Einen Benutzer mit einem Kommentar erstellen:**
   ```bash
   useradd -m -c "Neuer Benutzer für Testzwecke" neuerbenutzer
   ```

5. **Einen Benutzer mit einem Ablaufdatum erstellen:**
   ```bash
   useradd -m -e 2023-12-31 neuerbenutzer
   ```

## Tipps
- Überprüfen Sie nach dem Erstellen eines Benutzers, ob das Home-Verzeichnis und die Berechtigungen korrekt eingerichtet sind.
- Verwenden Sie den Befehl `passwd`, um ein Passwort für den neuen Benutzer festzulegen.
- Denken Sie daran, dass Sie Root-Rechte benötigen, um `useradd` auszuführen.