# [리눅스] Bash watch 사용법

## Aperçu
La commande `watch` est un utilitaire de ligne de commande qui permet d'exécuter une commande à intervalles réguliers et d'afficher la sortie dans le terminal. Son objectif principal est de surveiller les changements dans la sortie d'une commande, ce qui est particulièrement utile pour le suivi des fichiers logs, l'état des systèmes ou toute autre information dynamique.

## Utilisation
La syntaxe de base de la commande `watch` est la suivante :

```bash
watch [options] <commande>
```

### Options courantes :
- `-n <seconds>` : Définit l'intervalle en secondes entre les exécutions de la commande. Par défaut, cet intervalle est de 2 secondes.
- `-d` : Met en surbrillance les différences entre les sorties successives, ce qui facilite la visualisation des changements.
- `-t` : Supprime l'affichage de l'en-tête, ne montrant que la sortie de la commande.
- `-x` : Permet d'exécuter la commande avec des arguments, en utilisant la syntaxe `watch -x <commande> <arg1> <arg2>`.

## Exemples
### Exemple 1 : Surveiller l'utilisation de la mémoire
Pour surveiller l'utilisation de la mémoire sur votre système, vous pouvez utiliser la commande `free` avec `watch` :

```bash
watch -n 5 free -h
```
Dans cet exemple, `free -h` sera exécuté toutes les 5 secondes, affichant l'utilisation de la mémoire dans un format lisible.

### Exemple 2 : Suivre les changements dans un répertoire
Pour suivre les changements dans un répertoire spécifique, vous pouvez utiliser `ls` :

```bash
watch -d ls -l /path/to/directory
```
Ici, `ls -l` affichera le contenu du répertoire toutes les 2 secondes, et les différences seront mises en surbrillance.

## Conseils
- Utilisez l'option `-d` pour mieux visualiser les changements, surtout lorsque vous surveillez des sorties qui changent fréquemment.
- Si vous avez besoin d'un intervalle personnalisé, n'oubliez pas d'utiliser l'option `-n` pour définir la fréquence d'exécution de la commande.
- Pour des sorties longues, envisagez d'utiliser `-t` pour éviter l'encombrement de l'affichage avec des en-têtes répétitifs.
- Soyez conscient de la charge que cela peut imposer à votre système si vous exécutez des commandes lourdes à des intervalles très courts.