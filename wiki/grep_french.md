# [Linux] Bash grep utilisation : recherche de texte dans des fichiers

## Overview
La commande `grep` est utilisée pour rechercher des chaînes de caractères dans des fichiers. Elle permet de filtrer les lignes qui correspondent à un motif spécifié, ce qui en fait un outil puissant pour l'analyse de texte et le traitement de données.

## Usage
La syntaxe de base de la commande `grep` est la suivante :

```bash
grep [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `grep` :

- `-i` : Ignore la casse lors de la recherche.
- `-v` : Inverse la recherche, affichant les lignes qui ne correspondent pas au motif.
- `-r` : Recherche récursive dans les répertoires.
- `-n` : Affiche les numéros de ligne des correspondances.
- `-l` : Affiche uniquement les noms de fichiers contenant des correspondances.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `grep` :

1. **Recherche d'un mot dans un fichier :**
   ```bash
   grep "mot" fichier.txt
   ```

2. **Recherche sans tenir compte de la casse :**
   ```bash
   grep -i "mot" fichier.txt
   ```

3. **Recherche récursive dans un répertoire :**
   ```bash
   grep -r "mot" /chemin/du/répertoire
   ```

4. **Affichage des lignes avec leur numéro :**
   ```bash
   grep -n "mot" fichier.txt
   ```

5. **Affichage des fichiers contenant le mot :**
   ```bash
   grep -l "mot" *.txt
   ```

## Tips
- Utilisez l'option `-v` pour filtrer les lignes indésirables et simplifier vos résultats.
- Combinez `grep` avec d'autres commandes en utilisant des pipes (`|`) pour des analyses plus complexes.
- Pensez à utiliser des expressions régulières pour des recherches plus avancées et précises.