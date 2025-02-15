# [리눅스] Bash realpath 사용법

## Übersicht
Der Befehl `realpath` wird in der Bash verwendet, um den absoluten Pfad einer Datei oder eines Verzeichnisses zu ermitteln. Er löst symbolische Links auf und gibt den vollständigen, kanonischen Pfad zurück. Dies ist besonders nützlich, um sicherzustellen, dass Sie mit dem richtigen Pfad arbeiten, insbesondere in Skripten oder beim Umgang mit Dateien, die an verschiedenen Orten im Dateisystem gespeichert sind.

## Verwendung
Die grundlegende Syntax des `realpath`-Befehls lautet:

```bash
realpath [OPTIONEN] DATEI
```

### Häufige Optionen
- `-m`, `--canonicalize-missing`: Gibt den kanonischen Pfad zurück, auch wenn die Datei oder das Verzeichnis nicht existiert.
- `-q`, `--quiet`: Unterdrückt Fehlermeldungen, wenn die Datei nicht gefunden wird.
- `-s`, `--strip`: Entfernt alle symbolischen Links und gibt den physischen Pfad zurück.

## Beispiele
### Beispiel 1: Absoluten Pfad ermitteln
Um den absoluten Pfad einer Datei zu ermitteln, verwenden Sie den folgenden Befehl:

```bash
realpath ./mein_script.sh
```
Dieser Befehl gibt den vollständigen Pfad zu `mein_script.sh` zurück, unabhängig davon, wo Sie sich im Dateisystem befinden.

### Beispiel 2: Symbolische Links auflösen
Wenn Sie einen symbolischen Link haben und den tatsächlichen Pfad ermitteln möchten, können Sie Folgendes tun:

```bash
realpath /pfad/zu/symbolischem/link
```
Dieser Befehl gibt den kanonischen Pfad des Ziels des symbolischen Links zurück.

## Tipps
- Verwenden Sie `realpath` in Skripten, um sicherzustellen, dass Sie immer mit den korrekten Pfaden arbeiten, insbesondere wenn Sie mit relativen Pfaden oder symbolischen Links arbeiten.
- Kombinieren Sie `realpath` mit anderen Befehlen wie `cd`, um sicherzustellen, dass Sie in das richtige Verzeichnis wechseln, bevor Sie weitere Befehle ausführen.
- Nutzen Sie die Option `-m`, wenn Sie mit potenziell nicht vorhandenen Dateien arbeiten, um sicherzustellen, dass Sie trotzdem einen Pfad erhalten.

Mit diesen Informationen sind Sie gut gerüstet, um den `realpath`-Befehl in Ihren Bash-Skripten und -Befehlen effektiv zu nutzen.