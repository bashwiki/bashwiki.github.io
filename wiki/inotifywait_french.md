# [리눅스] Bash inotifywait 사용법

## Overview
La commande `inotifywait` est un outil puissant dans l'environnement Linux qui permet de surveiller les modifications apportées à des fichiers ou des répertoires en temps réel. Son principal objectif est de fournir une notification instantanée lorsque des événements spécifiques se produisent, tels que la création, la modification ou la suppression de fichiers. Cela en fait un outil essentiel pour les développeurs et les ingénieurs qui souhaitent automatiser des tâches en fonction des changements dans le système de fichiers.

## Usage
La syntaxe de base de la commande `inotifywait` est la suivante :

```bash
inotifywait [options] [fichiers ou répertoires]
```

### Options courantes :
- `-m` : Mode de surveillance continue. Permet à `inotifywait` de rester actif et de surveiller les événements indéfiniment.
- `-e` : Spécifie les événements à surveiller. Par exemple, `modify`, `create`, `delete`, etc.
- `-r` : Surveille récursivement les répertoires.
- `-q` : Mode silencieux. N'affiche que les événements sans les messages d'information supplémentaires.

## Examples
Voici quelques exemples pratiques de l'utilisation de `inotifywait`.

### Exemple 1 : Surveiller un répertoire pour des modifications
Pour surveiller un répertoire nommé `mon_dossier` et afficher les événements de modification, vous pouvez utiliser la commande suivante :

```bash
inotifywait -m -e modify mon_dossier
```

Cette commande affichera chaque fois qu'un fichier dans `mon_dossier` est modifié.

### Exemple 2 : Surveiller un répertoire de manière récursive
Si vous souhaitez surveiller tous les fichiers dans un répertoire et ses sous-répertoires pour des créations de fichiers, utilisez :

```bash
inotifywait -m -r -e create mon_dossier
```

Cela affichera une notification chaque fois qu'un nouveau fichier est créé dans `mon_dossier` ou dans l'un de ses sous-répertoires.

## Tips
- **Utiliser des scripts** : Combinez `inotifywait` avec des scripts shell pour automatiser des tâches. Par exemple, vous pouvez déclencher un script de sauvegarde chaque fois qu'un fichier est modifié.
- **Limiter les événements** : Pour éviter une surcharge d'informations, limitez les événements que vous surveillez en utilisant l'option `-e` pour spécifier uniquement ceux qui vous intéressent.
- **Surveillance de plusieurs répertoires** : Vous pouvez surveiller plusieurs répertoires en les listant dans la commande, ce qui vous permet de centraliser la surveillance des événements.

En utilisant `inotifywait`, vous pouvez rendre votre environnement de développement plus réactif et automatisé, facilitant ainsi la gestion des fichiers et des répertoires.