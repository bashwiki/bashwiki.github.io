# [Linux] Bash mpstat Utilisation : Surveillance des statistiques de CPU

## Overview
La commande `mpstat` est utilisée pour afficher les statistiques d'utilisation du processeur sur un système. Elle permet de surveiller la charge CPU par cœur, offrant ainsi une vue d'ensemble des performances du système.

## Usage
La syntaxe de base de la commande `mpstat` est la suivante :

```bash
mpstat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `mpstat` :

- `-P ALL` : Affiche les statistiques pour tous les processeurs.
- `-u` : Affiche l'utilisation du CPU en pourcentage.
- `-r` : Affiche les statistiques de mémoire.
- `-h` : Affiche l'aide et les options disponibles.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `mpstat` :

1. Afficher les statistiques d'utilisation CPU pour tous les processeurs :
   ```bash
   mpstat -P ALL
   ```

2. Afficher l'utilisation CPU en pourcentage :
   ```bash
   mpstat -u
   ```

3. Afficher les statistiques de mémoire :
   ```bash
   mpstat -r
   ```

4. Afficher les statistiques toutes les 5 secondes :
   ```bash
   mpstat 5
   ```

## Tips
- Utilisez `mpstat -P ALL` pour obtenir une vue détaillée de chaque cœur de processeur, ce qui est utile pour le diagnostic de performances.
- Combinez `mpstat` avec d'autres outils comme `grep` pour filtrer les résultats selon vos besoins.
- Pensez à exécuter `mpstat` avec des privilèges d'administrateur pour obtenir des informations complètes sur le système.