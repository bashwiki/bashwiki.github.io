# [리눅스] Bash xz 사용법

## Overview
Le commandement `xz` est un utilitaire de compression de fichiers qui utilise l'algorithme de compression LZMA (Lempel-Ziv-Markov chain algorithm). Son principal objectif est de réduire la taille des fichiers pour faciliter le stockage et le transfert. `xz` est particulièrement efficace pour la compression de fichiers texte et est souvent utilisé dans les distributions Linux pour compresser des paquets.

## Usage
La syntaxe de base de la commande `xz` est la suivante :

```bash
xz [options] [fichiers]
```

### Options courantes :
- `-d`, `--decompress` : Décompresse un fichier compressé.
- `-k`, `--keep` : Conserve le fichier d'origine après compression.
- `-f`, `--force` : Force la compression ou la décompression, même si cela écrase des fichiers existants.
- `-9` : Utilise le niveau de compression maximum (1 à 9, où 9 est le plus compressé).
- `-t`, `--test` : Vérifie l'intégrité d'un fichier compressé sans le décompresser.

## Examples
### Exemple 1 : Compression d'un fichier
Pour compresser un fichier nommé `exemple.txt`, vous pouvez utiliser la commande suivante :

```bash
xz exemple.txt
```
Cela créera un fichier compressé nommé `exemple.txt.xz` et supprimera le fichier d'origine.

### Exemple 2 : Décompression d'un fichier
Pour décompresser le fichier compressé que vous venez de créer, utilisez :

```bash
xz -d exemple.txt.xz
```
Cela restaurera le fichier original `exemple.txt`.

## Tips
- Pour conserver le fichier d'origine lors de la compression, utilisez l'option `-k` :

```bash
xz -k exemple.txt
```

- Si vous travaillez avec plusieurs fichiers, vous pouvez les compresser en une seule commande :

```bash
xz fichier1.txt fichier2.txt fichier3.txt
```

- Pour tester l'intégrité d'un fichier compressé sans le décompresser, utilisez :

```bash
xz -t exemple.txt.xz
```

En suivant ces conseils, vous pourrez utiliser `xz` de manière efficace pour gérer vos fichiers compressés.