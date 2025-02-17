# [Linux] Bash svn Utilisation : Gestion de versions de fichiers

## Overview
La commande `svn` (Subversion) est un système de contrôle de version qui permet de gérer les modifications apportées à des fichiers et des répertoires au fil du temps. Elle est largement utilisée pour le développement de logiciels, permettant aux utilisateurs de suivre les modifications, de collaborer et de revenir à des versions antérieures si nécessaire.

## Usage
La syntaxe de base de la commande `svn` est la suivante :

```bash
svn [options] [arguments]
```

## Common Options
Voici quelques options courantes de la commande `svn` :

- `checkout` : Récupère une copie locale d'un dépôt.
- `commit` : Envoie les modifications locales au dépôt.
- `update` : Met à jour la copie locale avec les dernières modifications du dépôt.
- `add` : Ajoute un nouveau fichier ou répertoire au contrôle de version.
- `delete` : Supprime un fichier ou répertoire du contrôle de version.
- `status` : Affiche l'état des fichiers dans la copie locale.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `svn` :

### Récupérer une copie du dépôt
```bash
svn checkout https://example.com/svn/repo
```

### Enregistrer des modifications
```bash
svn commit -m "Message de commit décrivant les modifications"
```

### Mettre à jour la copie locale
```bash
svn update
```

### Ajouter un nouveau fichier
```bash
svn add nouveau_fichier.txt
```

### Supprimer un fichier
```bash
svn delete ancien_fichier.txt
```

### Vérifier l'état des fichiers
```bash
svn status
```

## Tips
- Toujours ajouter un message descriptif lors de l'utilisation de `commit` pour faciliter le suivi des modifications.
- Utilisez `svn update` régulièrement pour vous assurer que votre copie locale est à jour avec le dépôt.
- Avant de supprimer des fichiers, vérifiez leur état avec `svn status` pour éviter de perdre des données importantes.