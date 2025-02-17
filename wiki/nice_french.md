# [Linux] Bash nice utilisation : Gérer la priorité des processus

## Overview
La commande `nice` permet de modifier la priorité d'exécution des processus sous Linux. En ajustant la priorité, vous pouvez influencer la quantité de ressources CPU qu'un processus peut utiliser, ce qui est particulièrement utile pour gérer les performances des applications en cours d'exécution.

## Usage
La syntaxe de base de la commande `nice` est la suivante :

```bash
nice [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `nice` :

- `-n`, `--adjustment`: Définit la valeur d'ajustement de la priorité (de -20 à 19).
- `-h`, `--help`: Affiche l'aide et les options disponibles.
- `-v`, `--version`: Affiche la version de la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `nice` :

1. Lancer un processus avec une priorité réduite :
   ```bash
   nice -n 10 ./mon_script.sh
   ```

2. Lancer un processus avec une priorité plus élevée (nécessite des privilèges administratifs) :
   ```bash
   sudo nice -n -5 ./mon_autre_script.sh
   ```

3. Vérifier la priorité d'un processus en cours d'exécution :
   ```bash
   ps -o pid,ni,cmd
   ```

## Tips
- Utilisez `nice` pour les tâches de fond qui ne nécessitent pas une utilisation intensive du CPU, afin de ne pas perturber les autres processus.
- Évitez d'utiliser des valeurs de priorité trop élevées (négatives) pour ne pas monopoliser le CPU.
- Combinez `nice` avec d'autres commandes comme `nohup` pour exécuter des processus en arrière-plan sans interruption.