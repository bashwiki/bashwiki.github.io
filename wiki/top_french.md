# [리눅스] Bash top 사용법

## Overview
La commande `top` est un utilitaire de surveillance des processus en temps réel sous Linux et d'autres systèmes d'exploitation Unix. Elle fournit une vue dynamique des processus en cours d'exécution, affichant des informations telles que l'utilisation du CPU, la mémoire, et d'autres ressources système. L'objectif principal de `top` est d'aider les ingénieurs et les développeurs à identifier les processus gourmands en ressources et à surveiller la performance du système.

## Usage
La syntaxe de base de la commande `top` est la suivante :

```bash
top [options]
```

### Options courantes :
- `-d <seconds>` : Définit l'intervalle de mise à jour en secondes. Par défaut, `top` se met à jour toutes les 3 secondes.
- `-n <number>` : Spécifie le nombre d'itérations à afficher avant de quitter. Par exemple, `-n 5` affichera 5 mises à jour avant de terminer.
- `-u <username>` : Affiche uniquement les processus appartenant à l'utilisateur spécifié.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `top`.

### Exemple 1 : Lancer `top` avec mise à jour toutes les 5 secondes
```bash
top -d 5
```
Cette commande lancera `top` et mettra à jour l'affichage toutes les 5 secondes.

### Exemple 2 : Afficher les processus d'un utilisateur spécifique
```bash
top -u john
```
Cette commande affichera uniquement les processus en cours d'exécution par l'utilisateur nommé "john".

## Tips
- Utilisez la touche `h` pendant que `top` est en cours d'exécution pour afficher l'aide intégrée et découvrir d'autres fonctionnalités.
- Vous pouvez trier les processus en appuyant sur les touches `P` (pour le CPU) ou `M` (pour la mémoire) pendant l'exécution de `top`.
- Pour quitter `top`, appuyez sur `q`.
- Pensez à utiliser `htop`, une alternative à `top`, qui offre une interface plus conviviale et des fonctionnalités supplémentaires, si elle est installée sur votre système. 

En utilisant `top`, vous pouvez efficacement surveiller et gérer les ressources de votre système, ce qui est essentiel pour maintenir des performances optimales lors du développement et du déploiement d'applications.