# [리눅스] Bash who 사용법

## Übersicht
Der Befehl `who` wird in der Bash verwendet, um Informationen über die Benutzer anzuzeigen, die derzeit am System angemeldet sind. Er gibt eine Liste der aktiven Benutzer, deren Anmeldezeiten und die Terminal-Sitzungen, die sie verwenden. Dieser Befehl ist nützlich für Systemadministratoren und Entwickler, um den Status der Benutzeranmeldungen auf einem System zu überwachen.

## Verwendung
Die grundlegende Syntax des Befehls `who` lautet:

```bash
who [OPTIONEN]
```

### Häufige Optionen
- `-a`: Zeigt alle verfügbaren Informationen an, einschließlich der Anmeldezeiten und der Benutzeraktivität.
- `-b`: Gibt die Zeit der letzten Systemstartmeldung aus.
- `-q`: Zeigt nur die angemeldeten Benutzer und die Anzahl der Benutzer an.
- `--help`: Zeigt eine Hilfemeldung mit den verfügbaren Optionen an.

## Beispiele
### Beispiel 1: Grundlegende Benutzerliste
Um eine einfache Liste der aktuell angemeldeten Benutzer anzuzeigen, verwenden Sie einfach den Befehl:

```bash
who
```

### Beispiel 2: Detaillierte Informationen anzeigen
Um detaillierte Informationen über die angemeldeten Benutzer zu erhalten, einschließlich Anmeldezeiten, verwenden Sie die `-a` Option:

```bash
who -a
```

## Tipps
- Verwenden Sie `who -q`, um schnell die Anzahl der angemeldeten Benutzer zu überprüfen, ohne eine vollständige Liste anzuzeigen.
- Kombinieren Sie den `who` Befehl mit anderen Befehlen wie `grep`, um spezifische Benutzer zu finden. Zum Beispiel:

```bash
who | grep username
```

Dieser Befehl filtert die Ausgabe von `who`, um nur Informationen über den Benutzer mit dem Namen "username" anzuzeigen.