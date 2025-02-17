# [Linux] Bash set : Modifier les options de shell

## Overview
La commande `set` dans Bash est utilisée pour modifier les options du shell et définir des variables d'environnement. Elle permet de contrôler le comportement du shell et d'ajuster son fonctionnement selon les besoins de l'utilisateur.

## Usage
La syntaxe de base de la commande `set` est la suivante :

```bash
set [options] [arguments]
```

## Common Options
Voici quelques options courantes de la commande `set` :

- `-e` : Arrête l'exécution si une commande échoue.
- `-u` : Traite les variables non définies comme une erreur.
- `-x` : Affiche les commandes et leurs arguments lors de leur exécution.
- `-o` : Active ou désactive des options spécifiques du shell.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `set` :

1. Activer l'arrêt sur erreur :
   ```bash
   set -e
   ```

2. Afficher les commandes exécutées :
   ```bash
   set -x
   ```

3. Traiter les variables non définies comme une erreur :
   ```bash
   set -u
   ```

4. Désactiver l'affichage des commandes :
   ```bash
   set +x
   ```

## Tips
- Utilisez `set -e` pour éviter que des erreurs passent inaperçues dans vos scripts.
- Combinez `set -u` avec `set -e` pour une gestion stricte des erreurs et des variables.
- Pensez à utiliser `set +` pour désactiver une option si vous n'en avez plus besoin dans votre script.