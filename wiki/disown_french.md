# [리눅스] Bash disown 사용법

## Overview
La commande `disown` dans Bash est utilisée pour détacher un ou plusieurs processus de la session de terminal en cours. Cela signifie que les processus ne seront plus associés à la session de terminal, ce qui permet de continuer leur exécution même si le terminal est fermé. Cette commande est particulièrement utile pour les utilisateurs qui lancent des tâches longues et souhaitent les laisser s'exécuter en arrière-plan sans avoir à garder le terminal ouvert.

## Usage
La syntaxe de base de la commande `disown` est la suivante :

```bash
disown [options] [jobspec]
```

### Options courantes :
- `-h` : Ne pas marquer le travail pour être tué lorsque le shell se termine.
- `-a` : Appliquer la commande à tous les travaux en arrière-plan.
- `-r` : Appliquer la commande uniquement aux travaux en cours d'exécution.

Si `jobspec` n'est pas spécifié, `disown` affecte le dernier travail en arrière-plan.

## Examples
### Exemple 1 : Détacher un travail spécifique
Supposons que vous ayez lancé un script en arrière-plan :

```bash
./long_script.sh &
```

Vous pouvez vérifier les travaux en cours avec la commande `jobs` :

```bash
jobs
```

Cela pourrait afficher quelque chose comme :

```
[1]+  12345 Running                 ./long_script.sh &
```

Pour détacher ce travail, utilisez :

```bash
disown %1
```

### Exemple 2 : Détacher tous les travaux en arrière-plan
Si vous avez plusieurs travaux en cours et que vous souhaitez tous les détacher, vous pouvez utiliser l'option `-a` :

```bash
disown -a
```

Cela détachera tous les travaux en arrière-plan de votre session de terminal.

## Tips
- Utilisez `jobs` pour lister tous les travaux en cours avant d'utiliser `disown`, afin de savoir quels travaux vous souhaitez détacher.
- Pensez à utiliser `disown` après avoir mis un travail en arrière-plan avec `&` ou après avoir suspendu un travail avec `Ctrl+Z` suivi de `bg`.
- Si vous détachez un travail, assurez-vous qu'il est bien configuré pour continuer à s'exécuter sans interaction avec le terminal, sinon il pourrait échouer si des entrées sont nécessaires.