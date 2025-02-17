# [Linux] Bash expr Utilisation : Évaluation d'expressions

## Overview
La commande `expr` est utilisée pour évaluer des expressions arithmétiques, des chaînes de caractères et des comparaisons. Elle permet d'effectuer des calculs simples et de manipuler des chaînes dans un environnement Bash.

## Usage
La syntaxe de base de la commande `expr` est la suivante :

```bash
expr [options] [arguments]
```

## Common Options
- `+` : Additionne deux nombres.
- `-` : Soustrait le deuxième nombre du premier.
- `*` : Multiplie deux nombres.
- `/` : Divise le premier nombre par le deuxième.
- `%` : Renvoie le reste de la division du premier nombre par le deuxième.
- `=` : Évalue si deux valeurs sont égales.
- `!=` : Évalue si deux valeurs ne sont pas égales.
- `>` : Évalue si la première valeur est supérieure à la deuxième.
- `<` : Évalue si la première valeur est inférieure à la deuxième.

## Common Examples

### Exemple 1 : Addition de deux nombres
```bash
result=$(expr 5 + 3)
echo $result  # Affiche 8
```

### Exemple 2 : Soustraction
```bash
result=$(expr 10 - 4)
echo $result  # Affiche 6
```

### Exemple 3 : Multiplication
```bash
result=$(expr 7 \* 6)
echo $result  # Affiche 42
```

### Exemple 4 : Division
```bash
result=$(expr 20 / 4)
echo $result  # Affiche 5
```

### Exemple 5 : Comparaison
```bash
if expr 5 \> 3; then
    echo "5 est supérieur à 3"  # Affiche ce message
fi
```

## Tips
- Utilisez des guillemets autour des arguments pour éviter des erreurs avec des espaces ou des caractères spéciaux.
- N'oubliez pas d'échapper le caractère `*` avec un antislash (`\`) pour éviter qu'il soit interprété par le shell.
- Pour des calculs plus complexes, envisagez d'utiliser `bc` ou `awk`, qui offrent plus de fonctionnalités.