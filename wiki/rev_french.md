# [리눅스] Bash rev 사용법

## Overview
La commande `rev` est un utilitaire de ligne de commande dans Bash qui inverse l'ordre des caractères de chaque ligne d'un fichier ou d'une entrée standard. Son principal objectif est de fournir une manière simple et rapide de retourner les chaînes de caractères, ce qui peut être utile dans divers scénarios de traitement de texte ou de débogage.

## Usage
La syntaxe de base de la commande `rev` est la suivante :

```
rev [OPTION]... [FICHIER]
```

### Options courantes :
- `FICHIER` : Spécifie le fichier à traiter. Si aucun fichier n'est fourni, `rev` lira l'entrée standard.
- `-h`, `--help` : Affiche l'aide et quitte.
- `-V`, `--version` : Affiche la version de `rev` et quitte.

## Examples
### Exemple 1 : Inverser une chaîne de caractères
Pour inverser une chaîne de caractères fournie via l'entrée standard, vous pouvez utiliser la commande suivante :

```bash
echo "Bonjour" | rev
```
**Sortie :**
```
ruojnoB
```

### Exemple 2 : Inverser le contenu d'un fichier
Supposons que vous ayez un fichier nommé `exemple.txt` contenant plusieurs lignes de texte. Pour inverser chaque ligne, utilisez la commande suivante :

```bash
rev exemple.txt
```
**Sortie :**
```
elmpaxe
tset
```

## Tips
- Utilisez `rev` en combinaison avec d'autres commandes de traitement de texte pour des opérations plus complexes. Par exemple, vous pouvez utiliser `cat` pour lire un fichier et `rev` pour inverser son contenu.
- Soyez conscient que `rev` inverse les caractères ligne par ligne. Si vous souhaitez inverser l'ordre des lignes elles-mêmes, envisagez d'utiliser la commande `tac` en complément.
- Pour traiter de grands fichiers, assurez-vous que votre terminal peut gérer la sortie, car `rev` affichera le contenu inversé directement dans la console.