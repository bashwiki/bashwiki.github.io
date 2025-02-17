# [Linux] Bash cron utilisation : Planification de tâches automatisées

## Overview
La commande `cron` est utilisée pour planifier l'exécution de tâches à des intervalles réguliers sur un système Unix/Linux. Elle permet aux utilisateurs de configurer des commandes ou des scripts à exécuter automatiquement à des moments spécifiques.

## Usage
La syntaxe de base de la commande `cron` est la suivante :

```bash
cron [options] [arguments]
```

Cependant, pour utiliser `cron`, vous devez généralement éditer le fichier crontab qui contient les tâches à exécuter.

## Common Options
Voici quelques options courantes pour `cron` :

- `-e` : Éditer le fichier crontab de l'utilisateur.
- `-l` : Lister les tâches cron de l'utilisateur.
- `-r` : Supprimer le fichier crontab de l'utilisateur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `cron` :

1. **Éditer le crontab :**
   Pour ajouter ou modifier des tâches cron, utilisez la commande suivante :
   ```bash
   crontab -e
   ```

2. **Lister les tâches cron :**
   Pour voir toutes les tâches cron configurées pour l'utilisateur actuel :
   ```bash
   crontab -l
   ```

3. **Exécuter un script tous les jours à 2h du matin :**
   Ajoutez la ligne suivante dans le fichier crontab :
   ```bash
   0 2 * * * /chemin/vers/votre/script.sh
   ```

4. **Exécuter une commande chaque lundi à 9h :**
   Ajoutez la ligne suivante dans le fichier crontab :
   ```bash
   0 9 * * 1 /usr/bin/somecommand
   ```

5. **Exécuter un script toutes les 15 minutes :**
   Ajoutez la ligne suivante dans le fichier crontab :
   ```bash
   */15 * * * * /chemin/vers/votre/script.sh
   ```

## Tips
- **Vérifiez les logs :** Consultez les logs de cron pour diagnostiquer les problèmes d'exécution des tâches. Les logs se trouvent généralement dans `/var/log/syslog` ou `/var/log/cron`.
- **Utilisez des chemins absolus :** Lorsque vous spécifiez des scripts ou des commandes dans crontab, utilisez des chemins absolus pour éviter les problèmes de chemin.
- **Testez vos commandes :** Avant de les ajouter à cron, testez vos commandes manuellement dans le terminal pour vous assurer qu'elles fonctionnent comme prévu.