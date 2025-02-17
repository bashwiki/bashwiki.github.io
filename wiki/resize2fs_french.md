# [Linux] Bash resize2fs Utilisation : Redimensionner un système de fichiers ext2/ext3/ext4

## Overview
La commande `resize2fs` est utilisée pour redimensionner un système de fichiers ext2, ext3 ou ext4. Elle permet d'augmenter ou de diminuer la taille d'un système de fichiers sans perdre de données, tant que l'espace disque est disponible.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
resize2fs [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `resize2fs` :

- `-f` : Force le redimensionnement même si le système de fichiers est monté.
- `-p` : Affiche le pourcentage de progression lors du redimensionnement.
- `-s` : Redimensionne le système de fichiers pour correspondre à la taille de la partition.
- `-M` : Réduit le système de fichiers à sa taille minimale.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `resize2fs` :

1. **Augmenter la taille d'un système de fichiers** :
   ```bash
   resize2fs /dev/sda1 20G
   ```
   Cela redimensionne le système de fichiers sur `/dev/sda1` à 20 Go.

2. **Réduire la taille d'un système de fichiers** :
   ```bash
   resize2fs /dev/sda1 10G
   ```
   Cela réduit la taille du système de fichiers sur `/dev/sda1` à 10 Go.

3. **Redimensionner pour correspondre à la taille de la partition** :
   ```bash
   resize2fs -s /dev/sda1
   ```
   Cela ajuste le système de fichiers pour qu'il corresponde à la taille actuelle de la partition.

4. **Afficher la progression du redimensionnement** :
   ```bash
   resize2fs -p /dev/sda1 15G
   ```
   Cela redimensionne le système de fichiers à 15 Go tout en affichant le pourcentage de progression.

## Tips
- **Sauvegarde** : Toujours faire une sauvegarde de vos données avant de redimensionner un système de fichiers.
- **Système de fichiers démonté** : Il est recommandé de démonter le système de fichiers avant d'utiliser `resize2fs` pour éviter toute corruption.
- **Vérification préalable** : Utilisez `e2fsck` pour vérifier l'intégrité du système de fichiers avant de le redimensionner.