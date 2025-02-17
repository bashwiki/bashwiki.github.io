# [Linux] Bash pwd utilisation : Afficher le répertoire de travail actuel

## Overview
La commande `pwd` (print working directory) est utilisée dans les systèmes Unix et Linux pour afficher le chemin absolu du répertoire de travail actuel dans lequel l'utilisateur se trouve. C'est un outil essentiel pour naviguer dans le système de fichiers.

## Usage
La syntaxe de base de la commande `pwd` est la suivante :

```bash
pwd [options]
```

## Common Options
Voici quelques options courantes pour la commande `pwd` :

- `-L` : Affiche le chemin logique du répertoire de travail actuel.
- `-P` : Affiche le chemin physique, en résolvant les liens symboliques.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `pwd` :

1. Afficher le répertoire de travail actuel :
   ```bash
   pwd
   ```

2. Afficher le chemin logique du répertoire de travail :
   ```bash
   pwd -L
   ```

3. Afficher le chemin physique du répertoire de travail :
   ```bash
   pwd -P
   ```

## Tips
- Utilisez `pwd` régulièrement pour vous assurer que vous êtes dans le bon répertoire avant d'exécuter d'autres commandes.
- Combinez `pwd` avec d'autres commandes comme `cd` pour naviguer efficacement dans le système de fichiers.
- N'oubliez pas que `pwd` est sensible aux permissions ; si vous n'avez pas accès à un répertoire, vous ne pourrez pas voir son chemin.