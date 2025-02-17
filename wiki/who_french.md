# [Linux] Bash who utilisation : afficher les utilisateurs connectés

## Overview
La commande `who` est utilisée pour afficher la liste des utilisateurs actuellement connectés au système. Elle fournit des informations sur les sessions des utilisateurs, y compris leur nom d'utilisateur, le terminal utilisé, la date et l'heure de connexion.

## Usage
La syntaxe de base de la commande `who` est la suivante :

```bash
who [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `who` :

- `-a` : Affiche toutes les informations disponibles, y compris les utilisateurs connectés et les utilisateurs qui ont été déconnectés.
- `-b` : Affiche la dernière fois que le système a été redémarré.
- `-q` : Affiche uniquement les noms d'utilisateur et le nombre total d'utilisateurs connectés.
- `--help` : Affiche l'aide sur la commande `who`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `who` :

1. Afficher la liste des utilisateurs connectés :
   ```bash
   who
   ```

2. Afficher toutes les informations, y compris les utilisateurs déconnectés :
   ```bash
   who -a
   ```

3. Afficher la dernière fois que le système a été redémarré :
   ```bash
   who -b
   ```

4. Afficher uniquement les noms d'utilisateur et le nombre total d'utilisateurs connectés :
   ```bash
   who -q
   ```

## Tips
- Utilisez `who -b` pour vérifier rapidement si le système a été redémarré récemment, ce qui peut être utile pour le dépannage.
- Combinez `who` avec d'autres commandes comme `grep` pour filtrer les résultats selon des critères spécifiques, par exemple :
  ```bash
  who | grep 'username'
  ```
- Pensez à utiliser `w` si vous souhaitez obtenir des informations supplémentaires sur les utilisateurs connectés, telles que l'activité en cours.