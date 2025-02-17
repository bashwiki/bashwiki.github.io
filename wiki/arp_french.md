# [Linux] Bash arp Utilisation : Gérer les tables ARP

## Overview
La commande `arp` est utilisée pour afficher et manipuler la table ARP (Address Resolution Protocol) d'un système. Elle permet de résoudre les adresses IP en adresses MAC et vice versa, ce qui est essentiel pour la communication sur un réseau local.

## Usage
La syntaxe de base de la commande `arp` est la suivante :

```bash
arp [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `arp` :

- `-a` : Affiche toutes les entrées de la table ARP.
- `-d <adresse>` : Supprime une entrée spécifique de la table ARP.
- `-s <adresse> <adresse_mac>` : Ajoute une entrée statique à la table ARP.
- `-n` : Affiche les adresses IP sous forme numérique, sans tenter de résoudre les noms d'hôtes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `arp` :

1. **Afficher toutes les entrées de la table ARP :**
   ```bash
   arp -a
   ```

2. **Supprimer une entrée de la table ARP :**
   ```bash
   arp -d 192.168.1.10
   ```

3. **Ajouter une entrée statique à la table ARP :**
   ```bash
   arp -s 192.168.1.20 00:11:22:33:44:55
   ```

4. **Afficher les adresses IP sans résoudre les noms d'hôtes :**
   ```bash
   arp -n
   ```

## Tips
- Utilisez `arp -a` régulièrement pour surveiller les appareils connectés à votre réseau.
- Soyez prudent lorsque vous ajoutez des entrées statiques, car cela peut entraîner des conflits d'adresses si l'adresse IP est déjà utilisée par un autre appareil.
- Pour des diagnostics réseau, combiner `arp` avec d'autres outils comme `ping` ou `traceroute` peut être très utile.