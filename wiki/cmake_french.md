# [Linux] Bash cmake : Générer des fichiers de construction à partir de fichiers de configuration

## Overview
La commande `cmake` est un outil de construction qui permet de gérer le processus de compilation de projets logiciels. Elle génère des fichiers de construction adaptés à différents systèmes de compilation à partir de fichiers de configuration, facilitant ainsi la création et la gestion de projets complexes.

## Usage
La syntaxe de base de la commande `cmake` est la suivante :

```bash
cmake [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `cmake` :

- `-S <source_dir>` : Spécifie le répertoire source contenant le fichier `CMakeLists.txt`.
- `-B <build_dir>` : Définit le répertoire de construction où les fichiers générés seront placés.
- `-D <var>=<value>` : Définit une variable CMake avec une valeur spécifique.
- `--build <dir>` : Compile le projet dans le répertoire spécifié.
- `--target <target>` : Spécifie une cible de construction particulière à construire.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `cmake` :

1. **Générer des fichiers de construction dans un répertoire spécifique :**

   ```bash
   cmake -S . -B build
   ```

2. **Construire le projet après l'avoir configuré :**

   ```bash
   cmake --build build
   ```

3. **Définir une variable lors de la configuration :**

   ```bash
   cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
   ```

4. **Construire une cible spécifique :**

   ```bash
   cmake --build build --target my_target
   ```

## Tips
- Toujours créer un répertoire de construction séparé pour garder votre répertoire source propre.
- Utilisez `cmake-gui` pour une interface graphique si vous préférez une approche visuelle.
- Vérifiez les messages d'erreur lors de l'exécution de `cmake` pour résoudre rapidement les problèmes de configuration.
- Consultez la documentation officielle de CMake pour des options avancées et des configurations spécifiques à votre projet.