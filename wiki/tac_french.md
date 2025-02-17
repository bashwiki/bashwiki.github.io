# [Linux] Bash tac Utilisation : Inverser le contenu des fichiers

## Overview
La commande `tac` est utilisée pour afficher le contenu d'un fichier en inversant l'ordre des lignes. Contrairement à la commande `cat`, qui affiche les lignes dans l'ordre normal, `tac` commence par la dernière ligne et termine par la première.

## Usage
La syntaxe de base de la commande `tac` est la suivante :

```bash
tac [options] [arguments]
```

## Common Options
- `-r`, `--regexp`: Interprète les motifs comme des expressions régulières.
- `-s`, `--separator`: Définit un séparateur personnalisé entre les lignes.
- `-b`, `--before`: Affiche le contenu avant le séparateur spécifié.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `tac` :

1. **Inverser le contenu d'un fichier :**
   ```bash
   tac fichier.txt
   ```

2. **Inverser le contenu d'un fichier avec un séparateur :**
   ```bash
   tac -s "," fichier.csv
   ```

3. **Utiliser tac avec une expression régulière :**
   ```bash
   tac -r fichier.txt
   ```

4. **Afficher le contenu d'un fichier en inversant les lignes et en ajoutant un séparateur :**
   ```bash
   tac -s " " fichier.txt
   ```

## Tips
- Utilisez `tac` en combinaison avec d'autres commandes comme `grep` ou `sort` pour des manipulations de texte plus avancées.
- Pensez à rediriger la sortie de `tac` vers un nouveau fichier si vous souhaitez conserver l'ordre inversé :
  ```bash
  tac fichier.txt > fichier_inverse.txt
  ```
- Pour visualiser rapidement les dernières lignes d'un fichier, `tac` peut être très utile, surtout pour les fichiers de logs.