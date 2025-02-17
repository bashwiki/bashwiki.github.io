# [Linux] Bash podman Verwendung: Container verwalten und ausführen

## Übersicht
Der `podman` Befehl ist ein leistungsstarkes Tool zur Verwaltung von Containern und Pods. Es ermöglicht Benutzern, Container zu erstellen, zu starten, zu stoppen und zu verwalten, ohne dass ein Daemon erforderlich ist. Podman ist besonders nützlich für Entwickler und Systemadministratoren, die Container-Anwendungen in einer sicheren und flexiblen Umgebung betreiben möchten.

## Verwendung
Die grundlegende Syntax des `podman` Befehls lautet:

```bash
podman [optionen] [argumente]
```

## Häufige Optionen
- `run`: Startet einen neuen Container.
- `ps`: Listet alle laufenden Container auf.
- `stop`: Stoppt einen laufenden Container.
- `rm`: Entfernt einen Container.
- `images`: Zeigt eine Liste der verfügbaren Container-Images an.
- `pull`: Lädt ein Container-Image aus einem Repository herunter.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `podman`:

### 1. Einen neuen Container starten
```bash
podman run -d --name mein-container nginx
```
Dieser Befehl startet einen neuen Container mit dem Namen "mein-container" im Hintergrund und verwendet das Nginx-Image.

### 2. Alle laufenden Container auflisten
```bash
podman ps
```
Dieser Befehl zeigt eine Liste aller derzeit laufenden Container an.

### 3. Einen Container stoppen
```bash
podman stop mein-container
```
Mit diesem Befehl wird der Container mit dem Namen "mein-container" gestoppt.

### 4. Einen Container entfernen
```bash
podman rm mein-container
```
Dieser Befehl entfernt den gestoppten Container "mein-container".

### 5. Ein Container-Image herunterladen
```bash
podman pull alpine
```
Dieser Befehl lädt das Alpine-Image aus dem Standard-Repository herunter.

## Tipps
- Verwenden Sie die Option `-it`, um interaktive Container zu starten, die eine Shell-Sitzung ermöglichen.
- Nutzen Sie `podman logs [container-name]`, um die Protokolle eines Containers anzuzeigen und Fehler zu diagnostizieren.
- Denken Sie daran, Container regelmäßig zu entfernen, um Speicherplatz zu sparen, insbesondere wenn Sie mit vielen Testcontainern arbeiten.