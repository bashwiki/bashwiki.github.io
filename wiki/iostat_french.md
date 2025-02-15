# [리눅스] Bash iostat 사용법

## Overview
La commande `iostat` est un outil de surveillance des performances des systèmes d'exploitation Unix et Linux. Elle permet de collecter et d'afficher des statistiques sur l'utilisation des entrées/sorties (I/O) des disques et des partitions, ainsi que sur l'utilisation du processeur. Son principal objectif est d'aider les administrateurs système et les développeurs à comprendre et à diagnostiquer les goulets d'étranglement liés aux performances I/O, ce qui est essentiel pour optimiser les performances des applications et des systèmes.

## Usage
La syntaxe de base de la commande `iostat` est la suivante :

```bash
iostat [options] [intervalle] [compte]
```

### Options courantes :
- `-c` : Affiche uniquement les statistiques du processeur.
- `-d` : Affiche uniquement les statistiques des disques.
- `-x` : Affiche des statistiques étendues pour chaque disque.
- `-m` : Affiche les statistiques en mégaoctets par seconde.
- `-p` : Affiche les statistiques pour les partitions et les disques.

L'intervalle et le compte permettent de spécifier la fréquence à laquelle les statistiques doivent être mises à jour et le nombre de mises à jour à afficher.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `iostat`.

### Exemple 1 : Afficher les statistiques de base
Pour afficher les statistiques de base sur l'utilisation des disques et du processeur, vous pouvez exécuter la commande suivante :

```bash
iostat
```

### Exemple 2 : Afficher les statistiques étendues des disques toutes les 5 secondes
Pour obtenir des statistiques détaillées sur les disques toutes les 5 secondes, utilisez la commande suivante :

```bash
iostat -x 5
```

## Tips
- Utilisez l'option `-m` pour obtenir des résultats plus lisibles en mégaoctets, ce qui facilite l'interprétation des données de performance.
- Combinez `iostat` avec d'autres outils comme `vmstat` ou `top` pour obtenir une vue d'ensemble plus complète des performances de votre système.
- Surveillez les valeurs de `iowait` dans les statistiques du processeur pour identifier les goulets d'étranglement liés aux I/O. Si `iowait` est élevé, cela peut indiquer que le système attend trop longtemps pour les opérations d'entrée/sortie.