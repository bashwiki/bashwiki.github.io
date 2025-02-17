# [Linux] Bash whoami Utilisation : Affiche le nom de l'utilisateur actuel

## Overview
La commande `whoami` est utilisée pour afficher le nom de l'utilisateur actuellement connecté à la session du terminal. C'est un moyen simple de vérifier sous quel compte vous travaillez, surtout lorsqu'il y a plusieurs utilisateurs sur un système.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
whoami [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `whoami` :

- `--help` : Affiche l'aide et les options disponibles pour la commande.
- `--version` : Affiche la version de la commande `whoami`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `whoami` :

1. **Afficher le nom de l'utilisateur actuel :**

   ```bash
   whoami
   ```

2. **Afficher l'aide de la commande :**

   ```bash
   whoami --help
   ```

3. **Afficher la version de la commande :**

   ```bash
   whoami --version
   ```

## Tips
- Utilisez `whoami` lorsque vous travaillez sur un serveur partagé pour vous assurer que vous exécutez des commandes sous le bon utilisateur.
- Combinez `whoami` avec d'autres commandes pour des scripts, par exemple, pour vérifier les permissions d'un utilisateur avant d'exécuter une tâche.
- N'oubliez pas que `whoami` ne nécessite pas d'options pour fonctionner dans sa forme la plus simple.