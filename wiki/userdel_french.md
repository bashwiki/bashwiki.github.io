# [리눅스] Bash userdel 사용법

## Overview
La commande `userdel` est utilisée dans les systèmes basés sur Linux pour supprimer un compte utilisateur. Son objectif principal est de retirer les informations d'un utilisateur du système, ce qui inclut la suppression de l'entrée correspondante dans le fichier `/etc/passwd` et, si spécifié, la suppression de son répertoire personnel et de ses fichiers associés.

## Usage
La syntaxe de base de la commande `userdel` est la suivante :

```bash
userdel [options] nom_utilisateur
```

### Options courantes :
- `-r` : Supprime le répertoire personnel de l'utilisateur ainsi que son contenu.
- `-f` : Force la suppression de l'utilisateur, même s'il est connecté.
- `-Z` : Supprime les attributs SELinux de l'utilisateur.

## Examples
### Exemple 1 : Suppression d'un utilisateur sans supprimer son répertoire personnel
Pour supprimer un utilisateur nommé `utilisateur1` sans toucher à son répertoire personnel, vous pouvez utiliser la commande suivante :

```bash
sudo userdel utilisateur1
```

### Exemple 2 : Suppression d'un utilisateur avec son répertoire personnel
Pour supprimer un utilisateur nommé `utilisateur2` ainsi que son répertoire personnel et tous ses fichiers, utilisez l'option `-r` :

```bash
sudo userdel -r utilisateur2
```

## Tips
- Avant de supprimer un utilisateur, il est conseillé de vérifier s'il est actuellement connecté au système. Vous pouvez utiliser la commande `who` pour lister les utilisateurs connectés.
- Pensez à faire une sauvegarde des données importantes avant de supprimer un compte utilisateur, surtout si vous utilisez l'option `-r`.
- Utilisez la commande `userdel` avec précaution, car une fois qu'un utilisateur est supprimé, il ne peut pas être récupéré facilement.