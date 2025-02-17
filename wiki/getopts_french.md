# [Linux] Bash getopts : [traitement des options de ligne de commande]

## Overview
La commande `getopts` est utilisée dans les scripts Bash pour analyser les options et les arguments de ligne de commande. Elle permet de gérer facilement les options courtes et de valider les entrées fournies par l'utilisateur.

## Usage
La syntaxe de base de la commande `getopts` est la suivante :

```bash
getopts [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `getopts` :

- `-a` : Permet de spécifier un argument pour une option.
- `-b` : Utilisé pour activer une fonctionnalité spécifique dans le script.
- `-c` : Indique que l'option nécessite un argument.

## Common Examples

### Exemple 1 : Options simples
```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "Option A activée"
      ;;
    b)
      echo "Option B avec argument : $OPTARG"
      ;;
    c)
      echo "Option C avec argument : $OPTARG"
      ;;
    \?)
      echo "Option invalide : -$OPTARG" >&2
      ;;
  esac
done
```

### Exemple 2 : Utilisation avec des arguments
```bash
#!/bin/bash

while getopts "f:o:" opt; do
  case $opt in
    f)
      echo "Fichier source : $OPTARG"
      ;;
    o)
      echo "Fichier de sortie : $OPTARG"
      ;;
    \?)
      echo "Option invalide : -$OPTARG" >&2
      ;;
  esac
done
```

### Exemple 3 : Gestion des options multiples
```bash
#!/bin/bash

while getopts "x:y:z:" opt; do
  case $opt in
    x)
      echo "Option X : $OPTARG"
      ;;
    y)
      echo "Option Y : $OPTARG"
      ;;
    z)
      echo "Option Z : $OPTARG"
      ;;
    \?)
      echo "Option invalide : -$OPTARG" >&2
      ;;
  esac
done
```

## Tips
- Utilisez des options courtes pour simplifier l'utilisation de votre script.
- N'oubliez pas de gérer les options invalides pour améliorer l'expérience utilisateur.
- Testez toujours votre script avec différentes combinaisons d'options pour vous assurer qu'il fonctionne comme prévu.