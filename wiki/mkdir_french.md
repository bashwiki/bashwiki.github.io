# [Linux] Bash mkdir Utilisation : Créer des répertoires

## Overview
La commande `mkdir` est utilisée pour créer des répertoires dans le système de fichiers. Elle permet aux utilisateurs d'organiser leurs fichiers en créant des dossiers selon leurs besoins.

## Usage
La syntaxe de base de la commande `mkdir` est la suivante :

```bash
mkdir [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `mkdir` :

- `-p` : Crée des répertoires parents si nécessaire. Par exemple, si le répertoire parent n'existe pas, il sera créé.
- `-v` : Affiche un message pour chaque répertoire créé, ce qui peut être utile pour le débogage.
- `-m` : Définit les permissions du répertoire créé en spécifiant un mode.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mkdir` :

1. **Créer un répertoire simple :**
   ```bash
   mkdir mon_dossier
   ```

2. **Créer plusieurs répertoires à la fois :**
   ```bash
   mkdir dossier1 dossier2 dossier3
   ```

3. **Créer un répertoire avec des répertoires parents :**
   ```bash
   mkdir -p parent/enfant
   ```

4. **Créer un répertoire avec des permissions spécifiques :**
   ```bash
   mkdir -m 755 mon_dossier
   ```

5. **Créer un répertoire et afficher un message :**
   ```bash
   mkdir -v mon_dossier
   ```

## Tips
- Utilisez l'option `-p` lorsque vous créez une structure de répertoires complexe pour éviter les erreurs si les répertoires parents n'existent pas.
- Vérifiez toujours les permissions des répertoires créés, surtout si vous utilisez l'option `-m`.
- N'oubliez pas que les noms de répertoires sont sensibles à la casse dans les systèmes de fichiers Linux.