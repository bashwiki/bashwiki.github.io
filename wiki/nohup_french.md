# [리눅스] Bash nohup 사용법

## Overview
Le commandement `nohup` (no hang up) est utilisé dans les systèmes Unix et Linux pour exécuter des commandes ou des scripts de manière à ce qu'ils continuent à s'exécuter même si la session de terminal est fermée. Cela est particulièrement utile pour les tâches de longue durée ou les processus qui doivent s'exécuter en arrière-plan sans interruption.

## Usage
La syntaxe de base de la commande `nohup` est la suivante :

```bash
nohup commande [arguments] &
```

### Options courantes :
- `&` : Place la commande en arrière-plan, permettant à l'utilisateur de continuer à utiliser le terminal.
- `nohup.out` : Par défaut, la sortie standard et la sortie d'erreur de la commande sont redirigées vers un fichier nommé `nohup.out` dans le répertoire courant, sauf si une autre redirection est spécifiée.

## Examples
### Exemple 1 : Exécution d'un script en arrière-plan
Supposons que vous ayez un script nommé `long_task.sh` que vous souhaitez exécuter en arrière-plan :

```bash
nohup ./long_task.sh &
```

Cela exécutera `long_task.sh` et continuera à s'exécuter même si vous fermez le terminal.

### Exemple 2 : Redirection de la sortie vers un fichier spécifique
Si vous souhaitez rediriger la sortie vers un fichier spécifique, vous pouvez le faire comme suit :

```bash
nohup ./long_task.sh > output.log 2>&1 &
```

Dans cet exemple, la sortie standard et la sortie d'erreur seront redirigées vers `output.log`.

## Tips
- **Vérifiez le fichier nohup.out** : Si vous ne spécifiez pas de redirection pour la sortie, vérifiez le fichier `nohup.out` pour voir les messages générés par votre commande.
- **Utilisez `jobs` et `bg`** : Si vous avez lancé une commande sans `nohup` et que vous souhaitez la mettre en arrière-plan, vous pouvez utiliser `Ctrl+Z` pour suspendre la tâche, puis `bg` pour la reprendre en arrière-plan.
- **Surveillez les processus** : Utilisez la commande `ps` ou `top` pour surveiller les processus en cours d'exécution et vous assurer que votre commande fonctionne comme prévu.

En utilisant `nohup`, vous pouvez facilement gérer des tâches de longue durée sans vous soucier de la fermeture de votre terminal.