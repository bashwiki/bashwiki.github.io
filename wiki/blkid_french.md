# [Linux] Bash blkid : Identifier les systèmes de fichiers

## Overview
La commande `blkid` est utilisée pour afficher les informations sur les périphériques de blocs, notamment les systèmes de fichiers et les UUID (Identifiants Universels Uniques) associés. Elle est particulièrement utile pour identifier les partitions et les disques sur un système Linux.

## Usage
La syntaxe de base de la commande `blkid` est la suivante :

```bash
blkid [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `blkid` :

- `-o` : Spécifie le format de sortie (par exemple, `value`, `full`, `list`).
- `-s` : Sélectionne les attributs spécifiques à afficher (par exemple, `UUID`, `TYPE`).
- `-p` : Ignore la recherche des périphériques non montés.
- `-c` : Spécifie un fichier de cache pour améliorer les performances.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `blkid` :

1. **Afficher toutes les informations sur les périphériques de blocs :**

   ```bash
   blkid
   ```

2. **Afficher uniquement les UUID des systèmes de fichiers :**

   ```bash
   blkid -s UUID
   ```

3. **Afficher les informations au format "value" :**

   ```bash
   blkid -o value
   ```

4. **Afficher les informations d'un périphérique spécifique :**

   ```bash
   blkid /dev/sda1
   ```

5. **Utiliser un fichier de cache pour améliorer les performances :**

   ```bash
   blkid -c /path/to/cachefile
   ```

## Tips
- Utilisez `blkid` avec `sudo` si vous ne voyez pas tous les périphériques, car certains peuvent nécessiter des privilèges élevés pour être accessibles.
- Pour une sortie plus lisible, combinez `blkid` avec `grep` pour filtrer les résultats selon vos besoins.
- Pensez à consulter la page de manuel (`man blkid`) pour découvrir toutes les options disponibles et des exemples supplémentaires.