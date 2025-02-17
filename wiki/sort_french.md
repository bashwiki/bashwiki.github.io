# [Linux] Bash sort utilisation : Trier les lignes d'un fichier

## Overview
La commande `sort` est utilisée pour trier les lignes d'un fichier ou d'une entrée standard. Elle peut trier les données par ordre alphabétique, numérique ou selon d'autres critères spécifiés par l'utilisateur.

## Usage
La syntaxe de base de la commande `sort` est la suivante :

```bash
sort [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `sort` :

- `-n` : Trie les lignes en utilisant l'ordre numérique.
- `-r` : Inverse l'ordre de tri (tri décroissant).
- `-k` : Spécifie une colonne ou un champ à utiliser pour le tri.
- `-u` : Supprime les doublons des résultats.
- `-o` : Écrit le résultat dans un fichier spécifié.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `sort` :

1. Trier un fichier par ordre alphabétique :
   ```bash
   sort fichier.txt
   ```

2. Trier un fichier numériquement :
   ```bash
   sort -n nombres.txt
   ```

3. Trier un fichier en ordre décroissant :
   ```bash
   sort -r fichier.txt
   ```

4. Trier en utilisant une colonne spécifique (par exemple, la deuxième colonne) :
   ```bash
   sort -k2 fichier.txt
   ```

5. Écrire le résultat trié dans un nouveau fichier :
   ```bash
   sort fichier.txt -o fichier_trie.txt
   ```

6. Supprimer les doublons lors du tri :
   ```bash
   sort -u fichier.txt
   ```

## Tips
- Utilisez l'option `-o` pour éviter d'écraser votre fichier d'origine si vous souhaitez sauvegarder le résultat trié dans un nouveau fichier.
- Pour trier des fichiers très volumineux, envisagez d'utiliser l'option `--parallel` pour améliorer les performances.
- Combinez `sort` avec d'autres commandes comme `uniq` pour des opérations de traitement de texte plus avancées.