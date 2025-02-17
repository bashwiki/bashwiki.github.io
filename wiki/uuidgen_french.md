# [Linux] Bash uuidgen Utilisation : Générer des identifiants uniques

## Overview
La commande `uuidgen` est utilisée pour générer des identifiants uniques universels (UUID). Ces identifiants sont souvent utilisés pour identifier de manière unique des objets dans des systèmes distribués, des bases de données, ou des fichiers.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
uuidgen [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `uuidgen` :

- `-r` : Génère un UUID aléatoire.
- `-t` : Génère un UUID basé sur le temps.
- `-h` : Affiche l'aide et les options disponibles.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `uuidgen` :

1. Générer un UUID simple :

   ```bash
   uuidgen
   ```

2. Générer un UUID aléatoire :

   ```bash
   uuidgen -r
   ```

3. Générer un UUID basé sur le temps :

   ```bash
   uuidgen -t
   ```

4. Générer plusieurs UUID à la fois :

   ```bash
   for i in {1..5}; do uuidgen; done
   ```

## Tips
- Utilisez `uuidgen` pour créer des identifiants uniques lors de la création de nouvelles entrées dans une base de données.
- Pensez à utiliser l'option `-r` pour des UUID qui ne doivent pas être prévisibles.
- Si vous avez besoin de plusieurs UUID, envisagez d'utiliser une boucle pour générer plusieurs identifiants en une seule commande.