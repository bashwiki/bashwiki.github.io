# [Linux] Bash factor usage : décompose les nombres en facteurs premiers

## Overview
La commande `factor` en Bash est utilisée pour décomposer un ou plusieurs nombres en leurs facteurs premiers. Cela permet d'analyser la structure des nombres et d'effectuer des calculs mathématiques plus complexes.

## Usage
La syntaxe de base de la commande `factor` est la suivante :

```bash
factor [options] [arguments]
```

## Common Options
- `-h`, `--help` : Affiche l'aide et les options disponibles pour la commande.
- `-V`, `--version` : Affiche la version de la commande `factor`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `factor` :

1. **Décomposer un nombre unique :**
   ```bash
   factor 28
   ```
   Sortie :
   ```
   28: 2 2 7
   ```

2. **Décomposer plusieurs nombres :**
   ```bash
   factor 15 21 35
   ```
   Sortie :
   ```
   15: 3 5
   21: 3 7
   35: 5 7
   ```

3. **Utiliser avec des nombres plus grands :**
   ```bash
   factor 1001
   ```
   Sortie :
   ```
   1001: 7 11 13
   ```

## Tips
- Assurez-vous de ne pas entrer de nombres négatifs ou de zéro, car `factor` ne les traite pas.
- Vous pouvez utiliser `factor` en combinaison avec d'autres commandes pour des analyses plus avancées, par exemple en utilisant un pipe pour traiter les résultats.
- Pour une utilisation rapide, n'hésitez pas à consulter l'aide avec `factor --help` pour découvrir d'autres options disponibles.