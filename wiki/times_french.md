# [Linux] Bash times : Afficher l'utilisation du temps CPU

## Overview
La commande `times` en Bash est utilisée pour afficher le temps d'exécution des processus en cours dans le shell. Elle fournit des informations sur le temps CPU utilisé par le shell et ses processus fils, ce qui peut être utile pour le diagnostic des performances.

## Usage
La syntaxe de base de la commande `times` est la suivante :

```
times [options] [arguments]
```

## Common Options
La commande `times` n'a pas beaucoup d'options, mais voici quelques éléments à considérer :
- `-p` : Affiche le temps au format POSIX.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `times` :

1. **Afficher le temps d'exécution des processus en cours :**
   ```bash
   times
   ```

2. **Afficher le temps d'exécution au format POSIX :**
   ```bash
   times -p
   ```

3. **Utiliser `times` après l'exécution de plusieurs commandes :**
   ```bash
   sleep 2
   ls
   times
   ```

## Tips
- Utilisez `times` après l'exécution de plusieurs commandes pour obtenir une vue d'ensemble de l'utilisation du temps CPU.
- Combinez `times` avec d'autres commandes pour analyser l'impact des processus sur les performances de votre système.
- Notez que `times` ne fonctionne que dans le contexte d'un shell interactif et ne sera pas utile dans des scripts non interactifs.