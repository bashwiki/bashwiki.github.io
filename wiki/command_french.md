# [Linux] Bash command usage : [afficher le contenu d'un fichier]

## Overview
La commande `cat` est utilisée pour afficher le contenu d'un fichier texte dans le terminal. Elle peut également être utilisée pour concaténer plusieurs fichiers et les afficher ou les rediriger vers un autre fichier.

## Usage
La syntaxe de base de la commande `cat` est la suivante :

```bash
cat [options] [fichiers]
```

## Common Options
- `-n` : Numérote toutes les lignes de la sortie.
- `-b` : Numérote seulement les lignes non vides.
- `-E` : Affiche un symbole `$` à la fin de chaque ligne.
- `-s` : Supprime les lignes vides répétées.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cat` :

1. Afficher le contenu d'un fichier :
   ```bash
   cat fichier.txt
   ```

2. Afficher plusieurs fichiers à la suite :
   ```bash
   cat fichier1.txt fichier2.txt
   ```

3. Numéroter les lignes d'un fichier :
   ```bash
   cat -n fichier.txt
   ```

4. Rediriger le contenu d'un fichier vers un autre fichier :
   ```bash
   cat fichier1.txt > fichier2.txt
   ```

5. Supprimer les lignes vides répétées :
   ```bash
   cat -s fichier.txt
   ```

## Tips
- Utilisez `cat` avec prudence pour les fichiers très volumineux, car cela peut surcharger le terminal. Dans ce cas, envisagez d'utiliser `less` ou `more`.
- Pour combiner plusieurs fichiers en un seul, vous pouvez utiliser `cat` avec la redirection `>` pour créer un nouveau fichier.
- N'oubliez pas que `cat` peut également être utilisé pour créer un nouveau fichier en entrant du texte directement dans le terminal, en utilisant `cat > nouveau_fichier.txt`.