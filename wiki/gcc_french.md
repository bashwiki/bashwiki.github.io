# [Linux] Bash gcc Utilisation : Compiler des programmes en C et C++

## Overview
La commande `gcc` (GNU Compiler Collection) est un compilateur principalement utilisé pour compiler des programmes écrits en C et C++. Il permet de transformer le code source en un exécutable, facilitant ainsi l'exécution des programmes sur un système d'exploitation.

## Usage
La syntaxe de base de la commande `gcc` est la suivante :

```bash
gcc [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `gcc` :

- `-o <nom>` : Spécifie le nom du fichier exécutable de sortie.
- `-Wall` : Active tous les avertissements lors de la compilation.
- `-g` : Inclut des informations de débogage dans l'exécutable.
- `-I <répertoire>` : Indique un répertoire supplémentaire à rechercher pour les fichiers d'en-tête.
- `-L <répertoire>` : Indique un répertoire supplémentaire à rechercher pour les bibliothèques.
- `-l <bibliothèque>` : Lie le programme avec une bibliothèque spécifiée.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `gcc` :

1. Compiler un fichier source simple en un exécutable :

   ```bash
   gcc mon_programme.c -o mon_programme
   ```

2. Compiler avec des avertissements activés :

   ```bash
   gcc -Wall mon_programme.c -o mon_programme
   ```

3. Compiler avec des informations de débogage :

   ```bash
   gcc -g mon_programme.c -o mon_programme
   ```

4. Compiler plusieurs fichiers source :

   ```bash
   gcc fichier1.c fichier2.c -o mon_programme
   ```

5. Lier une bibliothèque lors de la compilation :

   ```bash
   gcc mon_programme.c -o mon_programme -lm
   ```

## Tips
- Assurez-vous de toujours utiliser l'option `-Wall` pour détecter les erreurs potentielles dans votre code.
- Utilisez l'option `-g` lors du développement pour faciliter le débogage avec des outils comme `gdb`.
- Gardez votre code organisé en séparant les fichiers source et les fichiers d'en-tête, et utilisez les options `-I` et `-L` pour gérer les chemins d'accès.
- Pensez à consulter la documentation de `gcc` pour explorer d'autres options avancées qui peuvent améliorer votre processus de compilation.