# [리눅스] Bash cp 사용법

## Overview
La commande `cp` (copy) est utilisée dans les systèmes Unix/Linux pour copier des fichiers et des répertoires. Son but principal est de créer une copie d'un fichier ou d'un répertoire à un nouvel emplacement, tout en préservant le contenu original. Cette commande est essentielle pour la gestion des fichiers, la sauvegarde de données et l'organisation des systèmes de fichiers.

## Usage
La syntaxe de base de la commande `cp` est la suivante :

```bash
cp [options] source destination
```

### Options courantes :
- `-r` : Copie récursive, utilisée pour copier des répertoires et leur contenu.
- `-i` : Mode interactif, demande confirmation avant de remplacer un fichier existant.
- `-u` : Copie uniquement si le fichier source est plus récent que le fichier de destination ou si le fichier de destination n'existe pas.
- `-v` : Mode verbeux, affiche les fichiers au fur et à mesure de leur copie.
- `-a` : Archive, préserve les attributs du fichier (comme les permissions et les timestamps) lors de la copie.

## Examples
### Exemple 1 : Copier un fichier
Pour copier un fichier nommé `document.txt` dans un répertoire nommé `backup`, vous pouvez utiliser la commande suivante :

```bash
cp document.txt backup/
```

### Exemple 2 : Copier un répertoire
Pour copier un répertoire entier nommé `projets` dans un autre répertoire nommé `archives`, utilisez l'option `-r` :

```bash
cp -r projets/ archives/
```

## Tips
- Utilisez l'option `-i` pour éviter d'écraser accidentellement des fichiers existants, surtout lors de la copie de fichiers importants.
- Pour une copie de sauvegarde, envisagez d'utiliser l'option `-u` afin de ne copier que les fichiers qui ont été modifiés.
- En cas de copie de nombreux fichiers, l'option `-v` peut être utile pour suivre le progrès de la commande.
- Pensez à vérifier les permissions des fichiers copiés, surtout si vous utilisez la commande `cp` avec des fichiers sensibles ou des répertoires système.