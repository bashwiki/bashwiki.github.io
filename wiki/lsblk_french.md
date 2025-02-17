# [Linux] Bash lsblk Utilisation : Afficher les périphériques de bloc

## Overview
La commande `lsblk` est utilisée pour afficher des informations sur les périphériques de bloc disponibles sur un système Linux. Elle fournit une vue hiérarchique des disques, partitions et autres périphériques de stockage, ce qui est utile pour la gestion des disques.

## Usage
La syntaxe de base de la commande `lsblk` est la suivante :

```bash
lsblk [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `lsblk` :

- `-a` : Affiche tous les périphériques, y compris ceux qui ne sont pas montés.
- `-f` : Affiche les informations sur le système de fichiers.
- `-l` : Affiche la sortie sous forme de liste, plutôt que de l'arborescence par défaut.
- `-o` : Permet de spécifier les colonnes à afficher.
- `-p` : Affiche les chemins complets des périphériques.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `lsblk` :

1. **Afficher tous les périphériques de bloc :**
   ```bash
   lsblk
   ```

2. **Afficher tous les périphériques, y compris ceux non montés :**
   ```bash
   lsblk -a
   ```

3. **Afficher les informations sur le système de fichiers :**
   ```bash
   lsblk -f
   ```

4. **Afficher la sortie sous forme de liste :**
   ```bash
   lsblk -l
   ```

5. **Afficher des colonnes spécifiques (par exemple, NAME, SIZE, TYPE) :**
   ```bash
   lsblk -o NAME,SIZE,TYPE
   ```

## Tips
- Utilisez `lsblk` avec l'option `-f` pour obtenir des informations détaillées sur le système de fichiers, ce qui peut être utile pour le dépannage.
- Combinez `lsblk` avec d'autres commandes comme `grep` pour filtrer les résultats selon vos besoins.
- Pour une vue plus détaillée, envisagez d'utiliser `lsblk` avec l'option `-p` pour obtenir les chemins complets des périphériques.