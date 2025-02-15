# [리눅스] Bash cron 사용법

## Übersicht
Der Befehl `cron` ist ein Daemon in Unix-ähnlichen Betriebssystemen, der dazu dient, zeitgesteuerte Aufgaben (auch Cron-Jobs genannt) automatisch auszuführen. Er ermöglicht es Benutzern, Skripte oder Befehle zu bestimmten Zeiten oder in regelmäßigen Abständen auszuführen, ohne dass eine manuelle Intervention erforderlich ist. Dies ist besonders nützlich für Wartungsaufgaben, Backups oder regelmäßige Datenanalysen.

## Verwendung
Die grundlegende Syntax für die Verwendung von `cron` erfolgt über die Bearbeitung der Crontab-Datei. Um die Crontab für den aktuellen Benutzer zu bearbeiten, verwenden Sie den folgenden Befehl:

```bash
crontab -e
```

In der Crontab-Datei können Sie die Zeitpläne für Ihre Cron-Jobs festlegen. Die allgemeine Struktur eines Eintrags sieht folgendermaßen aus:

```
* * * * * Befehl
```

Die fünf Platzhalter stehen für:

- Minute (0-59)
- Stunde (0-23)
- Tag des Monats (1-31)
- Monat (1-12)
- Wochentag (0-7) (0 und 7 stehen für Sonntag)

Ein Beispiel für einen Cron-Job, der jeden Tag um 2 Uhr morgens ein Skript ausführt, könnte so aussehen:

```
0 2 * * * /pfad/zum/skript.sh
```

## Beispiele
Hier sind zwei praktische Beispiele für die Verwendung von `cron`:

1. **Tägliche Sicherung eines Verzeichnisses**:
   Um jeden Tag um 3 Uhr morgens ein Backup eines Verzeichnisses zu erstellen, fügen Sie Folgendes in die Crontab ein:

   ```
   0 3 * * * tar -czf /backup/verzeichnis_backup_$(date +\%Y\%m\%d).tar.gz /pfad/zum/verzeichnis
   ```

2. **Wöchentliche Systemupdates**:
   Um jeden Sonntag um 4 Uhr morgens Systemupdates durchzuführen, könnte der Cron-Job so aussehen:

   ```
   0 4 * * 0 apt-get update && apt-get upgrade -y
   ```

## Tipps
- **Testen Sie Ihre Skripte**: Stellen Sie sicher, dass Ihre Skripte manuell funktionieren, bevor Sie sie in einen Cron-Job einfügen.
- **Protokollierung**: Fügen Sie Protokollierungsbefehle hinzu, um die Ausgaben Ihrer Cron-Jobs zu überwachen. Zum Beispiel:

  ```
  0 2 * * * /pfad/zum/skript.sh >> /var/log/mein_cron.log 2>&1
  ```

- **Umgebungsvariablen**: Beachten Sie, dass die Umgebungsvariablen in Cron-Jobs möglicherweise anders sind als in Ihrer normalen Shell. Es kann hilfreich sein, die benötigten Variablen direkt im Skript zu setzen.
- **Verwenden Sie den Befehl `crontab -l`**: Dieser Befehl zeigt alle aktuellen Cron-Jobs für den Benutzer an, was nützlich ist, um sicherzustellen, dass alles korrekt eingerichtet ist.

Mit diesen Informationen sind Sie gut gerüstet, um `cron` effektiv zu nutzen und zeitgesteuerte Aufgaben in Ihrem System zu automatisieren.