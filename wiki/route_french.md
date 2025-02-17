# [Linux] Bash route usage : gérer les tables de routage

## Overview
La commande `route` est utilisée pour afficher et manipuler la table de routage IP du noyau. Elle permet de configurer les routes réseau, ce qui est essentiel pour le bon fonctionnement des communications entre différents réseaux.

## Usage
La syntaxe de base de la commande `route` est la suivante :

```
route [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `route` :

- `-n` : Affiche les adresses IP au lieu des noms d'hôtes pour une sortie plus rapide.
- `add` : Ajoute une nouvelle route à la table de routage.
- `del` : Supprime une route existante de la table de routage.
- `-net` : Indique que l'argument suivant est un réseau.
- `-host` : Indique que l'argument suivant est un hôte.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `route` :

1. **Afficher la table de routage actuelle :**
   ```bash
   route -n
   ```

2. **Ajouter une route vers un réseau spécifique :**
   ```bash
   route add -net 192.168.1.0/24 gw 192.168.0.1
   ```

3. **Supprimer une route existante :**
   ```bash
   route del -net 192.168.1.0/24
   ```

4. **Ajouter une route vers un hôte spécifique :**
   ```bash
   route add -host 10.0.0.5 gw 192.168.0.1
   ```

## Tips
- Utilisez l'option `-n` pour obtenir des résultats plus rapides, surtout si vous avez un grand nombre de routes.
- Vérifiez toujours la table de routage après avoir ajouté ou supprimé des routes pour vous assurer que les modifications ont été appliquées correctement.
- Pour des modifications permanentes, envisagez d'ajouter les routes dans les fichiers de configuration réseau de votre système.