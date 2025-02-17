# [Linux] Bash vmstat Utilisation : Afficher les statistiques système

## Overview
La commande `vmstat` (Virtual Memory Statistics) est utilisée pour afficher des informations sur la mémoire virtuelle, les processus, les entrées/sorties, et l'utilisation du CPU. Elle permet aux utilisateurs de surveiller les performances du système en temps réel.

## Usage
La syntaxe de base de la commande `vmstat` est la suivante :

```bash
vmstat [options] [interval] [count]
```

## Common Options
Voici quelques options courantes pour la commande `vmstat` :

- `-a` : Affiche des informations sur la mémoire active et inactive.
- `-m` : Affiche des informations sur la mémoire utilisée par les caches.
- `-s` : Affiche un résumé des statistiques de mémoire.
- `interval` : Définit l'intervalle de temps entre les mises à jour des statistiques (en secondes).
- `count` : Définit le nombre de mises à jour à afficher.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `vmstat` :

1. Afficher les statistiques système toutes les 2 secondes :

    ```bash
    vmstat 2
    ```

2. Afficher les statistiques de mémoire avec un résumé :

    ```bash
    vmstat -s
    ```

3. Afficher les statistiques toutes les 5 secondes, 10 fois :

    ```bash
    vmstat 5 10
    ```

4. Afficher les informations sur la mémoire active et inactive :

    ```bash
    vmstat -a
    ```

5. Afficher les statistiques de mémoire avec des informations sur les caches :

    ```bash
    vmstat -m
    ```

## Tips
- Utilisez `vmstat` en combinaison avec d'autres outils comme `top` ou `htop` pour une surveillance plus complète du système.
- Surveillez régulièrement les valeurs de mémoire et d'utilisation du CPU pour détecter les goulets d'étranglement.
- Pensez à rediriger la sortie de `vmstat` vers un fichier pour une analyse ultérieure, par exemple : 

    ```bash
    vmstat 2 > vmstat_output.txt
    ``` 

Ces conseils vous aideront à tirer le meilleur parti de la commande `vmstat` pour surveiller les performances de votre système.