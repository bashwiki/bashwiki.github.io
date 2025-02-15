# [리눅스] Bash kubectl 사용법

## Overview
`kubectl` est un outil en ligne de commande pour interagir avec les clusters Kubernetes. Il permet aux utilisateurs de déployer des applications, de gérer les ressources du cluster, et de récupérer des informations sur l'état des ressources. En résumé, `kubectl` est essentiel pour toute opération liée à Kubernetes, offrant une interface pour contrôler et automatiser les tâches dans un environnement Kubernetes.

## Usage
La syntaxe de base de la commande `kubectl` est la suivante :

```
kubectl [command] [type] [name] [flags]
```

### Options courantes :
- `get`: Récupère des informations sur les ressources.
- `apply`: Applique des modifications à des ressources à partir d'un fichier de configuration.
- `delete`: Supprime des ressources spécifiées.
- `describe`: Affiche des détails sur une ressource spécifique.
- `--namespace`: Spécifie le namespace dans lequel exécuter la commande.

## Examples
### Exemple 1 : Récupérer les pods
Pour lister tous les pods dans le namespace par défaut, vous pouvez utiliser la commande suivante :

```bash
kubectl get pods
```

### Exemple 2 : Appliquer une configuration
Si vous avez un fichier de configuration YAML nommé `deployment.yaml`, vous pouvez déployer les ressources définies dans ce fichier avec :

```bash
kubectl apply -f deployment.yaml
```

## Tips
- Utilisez `kubectl config get-contexts` pour vérifier le contexte actuel et vous assurer que vous interagissez avec le bon cluster.
- Ajoutez l'option `-o wide` à vos commandes `get` pour obtenir plus de détails sur les ressources.
- Familiarisez-vous avec les alias pour `kubectl` afin de simplifier les commandes longues, par exemple, en ajoutant `alias k=kubectl` dans votre fichier `.bashrc`.
- Utilisez `kubectl --help` pour obtenir une aide détaillée sur les commandes et options disponibles.