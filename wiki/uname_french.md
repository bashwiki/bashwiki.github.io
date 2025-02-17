# [Linux] Bash uname utilisation : Afficher les informations du système

## Overview
La commande `uname` est utilisée pour afficher des informations sur le système d'exploitation et le matériel sur lequel vous travaillez. Elle peut fournir des détails tels que le nom du noyau, la version et le type de machine.

## Usage
La syntaxe de base de la commande `uname` est la suivante :

```bash
uname [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `uname` :

- `-a` : Affiche toutes les informations disponibles sur le système.
- `-s` : Affiche le nom du noyau.
- `-n` : Affiche le nom de l'hôte du système.
- `-r` : Affiche la version du noyau.
- `-v` : Affiche des informations supplémentaires sur la version du noyau.
- `-m` : Affiche le type de machine.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `uname` :

1. Afficher toutes les informations du système :
   ```bash
   uname -a
   ```

2. Afficher uniquement le nom du noyau :
   ```bash
   uname -s
   ```

3. Afficher le nom de l'hôte :
   ```bash
   uname -n
   ```

4. Afficher la version du noyau :
   ```bash
   uname -r
   ```

5. Afficher le type de machine :
   ```bash
   uname -m
   ```

## Tips
- Utilisez `uname -a` pour obtenir un aperçu complet de votre système en une seule commande.
- Combinez `uname` avec d'autres commandes comme `grep` pour filtrer les informations spécifiques que vous recherchez.
- Pensez à utiliser `man uname` pour consulter le manuel et découvrir d'autres options disponibles.