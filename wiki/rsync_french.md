# [Linux] Bash rsync Utilisation : Synchroniser des fichiers et des répertoires

## Overview
La commande `rsync` est un outil puissant utilisé pour synchroniser des fichiers et des répertoires entre différents emplacements, que ce soit sur le même système ou entre des systèmes distants. Elle est particulièrement appréciée pour sa rapidité et son efficacité, car elle ne transfère que les différences entre les fichiers source et destination.

## Usage
La syntaxe de base de la commande `rsync` est la suivante :

```bash
rsync [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `rsync` :

- `-a` : Archive mode, qui préserve les permissions, les timestamps, et les liens symboliques.
- `-v` : Mode verbeux, pour afficher les fichiers en cours de transfert.
- `-z` : Compression des fichiers pendant le transfert pour économiser de la bande passante.
- `-r` : Récursif, pour copier des répertoires et leur contenu.
- `--delete` : Supprime les fichiers dans la destination qui ne sont pas présents dans la source.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `rsync` :

1. **Synchroniser un répertoire local avec un autre répertoire local :**

```bash
rsync -av /chemin/vers/source/ /chemin/vers/destination/
```

2. **Synchroniser un répertoire local avec un répertoire distant :**

```bash
rsync -av /chemin/vers/source/ utilisateur@serveur:/chemin/vers/destination/
```

3. **Synchroniser un répertoire distant avec un répertoire local :**

```bash
rsync -av utilisateur@serveur:/chemin/vers/source/ /chemin/vers/destination/
```

4. **Utiliser la compression pendant le transfert :**

```bash
rsync -avz /chemin/vers/source/ utilisateur@serveur:/chemin/vers/destination/
```

5. **Supprimer les fichiers dans la destination qui ne sont pas dans la source :**

```bash
rsync -av --delete /chemin/vers/source/ /chemin/vers/destination/
```

## Tips
- Toujours utiliser l'option `-n` (ou `--dry-run`) pour simuler le transfert avant de l'exécuter réellement. Cela permet de voir ce qui sera transféré sans effectuer de modifications.
- Faites attention à l'utilisation de la barre oblique (`/`) à la fin des chemins, car cela affecte le comportement de la synchronisation.
- Pour des transferts fréquents, envisagez d'utiliser des scripts pour automatiser le processus avec `cron` ou d'autres planificateurs de tâches.