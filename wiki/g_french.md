# [리눅스] Bash g++ 사용법

## Overview
La commande `g++` est un compilateur pour le langage de programmation C++. Il fait partie de la suite GNU Compiler Collection (GCC) et est utilisé pour compiler des fichiers source C++ en exécutables. Le principal objectif de `g++` est de transformer le code source écrit en C++ en code machine que l'ordinateur peut exécuter.

## Usage
La syntaxe de base de la commande `g++` est la suivante :

```bash
g++ [options] fichier_source.cpp -o nom_executable
```

### Options courantes :
- `-o nom_executable` : spécifie le nom du fichier exécutable à créer. Si cette option n'est pas fournie, le fichier exécutable par défaut sera nommé `a.out`.
- `-Wall` : active tous les avertissements, ce qui est utile pour détecter des erreurs potentielles dans le code.
- `-g` : inclut des informations de débogage dans l'exécutable, ce qui facilite le débogage avec des outils comme `gdb`.
- `-std=c++11` : spécifie la version du standard C++ à utiliser (dans cet exemple, C++11).

## Examples
### Exemple 1 : Compilation simple
Pour compiler un fichier source C++ nommé `programme.cpp` et créer un exécutable nommé `programme`, utilisez la commande suivante :

```bash
g++ programme.cpp -o programme
```

### Exemple 2 : Compilation avec avertissements et débogage
Pour compiler le même fichier tout en activant les avertissements et en incluant des informations de débogage, utilisez :

```bash
g++ -Wall -g programme.cpp -o programme
```

## Tips
- Toujours utiliser l'option `-Wall` pour être informé des avertissements potentiels dans votre code, cela peut vous aider à éviter des erreurs lors de l'exécution.
- Pensez à utiliser l'option `-std` pour vous assurer que votre code est conforme à la version de C++ que vous souhaitez utiliser.
- Si vous travaillez sur un projet plus complexe, envisagez d'utiliser un système de construction comme `Makefile` pour gérer la compilation de plusieurs fichiers source.