# [Linux] Bash basename utilisation : Extraire le nom de fichier d'un chemin

## Overview
La commande `basename` est utilisée pour extraire le nom de fichier d'un chemin donné, en supprimant le répertoire et, si nécessaire, l'extension du fichier. Cela permet de travailler facilement avec des noms de fichiers sans avoir à gérer les chemins complets.

## Usage
La syntaxe de base de la commande `basename` est la suivante :

```bash
basename [options] [arguments]
```

## Common Options
- `-a` : Traite plusieurs arguments et renvoie le nom de base pour chacun.
- `-s` : Supprime une extension spécifique du nom de fichier.
- `--help` : Affiche l'aide sur la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `basename` :

1. **Extraire le nom de fichier d'un chemin :**
   ```bash
   basename /chemin/vers/fichier.txt
   ```
   Sortie :
   ```
   fichier.txt
   ```

2. **Extraire le nom de fichier sans l'extension :**
   ```bash
   basename /chemin/vers/fichier.txt .txt
   ```
   Sortie :
   ```
   fichier
   ```

3. **Traiter plusieurs fichiers :**
   ```bash
   basename -a /chemin/vers/fichier1.txt /chemin/vers/fichier2.txt
   ```
   Sortie :
   ```
   fichier1.txt
   fichier2.txt
   ```

4. **Utiliser avec une extension personnalisée :**
   ```bash
   basename /chemin/vers/fichier.log .log
   ```
   Sortie :
   ```
   fichier
   ```

## Tips
- Utilisez `basename` dans des scripts pour simplifier la gestion des fichiers.
- Combinez `basename` avec d'autres commandes comme `find` pour traiter des fichiers de manière plus efficace.
- Pensez à utiliser l'option `-s` pour retirer des extensions spécifiques lorsque vous traitez des fichiers avec des noms similaires.