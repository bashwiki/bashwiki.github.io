# [리눅스] Bash pushd 사용법

## Overview
La commande `pushd` est utilisée dans le shell Bash pour manipuler la pile de répertoires. Son objectif principal est de changer le répertoire courant tout en sauvegardant l'ancien répertoire sur une pile. Cela permet aux utilisateurs de naviguer facilement entre différents répertoires sans perdre leur position précédente.

## Usage
La syntaxe de base de la commande `pushd` est la suivante :

```bash
pushd [répertoire]
```

### Options courantes
- **répertoire** : Spécifie le répertoire vers lequel vous souhaitez naviguer. Si aucun répertoire n'est fourni, `pushd` échangera le répertoire courant avec le répertoire en haut de la pile.

## Examples
### Exemple 1 : Navigation vers un répertoire
Supposons que vous soyez dans le répertoire `/home/user` et que vous souhaitiez naviguer vers `/var/log`. Vous pouvez utiliser la commande suivante :

```bash
pushd /var/log
```

Après l'exécution de cette commande, vous serez dans `/var/log`, et `/home/user` sera sauvegardé dans la pile.

### Exemple 2 : Échange de répertoires
Si vous souhaitez revenir au répertoire précédent, vous pouvez utiliser la commande `popd` :

```bash
popd
```

Cela vous ramènera au répertoire `/home/user` que vous avez précédemment sauvegardé.

## Tips
- Utilisez `dirs` pour afficher la pile de répertoires actuelle. Cela vous permet de voir où vous êtes et quels répertoires sont disponibles pour naviguer.
- Combinez `pushd` avec des scripts pour automatiser la navigation dans des répertoires complexes, ce qui peut améliorer votre flux de travail.
- N'oubliez pas que `pushd` et `popd` fonctionnent ensemble : chaque fois que vous utilisez `pushd`, assurez-vous d'utiliser `popd` pour revenir en arrière et maintenir votre pile de répertoires propre.