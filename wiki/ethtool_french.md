# [리눅스] Bash ethtool 사용법

## Overview
La commande `ethtool` est un utilitaire en ligne de commande utilisé pour interroger et contrôler les paramètres des interfaces réseau Ethernet sous Linux. Son objectif principal est de fournir des informations détaillées sur les capacités de la carte réseau, telles que la vitesse de connexion, le duplex, et d'autres paramètres de configuration. `ethtool` permet également de modifier certains réglages, comme l'activation ou la désactivation de la négociation automatique.

## Usage
La syntaxe de base de la commande `ethtool` est la suivante :

```bash
ethtool [options] <interface>
```

### Options courantes :
- `-h` ou `--help` : Affiche l'aide et les options disponibles.
- `-s` : Permet de modifier les paramètres de l'interface réseau.
- `-i` : Affiche des informations sur le pilote de l'interface.
- `-p` : Fait clignoter les LED de l'interface pour l'identifier.
- `-t` : Lance un test de diagnostic sur l'interface.

## Examples
### Exemple 1 : Afficher les informations de l'interface
Pour afficher les informations de la carte réseau `eth0`, vous pouvez utiliser la commande suivante :

```bash
ethtool eth0
```

Cette commande affichera des détails tels que la vitesse, le duplex, et l'état de la connexion.

### Exemple 2 : Modifier les paramètres de l'interface
Pour désactiver la négociation automatique sur l'interface `eth0` et définir la vitesse à 100 Mbps en mode duplex intégral, utilisez la commande :

```bash
ethtool -s eth0 speed 100 duplex full autoneg off
```

Cette commande configure l'interface avec les paramètres spécifiés.

## Tips
- Assurez-vous d'exécuter `ethtool` avec des privilèges suffisants (souvent en tant que superutilisateur) pour modifier les paramètres de l'interface.
- Utilisez `ethtool -i <interface>` pour vérifier le nom du pilote et la version, ce qui peut être utile pour le dépannage.
- Pour des diagnostics avancés, envisagez d'utiliser `ethtool -t <interface>` pour effectuer des tests de diagnostic sur l'interface réseau.
- Prenez note des paramètres actuels avant de les modifier, afin de pouvoir revenir à une configuration précédente si nécessaire.