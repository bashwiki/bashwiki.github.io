# [Linux] Bash df Utilisation : Afficher l'espace disque disponible

## Overview
La commande `df` (disk free) est utilisée pour afficher des informations sur l'espace disque utilisé et disponible sur les systèmes de fichiers montés. Elle permet aux utilisateurs de surveiller l'utilisation de l'espace disque et d'identifier les partitions qui pourraient être pleines.

## Usage
La syntaxe de base de la commande `df` est la suivante :

```bash
df [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `df` :

- `-h` : Affiche les tailles dans un format lisible par l'homme (par exemple, Ko, Mo, Go).
- `-T` : Affiche le type de système de fichiers.
- `-a` : Inclut les systèmes de fichiers qui ne sont pas montés.
- `-i` : Affiche l'utilisation des inodes au lieu de l'espace disque.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `df` :

1. Afficher l'espace disque disponible sur tous les systèmes de fichiers montés :

   ```bash
   df
   ```

2. Afficher l'espace disque dans un format lisible par l'homme :

   ```bash
   df -h
   ```

3. Afficher les informations de tous les systèmes de fichiers, y compris ceux qui ne sont pas montés :

   ```bash
   df -a
   ```

4. Afficher le type de système de fichiers avec les informations d'espace :

   ```bash
   df -T
   ```

5. Afficher l'utilisation des inodes :

   ```bash
   df -i
   ```

## Tips
- Utilisez l'option `-h` pour rendre les résultats plus faciles à lire, surtout si vous travaillez avec de grandes quantités de données.
- Combinez plusieurs options pour obtenir des informations plus détaillées, par exemple `df -hT` pour afficher à la fois la taille lisible par l'homme et le type de système de fichiers.
- Vérifiez régulièrement l'utilisation de l'espace disque pour éviter de remplir vos partitions, ce qui pourrait entraîner des problèmes de performance ou de fonctionnement.