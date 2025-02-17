# [Linux] Bash docker Verwendung: Container verwalten und Anwendungen bereitstellen

## Übersicht
Der `docker` Befehl ist ein leistungsstarkes Tool zur Verwaltung von Containern und zur Bereitstellung von Anwendungen in einer isolierten Umgebung. Docker ermöglicht es Entwicklern, Anwendungen zusammen mit ihren Abhängigkeiten zu paketieren, sodass sie überall konsistent ausgeführt werden können.

## Verwendung
Die grundlegende Syntax des `docker` Befehls lautet:

```bash
docker [optionen] [argumente]
```

## Häufige Optionen
- `run`: Startet einen neuen Container.
- `ps`: Listet alle laufenden Container auf.
- `stop`: Stoppt einen laufenden Container.
- `rm`: Entfernt einen Container.
- `images`: Zeigt alle verfügbaren Images an.
- `pull`: Lädt ein Image aus einem Repository herunter.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `docker` Befehls:

### 1. Einen neuen Container starten
```bash
docker run -d --name mein-container nginx
```
Dieser Befehl startet einen neuen Container mit dem Namen "mein-container" basierend auf dem Nginx-Image im Hintergrund.

### 2. Alle laufenden Container auflisten
```bash
docker ps
```
Mit diesem Befehl werden alle derzeit laufenden Container angezeigt.

### 3. Einen Container stoppen
```bash
docker stop mein-container
```
Dieser Befehl stoppt den Container mit dem Namen "mein-container".

### 4. Einen Container entfernen
```bash
docker rm mein-container
```
Hiermit wird der Container "mein-container" entfernt, sofern er gestoppt ist.

### 5. Ein Image herunterladen
```bash
docker pull ubuntu
```
Dieser Befehl lädt das Ubuntu-Image aus dem Docker Hub herunter.

## Tipps
- Verwenden Sie `docker-compose`, um mehrere Container als Teil einer Anwendung zu verwalten.
- Achten Sie darauf, Container regelmäßig zu aktualisieren, um Sicherheitslücken zu vermeiden.
- Nutzen Sie Volumes, um Daten zwischen Containern und dem Host-System persistent zu speichern.