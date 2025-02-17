# [Linux] Bash free : Afficher l'utilisation de la mémoire

## Overview
La commande `free` est utilisée pour afficher la quantité de mémoire libre et utilisée sur un système Linux. Elle fournit des informations sur la mémoire physique, la mémoire d'échange et les buffers utilisés par le noyau.

## Usage
La syntaxe de base de la commande `free` est la suivante :

```bash
free [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `free` :

- `-h` : Affiche les valeurs en format lisible par l'homme (Ko, Mo, Go).
- `-m` : Affiche la mémoire en mégaoctets.
- `-g` : Affiche la mémoire en gigaoctets.
- `-s <seconds>` : Met à jour l'affichage toutes les `<seconds>` secondes.
- `-t` : Affiche un total de la mémoire utilisée et libre.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `free` :

1. Afficher l'utilisation de la mémoire en format lisible par l'homme :

   ```bash
   free -h
   ```

2. Afficher la mémoire en mégaoctets :

   ```bash
   free -m
   ```

3. Afficher la mémoire en gigaoctets :

   ```bash
   free -g
   ```

4. Mettre à jour l'affichage toutes les 5 secondes :

   ```bash
   free -s 5
   ```

5. Afficher un total de la mémoire :

   ```bash
   free -t -h
   ```

## Tips
- Utilisez l'option `-h` pour faciliter la lecture des résultats, surtout sur les systèmes avec beaucoup de mémoire.
- Combinez `free` avec d'autres commandes comme `watch` pour surveiller l'utilisation de la mémoire en temps réel :

  ```bash
  watch free -h
  ```

- Pensez à utiliser `vmstat` pour obtenir des informations plus détaillées sur la mémoire et d'autres ressources système.