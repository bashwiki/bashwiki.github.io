# [리눅스] Bash renice 사용법

## Übersicht
Der Befehl `renice` wird in Unix-ähnlichen Betriebssystemen verwendet, um die Priorität eines laufenden Prozesses zu ändern. Die Priorität eines Prozesses bestimmt, wie viel CPU-Zeit er im Vergleich zu anderen Prozessen erhält. Ein niedrigerer Wert bedeutet eine höhere Priorität, während ein höherer Wert eine niedrigere Priorität anzeigt. Mit `renice` können Sie die Systemressourcen effizienter verwalten, indem Sie Prozessen, die weniger wichtig sind, eine niedrigere Priorität zuweisen.

## Verwendung
Die grundlegende Syntax des `renice`-Befehls lautet:

```bash
renice [OPTIONEN] NEUER_WERT [PID...]
```

### Häufige Optionen:
- `-n`, `--priority NEUER_WERT`: Gibt den neuen Prioritätswert an. Der Wert kann zwischen -20 (höchste Priorität) und 19 (niedrigste Priorität) liegen.
- `-p`, `--pid`: Gibt die Prozess-ID (PID) des Prozesses an, dessen Priorität geändert werden soll.
- `-g`, `--pgrp`: Ändert die Priorität aller Prozesse in einer bestimmten Prozessgruppe.
- `-u`, `--user`: Ändert die Priorität aller Prozesse eines bestimmten Benutzers.

## Beispiele
### Beispiel 1: Ändern der Priorität eines einzelnen Prozesses
Um die Priorität eines Prozesses mit der PID 1234 auf 10 zu ändern, verwenden Sie den folgenden Befehl:

```bash
renice -n 10 -p 1234
```

### Beispiel 2: Ändern der Priorität aller Prozesse eines Benutzers
Um die Priorität aller Prozesse eines Benutzers mit dem Benutzernamen "benutzername" auf 5 zu setzen, verwenden Sie:

```bash
renice -n 5 -u benutzername
```

## Tipps
- Seien Sie vorsichtig beim Ändern der Priorität von Prozessen, insbesondere wenn Sie die Priorität auf einen niedrigeren Wert setzen, da dies die Systemleistung beeinträchtigen kann.
- Um die aktuelle Priorität eines Prozesses zu überprüfen, können Sie den Befehl `ps` verwenden, z.B. `ps -o pid,ni,cmd` zeigt die PID, die nice-Werte und den Befehl an.
- Um die Berechtigung zum Ändern der Priorität eines Prozesses zu erhalten, müssen Sie möglicherweise Root-Rechte haben, insbesondere wenn Sie die Priorität eines Prozesses erhöhen möchten.