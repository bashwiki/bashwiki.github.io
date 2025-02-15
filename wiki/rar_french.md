# [리눅스] Bash rar 사용법

## Overview
La commande `rar` est un utilitaire de compression de fichiers qui permet de créer des archives au format RAR, ainsi que d'extraire des fichiers à partir de ces archives. Son principal objectif est de réduire la taille des fichiers pour faciliter le stockage et le transfert, tout en offrant des fonctionnalités avancées comme la récupération de données et le chiffrement.

## Usage
La syntaxe de base de la commande `rar` est la suivante :

```
rar [options] [command] [archive] [files]
```

### Options courantes :
- `a` : Ajouter des fichiers à une archive.
- `x` : Extraire des fichiers d'une archive.
- `v` : Afficher des informations détaillées sur le processus.
- `r` : Inclure les fichiers dans les sous-répertoires.
- `p` : Protéger l'archive par un mot de passe.

## Examples
### Exemple 1 : Créer une archive RAR
Pour créer une archive RAR nommée `archive.rar` contenant les fichiers `file1.txt` et `file2.txt`, vous pouvez utiliser la commande suivante :

```bash
rar a archive.rar file1.txt file2.txt
```

### Exemple 2 : Extraire une archive RAR
Pour extraire le contenu de l'archive `archive.rar` dans le répertoire courant, utilisez la commande :

```bash
rar x archive.rar
```

## Tips
- Utilisez l'option `-v` pour obtenir des informations détaillées lors de la création ou de l'extraction d'archives, ce qui peut être utile pour le débogage.
- Pensez à utiliser l'option `-p` pour protéger vos archives avec un mot de passe, surtout si elles contiennent des informations sensibles.
- Pour une compression optimale, envisagez d'utiliser l'option `-m5` pour définir le niveau de compression maximum lors de la création d'une archive.