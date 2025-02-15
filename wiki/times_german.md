# [리눅스] Bash times 사용법

## Übersicht
Der Befehl `times` in Bash wird verwendet, um die Gesamtzeit anzuzeigen, die der aktuelle Shell-Prozess sowie alle untergeordneten Prozesse für die Ausführung von Benutzerskripten und -befehlen benötigt haben. Der Befehl gibt die CPU-Zeit in Sekunden aus, die für die Ausführung von Prozessen verwendet wurde, und ist besonders nützlich für Entwickler und Ingenieure, die die Leistung ihrer Skripte und Programme analysieren möchten.

## Verwendung
Die grundlegende Syntax des Befehls `times` ist sehr einfach:

```bash
times
```

Es gibt keine speziellen Optionen oder Argumente, die mit dem Befehl verwendet werden können. Wenn `times` ohne Argumente aufgerufen wird, gibt es die CPU-Zeit für den aktuellen Shell-Prozess und alle untergeordneten Prozesse aus.

## Beispiele
Hier sind einige praktische Beispiele, wie man den Befehl `times` verwenden kann:

### Beispiel 1: Einfache Verwendung
Um die CPU-Zeit für den aktuellen Shell-Prozess anzuzeigen, geben Sie einfach den Befehl `times` ein:

```bash
# Führen Sie einige Befehle aus
sleep 2
ls -l

# Zeigen Sie die CPU-Zeit an
times
```

Die Ausgabe könnte etwa so aussehen:

```
   user     system      elapsed
   0.002     0.001      2.004
```

### Beispiel 2: Verwendung in einem Skript
Sie können den Befehl `times` auch in einem Bash-Skript verwenden, um die Ausführungszeit von Befehlen zu messen:

```bash
#!/bin/bash

# Skriptbeginn
echo "Starte Skript..."

# Führen Sie einige zeitaufwendige Befehle aus
sleep 3
find / -name "*.txt" > /dev/null

# Zeigen Sie die CPU-Zeit an
times
echo "Skript beendet."
```

## Tipps
- Verwenden Sie `times` am Ende eines Skripts oder nach einer Reihe von Befehlen, um eine präzise Messung der CPU-Zeit zu erhalten.
- Beachten Sie, dass `times` nur die CPU-Zeit anzeigt, nicht die Wandzeit. Dies bedeutet, dass es die Zeit misst, die die CPU tatsächlich mit der Ausführung von Prozessen verbracht hat, und nicht die gesamte Zeit, die vergangen ist.
- Um die Leistung Ihrer Skripte zu optimieren, können Sie `times` in Kombination mit anderen Befehlen wie `time` verwenden, um detailliertere Informationen über die Ausführungszeiten zu erhalten.