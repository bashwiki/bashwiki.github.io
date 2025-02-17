# [Linux] Bash column usage : Organiser les données en colonnes

## Overview
La commande `column` est utilisée pour formater les données en colonnes, ce qui facilite la lecture et l'analyse des informations affichées dans le terminal. Elle prend en entrée des données séparées par des espaces ou des tabulations et les réorganise pour les présenter de manière structurée.

## Usage
La syntaxe de base de la commande `column` est la suivante :

```bash
column [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `column` :

- `-t` : Crée un tableau en alignant les colonnes.
- `-s` : Définit un séparateur personnalisé (par défaut, c'est l'espace).
- `-n` : Ne pas ajouter de nouvelles lignes pour les lignes vides.
- `-x` : Remplit les colonnes de manière horizontale avant de passer à la suivante.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `column` :

1. **Aligner des données par défaut** :
   ```bash
   cat fichier.txt | column
   ```

2. **Utiliser un séparateur personnalisé** :
   ```bash
   cat fichier.csv | column -s, -t
   ```

3. **Créer un tableau à partir d'une liste d'éléments** :
   ```bash
   echo -e "Nom Âge\nAlice 30\nBob 25" | column -t
   ```

4. **Remplir les colonnes horizontalement** :
   ```bash
   echo -e "A\nB\nC\nD\nE" | column -x
   ```

## Tips
- Utilisez l'option `-t` pour toujours obtenir une sortie bien formatée, surtout lorsque vous travaillez avec des fichiers de données.
- Si vous traitez des fichiers CSV, n'oubliez pas de spécifier le séparateur avec `-s`.
- Pour des données très larges, envisagez de combiner `column` avec d'autres commandes comme `sort` ou `grep` pour un traitement plus efficace.