# [리눅스] Bash scp 사용법

## Übersicht
Der Befehl `scp` (Secure Copy Protocol) wird verwendet, um Dateien sicher zwischen einem lokalen und einem entfernten Host oder zwischen zwei entfernten Hosts zu kopieren. Es nutzt das SSH-Protokoll zur Datenübertragung, was bedeutet, dass die Übertragung verschlüsselt ist und somit eine sichere Übertragung gewährleistet ist. `scp` ist besonders nützlich für Entwickler und Ingenieure, die regelmäßig Dateien zwischen verschiedenen Servern oder zwischen ihrem lokalen System und einem Server austauschen müssen.

## Verwendung
Die grundlegende Syntax des `scp`-Befehls lautet:

```
scp [Optionen] Quelle Ziel
```

Hierbei kann die Quelle und das Ziel sowohl lokale als auch entfernte Pfade sein. Die häufigsten Optionen sind:

- `-r`: Kopiert Verzeichnisse rekursiv.
- `-P port`: Gibt den Port an, der für die SSH-Verbindung verwendet werden soll (Standard ist 22).
- `-i Datei`: Gibt eine spezifische private Schlüsseldatei für die Authentifizierung an.
- `-v`: Aktiviert den verbose Modus, um detaillierte Informationen über den Kopiervorgang anzuzeigen.

## Beispiele
### Beispiel 1: Eine Datei von lokal zu einem entfernten Server kopieren
Um eine Datei namens `beispiel.txt` von Ihrem lokalen Computer zu einem entfernten Server mit der IP-Adresse `192.168.1.10` zu kopieren, verwenden Sie den folgenden Befehl:

```bash
scp beispiel.txt benutzername@192.168.1.10:/pfad/zum/zielverzeichnis/
```

### Beispiel 2: Ein ganzes Verzeichnis auf einen entfernten Server kopieren
Um ein Verzeichnis namens `mein_verzeichnis` rekursiv auf einen entfernten Server zu kopieren, verwenden Sie:

```bash
scp -r mein_verzeichnis benutzername@192.168.1.10:/pfad/zum/zielverzeichnis/
```

## Tipps
- Stellen Sie sicher, dass Sie über die erforderlichen Berechtigungen zum Kopieren von Dateien auf den Zielserver verfügen.
- Verwenden Sie den `-v`-Schalter, um bei Problemen mit der Verbindung oder beim Kopieren von Dateien detaillierte Fehlermeldungen zu erhalten.
- Wenn Sie häufig mit demselben Server arbeiten, können Sie SSH-Schlüssel verwenden, um die Authentifizierung zu vereinfachen und Passworteingaben zu vermeiden.
- Achten Sie darauf, die richtigen Berechtigungen für die Dateien und Verzeichnisse zu setzen, um unbefugten Zugriff zu verhindern.