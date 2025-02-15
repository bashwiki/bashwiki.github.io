# [리눅스] Bash source 사용법

## Overview
La commande `source` dans Bash est utilisée pour exécuter des commandes à partir d'un fichier dans le contexte de l'environnement actuel du shell. Cela signifie que les variables définies ou modifiées dans le fichier source affecteront l'environnement du shell courant, contrairement à l'exécution d'un script de manière classique, qui créerait un nouveau sous-shell.

## Usage
La syntaxe de base de la commande `source` est la suivante :

```bash
source FICHIER
```

ou, de manière équivalente :

```bash
. FICHIER
```

### Options courantes
La commande `source` ne possède pas d'options spécifiques, mais il est important de noter que le fichier doit être un script exécutable ou un fichier contenant des commandes Bash valides.

## Examples
### Exemple 1 : Charger un fichier de configuration
Supposons que vous ayez un fichier de configuration `config.sh` qui définit plusieurs variables d'environnement. Vous pouvez le charger dans votre shell actuel avec :

```bash
source config.sh
```

Après avoir exécuté cette commande, toutes les variables définies dans `config.sh` seront disponibles dans votre shell.

### Exemple 2 : Exécuter des fonctions définies dans un script
Imaginons que vous ayez un fichier `functions.sh` contenant des fonctions Bash. Pour les rendre disponibles dans votre session actuelle, vous pouvez faire :

```bash
source functions.sh
```

Vous pourrez ensuite appeler les fonctions définies dans `functions.sh` directement dans votre terminal.

## Tips
- Utilisez `source` pour charger des fichiers de configuration ou des scripts contenant des fonctions que vous souhaitez utiliser dans votre session actuelle.
- Évitez d'utiliser `source` pour des scripts qui ne sont pas destinés à être exécutés dans le contexte du shell actuel, car cela pourrait entraîner des effets indésirables sur votre environnement.
- Pour vérifier si un fichier est correctement chargé, vous pouvez afficher une variable définie dans le fichier après l'avoir sourcé.