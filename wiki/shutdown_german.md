# [리눅스] Bash shutdown 사용법

## Übersicht
Der Befehl `shutdown` wird in Unix-ähnlichen Betriebssystemen verwendet, um das System sicher herunterzufahren oder neu zu starten. Er ermöglicht es Administratoren, das System zu einem bestimmten Zeitpunkt oder nach einer bestimmten Zeitspanne auszuschalten, was besonders nützlich ist, um Datenverlust zu vermeiden und sicherzustellen, dass alle Prozesse ordnungsgemäß beendet werden.

## Verwendung
Die grundlegende Syntax des `shutdown`-Befehls lautet:

```bash
shutdown [OPTIONEN] [ZEIT] [NACHRICHT]
```

### Häufige Optionen:
- `-h` oder `--halt`: Fährt das System herunter und schaltet es aus.
- `-r` oder `--reboot`: Startet das System nach dem Herunterfahren neu.
- `-P` oder `--poweroff`: Schaltet das System aus (dies ist oft die Standardaktion).
- `now`: Fährt das System sofort herunter.
- `+m`: Gibt an, dass das System in `m` Minuten heruntergefahren werden soll (z.B. `+5` für 5 Minuten).
- `hh:mm`: Gibt die Uhrzeit an, zu der das System heruntergefahren werden soll (z.B. `23:00` für 23 Uhr).

## Beispiele
1. Um das System sofort herunterzufahren, verwenden Sie den folgenden Befehl:

   ```bash
   shutdown now
   ```

2. Um das System in 10 Minuten herunterzufahren und eine Nachricht an alle Benutzer zu senden, verwenden Sie:

   ```bash
   shutdown +10 "Das System wird in 10 Minuten heruntergefahren."
   ```

## Tipps
- Verwenden Sie den Befehl `shutdown -c`, um einen geplanten Shutdown abzubrechen, falls Sie es sich anders überlegen.
- Informieren Sie Benutzer über bevorstehende Shutdowns, indem Sie eine Nachricht senden, um Datenverlust zu vermeiden.
- Testen Sie den Befehl in einer sicheren Umgebung, bevor Sie ihn auf Produktionssystemen verwenden, um sicherzustellen, dass Sie die gewünschten Ergebnisse erzielen.