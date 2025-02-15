# [리눅스] Bash uniq 사용법

## Overview
La commande `uniq` est un utilitaire de traitement de texte dans Unix/Linux qui permet de filtrer les lignes répétées dans un fichier ou une entrée standard. Son principal objectif est de supprimer les doublons consécutifs dans un fichier, ce qui est particulièrement utile lors de l'analyse de données ou de la préparation de rapports.

## Usage
La syntaxe de base de la commande `uniq` est la suivante :

```bash
uniq [options] [input_file] [output_file]
```

### Options courantes :
- `-c` : Compte le nombre d'occurrences de chaque ligne.
- `-d` : Affiche uniquement les lignes qui sont dupliquées.
- `-u` : Affiche uniquement les lignes uniques, c'est-à-dire celles qui ne sont pas répétées.
- `-i` : Ignore la casse lors de la comparaison des lignes.
- `-w N` : Compare seulement les N premiers caractères de chaque ligne.

## Examples
### Exemple 1 : Suppression des doublons
Supposons que vous ayez un fichier nommé `data.txt` contenant les lignes suivantes :

```
apple
apple
banana
orange
banana
```

Pour supprimer les doublons consécutifs, vous pouvez utiliser la commande suivante :

```bash
uniq data.txt
```

Cela produira la sortie suivante :

```
apple
banana
orange
banana
```

### Exemple 2 : Compter les occurrences
Pour compter combien de fois chaque ligne apparaît dans le fichier, utilisez l'option `-c` :

```bash
uniq -c data.txt
```

La sortie sera :

```
      2 apple
      1 banana
      1 orange
      1 banana
```

## Tips
- Assurez-vous que votre fichier est trié si vous souhaitez supprimer tous les doublons, pas seulement les doublons consécutifs. Vous pouvez utiliser la commande `sort` avant `uniq` pour cela.
- Combinez `uniq` avec d'autres commandes comme `sort` pour un traitement de données plus efficace. Par exemple, `sort data.txt | uniq -c` pour trier et compter les occurrences en une seule commande.
- Utilisez l'option `-i` si vous souhaitez que la comparaison soit insensible à la casse, ce qui peut être utile dans des contextes où la casse des lettres ne doit pas affecter le résultat.