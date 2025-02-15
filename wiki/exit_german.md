# [리눅스] Bash exit 사용법

## Übersicht
Der Befehl `exit` wird in Bash-Skripten und interaktiven Shell-Sitzungen verwendet, um die aktuelle Shell oder das Skript zu beenden. Der Hauptzweck des `exit`-Befehls besteht darin, einen Exit-Status zurückzugeben, der angibt, ob das Skript erfolgreich ausgeführt wurde oder ob ein Fehler aufgetreten ist. Ein Exit-Status von `0` bedeutet in der Regel Erfolg, während ein Wert ungleich `0` auf einen Fehler hinweist.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
exit [N]
```

Hierbei ist `N` eine optionale Ganzzahl, die den Exit-Status angibt. Wenn kein Wert angegeben wird, wird der Exit-Status des letzten ausgeführten Befehls verwendet.

### Gemeinsame Optionen
- `N`: Ein ganzzahliger Wert, der den Exit-Status angibt. Der Wert sollte im Bereich von `0` bis `255` liegen.

## Beispiele
### Beispiel 1: Einfaches Skript beenden
In einem Bash-Skript können Sie den `exit`-Befehl verwenden, um das Skript mit einem bestimmten Exit-Status zu beenden.

```bash
#!/bin/bash

echo "Das Skript wird jetzt beendet."
exit 0
```

In diesem Beispiel wird das Skript mit dem Exit-Status `0` beendet, was Erfolg bedeutet.

### Beispiel 2: Fehlerbehandlung
Sie können den `exit`-Befehl auch verwenden, um bei einem Fehler einen anderen Exit-Status zurückzugeben.

```bash
#!/bin/bash

if [ ! -f "meine_datei.txt" ]; then
    echo "Fehler: Datei nicht gefunden!"
    exit 1
fi

echo "Datei gefunden."
exit 0
```

In diesem Beispiel wird das Skript mit dem Exit-Status `1` beendet, wenn die Datei nicht gefunden wird.

## Tipps
- Verwenden Sie `exit 0`, um anzuzeigen, dass Ihr Skript erfolgreich abgeschlossen wurde.
- Verwenden Sie nicht nullbasierte Exit-Codes (z.B. `exit 1`, `exit 2`), um verschiedene Fehlerarten zu kennzeichnen. Dies kann bei der Fehlersuche hilfreich sein.
- Achten Sie darauf, dass der Exit-Status im Bereich von `0` bis `255` bleibt, da Werte außerhalb dieses Bereichs möglicherweise unerwartete Ergebnisse liefern.
- In interaktiven Shell-Sitzungen können Sie `exit` einfach eingeben, um die Sitzung zu beenden.