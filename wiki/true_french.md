# [Linux] Bash true : Exécuter une commande réussie

## Overview
La commande `true` est une commande simple qui ne fait rien et renvoie toujours un code de sortie de 0, indiquant un succès. Elle est souvent utilisée dans des scripts pour remplir des conditions ou comme un espace réservé.

## Usage
La syntaxe de base de la commande `true` est la suivante :

```bash
true [options] [arguments]
```

Cependant, `true` ne prend généralement pas d'options ou d'arguments.

## Common Options
La commande `true` n'a pas d'options communes, car son unique fonction est de renvoyer un succès. 

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `true` :

### Exemple 1 : Utilisation dans un script
```bash
#!/bin/bash
if true; then
    echo "Cette condition est toujours vraie."
fi
```

### Exemple 2 : Boucle infinie
```bash
while true; do
    echo "Cette boucle tourne indéfiniment."
    sleep 1
done
```

### Exemple 3 : Remplir un espace réservé
```bash
# Utilisation de true comme un espace réservé
command1 || true
command2 || true
```

## Tips
- Utilisez `true` dans des scripts pour créer des conditions qui doivent toujours réussir.
- Combinez `true` avec d'autres commandes pour gérer les erreurs sans interrompre l'exécution du script.
- Évitez d'utiliser `true` dans des scripts critiques où un échec pourrait passer inaperçu.