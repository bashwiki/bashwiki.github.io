# [Linux] Bash tput : Contrôler l'affichage du terminal

## Overview
La commande `tput` est utilisée pour contrôler les fonctionnalités d'affichage du terminal. Elle permet de manipuler les caractéristiques visuelles, comme les couleurs, les styles de texte et la position du curseur, en fonction des capacités du terminal.

## Usage
La syntaxe de base de la commande `tput` est la suivante :

```bash
tput [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `tput` :

- `setaf [n]` : Définit la couleur de premier plan (texte) à la couleur spécifiée par le numéro `n`.
- `setab [n]` : Définit la couleur d'arrière-plan à la couleur spécifiée par le numéro `n`.
- `bold` : Active le texte en gras.
- `clear` : Efface l'écran du terminal.
- `cup [x] [y]` : Déplace le curseur à la position spécifiée par les coordonnées `x` (ligne) et `y` (colonne).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `tput` :

1. **Changer la couleur du texte :**
   ```bash
   tput setaf 1  # Change le texte en rouge
   echo "Texte en rouge"
   tput sgr0     # Réinitialise les attributs du terminal
   ```

2. **Effacer l'écran :**
   ```bash
   tput clear
   ```

3. **Déplacer le curseur :**
   ```bash
   tput cup 10 20  # Déplace le curseur à la ligne 10, colonne 20
   echo "Texte à une position spécifique"
   ```

4. **Activer le texte en gras :**
   ```bash
   tput bold
   echo "Texte en gras"
   tput sgr0  # Réinitialise les attributs du terminal
   ```

5. **Changer la couleur d'arrière-plan :**
   ```bash
   tput setab 4  # Change l'arrière-plan en bleu
   echo "Texte avec arrière-plan bleu"
   tput sgr0     # Réinitialise les attributs du terminal
   ```

## Tips
- Utilisez `tput sgr0` après avoir appliqué des styles pour réinitialiser les attributs du terminal, afin d'éviter d'affecter les commandes suivantes.
- Testez les différentes couleurs et styles disponibles en utilisant `tput setaf` et `tput setab` avec des numéros de couleur allant de 0 à 7 (ou plus, selon le terminal).
- Intégrez `tput` dans vos scripts pour améliorer l'interaction utilisateur avec des sorties colorées et bien formatées.