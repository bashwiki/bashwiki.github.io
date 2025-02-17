# [Linux] Bash rmdir : Supprimer des répertoires vides

## Overview
La commande `rmdir` est utilisée pour supprimer des répertoires vides dans un système de fichiers. Si le répertoire contient des fichiers ou d'autres répertoires, la commande échouera et ne supprimera rien.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
rmdir [options] [arguments]
```

## Common Options
- `-p` : Supprime le répertoire spécifié ainsi que ses parents vides.
- `--ignore-fail-on-non-empty` : Ignore les erreurs si le répertoire n'est pas vide.
- `--verbose` : Affiche un message pour chaque répertoire supprimé.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `rmdir` :

1. Supprimer un répertoire vide :
   ```bash
   rmdir mon_repertoire
   ```

2. Supprimer un répertoire vide et ses parents vides :
   ```bash
   rmdir -p parent/enfant
   ```

3. Supprimer plusieurs répertoires vides à la fois :
   ```bash
   rmdir repertoire1 repertoire2
   ```

4. Utiliser l'option verbose pour voir les répertoires supprimés :
   ```bash
   rmdir --verbose mon_repertoire
   ```

## Tips
- Assurez-vous que le répertoire est vide avant d'utiliser `rmdir`, sinon la commande échouera.
- Utilisez l'option `-p` pour nettoyer les répertoires parents vides en une seule commande.
- Pour vérifier le contenu d'un répertoire avant de le supprimer, utilisez `ls` pour éviter des erreurs.