# [리눅스] Bash bc 사용법

## Overview
La commande `bc` (Basic Calculator) est un langage de calcul arbitraire qui permet d'effectuer des opérations mathématiques à la fois simples et complexes. Elle est particulièrement utile pour les ingénieurs et les développeurs qui ont besoin de réaliser des calculs précis dans un environnement de ligne de commande. `bc` prend en charge les opérations arithmétiques, les fonctions mathématiques, et peut gérer des nombres avec une précision définie par l'utilisateur.

## Usage
La syntaxe de base de la commande `bc` est la suivante :

```bash
bc [options] [fichier]
```

### Options courantes :
- `-l` : Charge la bibliothèque mathématique standard, ce qui permet d'utiliser des fonctions mathématiques avancées comme `sine`, `cosine`, etc.
- `-q` : Exécute `bc` en mode silencieux, sans afficher le message de bienvenue.
- `-e` : Exécute une expression directement à partir de la ligne de commande.

## Examples
### Exemple 1 : Calcul simple
Pour effectuer un calcul simple, vous pouvez exécuter `bc` et entrer des expressions mathématiques. Par exemple, pour additionner 5 et 3 :

```bash
echo "5 + 3" | bc
```
Cela affichera `8`.

### Exemple 2 : Utilisation de la bibliothèque mathématique
Pour utiliser des fonctions mathématiques, vous pouvez charger la bibliothèque avec l'option `-l`. Par exemple, pour calculer la racine carrée de 16 :

```bash
echo "scale=2; sqrt(16)" | bc -l
```
Cela affichera `4.00`, où `scale=2` définit le nombre de décimales à afficher.

## Tips
- Utilisez `scale` pour définir le nombre de décimales dans vos résultats. Par exemple, `scale=4; 10/3` donnera `3.3333`.
- Pour des calculs plus complexes, écrivez vos expressions dans un fichier texte et exécutez `bc` avec le nom du fichier. Cela facilite la gestion de calculs longs ou répétitifs.
- N'oubliez pas que `bc` traite les nombres comme des entiers par défaut, donc si vous souhaitez des résultats décimaux, assurez-vous de définir `scale` ou d'utiliser des nombres à virgule flottante.