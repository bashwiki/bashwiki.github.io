# [Linux] Bash g++ Utilisation : Compiler des programmes C++

## Overview
La commande `g++` est un compilateur pour le langage de programmation C++. Elle fait partie de la suite GNU Compiler Collection (GCC) et est utilisée pour transformer le code source C++ en un programme exécutable.

## Usage
La syntaxe de base de la commande `g++` est la suivante :

```bash
g++ [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `g++` :

- `-o <fichier>` : Spécifie le nom du fichier exécutable de sortie.
- `-Wall` : Active tous les avertissements de compilation.
- `-g` : Inclut des informations de débogage dans l'exécutable.
- `-std=<version>` : Définit la norme C++ à utiliser (par exemple, `-std=c++11`).
- `-I<répertoire>` : Ajoute un répertoire à la liste des chemins de recherche pour les fichiers d'en-tête.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `g++` :

1. Compiler un fichier source simple :

```bash
g++ mon_programme.cpp
```

2. Compiler avec un nom de fichier exécutable spécifique :

```bash
g++ mon_programme.cpp -o mon_executable
```

3. Compiler avec des avertissements activés :

```bash
g++ -Wall mon_programme.cpp
```

4. Compiler avec des informations de débogage :

```bash
g++ -g mon_programme.cpp -o mon_executable
```

5. Utiliser une norme C++ spécifique :

```bash
g++ -std=c++11 mon_programme.cpp -o mon_executable
```

## Tips
- Toujours utiliser l'option `-Wall` pour attraper les avertissements potentiels dans votre code.
- Si vous travaillez sur un projet plus vaste, envisagez d'utiliser un système de construction comme `Makefile` pour gérer les compilations.
- Testez régulièrement votre code en utilisant l'option `-g` pour faciliter le débogage.
- Gardez votre code organisé et utilisez des commentaires pour améliorer la lisibilité.