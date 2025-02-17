# [Linux] Bash w : Afficher les utilisateurs connectés

## Overview
La commande `w` est utilisée pour afficher les utilisateurs actuellement connectés au système ainsi que leurs activités. Elle fournit des informations sur l'heure de connexion, le temps d'inactivité, et les commandes en cours d'exécution.

## Usage
La syntaxe de base de la commande `w` est la suivante :

```bash
w [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `w` :

- `-h` : Supprime l'en-tête de la sortie.
- `-s` : Affiche une sortie plus concise, sans les colonnes supplémentaires.
- `-u` : Affiche le nom d'utilisateur au lieu de l'identifiant utilisateur (UID).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `w` :

1. Afficher tous les utilisateurs connectés :
   ```bash
   w
   ```

2. Afficher la sortie sans l'en-tête :
   ```bash
   w -h
   ```

3. Afficher une sortie concise :
   ```bash
   w -s
   ```

4. Afficher les utilisateurs avec leurs noms d'utilisateur :
   ```bash
   w -u
   ```

## Tips
- Utilisez `w` régulièrement pour surveiller l'activité des utilisateurs sur votre système.
- Combinez `w` avec d'autres commandes comme `grep` pour filtrer les résultats selon vos besoins.
- Pensez à utiliser l'option `-s` si vous souhaitez une vue simplifiée, surtout sur des systèmes avec de nombreux utilisateurs connectés.