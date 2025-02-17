# [Linux] Bash 7z Utilisation : Compresser et décompresser des fichiers

## Overview
La commande `7z` est un outil puissant pour la compression et la décompression de fichiers. Elle fait partie de l'archiveur 7-Zip, qui supporte plusieurs formats d'archive, y compris 7z, ZIP, RAR, et bien d'autres. Grâce à sa capacité à réduire la taille des fichiers, elle est très utile pour le stockage et le partage de données.

## Usage
La syntaxe de base de la commande `7z` est la suivante :

```
7z [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec la commande `7z` :

- `a` : Ajouter des fichiers à une archive.
- `x` : Extraire des fichiers d'une archive.
- `t` : Tester l'intégrité d'une archive.
- `l` : Lister le contenu d'une archive.
- `d` : Supprimer des fichiers d'une archive.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `7z` :

1. **Créer une archive 7z :**
   ```bash
   7z a archive.7z fichier1.txt fichier2.txt
   ```

2. **Extraire une archive 7z :**
   ```bash
   7z x archive.7z
   ```

3. **Lister le contenu d'une archive :**
   ```bash
   7z l archive.7z
   ```

4. **Tester l'intégrité d'une archive :**
   ```bash
   7z t archive.7z
   ```

5. **Supprimer un fichier d'une archive :**
   ```bash
   7z d archive.7z fichier1.txt
   ```

## Tips
- Utilisez des options de compression spécifiques pour optimiser la taille de l'archive, comme `-mx=9` pour une compression maximale.
- Pensez à vérifier l'intégrité de vos archives avec l'option `t` avant de les partager.
- Pour des archives volumineuses, envisagez de diviser l'archive en plusieurs volumes en utilisant l'option `-v` (par exemple, `7z a -v10m archive.7z fichier1 fichier2` pour créer des volumes de 10 Mo).