# [Linux] Bash popd : Gérer les répertoires dans la pile

## Overview
La commande `popd` est utilisée pour supprimer le répertoire supérieur de la pile de répertoires et se déplacer vers ce répertoire. Elle est souvent utilisée en conjonction avec la commande `pushd`, qui ajoute un répertoire à la pile.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
popd [options]
```

## Common Options
- `-n` : Ne pas changer de répertoire, juste supprimer le répertoire supérieur de la pile.
- `+N` : Accéder au répertoire à la position N dans la pile, en commençant par 0 pour le répertoire supérieur.

## Common Examples

### Exemple 1 : Retourner au répertoire précédent
```bash
pushd /chemin/vers/repertoire1
pushd /chemin/vers/repertoire2
popd
```
Dans cet exemple, après avoir exécuté `popd`, vous reviendrez à `/chemin/vers/repertoire1`.

### Exemple 2 : Utiliser l'option `-n`
```bash
pushd /chemin/vers/repertoire1
pushd /chemin/vers/repertoire2
popd -n
```
Ici, `popd -n` supprimera le répertoire supérieur de la pile sans changer le répertoire courant.

### Exemple 3 : Accéder à un répertoire spécifique dans la pile
```bash
pushd /chemin/vers/repertoire1
pushd /chemin/vers/repertoire2
pushd /chemin/vers/repertoire3
popd +1
```
Cet exemple vous ramènera à `/chemin/vers/repertoire2`, qui est le répertoire à la position 1 dans la pile.

## Tips
- Utilisez `pushd` et `popd` ensemble pour naviguer facilement entre plusieurs répertoires sans avoir à taper les chemins complets.
- Vérifiez l'état de la pile de répertoires avec la commande `dirs` pour voir quels répertoires sont actuellement stockés.
- Soyez prudent avec l'utilisation de l'option `+N`, car elle peut vous amener à un répertoire inattendu si vous ne connaissez pas bien l'ordre de la pile.