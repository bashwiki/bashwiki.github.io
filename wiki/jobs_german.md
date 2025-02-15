# [리눅스] Bash jobs 사용법

## Übersicht
Der Befehl `jobs` in Bash wird verwendet, um eine Liste der aktuellen Hintergrund- und gestoppten Prozesse anzuzeigen, die von der aktuellen Shell-Instanz verwaltet werden. Dies ist besonders nützlich, um den Status von Prozessen zu überwachen, die im Hintergrund laufen, oder um festzustellen, ob ein Prozess angehalten wurde.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
jobs [OPTIONEN]
```

### Häufige Optionen
- `-l`: Zeigt die Prozess-IDs (PIDs) der Jobs an.
- `-n`: Listet nur die Jobs auf, die seit der letzten Anzeige geändert wurden.
- `-p`: Gibt nur die PIDs der Jobs aus.

Wenn keine Optionen angegeben werden, zeigt `jobs` eine einfache Liste der aktuellen Jobs mit ihrem Status (gestoppt oder laufend) an.

## Beispiele
### Beispiel 1: Grundlegende Verwendung
Um alle aktuellen Jobs anzuzeigen, geben Sie einfach den Befehl `jobs` ein:

```bash
jobs
```

Die Ausgabe könnte wie folgt aussehen:

```
[1]+  1234 Stopped                 nano
[2]-  5678 Running                 sleep 100 &
```

### Beispiel 2: Jobs mit Prozess-IDs anzeigen
Um die Prozess-IDs der Jobs anzuzeigen, verwenden Sie die `-l` Option:

```bash
jobs -l
```

Die Ausgabe könnte so aussehen:

```
[1]+  1234 Stopped                 nano
[2]-  5678 Running                 sleep 100 &
```

## Tipps
- Verwenden Sie `jobs -l`, um schnell die Prozess-IDs zu erhalten, die Sie möglicherweise für andere Befehle wie `kill` benötigen.
- Wenn Sie mehrere Jobs haben, können Sie den Status jedes Jobs leicht überwachen, um sicherzustellen, dass sie wie erwartet laufen.
- Denken Sie daran, dass `jobs` nur die Jobs anzeigt, die von der aktuellen Shell gestartet wurden. Wenn Sie eine neue Shell oder ein neues Terminalfenster öffnen, sind diese Jobs nicht sichtbar.