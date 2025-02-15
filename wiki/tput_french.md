# [리눅스] Bash tput 사용법

## Overview
La commande `tput` est un utilitaire de terminal qui permet de contrôler les capacités d'affichage d'un terminal. Elle est principalement utilisée pour manipuler les attributs de l'affichage, tels que la couleur du texte, la position du curseur, et d'autres fonctionnalités de mise en forme. `tput` interagit avec la base de données des terminaux pour fournir des commandes qui peuvent rendre vos scripts Bash plus interactifs et visuellement attrayants.

## Usage
La syntaxe de base de la commande `tput` est la suivante :

```bash
tput [option] [argument]
```

### Options courantes :
- `setaf <num>` : Définit la couleur du texte (foreground) en utilisant un code de couleur numérique.
- `setab <num>` : Définit la couleur de fond (background) en utilisant un code de couleur numérique.
- `clear` : Efface l'écran du terminal.
- `cup <x> <y>` : Déplace le curseur à la position (x, y) dans le terminal.
- `bold` : Active le texte en gras.

## Examples
Voici quelques exemples pratiques montrant comment utiliser la commande `tput`.

### Exemple 1 : Changer la couleur du texte
Pour afficher un texte en rouge, vous pouvez utiliser la commande suivante :

```bash
tput setaf 1
echo "Ceci est un texte en rouge."
tput sgr0  # Réinitialise les attributs du terminal
```

### Exemple 2 : Effacer l'écran et déplacer le curseur
Pour effacer l'écran et déplacer le curseur à la position (5, 10), utilisez :

```bash
tput clear
tput cup 5 10
echo "Le curseur est maintenant à la ligne 5, colonne 10."
```

## Tips
- Utilisez `tput sgr0` à la fin de vos scripts pour réinitialiser les attributs du terminal à leur état par défaut, afin d'éviter que les modifications d'affichage n'affectent les commandes suivantes.
- Consultez la base de données des terminaux (comme `terminfo`) pour connaître les codes de couleur spécifiques à votre terminal, car ils peuvent varier d'un environnement à l'autre.
- Combinez plusieurs commandes `tput` pour créer des interfaces utilisateur textuelles plus complexes et attrayantes dans vos scripts.