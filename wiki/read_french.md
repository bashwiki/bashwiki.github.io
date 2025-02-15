# [리눅스] Bash read 사용법

## Overview
La commande `read` en Bash est utilisée pour lire l'entrée de l'utilisateur depuis le terminal. Elle permet de stocker les données saisies par l'utilisateur dans des variables, ce qui est essentiel pour interagir avec les scripts et collecter des informations dynamiques. `read` est souvent utilisé dans des scripts pour obtenir des valeurs de configuration ou pour demander des confirmations à l'utilisateur.

## Usage
La syntaxe de base de la commande `read` est la suivante :

```bash
read [options] variable_name
```

### Options courantes :
- `-p "message"` : Affiche un message avant de lire l'entrée de l'utilisateur.
- `-s` : Masque l'entrée (utile pour les mots de passe).
- `-t seconds` : Définit un délai d'attente en secondes pour l'entrée.
- `-a array_name` : Lit les entrées dans un tableau.

## Examples
### Exemple 1 : Lecture d'une entrée simple
```bash
echo "Entrez votre nom :"
read nom
echo "Bonjour, $nom !"
```
Dans cet exemple, le script demande à l'utilisateur d'entrer son nom et l'affiche ensuite.

### Exemple 2 : Lecture avec un message et un délai
```bash
read -t 10 -p "Entrez votre âge (vous avez 10 secondes) : " age
if [ -z "$age" ]; then
    echo "Aucune entrée reçue."
else
    echo "Vous avez $age ans."
fi
```
Ici, le script demande à l'utilisateur d'entrer son âge avec un message et un délai de 10 secondes. Si l'utilisateur ne saisit rien dans ce délai, un message d'avertissement est affiché.

## Tips
- Utilisez l'option `-s` pour masquer les entrées sensibles, comme les mots de passe, afin de protéger la confidentialité de l'utilisateur.
- Pensez à vérifier si la variable est vide après la lecture pour gérer les cas où l'utilisateur n'entre rien.
- Pour lire plusieurs valeurs en une seule ligne, vous pouvez spécifier plusieurs variables : `read var1 var2 var3`.
- Utilisez l'option `-a` pour stocker plusieurs entrées dans un tableau, ce qui peut être utile pour traiter des listes d'éléments.