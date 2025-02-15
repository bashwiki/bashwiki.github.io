# [리눅스] Bash users 사용법

## Übersicht
Der Befehl `users` wird in der Bash verwendet, um die aktuell angemeldeten Benutzer im System anzuzeigen. Er gibt eine Liste der Benutzernamen zurück, die zurzeit aktiv sind, und ist besonders nützlich für Systemadministratoren und Entwickler, die einen Überblick über die Benutzeraktivität auf einem Server oder in einer Umgebung erhalten möchten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
users
```

Es gibt keine speziellen Optionen für den Befehl `users`, da er einfach die Benutzernamen der aktuell angemeldeten Benutzer auflistet. Der Befehl gibt die Namen in einer einzigen Zeile zurück, wobei die Namen durch Leerzeichen getrennt sind.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `users`:

1. **Einfacher Aufruf**:
   Um die aktuell angemeldeten Benutzer anzuzeigen, geben Sie einfach den Befehl ein:

   ```bash
   users
   ```

   Beispielausgabe:
   ```
   alice bob charlie
   ```

   In diesem Beispiel sind die Benutzer `alice`, `bob` und `charlie` derzeit im System angemeldet.

2. **Verwendung in einem Skript**:
   Sie können den Befehl `users` auch in einem Bash-Skript verwenden, um die Benutzeraktivität zu protokollieren:

   ```bash
   #!/bin/bash
   echo "Aktuell angemeldete Benutzer: $(users)" >> benutzerprotokoll.txt
   ```

   Dieses Skript fügt die Liste der angemeldeten Benutzer in eine Datei namens `benutzerprotokoll.txt` ein.

## Tipps
- Der Befehl `users` ist besonders nützlich in Kombination mit anderen Befehlen wie `who` oder `w`, die zusätzliche Informationen über die Benutzeraktivität bereitstellen.
- Verwenden Sie `users` in Skripten, um die Benutzeraktivität zu überwachen oder zu protokollieren, was bei der Fehlersuche oder Systemüberwachung hilfreich sein kann.
- Beachten Sie, dass der Befehl nur die Benutzer anzeigt, die aktuell angemeldet sind, und nicht die, die sich möglicherweise in der Vergangenheit angemeldet haben oder die Sitzung beendet haben.