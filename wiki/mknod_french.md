# [Linux] Bash mknod : Créer des fichiers spéciaux

## Overview
La commande `mknod` est utilisée pour créer des fichiers spéciaux dans le système de fichiers Linux. Ces fichiers peuvent représenter des périphériques, tels que des disques durs ou des ports série, permettant ainsi aux programmes d'interagir avec le matériel.

## Usage
La syntaxe de base de la commande `mknod` est la suivante :

```bash
mknod [options] [arguments]
```

## Common Options
- `-m, --mode=MODE` : Définit les permissions du fichier créé.
- `-b, --block` : Crée un fichier de périphérique de type bloc.
- `-c, --char` : Crée un fichier de périphérique de type caractère.
- `-h, --help` : Affiche l'aide et les options disponibles pour la commande.
- `-V, --version` : Affiche la version de `mknod`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mknod` :

### Créer un fichier de périphérique de caractère
```bash
mknod /dev/mon_peripherique c 100 0
```
Dans cet exemple, un fichier de périphérique de caractère est créé avec un numéro majeur de 100 et un numéro mineur de 0.

### Créer un fichier de périphérique de bloc
```bash
mknod /dev/mon_disque b 200 0
```
Ici, un fichier de périphérique de bloc est créé avec un numéro majeur de 200 et un numéro mineur de 0.

### Définir des permissions lors de la création
```bash
mknod -m 660 /dev/mon_peripherique c 100 0
```
Cet exemple crée un fichier de périphérique de caractère avec des permissions définies à 660.

## Tips
- Assurez-vous d'avoir les droits d'administrateur (root) pour créer des fichiers spéciaux dans `/dev`.
- Utilisez `ls -l /dev` pour vérifier les fichiers de périphériques existants et leurs permissions.
- Soyez prudent lors de la création de fichiers de périphériques, car une mauvaise configuration peut entraîner des problèmes de système.