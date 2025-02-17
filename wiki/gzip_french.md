# [Linux] Bash gzip Utilisation : Compresser des fichiers

## Overview
La commande `gzip` est utilisée pour compresser des fichiers en utilisant l'algorithme de compression DEFLATE. Elle réduit la taille des fichiers, ce qui permet d'économiser de l'espace disque et de faciliter le transfert de données.

## Usage
La syntaxe de base de la commande `gzip` est la suivante :

```bash
gzip [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `gzip` :

- `-d`, `--decompress` : Décompresse un fichier compressé.
- `-k`, `--keep` : Garde le fichier d'origine après compression.
- `-v`, `--verbose` : Affiche des informations détaillées sur le processus de compression.
- `-r`, `--recursive` : Compresse tous les fichiers dans un répertoire et ses sous-répertoires.
- `-f`, `--force` : Force la compression, même si le fichier existe déjà.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `gzip` :

1. **Compresser un fichier :**
   ```bash
   gzip monfichier.txt
   ```

2. **Décompresser un fichier :**
   ```bash
   gzip -d monfichier.txt.gz
   ```

3. **Compresser un fichier tout en gardant l'original :**
   ```bash
   gzip -k monfichier.txt
   ```

4. **Compresser tous les fichiers d'un répertoire :**
   ```bash
   gzip -r mon_repertoire/
   ```

5. **Afficher des informations détaillées lors de la compression :**
   ```bash
   gzip -v monfichier.txt
   ```

## Tips
- Utilisez l'option `-k` si vous souhaitez conserver le fichier d'origine après compression.
- Pour une compression plus efficace, vous pouvez utiliser `gzip` avec des fichiers de grande taille.
- Pensez à vérifier l'espace disque disponible avant de compresser de nombreux fichiers, surtout si vous ne gardez pas les originaux.