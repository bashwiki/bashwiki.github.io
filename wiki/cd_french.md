# [리눅스] Bash cd 사용법

## Overview
La commande `cd`, qui signifie "change directory" (changer de répertoire), est utilisée dans le shell Bash pour naviguer entre les répertoires du système de fichiers. Son objectif principal est de modifier le répertoire de travail actuel, ce qui permet aux utilisateurs d'accéder à différents fichiers et sous-répertoires sans avoir à spécifier des chemins complets à chaque fois.

## Usage
La syntaxe de base de la commande `cd` est la suivante :

```bash
cd [options] [répertoire]
```

### Options courantes
- `..` : Permet de remonter d'un niveau dans l'arborescence des répertoires.
- `-` : Permet de revenir au dernier répertoire visité.
- `~` : Représente le répertoire personnel de l'utilisateur.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cd` :

1. **Naviguer vers un répertoire spécifique** :
   ```bash
   cd /home/utilisateur/Documents
   ```
   Cette commande vous amène directement au répertoire "Documents" de l'utilisateur.

2. **Revenir au répertoire parent** :
   ```bash
   cd ..
   ```
   Cela vous fera remonter d'un niveau dans l'arborescence des répertoires.

3. **Revenir au dernier répertoire** :
   ```bash
   cd -
   ```
   Cette commande vous ramène au dernier répertoire que vous avez visité.

## Tips
- Utilisez `cd ~` pour accéder rapidement à votre répertoire personnel.
- Vous pouvez utiliser la touche `Tab` pour l'auto-complétion des noms de répertoires, ce qui peut vous faire gagner du temps et éviter les erreurs de frappe.
- Pour voir votre répertoire de travail actuel, utilisez la commande `pwd` (print working directory) après avoir changé de répertoire.