# [Linux] Bash bzip2 utilisation : compresser et décompresser des fichiers

## Overview
La commande `bzip2` est utilisée pour compresser et décompresser des fichiers en utilisant l'algorithme de compression bzip2. Elle est particulièrement efficace pour réduire la taille des fichiers, ce qui facilite le stockage et le transfert.

## Usage
La syntaxe de base de la commande `bzip2` est la suivante :

```bash
bzip2 [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `bzip2` :

- `-d` : Décompresse un fichier.
- `-k` : Garde le fichier d'origine après compression.
- `-f` : Force la compression, même si le fichier de destination existe déjà.
- `-v` : Affiche des informations détaillées sur le processus de compression.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `bzip2` :

1. **Compresser un fichier :**
   ```bash
   bzip2 fichier.txt
   ```
   Cela crée un fichier compressé nommé `fichier.txt.bz2`.

2. **Décompresser un fichier :**
   ```bash
   bzip2 -d fichier.txt.bz2
   ```
   Cela restaure le fichier original `fichier.txt`.

3. **Compresser un fichier tout en gardant l'original :**
   ```bash
   bzip2 -k fichier.txt
   ```
   Le fichier compressé `fichier.txt.bz2` sera créé sans supprimer `fichier.txt`.

4. **Compresser plusieurs fichiers :**
   ```bash
   bzip2 fichier1.txt fichier2.txt
   ```
   Cela compressera `fichier1.txt` et `fichier2.txt` en `fichier1.txt.bz2` et `fichier2.txt.bz2`.

5. **Afficher des informations détaillées lors de la compression :**
   ```bash
   bzip2 -v fichier.txt
   ```
   Cela affichera des informations sur le processus de compression.

## Tips
- Utilisez l'option `-k` si vous souhaitez conserver le fichier original après compression.
- Pour des fichiers très volumineux, envisagez d'utiliser `pbzip2`, qui permet une compression parallèle et peut être plus rapide.
- Vérifiez toujours l'espace disque disponible avant de compresser de gros fichiers pour éviter les erreurs de manque d'espace.