# [Linux] Bash sed Utilisation : Modifier et transformer du texte

## Overview
La commande `sed`, qui signifie "stream editor", est un éditeur de texte non interactif utilisé pour effectuer des transformations sur des flux de texte. Elle est souvent utilisée pour rechercher, remplacer, insérer ou supprimer des lignes dans des fichiers ou des entrées standard.

## Usage
La syntaxe de base de la commande `sed` est la suivante :

```bash
sed [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `sed` :

- `-e` : Permet d'ajouter une expression de script.
- `-i` : Modifie le fichier en place (sans créer de copie).
- `-n` : Supprime l'affichage automatique des lignes, utile avec l'option `p` pour imprimer seulement les lignes spécifiées.
- `s/pattern/replacement/` : Effectue une substitution, remplaçant `pattern` par `replacement`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `sed` :

### Remplacer du texte dans un fichier
Pour remplacer "ancien" par "nouveau" dans un fichier `exemple.txt` :

```bash
sed -i 's/ancien/nouveau/g' exemple.txt
```

### Supprimer des lignes contenant un mot spécifique
Pour supprimer toutes les lignes contenant "supprimer" dans `exemple.txt` :

```bash
sed -i '/supprimer/d' exemple.txt
```

### Afficher uniquement les lignes qui contiennent un mot
Pour afficher uniquement les lignes contenant "afficher" :

```bash
sed -n '/afficher/p' exemple.txt
```

### Ajouter une ligne après une correspondance
Pour ajouter "Nouvelle ligne" après chaque ligne contenant "ajouter" :

```bash
sed '/ajouter/a Nouvelle ligne' exemple.txt
```

## Tips
- Utilisez l'option `-i` avec précaution, car elle modifie le fichier original. Pensez à faire une sauvegarde avant de l'utiliser.
- Testez vos commandes `sed` sans l'option `-i` d'abord pour voir les résultats avant de modifier le fichier.
- Combinez plusieurs commandes `sed` en utilisant l'option `-e` pour appliquer plusieurs transformations en une seule commande.