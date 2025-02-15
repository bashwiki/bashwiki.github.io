# [리눅스] Bash ip 사용법

## Overview
La commande `ip` est un outil puissant utilisé pour gérer les interfaces réseau sur les systèmes Linux. Elle fait partie de la suite d'outils iproute2 et remplace les anciennes commandes comme `ifconfig` et `route`. Le but principal de la commande `ip` est de fournir une interface pour configurer, surveiller et gérer les paramètres réseau, y compris les adresses IP, les routes et les interfaces.

## Usage
La syntaxe de base de la commande `ip` est la suivante :

```
ip [OPTIONS] OBJECT { COMMAND | help }
```

### Options courantes :
- `link` : Gérer les interfaces réseau.
- `addr` : Gérer les adresses IP.
- `route` : Gérer les tables de routage.
- `neigh` : Gérer les entrées de la table ARP.

## Examples
### Exemple 1 : Afficher les interfaces réseau
Pour afficher toutes les interfaces réseau et leurs paramètres, vous pouvez utiliser la commande suivante :

```bash
ip link show
```

Cette commande liste toutes les interfaces réseau disponibles sur le système, y compris leur état (up ou down).

### Exemple 2 : Ajouter une adresse IP à une interface
Pour ajouter une adresse IP à une interface spécifique (par exemple, `eth0`), utilisez la commande suivante :

```bash
sudo ip addr add 192.168.1.10/24 dev eth0
```

Cette commande attribue l'adresse IP `192.168.1.10` avec un masque de sous-réseau de `24` à l'interface `eth0`.

## Tips
- Utilisez `ip help` pour obtenir une liste complète des sous-commandes et options disponibles.
- Pour des opérations nécessitant des privilèges élevés, n'oubliez pas d'utiliser `sudo`.
- Familiarisez-vous avec les différentes sous-commandes (`link`, `addr`, `route`, etc.) pour tirer le meilleur parti de la commande `ip`.
- Utilisez `ip -s` pour afficher des statistiques supplémentaires sur les interfaces et les routes, ce qui peut être utile pour le dépannage.