# [Linux] Bash apt utilisation : Gestion des paquets

## Overview
La commande `apt` est un outil de gestion de paquets utilisé sur les systèmes basés sur Debian, comme Ubuntu. Elle permet d'installer, de mettre à jour et de supprimer des logiciels facilement depuis la ligne de commande.

## Usage
La syntaxe de base de la commande `apt` est la suivante :

```bash
apt [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `apt` :

- `update` : Met à jour la liste des paquets disponibles.
- `upgrade` : Met à jour tous les paquets installés vers leur dernière version.
- `install` : Installe un ou plusieurs paquets.
- `remove` : Supprime un ou plusieurs paquets.
- `search` : Recherche un paquet dans les dépôts.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `apt` :

1. **Mettre à jour la liste des paquets :**
   ```bash
   sudo apt update
   ```

2. **Mettre à jour tous les paquets installés :**
   ```bash
   sudo apt upgrade
   ```

3. **Installer un paquet (par exemple, `curl`) :**
   ```bash
   sudo apt install curl
   ```

4. **Supprimer un paquet (par exemple, `curl`) :**
   ```bash
   sudo apt remove curl
   ```

5. **Rechercher un paquet (par exemple, `git`) :**
   ```bash
   apt search git
   ```

## Tips
- Toujours exécuter `sudo apt update` avant d'installer ou de mettre à jour des paquets pour s'assurer que vous disposez des dernières informations sur les dépôts.
- Utilisez `apt list --upgradable` pour voir quels paquets peuvent être mis à jour avant d'exécuter `apt upgrade`.
- Pour une installation silencieuse, vous pouvez ajouter l'option `-y` à vos commandes, par exemple : `sudo apt install -y nom_du_paquet`.