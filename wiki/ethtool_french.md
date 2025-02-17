# [Linux] Bash ethtool : Outil pour interroger et configurer les interfaces réseau

## Overview
La commande `ethtool` est un utilitaire en ligne de commande utilisé pour interroger et configurer les paramètres des interfaces réseau Ethernet sous Linux. Elle permet d'obtenir des informations détaillées sur les interfaces, de modifier leurs paramètres et de diagnostiquer des problèmes de réseau.

## Usage
La syntaxe de base de la commande `ethtool` est la suivante :

```bash
ethtool [options] [arguments]
```

## Common Options
Voici quelques options courantes de `ethtool` avec de brèves explications :

- `-i` : Affiche les informations du pilote de l'interface réseau.
- `-s` : Modifie les paramètres de l'interface réseau.
- `-p` : Fait clignoter le port de l'interface pendant un certain temps pour l'identifier.
- `-t` : Exécute des tests de diagnostic sur l'interface.
- `-S` : Affiche les statistiques de l'interface réseau.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `ethtool` :

1. **Afficher les informations de base sur une interface réseau :**

   ```bash
   ethtool eth0
   ```

2. **Afficher les informations du pilote de l'interface :**

   ```bash
   ethtool -i eth0
   ```

3. **Modifier la vitesse et le mode duplex de l'interface :**

   ```bash
   ethtool -s eth0 speed 100 duplex full
   ```

4. **Faire clignoter le port de l'interface pendant 10 secondes :**

   ```bash
   ethtool -p eth0 10
   ```

5. **Afficher les statistiques de l'interface :**

   ```bash
   ethtool -S eth0
   ```

## Tips
- Assurez-vous d'exécuter `ethtool` avec des privilèges suffisants (souvent en tant que superutilisateur) pour modifier les paramètres de l'interface.
- Utilisez `ethtool` en combinaison avec d'autres commandes comme `ifconfig` ou `ip` pour obtenir une vue d'ensemble complète de la configuration réseau.
- Consultez la page de manuel (`man ethtool`) pour explorer toutes les options disponibles et approfondir votre compréhension de cet outil puissant.