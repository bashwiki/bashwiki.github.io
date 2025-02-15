# [리눅스] Bash nice 사용법

## Übersicht
Der Befehl `nice` in Bash wird verwendet, um die Priorität eines Prozesses zu steuern, der im Hintergrund ausgeführt wird. Die Hauptfunktion von `nice` besteht darin, die CPU-Zeit, die einem Prozess zugewiesen wird, zu beeinflussen, indem die "Nettigkeit" (nice value) des Prozesses geändert wird. Ein höherer Wert bedeutet eine niedrigere Priorität, während ein niedrigerer Wert eine höhere Priorität bedeutet. Dies ist besonders nützlich, um sicherzustellen, dass wichtige Prozesse genügend Ressourcen erhalten, während weniger wichtige Prozesse im Hintergrund laufen.

## Verwendung
Die grundlegende Syntax des `nice`-Befehls lautet:

```bash
nice [OPTIONEN] [Befehl [Argumente...]]
```

### Häufige Optionen:
- `-n, --adjustment=N`: Legt den Nettigkeitswert fest. Der Standardwert ist 10. Ein negativer Wert (z.B. -5) erhöht die Priorität, während ein positiver Wert (z.B. 15) die Priorität verringert.
- `--help`: Zeigt eine Hilfe-Seite mit Informationen zur Verwendung des Befehls an.
- `--version`: Gibt die Versionsnummer des `nice`-Befehls aus.

## Beispiele
### Beispiel 1: Standard-Nettigkeitswert verwenden
Um ein Programm mit dem Standard-Nettigkeitswert von 10 auszuführen, verwenden Sie den folgenden Befehl:

```bash
nice my_program
```

### Beispiel 2: Nettigkeitswert anpassen
Um ein Programm mit einer erhöhten Priorität (Nettigkeitswert von -5) auszuführen, verwenden Sie:

```bash
nice -n -5 my_program
```

In diesem Beispiel wird `my_program` mit einer höheren Priorität gestartet, was bedeutet, dass es mehr CPU-Ressourcen erhält als Prozesse mit einem höheren Nettigkeitswert.

## Tipps
- Verwenden Sie `nice`, um ressourcenintensive Prozesse zu starten, ohne die Leistung anderer wichtiger Anwendungen zu beeinträchtigen.
- Überprüfen Sie den aktuellen Nettigkeitswert eines laufenden Prozesses mit dem Befehl `ps -o pid,ni,cmd`.
- Seien Sie vorsichtig beim Festlegen negativer Nettigkeitswerte, da dies die Systemleistung beeinträchtigen kann, wenn zu viele Prozesse mit hoher Priorität gleichzeitig ausgeführt werden.
- Nutzen Sie `renice`, um die Nettigkeit eines bereits laufenden Prozesses zu ändern, falls erforderlich.