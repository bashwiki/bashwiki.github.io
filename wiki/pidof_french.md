# [Linux] Bash pidof : [trouver les identifiants de processus]

## Overview
La commande `pidof` est utilisée pour trouver les identifiants de processus (PID) d'un programme en cours d'exécution. Elle renvoie le ou les PID associés à un nom de programme spécifié, ce qui est utile pour gérer les processus sur un système Linux.

## Usage
La syntaxe de base de la commande `pidof` est la suivante :

```bash
pidof [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `pidof` :

- `-o` : Exclut les PID spécifiés de la sortie.
- `-s` : Affiche uniquement le premier PID trouvé.
- `-c` : Affiche le nombre de processus trouvés.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `pidof` :

1. **Trouver le PID d'un programme spécifique :**
   ```bash
   pidof firefox
   ```

2. **Exclure un PID de la sortie :**
   ```bash
   pidof -o 1234 firefox
   ```

3. **Afficher uniquement le premier PID trouvé :**
   ```bash
   pidof -s firefox
   ```

4. **Compter le nombre de processus d'un programme :**
   ```bash
   pidof -c firefox
   ```

## Tips
- Utilisez `pidof` avec des scripts pour automatiser la gestion des processus.
- Combinez `pidof` avec d'autres commandes comme `kill` pour terminer des processus spécifiques.
- Vérifiez toujours que le programme est en cours d'exécution avant d'utiliser `pidof`, sinon vous ne recevrez aucun résultat.