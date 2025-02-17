# [Linux] Bash builtin : Exécute une commande shell interne

## Overview
La commande `builtin` en Bash permet d'exécuter des commandes internes du shell, c'est-à-dire des commandes qui sont intégrées dans le shell lui-même, plutôt que d'appeler des exécutables externes. Cela peut être utile pour éviter de masquer des commandes internes par des exécutables externes du même nom.

## Usage
La syntaxe de base de la commande `builtin` est la suivante :

```bash
builtin [options] [arguments]
```

## Common Options
- `-h`, `--help` : Affiche l'aide pour la commande builtin.
- `-m`, `--man` : Affiche la page de manuel pour la commande builtin.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `builtin` :

### Exemple 1 : Utiliser `builtin` avec `echo`
```bash
builtin echo "Ceci est un message interne."
```

### Exemple 2 : Vérifier la version de `cd`
```bash
builtin cd /tmp
```

### Exemple 3 : Utiliser `builtin` pour forcer l'exécution d'une commande interne
```bash
builtin type -a echo
```

## Tips
- Utilisez `builtin` lorsque vous souhaitez vous assurer que vous exécutez la version interne d'une commande, surtout si une version externe est présente dans votre `$PATH`.
- Vérifiez toujours la documentation de la commande pour connaître les options spécifiques disponibles.
- Soyez prudent lors de l'utilisation de `builtin` dans des scripts, car cela peut affecter le comportement attendu si des commandes externes sont également utilisées.