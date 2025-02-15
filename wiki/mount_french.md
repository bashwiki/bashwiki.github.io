# [리눅스] Bash mount 사용법

## Overview
La commande `mount` est utilisée dans les systèmes d'exploitation de type Unix pour monter des systèmes de fichiers. Son objectif principal est de rendre un système de fichiers accessible à partir d'un point de montage dans l'arborescence du système de fichiers. En d'autres termes, `mount` permet à l'utilisateur d'accéder à des partitions, des disques ou des périphériques externes en les intégrant dans le système de fichiers existant.

## Usage
La syntaxe de base de la commande `mount` est la suivante :

```bash
mount [options] <source> <target>
```

- `<source>` : Il s'agit du chemin vers le périphérique ou le système de fichiers que vous souhaitez monter (par exemple, `/dev/sdb1`).
- `<target>` : C'est le point de montage où le système de fichiers sera accessible (par exemple, `/mnt/usb`).

### Options courantes :
- `-o` : Permet de spécifier des options de montage, comme `ro` (lecture seule), `rw` (lecture-écriture), etc.
- `-t` : Indique le type de système de fichiers (par exemple, `ext4`, `ntfs`, `vfat`).
- `-a` : Monte tous les systèmes de fichiers énumérés dans `/etc/fstab`.

## Examples
### Exemple 1 : Monter une partition
Pour monter une partition `ext4` située sur `/dev/sdb1` dans le répertoire `/mnt/data`, vous pouvez utiliser la commande suivante :

```bash
sudo mount -t ext4 /dev/sdb1 /mnt/data
```

### Exemple 2 : Monter une clé USB en lecture seule
Si vous souhaitez monter une clé USB en mode lecture seule, vous pouvez utiliser :

```bash
sudo mount -o ro /dev/sdc1 /mnt/usb
```

## Tips
- Assurez-vous que le répertoire cible (point de montage) existe avant de tenter de monter un système de fichiers. Vous pouvez créer un répertoire avec `mkdir`.
- Pour démonter un système de fichiers, utilisez la commande `umount` suivie du point de montage ou du périphérique.
- Vérifiez les systèmes de fichiers montés avec la commande `df -h` pour obtenir des informations sur l'espace utilisé et disponible.
- Soyez prudent lors du montage de systèmes de fichiers, surtout ceux qui contiennent des données critiques, pour éviter la corruption des données.