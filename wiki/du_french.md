# [리눅스] Bash du 사용법

## Overview
La commande `du` (Disk Usage) est utilisée pour estimer et afficher l'espace disque utilisé par des fichiers et des répertoires dans un système de fichiers. Son objectif principal est d'aider les utilisateurs à comprendre combien d'espace est occupé par des fichiers spécifiques ou des répertoires, ce qui est particulièrement utile pour la gestion de l'espace disque sur les serveurs et les systèmes de fichiers.

## Usage
La syntaxe de base de la commande `du` est la suivante :

```
du [options] [fichiers/répertoires]
```

### Options courantes :
- `-h` : Affiche la taille dans un format lisible par l'homme (par exemple, Ko, Mo, Go).
- `-s` : Affiche uniquement le total pour chaque argument, sans afficher les sous-répertoires.
- `-a` : Inclut les fichiers dans la sortie, pas seulement les répertoires.
- `-c` : Affiche un total cumulatif à la fin de la sortie.
- `--max-depth=N` : Limite la profondeur d'affichage des répertoires à N niveaux.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `du` :

1. Pour afficher l'utilisation de l'espace disque de tous les répertoires dans le répertoire courant, en format lisible par l'homme :

   ```bash
   du -h
   ```

2. Pour afficher uniquement le total de l'espace disque utilisé par un répertoire spécifique, par exemple `/var/log` :

   ```bash
   du -sh /var/log
   ```

3. Pour afficher l'utilisation de l'espace disque de tous les fichiers et répertoires jusqu'à une profondeur de 2 niveaux :

   ```bash
   du -h --max-depth=2
   ```

## Tips
- Utilisez l'option `-h` pour rendre les résultats plus faciles à lire, surtout lorsque vous travaillez avec de grandes quantités de données.
- Combinez `du` avec d'autres commandes comme `sort` pour trier les résultats par taille. Par exemple :

  ```bash
  du -h | sort -hr
  ```

- Pensez à utiliser l'option `-c` pour obtenir un total cumulatif lorsque vous analysez plusieurs répertoires.
- Si vous souhaitez exclure certains fichiers ou répertoires, vous pouvez utiliser `--exclude` suivi du motif à exclure.

En utilisant ces conseils et exemples, vous serez en mesure de tirer le meilleur parti de la commande `du` pour gérer efficacement l'espace disque sur vos systèmes.