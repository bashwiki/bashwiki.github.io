# [Linux] Bash seq : Générer des séquences de nombres

## Overview
La commande `seq` est utilisée pour générer des séquences de nombres. Elle permet de créer une liste de nombres en spécifiant un début, une fin, et éventuellement un pas. C'est un outil pratique pour les scripts et les opérations en ligne de commande.

## Usage
La syntaxe de base de la commande `seq` est la suivante :

```bash
seq [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `seq` :

- `-f, --format=FORMAT` : Permet de spécifier un format pour les nombres générés.
- `-s, --separator=STRING` : Définit un séparateur entre les nombres (par défaut, un saut de ligne).
- `-w, --equal-width` : Remplit les nombres avec des zéros pour qu'ils aient tous la même largeur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `seq` :

1. Générer une séquence de 1 à 10 :
   ```bash
   seq 1 10
   ```

2. Générer une séquence de 1 à 10 avec un pas de 2 :
   ```bash
   seq 1 2 10
   ```

3. Générer une séquence de 5 à 15 :
   ```bash
   seq 5 15
   ```

4. Générer une séquence de nombres avec un format spécifique :
   ```bash
   seq -f "Nombre: %g" 1 5
   ```

5. Générer une séquence de nombres séparés par une virgule :
   ```bash
   seq -s "," 1 5
   ```

## Tips
- Utilisez l'option `-w` pour garantir que tous les nombres ont la même largeur, ce qui peut être utile pour l'affichage.
- Combinez `seq` avec d'autres commandes en utilisant des pipes pour des opérations plus complexes.
- Pensez à utiliser `seq` dans des boucles pour automatiser des tâches répétitives dans vos scripts.