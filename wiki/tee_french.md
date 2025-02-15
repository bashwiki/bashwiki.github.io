# [리눅스] Bash tee 사용법

## Overview
La commande `tee` est un utilitaire de ligne de commande dans Bash qui permet de lire l'entrée standard et de l'écrire à la fois dans la sortie standard et dans un ou plusieurs fichiers. Son principal objectif est de permettre aux utilisateurs de rediriger la sortie d'une commande vers plusieurs destinations, ce qui est particulièrement utile pour le débogage ou la journalisation.

## Usage
La syntaxe de base de la commande `tee` est la suivante :

```bash
tee [options] [fichiers...]
```

### Options courantes :
- `-a` ou `--append` : Ajoute la sortie à la fin des fichiers spécifiés au lieu de les écraser.
- `-i` ou `--ignore-interrupts` : Ignore les signaux d'interruption.
- `-p` ou `--output-error` : Contrôle le comportement en cas d'erreur d'écriture dans les fichiers.

## Examples
### Exemple 1 : Écrire dans un fichier
```bash
echo "Ceci est un test" | tee fichier.txt
```
Dans cet exemple, la chaîne "Ceci est un test" est affichée à l'écran et écrite dans `fichier.txt`.

### Exemple 2 : Ajouter à un fichier existant
```bash
echo "Ajout d'une nouvelle ligne" | tee -a fichier.txt
```
Ici, la chaîne "Ajout d'une nouvelle ligne" est ajoutée à la fin de `fichier.txt`, tout en étant affichée à l'écran.

## Tips
- Utilisez l'option `-a` si vous souhaitez conserver le contenu existant d'un fichier lors de l'ajout de nouvelles données.
- Combinez `tee` avec d'autres commandes pour créer des pipelines puissants. Par exemple, vous pouvez utiliser `tee` pour enregistrer les résultats d'une commande tout en les affichant à l'écran.
- Faites attention aux permissions des fichiers lorsque vous utilisez `tee`, car cela peut entraîner des erreurs si vous essayez d'écrire dans un fichier sans les droits nécessaires.