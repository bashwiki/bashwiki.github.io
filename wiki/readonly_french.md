# [리눅스] Bash readonly 사용법

## Overview
La commande `readonly` en Bash est utilisée pour marquer une variable comme étant en lecture seule. Cela signifie que, une fois qu'une variable a été déclarée comme `readonly`, sa valeur ne peut plus être modifiée ou supprimée. Cette fonctionnalité est particulièrement utile pour protéger les variables critiques dans un script, garantissant ainsi que leur valeur reste constante tout au long de l'exécution.

## Usage
La syntaxe de base de la commande `readonly` est la suivante :

```bash
readonly VARIABLE_NAME=value
```

ou pour rendre une variable existante en lecture seule :

```bash
readonly VARIABLE_NAME
```

### Options communes
- `-p` : Affiche une liste des variables en lecture seule et leurs valeurs.

## Examples
### Exemple 1 : Déclaration d'une variable en lecture seule
```bash
readonly PI=3.14
echo $PI  # Affiche 3.14
PI=3.14159  # Cela provoquera une erreur : "bash: PI: readonly variable"
```

### Exemple 2 : Utilisation de l'option -p
```bash
readonly VAR1="Hello"
readonly VAR2="World"
readonly -p  # Affiche : declare -r VAR1="Hello" ; declare -r VAR2="World"
```

## Tips
- Utilisez `readonly` pour les variables qui ne doivent pas changer, comme les configurations ou les constantes.
- Si vous essayez de modifier une variable marquée comme `readonly`, Bash renverra une erreur, ce qui peut vous aider à identifier les erreurs dans votre script.
- Vous pouvez utiliser `declare -r` comme alternative à `readonly`, car les deux commandes fonctionnent de manière similaire pour déclarer des variables en lecture seule.