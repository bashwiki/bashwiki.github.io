# [Linux] Bash history Utilisation : Afficher l'historique des commandes

## Overview
La commande `history` dans Bash permet d'afficher la liste des commandes précédemment exécutées dans le terminal. Cela peut être très utile pour retrouver rapidement une commande que vous avez utilisée sans avoir à la retaper entièrement.

## Usage
La syntaxe de base de la commande `history` est la suivante :

```bash
history [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `history` :

- `-c` : Efface l'historique des commandes.
- `-d offset` : Supprime la commande à la position spécifiée par `offset`.
- `n` : Affiche les `n` dernières commandes de l'historique.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `history` :

### Afficher l'historique complet
```bash
history
```

### Afficher les 10 dernières commandes
```bash
history 10
```

### Effacer l'historique des commandes
```bash
history -c
```

### Supprimer une commande spécifique de l'historique
```bash
history -d 5
```
*(Cela supprimera la cinquième commande de l'historique.)*

## Tips
- Utilisez `!n` pour réexécuter la commande à la position `n` dans l'historique.
- Combinez `history` avec `grep` pour rechercher des commandes spécifiques. Par exemple :
  ```bash
  history | grep "git"
  ```
- Pensez à sauvegarder votre historique en utilisant `history -w` pour écrire l'historique actuel dans un fichier.