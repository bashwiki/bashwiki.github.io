# [Linux] Bash csvtool : Outil pour manipuler des fichiers CSV

## Overview
Le commandement `csvtool` est un outil puissant utilisé pour manipuler et traiter des fichiers CSV (Comma-Separated Values). Il permet d'extraire, de modifier et de formater des données contenues dans ces fichiers de manière efficace.

## Usage
La syntaxe de base de la commande `csvtool` est la suivante :

```bash
csvtool [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `csvtool` :

- `cut` : Permet de sélectionner certaines colonnes d'un fichier CSV.
- `format` : Modifie le format d'affichage des données.
- `head` : Affiche les premières lignes d'un fichier CSV.
- `tail` : Affiche les dernières lignes d'un fichier CSV.
- `join` : Combine plusieurs fichiers CSV sur une clé commune.

## Common Examples

### 1. Afficher les premières lignes d'un fichier CSV
Pour afficher les 5 premières lignes d'un fichier nommé `data.csv`, utilisez :

```bash
csvtool head -n 5 data.csv
```

### 2. Sélectionner des colonnes spécifiques
Pour extraire les colonnes 1 et 3 d'un fichier `data.csv`, vous pouvez utiliser :

```bash
csvtool cut -c 1,3 data.csv
```

### 3. Joindre deux fichiers CSV
Pour joindre `file1.csv` et `file2.csv` sur la première colonne, utilisez :

```bash
csvtool join -c 1 file1.csv file2.csv
```

### 4. Modifier le format d'affichage
Pour changer le format d'affichage des données dans `data.csv`, vous pouvez exécuter :

```bash
csvtool format '%s\t%s' data.csv
```

## Tips
- Toujours vérifier la structure de votre fichier CSV avant d'utiliser `csvtool` pour éviter des erreurs de format.
- Utilisez l'option `--help` pour obtenir une liste complète des options disponibles et de leur utilisation.
- Combinez `csvtool` avec d'autres commandes Unix pour des traitements de données plus complexes.