# [리눅스] Bash jq 사용법

## Overview
`jq` est un outil en ligne de commande léger et flexible pour le traitement et la manipulation de données JSON. Il permet aux utilisateurs de lire, écrire et transformer des données JSON de manière efficace. `jq` est particulièrement utile pour les développeurs et les ingénieurs qui travaillent avec des API ou des fichiers de configuration en JSON, car il facilite l'extraction et la manipulation des données.

## Usage
La syntaxe de base de la commande `jq` est la suivante :

```bash
jq [options] 'expression' fichier.json
```

### Options courantes :
- `-c` : Produit une sortie compactée (sans espaces inutiles).
- `-r` : Renvoie les résultats sous forme de texte brut au lieu de JSON.
- `-f fichier.jq` : Charge des expressions `jq` à partir d'un fichier externe.
- `--arg nom valeur` : Définit une variable dans l'expression `jq`.

## Examples
### Exemple 1 : Extraction d'une valeur
Supposons que vous ayez un fichier JSON nommé `data.json` contenant les informations suivantes :

```json
{
  "nom": "Alice",
  "age": 30,
  "ville": "Paris"
}
```

Pour extraire le nom, vous pouvez utiliser la commande suivante :

```bash
jq '.nom' data.json
```

Cela renverra :

```
"Alice"
```

### Exemple 2 : Filtrer un tableau
Considérons un fichier JSON `users.json` avec le contenu suivant :

```json
[
  {"nom": "Alice", "age": 30},
  {"nom": "Bob", "age": 25},
  {"nom": "Charlie", "age": 35}
]
```

Pour obtenir les utilisateurs âgés de plus de 30 ans, utilisez :

```bash
jq '.[] | select(.age > 30)' users.json
```

La sortie sera :

```json
{"nom": "Charlie", "age": 35}
```

## Tips
- Utilisez l'option `-r` pour obtenir des résultats au format texte brut lorsque vous souhaitez utiliser les données dans d'autres commandes ou scripts.
- Familiarisez-vous avec la syntaxe de `jq`, car elle offre une grande puissance pour la manipulation des données JSON. Vous pouvez combiner plusieurs filtres et expressions pour des transformations complexes.
- Testez vos expressions `jq` dans un environnement interactif ou en utilisant des fichiers d'exemple pour vous assurer qu'elles fonctionnent comme prévu avant de les intégrer dans des scripts.