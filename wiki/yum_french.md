# [리눅스] Bash yum 사용법

## Overview
Le commandement `yum` (Yellowdog Updater Modified) est un gestionnaire de paquets pour les systèmes basés sur RPM (Red Hat Package Manager). Son principal objectif est de faciliter l'installation, la mise à jour et la suppression de logiciels sur les distributions Linux telles que Red Hat, CentOS et Fedora. `yum` gère également les dépendances, ce qui signifie qu'il s'assure que tous les paquets nécessaires à l'installation d'un logiciel sont également installés.

## Usage
La syntaxe de base de la commande `yum` est la suivante :

```bash
yum [options] [command] [package]
```

### Options courantes :
- `install` : Installe un ou plusieurs paquets.
- `remove` : Supprime un ou plusieurs paquets.
- `update` : Met à jour tous les paquets installés ou un paquet spécifique.
- `search` : Recherche un paquet dans les dépôts configurés.
- `info` : Affiche des informations sur un paquet spécifique.
- `list` : Liste les paquets disponibles, installés ou obsolètes.

## Examples
### Exemple 1 : Installer un paquet
Pour installer un paquet, par exemple `httpd` (serveur web Apache), vous pouvez utiliser la commande suivante :

```bash
yum install httpd
```

### Exemple 2 : Mettre à jour tous les paquets
Pour mettre à jour tous les paquets installés sur votre système, exécutez :

```bash
yum update
```

## Tips
- **Utiliser `yum clean all`** : Cette commande permet de nettoyer le cache de `yum`, ce qui peut libérer de l'espace disque et résoudre certains problèmes de mise à jour.
- **Vérifier les dépendances** : Avant d'installer un paquet, utilisez `yum info [package]` pour vérifier les dépendances et les versions disponibles.
- **Utiliser `yum history`** : Cette commande vous permet de voir l'historique des transactions `yum`, ce qui peut être utile pour le dépannage ou pour revenir à une version antérieure d'un paquet.

En suivant ces conseils et en utilisant `yum` de manière efficace, vous pourrez gérer facilement les logiciels sur votre système Linux.