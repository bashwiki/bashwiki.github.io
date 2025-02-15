# [리눅스] Bash export 사용법

## Overview
La commande `export` dans Bash est utilisée pour définir des variables d'environnement. Lorsqu'une variable est exportée, elle devient accessible aux processus enfants du shell, ce qui permet à ces processus d'utiliser les valeurs de ces variables. Cela est particulièrement utile pour configurer des paramètres d'environnement nécessaires à l'exécution de programmes ou de scripts.

## Usage
La syntaxe de base de la commande `export` est la suivante :

```bash
export VARIABLE=valeur
```

- **VARIABLE** : le nom de la variable que vous souhaitez définir.
- **valeur** : la valeur que vous souhaitez assigner à la variable.

### Options courantes
- `-p` : affiche toutes les variables d'environnement exportées.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `export`.

### Exemple 1 : Exporter une variable simple
```bash
export MY_VAR="Hello, World!"
```
Dans cet exemple, nous créons une variable `MY_VAR` et lui assignons la valeur "Hello, World!". Cette variable sera accessible dans les processus enfants.

### Exemple 2 : Utiliser une variable exportée dans un script
```bash
export PATH=$PATH:/usr/local/bin
```
Ici, nous ajoutons `/usr/local/bin` à la variable d'environnement `PATH`, ce qui permet au système de rechercher des exécutables dans ce répertoire.

## Tips
- Utilisez des noms de variables en majuscules pour les variables d'environnement afin de les distinguer des variables locales.
- Vérifiez les variables exportées avec la commande `export -p` pour voir celles qui sont actuellement disponibles dans votre session.
- Évitez d'utiliser des espaces autour du signe `=` lors de l'assignation d'une valeur à une variable, sinon cela entraînera une erreur.