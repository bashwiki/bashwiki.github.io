# [Linux] Bash à at : Planifier des tâches à exécuter à une heure précise

## Overview
La commande `at` permet de planifier l'exécution de commandes ou de scripts à un moment précis dans le futur. C'est un outil pratique pour automatiser des tâches sans avoir à rester connecté à la machine.

## Usage
La syntaxe de base de la commande `at` est la suivante :

```bash
at [options] [time]
```

## Common Options
- `-f` : Spécifie un fichier contenant les commandes à exécuter.
- `-m` : Envoie un e-mail à l'utilisateur lorsque la tâche est terminée.
- `-q` : Définit la file d'attente à utiliser pour la tâche.
- `-l` : Liste les tâches planifiées pour l'utilisateur.
- `-d` : Supprime une tâche planifiée.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `at` :

1. **Planifier une commande pour s'exécuter dans 5 minutes :**
   ```bash
   echo "echo 'Bonjour, le monde!'" | at now + 5 minutes
   ```

2. **Planifier une tâche pour demain à 14h :**
   ```bash
   echo "backup.sh" | at 14:00 tomorrow
   ```

3. **Utiliser un fichier pour exécuter plusieurs commandes :**
   ```bash
   at -f /chemin/vers/mon_script.sh 09:00
   ```

4. **Lister les tâches planifiées :**
   ```bash
   at -l
   ```

5. **Supprimer une tâche planifiée :**
   ```bash
   at -d 1
   ```

## Tips
- Assurez-vous que le service `atd` est en cours d'exécution sur votre système pour que les tâches planifiées soient exécutées.
- Utilisez `at -m` pour recevoir une notification par e-mail lorsque votre tâche est terminée.
- Vérifiez régulièrement vos tâches planifiées avec `at -l` pour éviter d'avoir des tâches en attente indéfiniment.