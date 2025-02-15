# [리눅스] Bash mpstat 사용법

## Aperçu
La commande `mpstat` est un outil de surveillance des performances du système qui fait partie du paquet `sysstat`. Elle permet d'afficher des statistiques sur l'utilisation du processeur, en fournissant des informations détaillées sur l'activité de chaque cœur de processeur. Son objectif principal est d'aider les ingénieurs et les développeurs à analyser la charge du système et à identifier les goulets d'étranglement potentiels dans les performances.

## Utilisation
La syntaxe de base de la commande `mpstat` est la suivante :

```bash
mpstat [options] [intervalle] [nombre]
```

### Options courantes :
- `-P ALL` : Affiche les statistiques pour tous les processeurs.
- `-u` : Affiche l'utilisation du processeur (c'est l'option par défaut).
- `-h` : Affiche un aide-mémoire avec les options disponibles.
- `intervalle` : Spécifie la durée (en secondes) entre chaque affichage des statistiques.
- `nombre` : Indique combien de fois les statistiques doivent être affichées.

## Exemples
### Exemple 1 : Afficher l'utilisation du processeur toutes les 2 secondes
Pour afficher l'utilisation du processeur toutes les 2 secondes pendant 5 itérations, vous pouvez utiliser la commande suivante :

```bash
mpstat 2 5
```

### Exemple 2 : Afficher les statistiques de tous les processeurs
Pour voir les statistiques de tous les cœurs de processeur en temps réel, utilisez l'option `-P ALL` :

```bash
mpstat -P ALL 1
```

Cette commande affichera les statistiques de chaque processeur toutes les secondes.

## Conseils
- Utilisez `mpstat` en combinaison avec d'autres outils comme `iostat` et `vmstat` pour obtenir une vue d'ensemble complète des performances du système.
- Surveillez régulièrement l'utilisation du processeur pour identifier les tendances et les pics d'activité, ce qui peut vous aider à optimiser les performances de vos applications.
- Pensez à rediriger la sortie de `mpstat` vers un fichier pour une analyse ultérieure, par exemple :

```bash
mpstat 2 5 > statistiques_processeur.txt
```

Cela vous permettra de conserver un historique des performances du processeur pour une analyse approfondie.