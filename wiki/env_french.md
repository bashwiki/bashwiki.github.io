# [리눅스] Bash env 사용법

## Overview
La commande `env` est utilisée dans les systèmes Unix et Linux pour afficher ou modifier l'environnement d'exécution d'un programme. Son objectif principal est de permettre aux utilisateurs de voir les variables d'environnement actuelles et de lancer des programmes avec un environnement modifié. Cela peut être particulièrement utile pour tester des configurations ou exécuter des scripts dans des environnements spécifiques.

## Usage
La syntaxe de base de la commande `env` est la suivante :

```bash
env [OPTION]... [COMMAND [ARGUMENTS]...]
```

### Options courantes :
- `-i`, `--ignore-environment` : Exécute la commande dans un environnement vide, sans aucune variable d'environnement héritée.
- `-u`, `--unset=VAR` : Supprime la variable d'environnement spécifiée avant d'exécuter la commande.
- `VAR=value` : Définit une variable d'environnement pour la commande qui suit.

## Examples
### Exemple 1 : Afficher les variables d'environnement
Pour afficher toutes les variables d'environnement actuellement définies, vous pouvez simplement exécuter :

```bash
env
```

### Exemple 2 : Exécuter une commande avec une variable d'environnement définie
Pour exécuter une commande avec une variable d'environnement spécifique, vous pouvez utiliser :

```bash
env MY_VAR=HelloWorld bash -c 'echo $MY_VAR'
```
Dans cet exemple, la variable `MY_VAR` est définie sur `HelloWorld`, et la commande `echo` affichera cette valeur.

## Tips
- Utilisez `env` pour tester des scripts dans des environnements spécifiques sans affecter votre environnement global.
- Lorsque vous utilisez `-i`, soyez conscient que cela supprimera toutes les variables d'environnement, ce qui peut affecter le comportement de certaines commandes.
- Pour déboguer des scripts, vous pouvez utiliser `env` pour voir quelles variables d'environnement sont disponibles au moment de l'exécution.