# [Linux] Bash egrep utilisation : recherche avancée de motifs dans du texte

## Overview
La commande `egrep` est une version de la commande `grep` qui permet de rechercher des motifs dans des fichiers ou des entrées standard en utilisant des expressions régulières étendues. Elle est particulièrement utile pour des recherches plus complexes grâce à sa capacité à interpréter des métacaractères.

## Usage
La syntaxe de base de la commande `egrep` est la suivante :

```bash
egrep [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `egrep` :

- `-i` : Ignore la casse lors de la recherche.
- `-v` : Inverse la recherche, affichant les lignes qui ne correspondent pas au motif.
- `-c` : Affiche uniquement le nombre de lignes correspondantes.
- `-n` : Affiche les numéros de ligne avec les lignes correspondantes.
- `-r` : Recherche récursive dans les sous-répertoires.

## Common Examples
Voici quelques exemples pratiques d'utilisation de `egrep` :

1. **Recherche d'un mot dans un fichier :**
   ```bash
   egrep "mot" fichier.txt
   ```

2. **Recherche sans tenir compte de la casse :**
   ```bash
   egrep -i "mot" fichier.txt
   ```

3. **Affichage des lignes qui ne contiennent pas le mot :**
   ```bash
   egrep -v "mot" fichier.txt
   ```

4. **Recherche dans plusieurs fichiers :**
   ```bash
   egrep "mot" *.txt
   ```

5. **Recherche récursive dans un répertoire :**
   ```bash
   egrep -r "mot" /chemin/du/répertoire
   ```

## Tips
- Utilisez l'option `-n` pour obtenir le numéro de ligne, ce qui facilite la localisation des résultats dans de grands fichiers.
- Combinez `egrep` avec d'autres commandes comme `sort` ou `uniq` pour traiter les résultats de manière plus efficace.
- Familiarisez-vous avec les expressions régulières pour tirer le meilleur parti de `egrep`, car cela vous permettra de créer des motifs de recherche plus puissants et précis.