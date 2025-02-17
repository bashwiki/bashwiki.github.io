# [Linux] Bash readarray : Lire des lignes dans un tableau

## Overview
La commande `readarray` en Bash permet de lire des lignes d'un fichier ou de l'entrée standard et de les stocker dans un tableau. Cela facilite le traitement des données ligne par ligne dans des scripts.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
readarray [options] [nom_du_tableau]
```

## Common Options
- `-t` : Supprime les caractères de nouvelle ligne à la fin de chaque ligne lue.
- `-n N` : Lit au maximum N lignes.
- `-s N` : Ignore les N premières lignes.
- `-d DELIM` : Utilise un délimiteur spécifique au lieu du caractère de nouvelle ligne par défaut.

## Common Examples

### Exemple 1 : Lire un fichier dans un tableau
```bash
readarray lignes < fichier.txt
```
Cet exemple lit toutes les lignes de `fichier.txt` et les stocke dans le tableau `lignes`.

### Exemple 2 : Supprimer les nouvelles lignes
```bash
readarray -t lignes < fichier.txt
```
Ici, les nouvelles lignes à la fin de chaque ligne sont supprimées.

### Exemple 3 : Lire un nombre limité de lignes
```bash
readarray -n 5 lignes < fichier.txt
```
Cet exemple lit seulement les 5 premières lignes de `fichier.txt`.

### Exemple 4 : Ignorer les premières lignes
```bash
readarray -s 2 lignes < fichier.txt
```
Cela ignore les 2 premières lignes de `fichier.txt` et lit le reste dans le tableau.

### Exemple 5 : Utiliser un délimiteur personnalisé
```bash
readarray -d ',' lignes < fichier.csv
```
Ici, les lignes sont lues en utilisant une virgule comme délimiteur.

## Tips
- Utilisez l'option `-t` pour éviter d'avoir des caractères de nouvelle ligne indésirables dans votre tableau.
- Vérifiez la taille de votre tableau après la lecture avec `echo ${#lignes[@]}` pour vous assurer que vous avez lu le bon nombre de lignes.
- Combinez `readarray` avec d'autres commandes comme `grep` ou `awk` pour filtrer les données avant de les stocker dans un tableau.