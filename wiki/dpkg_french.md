# [리눅스] Bash dpkg 사용법

## Overview
Le command `dpkg` est un outil de gestion de paquets pour les systèmes basés sur Debian, comme Ubuntu. Il permet d'installer, de supprimer et de gérer les paquets logiciels au niveau local. `dpkg` est souvent utilisé pour manipuler des fichiers `.deb`, qui sont des archives contenant des fichiers nécessaires à l'installation d'un logiciel.

## Usage
La syntaxe de base de la commande `dpkg` est la suivante :

```bash
dpkg [options] <command>
```

### Options courantes :
- `-i` : Installe un paquet à partir d'un fichier `.deb`.
- `-r` : Supprime un paquet tout en conservant ses fichiers de configuration.
- `-P` : Supprime un paquet ainsi que ses fichiers de configuration.
- `-l` : Liste tous les paquets installés.
- `-s` : Affiche l'état d'un paquet spécifique.
- `-L` : Liste les fichiers installés par un paquet.

## Examples
### Exemple 1 : Installer un paquet
Pour installer un paquet à partir d'un fichier `.deb`, utilisez la commande suivante :

```bash
sudo dpkg -i nom_du_paquet.deb
```

### Exemple 2 : Lister les paquets installés
Pour afficher tous les paquets installés sur votre système, exécutez :

```bash
dpkg -l
```

## Tips
- Assurez-vous d'utiliser `sudo` si vous n'avez pas les privilèges nécessaires pour installer ou supprimer des paquets.
- Après l'installation d'un paquet avec `dpkg`, il peut être nécessaire d'exécuter `sudo apt-get install -f` pour corriger les dépendances manquantes.
- Utilisez `dpkg -s nom_du_paquet` pour vérifier si un paquet est installé et obtenir des informations supplémentaires à son sujet.
- Pour une gestion plus avancée des paquets, envisagez d'utiliser `apt` qui gère les dépendances automatiquement.