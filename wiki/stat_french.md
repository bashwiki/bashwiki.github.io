# [Linux] Bash stat Utilisation : Afficher les informations sur les fichiers

## Overview
La commande `stat` est utilisée pour afficher des informations détaillées sur un fichier ou un système de fichiers. Elle fournit des données telles que la taille, les permissions, les dates de création et de modification, ainsi que d'autres attributs importants.

## Usage
La syntaxe de base de la commande `stat` est la suivante :

```bash
stat [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec la commande `stat` :

- `-c` : Permet de spécifier un format de sortie personnalisé.
- `--format` : Identique à `-c`, permet de définir le format de sortie.
- `-f` : Affiche les informations sur le système de fichiers au lieu des fichiers individuels.
- `-L` : Suivre les liens symboliques pour afficher les informations du fichier cible.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `stat` :

1. Afficher des informations par défaut sur un fichier :
   ```bash
   stat mon_fichier.txt
   ```

2. Afficher des informations sur un répertoire :
   ```bash
   stat mon_dossier/
   ```

3. Utiliser un format de sortie personnalisé pour afficher uniquement la taille et les permissions :
   ```bash
   stat -c "Taille: %s, Permissions: %A" mon_fichier.txt
   ```

4. Afficher les informations sur le système de fichiers :
   ```bash
   stat -f /
   ```

5. Suivre un lien symbolique pour afficher les informations du fichier cible :
   ```bash
   stat -L mon_lien_symbolique
   ```

## Tips
- Utilisez l'option `-c` pour personnaliser la sortie selon vos besoins, ce qui peut rendre les informations plus lisibles.
- N'oubliez pas que `stat` peut également être utilisé sur des répertoires, ce qui est utile pour vérifier les permissions et les dates de modification.
- Combinez `stat` avec d'autres commandes comme `grep` pour filtrer les résultats si vous travaillez avec de nombreux fichiers.