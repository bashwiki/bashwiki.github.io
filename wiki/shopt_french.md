# [리눅스] Bash shopt 사용법

## Overview
La commande `shopt` est un outil dans Bash qui permet de modifier les options de comportement du shell. Elle est principalement utilisée pour activer ou désactiver des fonctionnalités spécifiques du shell, ce qui peut influencer la manière dont les commandes sont interprétées et exécutées. Cela permet aux utilisateurs de personnaliser leur environnement de travail en fonction de leurs besoins.

## Usage
La syntaxe de base de la commande `shopt` est la suivante :

```bash
shopt [options] [option_name]
```

### Options courantes :
- `-s` : Active une option spécifiée.
- `-u` : Désactive une option spécifiée.
- `-p` : Affiche les options actuellement définies avec leur état (activé ou désactivé).

## Examples
### Exemple 1 : Activer l'option `cdable_vars`
Cette option permet d'utiliser des variables dans les commandes `cd`. Par exemple, si vous avez une variable d'environnement `DIR`, vous pouvez faire :

```bash
shopt -s cdable_vars
DIR="/path/to/directory"
cd DIR  # Cela vous amènera à /path/to/directory
```

### Exemple 2 : Afficher toutes les options
Pour voir toutes les options disponibles et leur état actuel, vous pouvez utiliser :

```bash
shopt -p
```

Cela affichera une liste de toutes les options, vous permettant de vérifier lesquelles sont activées ou désactivées.

## Tips
- Utilisez `shopt -p` pour faire un audit de vos options actuelles avant de modifier quoi que ce soit. Cela vous aidera à comprendre l'impact de vos changements.
- Gardez à l'esprit que certaines options peuvent avoir des effets significatifs sur le comportement de votre shell. Il est donc conseillé de lire la documentation ou d'expérimenter dans un environnement contrôlé avant de les activer dans vos scripts de production.
- Vous pouvez ajouter des commandes `shopt` dans votre fichier `.bashrc` pour que vos préférences soient appliquées à chaque nouvelle session de terminal.