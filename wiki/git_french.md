# [Linux] Bash git utilisation : Gestion de versions de code

## Overview
La commande `git` est un système de contrôle de version distribué qui permet de suivre les modifications apportées aux fichiers et de collaborer avec d'autres développeurs. Elle est largement utilisée dans le développement de logiciels pour gérer le code source.

## Usage
La syntaxe de base de la commande git est la suivante :

```bash
git [options] [arguments]
```

## Common Options
Voici quelques options courantes de la commande git :

- `clone` : Crée une copie locale d'un dépôt distant.
- `add` : Ajoute des fichiers à l'index pour les préparer à un commit.
- `commit` : Enregistre les modifications dans l'historique du dépôt.
- `push` : Envoie les commits locaux vers un dépôt distant.
- `pull` : Récupère et intègre les modifications d'un dépôt distant dans la branche locale.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande git :

1. **Cloner un dépôt distant :**
   ```bash
   git clone https://github.com/username/repo.git
   ```

2. **Ajouter un fichier à l'index :**
   ```bash
   git add fichier.txt
   ```

3. **Faire un commit avec un message :**
   ```bash
   git commit -m "Ajout d'un nouveau fichier"
   ```

4. **Pousser les modifications vers le dépôt distant :**
   ```bash
   git push origin main
   ```

5. **Tirer les dernières modifications du dépôt distant :**
   ```bash
   git pull origin main
   ```

## Tips
- **Utilisez des messages de commit clairs** : Cela aide à comprendre l'historique des modifications.
- **Faites des commits fréquents** : Cela permet de suivre les changements plus facilement et de revenir en arrière si nécessaire.
- **Créez des branches pour les nouvelles fonctionnalités** : Cela permet de travailler sur des fonctionnalités sans affecter la branche principale.
- **Utilisez `git status` régulièrement** : Cela vous permet de voir l'état actuel de votre dépôt et les fichiers modifiés.

En suivant ces conseils, vous pourrez utiliser git de manière plus efficace et organisée.