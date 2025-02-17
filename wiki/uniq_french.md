# [Linux] Bash uniq : Éliminer les doublons dans un fichier

## Overview
La commande `uniq` est utilisée pour filtrer les lignes répétées dans un fichier ou dans l'entrée standard. Elle affiche uniquement les lignes uniques, ce qui est particulièrement utile pour traiter des fichiers contenant des données en double.

## Usage
La syntaxe de base de la commande `uniq` est la suivante :

```bash
uniq [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `uniq` :

- `-c` : Compte le nombre d'occurrences de chaque ligne.
- `-d` : Affiche uniquement les lignes qui apparaissent plus d'une fois.
- `-u` : Affiche uniquement les lignes qui apparaissent une seule fois.
- `-i` : Ignore la casse lors de la comparaison des lignes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `uniq` :

1. **Éliminer les doublons d'un fichier :**
   ```bash
   uniq fichier.txt
   ```

2. **Compter les occurrences de chaque ligne :**
   ```bash
   uniq -c fichier.txt
   ```

3. **Afficher uniquement les lignes dupliquées :**
   ```bash
   uniq -d fichier.txt
   ```

4. **Afficher uniquement les lignes uniques :**
   ```bash
   uniq -u fichier.txt
   ```

5. **Ignorer la casse lors de la suppression des doublons :**
   ```bash
   uniq -i fichier.txt
   ```

## Tips
- Assurez-vous que le fichier d'entrée est trié avant d'utiliser `uniq`, car il ne supprime que les doublons consécutifs.
- Vous pouvez combiner `uniq` avec d'autres commandes comme `sort` pour un traitement plus efficace des données.
- Utilisez `uniq -c` pour obtenir un aperçu rapide des occurrences des lignes dans vos fichiers, ce qui peut être utile pour l'analyse de données.