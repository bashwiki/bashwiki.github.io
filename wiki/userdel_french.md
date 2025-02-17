# [Linux] Bash userdel : Supprimer un utilisateur du système

## Overview
La commande `userdel` est utilisée pour supprimer un compte utilisateur du système Linux. Elle permet de retirer les informations de l'utilisateur ainsi que, si spécifié, son répertoire personnel et ses fichiers.

## Usage
La syntaxe de base de la commande `userdel` est la suivante :

```bash
userdel [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `userdel` :

- `-r` : Supprime le répertoire personnel de l'utilisateur et son contenu.
- `-f` : Force la suppression de l'utilisateur, même s'il est connecté.
- `-Z` : Supprime l'utilisateur tout en conservant les attributs de sécurité SELinux.

## Common Examples

### Supprimer un utilisateur sans supprimer son répertoire personnel
```bash
userdel nom_utilisateur
```

### Supprimer un utilisateur et son répertoire personnel
```bash
userdel -r nom_utilisateur
```

### Forcer la suppression d'un utilisateur
```bash
userdel -f nom_utilisateur
```

### Supprimer un utilisateur tout en conservant les attributs SELinux
```bash
userdel -Z nom_utilisateur
```

## Tips
- Toujours vérifier que l'utilisateur n'est pas connecté avant de le supprimer, pour éviter des problèmes.
- Utiliser l'option `-r` avec précaution, car cela supprimera définitivement tous les fichiers de l'utilisateur.
- Considérer de faire une sauvegarde des données de l'utilisateur avant de procéder à sa suppression.