# [Linux] Bash bash : Exécuter des commandes dans un shell

## Overview
La commande Bash est un interpréteur de commandes qui permet aux utilisateurs d'exécuter des scripts et des commandes dans un environnement de ligne de commande. Elle est largement utilisée dans les systèmes d'exploitation basés sur Unix, y compris Linux et macOS.

## Usage
La syntaxe de base de la commande Bash est la suivante :

```bash
bash [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec la commande Bash :

- `-c` : Exécute une commande spécifiée dans une chaîne.
- `-i` : Lance Bash en mode interactif.
- `-l` : Lance Bash comme un shell de connexion.
- `-s` : Lit les commandes à partir de l'entrée standard.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande Bash :

1. **Exécuter une commande simple :**
   ```bash
   bash -c 'echo "Bonjour, monde!"'
   ```

2. **Lancer un script Bash :**
   ```bash
   bash script.sh
   ```

3. **Exécuter Bash en mode interactif :**
   ```bash
   bash -i
   ```

4. **Lire des commandes à partir de l'entrée standard :**
   ```bash
   echo -e "echo 'Hello'\necho 'World'" | bash -s
   ```

## Tips
- Utilisez des scripts Bash pour automatiser des tâches répétitives.
- Commentez votre code avec `#` pour rendre vos scripts plus lisibles.
- Testez vos scripts dans un environnement contrôlé avant de les exécuter en production.
- N'oubliez pas d'utiliser des permissions appropriées pour vos scripts avec `chmod`.