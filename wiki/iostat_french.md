# [Linux] Bash iostat Utilisation : Surveillance des performances d'entrée/sortie

## Overview
La commande `iostat` est utilisée pour surveiller les performances des systèmes d'entrée/sortie (E/S) en affichant des statistiques sur l'utilisation du processeur ainsi que sur les périphériques de stockage. Elle permet aux administrateurs système d'identifier les goulets d'étranglement et d'optimiser les performances du système.

## Usage
La syntaxe de base de la commande `iostat` est la suivante :

```bash
iostat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `iostat` :

- `-c` : Affiche uniquement les statistiques du processeur.
- `-d` : Affiche uniquement les statistiques des périphériques de stockage.
- `-x` : Affiche des statistiques étendues pour les périphériques.
- `-m` : Affiche les statistiques en mégaoctets.
- `interval` : Définit l'intervalle de temps entre les rapports.
- `count` : Définit le nombre de rapports à afficher.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `iostat` :

1. Afficher les statistiques de base du processeur et des périphériques de stockage :
   ```bash
   iostat
   ```

2. Afficher uniquement les statistiques du processeur :
   ```bash
   iostat -c
   ```

3. Afficher des statistiques étendues pour les périphériques de stockage :
   ```bash
   iostat -x
   ```

4. Afficher les statistiques en mégaoctets toutes les 5 secondes, pour un total de 3 rapports :
   ```bash
   iostat -m 5 3
   ```

5. Afficher uniquement les statistiques des périphériques de stockage avec un intervalle de 10 secondes :
   ```bash
   iostat -d 10
   ```

## Tips
- Utilisez `iostat` en combinaison avec d'autres outils comme `vmstat` et `mpstat` pour obtenir une vue d'ensemble complète des performances du système.
- Surveillez régulièrement les statistiques pour détecter les tendances et anticiper les problèmes de performance.
- Pensez à rediriger la sortie de `iostat` vers un fichier pour une analyse ultérieure, par exemple :
  ```bash
  iostat -x 5 10 > iostat_output.txt
  ```