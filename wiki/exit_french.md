# [리눅스] Bash exit 사용법

## Overview
La commande `exit` dans Bash est utilisée pour quitter un shell ou un script en cours d'exécution. Elle permet de terminer le processus en cours et de retourner un code de sortie à l'environnement appelant. Ce code de sortie est un entier qui indique si le script ou la commande s'est terminé avec succès ou s'il y a eu une erreur. Par convention, un code de sortie de `0` indique un succès, tandis qu'un code différent de `0` indique une erreur.

## Usage
La syntaxe de base de la commande `exit` est la suivante :

```bash
exit [n]
```

Où `n` est un entier optionnel qui représente le code de sortie. Si aucun code n'est spécifié, le code de sortie sera celui de la dernière commande exécutée.

### Options courantes
- `n`: Un entier qui définit le code de sortie. Par exemple, `exit 1` indique une erreur, tandis que `exit 0` indique un succès.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `exit`.

### Exemple 1 : Quitter un script avec succès
```bash
#!/bin/bash
echo "Exécution du script..."
# Code du script ici
exit 0
```
Dans cet exemple, le script s'exécute et se termine avec succès en renvoyant le code de sortie `0`.

### Exemple 2 : Quitter un script avec une erreur
```bash
#!/bin/bash
echo "Une erreur s'est produite."
exit 1
```
Ici, le script signale une erreur et se termine avec le code de sortie `1`.

## Tips
- Utilisez toujours des codes de sortie explicites pour faciliter le débogage. Cela permet aux utilisateurs de comprendre rapidement si un script a réussi ou échoué.
- Lorsque vous écrivez des scripts complexes, envisagez d'utiliser des codes de sortie différents pour différents types d'erreurs. Cela peut aider à diagnostiquer des problèmes plus facilement.
- N'oubliez pas que la commande `exit` ne peut être utilisée que dans un shell interactif ou un script. Dans un terminal, elle fermera simplement le shell en cours.