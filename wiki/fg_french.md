# [리눅스] Bash fg 사용법

## Overview
La commande `fg` (foreground) dans Bash est utilisée pour ramener un processus en arrière-plan au premier plan. Cela permet à l'utilisateur d'interagir directement avec le processus, de lui fournir des entrées et de voir ses sorties en temps réel. `fg` est particulièrement utile lorsque vous avez lancé un processus en arrière-plan et que vous souhaitez lui redonner le contrôle du terminal.

## Usage
La syntaxe de base de la commande `fg` est la suivante :

```bash
fg [job_spec]
```

- `job_spec` : Cela fait référence à un identifiant de tâche spécifique. Si vous ne spécifiez pas de `job_spec`, `fg` ramènera la dernière tâche en arrière-plan au premier plan.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `fg` :

1. **Ramener la dernière tâche en arrière-plan au premier plan** :
   Si vous avez lancé un processus en arrière-plan, par exemple un éditeur de texte, vous pouvez le ramener au premier plan en utilisant simplement :

   ```bash
   fg
   ```

2. **Ramener une tâche spécifique au premier plan** :
   Supposons que vous ayez plusieurs tâches en arrière-plan. Vous pouvez les lister avec la commande `jobs` :

   ```bash
   jobs
   ```

   Cela pourrait afficher quelque chose comme :

   ```
   [1]+  12345 Stopped                 vim
   [2]-  12346 Running                 sleep 100 &
   ```

   Pour ramener la tâche `vim` (job 1) au premier plan, vous pouvez utiliser :

   ```bash
   fg %1
   ```

## Tips
- Utilisez la commande `jobs` pour voir toutes les tâches en arrière-plan avant d'utiliser `fg`. Cela vous aidera à identifier quelle tâche vous souhaitez ramener au premier plan.
- Si vous souhaitez suspendre une tâche en cours d'exécution au premier plan, vous pouvez utiliser `Ctrl + Z` pour la mettre en arrière-plan, puis utiliser `fg` pour la ramener au premier plan plus tard.
- N'oubliez pas que lorsque vous ramenez une tâche au premier plan, elle prendra le contrôle du terminal, ce qui signifie que vous ne pourrez pas exécuter d'autres commandes tant que cette tâche est en cours d'exécution.