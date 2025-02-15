# [리눅스] Bash awk 사용법

## Overview
`awk` est un puissant langage de programmation et un outil de traitement de texte utilisé principalement pour manipuler et analyser des fichiers texte. Son nom provient des initiales de ses créateurs : Alfred Aho, Peter Weinberger et Brian Kernighan. `awk` est particulièrement efficace pour traiter des données structurées, comme celles trouvées dans des fichiers CSV ou des rapports générés par d'autres programmes. Il permet de filtrer, transformer et extraire des informations spécifiques en fonction de critères définis par l'utilisateur.

## Usage
La syntaxe de base de la commande `awk` est la suivante :

```bash
awk 'pattern { action }' fichier
```

- **pattern** : Une expression qui détermine quelles lignes du fichier seront traitées. Si le motif est omis, `awk` traite toutes les lignes.
- **action** : Une série d'instructions à exécuter sur les lignes qui correspondent au motif. Si l'action est omise, `awk` imprime simplement les lignes correspondantes.
- **fichier** : Le nom du fichier texte à traiter. Si aucun fichier n'est spécifié, `awk` lit l'entrée standard.

### Options courantes
- `-F` : Définit le séparateur de champ. Par défaut, `awk` utilise des espaces ou des tabulations.
- `-v` : Permet de définir des variables d'environnement pour une utilisation dans le script `awk`.

## Examples
### Exemple 1 : Afficher la première colonne d'un fichier
Supposons que nous ayons un fichier `data.txt` contenant les lignes suivantes :

```
Alice 30
Bob 25
Charlie 35
```

Pour afficher uniquement la première colonne (les noms), vous pouvez utiliser la commande suivante :

```bash
awk '{ print $1 }' data.txt
```

### Exemple 2 : Filtrer les lignes en fonction d'une condition
Pour afficher les lignes où l'âge est supérieur à 30, vous pouvez utiliser :

```bash
awk '$2 > 30 { print $1 }' data.txt
```

Cela affichera :

```
Charlie
```

## Tips
- Utilisez le séparateur de champ `-F` pour traiter des fichiers avec des délimiteurs spécifiques, comme des virgules ou des points-virgules.
- Écrivez des scripts `awk` dans des fichiers séparés pour des traitements plus complexes, puis exécutez-les avec `awk -f script.awk fichier`.
- Profitez des variables intégrées comme `NR` (numéro de ligne) et `NF` (nombre de champs) pour des analyses plus avancées.
- Testez vos commandes `awk` dans un terminal avant de les intégrer dans des scripts pour vous assurer qu'elles fonctionnent comme prévu.