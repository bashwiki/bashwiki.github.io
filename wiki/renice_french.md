# [Linux] Bash renice : Ajuster la priorité des processus

## Overview
La commande `renice` permet de modifier la priorité d'exécution des processus en cours sur un système Linux. En ajustant la priorité, vous pouvez influencer la manière dont le système alloue les ressources CPU aux différents processus.

## Usage
La syntaxe de base de la commande `renice` est la suivante :

```bash
renice [options] [arguments]
```

## Common Options
- `-n`, `--priority` : Définit la nouvelle priorité. Les valeurs peuvent aller de -20 (priorité maximale) à 19 (priorité minimale).
- `-p`, `--pid` : Spécifie l'identifiant du processus (PID) dont vous souhaitez modifier la priorité.
- `-g`, `--pgrp` : Modifie la priorité de tous les processus d'un groupe de processus spécifié.
- `-u`, `--user` : Modifie la priorité de tous les processus d'un utilisateur spécifié.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `renice` :

1. **Modifier la priorité d'un processus par son PID :**
   ```bash
   renice -n 10 -p 1234
   ```
   Cela change la priorité du processus avec le PID 1234 à 10.

2. **Modifier la priorité de tous les processus d'un utilisateur :**
   ```bash
   renice -n 5 -u username
   ```
   Ici, tous les processus appartenant à l'utilisateur `username` auront leur priorité modifiée à 5.

3. **Modifier la priorité d'un groupe de processus :**
   ```bash
   renice -n -5 -g 5678
   ```
   Cela ajuste la priorité de tous les processus dans le groupe de processus avec l'ID 5678 à -5.

## Tips
- Utilisez `renice` avec prudence, car une priorité trop élevée pour un processus peut nuire aux performances globales du système.
- Pour vérifier les priorités des processus en cours, vous pouvez utiliser la commande `ps -eo pid,ni,comm` qui affiche le PID, la priorité (nice value) et le nom du processus.
- N'oubliez pas que seuls les utilisateurs ayant les droits appropriés peuvent augmenter la priorité d'un processus (c'est-à-dire donner une valeur `nice` négative).