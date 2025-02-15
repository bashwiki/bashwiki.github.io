# [리눅스] Bash df 사용법

## Overview
La commande `df` (disk free) est utilisée dans les systèmes Unix et Linux pour afficher des informations sur l'espace disque utilisé et disponible sur les systèmes de fichiers. Son objectif principal est de fournir un aperçu de l'utilisation de l'espace disque, ce qui est essentiel pour la gestion des ressources et le dépannage des problèmes de stockage.

## Usage
La syntaxe de base de la commande `df` est la suivante :

```bash
df [options] [fichiers]
```

### Options courantes :
- `-h` : Affiche les tailles dans un format lisible par l'homme (par exemple, Ko, Mo, Go).
- `-T` : Affiche le type de système de fichiers.
- `-a` : Inclut les systèmes de fichiers avec une taille de 0.
- `-i` : Affiche l'utilisation des inodes au lieu de l'espace disque.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `df` :

1. Pour afficher l'utilisation de l'espace disque de manière lisible par l'homme :

```bash
df -h
```

Cette commande affichera une liste de tous les systèmes de fichiers montés avec leur taille totale, l'espace utilisé, l'espace disponible et le point de montage.

2. Pour afficher les informations sur un système de fichiers spécifique, par exemple `/dev/sda1` :

```bash
df -h /dev/sda1
```

Cela fournira des détails uniquement pour le système de fichiers spécifié.

## Tips
- Utilisez l'option `-T` pour obtenir des informations supplémentaires sur le type de système de fichiers, ce qui peut être utile pour le dépannage.
- Combinez `df` avec d'autres commandes comme `grep` pour filtrer les résultats, par exemple :

```bash
df -h | grep '/dev/sda'
```

Cela affichera uniquement les informations concernant les systèmes de fichiers qui contiennent `/dev/sda`, facilitant ainsi la recherche d'informations spécifiques.