# [리눅스] Bash dirs 사용법

## Übersicht
Der Befehl `dirs` in Bash wird verwendet, um die aktuelle Liste der Verzeichnisse im Verzeichnisstapel anzuzeigen. Der Verzeichnisstapel ist eine Datenstruktur, die es Benutzern ermöglicht, zwischen verschiedenen Verzeichnissen zu navigieren, ohne den vollständigen Pfad jedes Mal eingeben zu müssen. Dies ist besonders nützlich für Entwickler und Ingenieure, die häufig zwischen verschiedenen Arbeitsverzeichnissen wechseln.

## Verwendung
Die grundlegende Syntax des Befehls `dirs` lautet:

```bash
dirs [OPTIONEN]
```

### Häufige Optionen
- `-l`: Zeigt die Verzeichnisse in einer langen Form an, wobei jedes Verzeichnis in einer neuen Zeile dargestellt wird.
- `-p`: Gibt die Verzeichnisse in einer durch Leerzeichen getrennten Liste aus, ohne zusätzliche Formatierungen.

## Beispiele
### Beispiel 1: Anzeigen des Verzeichnisstapels
Um den aktuellen Verzeichnisstapel anzuzeigen, geben Sie einfach den Befehl `dirs` ohne Optionen ein:

```bash
dirs
```
Die Ausgabe könnte folgendermaßen aussehen:
```
~/Projekt ~/Dokumente ~/Downloads
```

### Beispiel 2: Verwendung der langen Form
Um die Verzeichnisse in einer langen Form anzuzeigen, verwenden Sie die `-l` Option:

```bash
dirs -l
```
Die Ausgabe könnte so aussehen:
```
~/Projekt
~/Dokumente
~/Downloads
```

## Tipps
- Nutzen Sie `pushd` und `popd` in Kombination mit `dirs`, um effizient zwischen Verzeichnissen zu wechseln und den Überblick über Ihre Navigation zu behalten.
- Wenn Sie häufig zwischen denselben Verzeichnissen wechseln, können Sie `pushd` verwenden, um ein Verzeichnis hinzuzufügen und `dirs` verwenden, um schnell zu sehen, wo Sie sich befinden.
- Denken Sie daran, dass der Verzeichnisstapel nur für die aktuelle Shell-Sitzung gilt. Wenn Sie eine neue Sitzung starten, wird der Stapel zurückgesetzt.