# [Linux] Bash kubectl Utilisation : Gérer les ressources Kubernetes

## Overview
La commande `kubectl` est un outil en ligne de commande qui permet d'interagir avec un cluster Kubernetes. Elle est utilisée pour déployer des applications, inspecter et gérer les ressources, et exécuter des commandes dans des conteneurs.

## Usage
La syntaxe de base de la commande `kubectl` est la suivante :

```bash
kubectl [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `kubectl` :

- `get` : Récupérer des informations sur les ressources.
- `apply` : Appliquer des modifications à des ressources à partir d'un fichier de configuration.
- `delete` : Supprimer des ressources.
- `describe` : Afficher des détails sur une ressource spécifique.
- `logs` : Afficher les journaux d'un conteneur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `kubectl` :

### 1. Lister tous les pods
```bash
kubectl get pods
```

### 2. Appliquer un fichier de configuration
```bash
kubectl apply -f mon-fichier.yaml
```

### 3. Supprimer un déploiement
```bash
kubectl delete deployment mon-deploiement
```

### 4. Afficher les détails d'un service
```bash
kubectl describe service mon-service
```

### 5. Afficher les journaux d'un pod
```bash
kubectl logs mon-pod
```

## Tips
- Utilisez `kubectl get all` pour obtenir un aperçu rapide de toutes les ressources dans le namespace actuel.
- Pensez à utiliser des fichiers de configuration YAML pour gérer vos ressources de manière déclarative.
- N'oubliez pas de spécifier le namespace avec l'option `-n` si vous travaillez dans un namespace différent de celui par défaut.