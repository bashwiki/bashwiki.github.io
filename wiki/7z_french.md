# [리눅스] Bash 7z 사용법

## Overview
La commande `7z` est un outil de compression et de décompression de fichiers qui fait partie de l'archiveur 7-Zip. Elle est largement utilisée pour créer des archives compressées dans divers formats, notamment `.7z`, `.zip`, `.tar`, et bien d'autres. Son principal objectif est de réduire la taille des fichiers pour faciliter le stockage et le transfert, tout en offrant des fonctionnalités avancées telles que le chiffrement et la gestion des volumes.

## Usage
La syntaxe de base de la commande `7z` est la suivante :

```
7z [commande] [options] [archive] [fichiers]
```

### Commandes courantes
- `a` : Ajouter des fichiers à une archive.
- `x` : Extraire des fichiers d'une archive.
- `l` : Lister le contenu d'une archive.
- `d` : Supprimer des fichiers d'une archive.

### Options communes
- `-p` : Spécifier un mot de passe pour le chiffrement.
- `-m0=Type` : Définir le type de méthode de compression (ex. `-m0=lzma`).
- `-v` : Créer des volumes d'archive (utile pour les fichiers de grande taille).

## Examples
### Exemple 1 : Créer une archive
Pour créer une archive compressée nommée `archive.7z` contenant tous les fichiers du répertoire courant, utilisez la commande suivante :

```bash
7z a archive.7z *
```

### Exemple 2 : Extraire une archive
Pour extraire le contenu d'une archive `archive.7z` dans le répertoire courant, utilisez la commande suivante :

```bash
7z x archive.7z
```

## Tips
- Utilisez l'option `-p` pour protéger vos archives avec un mot de passe, surtout si elles contiennent des informations sensibles.
- Pour optimiser la compression, testez différentes méthodes de compression avec l'option `-m0=Type`.
- Pensez à utiliser l'option `-v` si vous travaillez avec de très gros fichiers, afin de les diviser en plusieurs volumes plus faciles à gérer.
- Consultez la documentation officielle de 7-Zip pour découvrir toutes les fonctionnalités avancées et les options disponibles.