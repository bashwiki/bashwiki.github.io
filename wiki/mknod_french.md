# [리눅스] Bash mknod 사용법

## Overview
La commande `mknod` est utilisée dans les systèmes Unix et Linux pour créer des fichiers spéciaux, tels que des fichiers de périphériques. Ces fichiers permettent à l'utilisateur d'interagir avec des périphériques matériels via le système de fichiers. Le principal objectif de `mknod` est de créer des fichiers de périphériques de type caractère ou bloc, qui sont essentiels pour la gestion des périphériques dans un environnement Unix.

## Usage
La syntaxe de base de la commande `mknod` est la suivante :

```
mknod [OPTION] NOM_TYPE NOM_FICHIER
```

### Options courantes :
- `-m, --mode=MODE` : Définit les permissions du fichier créé.
- `-b, --block` : Crée un fichier de périphérique de type bloc.
- `-c, --character` : Crée un fichier de périphérique de type caractère.

## Examples
### Exemple 1 : Création d'un fichier de périphérique de type caractère
Pour créer un fichier de périphérique de type caractère nommé `my_char_device` avec le numéro majeur 100 et le numéro mineur 0, vous pouvez utiliser la commande suivante :

```bash
mknod /dev/my_char_device c 100 0
```

### Exemple 2 : Création d'un fichier de périphérique de type bloc
Pour créer un fichier de périphérique de type bloc nommé `my_block_device` avec le numéro majeur 200 et le numéro mineur 1, utilisez la commande suivante :

```bash
mknod /dev/my_block_device b 200 1
```

## Tips
- Assurez-vous d'avoir les privilèges nécessaires (généralement en tant que superutilisateur) pour créer des fichiers de périphériques dans le répertoire `/dev`.
- Vérifiez toujours les numéros majeurs et mineurs des périphériques que vous souhaitez créer, car ils doivent correspondre à ceux attendus par le système.
- Utilisez `ls -l /dev` pour lister les fichiers de périphériques existants et vérifier leurs numéros majeurs et mineurs.
- Soyez prudent lors de la création de fichiers de périphériques, car une mauvaise configuration peut entraîner des problèmes de fonctionnement du système.