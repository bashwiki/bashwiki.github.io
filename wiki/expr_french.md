# [리눅스] Bash expr 사용법

## Overview
La commande `expr` est un utilitaire en ligne de commande sous Unix et Linux qui permet d'évaluer des expressions. Son principal objectif est de réaliser des opérations arithmétiques, de manipuler des chaînes de caractères et d'effectuer des comparaisons. Bien que `expr` soit souvent utilisé dans des scripts shell pour effectuer des calculs simples, il est important de noter qu'il est moins courant aujourd'hui en raison de l'existence d'autres outils comme `$(( ))` pour les calculs arithmétiques.

## Usage
La syntaxe de base de la commande `expr` est la suivante :

```
expr [expression]
```

### Options courantes :
- **Arithmétique** : `expr` peut effectuer des opérations comme l'addition (`+`), la soustraction (`-`), la multiplication (`*`), et la division (`/`).
- **Comparaison** : `expr` peut comparer des valeurs avec des opérateurs comme `=` (égal), `!=` (différent), `<` (moins que), et `>` (plus que).
- **Manipulation de chaînes** : `expr` peut également être utilisé pour extraire des sous-chaînes ou trouver la longueur d'une chaîne.

## Examples
### Exemple 1 : Opérations arithmétiques
Pour additionner deux nombres, vous pouvez utiliser la commande suivante :

```bash
result=$(expr 5 + 3)
echo $result
```
Cela affichera `8`.

### Exemple 2 : Comparaison de chaînes
Pour comparer deux chaînes de caractères, vous pouvez utiliser :

```bash
if expr "abc" = "abc" > /dev/null; then
    echo "Les chaînes sont égales."
else
    echo "Les chaînes ne sont pas égales."
fi
```
Cela affichera `Les chaînes sont égales.`

## Tips
- Utilisez des parenthèses pour contrôler l'ordre des opérations dans les expressions arithmétiques. Par exemple, `expr 2 + 3 \* 4` donnera `14`, tandis que `expr (2 + 3) \* 4` donnera une erreur de syntaxe.
- Évitez d'utiliser `expr` pour des calculs complexes. Pour des opérations arithmétiques avancées, envisagez d'utiliser `bc` ou `$(( ))`.
- N'oubliez pas d'échapper les caractères spéciaux comme `*` en utilisant un antislash (`\`) pour éviter des erreurs de syntaxe.
- Pour des scripts modernes, privilégiez l'utilisation de `let`, `(( ))`, ou `bc` pour une meilleure lisibilité et fonctionnalité.