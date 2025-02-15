# [리눅스] Bash readarray 사용법

## Overview
La commande `readarray` (ou `mapfile`) est utilisée dans Bash pour lire les lignes d'un fichier ou d'une entrée standard et les stocker dans un tableau. Cette commande est particulièrement utile pour manipuler des données ligne par ligne, ce qui est courant dans le traitement de fichiers texte ou de flux de données.

## Usage
La syntaxe de base de la commande `readarray` est la suivante :

```bash
readarray [options] array_name
```

### Options courantes :
- `-t` : Supprime les caractères de nouvelle ligne à la fin de chaque ligne lue, ce qui est souvent souhaitable pour éviter des éléments de tableau indésirables.
- `-n` : Limite le nombre de lignes à lire à `n`.
- `-s` : Ignore les `n` premières lignes du fichier ou de l'entrée standard.

## Examples
### Exemple 1 : Lire un fichier dans un tableau
Supposons que vous ayez un fichier nommé `data.txt` contenant plusieurs lignes de texte. Vous pouvez lire ce fichier dans un tableau comme suit :

```bash
readarray -t lines < data.txt
```

Après l'exécution de cette commande, chaque ligne du fichier `data.txt` sera stockée dans le tableau `lines`. Vous pouvez accéder à chaque élément du tableau en utilisant la syntaxe `${lines[index]}`.

### Exemple 2 : Lire l'entrée standard
Vous pouvez également utiliser `readarray` pour lire des lignes à partir de l'entrée standard. Par exemple :

```bash
echo -e "ligne 1\nligne 2\nligne 3" | readarray -t lines
```

Dans cet exemple, les lignes "ligne 1", "ligne 2" et "ligne 3" seront stockées dans le tableau `lines`.

## Tips
- Lorsque vous utilisez `readarray`, il est souvent utile d'utiliser l'option `-t` pour éviter d'avoir des caractères de nouvelle ligne dans les éléments du tableau.
- Pensez à vérifier la taille du tableau après la lecture en utilisant `${#lines[@]}` pour éviter les erreurs lors de l'accès aux éléments.
- `readarray` est particulièrement efficace pour traiter de grandes quantités de données, car il lit toutes les lignes en une seule opération, ce qui est plus performant que de lire ligne par ligne dans une boucle.