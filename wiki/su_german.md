# [리눅스] Bash su 사용법

## Übersicht
Der Befehl `su` (substitute user) wird in der Bash verwendet, um den Benutzerkontext zu wechseln. Primär wird er eingesetzt, um sich als ein anderer Benutzer, häufig als root, anzumelden. Dies ist besonders nützlich für Systemadministratoren, die administrative Aufgaben ausführen müssen, ohne sich abmelden und erneut anmelden zu müssen.

## Verwendung
Die grundlegende Syntax des `su`-Befehls lautet:

```bash
su [OPTION] [BENUTZERNAME]
```

### Häufige Optionen:
- `-` oder `--login`: Wechselt in die Umgebung des angegebenen Benutzers, als ob dieser sich gerade angemeldet hätte.
- `-c`: Führt einen Befehl als der angegebene Benutzer aus.
- `-s`: Gibt die Shell an, die verwendet werden soll.

## Beispiele
### Beispiel 1: Wechsel zu root
Um sich als root-Benutzer anzumelden, verwenden Sie einfach:

```bash
su -
```

Nach der Eingabe dieses Befehls werden Sie aufgefordert, das Passwort des root-Benutzers einzugeben. Nach erfolgreicher Eingabe haben Sie Zugriff auf alle administrativen Funktionen.

### Beispiel 2: Ausführen eines Befehls als ein anderer Benutzer
Um einen spezifischen Befehl als ein anderer Benutzer auszuführen, verwenden Sie die `-c`-Option:

```bash
su -c 'ls /root' benutzername
```

In diesem Beispiel wird der Befehl `ls /root` als der angegebene Benutzer ausgeführt, und Sie müssen das Passwort dieses Benutzers eingeben.

## Tipps
- Verwenden Sie `su -`, um sicherzustellen, dass Sie die vollständige Umgebung des Zielbenutzers erhalten, was oft für die Ausführung von Befehlen erforderlich ist.
- Seien Sie vorsichtig beim Arbeiten als root, da Sie unbeabsichtigt kritische Systemdateien ändern oder löschen können.
- Wenn Sie häufig zwischen Benutzern wechseln müssen, könnte es sinnvoll sein, `sudo` zu verwenden, da es eine sicherere und flexiblere Möglichkeit bietet, Berechtigungen zu verwalten.