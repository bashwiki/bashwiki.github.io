# [Linux] Bash lsattr : Afficher les attributs de fichiers

## Overview
La commande `lsattr` est utilisée pour afficher les attributs des fichiers dans un système de fichiers Linux. Ces attributs peuvent influencer le comportement des fichiers, comme la protection contre la suppression ou la modification.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
lsattr [options] [arguments]
```

## Common Options
- `-a` : Affiche les attributs de tous les fichiers, y compris ceux qui sont cachés.
- `-d` : Affiche les attributs des répertoires.
- `-R` : Affiche les attributs de manière récursive dans les sous-répertoires.
- `-v` : Affiche les attributs en mode verbeux.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `lsattr` :

1. Afficher les attributs des fichiers dans le répertoire courant :

    ```bash
    lsattr
    ```

2. Afficher les attributs de tous les fichiers, y compris les fichiers cachés :

    ```bash
    lsattr -a
    ```

3. Afficher les attributs d'un répertoire spécifique :

    ```bash
    lsattr -d /chemin/vers/le/répertoire
    ```

4. Afficher les attributs de manière récursive dans un répertoire :

    ```bash
    lsattr -R /chemin/vers/le/répertoire
    ```

5. Afficher les attributs en mode verbeux :

    ```bash
    lsattr -v
    ```

## Tips
- Utilisez `lsattr` régulièrement pour vérifier les attributs de vos fichiers, surtout avant de les modifier ou de les supprimer.
- Faites attention aux fichiers avec des attributs spéciaux comme `i` (immutable) qui empêchent toute modification.
- Combinez `lsattr` avec d'autres commandes comme `chattr` pour modifier les attributs si nécessaire.