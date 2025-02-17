# [Linux] Bash top utilisation : Afficher les processus en temps réel

## Overview
La commande `top` est un outil puissant qui permet d'afficher en temps réel les processus en cours d'exécution sur un système Linux. Elle fournit des informations sur l'utilisation du processeur, de la mémoire et d'autres ressources système, ce qui en fait un outil essentiel pour le monitoring et le diagnostic des performances.

## Usage
La syntaxe de base de la commande `top` est la suivante :

```bash
top [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec la commande `top` :

- `-d <seconds>` : Définit le délai entre les mises à jour de l'affichage (en secondes).
- `-n <number>` : Spécifie le nombre de mises à jour à afficher avant de quitter.
- `-u <user>` : Filtre les processus pour n'afficher que ceux appartenant à l'utilisateur spécifié.
- `-p <pid>` : Affiche uniquement le processus avec l'identifiant de processus (PID) spécifié.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `top` :

1. **Lancer `top` avec les paramètres par défaut :**
   ```bash
   top
   ```

2. **Afficher les processus avec une mise à jour toutes les 2 secondes :**
   ```bash
   top -d 2
   ```

3. **Afficher les processus d'un utilisateur spécifique :**
   ```bash
   top -u username
   ```

4. **Afficher un processus spécifique par son PID :**
   ```bash
   top -p 1234
   ```

5. **Afficher `top` pour un nombre limité de mises à jour (par exemple, 5) :**
   ```bash
   top -n 5
   ```

## Tips
- Pour quitter l'interface de `top`, appuyez sur `q`.
- Vous pouvez trier les processus en appuyant sur les touches `P` (pour le CPU) ou `M` (pour la mémoire) pendant que `top` est en cours d'exécution.
- Utilisez la touche `h` pour afficher l'aide et connaître les commandes disponibles dans l'interface de `top`.