# [리눅스] Bash mapfile 사용법

## Overview
La commande `mapfile`, également connue sous le nom de `readarray`, est utilisée dans Bash pour lire des lignes d'un fichier ou de l'entrée standard et les stocker dans un tableau. Son principal objectif est de simplifier le processus de lecture de données ligne par ligne, permettant ainsi aux développeurs et aux ingénieurs de manipuler facilement les données en mémoire.

## Usage
La syntaxe de base de la commande `mapfile` est la suivante :

```bash
mapfile [-t] array_name < input_file
```

### Options courantes :
- `-t` : Supprime les caractères de nouvelle ligne à la fin de chaque ligne lue, ce qui peut être utile pour éviter des problèmes lors de la manipulation des éléments du tableau.

## Examples
Voici quelques exemples pratiques illustrant l'utilisation de la commande `mapfile`.

### Exemple 1 : Lire un fichier dans un tableau
Supposons que vous ayez un fichier nommé `data.txt` contenant plusieurs lignes de texte. Vous pouvez lire ce fichier dans un tableau comme suit :

```bash
mapfile -t lines < data.txt
echo "${lines[0]}"  # Affiche la première ligne du fichier
```

### Exemple 2 : Lire l'entrée standard
Vous pouvez également utiliser `mapfile` pour lire des lignes à partir de l'entrée standard. Par exemple :

```bash
echo -e "ligne 1\nligne 2\nligne 3" | mapfile -t lines
echo "${lines[@]}"  # Affiche toutes les lignes lues
```

## Tips
- Utilisez l'option `-t` pour éviter d'avoir des caractères de nouvelle ligne dans les éléments du tableau, ce qui facilite leur manipulation.
- Vérifiez toujours la taille du tableau après l'utilisation de `mapfile` en utilisant `${#array_name[@]}` pour éviter des erreurs lors de l'accès aux éléments.
- `mapfile` est particulièrement utile pour traiter des fichiers volumineux ou des données en continu, car il permet de charger les données en mémoire de manière efficace.