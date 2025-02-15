# [리눅스] Bash wait 사용법

## Übersicht
Der `wait` Befehl in Bash wird verwendet, um auf die Beendigung eines oder mehrerer Hintergrundprozesse zu warten. Der Hauptzweck des Befehls besteht darin, sicherzustellen, dass ein Skript oder ein Befehl erst dann fortgesetzt wird, wenn die angegebenen Prozesse abgeschlossen sind. Dies ist besonders nützlich in Skripten, die mehrere Prozesse gleichzeitig ausführen und auf deren Ergebnisse angewiesen sind.

## Verwendung
Die grundlegende Syntax des `wait` Befehls lautet:

```bash
wait [PID...]
```

- **PID**: Die Prozess-ID eines oder mehrerer Hintergrundprozesse, auf die gewartet werden soll. Wenn keine PID angegeben wird, wartet `wait` auf alle Hintergrundprozesse, die im aktuellen Shell-Skript oder in der aktuellen Shell-Session ausgeführt werden.

## Beispiele

### Beispiel 1: Warten auf einen spezifischen Prozess
In diesem Beispiel starten wir einen Hintergrundprozess und verwenden `wait`, um auf dessen Beendigung zu warten.

```bash
#!/bin/bash

# Starte einen Hintergrundprozess
sleep 5 &

# Speichere die PID des Hintergrundprozesses
PID=$!

echo "Warte auf den Prozess mit PID $PID..."

# Warte auf den Hintergrundprozess
wait $PID

echo "Der Prozess mit PID $PID ist beendet."
```

### Beispiel 2: Warten auf mehrere Prozesse
In diesem Beispiel starten wir mehrere Hintergrundprozesse und warten, bis alle abgeschlossen sind.

```bash
#!/bin/bash

# Starte mehrere Hintergrundprozesse
sleep 3 &
PID1=$!
sleep 4 &
PID2=$!

echo "Warte auf die Prozesse mit PIDs $PID1 und $PID2..."

# Warte auf alle Hintergrundprozesse
wait $PID1
wait $PID2

echo "Alle Prozesse sind beendet."
```

## Tipps
- Verwenden Sie `wait` in Skripten, um sicherzustellen, dass alle Hintergrundprozesse abgeschlossen sind, bevor das Skript fortfährt oder beendet wird.
- Wenn Sie `wait` ohne Argumente verwenden, wartet es auf alle Hintergrundprozesse, was nützlich sein kann, wenn Sie mehrere Prozesse gleichzeitig ausführen.
- Achten Sie darauf, die Prozess-IDs (PIDs) zu speichern, wenn Sie mehrere Prozesse starten, um gezielt auf bestimmte Prozesse warten zu können.
- Der `wait` Befehl gibt den Exit-Status des Prozesses zurück, auf den gewartet wurde. Dies kann nützlich sein, um den Erfolg oder Misserfolg eines Prozesses zu überprüfen.