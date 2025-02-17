# [Linux] Bash du : évaluer l'utilisation de l'espace disque

## Overview
La commande `du` (disk usage) est utilisée pour estimer et afficher l'utilisation de l'espace disque des fichiers et des répertoires. Elle permet aux utilisateurs de comprendre combien d'espace est occupé par des fichiers spécifiques ou par des répertoires entiers.

## Usage
La syntaxe de base de la commande `du` est la suivante :

```bash
du [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `du` :

- `-h` : Affiche les tailles dans un format lisible par l'homme (par exemple, Ko, Mo, Go).
- `-s` : Affiche uniquement le total pour chaque argument, sans détailler les sous-répertoires.
- `-a` : Affiche les tailles de tous les fichiers, pas seulement des répertoires.
- `-c` : Affiche un total cumulatif à la fin de la sortie.
- `--max-depth=N` : Limite la profondeur d'affichage des sous-répertoires à N niveaux.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `du` :

1. Pour afficher l'utilisation de l'espace disque de tous les fichiers et répertoires dans le répertoire courant :

   ```bash
   du -h
   ```

2. Pour afficher uniquement le total de l'utilisation de l'espace disque pour le répertoire courant :

   ```bash
   du -sh
   ```

3. Pour afficher l'utilisation de l'espace disque de tous les fichiers dans un répertoire spécifique :

   ```bash
   du -ah /chemin/vers/le/répertoire
   ```

4. Pour afficher l'utilisation de l'espace disque avec un total cumulatif :

   ```bash
   du -ch /chemin/vers/le/répertoire/*
   ```

5. Pour limiter l'affichage des sous-répertoires à un niveau :

   ```bash
   du -h --max-depth=1
   ```

## Tips
- Utilisez l'option `-h` pour rendre les résultats plus faciles à lire, surtout lorsque vous travaillez avec de grandes quantités de données.
- Combinez `du` avec d'autres commandes comme `sort` pour trier les résultats par taille, par exemple :

  ```bash
  du -h | sort -hr
  ```

- Pensez à utiliser `du` avec `grep` pour filtrer les résultats si vous cherchez des fichiers ou répertoires spécifiques :

  ```bash
  du -ah | grep 'nom_du_fichier'
  ``` 

Ces conseils vous aideront à tirer le meilleur parti de la commande `du` et à gérer efficacement l'espace disque sur votre système.