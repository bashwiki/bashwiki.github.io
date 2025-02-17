# [Linux] Bash continue : Reprendre l'exécution d'une boucle

## Overview
La commande `continue` en Bash est utilisée pour sauter le reste du code dans une boucle en cours d'exécution et passer directement à l'itération suivante de cette boucle. Cela permet de contrôler le flux d'exécution des boucles, comme `for`, `while`, et `until`.

## Usage
Voici la syntaxe de base de la commande `continue` :

```bash
continue [n]
```

Ici, `n` est un nombre optionnel qui indique combien d'itérations de la boucle doivent être sautées. Si `n` n'est pas spécifié, la commande passe à l'itération suivante.

## Common Options
- `n` : Un nombre qui spécifie le nombre d'itérations à sauter. Par défaut, c'est 1.

## Common Examples

### Exemple 1 : Sauter à l'itération suivante
```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    continue
  fi
  echo "Numéro : $i"
done
```
Dans cet exemple, le nombre 3 ne sera pas affiché.

### Exemple 2 : Sauter plusieurs itérations
```bash
for i in {1..10}; do
  if [ $i -lt 5 ]; then
    continue 2
  fi
  echo "Numéro : $i"
done
```
Ici, les nombres 1 à 4 seront ignorés, et l'affichage commencera à 5.

### Exemple 3 : Utilisation dans une boucle while
```bash
count=0
while [ $count -lt 5 ]; do
  count=$((count + 1))
  if [ $count -eq 3 ]; then
    continue
  fi
  echo "Compteur : $count"
done
```
Dans cet exemple, le compteur 3 sera également ignoré lors de l'affichage.

## Tips
- Utilisez `continue` pour rendre votre code plus lisible en évitant des structures conditionnelles complexes.
- Soyez prudent lors de l'utilisation de l'option `n`, car sauter trop d'itérations peut rendre le comportement de la boucle difficile à comprendre.
- Testez toujours vos boucles avec des valeurs simples pour vous assurer que le comportement est celui attendu avant d'ajouter des logiques plus complexes.