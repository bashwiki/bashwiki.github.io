# [Linux] Bash-Benutzerbefehl: Benutzerinformationen anzeigen

## Übersicht
Der `users` Befehl zeigt die Benutzernamen der aktuell angemeldeten Benutzer auf dem System an. Dies ist nützlich, um schnell zu überprüfen, wer gerade eingeloggt ist.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
users [Optionen] [Argumente]
```

## Häufige Optionen
- `-n`: Zeigt die Anzahl der angemeldeten Benutzer an.
- `-r`: Gibt nur die Benutzernamen der Benutzer aus, die auf einer bestimmten Terminal-Sitzung angemeldet sind.

## Häufige Beispiele

1. **Einfaches Anzeigen der angemeldeten Benutzer:**

   ```bash
   users
   ```

2. **Anzeigen der Anzahl der angemeldeten Benutzer:**

   ```bash
   users -n
   ```

3. **Anzeigen der Benutzer auf einem bestimmten Terminal:**

   ```bash
   users -r
   ```

## Tipps
- Verwenden Sie `who` oder `w`, um detailliertere Informationen über die angemeldeten Benutzer zu erhalten, einschließlich ihrer Anmeldezeiten und aktiven Sitzungen.
- Der `users` Befehl ist besonders nützlich in Skripten, um die Benutzeraktivität zu überwachen.