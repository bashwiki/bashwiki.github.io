# [Linux] Bash jq Utilisation : Outil de traitement JSON

## Overview
Le commandement `jq` est un outil puissant en ligne de commande pour traiter et manipuler des données JSON. Il permet de filtrer, transformer et formater des données JSON de manière efficace, ce qui en fait un choix idéal pour les développeurs et les administrateurs système.

## Usage
La syntaxe de base de la commande `jq` est la suivante :

```bash
jq [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `jq` :

- `-c` : Affiche la sortie en format compact.
- `-r` : Renvoie la sortie sous forme de texte brut au lieu de JSON.
- `-f <file>` : Charge les filtres depuis un fichier externe.
- `--slurp` : Lit plusieurs fichiers JSON et les combine en un tableau.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `jq` :

1. **Afficher tout le contenu d'un fichier JSON :**

```bash
jq . fichier.json
```

2. **Filtrer une clé spécifique :**

```bash
jq '.nom' fichier.json
```

3. **Extraire plusieurs clés :**

```bash
jq '{nom: .nom, age: .age}' fichier.json
```

4. **Compter le nombre d'éléments dans un tableau :**

```bash
jq '.utilisateurs | length' fichier.json
```

5. **Convertir la sortie en texte brut :**

```bash
jq -r '.nom' fichier.json
```

## Tips
- Utilisez l'option `-c` pour obtenir une sortie plus compacte, surtout lorsque vous traitez de grandes quantités de données.
- N'hésitez pas à combiner plusieurs filtres pour obtenir des résultats plus complexes.
- Testez vos commandes `jq` dans un terminal interactif pour voir immédiatement les résultats et ajuster vos filtres en conséquence.