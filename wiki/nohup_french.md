# [Linux] Bash nohup utilisation : Exécuter des commandes sans interruption

## Overview
La commande `nohup` (no hang up) permet d'exécuter des commandes en arrière-plan, même si la session terminal est fermée. Cela signifie que les processus lancés avec `nohup` continueront à s'exécuter indépendamment des déconnexions ou des fermetures de terminal.

## Usage
La syntaxe de base de la commande `nohup` est la suivante :

```bash
nohup [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `nohup` :

- `&` : Permet d'exécuter la commande en arrière-plan.
- `-h` : Affiche l'aide sur l'utilisation de la commande.
- `-p` : Permet de spécifier un PID (identifiant de processus) pour le processus en cours.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `nohup` :

1. Exécuter un script en arrière-plan :
   ```bash
   nohup ./mon_script.sh &
   ```

2. Exécuter une commande longue et rediriger la sortie vers un fichier :
   ```bash
   nohup long_running_command > output.log &
   ```

3. Exécuter une commande et ignorer les signaux de déconnexion :
   ```bash
   nohup my_command &
   ```

4. Exécuter une commande avec des arguments :
   ```bash
   nohup my_command arg1 arg2 > output.log 2>&1 &
   ```

## Tips
- Toujours rediriger la sortie vers un fichier pour éviter que les messages ne soient perdus.
- Utiliser `jobs` pour vérifier les processus en arrière-plan.
- Pour arrêter un processus, utilisez `kill` avec le PID approprié.