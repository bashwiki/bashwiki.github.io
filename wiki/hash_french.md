# [Linux] Bash hash utilisation : Gérer le cache des commandes

## Overview
La commande `hash` en Bash est utilisée pour gérer le cache des commandes exécutées. Elle permet de mémoriser les chemins des commandes pour accélérer leur exécution lors des appels futurs. Cela évite de rechercher à chaque fois le chemin complet des exécutables.

## Usage
La syntaxe de base de la commande `hash` est la suivante :

```bash
hash [options] [arguments]
```

## Common Options
- `-r` : Réinitialise le cache des commandes, supprimant toutes les entrées mémorisées.
- `-p` : Spécifie un chemin pour une commande donnée, permettant de forcer l'utilisation de ce chemin.
- `-l` : Affiche la liste des commandes mémorisées dans le cache.

## Common Examples

### Afficher le cache des commandes
Pour voir les commandes actuellement mémorisées dans le cache, utilisez :

```bash
hash
```

### Réinitialiser le cache
Pour vider le cache des commandes, exécutez :

```bash
hash -r
```

### Spécifier un chemin pour une commande
Pour ajouter une commande avec un chemin spécifique, utilisez :

```bash
hash -p /usr/local/bin/ma_commande ma_commande
```

### Lister les commandes mémorisées
Pour afficher toutes les commandes mémorisées, utilisez :

```bash
hash -l
```

## Tips
- Utilisez `hash` après avoir installé de nouveaux programmes pour vous assurer que Bash utilise le bon chemin.
- Vérifiez régulièrement le cache avec `hash -l` pour éviter d'utiliser des chemins obsolètes.
- Si vous rencontrez des problèmes avec des commandes non trouvées, essayez de réinitialiser le cache avec `hash -r`.