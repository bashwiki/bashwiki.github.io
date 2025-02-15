# [리눅스] Bash command 사용법

## Overview
La commande `command` est utilisée dans les scripts Bash pour exécuter une commande sans que les fonctions ou les alias définis par l'utilisateur n'interfèrent. Son principal objectif est de permettre aux utilisateurs d'exécuter une commande spécifique, même si une fonction ou un alias du même nom existe dans l'environnement. Cela est particulièrement utile pour garantir que le comportement attendu d'une commande est respecté.

## Usage
La syntaxe de base de la commande `command` est la suivante :

```bash
command [options] [arguments]
```

### Options courantes
- `-v` : Affiche la version de la commande.
- `-p` : Utilise le chemin par défaut pour rechercher la commande, ignorant les alias et les fonctions.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `command`.

### Exemple 1 : Exécuter une commande sans alias
Supposons que vous ayez défini un alias pour la commande `ls`. Pour exécuter la commande `ls` sans que l'alias n'interfère, vous pouvez utiliser :

```bash
command ls
```

### Exemple 2 : Utiliser le chemin par défaut
Si vous souhaitez exécuter la commande `echo` en utilisant le chemin par défaut, vous pouvez faire :

```bash
command -p echo "Hello, World!"
```

Cela garantit que vous utilisez la version de `echo` qui se trouve dans le chemin par défaut, sans tenir compte d'éventuels alias.

## Tips
- Utilisez `command` lorsque vous êtes confronté à des conflits entre des commandes, des alias ou des fonctions pour vous assurer que vous exécutez la version correcte de la commande.
- Il est souvent utile de combiner `command` avec d'autres commandes pour éviter les comportements inattendus dans des scripts complexes.
- Familiarisez-vous avec les alias et les fonctions que vous avez définis pour mieux comprendre quand utiliser `command`.