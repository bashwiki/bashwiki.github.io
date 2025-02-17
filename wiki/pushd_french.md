# [Linux] Bash pushd : Gérer les répertoires dans la pile

## Overview
La commande `pushd` permet de changer de répertoire tout en le sauvegardant dans une pile. Cela facilite la navigation entre plusieurs répertoires en permettant de revenir rapidement à un répertoire précédent.

## Usage
La syntaxe de base de la commande `pushd` est la suivante :

```bash
pushd [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `pushd` :

- `+n` : Accède à l'élément à l'index `n` de la pile.
- `-n` : Accède à l'élément à l'index `-n` de la pile.
- `-` : Permet de revenir au répertoire précédent.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `pushd` :

1. **Changer de répertoire et sauvegarder l'ancien :**
   ```bash
   pushd /chemin/vers/nouveau/repertoire
   ```

2. **Accéder à un répertoire spécifique dans la pile :**
   ```bash
   pushd +1
   ```

3. **Revenir au répertoire précédent :**
   ```bash
   pushd -
   ```

4. **Afficher la pile actuelle des répertoires :**
   ```bash
   dirs
   ```

## Tips
- Utilisez `popd` pour retirer le répertoire du sommet de la pile et revenir au répertoire précédent.
- Combinez `pushd` avec `popd` pour naviguer efficacement entre plusieurs répertoires sans perdre votre place.
- Pensez à utiliser `dirs -v` pour afficher la pile avec des numéros d'index, ce qui facilite la navigation.