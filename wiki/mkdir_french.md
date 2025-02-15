# [리눅스] Bash mkdir 사용법

## Overview
La commande `mkdir` (make directory) est utilisée dans les systèmes d'exploitation basés sur Unix pour créer de nouveaux répertoires. Son objectif principal est de permettre aux utilisateurs de structurer leur système de fichiers en ajoutant des dossiers où ils peuvent organiser des fichiers et d'autres répertoires.

## Usage
La syntaxe de base de la commande `mkdir` est la suivante :

```bash
mkdir [options] nom_du_répertoire
```

### Options courantes :
- `-p` : Crée des répertoires parents si nécessaire. Par exemple, si vous essayez de créer un répertoire dans un chemin qui n'existe pas encore, cette option créera tous les répertoires parents requis.
- `-v` : Affiche un message pour chaque répertoire créé, ce qui peut être utile pour le débogage ou pour vérifier que la commande a fonctionné comme prévu.
- `-m` : Permet de définir les permissions du répertoire lors de sa création. Par exemple, `-m 755` définit les permissions à `rwxr-xr-x`.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mkdir` :

1. **Créer un répertoire simple :**
   ```bash
   mkdir mon_dossier
   ```
   Cette commande crée un répertoire nommé `mon_dossier` dans le répertoire courant.

2. **Créer des répertoires parents :**
   ```bash
   mkdir -p /chemin/vers/mon/nouveau/dossier
   ```
   Cette commande crée le répertoire `dossier` ainsi que tous les répertoires parents nécessaires dans le chemin spécifié.

## Tips
- Utilisez l'option `-v` pour obtenir des confirmations visuelles lors de la création de répertoires, surtout lorsque vous créez plusieurs répertoires à la fois.
- Lorsque vous utilisez l'option `-p`, soyez prudent, car elle peut créer plusieurs répertoires si le chemin spécifié n'existe pas.
- Pensez à vérifier les permissions de votre répertoire après sa création, surtout si vous utilisez l'option `-m` pour définir des permissions spécifiques.