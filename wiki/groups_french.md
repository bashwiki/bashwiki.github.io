# [Linux] Bash groups : afficher les groupes d'utilisateurs

## Overview
La commande `groups` est utilisée pour afficher les groupes auxquels un utilisateur appartient. Cela peut être utile pour comprendre les permissions d'accès et les rôles d'un utilisateur dans le système.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
groups [options] [arguments]
```

## Common Options
- `-h`, `--help` : Affiche l'aide et les options disponibles pour la commande.
- `-n`, `--no-group` : N'affiche pas le nom du groupe principal de l'utilisateur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `groups` :

1. **Afficher les groupes de l'utilisateur courant :**

   ```bash
   groups
   ```

2. **Afficher les groupes d'un utilisateur spécifique :**

   ```bash
   groups nom_utilisateur
   ```

3. **Afficher les groupes sans le groupe principal :**

   ```bash
   groups -n nom_utilisateur
   ```

## Tips
- Utilisez `groups` sans arguments pour rapidement vérifier vos propres groupes.
- Combinez `groups` avec d'autres commandes, comme `grep`, pour filtrer les résultats si vous recherchez un groupe spécifique.
- Pensez à vérifier les permissions des fichiers et des répertoires en fonction des groupes auxquels vous appartenez pour mieux gérer l'accès.