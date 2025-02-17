# [Linux] Bash killall Utilisation : Terminer tous les processus d'un nom donné

## Overview
La commande `killall` est utilisée pour terminer tous les processus qui correspondent à un nom donné. Cela permet de gérer facilement les applications ou les processus qui ne répondent plus ou qui consomment trop de ressources.

## Usage
La syntaxe de base de la commande `killall` est la suivante :

```bash
killall [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `killall` :

- `-u <utilisateur>` : Terminer uniquement les processus appartenant à un utilisateur spécifique.
- `-i` : Demander une confirmation avant de terminer chaque processus.
- `-q` : Ne pas afficher de messages d'erreur pour les processus qui ne sont pas trouvés.
- `-s <signal>` : Spécifier un signal à envoyer aux processus (par défaut, c'est le signal TERM).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `killall` :

- Terminer tous les processus appelés `firefox` :

```bash
killall firefox
```

- Terminer tous les processus de l'utilisateur `john` :

```bash
killall -u john
```

- Terminer tous les processus `gedit` en demandant une confirmation :

```bash
killall -i gedit
```

- Envoyer un signal spécifique (par exemple, SIGKILL) à tous les processus `myapp` :

```bash
killall -s SIGKILL myapp
```

## Tips
- Utilisez l'option `-i` pour éviter de terminer accidentellement des processus importants.
- Avant d'utiliser `killall`, vérifiez les processus en cours avec `ps` ou `top` pour éviter de fermer des applications essentielles.
- Soyez prudent avec l'utilisation de `killall` sur des processus critiques du système, car cela peut entraîner une instabilité.