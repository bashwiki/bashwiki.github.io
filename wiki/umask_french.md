# [Linux] Bash umask Utilisation : Gérer les permissions par défaut des fichiers

## Overview
La commande `umask` définit les permissions par défaut pour les nouveaux fichiers et répertoires créés dans un système Linux. Elle détermine quelles permissions seront retirées lors de la création d'un fichier, influençant ainsi la sécurité et l'accès aux fichiers.

## Usage
La syntaxe de base de la commande `umask` est la suivante :

```bash
umask [options] [arguments]
```

## Common Options
- `-S` : Affiche les permissions sous forme symbolique.
- `-p` : Affiche la valeur actuelle de umask dans un format qui peut être utilisé dans un script.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `umask` :

1. **Afficher la valeur actuelle de umask :**
   ```bash
   umask
   ```

2. **Définir umask à 022 (permissions par défaut pour les fichiers : rw-r--r--) :**
   ```bash
   umask 022
   ```

3. **Définir umask à 077 (permissions par défaut pour les fichiers : rw-------) :**
   ```bash
   umask 077
   ```

4. **Afficher umask en format symbolique :**
   ```bash
   umask -S
   ```

## Tips
- Utilisez `umask` dans vos scripts pour garantir des permissions sécurisées lors de la création de fichiers.
- Vérifiez régulièrement la valeur de `umask` pour éviter des permissions trop larges sur des fichiers sensibles.
- N'oubliez pas que `umask` affecte uniquement les fichiers nouvellement créés, pas ceux qui existent déjà.