# [Linux] Bash bc Utilisation : Calculatrice de précision arbitraire

## Overview
La commande `bc` (Basic Calculator) est un langage de calcul qui permet d'effectuer des opérations arithmétiques avec une précision arbitraire. Elle est souvent utilisée dans les scripts Bash pour effectuer des calculs complexes qui dépassent les capacités des opérations arithmétiques de base.

## Usage
La syntaxe de base de la commande `bc` est la suivante :

```bash
bc [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `bc` :

- `-l` : Charge la bibliothèque mathématique standard, permettant d'utiliser des fonctions mathématiques avancées.
- `-q` : Exécute `bc` en mode silencieux, sans afficher le message de bienvenue.
- `-e` : Exécute une expression donnée directement depuis la ligne de commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `bc` :

1. **Calcul simple :**
   ```bash
   echo "5 + 3" | bc
   ```
   Cela affichera `8`.

2. **Calcul avec précision :**
   ```bash
   echo "scale=2; 10 / 3" | bc
   ```
   Cela affichera `3.33`, où `scale=2` définit le nombre de décimales.

3. **Utilisation de la bibliothèque mathématique :**
   ```bash
   echo "scale=4; s(1)" | bc -l
   ```
   Cela affichera `0.8415`, qui est la valeur de sin(1) avec une précision de 4 décimales.

4. **Exécution d'une expression directement :**
   ```bash
   bc -e "2^10"
   ```
   Cela affichera `1024`, qui est 2 à la puissance 10.

## Tips
- Toujours définir `scale` pour les divisions afin d'obtenir le nombre de décimales souhaité.
- Utilisez `bc -l` pour accéder à des fonctions mathématiques avancées comme `s()` pour le sinus, `c()` pour le cosinus, etc.
- Pour des calculs plus complexes, envisagez d'écrire des scripts `bc` dans des fichiers et de les exécuter avec `bc nom_du_fichier`.

Avec ces informations, vous devriez être en mesure d'utiliser la commande `bc` efficacement pour vos besoins de calcul dans Bash.