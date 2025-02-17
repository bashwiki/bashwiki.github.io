# [Linux] Bash xargs : Exécuter des commandes avec des arguments

## Overview
La commande `xargs` est utilisée pour construire et exécuter des commandes à partir de l'entrée standard. Elle permet de passer des arguments à d'autres commandes, ce qui est particulièrement utile lorsque le nombre d'arguments dépasse la limite de la ligne de commande.

## Usage
La syntaxe de base de la commande `xargs` est la suivante :

```bash
xargs [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `xargs` :

- `-n N` : Limite le nombre d'arguments par commande à N.
- `-d DELIMITER` : Utilise un délimiteur spécifique au lieu de l'espace ou de la nouvelle ligne.
- `-0` : Traite l'entrée comme une liste de fichiers séparés par des caractères null (utile avec `find`).
- `-p` : Demande confirmation avant d'exécuter chaque commande.
- `-I {}` : Remplace `{}` par l'argument en cours dans la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `xargs` :

1. **Supprimer des fichiers listés dans un fichier :**
   ```bash
   cat fichiers_a_supprimer.txt | xargs rm
   ```

2. **Compresser tous les fichiers `.txt` dans un répertoire :**
   ```bash
   find . -name "*.txt" | xargs gzip
   ```

3. **Compter le nombre de lignes dans plusieurs fichiers :**
   ```bash
   ls *.txt | xargs wc -l
   ```

4. **Utiliser un délimiteur spécifique :**
   ```bash
   echo -e "fichier1.txt\nfichier2.txt" | xargs -d '\n' cp -t /destination/
   ```

5. **Exécuter une commande avec confirmation :**
   ```bash
   echo "fichier1.txt" | xargs -p rm
   ```

## Tips
- Utilisez l'option `-0` avec `find` pour éviter les problèmes avec les espaces dans les noms de fichiers.
- Combinez `xargs` avec `find` pour traiter un grand nombre de fichiers efficacement.
- Soyez prudent avec les commandes destructrices comme `rm` ; utilisez l'option `-p` pour confirmer avant l'exécution.