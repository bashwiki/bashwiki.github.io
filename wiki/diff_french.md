# [리눅스] Bash diff 사용법

## Overview
La commande `diff` est un outil puissant utilisé dans les systèmes Unix et Linux pour comparer le contenu de deux fichiers ou répertoires. Son principal objectif est de montrer les différences ligne par ligne entre les fichiers, ce qui est particulièrement utile pour les développeurs et les ingénieurs qui travaillent sur le code source ou des documents texte. `diff` peut également être utilisé pour générer des fichiers de patch qui peuvent être appliqués pour modifier un fichier existant.

## Usage
La syntaxe de base de la commande `diff` est la suivante :

```bash
diff [options] fichier1 fichier2
```

### Options courantes :
- `-u` : Affiche les différences dans un format unifié, qui est plus lisible et inclut quelques lignes de contexte.
- `-c` : Affiche les différences dans un format contextuel, qui fournit également un contexte autour des différences.
- `-i` : Ignore la casse lors de la comparaison.
- `-w` : Ignore les espaces blancs lors de la comparaison.
- `-r` : Compare les répertoires de manière récursive.

## Examples
### Exemple 1 : Comparer deux fichiers texte
Pour comparer deux fichiers texte simples, vous pouvez utiliser la commande suivante :

```bash
diff fichier1.txt fichier2.txt
```

Cela affichera les différences entre `fichier1.txt` et `fichier2.txt`.

### Exemple 2 : Comparer deux fichiers avec le format unifié
Pour obtenir un affichage plus lisible des différences, utilisez l'option `-u` :

```bash
diff -u fichier1.txt fichier2.txt
```

Cela affichera les différences avec un contexte, ce qui facilite la compréhension des modifications.

## Tips
- Utilisez l'option `-u` pour générer des fichiers de patch, car le format unifié est largement utilisé pour les modifications de code.
- Lorsque vous travaillez avec des fichiers de code source, envisagez d'utiliser `diff` avec des systèmes de contrôle de version comme Git pour suivre les modifications de manière efficace.
- Si vous comparez des répertoires, l'option `-r` est très utile pour voir toutes les différences dans les fichiers contenus dans ces répertoires.

En utilisant `diff`, vous pouvez facilement identifier et gérer les différences entre les fichiers, ce qui est essentiel pour le développement et la collaboration sur des projets.