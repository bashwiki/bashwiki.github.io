# [Linux] Bash timeout utilisation : Limiter la durée d'exécution d'une commande

## Overview
La commande `timeout` permet d'exécuter une commande avec une limite de temps. Si la commande ne se termine pas dans le délai imparti, `timeout` l'arrête automatiquement. Cela est particulièrement utile pour éviter que des processus ne s'éternisent.

## Usage
La syntaxe de base de la commande `timeout` est la suivante :

```bash
timeout [options] [durée] [commande] [arguments]
```

## Common Options
- `-k, --kill-after=DURÉE` : Spécifie une durée après laquelle le processus sera tué, même s'il est toujours en cours d'exécution.
- `-s, --signal=SIGNAL` : Définit le signal à envoyer au processus lorsque le temps est écoulé (par défaut, c'est `TERM`).
- `--preserve-status` : Préserve le code de sortie de la commande exécutée.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `timeout` :

1. **Exécuter une commande avec un délai de 5 secondes :**
   ```bash
   timeout 5s sleep 10
   ```
   Dans cet exemple, `sleep 10` sera interrompu après 5 secondes.

2. **Utiliser un signal spécifique pour tuer le processus :**
   ```bash
   timeout -s KILL 3s sleep 10
   ```
   Ici, le processus `sleep` sera tué avec le signal `KILL` après 3 secondes.

3. **Préserver le code de sortie de la commande :**
   ```bash
   timeout --preserve-status 2s false
   echo $?
   ```
   Dans cet exemple, `false` échoue immédiatement, et le code de sortie sera préservé.

4. **Killer un processus après une durée prolongée :**
   ```bash
   timeout -k 2s 5s sleep 10
   ```
   Cela envoie un signal de terminaison après 5 secondes, et si le processus est toujours actif après 2 secondes supplémentaires, il sera tué.

## Tips
- Utilisez `timeout` pour les scripts automatisés afin d'éviter les blocages.
- Testez toujours vos commandes avec un délai plus court pour vous assurer qu'elles se comportent comme prévu.
- Pensez à utiliser `--preserve-status` si le code de sortie est important pour le traitement ultérieur.