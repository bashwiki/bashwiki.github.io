# [Linux] Bash xz : Compression de fichiers

## Overview
La commande `xz` est utilisée pour compresser et décompresser des fichiers en utilisant l'algorithme de compression LZMA. Elle est particulièrement efficace pour réduire la taille des fichiers tout en maintenant une bonne qualité de compression.

## Usage
La syntaxe de base de la commande `xz` est la suivante :

```bash
xz [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `xz` :

- `-d`, `--decompress` : Décompresse un fichier.
- `-k`, `--keep` : Garde le fichier d'origine après compression.
- `-f`, `--force` : Force la compression même si le fichier de sortie existe déjà.
- `-9` : Utilise le niveau de compression maximum (1 à 9, où 9 est le plus compressé).
- `-v`, `--verbose` : Affiche des informations détaillées sur le processus de compression.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `xz` :

1. **Compresser un fichier :**
   ```bash
   xz fichier.txt
   ```

2. **Décompresser un fichier :**
   ```bash
   xz -d fichier.txt.xz
   ```

3. **Compresser un fichier tout en gardant l'original :**
   ```bash
   xz -k fichier.txt
   ```

4. **Compresser avec le niveau de compression maximum :**
   ```bash
   xz -9 fichier.txt
   ```

5. **Afficher des informations détaillées lors de la compression :**
   ```bash
   xz -v fichier.txt
   ```

## Tips
- Pour une compression plus rapide, utilisez un niveau de compression plus bas (par exemple, `-1`).
- Si vous travaillez avec de nombreux fichiers, envisagez d'utiliser des outils comme `tar` en combinaison avec `xz` pour compresser des archives entières.
- Vérifiez toujours l'espace disque disponible avant de compresser de gros fichiers, surtout si vous ne conservez pas les originaux.