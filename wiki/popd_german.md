# [Linux] Bash popd Verwendung: Wechselt das Verzeichnis zurück

## Übersicht
Der Befehl `popd` wird in der Bash verwendet, um das zuletzt gespeicherte Verzeichnis von der Verzeichnisstapel (Directory Stack) zu entfernen und zu diesem zurückzukehren. Dies ist besonders nützlich, wenn Sie zwischen mehreren Verzeichnissen navigieren und Ihre vorherigen Standorte schnell wieder erreichen möchten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
popd [optionen]
```

## Häufige Optionen
- `-n`: Zeigt das Verzeichnis an, ohne es tatsächlich zu wechseln.
- `+n`: Wechselt zu dem Verzeichnis, das sich an der Position `n` im Verzeichnisstapel befindet.
- `-n`: Wechselt zu dem Verzeichnis, das sich an der Position `-n` von oben im Stapel befindet.

## Häufige Beispiele

### Beispiel 1: Einfaches Zurückkehren
Zuerst fügen wir ein Verzeichnis zum Stapel hinzu und kehren dann zurück:

```bash
pushd /home/user/documents
popd
```

### Beispiel 2: Wechseln zu einem bestimmten Verzeichnis im Stapel
Wenn Sie mehrere Verzeichnisse im Stapel haben, können Sie zu einem bestimmten zurückkehren:

```bash
pushd /home/user/documents
pushd /home/user/downloads
popd +1
```

### Beispiel 3: Anzeigen des aktuellen Verzeichnisses im Stapel
Um zu sehen, welches Verzeichnis Sie als nächstes erreichen können, verwenden Sie die `-n` Option:

```bash
pushd /home/user/documents
pushd /home/user/downloads
popd -n
```

## Tipps
- Verwenden Sie `pushd` und `popd` zusammen, um effizient zwischen Verzeichnissen zu navigieren.
- Überprüfen Sie den aktuellen Verzeichnisstapel mit dem Befehl `dirs`, um eine Übersicht über Ihre Navigation zu erhalten.
- Nutzen Sie die Optionen `+n` und `-n`, um gezielt zu bestimmten Verzeichnissen im Stapel zu wechseln, ohne die Reihenfolge zu stören.