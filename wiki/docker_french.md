# [Linux] Bash docker utilisation : Gérer des conteneurs et des images

## Overview
La commande `docker` est utilisée pour gérer des conteneurs et des images dans l'environnement Docker. Elle permet aux utilisateurs de créer, exécuter et gérer des applications dans des conteneurs, facilitant ainsi le déploiement et la gestion des applications.

## Usage
La syntaxe de base de la commande `docker` est la suivante :

```bash
docker [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `docker` :

- `run` : Crée et exécute un conteneur à partir d'une image.
- `ps` : Affiche les conteneurs en cours d'exécution.
- `images` : Liste toutes les images disponibles sur le système.
- `rm` : Supprime un ou plusieurs conteneurs.
- `rmi` : Supprime une ou plusieurs images.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `docker` :

1. **Exécuter un conteneur Nginx :**
   ```bash
   docker run -d -p 80:80 nginx
   ```

2. **Lister les conteneurs en cours d'exécution :**
   ```bash
   docker ps
   ```

3. **Lister toutes les images disponibles :**
   ```bash
   docker images
   ```

4. **Supprimer un conteneur :**
   ```bash
   docker rm <container_id>
   ```

5. **Supprimer une image :**
   ```bash
   docker rmi <image_id>
   ```

## Tips
- Utilisez `docker-compose` pour gérer plusieurs conteneurs et simplifier la configuration de vos applications.
- N'oubliez pas de toujours vérifier l'état de vos conteneurs avec `docker ps` avant de tenter de les supprimer.
- Pensez à taguer vos images pour une meilleure organisation et gestion des versions.