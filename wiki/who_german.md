# [Linux] Bash who Verwendung: Zeigt angemeldete Benutzer an

## Übersicht
Der Befehl `who` wird verwendet, um Informationen über die Benutzer anzuzeigen, die derzeit am System angemeldet sind. Er zeigt Details wie den Benutzernamen, das Terminal, die Anmeldezeit und die IP-Adresse oder den Hostnamen des Benutzers an.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
who [Optionen] [Argumente]
```

## Häufige Optionen
- `-b`: Zeigt die letzte Systemstartzeit an.
- `-q`: Gibt nur die angemeldeten Benutzernamen und die Anzahl der Benutzer aus.
- `-H`: Fügt eine Kopfzeile zu den Ausgaben hinzu.
- `--help`: Zeigt die Hilfeseite für den Befehl an.

## Häufige Beispiele

1. **Einfacher Aufruf von who**
   ```bash
   who
   ```

2. **Anzeigen der letzten Systemstartzeit**
   ```bash
   who -b
   ```

3. **Anzeigen der angemeldeten Benutzer mit Kopfzeile**
   ```bash
   who -H
   ```

4. **Anzeigen der Anzahl der angemeldeten Benutzer**
   ```bash
   who -q
   ```

## Tipps
- Verwenden Sie `who -H`, um die Ausgabe besser lesbar zu machen, insbesondere wenn Sie viele Benutzer haben.
- Kombinieren Sie `who` mit anderen Befehlen wie `grep`, um nach bestimmten Benutzern zu suchen.
- Nutzen Sie `man who`, um weitere Informationen und Optionen zu erhalten.