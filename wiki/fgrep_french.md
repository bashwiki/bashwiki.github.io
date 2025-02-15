# [리눅스] Bash fgrep 사용법

## Overview
La commande `fgrep` est un utilitaire de recherche dans les fichiers qui permet de trouver des chaînes de caractères exactes. Contrairement à `grep`, qui interprète les expressions régulières, `fgrep` recherche des motifs littéraux, ce qui le rend particulièrement utile lorsque vous souhaitez rechercher des chaînes sans avoir à vous soucier des caractères spéciaux ou des métacaractères.

## Usage
La syntaxe de base de la commande `fgrep` est la suivante :

```bash
fgrep [options] motif [fichier...]
```

### Options courantes :
- `-i` : Ignore la casse lors de la recherche.
- `-v` : Inverse la recherche, affichant les lignes qui ne contiennent pas le motif.
- `-c` : Affiche uniquement le nombre de lignes contenant le motif.
- `-n` : Affiche les numéros de ligne avec les lignes correspondantes.

## Examples
### Exemple 1 : Recherche d'une chaîne dans un fichier
Pour rechercher la chaîne "erreur" dans un fichier nommé `journal.txt`, vous pouvez utiliser la commande suivante :

```bash
fgrep "erreur" journal.txt
```

### Exemple 2 : Recherche insensible à la casse
Si vous souhaitez rechercher la chaîne "Avertissement" sans tenir compte de la casse, utilisez l'option `-i` :

```bash
fgrep -i "Avertissement" journal.txt
```

## Tips
- Utilisez `fgrep` lorsque vous savez que votre motif ne contient pas de métacaractères, ce qui peut éviter des résultats inattendus.
- Pour des recherches dans plusieurs fichiers, vous pouvez spécifier plusieurs fichiers ou utiliser des jokers, par exemple `*.txt`.
- Pensez à combiner `fgrep` avec d'autres commandes comme `sort` ou `uniq` pour traiter les résultats de manière plus efficace.