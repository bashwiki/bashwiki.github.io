# [리눅스] Bash egrep 사용법

## Overview
La commande `egrep` est une version améliorée de la commande `grep`, utilisée pour rechercher des motifs dans des fichiers ou des flux de texte. Elle permet d'utiliser des expressions régulières étendues, ce qui la rend particulièrement utile pour des recherches complexes. Son principal objectif est de faciliter la recherche de chaînes de caractères qui correspondent à des motifs spécifiques dans de grandes quantités de données.

## Usage
La syntaxe de base de la commande `egrep` est la suivante :

```bash
egrep [options] motif [fichier...]
```

### Options courantes :
- `-i` : Ignore la casse lors de la recherche.
- `-v` : Inverse le motif, affichant les lignes qui ne correspondent pas au motif.
- `-c` : Affiche uniquement le nombre de lignes qui correspondent au motif.
- `-n` : Affiche les numéros de ligne des correspondances.
- `-r` : Recherche récursivement dans les répertoires.

## Examples
### Exemple 1 : Recherche simple
Pour rechercher toutes les lignes contenant le mot "erreur" dans un fichier nommé `journal.txt`, vous pouvez utiliser la commande suivante :

```bash
egrep "erreur" journal.txt
```

### Exemple 2 : Recherche avec des options
Pour rechercher toutes les lignes contenant le mot "erreur" ou "avertissement" dans un fichier, sans tenir compte de la casse, et afficher les numéros de ligne, utilisez :

```bash
egrep -i -n "erreur|avertissement" journal.txt
```

## Tips
- Utilisez les expressions régulières pour affiner vos recherches. Par exemple, `egrep "^Début" fichier.txt` trouvera toutes les lignes qui commencent par "Début".
- Combinez `egrep` avec d'autres commandes comme `sort` ou `uniq` pour traiter les résultats de recherche.
- Pensez à utiliser l'option `-r` pour rechercher dans tous les fichiers d'un répertoire, ce qui peut être très utile pour l'analyse de journaux ou de fichiers de configuration.