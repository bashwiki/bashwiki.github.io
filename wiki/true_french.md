# [리눅스] Bash true 사용법

## Overview
La commande `true` est une commande intégrée dans Bash qui ne fait rien et renvoie toujours un code de sortie de 0. Son principal objectif est d'être utilisée dans des scripts ou des pipelines où une commande qui réussit est nécessaire. Cela peut être utile pour des constructions conditionnelles ou des boucles infinies.

## Usage
La syntaxe de base de la commande `true` est très simple :

```bash
true
```

Il n'y a pas d'options ou d'arguments à passer à la commande `true`, car son unique fonction est de retourner un code de sortie de succès (0).

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `true` :

### Exemple 1 : Utilisation dans une boucle
Vous pouvez utiliser `true` dans une boucle infinie pour exécuter des commandes jusqu'à ce qu'une condition soit remplie :

```bash
while true; do
    echo "Cette boucle s'exécute indéfiniment jusqu'à ce qu'elle soit interrompue."
    sleep 1
done
```

### Exemple 2 : Utilisation avec des conditions
Vous pouvez également utiliser `true` pour forcer une condition à être toujours vraie dans un script :

```bash
if true; then
    echo "Cette condition est toujours vraie."
fi
```

## Tips
- Utilisez `true` dans des scripts pour simplifier la logique conditionnelle lorsque vous avez besoin d'une commande qui réussit systématiquement.
- Évitez d'utiliser `true` dans des contextes où une commande ayant un effet réel est nécessaire, car cela pourrait entraîner des comportements inattendus.
- Pour des tests ou des démonstrations, `true` peut être utilisé pour simuler des succès sans exécuter de tâches réelles.