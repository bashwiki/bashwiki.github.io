# [리눅스] Bash sed 사용법

## Overview
Le `sed` (Stream Editor) est un éditeur de texte non interactif qui permet de traiter et de modifier des flux de texte. Il est principalement utilisé pour effectuer des substitutions, des suppressions ou des insertions de texte dans des fichiers ou des flux de données. Grâce à sa capacité à traiter des fichiers ligne par ligne, `sed` est particulièrement utile pour automatiser des tâches de manipulation de texte dans des scripts shell.

## Usage
La syntaxe de base de la commande `sed` est la suivante :

```bash
sed [options] 'commande' fichier
```

### Options courantes :
- `-e` : Permet d'ajouter plusieurs commandes `sed` à exécuter.
- `-i` : Modifie le fichier en place (sans créer de fichier temporaire).
- `-n` : Supprime l'affichage automatique des lignes, utile avec la commande `p` pour afficher uniquement les lignes spécifiées.
- `-f` : Permet de lire les commandes `sed` à partir d'un fichier.

## Examples
### Exemple 1 : Remplacer du texte
Pour remplacer toutes les occurrences de "chat" par "chien" dans un fichier `animaux.txt`, vous pouvez utiliser la commande suivante :

```bash
sed 's/chat/chien/g' animaux.txt
```

### Exemple 2 : Supprimer des lignes
Pour supprimer toutes les lignes contenant le mot "erreur" dans un fichier `log.txt`, utilisez :

```bash
sed '/erreur/d' log.txt
```

## Tips
- Lorsque vous utilisez l'option `-i`, faites attention, car cela modifie le fichier d'origine. Il est souvent judicieux de faire une sauvegarde avant de procéder.
- Pour tester vos commandes `sed` sans modifier le fichier, omettez l'option `-i` et redirigez la sortie vers un nouveau fichier.
- Utilisez des expressions régulières pour des substitutions plus complexes, mais assurez-vous de bien comprendre leur syntaxe pour éviter des résultats inattendus.