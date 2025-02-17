# [Linux] Bash fc Utilisation : Gérer l'historique des commandes

## Overview
La commande `fc` (fix command) est utilisée pour afficher, modifier et réexécuter des commandes précédemment exécutées dans le shell Bash. Elle permet aux utilisateurs de gérer facilement leur historique de commandes.

## Usage
La syntaxe de base de la commande `fc` est la suivante :

```bash
fc [options] [arguments]
```

## Common Options
- `-l` : Liste les commandes de l'historique.
- `-r` : Inverse l'ordre des commandes lors de l'affichage.
- `-s` : Exécute la commande spécifiée sans l'afficher.
- `-n` : Ne pas afficher les numéros de ligne lors de la liste des commandes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `fc` :

### Afficher les dernières commandes
Pour afficher les 10 dernières commandes de l'historique, vous pouvez utiliser :

```bash
fc -l -n -10
```

### Modifier une commande spécifique
Si vous souhaitez modifier la commande numéro 25 dans votre historique, exécutez :

```bash
fc 25
```

### Exécuter une commande directement
Pour exécuter la dernière commande sans l'afficher, utilisez :

```bash
fc -s
```

### Inverser l'affichage des commandes
Pour afficher les 5 dernières commandes dans l'ordre inverse, utilisez :

```bash
fc -r -l -5
```

## Tips
- Utilisez `fc` pour corriger rapidement des erreurs dans les commandes précédentes sans avoir à les retaper entièrement.
- Familiarisez-vous avec les numéros de ligne de l'historique pour naviguer plus efficacement dans vos commandes.
- Pensez à utiliser `fc -s` pour exécuter rapidement des commandes que vous avez récemment utilisées sans les modifier.