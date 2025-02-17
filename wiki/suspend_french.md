# [Linux] Bash suspend utilisation : Suspendre un processus en cours

## Overview
La commande `suspend` est utilisée dans un environnement de terminal pour suspendre un processus en cours d'exécution. Cela permet de mettre temporairement en pause un processus afin de le reprendre ultérieurement.

## Usage
La syntaxe de base de la commande `suspend` est la suivante :

```bash
suspend [options] [arguments]
```

## Common Options
La commande `suspend` ne dispose pas de nombreuses options, car son utilisation principale est assez simple. Cependant, voici quelques points à considérer :

- `-h`, `--help` : Affiche l'aide et les options disponibles pour la commande.
- `-v`, `--version` : Affiche la version de la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `suspend` :

### Exemple 1 : Suspendre un processus
Pour suspendre un processus en cours d'exécution dans un terminal, vous pouvez simplement utiliser la combinaison de touches suivante :

```bash
Ctrl + Z
```

### Exemple 2 : Reprendre un processus suspendu
Pour reprendre un processus que vous avez suspendu, utilisez la commande `fg` :

```bash
fg
```

### Exemple 3 : Lister les processus suspendus
Pour voir les processus suspendus, utilisez la commande `jobs` :

```bash
jobs
```

## Tips
- Utilisez `Ctrl + Z` pour suspendre rapidement un processus sans avoir besoin de taper une commande.
- Pour reprendre un processus spécifique, utilisez `fg %n`, où `n` est le numéro du job affiché par la commande `jobs`.
- Si vous souhaitez exécuter un processus en arrière-plan après l'avoir suspendu, utilisez `bg` pour le relancer en arrière-plan.