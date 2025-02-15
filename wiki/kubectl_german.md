# [리눅스] Bash kubectl 사용법

## Übersicht
`kubectl` ist das Kommandozeilenwerkzeug für die Interaktion mit Kubernetes-Clustern. Es ermöglicht Entwicklern und Systemadministratoren, Anwendungen zu verwalten, Cluster-Ressourcen zu steuern und den Status von Anwendungen und Diensten zu überwachen. Mit `kubectl` können Sie Pods, Deployments, Services und viele andere Kubernetes-Ressourcen erstellen, aktualisieren und löschen.

## Verwendung
Die grundlegende Syntax des `kubectl`-Befehls lautet:

```
kubectl [Befehl] [Ressource] [Name] [Optionen]
```

Hier sind einige häufig verwendete Optionen:

- `get`: Zeigt eine Liste von Ressourcen an.
- `describe`: Gibt detaillierte Informationen über eine bestimmte Ressource aus.
- `apply`: Wendet Konfigurationsänderungen auf Ressourcen an.
- `delete`: Löscht eine bestimmte Ressource.
- `-n` oder `--namespace`: Gibt den Namespace an, in dem der Befehl ausgeführt werden soll.

## Beispiele
### Beispiel 1: Pods auflisten
Um alle Pods in einem Kubernetes-Cluster aufzulisten, verwenden Sie den folgenden Befehl:

```bash
kubectl get pods
```

### Beispiel 2: Details zu einem bestimmten Pod anzeigen
Um detaillierte Informationen zu einem bestimmten Pod namens `my-pod` zu erhalten, verwenden Sie:

```bash
kubectl describe pod my-pod
```

## Tipps
- Nutzen Sie die Option `-o` (Output), um die Ausgabe in verschiedenen Formaten wie JSON oder YAML zu erhalten. Beispiel: `kubectl get pods -o json`.
- Verwenden Sie `kubectl config use-context`, um zwischen verschiedenen Kubernetes-Kontexten zu wechseln, wenn Sie mit mehreren Clustern arbeiten.
- Überprüfen Sie regelmäßig die Kubernetes-Dokumentation, um über neue Funktionen und Best Practices auf dem Laufenden zu bleiben.
- Nutzen Sie Aliase in Ihrer Shell, um häufig verwendete `kubectl`-Befehle zu verkürzen und die Effizienz zu steigern.