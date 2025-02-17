# [Linux] Bash readonly utilisation : Définit des variables en lecture seule

## Overview
La commande `readonly` en Bash permet de définir des variables qui ne peuvent pas être modifiées par la suite. Une fois qu'une variable est marquée comme `readonly`, toute tentative de modification de cette variable entraînera une erreur. Cela est utile pour protéger des valeurs critiques dans vos scripts.

## Usage
La syntaxe de base de la commande `readonly` est la suivante :

```bash
readonly [options] [arguments]
```

## Common Options
- `-p` : Affiche les variables en lecture seule et leurs valeurs.

## Common Examples

### Exemple 1 : Définir une variable en lecture seule
```bash
MY_VAR="Hello"
readonly MY_VAR
```
Dans cet exemple, `MY_VAR` est définie comme une variable en lecture seule. Toute tentative de modification de `MY_VAR` échouera.

### Exemple 2 : Essayer de modifier une variable en lecture seule
```bash
MY_VAR="Hello"
readonly MY_VAR
MY_VAR="World"  # Cela générera une erreur
```
Ici, la tentative de modification de `MY_VAR` après l'avoir déclarée comme `readonly` entraînera une erreur.

### Exemple 3 : Afficher les variables en lecture seule
```bash
readonly -p
```
Cette commande affichera toutes les variables qui ont été définies comme `readonly` dans l'environnement actuel.

## Tips
- Utilisez `readonly` pour protéger les variables qui contiennent des informations sensibles ou critiques pour le fonctionnement de votre script.
- Pensez à utiliser `readonly` dans des scripts complexes pour éviter des modifications accidentelles de variables importantes.
- N'oubliez pas que `readonly` ne s'applique qu'à la session actuelle du shell ; les variables ne seront pas en lecture seule dans d'autres sessions ou scripts à moins d'être redéfinies.