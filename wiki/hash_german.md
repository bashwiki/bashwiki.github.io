# [리눅스] Bash hash 사용법

## Übersicht
Der `hash` Befehl in Bash wird verwendet, um den Speicherort von ausführbaren Dateien zu verwalten, die in der aktuellen Shell-Sitzung verwendet werden. Der Hauptzweck des `hash` Befehls besteht darin, die Suche nach Befehlen zu optimieren, indem die Pfade zu den zuletzt verwendeten Befehlen gespeichert werden. Dies beschleunigt die Ausführung von Befehlen, da Bash nicht jedes Mal im `$PATH` nach dem Speicherort der ausführbaren Dateien suchen muss.

## Verwendung
Die grundlegende Syntax des `hash` Befehls ist:

```bash
hash [OPTIONEN] [BEBEFEHL]
```

### Häufige Optionen:
- `-r`: Diese Option leert den Hash-Cache und zwingt Bash, beim nächsten Ausführen eines Befehls erneut im `$PATH` zu suchen.
- `-p`: Mit dieser Option kann ein spezifischer Pfad für einen Befehl angegeben werden, um ihn im Hash-Cache zu speichern.

## Beispiele
### Beispiel 1: Überprüfen des Hash-Caches
Um den aktuellen Hash-Cache anzuzeigen, können Sie einfach den `hash` Befehl ohne Optionen verwenden:

```bash
hash
```

Dies gibt eine Liste der Befehle und ihrer zugehörigen Pfade zurück, die in der aktuellen Sitzung gespeichert sind.

### Beispiel 2: Hinzufügen eines neuen Befehls zum Hash
Wenn Sie einen Befehl mit einem spezifischen Pfad zum Hash-Cache hinzufügen möchten, verwenden Sie die `-p` Option:

```bash
hash -p mein_befehl /usr/local/bin/mein_befehl
```

Hierbei wird der Befehl `mein_befehl` mit dem angegebenen Pfad im Hash-Cache gespeichert.

## Tipps
- Verwenden Sie den `-r` Schalter, wenn Sie Änderungen an den ausführbaren Dateien vorgenommen haben oder wenn Sie sicherstellen möchten, dass Bash die neuesten Versionen der Befehle verwendet.
- Überprüfen Sie regelmäßig den Hash-Cache, insbesondere wenn Sie häufig neue Programme installieren oder deinstallieren, um sicherzustellen, dass Ihre Befehle korrekt aufgelöst werden.
- Der `hash` Befehl ist besonders nützlich in Skripten oder bei der Arbeit in Umgebungen, in denen viele benutzerdefinierte Befehle verwendet werden.