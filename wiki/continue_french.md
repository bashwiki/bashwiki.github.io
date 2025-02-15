# [리눅스] Bash continue 사용법

## Overview
La commande `continue` en Bash est utilisée dans le contexte des boucles. Son rôle principal est de sauter le reste des instructions dans l'itération courante d'une boucle et de passer directement à l'itération suivante. Cela est particulièrement utile lorsque vous souhaitez ignorer certaines conditions ou valeurs sans sortir complètement de la boucle.

## Usage
La syntaxe de base de la commande `continue` est la suivante :

```bash
continue [N]
```

- `N` (optionnel) : Si spécifié, `N` indique le nombre de niveaux de boucles à sauter. Par défaut, `continue` affecte la boucle la plus interne.

## Examples
Voici quelques exemples pratiques illustrant l'utilisation de la commande `continue`.

### Exemple 1 : Ignorer les nombres pairs
Dans cet exemple, nous allons utiliser `continue` pour ignorer les nombres pairs dans une boucle `for`.

```bash
for i in {1..10}; do
    if (( i % 2 == 0 )); then
        continue
    fi
    echo "Nombre impair : $i"
done
```
Dans ce script, les nombres pairs ne seront pas affichés. Seuls les nombres impairs seront imprimés.

### Exemple 2 : Sauter des fichiers spécifiques
Supposons que vous souhaitiez traiter tous les fichiers d'un répertoire, mais que vous souhaitiez ignorer les fichiers temporaires. Voici comment vous pourriez le faire :

```bash
for file in *; do
    if [[ $file == *.tmp ]]; then
        continue
    fi
    echo "Traitement du fichier : $file"
done
```
Dans cet exemple, tous les fichiers avec l'extension `.tmp` seront ignorés, et seul le traitement des autres fichiers sera effectué.

## Tips
- Utilisez `continue` pour rendre votre code plus lisible en évitant des structures conditionnelles complexes.
- Soyez prudent avec l'utilisation de `continue` dans des boucles imbriquées, car il affecte uniquement la boucle la plus interne par défaut. Si vous devez sauter plusieurs niveaux, spécifiez le nombre approprié.
- Testez toujours votre script avec des données d'entrée variées pour vous assurer que la logique de saut fonctionne comme prévu.

En suivant ces conseils, vous pourrez utiliser efficacement la commande `continue` dans vos scripts Bash.