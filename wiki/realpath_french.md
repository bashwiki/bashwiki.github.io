# [리눅스] Bash realpath 사용법

## Overview
La commande `realpath` est utilisée pour résoudre les chemins de fichiers et de répertoires en leurs chemins absolus. Elle prend en entrée un chemin relatif ou un chemin symbolique et renvoie le chemin complet qui correspond à l'emplacement réel sur le système de fichiers. Cela est particulièrement utile pour éviter les ambiguïtés liées aux chemins relatifs ou aux liens symboliques.

## Usage
La syntaxe de base de la commande `realpath` est la suivante :

```bash
realpath [options] <path>
```

### Options courantes
- `-m`, `--canonicalize-missing` : Cette option permet de renvoyer un chemin canonique même si le fichier ou le répertoire n'existe pas.
- `-q`, `--quiet` : Suppresse les messages d'erreur, ce qui peut être utile si vous ne souhaitez pas afficher d'erreurs pour les chemins non valides.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `realpath`.

### Exemple 1 : Résoudre un chemin relatif
```bash
$ realpath ./documents/projet
/home/utilisateur/documents/projet
```
Dans cet exemple, `realpath` convertit le chemin relatif `./documents/projet` en son chemin absolu.

### Exemple 2 : Résoudre un lien symbolique
```bash
$ ln -s /var/log/syslog symlink
$ realpath symlink
/var/log/syslog
```
Ici, nous avons d'abord créé un lien symbolique nommé `symlink` pointant vers `/var/log/syslog`. Ensuite, `realpath` résout ce lien symbolique en renvoyant le chemin réel.

## Tips
- Utilisez `realpath` pour vérifier les chemins avant de les utiliser dans des scripts, afin d'éviter les erreurs dues à des chemins incorrects.
- Combinez `realpath` avec d'autres commandes comme `cd` pour naviguer facilement vers des répertoires en utilisant des chemins absolus.
- Si vous travaillez avec des scripts qui manipulent des fichiers, il est judicieux d'utiliser `realpath` pour garantir que vous travaillez avec les chemins corrects, surtout lorsque des liens symboliques sont impliqués.