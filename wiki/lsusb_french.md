# [리눅스] Bash lsusb 사용법

## Aperçu
La commande `lsusb` est un outil de ligne de commande utilisé sous les systèmes d'exploitation basés sur Linux pour afficher des informations sur les périphériques USB connectés à un système. Son objectif principal est de fournir une vue d'ensemble des périphériques USB, y compris leurs identifiants, leurs classes et d'autres détails pertinents. Cela est particulièrement utile pour les développeurs et les ingénieurs qui travaillent avec des dispositifs USB ou qui ont besoin de diagnostiquer des problèmes liés à ces périphériques.

## Utilisation
La syntaxe de base de la commande `lsusb` est la suivante :

```bash
lsusb [options]
```

### Options courantes
- `-v` : Affiche des informations détaillées sur chaque périphérique USB. Cette option peut produire beaucoup de sorties, donc elle est souvent utilisée avec `less` pour une navigation plus facile.
- `-t` : Affiche la hiérarchie des périphériques USB sous forme d'arbre.
- `-s [bus]:[device]` : Affiche uniquement les informations sur le périphérique spécifié par son bus et son numéro de périphérique.
- `-d [vendor]:[product]` : Affiche uniquement les informations sur le périphérique correspondant à l'identifiant du vendeur et à l'identifiant du produit.

## Exemples
Voici quelques exemples pratiques de l'utilisation de la commande `lsusb`.

### Exemple 1 : Afficher la liste des périphériques USB
Pour afficher tous les périphériques USB connectés, exécutez simplement :

```bash
lsusb
```

Cela produira une sortie similaire à :

```
Bus 002 Device 003: ID 1234:5678 Example Corp. Example Device
Bus 002 Device 004: ID 8765:4321 Another Corp. Another Device
```

### Exemple 2 : Afficher des informations détaillées sur un périphérique
Pour obtenir des informations détaillées sur un périphérique spécifique, utilisez l'option `-v` :

```bash
lsusb -v -s 002:003
```

Cela affichera des informations complètes sur le périphérique connecté au bus 002 et au numéro de périphérique 003.

## Conseils
- Lorsque vous utilisez l'option `-v`, il peut être utile de rediriger la sortie vers un fichier ou d'utiliser `less` pour faciliter la lecture, par exemple :

```bash
lsusb -v | less
```

- Si vous travaillez avec plusieurs périphériques USB, notez les identifiants de vendeur et de produit, car cela peut vous aider à identifier rapidement un périphérique spécifique lors du dépannage.
- Utilisez l'option `-t` pour visualiser la structure hiérarchique des périphériques USB, ce qui peut être utile pour comprendre comment les périphériques sont connectés entre eux.

En utilisant `lsusb`, vous pouvez facilement gérer et diagnostiquer les périphériques USB sur votre système Linux.