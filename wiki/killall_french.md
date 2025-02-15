# [리눅스] Bash killall 사용법

## Overview
La commande `killall` est utilisée dans les systèmes Unix et Linux pour terminer des processus en cours d'exécution en fonction de leur nom. Contrairement à la commande `kill`, qui nécessite un identifiant de processus (PID), `killall` permet de cibler tous les processus portant un nom spécifique, ce qui en fait un outil pratique pour gérer plusieurs instances d'un programme.

## Usage
La syntaxe de base de la commande `killall` est la suivante :

```bash
killall [options] nom_du_processus
```

### Options courantes :
- `-u utilisateur` : Terminer uniquement les processus appartenant à un utilisateur spécifique.
- `-i` : Demander une confirmation avant de tuer chaque processus.
- `-q` : Mode silencieux, ne pas afficher de messages d'erreur.
- `-s signal` : Spécifier le signal à envoyer (par défaut, c'est `TERM`).

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `killall` :

1. Pour terminer tous les processus nommés `firefox` :

   ```bash
   killall firefox
   ```

2. Pour forcer la fermeture de tous les processus `gedit` en envoyant le signal `KILL` :

   ```bash
   killall -s KILL gedit
   ```

## Tips
- Utilisez l'option `-i` pour éviter de terminer accidentellement des processus importants. Cela vous demandera une confirmation avant de procéder.
- Soyez prudent lorsque vous utilisez `killall` avec des noms de processus génériques, car cela peut affecter plusieurs instances de programmes similaires.
- Pour vérifier quels processus seront affectés avant d'utiliser `killall`, vous pouvez utiliser la commande `pgrep` avec le même nom de processus :

   ```bash
   pgrep firefox
   ```

En suivant ces conseils, vous pourrez utiliser `killall` de manière efficace et sécurisée dans vos tâches de gestion des processus.