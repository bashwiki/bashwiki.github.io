# [리눅스] Bash last 사용법

## Überblick
Der Befehl `last` wird in Unix-ähnlichen Betriebssystemen verwendet, um eine Liste der letzten Benutzeranmeldungen anzuzeigen. Er liest die Datei `/var/log/wtmp`, die Informationen über Anmeldungen, Abmeldungen und Systemstarts speichert. Der Hauptzweck des Befehls ist es, Administratoren und Benutzern zu helfen, die Anmeldeaktivitäten auf einem System zu überwachen und zu analysieren.

## Verwendung
Die grundlegende Syntax des Befehls `last` lautet:

```bash
last [OPTIONEN] [BENUTZER]
```

### Häufige Optionen
- `-a`: Zeigt die Hostnamen der Benutzer an, die sich angemeldet haben.
- `-n NUM`: Gibt die letzten NUM Anmeldungen an. Wenn NUM nicht angegeben ist, werden standardmäßig die letzten 10 Anmeldungen angezeigt.
- `-x`: Zeigt auch Systemstarts und -abschaltungen an.
- `-R`: Unterdrückt die Anzeige der Hostnamen.

## Beispiele
### Beispiel 1: Letzte Anmeldungen anzeigen
Um die letzten 10 Anmeldungen anzuzeigen, verwenden Sie einfach:

```bash
last
```

### Beispiel 2: Letzte Anmeldungen eines bestimmten Benutzers
Um die letzten Anmeldungen eines bestimmten Benutzers, z.B. `alice`, anzuzeigen, verwenden Sie:

```bash
last alice
```

### Beispiel 3: Letzte 5 Anmeldungen mit Hostnamen
Um die letzten 5 Anmeldungen anzuzeigen und die Hostnamen einzuschließen, verwenden Sie:

```bash
last -a -n 5
```

## Tipps
- Verwenden Sie die Option `-x`, um auch Systemereignisse wie Neustarts und Herunterfahren zu überwachen. Dies kann hilfreich sein, um zu verstehen, wann das System zuletzt gestartet oder heruntergefahren wurde.
- Beachten Sie, dass die Informationen in der Datei `/var/log/wtmp` gespeichert werden. Wenn diese Datei gelöscht oder beschädigt wird, gehen die Anmeldeinformationen verloren.
- Um die Ausgabe von `last` besser lesbar zu machen, können Sie die Ergebnisse durch `less` oder `more` pipen, z.B. `last | less`.