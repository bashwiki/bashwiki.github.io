# [Linux] Bash paste Utilisation : Combiner des fichiers ligne par ligne

## Overview
La commande `paste` est utilisée pour fusionner des fichiers ligne par ligne. Elle permet d'assembler plusieurs fichiers en une seule sortie, en séparant les lignes par un caractère spécifique, généralement une tabulation.

## Usage
La syntaxe de base de la commande `paste` est la suivante :

```bash
paste [options] [arguments]
```

## Common Options
- `-d` : Spécifie un ou plusieurs délimiteurs au lieu de la tabulation par défaut.
- `-s` : Combine les lignes de chaque fichier en une seule ligne.
- `-z` : Traite les fichiers comme des flux de données, en utilisant un délimiteur nul.

## Common Examples

### Exemple 1 : Fusionner deux fichiers avec des tabulations
```bash
paste fichier1.txt fichier2.txt
```
Cela combine les lignes de `fichier1.txt` et `fichier2.txt`, séparées par des tabulations.

### Exemple 2 : Utiliser un délimiteur personnalisé
```bash
paste -d ',' fichier1.txt fichier2.txt
```
Ici, les lignes sont fusionnées avec une virgule comme délimiteur.

### Exemple 3 : Combiner les lignes en une seule ligne
```bash
paste -s fichier1.txt
```
Cette commande prend toutes les lignes de `fichier1.txt` et les combine en une seule ligne.

### Exemple 4 : Utiliser un délimiteur nul
```bash
paste -z fichier1.txt fichier2.txt
```
Cela permet de traiter les fichiers comme des flux de données, en utilisant un délimiteur nul.

## Tips
- Lorsque vous utilisez des délimiteurs personnalisés, assurez-vous qu'ils ne sont pas présents dans les fichiers pour éviter toute confusion.
- Pour des fichiers de grande taille, envisagez d'utiliser `paste` en conjonction avec d'autres commandes comme `sort` pour une meilleure organisation des données.
- Testez toujours vos commandes avec des fichiers d'exemple avant de les appliquer à des fichiers importants pour éviter toute perte de données.