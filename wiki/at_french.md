# [리눅스] Bash at 사용법

## Overview
La commande `at` est un utilitaire de planification de tâches dans les systèmes Unix et Linux. Elle permet aux utilisateurs de programmer l'exécution de commandes ou de scripts à un moment précis dans le futur. Contrairement à `cron`, qui exécute des tâches à intervalles réguliers, `at` est utilisé pour des tâches uniques, ce qui le rend idéal pour des opérations ponctuelles.

## Usage
La syntaxe de base de la commande `at` est la suivante :

```bash
at [options] TIME
```

### Options courantes :
- `-f FILE` : Spécifie un fichier contenant les commandes à exécuter.
- `-m` : Envoie un e-mail à l'utilisateur après l'exécution de la tâche, même si aucune sortie n'est produite.
- `-q QUEUE` : Permet de spécifier une file d'attente pour la tâche.
- `-v` : Affiche la date et l'heure auxquelles la tâche sera exécutée.

Le paramètre `TIME` peut être spécifié de plusieurs manières, par exemple :
- `now + 1 hour`
- `tomorrow`
- `5:00 PM`

## Examples
### Exemple 1 : Exécution d'une commande simple
Pour exécuter une commande simple, comme afficher "Hello World" dans le terminal dans 5 minutes, vous pouvez utiliser :

```bash
echo "echo 'Hello World'" | at now + 5 minutes
```

### Exemple 2 : Exécution d'un script
Si vous avez un script nommé `backup.sh` que vous souhaitez exécuter demain à 2 heures du matin, vous pouvez le faire avec :

```bash
at 2:00 AM tomorrow -f backup.sh
```

## Tips
- Assurez-vous que le service `atd` est en cours d'exécution sur votre système, car `at` dépend de ce démon pour exécuter les tâches programmées.
- Utilisez `atq` pour lister les tâches programmées et `atrm` pour supprimer une tâche spécifique.
- Pour des tâches qui nécessitent des privilèges élevés, assurez-vous d'exécuter `at` avec les permissions appropriées ou en tant que superutilisateur si nécessaire.
- Pensez à tester vos commandes dans un environnement sûr avant de les programmer pour éviter des erreurs inattendues.