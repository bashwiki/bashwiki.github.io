# [Linux] Bash jobs Utilisation : Gérer les tâches en arrière-plan

## Overview
La commande `jobs` est utilisée dans Bash pour afficher la liste des tâches en arrière-plan et des tâches suspendues dans le shell actuel. Elle permet aux utilisateurs de suivre l'état des processus qu'ils ont lancés.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
jobs [options] [arguments]
```

## Common Options
- `-l` : Affiche les numéros de processus (PID) en plus des informations sur les tâches.
- `-n` : Affiche uniquement les tâches qui ont changé d'état depuis la dernière exécution de la commande.
- `-p` : Affiche uniquement les numéros de processus des tâches.

## Common Examples

1. **Afficher toutes les tâches en arrière-plan :**
   ```bash
   jobs
   ```

2. **Afficher les tâches avec les numéros de processus :**
   ```bash
   jobs -l
   ```

3. **Afficher uniquement les tâches qui ont changé d'état :**
   ```bash
   jobs -n
   ```

4. **Afficher uniquement les numéros de processus :**
   ```bash
   jobs -p
   ```

## Tips
- Utilisez `bg` pour reprendre une tâche suspendue en arrière-plan après l'avoir arrêtée avec `Ctrl+Z`.
- Utilisez `fg` pour ramener une tâche en arrière-plan au premier plan.
- Vérifiez régulièrement l'état de vos tâches en utilisant `jobs` pour éviter d'avoir des processus orphelins.