# [리눅스] Bash free 사용법

## Overview
La commande `free` est un outil essentiel dans les systèmes d'exploitation basés sur Linux qui permet aux utilisateurs de surveiller l'utilisation de la mémoire du système. Elle fournit des informations sur la mémoire totale, utilisée, libre, ainsi que sur la mémoire tampon et le cache. L'objectif principal de cette commande est d'aider les ingénieurs et développeurs à évaluer la performance de la mémoire et à diagnostiquer d'éventuels problèmes liés à la mémoire.

## Usage
La syntaxe de base de la commande `free` est la suivante :

```
free [options]
```

### Options courantes :
- `-h` : Affiche les valeurs dans un format lisible par l'homme (par exemple, en utilisant des unités comme Ko, Mo, Go).
- `-m` : Affiche les valeurs en mégaoctets.
- `-g` : Affiche les valeurs en gigaoctets.
- `-s <seconds>` : Met à jour les informations à intervalles réguliers spécifiés en secondes.
- `-t` : Affiche une ligne supplémentaire avec les totaux de la mémoire.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `free`.

### Exemple 1 : Afficher l'utilisation de la mémoire en format lisible
```bash
free -h
```
Cet exemple affiche l'utilisation de la mémoire avec des unités compréhensibles, facilitant ainsi la lecture des données.

### Exemple 2 : Afficher l'utilisation de la mémoire toutes les 5 secondes
```bash
free -h -s 5
```
Cette commande met à jour et affiche l'utilisation de la mémoire toutes les 5 secondes, ce qui est utile pour surveiller les changements en temps réel.

## Tips
- Utilisez l'option `-h` pour rendre les résultats plus faciles à interpréter, surtout si vous travaillez avec de grandes quantités de mémoire.
- Combinez `free` avec d'autres commandes comme `watch` pour surveiller l'utilisation de la mémoire en continu :
  ```bash
  watch free -h
  ```
- Pensez à vérifier régulièrement l'utilisation de la mémoire, surtout lors de l'exécution d'applications gourmandes en ressources, afin d'anticiper les problèmes de performance.