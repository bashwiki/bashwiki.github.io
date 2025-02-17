# [Linux] Bash hostname utilisation : afficher ou définir le nom d'hôte

## Overview
La commande `hostname` permet d'afficher ou de définir le nom d'hôte d'un système. Le nom d'hôte est un identifiant unique qui permet de distinguer un ordinateur sur un réseau.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
hostname [options] [arguments]
```

## Common Options
- `-a` : Affiche le nom d'hôte alias.
- `-d` : Affiche le nom de domaine.
- `-f` : Affiche le nom d'hôte complet (FQDN).
- `-i` : Affiche l'adresse IP du nom d'hôte.
- `-s` : Affiche le nom d'hôte court.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `hostname` :

1. Afficher le nom d'hôte actuel :
   ```bash
   hostname
   ```

2. Afficher le nom d'hôte complet :
   ```bash
   hostname -f
   ```

3. Afficher l'adresse IP associée au nom d'hôte :
   ```bash
   hostname -i
   ```

4. Définir un nouveau nom d'hôte (nécessite des privilèges administratifs) :
   ```bash
   sudo hostname nouveau-nom
   ```

5. Afficher le nom de domaine :
   ```bash
   hostname -d
   ```

## Tips
- Utilisez `sudo` pour changer le nom d'hôte, car cela nécessite des droits d'administrateur.
- Pour que le changement de nom d'hôte soit permanent, modifiez le fichier `/etc/hostname` et redémarrez le système.
- Vérifiez toujours le nom d'hôte après un changement pour vous assurer qu'il a été appliqué correctement.