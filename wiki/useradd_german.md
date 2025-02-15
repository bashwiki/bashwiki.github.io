# [리눅스] Bash useradd 사용법

## Überblick
Der Befehl `useradd` wird in Linux-Systemen verwendet, um neue Benutzerkonten zu erstellen. Er ist ein grundlegendes Werkzeug für Systemadministratoren, um Benutzer in einem System zu verwalten. Mit `useradd` können Sie verschiedene Optionen angeben, um Benutzerkonten mit spezifischen Eigenschaften zu erstellen, wie z.B. Benutzername, Heimatverzeichnis und Shell.

## Verwendung
Die grundlegende Syntax des Befehls `useradd` lautet:

```bash
useradd [OPTIONEN] BENUTZERNAME
```

Hierbei ist `BENUTZERNAME` der Name des neuen Benutzers, den Sie erstellen möchten. Zu den häufig verwendeten Optionen gehören:

- `-m`: Erstellt das Heimatverzeichnis des Benutzers, falls es nicht existiert.
- `-s`: Gibt die Standard-Shell für den Benutzer an (z.B. `/bin/bash`).
- `-G`: Fügt den Benutzer einer oder mehreren Gruppen hinzu (z.B. `-G sudo`).
- `-c`: Fügt einen Kommentar hinzu, der typischerweise den vollständigen Namen des Benutzers enthält.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `useradd`:

1. **Neuen Benutzer mit Heimatverzeichnis erstellen**:
   ```bash
   useradd -m -s /bin/bash neuerbenutzer
   ```
   Dieser Befehl erstellt einen neuen Benutzer namens `neuerbenutzer`, erstellt ein Heimatverzeichnis und setzt die Standard-Shell auf `/bin/bash`.

2. **Benutzer mit Gruppenmitgliedschaft erstellen**:
   ```bash
   useradd -m -s /bin/bash -G sudo neuerbenutzer
   ```
   In diesem Beispiel wird der Benutzer `neuerbenutzer` erstellt, der Mitglied der `sudo`-Gruppe ist, was ihm administrative Berechtigungen verleiht.

## Tipps
- Stellen Sie sicher, dass Sie nach der Erstellung eines Benutzers das Passwort mit dem Befehl `passwd BENUTZERNAME` setzen, um den Benutzer aktiv zu machen.
- Überprüfen Sie die Benutzerinformationen mit dem Befehl `id BENUTZERNAME`, um sicherzustellen, dass der Benutzer korrekt erstellt wurde und die richtigen Gruppenmitgliedschaften hat.
- Verwenden Sie die Option `-d`, um ein benutzerdefiniertes Heimatverzeichnis anzugeben, falls das Standardverzeichnis nicht verwendet werden soll.
- Es ist eine gute Praxis, Kommentare mit der `-c`-Option hinzuzufügen, um die Benutzerverwaltung zu erleichtern und die Identität der Benutzer klarzustellen.