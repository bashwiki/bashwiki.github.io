# [리눅스] Bash docker 사용법

## Übersicht
Der Befehl `docker` ist ein Kommandozeilenwerkzeug, das zur Verwaltung von Containern verwendet wird. Docker ermöglicht es Entwicklern und Ingenieuren, Anwendungen in Containern zu isolieren, zu paketieren und zu verteilen. Container sind leichtgewichtige, portable und in sich geschlossene Umgebungen, die alles enthalten, was zum Ausführen einer Anwendung erforderlich ist, einschließlich Code, Laufzeit, Bibliotheken und Abhängigkeiten.

## Verwendung
Die grundlegende Syntax des `docker`-Befehls lautet:

```bash
docker [OPTIONS] COMMAND [ARG...]
```

Hier sind einige häufig verwendete Optionen und Befehle:

- `run`: Startet einen neuen Container.
- `ps`: Listet alle laufenden Container auf.
- `images`: Zeigt alle verfügbaren Images an.
- `pull`: Lädt ein Image aus einem Docker-Repository herunter.
- `build`: Erstellt ein neues Image aus einem Dockerfile.

## Beispiele
### Beispiel 1: Einen neuen Container starten
Um einen neuen Container mit dem offiziellen Nginx-Image zu starten, verwenden Sie den folgenden Befehl:

```bash
docker run -d -p 80:80 nginx
```
Dieser Befehl startet einen Nginx-Server im Hintergrund (`-d` für detached mode) und leitet den Port 80 des Containers auf den Port 80 des Hosts weiter.

### Beispiel 2: Alle laufenden Container auflisten
Um alle derzeit laufenden Container anzuzeigen, verwenden Sie:

```bash
docker ps
```
Dieser Befehl zeigt eine Liste aller aktiven Container mit ihren IDs, Namen und Status an.

## Tipps
- Verwenden Sie `docker-compose`, um mehrere Container als Teil einer Anwendung zu verwalten. Dies erleichtert die Orchestrierung komplexer Anwendungen.
- Nutzen Sie `docker logs [CONTAINER_ID]`, um die Protokolle eines Containers zu überprüfen, was bei der Fehlersuche hilfreich sein kann.
- Halten Sie Ihre Docker-Images und -Container sauber, indem Sie regelmäßig nicht mehr benötigte Images und Container mit `docker system prune` entfernen.
- Achten Sie darauf, die Docker-Dokumentation zu lesen, um die neuesten Funktionen und Best Practices zu verstehen.