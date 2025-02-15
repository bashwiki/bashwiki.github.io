# [리눅스] Bash sort 사용법

## Overview
La commande `sort` est un utilitaire de ligne de commande sous Unix/Linux qui permet de trier les lignes d'un fichier ou de l'entrée standard. Son objectif principal est d'organiser les données en fonction de l'ordre lexicographique, numérique ou selon d'autres critères spécifiés par l'utilisateur. Cela est particulièrement utile pour le traitement de données, la préparation de rapports ou l'analyse de fichiers texte.

## Usage
La syntaxe de base de la commande `sort` est la suivante :

```bash
sort [options] [fichier...]
```

### Options courantes :
- `-n` : Trie les lignes en fonction de leur valeur numérique.
- `-r` : Inverse l'ordre de tri (tri décroissant).
- `-k` : Spécifie une clé de tri. Par exemple, `-k 2` trie selon la deuxième colonne.
- `-u` : Supprime les doublons des lignes triées.
- `-o` : Écrit le résultat dans un fichier spécifié au lieu de l'afficher sur la sortie standard.

## Examples
### Exemple 1 : Trier un fichier texte
Supposons que vous ayez un fichier nommé `nombres.txt` contenant les lignes suivantes :

```
3
1
4
1
5
9
2
6
5
3
5
```

Pour trier ce fichier par ordre croissant, vous pouvez utiliser la commande suivante :

```bash
sort nombres.txt
```

### Exemple 2 : Trier par ordre numérique et inverse
Pour trier le même fichier en ordre décroissant, vous pouvez utiliser les options `-n` et `-r` :

```bash
sort -nr nombres.txt
```

## Tips
- Lorsque vous traitez de grands fichiers, envisagez d'utiliser l'option `-o` pour écrire directement le résultat dans un fichier, ce qui peut être plus efficace.
- Pour trier des données basées sur plusieurs colonnes, utilisez l'option `-k` pour spécifier la colonne à trier, par exemple `sort -k 1,1 -k 2,2` pour trier d'abord par la première colonne, puis par la deuxième.
- Pensez à utiliser `sort -u` pour obtenir une liste unique de lignes triées, ce qui est utile pour éliminer les doublons.

La commande `sort` est un outil puissant et flexible qui peut grandement faciliter le traitement et l'analyse des données textuelles.