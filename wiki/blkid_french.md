# [리눅스] Bash blkid 사용법

## Overview
La commande `blkid` est un utilitaire de ligne de commande sous Linux qui permet d'afficher les informations sur les périphériques de bloc. Son objectif principal est d'identifier les systèmes de fichiers et les partitions sur les disques, en fournissant des détails tels que le type de système de fichiers, l'UUID (Identifiant Universel Unique), et le label des partitions. Cela est particulièrement utile pour la gestion des disques et des systèmes de fichiers.

## Usage
La syntaxe de base de la commande `blkid` est la suivante :

```bash
blkid [options] [device...]
```

### Options courantes :
- `-o` : Spécifie le format de sortie. Par exemple, `-o value` pour afficher uniquement les valeurs.
- `-s` : Permet de sélectionner les attributs à afficher, comme `UUID`, `TYPE`, etc.
- `-p` : Ignore les périphériques non montés.
- `-c` : Utilise un fichier de cache pour améliorer les performances.

## Examples
### Exemple 1 : Afficher toutes les informations sur les périphériques de bloc
Pour afficher toutes les informations sur les périphériques de bloc disponibles, il suffit d'exécuter :

```bash
blkid
```

Cela affichera une liste de tous les périphériques de bloc avec leurs attributs respectifs.

### Exemple 2 : Afficher uniquement l'UUID d'un périphérique spécifique
Pour afficher uniquement l'UUID d'un périphérique spécifique, vous pouvez utiliser l'option `-s` comme suit :

```bash
blkid -s UUID /dev/sda1
```

Cela retournera l'UUID de la partition `/dev/sda1`.

## Tips
- Utilisez `blkid` avec des privilèges d'administrateur (par exemple, avec `sudo`) pour garantir que vous avez accès à toutes les informations des périphériques.
- Pour une sortie plus lisible, envisagez d'utiliser l'option `-o value` pour obtenir uniquement les valeurs sans les étiquettes.
- Pensez à utiliser `blkid` dans des scripts pour automatiser la gestion des disques et des systèmes de fichiers.