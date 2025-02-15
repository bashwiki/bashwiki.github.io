# [리눅스] Bash bash 사용법

## Overview
La commande `bash` est l'interpréteur de commandes Bourne Again SHell, qui est une version améliorée de l'interpréteur de commandes original Bourne Shell (`sh`). Son principal objectif est de fournir un environnement de ligne de commande pour exécuter des scripts et des commandes interactives. `bash` est largement utilisé dans les systèmes Unix et Linux, et il est connu pour sa compatibilité avec les scripts shell, sa gestion des variables, et ses fonctionnalités avancées comme l'édition de commandes et l'historique.

## Usage
La syntaxe de base de la commande `bash` est la suivante :

```bash
bash [options] [file]
```

### Options courantes :
- `-c`: Exécute les commandes spécifiées dans une chaîne de caractères.
- `-i`: Lance `bash` en mode interactif, même si l'entrée n'est pas un terminal.
- `-l`: Démarre `bash` comme un shell de connexion, ce qui signifie qu'il lira les fichiers de configuration de l'utilisateur.
- `-s`: Lit les commandes depuis l'entrée standard.

## Examples
### Exemple 1 : Exécution d'un script
Pour exécuter un script shell nommé `script.sh`, vous pouvez utiliser la commande suivante :

```bash
bash script.sh
```

### Exemple 2 : Exécution de commandes en ligne
Pour exécuter une série de commandes directement depuis la ligne de commande, vous pouvez utiliser l'option `-c` :

```bash
bash -c 'echo "Hello, World!" && ls -l'
```

Cet exemple affichera "Hello, World!" suivi d'une liste détaillée des fichiers dans le répertoire courant.

## Tips
- Utilisez `bash` pour exécuter des scripts shell afin de profiter de ses fonctionnalités avancées, comme la gestion des erreurs et le débogage.
- Familiarisez-vous avec les raccourcis clavier de `bash`, comme `Ctrl + R` pour rechercher dans l'historique des commandes, afin d'améliorer votre efficacité.
- Lorsque vous écrivez des scripts, commencez toujours par la ligne shebang `#!/bin/bash` pour indiquer que le script doit être exécuté avec `bash`.