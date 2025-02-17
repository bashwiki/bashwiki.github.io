# [Linux] Bash exit usage : Terminer un script ou une session

## Overview
La commande `exit` est utilisée dans les scripts Bash pour terminer l'exécution d'un script ou d'une session de terminal. Elle permet également de renvoyer un code de sortie qui peut indiquer le succès ou l'échec d'une opération.

## Usage
La syntaxe de base de la commande `exit` est la suivante :

```bash
exit [options] [n]
```

Ici, `n` est un nombre entier qui représente le code de sortie.

## Common Options
- `n` : Un code de sortie numérique. Par convention, un code de sortie de `0` indique un succès, tandis qu'un code différent de `0` indique une erreur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `exit` :

1. Terminer un script avec succès :
   ```bash
   #!/bin/bash
   echo "Script terminé avec succès."
   exit 0
   ```

2. Terminer un script avec une erreur :
   ```bash
   #!/bin/bash
   echo "Une erreur est survenue."
   exit 1
   ```

3. Utiliser exit dans une session interactive :
   ```bash
   exit
   ```

4. Terminer un script après une condition :
   ```bash
   #!/bin/bash
   if [ ! -f "fichier.txt" ]; then
       echo "Le fichier n'existe pas."
       exit 1
   fi
   echo "Le fichier existe."
   exit 0
   ```

## Tips
- Utilisez `exit 0` pour indiquer que votre script s'est exécuté avec succès.
- Utilisez des codes de sortie différents pour différentes erreurs afin de faciliter le débogage.
- N'oubliez pas que `exit` terminera non seulement le script, mais aussi la session de terminal si elle est utilisée dans un terminal interactif.