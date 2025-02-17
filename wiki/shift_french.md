# [Linux] Bash shift usage : Décale les paramètres positionnels

## Overview
La commande `shift` en Bash est utilisée pour décaler les paramètres positionnels vers la gauche. Cela signifie que le premier paramètre devient le second, le second devient le troisième, et ainsi de suite. Cela est particulièrement utile dans les scripts où vous souhaitez traiter les arguments un par un.

## Usage
La syntaxe de base de la commande `shift` est la suivante :

```bash
shift [n]
```

Ici, `n` est un nombre optionnel qui indique combien de positions vous souhaitez décaler. Si `n` n'est pas spécifié, le décalage par défaut est de 1.

## Common Options
- `n` : Un nombre qui spécifie le nombre de positions à décaler. Si omis, décalage de 1.

## Common Examples

### Exemple 1 : Décalage simple
```bash
#!/bin/bash
echo "Avant shift: $1 $2 $3"
shift
echo "Après shift: $1 $2 $3"
```
Dans cet exemple, le premier argument est décalé, et `$2` devient `$1`, `$3` devient `$2`, et la variable `$3` devient vide.

### Exemple 2 : Décalage de plusieurs positions
```bash
#!/bin/bash
echo "Avant shift: $1 $2 $3 $4"
shift 2
echo "Après shift: $1 $2 $3 $4"
```
Ici, les deux premiers arguments sont décalés, laissant `$3` comme nouveau `$1` et `$4` comme nouveau `$2`.

### Exemple 3 : Utilisation dans une boucle
```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Traitement de l'argument: $1"
    shift
done
```
Cet exemple montre comment utiliser `shift` dans une boucle pour traiter tous les arguments un par un jusqu'à ce qu'il n'en reste plus.

## Tips
- Utilisez `shift` lorsque vous traitez des scripts avec de nombreux arguments pour simplifier la gestion des paramètres.
- Soyez prudent avec le nombre de décalages que vous effectuez pour éviter de perdre des arguments importants.
- Combinez `shift` avec des structures de contrôle comme des boucles pour un traitement efficace des arguments.