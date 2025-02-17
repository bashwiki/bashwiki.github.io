# [Linux] Bash lsusb Utilisation : Afficher les périphériques USB connectés

## Overview
La commande `lsusb` est utilisée pour afficher des informations sur les périphériques USB connectés à votre système. Elle permet de lister tous les périphériques USB, d'afficher leurs identifiants et d'obtenir des détails supplémentaires sur chacun d'eux.

## Usage
La syntaxe de base de la commande `lsusb` est la suivante :

```bash
lsusb [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `lsusb` :

- `-v` : Affiche des informations détaillées sur chaque périphérique.
- `-t` : Affiche la topologie des périphériques USB sous forme d'arborescence.
- `-s <bus>:<device>` : Affiche uniquement le périphérique spécifié par son bus et son numéro de périphérique.
- `-d <vendor>:<product>` : Affiche uniquement les périphériques correspondant à l'identifiant du vendeur et du produit.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `lsusb` :

1. **Lister tous les périphériques USB :**
   ```bash
   lsusb
   ```

2. **Afficher des informations détaillées sur tous les périphériques :**
   ```bash
   lsusb -v
   ```

3. **Afficher la topologie des périphériques USB :**
   ```bash
   lsusb -t
   ```

4. **Afficher un périphérique spécifique en utilisant son bus et son numéro :**
   ```bash
   lsusb -s 001:002
   ```

5. **Afficher un périphérique spécifique en utilisant l'identifiant du vendeur et du produit :**
   ```bash
   lsusb -d 1234:5678
   ```

## Tips
- Utilisez `lsusb -v` avec précaution, car cela peut générer beaucoup d'informations, surtout si vous avez de nombreux périphériques connectés.
- Combinez `lsusb` avec d'autres commandes comme `grep` pour filtrer les résultats et trouver rapidement un périphérique spécifique.
- Pensez à exécuter `lsusb` avec des privilèges administratifs si vous avez besoin d'accéder à des informations plus sensibles sur les périphériques.