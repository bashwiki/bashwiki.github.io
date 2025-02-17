# [Linux] Bash diff utilisation : Comparer des fichiers ligne par ligne

## Overview
La commande `diff` est utilisée pour comparer le contenu de deux fichiers ligne par ligne. Elle affiche les différences entre ces fichiers, ce qui est particulièrement utile pour les développeurs et les rédacteurs qui souhaitent suivre les modifications apportées à des fichiers texte.

## Usage
La syntaxe de base de la commande `diff` est la suivante :

```bash
diff [options] [fichier1] [fichier2]
```

## Common Options
Voici quelques options courantes de la commande `diff` :

- `-u` : Affiche les différences en mode unifié, ce qui rend la sortie plus lisible.
- `-c` : Affiche les différences en mode contextuel, fournissant un aperçu des lignes environnantes.
- `-i` : Ignore la casse lors de la comparaison.
- `-w` : Ignore les espaces blancs lors de la comparaison.
- `-r` : Compare récursivement les répertoires.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `diff` :

1. Comparer deux fichiers texte simples :
   ```bash
   diff fichier1.txt fichier2.txt
   ```

2. Afficher les différences en mode unifié :
   ```bash
   diff -u fichier1.txt fichier2.txt
   ```

3. Comparer deux répertoires récursivement :
   ```bash
   diff -r dossier1/ dossier2/
   ```

4. Ignorer les espaces blancs lors de la comparaison :
   ```bash
   diff -w fichier1.txt fichier2.txt
   ```

5. Afficher les différences en mode contextuel :
   ```bash
   diff -c fichier1.txt fichier2.txt
   ```

## Tips
- Utilisez l'option `-u` pour obtenir une sortie plus claire et plus facile à lire, surtout lorsque vous partagez les résultats avec d'autres.
- Lorsque vous comparez des répertoires, l'option `-r` est très utile pour voir toutes les différences dans les fichiers contenus dans ces répertoires.
- Pensez à rediriger la sortie de `diff` vers un fichier si vous souhaitez conserver un enregistrement des différences :
  ```bash
  diff fichier1.txt fichier2.txt > differences.txt
  ```