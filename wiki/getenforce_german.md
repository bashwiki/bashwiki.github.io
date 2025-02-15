# [리눅스] Bash getenforce 사용법

## Übersicht
Der Befehl `getenforce` wird in Linux-Systemen verwendet, um den aktuellen Status des SELinux (Security-Enhanced Linux) zu überprüfen. SELinux ist eine Sicherheitsarchitektur für Linux, die erweiterte Zugriffskontrollen bereitstellt. Der `getenforce`-Befehl gibt an, ob SELinux im Modus "Enforcing", "Permissive" oder "Disabled" läuft. Dies ist besonders wichtig für Systemadministratoren und Entwickler, die sicherstellen möchten, dass ihre Anwendungen in einer sicheren Umgebung betrieben werden.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
getenforce
```

Es sind keine speziellen Optionen erforderlich, da der Befehl einfach den aktuellen Status von SELinux zurückgibt. Die möglichen Rückgabewerte sind:

- `Enforcing`: SELinux ist aktiv und durchsetzt die Sicherheitsrichtlinien.
- `Permissive`: SELinux ist aktiv, aber es werden keine Richtlinien durchgesetzt; stattdessen werden nur Warnungen protokolliert.
- `Disabled`: SELinux ist deaktiviert.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `getenforce`:

1. **Überprüfen des SELinux-Status**:
   Um den aktuellen Status von SELinux zu überprüfen, geben Sie einfach den folgenden Befehl ein:

   ```bash
   getenforce
   ```

   Die Ausgabe könnte beispielsweise `Enforcing` sein, was bedeutet, dass SELinux aktiv ist und Richtlinien durchsetzt.

2. **Verwendung in einem Skript**:
   Sie können `getenforce` auch in einem Bash-Skript verwenden, um bestimmte Aktionen basierend auf dem SELinux-Status auszuführen. Hier ist ein einfaches Beispiel:

   ```bash
   #!/bin/bash

   status=$(getenforce)

   if [ "$status" == "Enforcing" ]; then
       echo "SELinux ist aktiv und durchsetzt Richtlinien."
   else
       echo "SELinux ist nicht im Enforcing-Modus."
   fi
   ```

## Tipps
- Überprüfen Sie regelmäßig den SELinux-Status, insbesondere nach Änderungen an der Systemkonfiguration oder nach der Installation neuer Software.
- Verwenden Sie den Befehl in Kombination mit anderen SELinux-Befehlen wie `setenforce`, um den Modus von SELinux zu ändern, falls erforderlich.
- Dokumentieren Sie Änderungen am SELinux-Status, um sicherzustellen, dass alle Teammitglieder über die Sicherheitsrichtlinien informiert sind.