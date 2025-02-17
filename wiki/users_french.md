# [Linux] Utilisateurs Bash : Afficher les informations sur les utilisateurs

## Overview
La commande `users` affiche les noms des utilisateurs actuellement connectés au système. C'est un outil simple mais efficace pour obtenir rapidement une vue d'ensemble des sessions utilisateur actives.

## Usage
La syntaxe de base de la commande `users` est la suivante :

```bash
users [options] [arguments]
```

## Common Options
- `-n` : Affiche le nombre d'utilisateurs connectés.
- `-r` : Affiche uniquement les utilisateurs réels (pas les utilisateurs de service).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `users` :

1. **Afficher les utilisateurs connectés :**
   ```bash
   users
   ```

2. **Afficher le nombre d'utilisateurs connectés :**
   ```bash
   users -n
   ```

3. **Afficher uniquement les utilisateurs réels :**
   ```bash
   users -r
   ```

## Tips
- Utilisez la commande `who` pour obtenir plus de détails sur les utilisateurs connectés, comme leur terminal et l'heure de connexion.
- Combinez `users` avec d'autres commandes comme `wc -l` pour compter le nombre d'utilisateurs connectés :
  ```bash
  users | wc -w
  ```