# [Linux] Bash pkill Utilisation : Terminer des processus par nom

## Overview
La commande `pkill` est utilisée pour terminer des processus en fonction de leur nom ou d'autres attributs. Elle permet de gérer facilement les processus en cours d'exécution sans avoir à rechercher leur identifiant de processus (PID).

## Usage
La syntaxe de base de la commande `pkill` est la suivante :

```bash
pkill [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `pkill` :

- `-f` : Correspond à l'ensemble de la ligne de commande du processus.
- `-n` : Tuer le dernier processus correspondant au critère.
- `-o` : Tuer le premier processus correspondant au critère.
- `-signal` : Spécifier le signal à envoyer au processus (par défaut, c'est SIGTERM).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `pkill` :

1. Terminer tous les processus nommés `firefox` :
   ```bash
   pkill firefox
   ```

2. Terminer tous les processus contenant le mot `python` dans leur ligne de commande :
   ```bash
   pkill -f python
   ```

3. Terminer le dernier processus `nginx` lancé :
   ```bash
   pkill -n nginx
   ```

4. Envoyer un signal spécifique (comme SIGKILL) à tous les processus `ssh` :
   ```bash
   pkill -9 ssh
   ```

## Tips
- Utilisez `pkill -l` pour lister tous les signaux disponibles que vous pouvez envoyer.
- Soyez prudent lorsque vous utilisez `pkill` sans options, car cela peut terminer plusieurs processus si le nom est générique.
- Pour tester la commande sans tuer de processus, vous pouvez utiliser `pgrep`, qui affiche les processus correspondants sans les terminer.