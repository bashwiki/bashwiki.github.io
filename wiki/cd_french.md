# [Linux] Bash cd Utilisation : Changer de répertoire

## Overview
La commande `cd` (change directory) est utilisée pour naviguer entre les répertoires dans un système de fichiers. Elle permet à l'utilisateur de se déplacer vers un répertoire spécifique afin d'exécuter des commandes ou d'accéder à des fichiers.

## Usage
La syntaxe de base de la commande `cd` est la suivante :

```bash
cd [options] [arguments]
```

## Common Options
- `-`: Retourne au dernier répertoire visité.
- `..`: Permet de remonter d'un niveau dans l'arborescence des répertoires.
- `~`: Représente le répertoire personnel de l'utilisateur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cd` :

1. **Accéder à un répertoire spécifique :**
   ```bash
   cd /chemin/vers/le/répertoire
   ```

2. **Revenir au répertoire parent :**
   ```bash
   cd ..
   ```

3. **Accéder au répertoire personnel :**
   ```bash
   cd ~
   ```

4. **Retourner au dernier répertoire visité :**
   ```bash
   cd -
   ```

5. **Accéder à un répertoire relatif :**
   ```bash
   cd dossier/sous-dossier
   ```

## Tips
- Utilisez `cd -` pour naviguer rapidement entre deux répertoires.
- Vous pouvez utiliser la touche `Tab` pour l'auto-complétion des noms de répertoires.
- Pour afficher le répertoire courant, utilisez la commande `pwd` après avoir changé de répertoire.