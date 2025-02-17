# [Linux] Bash crontab Utilisation : Planification de tâches automatisées

## Overview
La commande `crontab` permet de planifier des tâches à exécuter automatiquement à des intervalles réguliers sur un système Unix/Linux. Elle utilise un fichier de configuration appelé "crontab" qui contient des lignes spécifiant les commandes à exécuter et leur fréquence.

## Usage
La syntaxe de base de la commande `crontab` est la suivante :

```bash
crontab [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `crontab` :

- `-e` : Édite le fichier crontab de l'utilisateur courant.
- `-l` : Affiche le contenu du fichier crontab de l'utilisateur courant.
- `-r` : Supprime le fichier crontab de l'utilisateur courant.
- `-i` : Demande une confirmation avant de supprimer le crontab.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `crontab` :

1. **Éditer le crontab :**
   Pour ouvrir le fichier crontab dans l'éditeur par défaut :
   ```bash
   crontab -e
   ```

2. **Lister les tâches planifiées :**
   Pour afficher toutes les tâches planifiées de l'utilisateur :
   ```bash
   crontab -l
   ```

3. **Supprimer le crontab :**
   Pour supprimer toutes les tâches planifiées (avec confirmation) :
   ```bash
   crontab -r -i
   ```

4. **Planifier une tâche :**
   Pour exécuter un script tous les jours à 2h du matin, ajoutez la ligne suivante dans le crontab :
   ```bash
   0 2 * * * /chemin/vers/script.sh
   ```

5. **Planifier une tâche chaque minute :**
   Pour exécuter une commande chaque minute :
   ```bash
   * * * * * /chemin/vers/commande
   ```

## Tips
- **Utilisez des chemins absolus :** Lorsque vous spécifiez des scripts ou des commandes, utilisez des chemins absolus pour éviter des erreurs de chemin.
- **Vérifiez les logs :** Consultez les logs du système pour diagnostiquer les problèmes d'exécution des tâches planifiées.
- **Testez vos commandes :** Avant de les ajouter au crontab, testez vos commandes dans le terminal pour vous assurer qu'elles fonctionnent comme prévu.