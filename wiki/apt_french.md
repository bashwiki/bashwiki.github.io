# [리눅스] Bash apt 사용법

## Overview
La commande `apt` (Advanced Package Tool) est un gestionnaire de paquets utilisé sur les systèmes basés sur Debian, comme Ubuntu. Son objectif principal est de simplifier l'installation, la mise à jour et la gestion des logiciels. `apt` permet aux utilisateurs de rechercher, d'installer, de mettre à jour et de supprimer des paquets logiciels de manière efficace, tout en gérant les dépendances nécessaires.

## Usage
La syntaxe de base de la commande `apt` est la suivante :

```bash
apt [options] commande [paquet...]
```

### Options courantes :
- `update` : Met à jour la liste des paquets disponibles et de leurs versions.
- `upgrade` : Installe les mises à jour des paquets installés.
- `install` : Installe un ou plusieurs paquets spécifiés.
- `remove` : Supprime un ou plusieurs paquets spécifiés.
- `search` : Recherche un paquet dans les dépôts disponibles.
- `show` : Affiche des informations détaillées sur un paquet.

## Examples
### Exemple 1 : Mettre à jour la liste des paquets
Pour mettre à jour la liste des paquets disponibles, vous pouvez utiliser la commande suivante :

```bash
sudo apt update
```

### Exemple 2 : Installer un paquet
Pour installer un paquet, par exemple `curl`, vous pouvez exécuter :

```bash
sudo apt install curl
```

## Tips
- Toujours exécuter `apt update` avant d'installer ou de mettre à jour des paquets pour s'assurer que vous disposez des dernières informations sur les paquets disponibles.
- Utilisez `apt upgrade` pour mettre à jour tous les paquets installés en une seule commande.
- Pour éviter les problèmes de dépendances, utilisez `apt full-upgrade` qui gère les changements de dépendances plus complexes.
- Pensez à utiliser `apt search` pour trouver des paquets si vous n'êtes pas sûr du nom exact du logiciel que vous souhaitez installer.