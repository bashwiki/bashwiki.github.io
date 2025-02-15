# [리눅스] Bash disown 사용법

## Übersicht
Der Befehl `disown` in Bash wird verwendet, um einen laufenden Hintergrundprozess von der aktuellen Shell zu trennen. Dies bedeutet, dass der Prozess nicht mehr mit der Shell verbunden ist, die ihn gestartet hat, und somit nicht mehr durch das Schließen der Shell beendet wird. Der Hauptzweck von `disown` ist es, sicherzustellen, dass ein Prozess weiterhin läuft, selbst wenn die Shell, die ihn gestartet hat, beendet wird.

## Verwendung
Die grundlegende Syntax des Befehls `disown` lautet:

```bash
disown [OPTION] [JOB_SPEC]
```

### Häufige Optionen:
- `-h`: Diese Option verhindert, dass die angegebene Aufgabe beim Schließen der Shell beendet wird, ohne sie vollständig von der Shell zu trennen.
- `-a`: Diese Option bewirkt, dass alle aktuellen Jobs von der Shell getrennt werden.
- `-r`: Diese Option listet nur die laufenden Jobs auf.

Wenn keine spezifische Job-Spezifikation angegeben wird, wird der letzte Hintergrundprozess standardmäßig verwendet.

## Beispiele
### Beispiel 1: Einen Hintergrundprozess disown
Angenommen, Sie haben einen langen Prozess gestartet, z.B. ein Skript, das im Hintergrund läuft:

```bash
./mein_script.sh &
```

Um diesen Prozess von der Shell zu trennen, verwenden Sie:

```bash
disown
```

### Beispiel 2: Alle Hintergrundprozesse disown
Wenn Sie mehrere Hintergrundprozesse haben und alle von der Shell trennen möchten, können Sie dies mit der Option `-a` tun:

```bash
disown -a
```

## Tipps
- Verwenden Sie `jobs`, um eine Liste aller Hintergrundjobs anzuzeigen, bevor Sie `disown` verwenden. Dies hilft Ihnen, den Überblick über die laufenden Prozesse zu behalten.
- Seien Sie vorsichtig beim Verwenden von `disown`, da Sie möglicherweise einen Prozess trennen, den Sie später wieder benötigen könnten. Überlegen Sie, ob Sie den Prozess stattdessen mit `bg` oder `fg` weiterverwenden möchten.
- Es ist ratsam, `disown` zu verwenden, wenn Sie sicher sind, dass Sie den Prozess nicht mehr überwachen müssen, da Sie keinen Zugriff mehr auf die Ausgabe oder den Status des Prozesses haben, nachdem er disowned wurde.