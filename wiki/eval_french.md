# [Linux] Bash eval : Évaluer des commandes dans une chaîne

## Overview
La commande `eval` en Bash permet d'évaluer une chaîne de caractères comme une commande Bash. Cela signifie qu'elle prend une chaîne de texte et l'exécute comme si c'était une commande entrée directement dans le terminal.

## Usage
La syntaxe de base de la commande `eval` est la suivante :

```bash
eval [options] [arguments]
```

## Common Options
`eval` n'a pas d'options spécifiques, mais il prend en charge les arguments qui sont des chaînes de commandes à évaluer.

## Common Examples

### Exemple 1 : Évaluer une simple commande
```bash
cmd="ls -l"
eval $cmd
```
Cet exemple crée une variable `cmd` contenant la commande `ls -l`, puis l'évalue pour afficher la liste des fichiers dans le répertoire courant.

### Exemple 2 : Utiliser des variables dans une commande
```bash
file="mon_fichier.txt"
cmd="cat $file"
eval $cmd
```
Ici, nous définissons une variable `file` et utilisons `eval` pour évaluer la commande qui affiche le contenu de `mon_fichier.txt`.

### Exemple 3 : Évaluation de plusieurs commandes
```bash
commands="echo 'Bonjour'; echo 'Au revoir'"
eval $commands
```
Cet exemple montre comment `eval` peut exécuter plusieurs commandes séparées par un point-virgule.

## Tips
- **Soyez prudent avec les entrées** : Évitez d'utiliser `eval` avec des entrées non fiables, car cela peut conduire à des problèmes de sécurité.
- **Utilisez des guillemets** : Lorsque vous évaluez des chaînes contenant des espaces, entourez-les de guillemets pour éviter des erreurs de syntaxe.
- **Débogage** : Utilisez `echo` pour afficher la commande avant de l'évaluer, cela peut aider à comprendre ce qui sera exécuté.