# [Linux] Bash htop Utilisation : Affichage interactif des processus système

## Overview
La commande `htop` est un outil interactif de surveillance des processus sous Linux. Contrairement à la commande `top`, `htop` offre une interface utilisateur plus conviviale, permettant de visualiser en temps réel l'utilisation des ressources système, tels que le CPU, la mémoire et les processus en cours d'exécution.

## Usage
La syntaxe de base de la commande `htop` est la suivante :

```bash
htop [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `htop` :

- `-d, --delay <seconds>` : Définit le délai d'actualisation en secondes.
- `-p, --pid <pid>` : Affiche uniquement les processus avec l'ID spécifié.
- `-s, --sort-key <key>` : Définit la clé de tri pour l'affichage des processus (par exemple, `PERCENT_CPU` ou `MEMORY`).
- `-u, --user <user>` : Affiche uniquement les processus appartenant à l'utilisateur spécifié.

## Common Examples
Voici quelques exemples pratiques d'utilisation de `htop` :

1. **Lancer htop sans options** :
   ```bash
   htop
   ```

2. **Afficher les processus d'un utilisateur spécifique** :
   ```bash
   htop -u nom_utilisateur
   ```

3. **Définir un délai d'actualisation de 2 secondes** :
   ```bash
   htop -d 2
   ```

4. **Afficher uniquement un processus spécifique par son PID** :
   ```bash
   htop -p 1234
   ```

5. **Trier les processus par utilisation du CPU** :
   ```bash
   htop -s PERCENT_CPU
   ```

## Tips
- Utilisez les touches de fonction (F1 à F10) pour accéder à diverses fonctionnalités, comme l'aide ou le tri des processus.
- Vous pouvez tuer un processus directement depuis l'interface de `htop` en sélectionnant le processus et en appuyant sur `F9`.
- Personnalisez l'affichage en utilisant les options de configuration accessibles via `F2` pour adapter `htop` à vos besoins spécifiques.