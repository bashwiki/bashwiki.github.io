# [리눅스] Bash chattr 사용법

## Overview
La commande `chattr` (change attribute) est utilisée sous Linux pour modifier les attributs des fichiers et des répertoires sur un système de fichiers. Son objectif principal est de contrôler la manière dont les fichiers peuvent être modifiés ou supprimés, offrant ainsi une couche de protection supplémentaire contre les modifications non désirées. Par exemple, il peut empêcher la suppression d'un fichier ou le rendre immuable.

## Usage
La syntaxe de base de la commande `chattr` est la suivante :

```bash
chattr [options] [attributs] [fichier]
```

### Options courantes :
- `+` : Ajoute un attribut.
- `-` : Supprime un attribut.
- `=` : Définit un attribut, remplaçant tous les attributs précédents.
- `a` : Permet d'ajouter des données à un fichier, mais empêche sa suppression.
- `i` : Rend un fichier immuable, empêchant toute modification ou suppression.
- `d` : Ignore les fichiers lors de la sauvegarde avec `dump`.

## Examples
### Exemple 1 : Rendre un fichier immuable
Pour rendre un fichier nommé `important.txt` immuable, vous pouvez utiliser la commande suivante :

```bash
chattr +i important.txt
```

Après avoir exécuté cette commande, le fichier `important.txt` ne pourra plus être modifié ou supprimé, même par l'utilisateur root.

### Exemple 2 : Retirer l'attribut immuable
Pour retirer l'attribut immuable d'un fichier, utilisez :

```bash
chattr -i important.txt
```

Cela permettra à nouveau de modifier ou de supprimer le fichier.

## Tips
- Utilisez `lsattr` pour vérifier les attributs des fichiers dans un répertoire. Cela vous permet de voir quels attributs sont actuellement appliqués.
- Soyez prudent lors de l'utilisation de l'attribut immuable (`i`), car il peut rendre la gestion des fichiers plus complexe si vous oubliez que cet attribut est actif.
- Les attributs de fichiers ne sont pas transférés lors de la copie de fichiers avec des commandes comme `cp`. Si vous avez besoin de conserver ces attributs, envisagez d'utiliser des outils spécifiques ou des systèmes de sauvegarde qui prennent en charge les attributs de fichiers.

En suivant ces conseils et en utilisant `chattr` judicieusement, vous pouvez renforcer la sécurité et la gestion de vos fichiers sous Linux.