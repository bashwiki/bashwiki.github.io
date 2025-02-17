# [Linux] Bash let : Évaluer des expressions arithmétiques

## Overview
La commande `let` dans Bash est utilisée pour évaluer des expressions arithmétiques. Elle permet d'effectuer des calculs simples et d'assigner des valeurs à des variables en utilisant des opérations mathématiques.

## Usage
La syntaxe de base de la commande `let` est la suivante :

```bash
let [options] [arguments]
```

## Common Options
- `-n` : Ne pas afficher le résultat de l'évaluation.
- `-e` : Arrêter l'exécution si une erreur se produit lors de l'évaluation.

## Common Examples

### Exemple 1 : Addition simple
```bash
let "a = 5 + 3"
echo $a  # Affiche 8
```

### Exemple 2 : Soustraction
```bash
let "b = 10 - 4"
echo $b  # Affiche 6
```

### Exemple 3 : Multiplication
```bash
let "c = 7 * 6"
echo $c  # Affiche 42
```

### Exemple 4 : Division
```bash
let "d = 20 / 4"
echo $d  # Affiche 5
```

### Exemple 5 : Utilisation de variables
```bash
x=10
y=5
let "result = x + y"
echo $result  # Affiche 15
```

## Tips
- Utilisez des guillemets autour de l'expression pour éviter des erreurs de syntaxe, surtout si vous utilisez des espaces.
- `let` ne nécessite pas le signe `$` pour les variables, ce qui le rend légèrement différent des autres commandes.
- Pour des calculs plus complexes, envisagez d'utiliser `expr` ou `$(( ))`, qui sont également couramment utilisés pour les opérations arithmétiques dans Bash.