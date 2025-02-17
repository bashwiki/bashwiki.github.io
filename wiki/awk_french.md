# [Linux] Bash awk utilisation : Traitement et analyse de texte

## Overview
La commande `awk` est un puissant outil de traitement de texte et d'analyse de données en ligne de commande. Elle permet de manipuler et d'extraire des informations à partir de fichiers texte ou de flux de données, en utilisant des motifs et des actions définis par l'utilisateur.

## Usage
La syntaxe de base de la commande `awk` est la suivante :

```bash
awk [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `awk` :

- `-F` : Définit le séparateur de champs (par défaut, c'est un espace ou une tabulation).
- `-v` : Permet de définir une variable avant l'exécution du programme `awk`.
- `-f` : Spécifie un fichier contenant le programme `awk` à exécuter.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `awk` :

1. **Afficher la première colonne d'un fichier :**
   ```bash
   awk '{print $1}' fichier.txt
   ```

2. **Utiliser un séparateur de champs personnalisé (par exemple, une virgule) :**
   ```bash
   awk -F',' '{print $2}' fichier.csv
   ```

3. **Compter le nombre de lignes dans un fichier :**
   ```bash
   awk 'END {print NR}' fichier.txt
   ```

4. **Filtrer les lignes contenant un mot spécifique :**
   ```bash
   awk '/mot/' fichier.txt
   ```

5. **Calculer la somme d'une colonne numérique :**
   ```bash
   awk '{s+=$1} END {print s}' fichier.txt
   ```

## Tips
- Utilisez des commentaires dans vos scripts `awk` pour rendre le code plus lisible.
- Testez vos commandes `awk` avec des fichiers d'exemple avant de les appliquer à des données critiques.
- Combinez `awk` avec d'autres commandes Unix pour des traitements plus complexes, par exemple en utilisant des pipes (`|`).