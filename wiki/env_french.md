# [Linux] Bash env Utilisation : Gérer les variables d'environnement

## Overview
La commande `env` est utilisée pour afficher ou modifier les variables d'environnement dans un shell. Elle permet également d'exécuter une commande dans un environnement modifié, ce qui est utile pour tester des configurations sans affecter l'environnement global.

## Usage
La syntaxe de base de la commande `env` est la suivante :

```bash
env [options] [arguments]
```

## Common Options
- `-i` : Exécute la commande dans un environnement vide, sans aucune variable d'environnement.
- `-u VAR` : Supprime la variable d'environnement `VAR` avant d'exécuter la commande.
- `VAR=value` : Définit une variable d'environnement `VAR` avec la valeur `value` pour la commande à exécuter.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `env` :

1. **Afficher toutes les variables d'environnement :**
   ```bash
   env
   ```

2. **Exécuter une commande avec une variable d'environnement temporaire :**
   ```bash
   env MY_VAR=Hello world
   ```

3. **Supprimer une variable d'environnement avant d'exécuter une commande :**
   ```bash
   env -u MY_VAR echo "MY_VAR is unset"
   ```

4. **Exécuter une commande dans un environnement vide :**
   ```bash
   env -i bash
   ```

## Tips
- Utilisez `env` pour tester des commandes avec des variables d'environnement spécifiques sans modifier votre session actuelle.
- Combinez `env` avec d'autres commandes pour créer des scripts flexibles qui s'adaptent à différents environnements.
- Vérifiez toujours les variables d'environnement avant d'exécuter des commandes critiques pour éviter des comportements inattendus.