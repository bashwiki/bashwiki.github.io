# [Linux] Bash find utilisation : rechercher des fichiers

## Overview
La commande `find` est un outil puissant utilisé pour rechercher des fichiers et des répertoires dans une hiérarchie de fichiers. Elle permet de localiser des fichiers en fonction de divers critères tels que le nom, la taille, la date de modification, et bien plus encore.

## Usage
La syntaxe de base de la commande `find` est la suivante :

```bash
find [options] [arguments]
```

## Common Options
Voici quelques options courantes de la commande `find` :

- `-name <pattern>` : recherche des fichiers dont le nom correspond au motif spécifié.
- `-type <type>` : recherche des fichiers d'un type spécifique (par exemple, `f` pour fichiers, `d` pour répertoires).
- `-size <n>` : recherche des fichiers d'une taille spécifique (par exemple, `+100M` pour des fichiers de plus de 100 Mo).
- `-mtime <n>` : recherche des fichiers modifiés il y a `n` jours (par exemple, `-mtime -7` pour les fichiers modifiés au cours des 7 derniers jours).
- `-exec <command> {} \;` : exécute une commande sur chaque fichier trouvé.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `find` :

- **Rechercher un fichier par nom :**
  ```bash
  find /chemin/vers/dossier -name "fichier.txt"
  ```

- **Rechercher tous les fichiers de type répertoire :**
  ```bash
  find /chemin/vers/dossier -type d
  ```

- **Rechercher des fichiers de plus de 100 Mo :**
  ```bash
  find /chemin/vers/dossier -size +100M
  ```

- **Rechercher des fichiers modifiés au cours des 7 derniers jours :**
  ```bash
  find /chemin/vers/dossier -mtime -7
  ```

- **Exécuter une commande sur chaque fichier trouvé :**
  ```bash
  find /chemin/vers/dossier -name "*.log" -exec rm {} \;
  ```

## Tips
- Utilisez des chemins absolus pour éviter toute confusion sur le répertoire de recherche.
- Combinez plusieurs options pour affiner votre recherche (par exemple, `-name` avec `-type`).
- Soyez prudent avec l'option `-exec`, surtout si vous supprimez des fichiers, pour éviter des pertes de données accidentelles.
- Testez vos commandes `find` sans l'option `-exec` d'abord pour vous assurer que vous ciblez les bons fichiers.