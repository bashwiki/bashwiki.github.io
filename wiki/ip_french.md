# [Linux] Bash ip utilisation : Gérer les adresses IP et les interfaces réseau

## Overview
La commande `ip` est un outil puissant utilisé pour gérer les interfaces réseau, les adresses IP, les routes et d'autres aspects de la configuration réseau sur les systèmes Linux. Elle remplace les anciennes commandes comme `ifconfig` et `route`.

## Usage
La syntaxe de base de la commande `ip` est la suivante :

```bash
ip [options] [arguments]
```

## Common Options
Voici quelques options courantes de la commande `ip` :

- `addr` : Gérer les adresses IP.
- `link` : Gérer les interfaces réseau.
- `route` : Gérer les tables de routage.
- `neigh` : Gérer les entrées de la table ARP.
- `monitor` : Surveiller les changements dans l'état des interfaces ou des adresses.

## Common Examples

### Afficher les interfaces réseau
Pour lister toutes les interfaces réseau disponibles sur le système, utilisez :

```bash
ip link show
```

### Afficher les adresses IP
Pour afficher les adresses IP configurées sur toutes les interfaces, utilisez :

```bash
ip addr show
```

### Ajouter une adresse IP à une interface
Pour ajouter une adresse IP à une interface spécifique, par exemple `eth0`, utilisez :

```bash
ip addr add 192.168.1.100/24 dev eth0
```

### Supprimer une adresse IP d'une interface
Pour supprimer une adresse IP d'une interface, par exemple `eth0`, utilisez :

```bash
ip addr del 192.168.1.100/24 dev eth0
```

### Afficher la table de routage
Pour afficher la table de routage actuelle, utilisez :

```bash
ip route show
```

## Tips
- Utilisez `ip -h` pour afficher l'aide et obtenir des informations sur les options disponibles.
- Combinez les commandes avec `grep` pour filtrer les résultats, par exemple : `ip addr show | grep 192.168`.
- Pensez à exécuter la commande avec des privilèges élevés (par exemple, en utilisant `sudo`) si vous devez apporter des modifications à la configuration réseau.