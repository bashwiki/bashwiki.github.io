# [Linux] Bash useradd : Ajouter un nouvel utilisateur au système

## Overview
La commande `useradd` est utilisée pour créer un nouvel utilisateur sur un système Linux. Elle permet de définir des paramètres tels que le nom d'utilisateur, le répertoire personnel et le shell par défaut.

## Usage
La syntaxe de base de la commande `useradd` est la suivante :

```bash
useradd [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `useradd` :

- `-m` : Crée un répertoire personnel pour l'utilisateur.
- `-s` : Définit le shell par défaut pour l'utilisateur.
- `-G` : Ajoute l'utilisateur à un ou plusieurs groupes supplémentaires.
- `-c` : Permet d'ajouter un commentaire, souvent utilisé pour le nom complet de l'utilisateur.
- `-d` : Spécifie un répertoire personnel différent de celui par défaut.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `useradd` :

1. **Créer un nouvel utilisateur avec un répertoire personnel :**
   ```bash
   useradd -m nouvel_utilisateur
   ```

2. **Créer un utilisateur avec un shell spécifique :**
   ```bash
   useradd -m -s /bin/bash nouvel_utilisateur
   ```

3. **Créer un utilisateur et l'ajouter à des groupes supplémentaires :**
   ```bash
   useradd -m -G sudo,admin nouvel_utilisateur
   ```

4. **Créer un utilisateur avec un commentaire :**
   ```bash
   useradd -m -c "Jean Dupont" nouvel_utilisateur
   ```

5. **Créer un utilisateur avec un répertoire personnel personnalisé :**
   ```bash
   useradd -m -d /home/jean nouvel_utilisateur
   ```

## Tips
- Toujours vérifier les options disponibles avec `man useradd` pour une compréhension complète.
- Pensez à définir un mot de passe pour le nouvel utilisateur avec la commande `passwd nouvel_utilisateur` après l'avoir créé.
- Utilisez l'option `-e` pour définir une date d'expiration pour le compte utilisateur si nécessaire.