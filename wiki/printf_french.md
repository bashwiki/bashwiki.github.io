# [Linux] Bash printf Utilisation : Afficher des chaînes formatées

## Overview
La commande `printf` en Bash est utilisée pour afficher des chaînes de caractères formatées. Elle permet un contrôle précis sur la sortie, ce qui la rend très utile pour formater des données avant de les afficher à l'écran ou de les écrire dans un fichier.

## Usage
La syntaxe de base de la commande `printf` est la suivante :

```bash
printf [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `printf` :

- `-v`: Assigne la sortie à une variable au lieu de l'afficher.
- `--help`: Affiche l'aide et les options disponibles.
- `--version`: Affiche la version de `printf`.

## Common Examples

### Exemple 1 : Afficher une chaîne simple
```bash
printf "Bonjour, monde!\n"
```
Cela affichera : `Bonjour, monde!`

### Exemple 2 : Formater des nombres
```bash
printf "Le nombre est : %.2f\n" 3.14159
```
Cela affichera : `Le nombre est : 3.14`

### Exemple 3 : Afficher plusieurs valeurs
```bash
printf "Nom : %s, Âge : %d\n" "Alice" 30
```
Cela affichera : `Nom : Alice, Âge : 30`

### Exemple 4 : Utiliser des variables
```bash
nom="Bob"
age=25
printf "Nom : %s, Âge : %d\n" "$nom" "$age"
```
Cela affichera : `Nom : Bob, Âge : 25`

### Exemple 5 : Écrire dans un fichier
```bash
printf "Ceci est une ligne.\n" > fichier.txt
```
Cela écrira `Ceci est une ligne.` dans `fichier.txt`.

## Tips
- Utilisez `\n` pour ajouter des sauts de ligne dans vos chaînes.
- Pour afficher des pourcentages, doublez le symbole `%` : `printf "Taux : %%\n"`
- Pensez à utiliser des formats appropriés pour vos données (e.g., `%d` pour les entiers, `%f` pour les flottants).
- Testez vos formats avec des valeurs différentes pour vous assurer que la sortie est comme prévu.