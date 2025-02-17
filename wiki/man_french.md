# [Linux] Bash man Utilisation : Afficher la documentation des commandes

## Overview
La commande `man` est utilisée pour afficher les pages de manuel des commandes et des programmes dans un système Unix/Linux. Elle fournit des informations détaillées sur l'utilisation, les options et les fonctionnalités des commandes.

## Usage
La syntaxe de base de la commande `man` est la suivante :

```bash
man [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `man` :

- `-k` : Recherche dans les pages de manuel les mots-clés spécifiés.
- `-f` : Affiche une courte description des pages de manuel correspondant aux arguments.
- `-a` : Affiche toutes les pages de manuel correspondant à la commande demandée, une par une.
- `-w` : Affiche le chemin du fichier de la page de manuel sans l'ouvrir.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `man` :

- Pour afficher la page de manuel de la commande `ls` :

```bash
man ls
```

- Pour rechercher des pages de manuel contenant le mot "copy" :

```bash
man -k copy
```

- Pour afficher la page de manuel de `grep` et toutes ses sections :

```bash
man -a grep
```

- Pour obtenir le chemin du fichier de la page de manuel de `mkdir` :

```bash
man -w mkdir
```

## Tips
- Utilisez la touche `q` pour quitter la page de manuel.
- Vous pouvez naviguer dans la page avec les flèches directionnelles ou les touches `Page Up` et `Page Down`.
- Pour rechercher un terme dans la page de manuel, appuyez sur `/` suivi du terme recherché, puis appuyez sur `Entrée`.