# [리눅스] Bash builtin 사용법

## Overview
La commande `builtin` dans Bash est utilisée pour exécuter des commandes intégrées (builtins) qui sont disponibles dans le shell, plutôt que d'exécuter des commandes externes. Cela permet d'accéder à des fonctionnalités spécifiques du shell qui ne sont pas disponibles en tant que programmes séparés. Par exemple, des commandes comme `echo`, `cd`, et `exit` sont des builtins. L'utilisation de `builtin` peut également aider à éviter les conflits avec des commandes externes ayant le même nom.

## Usage
La syntaxe de base de la commande `builtin` est la suivante :

```bash
builtin [commande] [options]
```

### Options courantes
- `-p` : Affiche le chemin complet de la commande builtin.
- `-f` : Force l'exécution de la commande builtin, même si une fonction du même nom existe.

## Examples

### Exemple 1 : Utilisation de `builtin` pour exécuter `echo`
Dans cet exemple, nous allons utiliser `builtin` pour s'assurer que nous exécutons la commande `echo` intégrée et non une fonction ou un script externe qui pourrait avoir le même nom.

```bash
# Définir une fonction echo
echo() {
    echo "Ceci est une fonction personnalisée."
}

# Utiliser builtin pour exécuter la commande echo intégrée
builtin echo "Ceci est la commande intégrée echo."
```

### Exemple 2 : Utilisation de `builtin` avec `cd`
Dans cet exemple, nous allons utiliser `builtin` pour changer de répertoire, en nous assurant que nous utilisons la commande intégrée `cd`.

```bash
# Changer de répertoire en utilisant la commande builtin
builtin cd /home/user
# Vérifier le répertoire courant
pwd
```

## Tips
- Utilisez `builtin` lorsque vous avez besoin de vous assurer que vous exécutez la version intégrée d'une commande, surtout si vous avez défini des fonctions avec le même nom.
- Soyez conscient que toutes les commandes ne sont pas des builtins. Pour vérifier si une commande est un builtin, vous pouvez utiliser la commande `type` suivie du nom de la commande.
- Gardez à l'esprit que l'utilisation de `builtin` peut améliorer les performances dans certains cas, car les builtins sont généralement plus rapides que les commandes externes.