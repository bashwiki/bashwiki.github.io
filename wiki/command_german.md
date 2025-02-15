# [리눅스] Bash command 사용법

## Übersicht
Der Befehl `command` in Bash wird verwendet, um eine bestimmte Aufgabe auszuführen, ohne dass die Shell die Aliase oder Funktionen berücksichtigt, die möglicherweise für den angegebenen Befehl definiert sind. Dies ist besonders nützlich, wenn Sie sicherstellen möchten, dass Sie die ursprüngliche Version eines Befehls verwenden, anstatt eine modifizierte Version, die durch Aliase oder Funktionen in Ihrer Shell-Umgebung beeinflusst werden könnte.

## Verwendung
Die grundlegende Syntax des `command`-Befehls lautet:

```bash
command [OPTION]... COMMAND [ARGUMENTE]...
```

### Häufige Optionen
- `-v` oder `--verbose`: Gibt den Befehl aus, der ausgeführt wird, bevor er tatsächlich ausgeführt wird.
- `-p` oder `--preserve`: Sucht den Befehl in den Standardverzeichnissen, anstatt in den Aliassen oder Funktionen.

## Beispiele
Hier sind einige praktische Beispiele, wie der `command`-Befehl verwendet werden kann:

1. **Verwendung von `command`, um einen Alias zu umgehen**:
   Angenommen, Sie haben einen Alias für `ls` definiert, der zusätzliche Optionen hinzufügt. Sie können den ursprünglichen `ls`-Befehl wie folgt aufrufen:

   ```bash
   command ls
   ```

2. **Verwendung von `command` mit der `-v` Option**:
   Um zu sehen, welcher Befehl tatsächlich ausgeführt wird, können Sie die `-v` Option verwenden:

   ```bash
   command -v ls
   ```

   Dies gibt den vollständigen Pfad zum `ls`-Befehl aus, ohne dass Aliase oder Funktionen berücksichtigt werden.

## Tipps
- Verwenden Sie `command`, wenn Sie sicherstellen möchten, dass Sie die Standardversion eines Befehls verwenden, insbesondere in Skripten, in denen Aliase oder Funktionen möglicherweise die erwartete Funktionalität ändern.
- Überprüfen Sie regelmäßig Ihre Aliase und Funktionen, um sicherzustellen, dass sie nicht unbeabsichtigt die Verwendung von Standardbefehlen beeinträchtigen.
- Nutzen Sie die `-p` Option, um sicherzustellen, dass der Befehl aus den Standardverzeichnissen geladen wird, was hilfreich sein kann, wenn Sie sicherstellen möchten, dass Sie die richtige Version eines Befehls verwenden.