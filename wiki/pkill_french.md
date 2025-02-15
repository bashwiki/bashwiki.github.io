# [리눅스] Bash pkill 사용법

## Overview
La commande `pkill` est utilisée dans les systèmes Unix et Linux pour envoyer des signaux à des processus en fonction de leur nom ou d'autres attributs. Son objectif principal est de permettre aux utilisateurs de terminer ou de manipuler des processus en spécifiant simplement le nom du processus, sans avoir à rechercher son identifiant de processus (PID). Cela en fait un outil pratique pour la gestion des processus.

## Usage
La syntaxe de base de la commande `pkill` est la suivante :

```bash
pkill [options] nom_du_processus
```

### Options courantes :
- `-9` : Force l'arrêt du processus en envoyant le signal SIGKILL.
- `-f` : Correspond à l'ensemble de la ligne de commande du processus, pas seulement au nom.
- `-u` : Filtre les processus par utilisateur.
- `-l` : Affiche la liste des signaux disponibles.
- `-n` : Ne tue que le dernier processus correspondant.
- `-o` : Ne tue que le premier processus correspondant.

## Examples
### Exemple 1 : Terminer un processus par son nom
Pour terminer tous les processus appelés `firefox`, vous pouvez utiliser la commande suivante :

```bash
pkill firefox
```

### Exemple 2 : Forcer l'arrêt d'un processus
Si vous souhaitez forcer l'arrêt de tous les processus `chrome`, vous pouvez utiliser le signal SIGKILL comme suit :

```bash
pkill -9 chrome
```

## Tips
- Utilisez l'option `-u` pour cibler les processus d'un utilisateur spécifique, ce qui peut être utile dans un environnement multi-utilisateur.
- Avant de tuer des processus, il peut être judicieux d'utiliser `pgrep` pour vérifier quels processus seront affectés par votre commande `pkill`.
- Soyez prudent avec l'utilisation de `pkill` et surtout avec l'option `-9`, car cela ne permet pas aux processus de se fermer proprement, ce qui peut entraîner une perte de données.