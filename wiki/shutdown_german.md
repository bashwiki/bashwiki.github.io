# [Linux] Bash shutdown Verwendung: System herunterfahren oder neu starten

## Übersicht
Der Befehl `shutdown` wird verwendet, um ein Linux-System sicher herunterzufahren oder neu zu starten. Er ermöglicht es Benutzern, das System zu einem bestimmten Zeitpunkt oder nach einer bestimmten Zeitspanne auszuschalten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
shutdown [Optionen] [Zeit] [Nachricht]
```

## Häufige Optionen
- `-h`: Fährt das System herunter.
- `-r`: Startet das System neu.
- `-P`: Schaltet das System aus (verfügbar in einigen Distributionen).
- `now`: Führt den Shutdown sofort aus.
- `+m`: Fährt das System nach m Minuten herunter.
- `hh:mm`: Fährt das System um die angegebene Uhrzeit herunter.

## Häufige Beispiele

1. **System sofort herunterfahren:**
   ```bash
   shutdown -h now
   ```

2. **System in 10 Minuten herunterfahren:**
   ```bash
   shutdown -h +10
   ```

3. **System um 22:00 Uhr neu starten:**
   ```bash
   shutdown -r 22:00
   ```

4. **Nachricht an alle Benutzer senden:**
   ```bash
   shutdown -h now "Das System wird heruntergefahren für Wartungsarbeiten."
   ```

5. **System sofort neu starten:**
   ```bash
   shutdown -r now
   ```

## Tipps
- Verwenden Sie `shutdown -h now`, um sicherzustellen, dass alle Prozesse ordnungsgemäß beendet werden, bevor das System heruntergefahren wird.
- Informieren Sie andere Benutzer über geplante Herunterfahrvorgänge, indem Sie eine Nachricht mit dem Befehl senden.
- Nutzen Sie `shutdown -c`, um einen geplanten Shutdown abzubrechen, falls nötig.