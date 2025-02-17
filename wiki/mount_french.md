# [Linux] Bash mount utilisation : Monter des systèmes de fichiers

## Overview
La commande `mount` est utilisée pour monter des systèmes de fichiers dans le système d'exploitation Linux. Elle permet d'accéder à des périphériques de stockage, tels que des disques durs, des clés USB ou des partitions, en les rendant disponibles dans le système de fichiers.

## Usage
La syntaxe de base de la commande `mount` est la suivante :

```
mount [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec la commande `mount` :

- `-t type` : Spécifie le type de système de fichiers (par exemple, ext4, ntfs).
- `-o options` : Permet de définir des options de montage supplémentaires (comme `ro` pour lecture seule).
- `-a` : Monte tous les systèmes de fichiers mentionnés dans le fichier `/etc/fstab`.
- `-r` : Monte le système de fichiers en mode lecture seule.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mount` :

1. Monter une clé USB :
   ```bash
   mount /dev/sdb1 /mnt/usb
   ```

2. Monter un système de fichiers NTFS en lecture seule :
   ```bash
   mount -t ntfs -o ro /dev/sdc1 /mnt/ntfs
   ```

3. Monter tous les systèmes de fichiers définis dans `/etc/fstab` :
   ```bash
   mount -a
   ```

4. Monter une partition ext4 avec des options spécifiques :
   ```bash
   mount -t ext4 -o defaults,noatime /dev/sda1 /mnt/data
   ```

## Tips
- Assurez-vous que le répertoire de destination (point de montage) existe avant de monter un système de fichiers.
- Utilisez `umount` pour démonter un système de fichiers lorsque vous avez terminé de l'utiliser.
- Vérifiez les permissions et les options de montage pour éviter des problèmes d'accès aux données.