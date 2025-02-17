# [Linux] Bash gunzip : Décompresser des fichiers gzip

## Overview
La commande `gunzip` est utilisée pour décompresser des fichiers compressés au format gzip. Elle permet de restaurer les fichiers à leur état original après compression, facilitant ainsi leur utilisation.

## Usage
La syntaxe de base de la commande `gunzip` est la suivante :

```bash
gunzip [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `gunzip` :

- `-c` : Affiche le contenu décompressé sur la sortie standard sans supprimer le fichier d'origine.
- `-f` : Force la décompression, même si le fichier de destination existe déjà.
- `-k` : Conserve le fichier compressé après la décompression.
- `-r` : Décompresse les fichiers dans les sous-répertoires de manière récursive.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `gunzip` :

1. Décompresser un fichier gzip :

   ```bash
   gunzip fichier.txt.gz
   ```

2. Afficher le contenu décompressé sans supprimer le fichier d'origine :

   ```bash
   gunzip -c fichier.txt.gz
   ```

3. Décompresser tout fichier gzip dans un répertoire :

   ```bash
   gunzip *.gz
   ```

4. Décompresser un fichier tout en conservant l'original :

   ```bash
   gunzip -k fichier.txt.gz
   ```

5. Décompresser récursivement dans un répertoire :

   ```bash
   gunzip -r dossier/
   ```

## Tips
- Utilisez l'option `-c` pour vérifier le contenu d'un fichier gzip sans le décompresser.
- Si vous avez besoin de décompresser plusieurs fichiers, utilisez des jokers comme `*.gz` pour gagner du temps.
- Pensez à utiliser l'option `-k` si vous souhaitez conserver les fichiers compressés pour une utilisation future.