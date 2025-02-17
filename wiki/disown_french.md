# [Linux] Bash disown : Gérer les tâches en arrière-plan

## Overview
La commande `disown` est utilisée dans Bash pour retirer un ou plusieurs travaux de la liste des travaux gérés par le shell. Cela permet de continuer l'exécution de ces travaux même après la fermeture du terminal, évitant ainsi qu'ils ne soient interrompus.

## Usage
La syntaxe de base de la commande `disown` est la suivante :

```bash
disown [options] [arguments]
```

## Common Options
- `-h` : Ne pas signaler le travail à la commande `kill` lors de la fermeture du terminal.
- `-a` : Appliquer `disown` à tous les travaux en cours.
- `-r` : Appliquer `disown` uniquement aux travaux en arrière-plan.

## Common Examples

### Exemple 1 : Retirer un travail spécifique
Pour retirer un travail spécifique de la liste des travaux, utilisez :

```bash
disown %1
```
Cela retire le travail numéro 1 de la liste.

### Exemple 2 : Retirer tous les travaux
Pour retirer tous les travaux en cours, utilisez :

```bash
disown -a
```
Cela déconnecte tous les travaux en cours du terminal.

### Exemple 3 : Retirer un travail en arrière-plan
Pour retirer un travail en arrière-plan, utilisez :

```bash
disown -r
```
Cela déconnecte tous les travaux en arrière-plan.

## Tips
- Utilisez `jobs` pour voir la liste des travaux en cours avant d'utiliser `disown`.
- Pensez à utiliser `nohup` en combinaison avec `disown` pour garantir que les travaux continuent à s'exécuter même après la déconnexion.
- Soyez prudent lorsque vous retirez des travaux, car vous ne pourrez plus les gérer avec des commandes comme `fg` ou `bg` après avoir utilisé `disown`.