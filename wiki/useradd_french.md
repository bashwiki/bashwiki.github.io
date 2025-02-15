# [리눅스] Bash useradd 사용법

## Overview
La commande `useradd` est utilisée pour créer un nouvel utilisateur sur un système Linux. Son objectif principal est d'ajouter un compte utilisateur au système, permettant ainsi à l'utilisateur d'accéder aux ressources et services disponibles. Cette commande est souvent utilisée par les administrateurs système pour gérer les utilisateurs et leurs permissions.

## Usage
La syntaxe de base de la commande `useradd` est la suivante :

```bash
useradd [options] nom_utilisateur
```

### Options courantes :
- `-m` : Crée un répertoire personnel pour l'utilisateur.
- `-s` : Définit le shell par défaut pour l'utilisateur (par exemple, `/bin/bash`).
- `-G` : Ajoute l'utilisateur à un ou plusieurs groupes supplémentaires, séparés par des virgules.
- `-c` : Ajoute un commentaire, souvent utilisé pour indiquer le nom complet de l'utilisateur.
- `-d` : Spécifie le chemin du répertoire personnel de l'utilisateur.

## Examples
### Exemple 1 : Création d'un utilisateur avec un répertoire personnel
Pour créer un nouvel utilisateur nommé `alice` avec un répertoire personnel, vous pouvez utiliser la commande suivante :

```bash
sudo useradd -m alice
```

### Exemple 2 : Création d'un utilisateur avec un shell spécifique et ajout à un groupe
Pour créer un utilisateur nommé `bob`, avec un shell par défaut de `/bin/bash` et l'ajouter au groupe `developers`, utilisez :

```bash
sudo useradd -m -s /bin/bash -G developers bob
```

## Tips
- Toujours vérifier les utilisateurs existants avec la commande `cat /etc/passwd` avant de créer un nouvel utilisateur pour éviter les conflits de noms.
- Utilisez l'option `-c` pour ajouter des informations utiles sur l'utilisateur, ce qui peut faciliter la gestion des comptes.
- Pensez à définir un mot de passe pour le nouvel utilisateur avec la commande `passwd` après avoir créé le compte, par exemple :

```bash
sudo passwd alice
```
- Pour une gestion plus avancée des utilisateurs, envisagez d'utiliser des outils comme `usermod` et `userdel` pour modifier ou supprimer des comptes utilisateur respectivement.