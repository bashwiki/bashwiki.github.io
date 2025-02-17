# [Linux] Bash source : Exécuter des scripts dans le shell courant

## Overview
La commande `source` permet d'exécuter des scripts shell dans le contexte du shell courant. Cela signifie que les variables et les fonctions définies dans le script restent disponibles après son exécution, contrairement à l'exécution d'un script en tant que processus séparé.

## Usage
La syntaxe de base de la commande `source` est la suivante :

```bash
source [options] [arguments]
```

## Common Options
- `-h`, `--help` : Affiche l'aide et les options disponibles pour la commande.
- `-V`, `--version` : Affiche la version de la commande.

## Common Examples

### Exécuter un script
Pour exécuter un script nommé `script.sh`, utilisez la commande suivante :

```bash
source script.sh
```

### Charger des variables d'environnement
Supposons que vous ayez un fichier `env.sh` qui définit des variables d'environnement. Vous pouvez les charger dans votre session actuelle avec :

```bash
source env.sh
```

### Définir des fonctions
Si vous avez un script qui définit des fonctions, vous pouvez les rendre disponibles dans votre shell en utilisant :

```bash
source functions.sh
```

### Recharger un script après modification
Après avoir modifié un script, vous pouvez le recharger sans quitter votre session en utilisant :

```bash
source script.sh
```

## Tips
- Utilisez `source` plutôt que `./script.sh` lorsque vous souhaitez que les modifications apportées aux variables ou fonctions soient disponibles dans votre session actuelle.
- Pour éviter les erreurs, assurez-vous que le script que vous sourcez a les permissions d'exécution appropriées.
- Il est courant de placer des commandes `source` dans votre fichier `.bashrc` ou `.bash_profile` pour charger automatiquement des configurations à chaque ouverture de terminal.