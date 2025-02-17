# [Linux] Bash dirs usage : Afficher les répertoires de la pile

## Overview
La commande `dirs` est utilisée pour afficher la liste des répertoires dans la pile de répertoires de l'environnement de shell. Cela permet aux utilisateurs de visualiser facilement les répertoires qu'ils ont visités récemment et de naviguer rapidement entre eux.

## Usage
La syntaxe de base de la commande `dirs` est la suivante :

```bash
dirs [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `dirs` :

- `-l` : Affiche les répertoires en utilisant des chemins longs.
- `-p` : Affiche les répertoires dans un format de liste, un par ligne.
- `-c` : Efface la pile de répertoires.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `dirs` :

1. **Afficher la pile de répertoires actuelle :**

   ```bash
   dirs
   ```

2. **Afficher la pile de répertoires avec des chemins longs :**

   ```bash
   dirs -l
   ```

3. **Afficher la pile de répertoires un par ligne :**

   ```bash
   dirs -p
   ```

4. **Effacer la pile de répertoires :**

   ```bash
   dirs -c
   ```

## Tips
- Utilisez `pushd` et `popd` en conjonction avec `dirs` pour gérer efficacement votre pile de répertoires.
- Vérifiez régulièrement votre pile de répertoires pour éviter de vous perdre dans une navigation complexe.
- Combinez `dirs` avec d'autres commandes comme `cd` pour une navigation plus fluide dans votre terminal.