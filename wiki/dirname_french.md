# [리눅스] Bash dirname 사용법

## Overview
La commande `dirname` est un utilitaire en ligne de commande qui permet d'extraire le chemin du répertoire d'un fichier ou d'un chemin donné. Son objectif principal est de retourner la partie du chemin qui précède le nom du fichier, ce qui est particulièrement utile pour manipuler des chemins de fichiers dans des scripts ou des environnements de développement.

## Usage
La syntaxe de base de la commande `dirname` est la suivante :

```bash
dirname [CHEMIN]
```

### Options courantes
- `-z` : Traite les chemins vides comme des chaînes vides. Cela peut être utile pour éviter des erreurs lors de l'utilisation de variables qui pourraient ne pas contenir de valeur.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `dirname`.

### Exemple 1 : Extraire le répertoire d'un chemin
Supposons que vous ayez un fichier situé à `/home/utilisateur/documents/fichier.txt`. Pour obtenir le chemin du répertoire, vous pouvez exécuter :

```bash
dirname /home/utilisateur/documents/fichier.txt
```

Cela affichera :

```
/home/utilisateur/documents
```

### Exemple 2 : Utilisation avec une variable
Vous pouvez également utiliser `dirname` avec une variable contenant un chemin. Par exemple :

```bash
chemin="/var/log/syslog"
echo $(dirname $chemin)
```

Cela affichera :

```
/var/log
```

## Tips
- Utilisez `dirname` dans des scripts pour automatiser la gestion des chemins de fichiers. Cela peut vous aider à éviter des erreurs lors de la manipulation de fichiers.
- Combinez `dirname` avec d'autres commandes comme `basename` pour obtenir à la fois le répertoire et le nom de fichier d'un chemin donné.
- Soyez prudent avec les chemins relatifs et absolus, car `dirname` renverra des résultats différents selon le type de chemin que vous fournissez.