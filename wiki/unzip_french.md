# [리눅스] Bash unzip 사용법

## Overview
La commande `unzip` est un utilitaire de ligne de commande utilisé pour extraire des fichiers compressés au format ZIP. Son objectif principal est de décompresser les fichiers et de restaurer leur structure d'origine, permettant ainsi aux utilisateurs d'accéder aux fichiers contenus dans une archive ZIP.

## Usage
La syntaxe de base de la commande `unzip` est la suivante :

```bash
unzip [options] fichier.zip
```

### Options courantes :
- `-d <répertoire>` : Spécifie le répertoire dans lequel les fichiers extraits doivent être placés. Si ce répertoire n'existe pas, il sera créé.
- `-l` : Liste le contenu de l'archive ZIP sans l'extraire.
- `-o` : Écrase les fichiers existants sans demander confirmation.
- `-q` : Mode silencieux, ne montre pas les messages de progression.

## Examples
### Exemple 1 : Extraire une archive ZIP dans le répertoire courant
Pour extraire tous les fichiers d'une archive nommée `archive.zip` dans le répertoire courant, utilisez la commande suivante :

```bash
unzip archive.zip
```

### Exemple 2 : Extraire une archive ZIP dans un répertoire spécifique
Pour extraire les fichiers de `archive.zip` dans un répertoire nommé `dossier_extrait`, vous pouvez utiliser :

```bash
unzip archive.zip -d dossier_extrait
```

## Tips
- Assurez-vous que vous avez les permissions nécessaires pour écrire dans le répertoire de destination lors de l'extraction des fichiers.
- Utilisez l'option `-l` pour vérifier le contenu d'une archive ZIP avant de l'extraire, ce qui peut vous aider à éviter d'extraire des fichiers non désirés.
- Pensez à utiliser l'option `-o` avec précaution, car elle écrasera les fichiers existants sans confirmation, ce qui peut entraîner une perte de données.