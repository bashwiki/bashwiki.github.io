# [리눅스] Bash stat 사용법

## Overview
La commande `stat` est utilisée pour afficher des informations détaillées sur un fichier ou un système de fichiers. Elle fournit des données telles que la taille du fichier, les permissions, le propriétaire, les timestamps (dates de création, de modification et d'accès), et d'autres attributs importants. Cela permet aux développeurs et aux ingénieurs de mieux comprendre les caractéristiques d'un fichier et son état dans le système.

## Usage
La syntaxe de base de la commande `stat` est la suivante :

```bash
stat [options] fichier
```

### Options courantes :
- `-c` : Permet de spécifier un format de sortie personnalisé.
- `-f` : Affiche des informations sur le système de fichiers contenant le fichier spécifié.
- `--format` : Semblable à `-c`, permet de définir un format de sortie.
- `-t` : Affiche les informations sous forme de tableau.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `stat`.

### Exemple 1 : Informations de base sur un fichier
Pour afficher les informations détaillées d'un fichier nommé `exemple.txt`, vous pouvez utiliser la commande suivante :

```bash
stat exemple.txt
```

### Exemple 2 : Formatage personnalisé
Pour afficher uniquement la taille et la date de dernière modification d'un fichier, utilisez l'option `--format` :

```bash
stat --format="Taille : %s octets, Modifié le : %y" exemple.txt
```

## Tips
- Utilisez l'option `-f` pour obtenir des informations sur le système de fichiers, ce qui peut être utile pour diagnostiquer des problèmes liés à l'espace disque.
- Pour des scripts automatisés, envisagez d'utiliser l'option `-c` pour formater la sortie de manière à ce qu'elle soit facilement analysable.
- Familiarisez-vous avec les différents formats de sortie disponibles pour tirer le meilleur parti de la commande `stat` dans vos tâches quotidiennes.