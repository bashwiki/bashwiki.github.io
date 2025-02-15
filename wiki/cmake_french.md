# [리눅스] Bash cmake 사용법

## Overview
La commande `cmake` est un outil de construction multiplateforme qui utilise des fichiers de configuration pour générer des fichiers de projet pour divers systèmes de construction, tels que Makefiles ou des projets Visual Studio. Son objectif principal est de simplifier le processus de compilation de logiciels en automatisant la configuration des projets, ce qui permet aux développeurs de se concentrer sur le code plutôt que sur les détails de construction.

## Usage
La syntaxe de base de la commande `cmake` est la suivante :

```bash
cmake [options] <répertoire_source>
```

### Options courantes :
- `-B <répertoire_build>` : Spécifie le répertoire où les fichiers de construction seront générés.
- `-S <répertoire_source>` : Indique le répertoire source contenant le fichier CMakeLists.txt.
- `-D <variable>=<valeur>` : Définit une variable pour la configuration du projet.
- `--build <répertoire_build>` : Lance le processus de construction dans le répertoire spécifié.

## Examples
### Exemple 1 : Configuration d'un projet
Pour configurer un projet à partir d'un répertoire source, vous pouvez utiliser la commande suivante :

```bash
cmake -S . -B build
```
Cette commande configure le projet en utilisant le répertoire courant comme source et crée un répertoire `build` pour les fichiers de construction.

### Exemple 2 : Construction du projet
Une fois que le projet est configuré, vous pouvez le construire avec :

```bash
cmake --build build
```
Cette commande compile le projet en utilisant les fichiers générés dans le répertoire `build`.

## Tips
- Assurez-vous que le fichier `CMakeLists.txt` est correctement configuré dans votre répertoire source, car il contient les instructions nécessaires pour la construction du projet.
- Utilisez l'option `-D` pour personnaliser les paramètres de construction, comme les chemins d'installation ou les options de compilation spécifiques.
- Pour des projets complexes, envisagez d'utiliser des sous-répertoires avec des fichiers `CMakeLists.txt` séparés pour une meilleure organisation.
- N'hésitez pas à consulter la documentation officielle de CMake pour des options avancées et des fonctionnalités supplémentaires.