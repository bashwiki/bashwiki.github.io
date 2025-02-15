# [리눅스] Bash declare 사용법

## Overview
La commande `declare` dans Bash est utilisée pour déclarer des variables et définir leurs attributs. Elle permet de spécifier le type de variable (comme un tableau ou une variable associative) et d'autres propriétés, telles que la lecture seule. Cela aide à gérer les variables de manière plus structurée et à éviter les erreurs potentielles lors de l'utilisation des variables dans des scripts.

## Usage
La syntaxe de base de la commande `declare` est la suivante :

```bash
declare [options] [variable_name]
```

### Options courantes :
- `-a` : Déclare un tableau.
- `-A` : Déclare un tableau associatif.
- `-r` : Rend la variable en lecture seule.
- `-x` : Exporter la variable pour qu'elle soit disponible dans les sous-shells.
- `-i` : Déclare une variable entière, ce qui signifie que toute valeur assignée sera traitée comme un entier.

## Examples

### Exemple 1 : Déclaration d'un tableau
```bash
declare -a fruits
fruits=("pomme" "banane" "cerise")
echo "${fruits[1]}"  # Affiche "banane"
```
Dans cet exemple, nous déclarons un tableau nommé `fruits` et y assignons trois valeurs. Ensuite, nous affichons la deuxième valeur du tableau.

### Exemple 2 : Variable en lecture seule
```bash
declare -r PI=3.14
echo "$PI"  # Affiche "3.14"
PI=3.14159  # Erreur : tentative de modification d'une variable en lecture seule
```
Ici, nous déclarons une variable `PI` comme étant en lecture seule. Toute tentative de modification de cette variable entraînera une erreur.

## Tips
- Utilisez `declare` pour rendre vos scripts plus robustes en définissant clairement le type et les propriétés des variables.
- Pensez à utiliser `-x` pour les variables qui doivent être accessibles dans des sous-shells, comme lors de l'exécution de scripts ou de commandes subséquentes.
- Évitez de mélanger les types de variables dans un même contexte pour prévenir les comportements inattendus.
- Utilisez `declare -p` pour afficher les variables et leurs attributs, ce qui peut être utile pour le débogage.

En utilisant la commande `declare`, vous pouvez améliorer la lisibilité et la maintenabilité de vos scripts Bash.