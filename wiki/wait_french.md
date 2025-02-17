# [Linux] Bash wait : Attendre la fin d'un processus

## Overview
La commande `wait` en Bash est utilisée pour attendre la fin d'un ou plusieurs processus en arrière-plan. Elle permet de synchroniser l'exécution des scripts en s'assurant que certaines tâches sont terminées avant de continuer.

## Usage
La syntaxe de base de la commande `wait` est la suivante :

```bash
wait [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `wait` :

- `-n` : Attend la fin du premier processus en arrière-plan.
- `PID` : Attend la fin du processus spécifié par son identifiant de processus (PID).

## Common Examples

### Attendre tous les processus en arrière-plan
Pour attendre que tous les processus en arrière-plan se terminent, utilisez simplement :

```bash
sleep 5 &  # Démarre un processus en arrière-plan
sleep 3 &  # Démarre un autre processus en arrière-plan
wait        # Attend que tous les processus en arrière-plan se terminent
echo "Tous les processus sont terminés."
```

### Attendre un processus spécifique
Pour attendre un processus spécifique, vous devez connaître son PID :

```bash
sleep 10 &  # Démarre un processus en arrière-plan
PID=$!      # Récupère le PID du dernier processus en arrière-plan
wait $PID   # Attend que le processus avec ce PID se termine
echo "Le processus avec PID $PID est terminé."
```

### Attendre le premier processus terminé
Pour attendre le premier processus qui se termine :

```bash
sleep 5 &  # Démarre un processus en arrière-plan
sleep 3 &  # Démarre un autre processus en arrière-plan
wait -n     # Attend la fin du premier processus en arrière-plan
echo "Le premier processus est terminé."
```

## Tips
- Utilisez `wait` dans des scripts pour gérer l'ordre d'exécution des tâches.
- Vérifiez le code de sortie d'un processus après `wait` en utilisant `$?` pour savoir s'il s'est terminé avec succès.
- Évitez d'utiliser `wait` sans arguments si vous avez des processus spécifiques à surveiller, car cela attendra tous les processus en arrière-plan.