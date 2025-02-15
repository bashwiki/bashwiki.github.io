# [리눅스] Bash lsblk 사용법

## Overview
La commande `lsblk` (list block devices) est utilisée pour afficher des informations sur les périphériques de bloc disponibles sur un système Linux. Elle permet aux utilisateurs de visualiser la hiérarchie des périphériques de stockage, y compris les disques durs, les partitions et les volumes logiques. C'est un outil essentiel pour les ingénieurs et les développeurs qui souhaitent gérer et surveiller les périphériques de stockage.

## Usage
La syntaxe de base de la commande `lsblk` est la suivante :

```bash
lsblk [options]
```

### Options courantes :
- `-a`, `--all` : Affiche tous les périphériques, y compris ceux qui ne sont pas montés.
- `-f`, `--fs` : Affiche des informations sur le système de fichiers, y compris le type de système de fichiers et l'étiquette.
- `-l`, `--list` : Affiche les périphériques sous forme de liste plutôt que sous forme d'arborescence.
- `-o`, `--output` : Permet de spécifier les colonnes à afficher. Par exemple, `lsblk -o NAME,SIZE,TYPE,MOUNTPOINT`.
- `-p`, `--paths` : Affiche les chemins complets des périphériques.

## Examples
### Exemple 1 : Afficher la liste des périphériques de bloc
Pour afficher tous les périphériques de bloc disponibles sur votre système, utilisez la commande suivante :

```bash
lsblk
```

Cela affichera une liste des disques et partitions avec leurs tailles et points de montage.

### Exemple 2 : Afficher les informations sur le système de fichiers
Pour obtenir des informations détaillées sur les systèmes de fichiers des périphériques de bloc, vous pouvez utiliser l'option `-f` :

```bash
lsblk -f
```

Cela affichera des informations supplémentaires, telles que le type de système de fichiers et l'étiquette.

## Tips
- Utilisez l'option `-o` pour personnaliser les colonnes affichées selon vos besoins spécifiques. Cela peut rendre la sortie plus lisible et pertinente.
- Combinez `lsblk` avec d'autres commandes comme `grep` pour filtrer les résultats. Par exemple, pour trouver un périphérique spécifique, vous pouvez exécuter `lsblk | grep sda`.
- Pensez à utiliser `lsblk -a` pour voir tous les périphériques, même ceux qui ne sont pas montés, ce qui peut être utile lors de la gestion de disques externes ou de partitions non utilisées.

En utilisant `lsblk`, vous pouvez facilement obtenir une vue d'ensemble de votre configuration de stockage et prendre des décisions éclairées concernant la gestion de vos périphériques de bloc.