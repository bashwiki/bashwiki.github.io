# [리눅스] Bash popd 사용법

## Overview
La commande `popd` est utilisée dans l'environnement de shell Bash pour gérer la pile de répertoires. Son but principal est de supprimer le répertoire le plus récemment ajouté à la pile et de changer le répertoire de travail courant pour celui-ci. Cela permet aux utilisateurs de naviguer facilement entre plusieurs répertoires sans avoir à taper les chemins complets.

## Usage
La syntaxe de base de la commande `popd` est la suivante :

```bash
popd [options]
```

### Options courantes :
- `-n` : Ne change pas le répertoire de travail, mais supprime le répertoire du sommet de la pile.
- `+n` : Supprime le répertoire à la position `n` dans la pile (en commençant par 0 pour le sommet).
- `-n` : Supprime le répertoire à la position `n` en partant de la fin de la pile.

## Examples
### Exemple 1 : Utilisation de base
Supposons que vous ayez déjà ajouté des répertoires à la pile avec la commande `pushd`. Vous pouvez revenir au répertoire précédent avec :

```bash
pushd /chemin/vers/repertoire1
pushd /chemin/vers/repertoire2
popd
```

Après l'exécution de `popd`, vous serez de retour dans `/chemin/vers/repertoire1`.

### Exemple 2 : Utilisation avec l'option `-n`
Si vous souhaitez simplement retirer un répertoire de la pile sans changer le répertoire courant, vous pouvez utiliser l'option `-n` :

```bash
pushd /chemin/vers/repertoire1
pushd /chemin/vers/repertoire2
popd -n
```

Dans cet exemple, `popd -n` retirera `/chemin/vers/repertoire2` de la pile, mais vous resterez dans `/chemin/vers/repertoire2`.

## Tips
- Utilisez `dirs` pour afficher le contenu actuel de la pile de répertoires avant ou après l'utilisation de `popd`. Cela vous aidera à visualiser votre position dans la pile.
- Combinez `pushd` et `popd` pour créer des scripts de navigation efficaces lorsque vous travaillez sur plusieurs projets ou répertoires.
- Soyez conscient de l'ordre dans lequel vous utilisez `pushd` et `popd`, car un mauvais usage peut vous ramener à un répertoire inattendu.