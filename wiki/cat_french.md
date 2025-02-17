# [Linux] Bash cat utilisation : Afficher le contenu des fichiers

## Overview
La commande `cat` (abréviation de "concatenate") est utilisée pour afficher le contenu des fichiers dans le terminal. Elle permet également de combiner plusieurs fichiers en un seul ou de créer de nouveaux fichiers à partir de l'entrée standard.

## Usage
La syntaxe de base de la commande `cat` est la suivante :

```bash
cat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `cat` :

- `-n` : Numérote toutes les lignes de sortie.
- `-b` : Numérote uniquement les lignes non vides.
- `-E` : Affiche un symbole `$` à la fin de chaque ligne.
- `-s` : Supprime les lignes vides supplémentaires.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cat` :

1. **Afficher le contenu d'un fichier :**
   ```bash
   cat fichier.txt
   ```

2. **Afficher le contenu de plusieurs fichiers :**
   ```bash
   cat fichier1.txt fichier2.txt
   ```

3. **Créer un nouveau fichier à partir de l'entrée standard :**
   ```bash
   cat > nouveau_fichier.txt
   ```
   (Tapez votre texte, puis appuyez sur `CTRL+D` pour enregistrer.)

4. **Numéroter les lignes d'un fichier :**
   ```bash
   cat -n fichier.txt
   ```

5. **Supprimer les lignes vides supplémentaires :**
   ```bash
   cat -s fichier.txt
   ```

## Tips
- Utilisez `cat` avec prudence pour les fichiers très volumineux, car cela peut surcharger le terminal.
- Combinez `cat` avec d'autres commandes comme `grep` pour filtrer le contenu affiché.
- Pour une meilleure lisibilité, envisagez d'utiliser `less` ou `more` pour parcourir de longs fichiers au lieu de `cat`.