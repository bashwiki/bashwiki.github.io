# [Linux] Bash local : Définir des variables locales dans une fonction

## Overview
La commande `local` en Bash est utilisée pour déclarer des variables locales à une fonction. Cela signifie que ces variables ne sont accessibles qu'à l'intérieur de la fonction où elles sont définies, évitant ainsi les conflits avec d'autres variables ayant le même nom dans le script.

## Usage
La syntaxe de base de la commande `local` est la suivante :

```bash
local [options] [nom_variable]=[valeur]
```

## Common Options
- Il n'y a pas d'options spécifiques pour la commande `local`, mais vous pouvez l'utiliser avec des déclarations de variables comme suit :
  - `local var=value` : Déclare une variable locale `var` avec la valeur `value`.

## Common Examples

### Exemple 1 : Déclaration d'une variable locale
```bash
ma_fonction() {
    local message="Bonjour, monde!"
    echo $message
}

ma_fonction  # Affiche : Bonjour, monde!
echo $message  # Ne renvoie rien, car 'message' est local à ma_fonction
```

### Exemple 2 : Utilisation de variables locales dans des calculs
```bash
calculer() {
    local a=5
    local b=10
    local somme=$((a + b))
    echo "La somme est : $somme"
}

calculer  # Affiche : La somme est : 15
```

### Exemple 3 : Éviter les conflits de variables
```bash
var="Global"

ma_fonction() {
    local var="Local"
    echo "Variable dans la fonction : $var"
}

ma_fonction  # Affiche : Variable dans la fonction : Local
echo "Variable globale : $var"  # Affiche : Variable globale : Global
```

## Tips
- Utilisez `local` pour éviter les effets de bord dans vos scripts, surtout lorsque vous travaillez avec des fonctions complexes.
- N'oubliez pas que les variables locales ne sont pas accessibles en dehors de la fonction, ce qui peut aider à maintenir la propreté de votre espace de noms.
- Si vous avez besoin de variables accessibles en dehors de la fonction, utilisez simplement des variables globales sans `local`.