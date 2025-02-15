# [리눅스] Bash head 사용법

## Overview
La commande `head` est un utilitaire de ligne de commande dans Bash qui permet d'afficher les premières lignes d'un fichier texte. Son principal objectif est de fournir un aperçu rapide du contenu d'un fichier, ce qui est particulièrement utile lors de l'examen de fichiers volumineux. Par défaut, `head` affiche les dix premières lignes, mais cette valeur peut être modifiée selon les besoins de l'utilisateur.

## Usage
La syntaxe de base de la commande `head` est la suivante :

```bash
head [options] [fichier...]
```

### Options courantes :
- `-n [nombre]` : Spécifie le nombre de lignes à afficher. Par exemple, `head -n 5 fichier.txt` affichera les cinq premières lignes du fichier `fichier.txt`.
- `-c [nombre]` : Affiche le nombre de caractères spécifié à partir du début du fichier. Par exemple, `head -c 20 fichier.txt` affichera les 20 premiers caractères.
- `-q` : Ne pas afficher les en-têtes de fichier lors de l'affichage de plusieurs fichiers.
- `-v` : Affiche les en-têtes de fichier même s'il n'y a qu'un seul fichier.

## Examples
Voici quelques exemples pratiques d'utilisation de la commande `head` :

1. Afficher les dix premières lignes d'un fichier :

```bash
head fichier.txt
```

2. Afficher les cinq premières lignes d'un fichier spécifique :

```bash
head -n 5 fichier.txt
```

3. Afficher les 30 premiers caractères d'un fichier :

```bash
head -c 30 fichier.txt
```

## Tips
- Utilisez `head` en combinaison avec d'autres commandes, comme `grep` ou `sort`, pour filtrer ou trier les données avant d'afficher les premières lignes.
- Si vous travaillez avec plusieurs fichiers, utilisez l'option `-q` pour éviter d'afficher les noms de fichiers en tête, ce qui peut rendre la sortie plus propre.
- Pensez à utiliser `head` en conjonction avec `tail` pour naviguer facilement dans un fichier, par exemple pour afficher les lignes du milieu d'un fichier.

En utilisant la commande `head`, vous pouvez rapidement obtenir un aperçu des données contenues dans vos fichiers, ce qui est essentiel pour le développement et l'ingénierie.