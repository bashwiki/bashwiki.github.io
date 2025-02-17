# [Linux] Bash declare usage : Déclare des variables et des attributs

## Overview
La commande `declare` en Bash est utilisée pour déclarer des variables et définir leurs attributs. Elle permet de spécifier le type de variable, comme un tableau ou une variable entière, et d'assigner des propriétés telles que la lecture seule.

## Usage
La syntaxe de base de la commande `declare` est la suivante :

```bash
declare [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `declare` :

- `-a` : Déclare une variable comme un tableau.
- `-i` : Déclare une variable comme un entier, ce qui permet d'effectuer des opérations arithmétiques automatiquement.
- `-r` : Déclare une variable comme étant en lecture seule.
- `-x` : Exporter la variable pour qu'elle soit disponible dans les sous-shells.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `declare` :

### Déclarer un tableau
```bash
declare -a fruits=("pomme" "banane" "cerise")
echo ${fruits[1]}  # Affiche "banane"
```

### Déclarer une variable entière
```bash
declare -i nombre=5
nombre=nombre+10
echo $nombre  # Affiche "15"
```

### Déclarer une variable en lecture seule
```bash
declare -r constant=100
echo $constant  # Affiche "100"
# constant=200  # Cela provoquera une erreur
```

### Exporter une variable
```bash
declare -x chemin="/usr/local/bin"
echo $chemin  # Affiche "/usr/local/bin"
```

## Tips
- Utilisez `declare -p` pour afficher les attributs et la valeur d'une variable.
- Préférez utiliser `declare` pour des variables qui nécessitent des attributs spécifiques afin d'améliorer la lisibilité et la maintenabilité de votre script.
- Soyez prudent avec les variables en lecture seule ; une fois définies, elles ne peuvent pas être modifiées.