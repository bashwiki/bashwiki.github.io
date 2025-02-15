# [리눅스] Bash svn 사용법

## Übersicht
Der Befehl `svn` steht für Subversion und ist ein Versionskontrollsystem, das es Entwicklern ermöglicht, Änderungen an Dateien und Verzeichnissen über die Zeit zu verfolgen. Es wird häufig in Softwareprojekten verwendet, um den Quellcode zu verwalten, Änderungen zu protokollieren und die Zusammenarbeit zwischen mehreren Entwicklern zu erleichtern. Mit `svn` können Benutzer Änderungen an einem Projekt vornehmen, diese Änderungen speichern und bei Bedarf zu früheren Versionen zurückkehren.

## Verwendung
Die grundlegende Syntax des `svn`-Befehls lautet:

```
svn [Befehl] [Optionen] [Ziel]
```

Hier sind einige häufig verwendete Optionen:

- `checkout`: Klont ein Repository auf den lokalen Computer.
- `commit`: Speichert Änderungen im lokalen Arbeitsverzeichnis im Repository.
- `update`: Aktualisiert das lokale Arbeitsverzeichnis mit den neuesten Änderungen aus dem Repository.
- `add`: Fügt neue Dateien oder Verzeichnisse zum Versionskontrollsystem hinzu.
- `delete`: Entfernt Dateien oder Verzeichnisse aus dem Versionskontrollsystem.

## Beispiele

### Beispiel 1: Repository auschecken
Um ein Repository auf Ihren lokalen Computer zu klonen, verwenden Sie den `checkout`-Befehl:

```bash
svn checkout https://example.com/svn/repo/trunk
```

Dieser Befehl lädt den Inhalt des `trunk`-Verzeichnisses des angegebenen Repositories in ein neues Verzeichnis auf Ihrem lokalen System.

### Beispiel 2: Änderungen speichern
Nachdem Sie Änderungen an Ihren Dateien vorgenommen haben, können Sie diese mit dem `commit`-Befehl speichern:

```bash
svn commit -m "Meine Änderungen an der Datei"
```

Hierbei wird die Nachricht "Meine Änderungen an der Datei" als Beschreibung für die vorgenommenen Änderungen im Repository gespeichert.

## Tipps
- Verwenden Sie `svn status`, um den aktuellen Status Ihrer Arbeitskopie zu überprüfen. Dies zeigt Ihnen, welche Dateien geändert, hinzugefügt oder gelöscht wurden.
- Führen Sie regelmäßig `svn update` aus, um sicherzustellen, dass Ihre lokale Kopie des Repositories mit den neuesten Änderungen synchronisiert ist.
- Achten Sie darauf, aussagekräftige Commit-Nachrichten zu schreiben, um die Nachverfolgbarkeit von Änderungen zu erleichtern.
- Nutzen Sie Branches, um an neuen Funktionen oder Bugfixes zu arbeiten, ohne die Hauptentwicklungslinie zu stören.