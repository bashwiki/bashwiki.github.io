# [리눅스] Bash pwd 사용법

## Overview
La commande `pwd` (print working directory) est utilisée dans les systèmes Unix et Linux pour afficher le chemin absolu du répertoire de travail actuel. Son principal objectif est d'informer l'utilisateur de l'emplacement exact dans le système de fichiers où il se trouve à un moment donné. Cela est particulièrement utile lors de la navigation dans des répertoires ou lors de l'exécution de scripts.

## Usage
La syntaxe de base de la commande `pwd` est la suivante :

```bash
pwd [options]
```

### Options courantes
- `-L` : Affiche le chemin logique du répertoire de travail actuel. C'est l'option par défaut.
- `-P` : Affiche le chemin physique, en résolvant tous les liens symboliques. Cela peut être utile pour obtenir le chemin réel sur le système de fichiers.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `pwd`.

### Exemple 1 : Afficher le répertoire de travail actuel
```bash
$ pwd
/home/utilisateur/projet
```
Dans cet exemple, la commande `pwd` affiche le chemin absolu du répertoire de travail actuel, qui est `/home/utilisateur/projet`.

### Exemple 2 : Afficher le chemin physique
```bash
$ cd /home/utilisateur/projet/symlink
$ pwd -P
/home/utilisateur/projet/réel
```
Dans cet exemple, après avoir changé de répertoire vers un lien symbolique, l'utilisation de `pwd -P` affiche le chemin réel, résolvant ainsi le lien symbolique.

## Tips
- Utilisez `pwd` régulièrement pour vous assurer que vous êtes dans le bon répertoire avant d'exécuter des commandes qui pourraient affecter des fichiers ou des répertoires.
- Combinez `pwd` avec d'autres commandes comme `cd` pour naviguer efficacement dans le système de fichiers.
- Si vous travaillez avec des scripts, envisagez d'utiliser `pwd` pour capturer le chemin actuel et l'utiliser dans des opérations de fichiers.