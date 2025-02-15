# [리눅스] Bash arp 사용법

## Overview
La commande `arp` est utilisée pour manipuler la table ARP (Address Resolution Protocol) sur un système. Son objectif principal est de permettre aux utilisateurs de visualiser et de gérer les adresses IP et leurs correspondances avec les adresses MAC sur un réseau local. Cela est particulièrement utile pour le dépannage des problèmes de connectivité réseau et pour la gestion des appareils sur un réseau.

## Usage
La syntaxe de base de la commande `arp` est la suivante :

```
arp [options] [hostname]
```

### Options courantes :
- `-a` : Affiche toutes les entrées de la table ARP.
- `-d hostname` : Supprime l'entrée ARP pour l'hôte spécifié.
- `-s hostname hw_addr` : Ajoute une entrée ARP statique pour l'hôte spécifié avec l'adresse matérielle donnée.
- `-n` : Affiche les adresses IP sous forme numérique, sans tenter de résoudre les noms d'hôtes.

## Examples
### Exemple 1 : Afficher la table ARP
Pour afficher toutes les entrées de la table ARP, vous pouvez utiliser la commande suivante :

```bash
arp -a
```

Cette commande listera toutes les adresses IP et leurs correspondances MAC sur le réseau local.

### Exemple 2 : Ajouter une entrée ARP statique
Pour ajouter une entrée ARP statique, utilisez la commande suivante :

```bash
arp -s 192.168.1.10 00:1A:2B:3C:4D:5E
```

Dans cet exemple, nous ajoutons une entrée ARP pour l'adresse IP `192.168.1.10` avec l'adresse MAC `00:1A:2B:3C:4D:5E`.

## Tips
- Utilisez l'option `-n` si vous souhaitez éviter la résolution de noms d'hôtes, ce qui peut accélérer l'affichage des résultats.
- Soyez prudent lorsque vous utilisez l'option `-d` pour supprimer des entrées, car cela peut affecter la connectivité réseau des appareils concernés.
- Les entrées ARP statiques peuvent être utiles pour éviter les conflits d'adresses IP et assurer une communication fiable avec des appareils spécifiques sur le réseau.