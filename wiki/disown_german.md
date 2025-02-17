# [Linux] Bash disown Verwendung: Prozesse im Hintergrund verwalten

## Übersicht
Der Befehl `disown` wird in der Bash verwendet, um einen laufenden Hintergrundprozess von der aktuellen Shell zu trennen. Dadurch wird der Prozess nicht mehr an die Shell gebunden, was bedeutet, dass er weiterläuft, auch wenn die Shell geschlossen wird.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
disown [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`: Verhindert, dass die angegebene Job-ID oder der Prozess von der Shell beendet wird, wenn die Shell geschlossen wird.
- `-a`: Wendet den Befehl auf alle Jobs an, die in der aktuellen Shell laufen.
- `-r`: Wendet den Befehl nur auf die laufenden Jobs an.

## Häufige Beispiele

1. **Einen Job im Hintergrund starten und disown verwenden:**
   ```bash
   sleep 300 &
   disown
   ```
   In diesem Beispiel wird der `sleep`-Befehl im Hintergrund gestartet und anschließend von der Shell getrennt.

2. **Einen bestimmten Job disownen:**
   ```bash
   sleep 300 &
   disown %1
   ```
   Hier wird der erste Hintergrundjob (`%1`) von der Shell getrennt.

3. **Alle Jobs disownen:**
   ```bash
   disown -a
   ```
   Mit diesem Befehl werden alle laufenden Hintergrundjobs von der Shell getrennt.

## Tipps
- Verwenden Sie `jobs`, um eine Liste aller Hintergrundjobs anzuzeigen, bevor Sie `disown` verwenden.
- Seien Sie vorsichtig beim Disownen von Prozessen, die möglicherweise wichtige Ausgaben erzeugen, da Sie diese nicht mehr sehen können, wenn die Shell geschlossen wird.
- Nutzen Sie `disown -h`, wenn Sie einen Job vor dem Schließen der Shell schützen möchten, ohne ihn zu trennen.