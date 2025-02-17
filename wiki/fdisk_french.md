# [Linux] Bash fdisk utilisation : Gestion des partitions de disque

## Overview
La commande `fdisk` est un utilitaire de partitionnement de disque utilisé sous Linux pour créer, supprimer et gérer les partitions sur un disque dur. Elle permet aux utilisateurs de manipuler les tables de partitions et de gérer l'espace de stockage de manière efficace.

## Usage
La syntaxe de base de la commande `fdisk` est la suivante :

```bash
fdisk [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `fdisk` :

- `-l` : Liste toutes les partitions sur tous les disques.
- `-u` : Utilise des unités de secteurs pour afficher les tailles de partition.
- `-s` : Affiche la taille d'une partition spécifiée.
- `-v` : Affiche la version de `fdisk`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `fdisk` :

1. **Lister les partitions sur un disque** :
   ```bash
   fdisk -l
   ```

2. **Afficher la taille d'une partition spécifique** :
   ```bash
   fdisk -s /dev/sda1
   ```

3. **Démarrer `fdisk` pour un disque spécifique** :
   ```bash
   fdisk /dev/sda
   ```

4. **Créer une nouvelle partition** :
   - Démarrez `fdisk` sur le disque :
     ```bash
     fdisk /dev/sda
     ```
   - Ensuite, suivez les instructions pour créer une nouvelle partition en utilisant la commande `n`.

## Tips
- **Sauvegarde** : Avant de modifier les partitions, assurez-vous de sauvegarder vos données importantes.
- **Utilisation prudente** : Soyez prudent lors de la suppression ou du formatage des partitions, car cela peut entraîner la perte de données.
- **Vérification** : Après avoir effectué des modifications, utilisez `fdisk -l` pour vérifier que les changements ont été appliqués correctement.