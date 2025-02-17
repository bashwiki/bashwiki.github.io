# [Linux] Bash return usage équivalent : Retourner le statut d'un processus

## Overview
La commande `return` dans Bash est utilisée pour terminer une fonction et renvoyer un code de statut à l'environnement appelant. Ce code de statut peut être utilisé pour indiquer si la fonction a réussi ou échoué.

## Usage
La syntaxe de base de la commande `return` est la suivante :

```bash
return [options] [n]
```

Ici, `n` est un entier qui représente le code de statut que vous souhaitez renvoyer.

## Common Options
- `n` : Un entier entre 0 et 255 qui représente le code de statut à renvoyer. Par convention, 0 indique le succès, tandis que toute autre valeur indique une erreur.

## Common Examples

### Exemple 1 : Retourner un statut de succès
```bash
function test_success {
    echo "Cette fonction a réussi."
    return 0
}

test_success
echo "Statut de retour : $?"
```

### Exemple 2 : Retourner un statut d'erreur
```bash
function test_failure {
    echo "Cette fonction a échoué."
    return 1
}

test_failure
echo "Statut de retour : $?"
```

### Exemple 3 : Utiliser `return` dans une condition
```bash
function check_value {
    if [ "$1" -lt 10 ]; then
        return 0  # Succès
    else
        return 1  # Échec
    fi
}

check_value 5
echo "Statut de retour : $?"  # Affiche 0

check_value 15
echo "Statut de retour : $?"  # Affiche 1
```

## Tips
- Utilisez `return` uniquement à l'intérieur des fonctions. En dehors des fonctions, `return` ne fonctionnera pas et générera une erreur.
- Vérifiez toujours le code de statut après l'appel d'une fonction pour gérer les erreurs de manière appropriée.
- Gardez à l'esprit que le code de statut est limité à une plage de 0 à 255.