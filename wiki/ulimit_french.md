# [Linux] Bash ulimit : Limiter les ressources du shell

## Overview
La commande `ulimit` est utilisée dans les systèmes Unix et Linux pour définir des limites sur les ressources que les processus peuvent utiliser. Cela inclut des éléments tels que la mémoire, le nombre de fichiers ouverts, et le temps d'exécution. Cette commande est particulièrement utile pour gérer les ressources dans un environnement multi-utilisateur ou pour éviter qu'un processus ne consomme toutes les ressources disponibles.

## Usage
La syntaxe de base de la commande `ulimit` est la suivante :

```bash
ulimit [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `ulimit` :

- `-a` : Affiche toutes les limites actuelles.
- `-c` : Définit la taille maximale des fichiers de core dump.
- `-d` : Définit la taille maximale de la mémoire de données.
- `-f` : Définit la taille maximale des fichiers créés.
- `-l` : Définit la taille maximale de la mémoire verrouillée.
- `-n` : Définit le nombre maximal de fichiers ouverts.
- `-t` : Définit le temps maximal d'exécution en secondes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `ulimit` :

1. **Afficher toutes les limites actuelles :**
   ```bash
   ulimit -a
   ```

2. **Définir la taille maximale d'un fichier à 100 Mo :**
   ```bash
   ulimit -f 102400
   ```

3. **Limiter le nombre de fichiers ouverts à 50 :**
   ```bash
   ulimit -n 50
   ```

4. **Définir la taille maximale de la mémoire de données à 512 Mo :**
   ```bash
   ulimit -d 524288
   ```

5. **Activer le core dump pour les processus :**
   ```bash
   ulimit -c unlimited
   ```

## Tips
- Assurez-vous d'utiliser `ulimit` dans un shell interactif, car les limites définies ne s'appliquent qu'à la session en cours.
- Pour appliquer des limites de manière permanente, vous pouvez ajouter les commandes `ulimit` dans votre fichier de configuration de shell, comme `.bashrc` ou `.bash_profile`.
- Faites attention en augmentant les limites, car cela peut affecter la stabilité du système, surtout dans un environnement partagé.