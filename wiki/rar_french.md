# [Linux] Bash rar utilisation : Compresser et décompresser des fichiers

## Overview
La commande `rar` est utilisée pour créer et gérer des archives au format RAR. Elle permet de compresser des fichiers et des dossiers pour économiser de l'espace disque et faciliter le partage.

## Usage
La syntaxe de base de la commande `rar` est la suivante :

```bash
rar [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `rar` :

- `a` : Ajouter des fichiers à une archive.
- `x` : Extraire des fichiers d'une archive.
- `t` : Tester l'intégrité des fichiers dans une archive.
- `v` : Afficher des informations détaillées sur le processus.
- `m` : Définir le niveau de compression (0 à 5, où 0 est sans compression et 5 est la compression maximale).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `rar` :

1. **Créer une archive RAR :**
   ```bash
   rar a archive.rar fichier1.txt fichier2.txt
   ```

2. **Extraire une archive RAR :**
   ```bash
   rar x archive.rar
   ```

3. **Tester l'intégrité d'une archive RAR :**
   ```bash
   rar t archive.rar
   ```

4. **Ajouter un fichier à une archive existante :**
   ```bash
   rar a archive.rar fichier3.txt
   ```

5. **Créer une archive avec un niveau de compression spécifique :**
   ```bash
   rar a -m5 archive_compressed.rar dossier/
   ```

## Tips
- Utilisez `-v` pour obtenir des informations détaillées lors de la création ou de l'extraction d'archives.
- Pensez à vérifier l'intégrité de vos archives avec l'option `t` après leur création.
- Pour un meilleur contrôle, consultez la documentation officielle de `rar` en utilisant `man rar` dans le terminal.