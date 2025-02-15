# [리눅스] Bash htop 사용법

## Overview
`htop` est un outil interactif de visualisation des processus qui permet aux utilisateurs de surveiller l'utilisation des ressources système en temps réel. Contrairement à la commande `top`, `htop` offre une interface utilisateur plus conviviale, avec des couleurs et des graphiques, facilitant ainsi la compréhension des performances du système. Il permet également de gérer les processus, comme les tuer ou les renicer, directement depuis l'interface.

## Usage
La syntaxe de base de la commande `htop` est simple :

```bash
htop
```

### Options courantes
- `-h`, `--help` : Affiche l'aide et les options disponibles.
- `-s`, `--sort` : Permet de trier les processus par une colonne spécifique (par exemple, `%CPU`, `%MEM`).
- `-p`, `--pid` : Affiche uniquement les processus spécifiés par leurs identifiants de processus (PID).
- `-C`, `--no-color` : Démarre `htop` sans couleurs.

## Examples
### Exemple 1 : Lancer htop
Pour lancer `htop`, il suffit de taper la commande suivante dans votre terminal :

```bash
htop
```

Cela ouvrira l'interface `htop`, où vous pourrez voir tous les processus en cours d'exécution, ainsi que leur utilisation de la CPU, de la mémoire, et d'autres ressources.

### Exemple 2 : Trier les processus par utilisation CPU
Pour trier les processus par leur utilisation CPU, vous pouvez utiliser l'interface de `htop` en appuyant sur `F6` pour sélectionner la colonne de tri. Vous pouvez également démarrer `htop` avec un tri par défaut en utilisant :

```bash
htop -s PERCENT_CPU
```

Cela affichera les processus triés par pourcentage d'utilisation de la CPU dès le lancement.

## Tips
- Utilisez les touches de fonction (F1 à F10) pour accéder rapidement aux différentes fonctionnalités de `htop`, comme l'aide, le tri, ou la gestion des processus.
- Pour quitter `htop`, appuyez simplement sur `q`.
- Vous pouvez personnaliser l'affichage en utilisant les options de configuration accessibles via `F2`, ce qui vous permet de choisir les colonnes à afficher et leur ordre.
- Si vous souhaitez surveiller un processus spécifique, notez son PID et utilisez l'option `-p` pour ne voir que ce processus.

En utilisant `htop`, vous pouvez facilement surveiller et gérer les performances de votre système, ce qui en fait un outil indispensable pour les ingénieurs et les développeurs.