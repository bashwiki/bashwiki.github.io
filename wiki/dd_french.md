# [Linux] Bash dd : Copier et convertir des fichiers

## Overview
La commande `dd` est un utilitaire puissant utilisé pour copier et convertir des fichiers. Il est souvent utilisé pour créer des images de disque, sauvegarder des partitions ou transférer des données entre différents formats.

## Usage
La syntaxe de base de la commande `dd` est la suivante :

```bash
dd [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `dd` :

- `if=` : Spécifie le fichier d'entrée (input file).
- `of=` : Spécifie le fichier de sortie (output file).
- `bs=` : Définit la taille du bloc à lire et à écrire.
- `count=` : Limite le nombre de blocs à copier.
- `status=` : Affiche des informations sur le statut de la commande (par exemple, `none`, `noxfer`, `progress`).

## Common Examples

### Copier un fichier
Pour copier un fichier d'un emplacement à un autre :

```bash
dd if=source.txt of=destination.txt
```

### Créer une image ISO d'un disque
Pour créer une image ISO d'un disque (par exemple, `/dev/sr0`) :

```bash
dd if=/dev/sr0 of=image.iso bs=2048
```

### Sauvegarder une partition
Pour sauvegarder une partition (par exemple, `/dev/sda1`) dans un fichier :

```bash
dd if=/dev/sda1 of=backup.img bs=4M
```

### Restaurer une image sur un disque
Pour restaurer une image sur un disque :

```bash
dd if=backup.img of=/dev/sda1 bs=4M
```

### Copier des données avec un affichage de progression
Pour copier des données tout en affichant la progression :

```bash
dd if=/dev/zero of=output.img bs=1M count=100 status=progress
```

## Tips
- **Soyez prudent** : `dd` peut écraser des données sans avertissement. Vérifiez toujours les fichiers d'entrée et de sortie.
- **Utilisez `status=progress`** : Cela vous permet de suivre la progression de la commande, ce qui est utile pour les grandes opérations.
- **Testez avec un petit fichier** : Avant d'exécuter des commandes sur des disques ou des partitions, testez avec des fichiers plus petits pour éviter des erreurs coûteuses.