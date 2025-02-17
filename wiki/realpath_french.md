# [Linux] Bash realpath utilisation : Résoudre les chemins de fichiers

## Overview
La commande `realpath` est utilisée pour résoudre les chemins de fichiers en renvoyant le chemin absolu d'un fichier ou d'un répertoire. Elle normalise également le chemin, en éliminant les références aux répertoires parents (`..`) et en suivant les liens symboliques.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
realpath [options] [arguments]
```

## Common Options
- `-m`, `--canonicalize-missing` : Renvoie le chemin canonique d'un fichier manquant, en créant les répertoires nécessaires.
- `-s`, `--strip` : Supprime les parties du chemin qui ne sont pas nécessaires pour atteindre le fichier.
- `-z`, `--zero` : Termine chaque sortie par un caractère nul au lieu d'un saut de ligne.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `realpath` :

1. **Obtenir le chemin absolu d'un fichier :**
   ```bash
   realpath mon_fichier.txt
   ```

2. **Résoudre un chemin avec des répertoires parents :**
   ```bash
   realpath ../mon_dossier/mon_fichier.txt
   ```

3. **Utiliser l'option pour un fichier manquant :**
   ```bash
   realpath -m mon_fichier_inexistant.txt
   ```

4. **Afficher le chemin d'un lien symbolique :**
   ```bash
   realpath mon_lien_symbolique
   ```

5. **Utiliser l'option pour supprimer les parties inutiles :**
   ```bash
   realpath -s /chemin/vers/../mon_fichier.txt
   ```

## Tips
- Utilisez `realpath` pour vérifier les chemins de fichiers avant de les utiliser dans des scripts afin d'éviter les erreurs de chemin.
- Combinez `realpath` avec d'autres commandes comme `find` pour obtenir des chemins absolus de fichiers trouvés.
- Pensez à utiliser l'option `-m` lorsque vous travaillez avec des fichiers qui peuvent ne pas exister, pour éviter des erreurs dans vos scripts.