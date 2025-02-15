# [리눅스] Bash rsync 사용법

## Overview
`rsync` est un outil de synchronisation de fichiers très puissant et flexible utilisé dans les systèmes Unix et Linux. Son objectif principal est de transférer et de synchroniser des fichiers et des répertoires entre deux emplacements, que ce soit sur la même machine ou entre des machines distantes. `rsync` est particulièrement apprécié pour sa capacité à ne transférer que les différences entre les fichiers source et destination, ce qui le rend très efficace en termes de bande passante et de temps.

## Usage
La syntaxe de base de la commande `rsync` est la suivante :

```bash
rsync [options] source destination
```

### Options courantes :
- `-a` : Archive mode. Cela permet de conserver les permissions, les timestamps, et de copier les répertoires de manière récursive.
- `-v` : Verbose. Affiche des informations détaillées sur le processus de synchronisation.
- `-z` : Compression. Compresse les fichiers pendant le transfert pour économiser de la bande passante.
- `-r` : Récursif. Copie les répertoires de manière récursive.
- `--delete` : Supprime les fichiers dans la destination qui ne sont pas présents dans la source.

## Examples
### Exemple 1 : Synchroniser un répertoire local
Pour synchroniser un répertoire local vers un autre répertoire local, vous pouvez utiliser la commande suivante :

```bash
rsync -av /chemin/vers/source/ /chemin/vers/destination/
```

Cette commande copie tous les fichiers et répertoires de `source` vers `destination`, en préservant les permissions et les timestamps.

### Exemple 2 : Synchroniser avec un serveur distant
Pour synchroniser un répertoire local vers un serveur distant, utilisez la commande suivante :

```bash
rsync -avz /chemin/vers/source/ utilisateur@serveur:/chemin/vers/destination/
```

Ici, `utilisateur` est votre nom d'utilisateur sur le serveur distant et `serveur` est l'adresse IP ou le nom de domaine du serveur.

## Tips
- Utilisez l'option `--dry-run` pour simuler une synchronisation sans effectuer de modifications. Cela vous permet de voir ce qui serait transféré.
- Pensez à utiliser `rsync` avec `cron` pour automatiser les sauvegardes régulières.
- Vérifiez toujours les permissions des fichiers et répertoires après une synchronisation pour vous assurer qu'elles sont correctes.
- Pour des transferts sécurisés, combinez `rsync` avec `ssh` pour chiffrer vos données en transit.