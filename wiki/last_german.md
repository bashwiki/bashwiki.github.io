# [Linux] Bash last Verwendung: Zeigt die letzten Anmeldungen an

## Übersicht
Der Befehl `last` wird in Bash verwendet, um die letzten Anmeldungen von Benutzern auf einem System anzuzeigen. Er liest die Datei `/var/log/wtmp`, in der alle Anmelde- und Abmeldeereignisse protokolliert werden.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
last [Optionen] [Argumente]
```

## Häufige Optionen
- `-a`: Zeigt die Hostnamen der Benutzer an.
- `-n [anzahl]`: Gibt die Anzahl der letzten Anmeldungen an, die angezeigt werden sollen.
- `-R`: Unterdrückt die Anzeige von Hostnamen.
- `-x`: Zeigt auch Systemstart- und Shutdown-Ereignisse an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des Befehls `last`:

1. **Alle letzten Anmeldungen anzeigen:**

   ```bash
   last
   ```

2. **Die letzten 5 Anmeldungen anzeigen:**

   ```bash
   last -n 5
   ```

3. **Anmeldungen mit Hostnamen anzeigen:**

   ```bash
   last -a
   ```

4. **Anmeldungen ohne Hostnamen anzeigen:**

   ```bash
   last -R
   ```

5. **Systemstart- und Shutdown-Ereignisse anzeigen:**

   ```bash
   last -x
   ```

## Tipps
- Verwenden Sie `last -n [anzahl]`, um die Ausgabe zu begrenzen und nur die neuesten Anmeldungen zu sehen.
- Kombinieren Sie `last` mit `grep`, um nach einem bestimmten Benutzer zu suchen, z.B. `last | grep benutzername`.
- Überprüfen Sie regelmäßig die Anmeldungen, um unautorisierte Zugriffe zu erkennen.