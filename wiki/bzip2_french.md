# [리눅스] Bash bzip2 사용법

## Overview
Le command `bzip2` est un utilitaire de compression de fichiers qui utilise l'algorithme de compression Burrows-Wheeler. Son objectif principal est de réduire la taille des fichiers, ce qui facilite leur stockage et leur transfert. `bzip2` est particulièrement efficace pour compresser des fichiers texte et peut atteindre des taux de compression plus élevés que d'autres utilitaires comme `gzip`.

## Usage
La syntaxe de base de la commande `bzip2` est la suivante :

```bash
bzip2 [options] [fichier...]
```

### Options courantes :
- `-d`, `--decompress` : Décompresse un fichier `.bz2`.
- `-k`, `--keep` : Garde le fichier d'origine après compression.
- `-f`, `--force` : Force la compression, même si le fichier de destination existe déjà.
- `-v`, `--verbose` : Affiche des informations détaillées sur le processus de compression.
- `-z`, `--compress` : Compresse le fichier (comportement par défaut).

## Examples
### Exemple 1 : Compression d'un fichier
Pour compresser un fichier nommé `exemple.txt`, vous pouvez utiliser la commande suivante :

```bash
bzip2 exemple.txt
```
Cela créera un fichier compressé nommé `exemple.txt.bz2` et supprimera le fichier d'origine.

### Exemple 2 : Décompression d'un fichier
Pour décompresser un fichier compressé, utilisez l'option `-d` :

```bash
bzip2 -d exemple.txt.bz2
```
Cela restaurera le fichier d'origine `exemple.txt` et supprimera le fichier compressé.

## Tips
- Utilisez l'option `-k` si vous souhaitez conserver le fichier d'origine après la compression. Par exemple :

```bash
bzip2 -k exemple.txt
```

- Pour compresser plusieurs fichiers à la fois, vous pouvez les spécifier tous dans la même commande :

```bash
bzip2 fichier1.txt fichier2.txt fichier3.txt
```

- Si vous travaillez avec des fichiers très volumineux, envisagez d'utiliser `pbzip2`, une version parallèle de `bzip2`, qui peut accélérer le processus de compression en utilisant plusieurs cœurs de processeur.