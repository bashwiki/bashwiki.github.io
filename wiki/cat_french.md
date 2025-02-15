# [리눅스] Bash cat 사용법

## Aperçu

La commande `cat` (abréviation de "concatenate") est un utilitaire de ligne de commande dans Unix et Linux qui permet de lire, concaténer et afficher le contenu de fichiers. Son utilisation principale est de visualiser le contenu des fichiers texte, mais elle peut également être utilisée pour combiner plusieurs fichiers en un seul.

## Utilisation

La syntaxe de base de la commande `cat` est la suivante :

```bash
cat [options] [fichier...]
```

### Options courantes

- `-n` : Numérote toutes les lignes de sortie.
- `-b` : Numérote uniquement les lignes non vides.
- `-E` : Affiche un symbole `$` à la fin de chaque ligne.
- `-s` : Supprime les lignes vides successives.

## Exemples

### Exemple 1 : Afficher le contenu d'un fichier

Pour afficher le contenu d'un fichier texte nommé `exemple.txt`, vous pouvez utiliser la commande suivante :

```bash
cat exemple.txt
```

### Exemple 2 : Combiner plusieurs fichiers

Pour combiner le contenu de deux fichiers, `fichier1.txt` et `fichier2.txt`, et afficher le résultat dans le terminal, utilisez :

```bash
cat fichier1.txt fichier2.txt
```

## Conseils

- Utilisez `cat` avec prudence pour les fichiers volumineux, car cela peut surcharger le terminal. Dans ce cas, envisagez d'utiliser `less` ou `more` pour une navigation plus facile.
- Pour rediriger la sortie de `cat` vers un nouveau fichier, vous pouvez utiliser le symbole `>` :

```bash
cat fichier1.txt fichier2.txt > fichier_combine.txt
```

- N'oubliez pas que `cat` peut également être utilisé pour créer de nouveaux fichiers en utilisant l'entrée standard. Par exemple, vous pouvez créer un fichier en tapant :

```bash
cat > nouveau_fichier.txt
```

Puis, tapez votre texte et terminez avec `CTRL+D` pour enregistrer.