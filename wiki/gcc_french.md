# [리눅스] Bash gcc 사용법

## Overview
La commande `gcc` (GNU Compiler Collection) est un compilateur pour le langage de programmation C, mais il prend également en charge d'autres langages comme C++, Objective-C, Fortran, Ada, et bien d'autres. Son objectif principal est de traduire le code source écrit en langage de programmation en code machine exécutable, permettant ainsi aux développeurs de créer des applications et des programmes.

## Usage
La syntaxe de base de la commande `gcc` est la suivante :

```bash
gcc [options] fichier_source.c -o nom_executable
```

### Options courantes :
- `-o nom_executable` : Spécifie le nom du fichier exécutable généré.
- `-Wall` : Active tous les avertissements, ce qui est utile pour détecter les erreurs potentielles dans le code.
- `-g` : Inclut des informations de débogage dans l'exécutable, facilitant le débogage avec des outils comme `gdb`.
- `-O` : Active l'optimisation du code pour améliorer les performances. Par exemple, `-O2` est un niveau d'optimisation courant.
- `-I` : Indique un répertoire supplémentaire à rechercher pour les fichiers d'en-tête.

## Examples
### Exemple 1 : Compilation simple
Pour compiler un fichier source C nommé `mon_programme.c` et créer un exécutable nommé `mon_programme`, utilisez la commande suivante :

```bash
gcc mon_programme.c -o mon_programme
```

### Exemple 2 : Compilation avec avertissements et débogage
Pour compiler le même fichier tout en activant les avertissements et en incluant des informations de débogage, vous pouvez exécuter :

```bash
gcc -Wall -g mon_programme.c -o mon_programme
```

## Tips
- Utilisez toujours l'option `-Wall` pour être informé des avertissements potentiels dans votre code. Cela peut vous aider à éviter des erreurs difficiles à détecter plus tard.
- Pensez à organiser votre code en plusieurs fichiers source et utilisez l'option `-I` pour inclure des fichiers d'en-tête personnalisés.
- Pour les projets plus complexes, envisagez d'utiliser un système de construction comme `Make` pour automatiser le processus de compilation.
- Testez régulièrement votre code en utilisant l'option `-g` pour faciliter le débogage, surtout lors du développement de nouvelles fonctionnalités.