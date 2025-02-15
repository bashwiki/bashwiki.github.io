# [리눅스] Bash dmesg 사용법

## Overview
La commande `dmesg` est utilisée pour afficher les messages du noyau Linux et les messages du système d'exploitation. Elle permet aux ingénieurs et développeurs de visualiser les événements liés au matériel, aux pilotes et aux autres messages de diagnostic générés par le noyau lors du démarrage ou pendant l'exécution du système. Cela peut être particulièrement utile pour le dépannage et l'analyse des performances.

## Usage
La syntaxe de base de la commande `dmesg` est la suivante :

```bash
dmesg [options]
```

### Options courantes :
- `-C` : Efface le tampon des messages du noyau.
- `-c` : Affiche les messages du noyau et les efface ensuite.
- `-n <niveau>` : Définit le niveau de priorité des messages à afficher.
- `-T` : Affiche les horodatages des messages dans un format lisible (convertit les timestamps en heures et dates).
- `--follow` : Affiche les nouveaux messages en temps réel (similaire à `tail -f`).

## Examples
### Exemple 1 : Afficher les messages du noyau
Pour afficher tous les messages du noyau, il suffit d'exécuter :

```bash
dmesg
```

### Exemple 2 : Afficher les messages avec horodatage
Pour afficher les messages du noyau avec des horodatages lisibles, utilisez l'option `-T` :

```bash
dmesg -T
```

## Tips
- Utilisez `dmesg | less` pour faire défiler les messages de manière plus confortable, surtout si vous avez beaucoup de messages à consulter.
- Pour surveiller les messages du noyau en temps réel, combinez `dmesg` avec l'option `--follow` :

```bash
dmesg --follow
```
- Pensez à utiliser `dmesg -C` avant de démarrer un test pour effacer les anciens messages et obtenir un aperçu clair des événements récents.