# [Linux] Bash id : afficher les informations d'identité d'un utilisateur

## Overview
La commande `id` est utilisée dans les systèmes Unix et Linux pour afficher les informations d'identité d'un utilisateur, y compris son UID (User ID), son GID (Group ID) et les groupes auxquels il appartient. C'est un outil essentiel pour la gestion des utilisateurs et des permissions.

## Usage
La syntaxe de base de la commande `id` est la suivante :

```bash
id [options] [arguments]
```

## Common Options
- `-u` : Affiche uniquement l'UID de l'utilisateur.
- `-g` : Affiche uniquement le GID du groupe principal de l'utilisateur.
- `-G` : Affiche tous les GIDs des groupes auxquels l'utilisateur appartient.
- `-n` : Affiche les noms au lieu des identifiants numériques.
- `-r` : Affiche l'UID ou le GID en mode "réel" (non effectif).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `id` :

1. Afficher les informations d'identité de l'utilisateur actuel :
   ```bash
   id
   ```

2. Afficher uniquement l'UID de l'utilisateur actuel :
   ```bash
   id -u
   ```

3. Afficher uniquement le GID du groupe principal de l'utilisateur actuel :
   ```bash
   id -g
   ```

4. Afficher tous les GIDs des groupes auxquels l'utilisateur actuel appartient :
   ```bash
   id -G
   ```

5. Afficher les informations d'identité d'un utilisateur spécifique (par exemple, "alice") :
   ```bash
   id alice
   ```

6. Afficher les noms des groupes au lieu des identifiants numériques :
   ```bash
   id -nG
   ```

## Tips
- Utilisez `id` sans options pour obtenir un aperçu complet de votre identité d'utilisateur.
- Combinez les options pour obtenir des informations spécifiques, par exemple, `id -u -n` pour afficher le nom de l'utilisateur actuel avec son UID.
- Vérifiez les permissions des fichiers et des répertoires en utilisant `id` pour comprendre à quels groupes vous appartenez.