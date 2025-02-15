# [리눅스] Bash fc 사용법

## Overview
La commande `fc` (fix command) dans Bash est utilisée pour rappeler, modifier et réexécuter des commandes précédemment exécutées dans la session de terminal actuelle. Son principal objectif est de faciliter la correction et la réutilisation des commandes, ce qui peut améliorer l'efficacité lors du travail dans le shell.

## Usage
La syntaxe de base de la commande `fc` est la suivante :

```bash
fc [options] [first] [last]
```

### Options courantes :
- `-l` : Liste les commandes dans l'historique. Par défaut, elle affiche les 16 dernières commandes.
- `-r` : Inverse l'ordre des commandes affichées ou exécutées.
- `-s` : Exécute la commande sans l'afficher dans l'éditeur.
- `-n` : Ne pas afficher les numéros de ligne lors de la liste des commandes.

## Examples
### Exemple 1 : Lister les commandes précédentes
Pour afficher les 10 dernières commandes de l'historique, vous pouvez utiliser :

```bash
fc -l -n 1 10
```

Cela affichera les commandes sans les numéros de ligne.

### Exemple 2 : Modifier et réexécuter une commande
Si vous souhaitez modifier la dernière commande exécutée, vous pouvez simplement utiliser :

```bash
fc
```

Cela ouvrira l'éditeur de texte par défaut avec la dernière commande. Après avoir effectué les modifications, enregistrez et fermez l'éditeur pour exécuter la commande modifiée.

## Tips
- Utilisez `fc -l` pour rapidement parcourir votre historique et identifier les commandes que vous souhaitez réutiliser ou modifier.
- Si vous travaillez souvent avec des commandes longues, envisagez d'utiliser `fc` en combinaison avec des éditeurs comme `vim` ou `nano` pour une édition plus facile.
- N'oubliez pas que `fc` ne fonctionne que pour les commandes de la session actuelle. Si vous fermez le terminal, l'historique sera perdu à moins qu'il ne soit enregistré dans le fichier d'historique de Bash.