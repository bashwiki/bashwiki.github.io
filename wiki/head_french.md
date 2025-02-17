# [Linux] Bash head utilisation : Afficher les premières lignes d'un fichier

## Overview
La commande `head` est utilisée pour afficher les premières lignes d'un fichier texte. Par défaut, elle montre les 10 premières lignes, mais cela peut être modifié à l'aide d'options.

## Usage
La syntaxe de base de la commande `head` est la suivante :

```bash
head [options] [arguments]
```

## Common Options
- `-n [nombre]` : Spécifie le nombre de lignes à afficher. Par exemple, `-n 5` affichera les 5 premières lignes.
- `-c [nombre]` : Affiche le nombre de caractères spécifié au lieu de lignes.
- `-q` : Ne pas afficher les noms de fichiers lors de l'affichage de plusieurs fichiers.
- `-v` : Toujours afficher les noms de fichiers, même s'il n'y a qu'un seul fichier.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `head` :

1. Afficher les 10 premières lignes d'un fichier :
   ```bash
   head fichier.txt
   ```

2. Afficher les 5 premières lignes d'un fichier :
   ```bash
   head -n 5 fichier.txt
   ```

3. Afficher les 20 premiers caractères d'un fichier :
   ```bash
   head -c 20 fichier.txt
   ```

4. Afficher les 10 premières lignes de plusieurs fichiers :
   ```bash
   head fichier1.txt fichier2.txt
   ```

5. Afficher les 5 premières lignes sans afficher les noms de fichiers :
   ```bash
   head -q -n 5 fichier1.txt fichier2.txt
   ```

## Tips
- Utilisez `head` en combinaison avec d'autres commandes, comme `grep`, pour filtrer les résultats avant d'afficher les premières lignes.
- Pour visualiser rapidement le début d'un fichier volumineux, `head` est plus efficace que d'ouvrir le fichier entier dans un éditeur de texte.
- Pensez à utiliser l'option `-v` si vous travaillez avec plusieurs fichiers et souhaitez garder une trace de l'origine des lignes affichées.