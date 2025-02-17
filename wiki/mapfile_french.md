# [Linux] Bash mapfile : Lire des fichiers dans un tableau

## Overview
La commande `mapfile` en Bash permet de lire des lignes d'un fichier et de les stocker dans un tableau. Cela facilite le traitement de données ligne par ligne, en rendant l'accès aux lignes plus simple et plus efficace.

## Usage
La syntaxe de base de la commande `mapfile` est la suivante :

```bash
mapfile [options] [arguments]
```

## Common Options
- `-t` : Supprime les caractères de nouvelle ligne à la fin de chaque ligne.
- `-n <number>` : Lit jusqu'à `<number>` lignes du fichier.
- `-O <number>` : Définit l'index de départ pour le tableau.
- `-s <number>` : Ignore les `<number>` premières lignes du fichier.

## Common Examples

### Exemple 1 : Lire un fichier dans un tableau
```bash
mapfile -t mon_tableau < mon_fichier.txt
```
Dans cet exemple, chaque ligne de `mon_fichier.txt` est lue et stockée dans le tableau `mon_tableau`.

### Exemple 2 : Ignorer les premières lignes
```bash
mapfile -s 2 -t mon_tableau < mon_fichier.txt
```
Ici, les deux premières lignes de `mon_fichier.txt` sont ignorées, et le reste est stocké dans `mon_tableau`.

### Exemple 3 : Limiter le nombre de lignes lues
```bash
mapfile -n 5 -t mon_tableau < mon_fichier.txt
```
Cet exemple lit seulement les cinq premières lignes de `mon_fichier.txt` et les stocke dans `mon_tableau`.

## Tips
- Utilisez l'option `-t` pour éviter les caractères de nouvelle ligne indésirables dans votre tableau.
- Pensez à vérifier la taille de votre tableau après la lecture pour éviter des erreurs lors de l'accès aux éléments.
- `mapfile` est particulièrement utile pour le traitement de fichiers de configuration ou de logs où chaque ligne représente une entrée distincte.