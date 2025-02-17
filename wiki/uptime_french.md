# [Linux] Bash uptime : Affiche le temps de fonctionnement du système

## Overview
La commande `uptime` permet d'afficher depuis combien de temps le système fonctionne, ainsi que le nombre d'utilisateurs connectés et la charge moyenne du système sur les 1, 5 et 15 dernières minutes. C'est un outil utile pour surveiller la santé et la performance d'un serveur ou d'une machine.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
uptime [options]
```

## Common Options
Voici quelques options courantes pour la commande `uptime` :

- `-p` : Affiche le temps de fonctionnement sous une forme lisible.
- `-s` : Affiche l'heure à laquelle le système a démarré.

## Common Examples

### Exemple 1 : Afficher le temps de fonctionnement
Pour afficher le temps de fonctionnement du système, utilisez simplement :

```bash
uptime
```

### Exemple 2 : Afficher le temps de fonctionnement de manière lisible
Pour obtenir une sortie plus lisible, utilisez l'option `-p` :

```bash
uptime -p
```

### Exemple 3 : Afficher l'heure de démarrage du système
Pour voir à quelle heure le système a démarré, utilisez l'option `-s` :

```bash
uptime -s
```

## Tips
- Utilisez `uptime` régulièrement pour surveiller la performance de votre système, surtout sur des serveurs critiques.
- Combinez `uptime` avec d'autres commandes comme `top` ou `htop` pour obtenir une vue d'ensemble de l'état de votre système.
- Pensez à automatiser la vérification de l'uptime dans des scripts de surveillance pour être alerté en cas de redémarrage inattendu.