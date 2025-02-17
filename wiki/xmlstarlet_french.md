# [Linux] Bash xmlstarlet : Manipuler et interroger des fichiers XML

## Overview
Le commandement `xmlstarlet` est un outil puissant en ligne de commande utilisé pour manipuler, interroger et transformer des fichiers XML. Il permet d'effectuer des opérations telles que la validation, la transformation XSLT, et l'extraction de données XML.

## Usage
La syntaxe de base de la commande `xmlstarlet` est la suivante :

```bash
xmlstarlet [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `xmlstarlet` :

- `xmlstarlet sel` : Sélectionne des nœuds dans un document XML.
- `xmlstarlet ed` : Édite un document XML.
- `xmlstarlet val` : Valide un document XML contre un schéma.
- `xmlstarlet tr` : Transforme un document XML en utilisant XSLT.
- `xmlstarlet fo` : Formate un document XML pour une meilleure lisibilité.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `xmlstarlet` :

### Sélectionner des nœuds
Pour sélectionner tous les éléments `<title>` d'un fichier XML :

```bash
xmlstarlet sel -t -m "//title" -v "." -n fichier.xml
```

### Éditer un document XML
Pour ajouter un nouvel élément `<author>` dans chaque `<book>` :

```bash
xmlstarlet ed -s "//book" -t -n "author" -v "Nom de l'Auteur" fichier.xml
```

### Valider un document XML
Pour valider un fichier XML contre un schéma XSD :

```bash
xmlstarlet val -e -s schema.xsd fichier.xml
```

### Transformer un document XML
Pour transformer un fichier XML en utilisant une feuille de style XSLT :

```bash
xmlstarlet tr style.xsl -o sortie.xml fichier.xml
```

### Formater un document XML
Pour formater un fichier XML pour une meilleure lisibilité :

```bash
xmlstarlet fo fichier.xml > fichier_formate.xml
```

## Tips
- Utilisez `xmlstarlet --help` pour afficher toutes les options disponibles et leur description.
- Pour des fichiers XML volumineux, envisagez d'utiliser des options de filtrage pour améliorer les performances.
- Testez vos transformations XSLT avec des fichiers XML de petite taille avant de les appliquer à des fichiers plus grands.