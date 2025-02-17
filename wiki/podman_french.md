# [Linux] Bash podman : Gestion des conteneurs sans démon

## Overview
La commande `podman` est un outil de gestion de conteneurs qui permet aux utilisateurs de créer, exécuter et gérer des conteneurs et des images de conteneurs. Contrairement à d'autres outils, `podman` fonctionne sans nécessiter un démon en cours d'exécution, ce qui le rend léger et facile à utiliser.

## Usage
La syntaxe de base de la commande `podman` est la suivante :

```bash
podman [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `podman` :

- `run` : Exécute un conteneur.
- `pull` : Télécharge une image de conteneur depuis un registre.
- `ps` : Affiche les conteneurs en cours d'exécution.
- `images` : Liste les images de conteneurs disponibles localement.
- `rm` : Supprime un ou plusieurs conteneurs.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `podman` :

1. **Exécuter un conteneur simple** :
   ```bash
   podman run hello-world
   ```

2. **Télécharger une image de conteneur** :
   ```bash
   podman pull ubuntu
   ```

3. **Lister les conteneurs en cours d'exécution** :
   ```bash
   podman ps
   ```

4. **Lister toutes les images de conteneurs** :
   ```bash
   podman images
   ```

5. **Supprimer un conteneur** :
   ```bash
   podman rm <container_id>
   ```

## Tips
- Utilisez `podman --help` pour obtenir une liste complète des commandes et options disponibles.
- Pensez à utiliser des alias pour les commandes `podman` que vous utilisez fréquemment afin de gagner du temps.
- Vérifiez toujours les images et les conteneurs avant de les supprimer pour éviter de perdre des données importantes.