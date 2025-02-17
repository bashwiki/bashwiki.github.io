# [Linux] Bash kubectl Verwendung: Kubernetes-Cluster verwalten

## Übersicht
Der `kubectl` Befehl ist das Kommandozeilenwerkzeug zur Interaktion mit Kubernetes-Clustern. Mit `kubectl` können Benutzer Ressourcen im Cluster erstellen, anzeigen, aktualisieren und löschen. Es ist ein unverzichtbares Tool für die Verwaltung von Kubernetes-Anwendungen.

## Verwendung
Die grundlegende Syntax des `kubectl` Befehls lautet:

```bash
kubectl [optionen] [argumente]
```

## Häufige Optionen
- `get`: Zeigt Informationen über Ressourcen an.
- `create`: Erstellt neue Ressourcen.
- `apply`: Wendet Änderungen an bestehenden Ressourcen an.
- `delete`: Löscht Ressourcen.
- `describe`: Zeigt detaillierte Informationen über eine bestimmte Ressource an.
- `logs`: Zeigt die Protokolle eines Pods an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `kubectl`:

### Ressourcen auflisten
Um alle Pods im aktuellen Namespace aufzulisten:

```bash
kubectl get pods
```

### Einen neuen Pod erstellen
Um einen neuen Pod mit einer bestimmten Konfiguration zu erstellen:

```bash
kubectl create -f pod.yaml
```

### Änderungen anwenden
Um Änderungen an einer bestehenden Ressource anzuwenden:

```bash
kubectl apply -f deployment.yaml
```

### Ressourcen löschen
Um einen bestimmten Pod zu löschen:

```bash
kubectl delete pod mein-pod
```

### Protokolle eines Pods anzeigen
Um die Protokolle eines bestimmten Pods anzuzeigen:

```bash
kubectl logs mein-pod
```

## Tipps
- Verwenden Sie `kubectl get all`, um eine Übersicht über alle Ressourcen im aktuellen Namespace zu erhalten.
- Nutzen Sie die `-n` Option, um Ressourcen in einem bestimmten Namespace anzuzeigen, z.B. `kubectl get pods -n mein-namespace`.
- Verwenden Sie `--help`, um eine Liste aller verfügbaren Optionen und Argumente für einen bestimmten Befehl zu erhalten, z.B. `kubectl get --help`.