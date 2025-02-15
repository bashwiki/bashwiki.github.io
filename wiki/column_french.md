# [리눅스] Bash column 사용법

## Overview
La commande `column` est un utilitaire de ligne de commande en Bash qui permet de formater des données en colonnes. Son objectif principal est de rendre les données textuelles plus lisibles en les organisant en colonnes alignées, ce qui est particulièrement utile lors de l'affichage de résultats de commandes ou de fichiers contenant des données tabulaires.

## Usage
La syntaxe de base de la commande `column` est la suivante :

```bash
column [options] [fichier]
```

### Options courantes :
- `-t` : Aligne les colonnes en fonction des délimiteurs, créant un tableau.
- `-s` : Définit un délimiteur personnalisé pour séparer les colonnes (par défaut, c'est l'espace).
- `-n` : Ne pas ajouter de nouvelles lignes pour les colonnes vides.
- `-x` : Remplit les colonnes horizontalement avant de passer à la colonne suivante.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `column`.

### Exemple 1 : Formatage simple
Supposons que vous ayez un fichier texte nommé `data.txt` contenant les éléments suivants :

```
Nom Age Ville
Alice 30 Paris
Bob 25 Lyon
Charlie 35 Marseille
```

Vous pouvez utiliser la commande `column` pour afficher ces données en colonnes :

```bash
column -t data.txt
```

Cela produira une sortie formatée comme suit :

```
Nom      Age  Ville
Alice    30   Paris
Bob      25   Lyon
Charlie  35   Marseille
```

### Exemple 2 : Utilisation d'un délimiteur personnalisé
Si vous avez un fichier `data.csv` avec des données séparées par des virgules :

```
Nom,Age,Ville
Alice,30,Paris
Bob,25,Lyon
Charlie,35,Marseille
```

Vous pouvez utiliser `column` avec l'option `-s` pour spécifier la virgule comme délimiteur :

```bash
column -t -s, data.csv
```

La sortie sera :

```
Nom      Age  Ville
Alice    30   Paris
Bob      25   Lyon
Charlie  35   Marseille
```

## Tips
- Pour une meilleure lisibilité, utilisez toujours l'option `-t` pour aligner les colonnes.
- Si vous travaillez avec des fichiers de données volumineux, envisagez d'utiliser `column` en combinaison avec d'autres commandes comme `cat` ou `grep` pour filtrer et formater les données avant l'affichage.
- Testez différents délimiteurs avec l'option `-s` pour voir ce qui fonctionne le mieux avec vos données spécifiques.
- Pensez à rediriger la sortie de `column` vers un fichier si vous souhaitez conserver le formatage pour une utilisation ultérieure :

```bash
column -t data.txt > formatted_data.txt
``` 

En suivant ces conseils, vous pouvez tirer le meilleur parti de la commande `column` pour améliorer la lisibilité de vos données en ligne de commande.