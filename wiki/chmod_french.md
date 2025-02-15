# [리눅스] Bash chmod 사용법

## Overview
La commande `chmod` (change mode) est utilisée dans les systèmes Unix et Linux pour modifier les permissions d'accès des fichiers et des répertoires. Son objectif principal est de contrôler qui peut lire, écrire ou exécuter un fichier ou un répertoire, permettant ainsi de gérer la sécurité et l'accès aux ressources du système.

## Usage
La syntaxe de base de la commande `chmod` est la suivante :

```bash
chmod [options] mode fichier
```

### Options courantes :
- `-R` : Applique les modifications de manière récursive à tous les fichiers et sous-répertoires.
- `-v` : Affiche les modifications effectuées pour chaque fichier.
- `-c` : Affiche les fichiers dont les permissions ont été changées.

### Modes :
Les modes peuvent être spécifiés de deux manières :
1. **Symbolique** : Utilise des lettres pour définir les permissions.
   - `u` : utilisateur (owner)
   - `g` : groupe
   - `o` : autres
   - `a` : tous (user, group, others)
   - `+` : ajouter une permission
   - `-` : retirer une permission
   - `=` : définir exactement les permissions

2. **Octale** : Utilise des chiffres pour définir les permissions.
   - `4` : lecture (read)
   - `2` : écriture (write)
   - `1` : exécution (execute)

Par exemple, `chmod 755 fichier` donne au propriétaire toutes les permissions (7), et aux autres utilisateurs la permission de lire et d'exécuter (5).

## Examples
### Exemple 1 : Changer les permissions d'un fichier
Pour donner au propriétaire d'un fichier `script.sh` la permission d'exécution, tout en gardant les permissions de lecture et d'écriture pour le groupe et les autres, vous pouvez utiliser :

```bash
chmod 755 script.sh
```

### Exemple 2 : Modifier les permissions de manière récursive
Pour donner à tous les fichiers et sous-répertoires dans un répertoire `mon_dossier` la permission d'exécution, vous pouvez utiliser :

```bash
chmod -R +x mon_dossier
```

## Tips
- Avant de modifier les permissions, utilisez `ls -l` pour vérifier les permissions actuelles d'un fichier ou d'un répertoire.
- Soyez prudent avec les permissions `777`, car cela donne un accès complet à tous les utilisateurs, ce qui peut poser des problèmes de sécurité.
- Utilisez l'option `-v` pour voir les changements effectués, ce qui peut être utile pour le débogage.
- Pour des scripts, il est souvent recommandé de donner des permissions d'exécution uniquement aux utilisateurs qui en ont besoin, afin de minimiser les risques de sécurité.