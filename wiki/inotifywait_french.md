# [Linux] Bash inotifywait : Surveille les modifications de fichiers

## Overview
La commande `inotifywait` est un outil puissant qui permet de surveiller les modifications apportées aux fichiers et répertoires sous Linux. Il utilise l'interface inotify du noyau Linux pour détecter les événements tels que les créations, les suppressions, et les modifications de fichiers.

## Usage
La syntaxe de base de la commande `inotifywait` est la suivante :

```bash
inotifywait [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `inotifywait` :

- `-m` : Mode de surveillance continue. Permet de surveiller les événements indéfiniment.
- `-r` : Surveille récursivement les répertoires.
- `-e` : Spécifie les événements à surveiller (par exemple, `modify`, `create`, `delete`).
- `--format` : Permet de personnaliser la sortie des événements.
- `-q` : Mode silencieux, n'affiche que les événements sans messages d'information.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `inotifywait` :

### Surveiller un répertoire pour les modifications
```bash
inotifywait -m /chemin/vers/répertoire
```

### Surveiller un fichier spécifique pour les modifications
```bash
inotifywait -m -e modify /chemin/vers/fichier.txt
```

### Surveiller un répertoire et ses sous-répertoires
```bash
inotifywait -mr -e create,delete /chemin/vers/répertoire
```

### Utiliser un format personnalisé pour la sortie
```bash
inotifywait -m --format '%w%f %e' -e modify /chemin/vers/répertoire
```

## Tips
- Utilisez l'option `-m` pour surveiller les événements en continu, ce qui est utile pour des scripts de surveillance.
- Combinez `inotifywait` avec d'autres commandes dans un script pour automatiser des tâches en réponse à des événements de fichiers.
- Pensez à rediriger la sortie vers un fichier log pour garder une trace des modifications surveillées.