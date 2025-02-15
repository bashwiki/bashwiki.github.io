# [리눅스] Bash shift 사용법

## Overview
La commande `shift` en Bash est utilisée pour décaler les paramètres positionnels d'un script ou d'une fonction. Son objectif principal est de modifier la position des arguments passés au script, permettant ainsi d'accéder à des paramètres supplémentaires de manière plus simple. En utilisant `shift`, le premier argument devient le second, le second devient le troisième, et ainsi de suite. Cela est particulièrement utile lors du traitement d'un nombre variable d'arguments.

## Usage
La syntaxe de base de la commande `shift` est la suivante :

```bash
shift [n]
```

- `n` : Un entier optionnel qui spécifie le nombre de positions à décaler. Si `n` n'est pas fourni, la valeur par défaut est 1, ce qui signifie que tous les paramètres sont décalés d'une position vers la gauche.

## Examples
Voici quelques exemples pratiques illustrant l'utilisation de la commande `shift`.

### Exemple 1 : Décalage simple
```bash
#!/bin/bash

echo "Avant shift : $1 $2 $3"
shift
echo "Après shift : $1 $2 $3"
```
Dans cet exemple, si le script est exécuté avec trois arguments (par exemple, `./script.sh arg1 arg2 arg3`), la sortie sera :
```
Avant shift : arg1 arg2 arg3
Après shift : arg2 arg3
```

### Exemple 2 : Décalage multiple
```bash
#!/bin/bash

echo "Avant shift : $1 $2 $3 $4"
shift 2
echo "Après shift : $1 $2 $3 $4"
```
Si ce script est exécuté avec quatre arguments (par exemple, `./script.sh arg1 arg2 arg3 arg4`), la sortie sera :
```
Avant shift : arg1 arg2 arg3 arg4
Après shift : arg3 arg4
```

## Tips
- Utilisez `shift` dans des boucles pour traiter des arguments de manière itérative, ce qui peut simplifier le code lorsque vous travaillez avec un grand nombre d'arguments.
- Soyez prudent lorsque vous utilisez `shift` dans des scripts, car il peut entraîner la perte d'arguments si vous ne les gérez pas correctement. Assurez-vous de toujours vérifier le nombre d'arguments restants après le décalage.
- Combinez `shift` avec d'autres commandes comme `getopts` pour gérer des options de ligne de commande plus complexes.