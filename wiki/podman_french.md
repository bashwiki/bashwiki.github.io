# [리눅스] Bash podman 사용법

## Overview
`podman` est un outil de gestion de conteneurs qui permet aux utilisateurs de créer, exécuter et gérer des conteneurs et des images de conteneurs. Contrairement à d'autres outils comme Docker, `podman` fonctionne sans démon, ce qui signifie qu'il peut être exécuté en tant qu'utilisateur non privilégié. Cela améliore la sécurité et la flexibilité lors de la gestion des conteneurs.

## Usage
La syntaxe de base de la commande `podman` est la suivante :

```
podman [OPTIONS] COMMAND [ARG...]
```

### Options courantes :
- `--help` : Affiche l'aide pour la commande.
- `--version` : Affiche la version de `podman`.
- `-v`, `--verbose` : Affiche des informations détaillées sur l'exécution de la commande.
- `-q`, `--quiet` : Exécute la commande en mode silencieux, sans sortie standard.

## Examples
### Exemple 1 : Exécuter un conteneur
Pour exécuter un conteneur basé sur l'image `alpine`, vous pouvez utiliser la commande suivante :

```bash
podman run -it alpine /bin/sh
```
Cette commande télécharge l'image `alpine` si elle n'est pas déjà présente localement et ouvre un shell interactif à l'intérieur du conteneur.

### Exemple 2 : Lister les conteneurs en cours d'exécution
Pour afficher tous les conteneurs en cours d'exécution, utilisez :

```bash
podman ps
```
Cette commande affiche une liste des conteneurs actifs avec leurs identifiants, noms et états.

## Tips
- **Utiliser des alias** : Pour simplifier l'utilisation de `podman`, envisagez de créer des alias dans votre fichier `.bashrc` ou `.bash_profile` pour les commandes que vous utilisez fréquemment.
- **Gestion des images** : Utilisez `podman images` pour lister toutes les images disponibles sur votre système et `podman rmi <image_id>` pour supprimer une image non utilisée.
- **Sécurité** : Étant donné que `podman` fonctionne sans démon, il est recommandé de l'utiliser dans des environnements où la sécurité est une préoccupation, car il réduit la surface d'attaque par rapport à d'autres solutions de conteneurs.