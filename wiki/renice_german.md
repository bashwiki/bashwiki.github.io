# [Linux] Bash renice Verwendung: Ändert die Priorität von Prozessen

## Übersicht
Der Befehl `renice` wird verwendet, um die Priorität von laufenden Prozessen in einem Linux- oder Unix-System zu ändern. Mit `renice` können Sie die CPU-Zuteilung für Prozesse anpassen, um sicherzustellen, dass wichtige Anwendungen mehr Ressourcen erhalten als weniger wichtige.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
renice [Optionen] [Wert] [PID...]
```

Hierbei steht `[Wert]` für die neue Priorität, die Sie dem Prozess zuweisen möchten, und `[PID...]` für die Prozess-ID(en) der Prozesse, deren Priorität geändert werden soll.

## Häufige Optionen
- `-n, --priority`: Gibt den neuen Prioritätswert an. Der Wert kann zwischen -20 (höchste Priorität) und 19 (niedrigste Priorität) liegen.
- `-p, --pid`: Gibt die Prozess-ID an, für die die Priorität geändert werden soll.
- `-g, --pgroup`: Ändert die Priorität aller Prozesse in einer bestimmten Prozessgruppe.
- `-u, --user`: Ändert die Priorität aller Prozesse eines bestimmten Benutzers.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `renice`:

1. Ändern der Priorität eines Prozesses mit der PID 1234 auf 10:

   ```bash
   renice 10 -p 1234
   ```

2. Ändern der Priorität aller Prozesse eines bestimmten Benutzers (z. B. `username`) auf 5:

   ```bash
   renice 5 -u username
   ```

3. Ändern der Priorität aller Prozesse in einer bestimmten Prozessgruppe (z. B. Gruppe 5678) auf -5:

   ```bash
   renice -5 -g 5678
   ```

4. Überprüfen der aktuellen Priorität eines Prozesses (z. B. PID 1234) vor der Änderung:

   ```bash
   ps -o pid,ni,cmd -p 1234
   ```

## Tipps
- Verwenden Sie `renice` mit Bedacht, da das Setzen einer hohen Priorität für einen Prozess andere Prozesse negativ beeinflussen kann.
- Überprüfen Sie regelmäßig die Prioritäten Ihrer Prozesse mit dem Befehl `ps`, um sicherzustellen, dass alles reibungslos läuft.
- Um die Auswirkungen von Änderungen zu testen, können Sie die Priorität eines Prozesses vor und nach der Änderung vergleichen.