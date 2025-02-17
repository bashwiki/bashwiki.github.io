# [Linux] Bash shutdown utilisation : Arrêter ou redémarrer le système

## Overview
La commande `shutdown` est utilisée pour arrêter ou redémarrer un système Linux de manière contrôlée. Elle permet aux utilisateurs d'éteindre ou de redémarrer leur machine, en informant les utilisateurs connectés et en fermant les services en cours.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
shutdown [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `shutdown` :

- `-h` : Arrête le système.
- `-r` : Redémarre le système.
- `-t` : Définit le délai avant l'arrêt (en secondes).
- `now` : Indique que l'arrêt doit se faire immédiatement.
- `+m` : Indique que l'arrêt doit se faire après `m` minutes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `shutdown` :

- Pour arrêter le système immédiatement :

```bash
shutdown -h now
```

- Pour redémarrer le système après 5 minutes :

```bash
shutdown -r +5
```

- Pour arrêter le système à une heure précise (par exemple, 22h30) :

```bash
shutdown -h 22:30
```

- Pour annuler un arrêt programmé :

```bash
shutdown -c
```

## Tips
- Assurez-vous d'informer les utilisateurs connectés avant d'arrêter ou de redémarrer le système pour éviter toute perte de données.
- Utilisez l'option `-t` pour donner un délai suffisant aux services et utilisateurs pour se préparer à l'arrêt.
- Pensez à vérifier les processus en cours avant d'arrêter le système afin de ne pas interrompre des tâches importantes.