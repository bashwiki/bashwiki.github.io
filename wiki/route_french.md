# [리눅스] Bash route 사용법

## Overview
La commande `route` est utilisée pour afficher et manipuler la table de routage IP du système. Elle permet aux utilisateurs de gérer les routes réseau, ce qui est essentiel pour le bon fonctionnement des communications entre différents réseaux. En utilisant `route`, les ingénieurs et développeurs peuvent ajouter, supprimer ou modifier des routes, facilitant ainsi la gestion du trafic réseau.

## Usage
La syntaxe de base de la commande `route` est la suivante :

```
route [OPTION] [ARGUMENTS]
```

### Options courantes :
- `-n` : Affiche les adresses IP sous forme numérique au lieu de tenter de résoudre les noms d'hôtes.
- `add` : Ajoute une nouvelle route à la table de routage.
- `del` : Supprime une route existante de la table de routage.
- `-net` : Indique que l'argument suivant est un réseau.
- `-host` : Indique que l'argument suivant est un hôte.

## Examples
### Exemple 1 : Afficher la table de routage
Pour afficher la table de routage actuelle sans tenter de résoudre les noms d'hôtes, vous pouvez utiliser la commande suivante :

```bash
route -n
```

### Exemple 2 : Ajouter une nouvelle route
Pour ajouter une route vers un réseau spécifique, utilisez la commande suivante. Par exemple, pour ajouter une route vers le réseau 192.168.1.0 avec une passerelle 192.168.0.1 :

```bash
route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.0.1
```

### Exemple 3 : Supprimer une route
Pour supprimer la route que nous venons d'ajouter, vous pouvez exécuter :

```bash
route del -net 192.168.1.0
```

## Tips
- **Vérifiez toujours votre table de routage** : Avant d'ajouter ou de supprimer des routes, il est bon de vérifier la table de routage actuelle pour éviter les conflits.
- **Utilisez `-n` pour des résultats plus rapides** : L'option `-n` peut accélérer l'affichage de la table de routage en évitant la résolution des noms d'hôtes.
- **Soyez prudent avec les modifications** : Les modifications apportées à la table de routage peuvent affecter la connectivité réseau. Assurez-vous de comprendre les implications de chaque changement avant de l'appliquer.