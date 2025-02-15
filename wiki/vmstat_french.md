# [리눅스] Bash vmstat 사용법

## Overview
La commande `vmstat` (Virtual Memory Statistics) est un outil de surveillance des performances du système qui fournit des informations sur la mémoire virtuelle, les processus, les entrées/sorties, et l'utilisation du CPU. Son objectif principal est d'aider les ingénieurs et les développeurs à analyser le comportement du système et à identifier les goulets d'étranglement en matière de ressources.

## Usage
La syntaxe de base de la commande `vmstat` est la suivante :

```bash
vmstat [options] [interval] [count]
```

### Options courantes :
- `-a` : Affiche des informations sur la mémoire active et inactive.
- `-m` : Affiche des statistiques sur la mémoire de page.
- `-s` : Affiche un résumé des statistiques de mémoire.
- `-d` : Affiche des statistiques sur les disques.
- `interval` : Définit l'intervalle en secondes entre les mises à jour des statistiques.
- `count` : Définit le nombre de mises à jour à afficher.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `vmstat`.

### Exemple 1 : Surveillance de la mémoire et du CPU
Pour afficher les statistiques de la mémoire et du CPU toutes les 2 secondes pendant 5 itérations, vous pouvez utiliser la commande suivante :

```bash
vmstat 2 5
```

### Exemple 2 : Affichage des statistiques de la mémoire de page
Pour obtenir des informations détaillées sur la mémoire de page, utilisez l'option `-m` :

```bash
vmstat -m
```

## Tips
- Utilisez `vmstat` en combinaison avec d'autres outils comme `top` ou `iostat` pour une analyse plus complète des performances du système.
- Surveillez régulièrement l'utilisation de la mémoire et du CPU pour anticiper les problèmes de performance avant qu'ils ne deviennent critiques.
- Considérez l'utilisation de l'option `-s` pour obtenir un résumé rapide des statistiques de mémoire, ce qui peut être utile pour un diagnostic rapide.

En utilisant `vmstat`, vous pouvez obtenir une vue d'ensemble utile des performances de votre système, ce qui vous permet de prendre des décisions éclairées sur l'optimisation des ressources.