# [Linux] Bash test usage : Vérifier les expressions conditionnelles

## Overview
La commande `test` est utilisée dans Bash pour évaluer des expressions conditionnelles. Elle permet de vérifier des conditions telles que l'existence de fichiers, les comparaisons numériques, et d'autres expressions logiques. Cette commande est souvent utilisée dans les scripts pour contrôler le flux d'exécution.

## Usage
La syntaxe de base de la commande `test` est la suivante :

```bash
test [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `test` :

- `-e [fichier]` : Vérifie si le fichier existe.
- `-d [répertoire]` : Vérifie si le chemin spécifié est un répertoire.
- `-f [fichier]` : Vérifie si le chemin spécifié est un fichier régulier.
- `-z [chaîne]` : Vérifie si la chaîne est vide.
- `-n [chaîne]` : Vérifie si la chaîne n'est pas vide.
- `[valeur1] -eq [valeur2]` : Vérifie si deux valeurs numériques sont égales.
- `[valeur1] -lt [valeur2]` : Vérifie si la première valeur est inférieure à la seconde.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `test` :

1. Vérifier si un fichier existe :

   ```bash
   test -e mon_fichier.txt && echo "Le fichier existe."
   ```

2. Vérifier si un répertoire existe :

   ```bash
   test -d mon_repertoire && echo "C'est un répertoire."
   ```

3. Vérifier si une chaîne est vide :

   ```bash
   ma_chaine=""
   test -z "$ma_chaine" && echo "La chaîne est vide."
   ```

4. Comparer deux nombres :

   ```bash
   a=5
   b=10
   test $a -lt $b && echo "$a est inférieur à $b."
   ```

5. Vérifier si un fichier est un fichier régulier :

   ```bash
   test -f mon_script.sh && echo "C'est un fichier régulier."
   ```

## Tips
- Utilisez `[` et `]` comme une alternative à `test`. Par exemple, `[` est équivalent à `test`, ce qui peut rendre votre code plus lisible.
- N'oubliez pas d'ajouter des espaces autour des opérateurs pour éviter les erreurs de syntaxe.
- Combinez plusieurs tests en utilisant `-a` (et) ou `-o` (ou) pour des vérifications plus complexes.
- Utilisez `if` pour une structure de contrôle plus claire dans vos scripts, par exemple :

   ```bash
   if test -e mon_fichier.txt; then
       echo "Le fichier existe."
   fi
   ```