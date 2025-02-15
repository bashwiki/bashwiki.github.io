# [리눅스] Bash mv 사용법

## Overview
La commande `mv` est utilisée dans Bash pour déplacer ou renommer des fichiers et des répertoires. Son principal objectif est de permettre aux utilisateurs de réorganiser leur système de fichiers en déplaçant des éléments d'un emplacement à un autre ou en changeant leur nom sans créer de copies supplémentaires.

## Usage
La syntaxe de base de la commande `mv` est la suivante :

```bash
mv [options] source destination
```

### Options courantes :
- `-i` : Demande confirmation avant d'écraser un fichier existant.
- `-u` : Déplace uniquement si le fichier source est plus récent que le fichier de destination ou si le fichier de destination n'existe pas.
- `-v` : Affiche les actions effectuées par la commande, utile pour le débogage.

## Examples
### Exemple 1 : Déplacer un fichier
Pour déplacer un fichier nommé `document.txt` vers un répertoire nommé `dossier` :

```bash
mv document.txt dossier/
```

### Exemple 2 : Renommer un fichier
Pour renommer un fichier de `ancien_nom.txt` à `nouveau_nom.txt` :

```bash
mv ancien_nom.txt nouveau_nom.txt
```

## Tips
- Utilisez l'option `-i` pour éviter d'écraser accidentellement des fichiers existants.
- Lorsque vous déplacez des fichiers vers un répertoire, assurez-vous que le répertoire de destination existe pour éviter les erreurs.
- Pour des opérations de déplacement fréquentes, envisagez d'utiliser des alias dans votre fichier `.bashrc` pour simplifier la syntaxe.