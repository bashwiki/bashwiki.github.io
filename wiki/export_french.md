# [Linux] Bash export : Gérer les variables d'environnement

## Overview
La commande `export` en Bash est utilisée pour définir des variables d'environnement qui seront accessibles aux processus enfants. Cela permet de partager des informations entre différents programmes exécutés dans le même shell.

## Usage
La syntaxe de base de la commande `export` est la suivante :

```bash
export [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `export` :

- `-n` : Supprime l'exportation d'une variable, la rendant non disponible pour les processus enfants.
- `-p` : Affiche toutes les variables d'environnement exportées.

## Common Examples

### Exporter une variable
Pour créer une variable d'environnement et la rendre accessible aux processus enfants, utilisez :

```bash
export NOM_VARIABLE="valeur"
```

### Vérifier les variables exportées
Pour afficher toutes les variables d'environnement exportées, utilisez :

```bash
export -p
```

### Supprimer l'exportation d'une variable
Pour rendre une variable non exportée, utilisez :

```bash
export -n NOM_VARIABLE
```

### Utiliser une variable exportée dans un script
Si vous avez exporté une variable, vous pouvez l'utiliser dans un script comme ceci :

```bash
#!/bin/bash
export MON_VARIABLE="Bonjour"
bash -c 'echo $MON_VARIABLE'  # Affiche "Bonjour"
```

## Tips
- Utilisez `export` pour rendre les variables d'environnement disponibles dans les scripts ou les sous-shells.
- Vérifiez régulièrement les variables exportées avec `export -p` pour éviter les conflits.
- Évitez d'utiliser des noms de variables qui pourraient entrer en conflit avec des commandes ou des variables système.