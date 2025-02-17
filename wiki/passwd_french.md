# [Linux] Bash passwd : Changer le mot de passe des utilisateurs

## Overview
La commande `passwd` est utilisée pour changer le mot de passe d'un utilisateur dans un système Linux. Elle permet aux utilisateurs de mettre à jour leur propre mot de passe ou à un administrateur de modifier le mot de passe d'un autre utilisateur.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
passwd [options] [arguments]
```

## Common Options
- `-d` : Supprime le mot de passe de l'utilisateur, rendant le compte sans mot de passe.
- `-e` : Force l'utilisateur à changer son mot de passe à la prochaine connexion.
- `-l` : Verrouille le compte de l'utilisateur.
- `-u` : Déverrouille le compte de l'utilisateur.
- `-S` : Affiche l'état du mot de passe pour l'utilisateur spécifié.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `passwd` :

1. **Changer votre propre mot de passe :**
   ```bash
   passwd
   ```

2. **Changer le mot de passe d'un autre utilisateur (nécessite des privilèges d'administrateur) :**
   ```bash
   sudo passwd nom_utilisateur
   ```

3. **Forcer un utilisateur à changer son mot de passe lors de la prochaine connexion :**
   ```bash
   sudo passwd -e nom_utilisateur
   ```

4. **Supprimer le mot de passe d'un utilisateur :**
   ```bash
   sudo passwd -d nom_utilisateur
   ```

5. **Afficher l'état du mot de passe d'un utilisateur :**
   ```bash
   passwd -S nom_utilisateur
   ```

## Tips
- Assurez-vous de choisir un mot de passe fort pour améliorer la sécurité de votre compte.
- Utilisez l'option `-e` après avoir changé un mot de passe pour forcer un changement lors de la prochaine connexion.
- Évitez de partager votre mot de passe avec d'autres utilisateurs pour maintenir la confidentialité de votre compte.