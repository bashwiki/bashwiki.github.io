# [리눅스] Bash rmdir 사용법

## Overview
La commande `rmdir` est utilisée dans les systèmes Unix et Linux pour supprimer des répertoires vides. Son principal objectif est de permettre aux utilisateurs de gérer la structure de fichiers en supprimant les répertoires qui ne contiennent aucun fichier ou sous-répertoire. Si le répertoire n'est pas vide, la commande échouera et affichera un message d'erreur.

## Usage
La syntaxe de base de la commande `rmdir` est la suivante :

```bash
rmdir [options] répertoire
```

### Options courantes
- `-p` : Supprime le répertoire spécifié ainsi que tous ses répertoires parents vides.
- `--ignore-fail-on-non-empty` : Ignore les erreurs si le répertoire n'est pas vide.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `rmdir`.

### Exemple 1 : Supprimer un répertoire vide
Pour supprimer un répertoire vide nommé `mon_dossier`, vous pouvez utiliser la commande suivante :

```bash
rmdir mon_dossier
```

### Exemple 2 : Supprimer un répertoire et ses parents vides
Si vous avez un répertoire `parent` qui contient un sous-répertoire `enfant`, et que vous souhaitez supprimer `enfant` ainsi que `parent` si celui-ci est également vide, utilisez :

```bash
rmdir -p parent/enfant
```

## Tips
- Assurez-vous que le répertoire que vous souhaitez supprimer est bien vide avant d'utiliser `rmdir`, car la commande échouera si des fichiers ou des sous-répertoires sont présents.
- Utilisez l'option `-p` avec précaution, car elle supprimera tous les répertoires parents vides, ce qui pourrait entraîner la suppression de plusieurs répertoires en une seule commande.
- Pour vérifier le contenu d'un répertoire avant de le supprimer, utilisez la commande `ls` pour éviter des erreurs potentielles.