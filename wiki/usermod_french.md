# [Linux] Bash usermod : Gérer les utilisateurs

## Overview
La commande `usermod` est utilisée pour modifier les comptes d'utilisateurs sur un système Linux. Elle permet d'ajuster divers paramètres d'un utilisateur, tels que le groupe d'appartenance, le nom d'utilisateur, le répertoire personnel, et plus encore.

## Usage
La syntaxe de base de la commande `usermod` est la suivante :

```bash
usermod [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `usermod` :

- `-aG` : Ajoute l'utilisateur à un ou plusieurs groupes supplémentaires.
- `-d` : Change le répertoire personnel de l'utilisateur.
- `-l` : Modifie le nom d'utilisateur.
- `-s` : Change le shell par défaut de l'utilisateur.
- `-u` : Change l'UID (identifiant utilisateur) de l'utilisateur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `usermod` :

1. **Ajouter un utilisateur à un groupe** :
   ```bash
   usermod -aG sudo nom_utilisateur
   ```
   Cet exemple ajoute `nom_utilisateur` au groupe `sudo`, lui permettant d'exécuter des commandes avec des privilèges élevés.

2. **Changer le répertoire personnel d'un utilisateur** :
   ```bash
   usermod -d /nouveau/repertoire nom_utilisateur
   ```
   Cela modifie le répertoire personnel de `nom_utilisateur` vers `/nouveau/repertoire`.

3. **Modifier le nom d'utilisateur** :
   ```bash
   usermod -l nouveau_nom ancien_nom
   ```
   Cet exemple change le nom d'utilisateur de `ancien_nom` à `nouveau_nom`.

4. **Changer le shell par défaut d'un utilisateur** :
   ```bash
   usermod -s /bin/zsh nom_utilisateur
   ```
   Cela définit `/bin/zsh` comme le shell par défaut pour `nom_utilisateur`.

## Tips
- Toujours faire une sauvegarde des données importantes avant de modifier les comptes d'utilisateurs.
- Utilisez `usermod` avec précaution, car des modifications incorrectes peuvent empêcher un utilisateur de se connecter.
- Vérifiez les groupes d'un utilisateur après modification avec la commande `groups nom_utilisateur` pour confirmer que les changements ont été appliqués correctement.