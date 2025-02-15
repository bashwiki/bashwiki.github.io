# [리눅스] Bash docker 사용법

## Overview
La commande `docker` est un outil essentiel pour les développeurs et les ingénieurs qui souhaitent créer, déployer et gérer des applications dans des conteneurs. Docker permet d'encapsuler une application et toutes ses dépendances dans un conteneur léger et portable, facilitant ainsi le déploiement sur n'importe quel environnement. Son principal objectif est de simplifier le processus de développement et de déploiement d'applications en assurant la cohérence entre les environnements de développement, de test et de production.

## Usage
La syntaxe de base de la commande `docker` est la suivante :

```bash
docker [OPTIONS] COMMAND [ARG...]
```

### Options courantes
- `-v`, `--version` : Affiche la version de Docker installée.
- `--help` : Affiche l'aide et la liste des commandes disponibles.
- `-D`, `--debug` : Active le mode débogage pour obtenir des informations détaillées sur les opérations en cours.

### Commandes principales
- `docker run` : Crée et exécute un conteneur.
- `docker ps` : Liste les conteneurs en cours d'exécution.
- `docker images` : Affiche les images Docker disponibles sur le système.
- `docker stop` : Arrête un conteneur en cours d'exécution.

## Examples
### Exemple 1 : Exécuter un conteneur simple
Pour exécuter un conteneur basé sur l'image `hello-world`, vous pouvez utiliser la commande suivante :

```bash
docker run hello-world
```
Cette commande télécharge l'image `hello-world` si elle n'est pas déjà présente sur votre machine et exécute le conteneur, affichant un message de bienvenue.

### Exemple 2 : Lister les conteneurs en cours d'exécution
Pour voir tous les conteneurs qui s'exécutent actuellement, utilisez :

```bash
docker ps
```
Cette commande affichera une liste des conteneurs actifs, avec des informations telles que l'ID du conteneur, le nom de l'image, et le statut.

## Tips
- **Utilisez des images officielles** : Lorsque vous créez des conteneurs, privilégiez les images officielles disponibles sur Docker Hub pour garantir la sécurité et la fiabilité.
- **Nettoyez régulièrement** : Utilisez `docker system prune` pour supprimer les conteneurs, images et volumes inutilisés afin de libérer de l'espace disque.
- **Automatisez avec des scripts** : Intégrez des commandes Docker dans des scripts pour automatiser le déploiement et la gestion des conteneurs, ce qui peut améliorer l'efficacité de votre flux de travail.

En suivant ces conseils et en utilisant la commande `docker`, vous pourrez gérer efficacement vos applications conteneurisées.