# [리눅스] Bash getopts 사용법

## Overview
La commande `getopts` est utilisée dans les scripts Bash pour analyser les options de ligne de commande. Elle permet de gérer les arguments passés au script de manière structurée, facilitant ainsi la création de scripts qui acceptent des options et des arguments. `getopts` est particulièrement utile pour les scripts qui nécessitent des options courtes (comme `-a`, `-b`) et peut également être utilisé pour des options longues en combinaison avec d'autres techniques.

## Usage
La syntaxe de base de `getopts` est la suivante :

```bash
getopts "options" variable
```

- **options** : Une chaîne de caractères contenant les options que le script peut accepter. Chaque option peut être suivie d'un deux-points (`:`) si elle nécessite un argument.
- **variable** : Le nom de la variable qui recevra l'option actuelle.

### Exemple d'options
- `a` : option sans argument
- `b:` : option avec un argument

## Examples
Voici quelques exemples pratiques de l'utilisation de `getopts`.

### Exemple 1 : Options simples
```bash
#!/bin/bash

while getopts "ab:" option; do
  case $option in
    a) echo "Option A activée" ;;
    b) echo "Option B activée avec argument : $OPTARG" ;;
    *) echo "Option invalide" ;;
  esac
done
```
Dans cet exemple, le script accepte l'option `-a` sans argument et l'option `-b` avec un argument. Pour exécuter ce script, vous pouvez utiliser la commande suivante :

```bash
./script.sh -a -b valeur
```

### Exemple 2 : Gestion des erreurs
```bash
#!/bin/bash

while getopts "x:y:z:" option; do
  case $option in
    x) echo "Option X avec argument : $OPTARG" ;;
    y) echo "Option Y avec argument : $OPTARG" ;;
    z) echo "Option Z avec argument : $OPTARG" ;;
    *) echo "Usage: $0 [-x arg] [-y arg] [-z arg]" ;;
  esac
done
```
Dans cet exemple, si une option invalide est fournie, le script affiche un message d'utilisation.

## Tips
- **Utilisez `OPTIND`** : Après avoir utilisé `getopts`, vous pouvez réinitialiser l'index des options avec `OPTIND=1` si vous souhaitez analyser à nouveau les options.
- **Gestion des arguments** : Assurez-vous de vérifier si les options qui nécessitent des arguments sont fournies avec un argument valide.
- **Boucle infinie** : Utilisez une boucle `while` pour continuer à traiter les options jusqu'à ce qu'il n'y en ait plus à analyser.
- **Documentation** : Documentez toujours les options acceptées par votre script pour faciliter son utilisation par d'autres développeurs.

En suivant ces conseils, vous pouvez créer des scripts Bash robustes et faciles à utiliser en utilisant `getopts`.