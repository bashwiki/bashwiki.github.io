# [리눅스] Bash lsattr 사용법

## Overview
La commande `lsattr` est utilisée sous Linux pour afficher les attributs de fichiers et de répertoires. Ces attributs sont des paramètres qui modifient le comportement des fichiers, comme la protection contre la suppression ou la modification. `lsattr` est particulièrement utile pour les administrateurs système et les développeurs qui souhaitent gérer la sécurité et l'intégrité des fichiers.

## Usage
La syntaxe de base de la commande `lsattr` est la suivante :

```bash
lsattr [options] [fichier...]
```

### Options courantes :
- `-a` : Affiche les attributs de tous les fichiers, y compris ceux qui commencent par un point (fichiers cachés).
- `-d` : Affiche les attributs des répertoires, sans lister leur contenu.
- `-R` : Parcourt récursivement les répertoires pour afficher les attributs de tous les fichiers et sous-répertoires.
- `-V` : Affiche les attributs de manière verbose, fournissant plus de détails.

## Examples
### Exemple 1 : Afficher les attributs d'un fichier
Pour afficher les attributs d'un fichier spécifique, utilisez la commande suivante :

```bash
lsattr mon_fichier.txt
```

Cette commande affichera les attributs associés à `mon_fichier.txt`.

### Exemple 2 : Afficher les attributs de tous les fichiers dans un répertoire
Pour afficher les attributs de tous les fichiers dans un répertoire, y compris les fichiers cachés, utilisez :

```bash
lsattr -a /chemin/vers/le/répertoire
```

Cela affichera les attributs de tous les fichiers dans le répertoire spécifié.

## Tips
- Utilisez `lsattr` avec l'option `-R` pour obtenir une vue complète des attributs dans une hiérarchie de répertoires, ce qui peut être utile pour les audits de sécurité.
- Vérifiez régulièrement les attributs de fichiers critiques pour vous assurer qu'ils n'ont pas été modifiés sans autorisation.
- Combinez `lsattr` avec d'autres commandes comme `grep` pour filtrer les résultats et trouver rapidement des fichiers avec des attributs spécifiques. Par exemple :

```bash
lsattr -a | grep '^i'
```

Cette commande affichera tous les fichiers ayant l'attribut "i" (immutable), ce qui signifie qu'ils ne peuvent pas être modifiés ou supprimés.