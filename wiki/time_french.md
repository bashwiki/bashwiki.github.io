# [Linux] Bash time utilisation : mesurer le temps d'exécution des commandes

## Overview
La commande `time` permet de mesurer le temps d'exécution d'une commande ou d'un programme dans un terminal. Elle fournit des informations sur le temps écoulé, le temps CPU utilisé et d'autres statistiques utiles.

## Usage
La syntaxe de base de la commande `time` est la suivante :

```bash
time [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `time` :

- `-p` : Affiche le temps au format POSIX.
- `-o <file>` : Enregistre la sortie dans un fichier spécifié.
- `-v` : Affiche des informations détaillées sur l'exécution.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `time` :

1. Mesurer le temps d'exécution d'une commande simple :

    ```bash
    time ls -l
    ```

2. Mesurer le temps d'exécution d'un script :

    ```bash
    time ./mon_script.sh
    ```

3. Enregistrer la sortie dans un fichier :

    ```bash
    time -o temps.txt ./mon_programme
    ```

4. Afficher des informations détaillées sur l'exécution :

    ```bash
    time -v ./mon_autre_programme
    ```

## Tips
- Utilisez l'option `-o` pour conserver les résultats dans un fichier pour une analyse ultérieure.
- Combinez `time` avec des commandes complexes pour optimiser les performances.
- N'oubliez pas que `time` mesure uniquement le temps d'exécution de la commande spécifiée, pas celui des sous-commandes.