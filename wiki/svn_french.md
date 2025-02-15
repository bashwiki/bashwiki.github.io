# [리눅스] Bash svn 사용법

## Overview
La commande `svn` (Subversion) est un système de contrôle de version open-source qui permet de gérer des fichiers et des répertoires, ainsi que les modifications apportées à ces fichiers au fil du temps. Son objectif principal est de faciliter la collaboration entre plusieurs développeurs en permettant le suivi des modifications, la gestion des versions et la restauration des versions antérieures des fichiers.

## Usage
La syntaxe de base de la commande `svn` est la suivante :

```
svn [options] commande [arguments]
```

### Options courantes :
- `checkout` : Récupère un projet depuis un dépôt et crée une copie locale.
- `commit` : Envoie les modifications locales au dépôt.
- `update` : Met à jour la copie locale avec les dernières modifications du dépôt.
- `add` : Ajoute un nouveau fichier ou répertoire à la copie de travail.
- `delete` : Supprime un fichier ou répertoire de la copie de travail.
- `status` : Affiche l'état des fichiers dans la copie de travail.

## Examples
### Exemple 1 : Récupérer un projet depuis un dépôt
Pour récupérer un projet depuis un dépôt Subversion, utilisez la commande `checkout` :

```bash
svn checkout https://example.com/svn/mon_projet
```

Cette commande crée une copie locale du projet à l'emplacement spécifié.

### Exemple 2 : Envoyer des modifications au dépôt
Après avoir modifié des fichiers dans votre copie locale, vous pouvez envoyer ces modifications au dépôt avec la commande `commit` :

```bash
svn commit -m "Ajout d'une nouvelle fonctionnalité"
```

L'option `-m` permet d'ajouter un message de commit décrivant les modifications.

## Tips
- **Utilisez des messages de commit clairs** : Lorsque vous utilisez la commande `commit`, assurez-vous d'écrire des messages de commit descriptifs pour faciliter la compréhension des modifications apportées.
- **Mettez à jour régulièrement** : Avant de commencer à travailler sur un projet, utilisez `svn update` pour vous assurer que votre copie locale est à jour avec les dernières modifications du dépôt.
- **Vérifiez l'état de votre copie de travail** : Utilisez `svn status` pour voir quels fichiers ont été modifiés, ajoutés ou supprimés avant de faire un commit.
- **Sauvegardez vos modifications** : Avant de faire des modifications majeures, envisagez de créer une branche pour éviter d'affecter la version principale du projet.

En suivant ces conseils, vous pourrez utiliser la commande `svn` de manière efficace pour gérer vos projets de développement.