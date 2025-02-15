# [리눅스] Bash exec 사용법

## Overview
La commande `exec` dans Bash est utilisée pour exécuter une commande dans le contexte du shell actuel, remplaçant ainsi le processus du shell par le processus de la commande exécutée. Cela signifie que lorsque vous utilisez `exec`, le shell ne revient pas à l'invite de commande après l'exécution de la commande. Cette fonctionnalité est particulièrement utile pour les scripts où vous souhaitez remplacer le shell par un autre programme sans créer un nouveau processus.

## Usage
La syntaxe de base de la commande `exec` est la suivante :

```bash
exec [options] command [arguments]
```

### Options courantes :
- `-a name` : Permet de spécifier un nom différent pour le programme exécuté.
- `-l` : Lance le programme comme un shell de connexion.
- `-p` : Ignore les variables d'environnement du shell actuel.

## Examples
### Exemple 1 : Remplacer le shell par un autre programme
Si vous souhaitez remplacer le shell actuel par un éditeur de texte comme `nano`, vous pouvez utiliser la commande suivante :

```bash
exec nano
```

Dans cet exemple, le shell sera remplacé par `nano`, et une fois que vous aurez terminé d'éditer, vous ne retournerez pas à l'invite de commande.

### Exemple 2 : Exécuter un script avec exec
Vous pouvez également utiliser `exec` pour exécuter un script shell :

```bash
exec ./mon_script.sh
```

Cela remplacera le shell actuel par l'exécution de `mon_script.sh`. Si le script se termine, il n'y aura pas de retour à l'invite de commande.

## Tips
- Utilisez `exec` avec précaution, car une fois que vous avez remplacé le shell, vous ne pourrez pas revenir à l'invite de commande à moins de quitter le programme exécuté.
- `exec` peut être utile pour optimiser l'utilisation de la mémoire, car il évite de créer un nouveau processus pour le programme exécuté.
- Pensez à utiliser `exec` dans des scripts où vous n'avez pas besoin de revenir à l'invite de commande après l'exécution d'une tâche.