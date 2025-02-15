# [리눅스] Bash fdisk 사용법

## Overview
La commande `fdisk` est un utilitaire de partitionnement de disque sous Linux. Son objectif principal est de créer, supprimer, redimensionner et gérer les partitions sur un disque dur. `fdisk` est particulièrement utile pour les administrateurs système et les développeurs qui ont besoin de gérer la structure de stockage de leurs systèmes.

## Usage
La syntaxe de base de la commande `fdisk` est la suivante :

```
fdisk [options] <disque>
```

### Options courantes :
- `-l` : Liste toutes les partitions sur tous les disques.
- `-u` : Utilise les unités de secteurs pour les tailles de partition.
- `-v` : Affiche la version de `fdisk`.
- `-s <disque>` : Affiche la taille d'une partition spécifiée.

## Examples
### Exemple 1 : Lister les partitions
Pour afficher toutes les partitions sur tous les disques, vous pouvez utiliser la commande suivante :

```bash
fdisk -l
```

Cette commande affichera une liste de tous les disques et de leurs partitions, y compris des informations sur la taille, le type et le système de fichiers.

### Exemple 2 : Vérifier la taille d'une partition spécifique
Pour connaître la taille d'une partition, par exemple `/dev/sda1`, vous pouvez exécuter :

```bash
fdisk -s /dev/sda1
```

Cela affichera la taille de la partition spécifiée en secteurs.

## Tips
- **Prudence** : Lorsque vous utilisez `fdisk`, soyez très prudent, surtout lors de la création ou de la suppression de partitions, car cela peut entraîner la perte de données.
- **Sauvegarde** : Avant de modifier des partitions, il est toujours recommandé de sauvegarder vos données importantes.
- **Utilisation avec sudo** : La plupart des opérations nécessitent des privilèges d'administrateur, donc n'oubliez pas d'utiliser `sudo` si nécessaire.
- **Documentation** : Consultez la page de manuel de `fdisk` en utilisant `man fdisk` pour obtenir des informations détaillées sur les options et l'utilisation.