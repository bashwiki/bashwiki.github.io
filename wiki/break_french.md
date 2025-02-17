# [Linux] Bash break : Terminer une boucle

## Overview
La commande `break` est utilisée dans les scripts Bash pour sortir d'une boucle. Elle permet de quitter une boucle `for`, `while` ou `until` avant qu'elle ne se termine naturellement, ce qui peut être utile pour contrôler le flux d'exécution d'un script.

## Usage
La syntaxe de base de la commande `break` est la suivante :

```bash
break [n]
```

Ici, `n` est un nombre optionnel qui spécifie le niveau de la boucle à quitter. Si `n` n'est pas fourni, `break` sort de la boucle la plus interne.

## Common Options
- `n` : (optionnel) Spécifie le nombre de niveaux de boucle à quitter. Par défaut, il quitte la boucle la plus interne.

## Common Examples

### Exemple 1 : Sortir d'une boucle `for`
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        break
    fi
    echo "Nombre : $i"
done
```
Dans cet exemple, la boucle s'arrête lorsque `i` atteint 3, donc les nombres 1 et 2 seront affichés.

### Exemple 2 : Sortir d'une boucle `while`
```bash
count=1
while [ $count -le 5 ]; do
    if [ $count -eq 4 ]; then
        break
    fi
    echo "Compteur : $count"
    ((count++))
done
```
Ici, la boucle s'arrête lorsque `count` est égal à 4, affichant ainsi les valeurs 1, 2 et 3.

### Exemple 3 : Utilisation de `break` avec un niveau
```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            break 2
        fi
        echo "i: $i, j: $j"
    done
done
```
Dans cet exemple, `break 2` sort des deux boucles lorsque `j` est égal à 2, donc aucune sortie n'est affichée.

## Tips
- Utilisez `break` judicieusement pour éviter de rendre votre code difficile à lire. Trop de niveaux de sortie peuvent créer de la confusion.
- Pensez à utiliser `break` en combinaison avec des conditions pour un contrôle précis sur le flux de votre script.
- Testez toujours vos scripts dans un environnement sûr pour vous assurer que l'utilisation de `break` fonctionne comme prévu.