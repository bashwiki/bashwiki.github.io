# [리눅스] Bash umask 사용법

## Aperçu

La commande `umask` est utilisée dans les systèmes Unix et Linux pour définir les permissions par défaut des fichiers et des répertoires créés par un utilisateur. Le terme "umask" signifie "user file creation mask", et il détermine les permissions qui seront masquées lors de la création de nouveaux fichiers ou répertoires. Par défaut, les fichiers sont généralement créés avec des permissions de lecture et d'écriture, mais la valeur de umask peut restreindre ces permissions.

## Utilisation

La syntaxe de base de la commande `umask` est la suivante :

```bash
umask [options] [valeur]
```

### Options communes

- **valeur** : Spécifie la valeur de umask à définir. Cette valeur est généralement exprimée en octal (par exemple, 022, 077).
- Si aucune valeur n'est fournie, `umask` affichera la valeur actuelle de umask.

## Exemples

### Exemple 1 : Afficher la valeur actuelle de umask

Pour afficher la valeur actuelle de umask, il suffit de taper :

```bash
umask
```

Cela retournera une valeur, par exemple `0022`, qui indique les permissions masquées.

### Exemple 2 : Définir une nouvelle valeur de umask

Pour définir une nouvelle valeur de umask, par exemple `007`, qui permet aux fichiers d'être créés sans permissions pour le groupe et les autres, vous pouvez utiliser :

```bash
umask 007
```

Après avoir exécuté cette commande, tous les nouveaux fichiers créés auront des permissions de `rw-------` (lecture et écriture pour le propriétaire seulement).

## Conseils

- **Comprendre les permissions** : Avant de modifier la valeur de umask, il est essentiel de comprendre comment les permissions fonctionnent dans Unix/Linux. Les valeurs umask sont soustraites des permissions par défaut (généralement 666 pour les fichiers et 777 pour les répertoires).
- **Utiliser des valeurs appropriées** : Évitez d'utiliser des valeurs de umask trop restrictives, car cela pourrait empêcher les autres utilisateurs ou groupes d'accéder aux fichiers que vous créez.
- **Configurer dans les fichiers de profil** : Pour rendre les changements de umask permanents, vous pouvez ajouter la commande `umask` dans vos fichiers de profil utilisateur, comme `~/.bashrc` ou `~/.profile`.

En suivant ces conseils, vous pourrez gérer efficacement les permissions de vos fichiers et répertoires créés dans un environnement Unix/Linux.