# [Linux] Bash fgrep Utilisation : Recherche de chaînes fixes dans des fichiers

## Overview
La commande `fgrep` est utilisée pour rechercher des chaînes de caractères fixes dans des fichiers. Contrairement à `grep`, `fgrep` ne traite pas les expressions régulières, ce qui en fait un outil rapide pour des recherches littérales.

## Usage
La syntaxe de base de la commande `fgrep` est la suivante :

```bash
fgrep [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `fgrep` :

- `-i` : Ignore la casse lors de la recherche.
- `-v` : Inverse la recherche, affichant les lignes qui ne contiennent pas la chaîne.
- `-c` : Affiche le nombre de lignes correspondantes au lieu des lignes elles-mêmes.
- `-n` : Affiche les numéros de ligne avec les lignes correspondantes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `fgrep` :

1. **Recherche d'une chaîne dans un fichier :**
   ```bash
   fgrep "chaîne" fichier.txt
   ```

2. **Recherche sans tenir compte de la casse :**
   ```bash
   fgrep -i "chaîne" fichier.txt
   ```

3. **Compter le nombre de lignes contenant une chaîne :**
   ```bash
   fgrep -c "chaîne" fichier.txt
   ```

4. **Afficher les lignes qui ne contiennent pas une chaîne :**
   ```bash
   fgrep -v "chaîne" fichier.txt
   ```

5. **Afficher les numéros de ligne avec les résultats :**
   ```bash
   fgrep -n "chaîne" fichier.txt
   ```

## Tips
- Utilisez `fgrep` lorsque vous avez besoin de rechercher des chaînes fixes pour une performance optimale.
- Combinez les options pour affiner vos recherches, par exemple, `fgrep -i -n "chaîne" fichier.txt` pour une recherche insensible à la casse avec numéros de ligne.
- Pensez à rediriger la sortie vers un fichier si vous traitez de grandes quantités de données, par exemple : `fgrep "chaîne" fichier.txt > résultats.txt`.