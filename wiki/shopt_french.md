# [Linux] Bash shopt : Gérer les options de shell

## Overview
La commande `shopt` dans Bash permet de modifier les options du shell. Elle est utilisée pour activer ou désactiver des fonctionnalités spécifiques qui peuvent influencer le comportement de l'interpréteur de commandes.

## Usage
La syntaxe de base de la commande `shopt` est la suivante :

```bash
shopt [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `shopt` :

- `-s` : Active une option.
- `-u` : Désactive une option.
- `-p` : Affiche les options actuellement définies.

## Common Examples

### Activer une option
Pour activer l'option `cdable_vars`, qui permet d'utiliser des variables dans les chemins de répertoire :

```bash
shopt -s cdable_vars
```

### Désactiver une option
Pour désactiver l'option `cdable_vars` :

```bash
shopt -u cdable_vars
```

### Afficher les options
Pour afficher toutes les options de shell actuellement définies :

```bash
shopt
```

### Vérifier une option spécifique
Pour vérifier si une option est activée ou désactivée, par exemple `nullglob` :

```bash
shopt nullglob
```

## Tips
- Utilisez `shopt` dans vos scripts pour garantir un comportement cohérent du shell.
- Consultez la documentation de Bash pour découvrir d'autres options disponibles avec `shopt`.
- Pensez à sauvegarder vos paramètres de shell dans votre fichier `.bashrc` pour les rendre persistants entre les sessions.