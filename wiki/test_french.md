# [리눅스] Bash test 사용법

## Overview
La commande `test` est un utilitaire de ligne de commande dans Bash qui permet d'évaluer des expressions conditionnelles. Son principal objectif est de vérifier des conditions telles que l'existence de fichiers, les comparaisons numériques et les comparaisons de chaînes. `test` renvoie un code de sortie qui indique si la condition est vraie (0) ou fausse (1), ce qui est particulièrement utile dans les scripts shell pour contrôler le flux d'exécution.

## Usage
La syntaxe de base de la commande `test` est la suivante :

```bash
test EXPRESSION
```

ou, de manière équivalente :

```bash
[ EXPRESSION ]
```

### Options courantes
- `-e FICHIER` : Vérifie si le fichier spécifié existe.
- `-f FICHIER` : Vérifie si le fichier spécifié est un fichier régulier.
- `-d FICHIER` : Vérifie si le fichier spécifié est un répertoire.
- `-z CHAÎNE` : Vérifie si la chaîne est vide.
- `-n CHAÎNE` : Vérifie si la chaîne n'est pas vide.
- `NUM1 -eq NUM2` : Vérifie si NUM1 est égal à NUM2.
- `NUM1 -ne NUM2` : Vérifie si NUM1 n'est pas égal à NUM2.
- `NUM1 -lt NUM2` : Vérifie si NUM1 est inférieur à NUM2.
- `NUM1 -gt NUM2` : Vérifie si NUM1 est supérieur à NUM2.

## Examples
### Exemple 1 : Vérifier l'existence d'un fichier
```bash
if test -e mon_fichier.txt; then
    echo "Le fichier existe."
else
    echo "Le fichier n'existe pas."
fi
```
Dans cet exemple, nous utilisons `test` pour vérifier si `mon_fichier.txt` existe. Si c'est le cas, un message est affiché.

### Exemple 2 : Comparaison de nombres
```bash
a=5
b=10

if test $a -lt $b; then
    echo "$a est inférieur à $b."
else
    echo "$a n'est pas inférieur à $b."
fi
```
Ici, nous comparons deux nombres. Si `a` est inférieur à `b`, un message approprié est affiché.

## Tips
- Utilisez les crochets `[` et `]` comme une alternative à `test` pour rendre votre code plus lisible, mais assurez-vous d'inclure des espaces autour des crochets.
- Évitez d'utiliser des variables non définies dans les expressions pour prévenir les erreurs. Utilisez `-n` pour vérifier si une variable est définie avant de l'utiliser.
- Combinez plusieurs conditions en utilisant `-a` (et) ou `-o` (ou) pour des évaluations plus complexes.
- Pour une meilleure lisibilité, envisagez d'utiliser `[[ ... ]]` qui offre des fonctionnalités supplémentaires par rapport à `test` et est plus sûr pour les comparaisons de chaînes.