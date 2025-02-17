# [Linux] Bash su Verwendung: Benutzerwechsel im Terminal

## Übersicht
Der `su`-Befehl (substitute user) wird verwendet, um den aktuellen Benutzer im Terminal zu wechseln. Standardmäßig wechselt er zu einem anderen Benutzer, oft zum Superuser (root), was Administratorrechte gewährt.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
su [Optionen] [Benutzername]
```

## Häufige Optionen
- `-l` oder `--login`: Startet eine neue Login-Sitzung für den angegebenen Benutzer.
- `-c`: Führt einen Befehl als der angegebene Benutzer aus.
- `-s`: Gibt die Shell an, die verwendet werden soll.

## Häufige Beispiele
Um zu einem anderen Benutzer zu wechseln, verwenden Sie:

```bash
su benutzername
```

Um zu root zu wechseln und eine Login-Sitzung zu starten:

```bash
su -l
```

Um einen spezifischen Befehl als ein anderer Benutzer auszuführen:

```bash
su -c 'Befehl' benutzername
```

Um die Shell für den Benutzer zu ändern:

```bash
su -s /bin/bash benutzername
```

## Tipps
- Verwenden Sie `su -l`, um sicherzustellen, dass die Umgebungsvariablen des neuen Benutzers geladen werden.
- Seien Sie vorsichtig beim Arbeiten als root, um unbeabsichtigte Änderungen am System zu vermeiden.
- Nutzen Sie `sudo`, wenn Sie nur gelegentlich Administratorrechte benötigen, um die Sicherheit zu erhöhen.