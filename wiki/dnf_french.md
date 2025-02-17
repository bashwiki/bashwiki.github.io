# [Linux] Bash dnf : Gestionnaire de paquets pour les distributions basées sur RPM

## Overview
La commande `dnf` (Dandified YUM) est un gestionnaire de paquets pour les distributions Linux basées sur RPM, comme Fedora et CentOS. Elle permet d'installer, de mettre à jour, de supprimer et de gérer des paquets logiciels facilement.

## Usage
La syntaxe de base de la commande `dnf` est la suivante :

```bash
dnf [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `dnf` :

- `install` : Installe un ou plusieurs paquets.
- `remove` : Supprime un ou plusieurs paquets.
- `update` : Met à jour tous les paquets installés vers la dernière version.
- `search` : Recherche un paquet dans les dépôts disponibles.
- `info` : Affiche des informations sur un paquet spécifique.
- `list` : Liste les paquets installés ou disponibles.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `dnf` :

- Pour installer un paquet, par exemple `vim` :

```bash
dnf install vim
```

- Pour supprimer un paquet, par exemple `nano` :

```bash
dnf remove nano
```

- Pour mettre à jour tous les paquets installés :

```bash
dnf update
```

- Pour rechercher un paquet, par exemple `httpd` :

```bash
dnf search httpd
```

- Pour afficher des informations sur un paquet, par exemple `curl` :

```bash
dnf info curl
```

- Pour lister tous les paquets installés :

```bash
dnf list installed
```

## Tips
- Toujours vérifier les mises à jour de sécurité en utilisant `dnf update` régulièrement.
- Utilisez `dnf clean all` pour libérer de l'espace disque en supprimant les fichiers temporaires.
- Pour éviter les conflits de dépendances, utilisez l'option `--best` lors de l'installation ou de la mise à jour d'un paquet.