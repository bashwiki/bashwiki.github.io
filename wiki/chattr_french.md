# [Linux] Bash chattr utilisation : Gérer les attributs des fichiers

## Overview
La commande `chattr` permet de modifier les attributs des fichiers dans un système de fichiers Linux. Elle est principalement utilisée pour protéger des fichiers contre des modifications accidentelles ou non autorisées.

## Usage
La syntaxe de base de la commande `chattr` est la suivante :

```bash
chattr [options] [arguments]
```

## Common Options
Voici quelques options courantes de `chattr` avec de brèves explications :

- `+a` : Permet d'ajouter un attribut, rendant le fichier append-only (ajout uniquement).
- `+i` : Rend le fichier immuable, empêchant toute modification.
- `-a` : Supprime l'attribut append-only.
- `-i` : Supprime l'attribut immuable.
- `-R` : Applique les changements de manière récursive à tous les fichiers dans un répertoire.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `chattr` :

1. Rendre un fichier immuable :
   ```bash
   chattr +i mon_fichier.txt
   ```

2. Rendre un fichier append-only :
   ```bash
   chattr +a mon_log.txt
   ```

3. Supprimer l'attribut immuable d'un fichier :
   ```bash
   chattr -i mon_fichier.txt
   ```

4. Appliquer l'attribut immuable à tous les fichiers d'un répertoire :
   ```bash
   chattr +i -R mon_repertoire/
   ```

## Tips
- Utilisez `lsattr` pour vérifier les attributs des fichiers avant de les modifier.
- Soyez prudent lors de l'utilisation de l'attribut immuable, car il peut rendre difficile la suppression ou la modification du fichier.
- Pensez à documenter les changements d'attributs pour éviter toute confusion au sein de votre équipe.