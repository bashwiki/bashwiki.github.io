# [리눅스] Bash times 사용법

## Overview
La commande `times` dans Bash est utilisée pour afficher le temps d'exécution des processus de l'utilisateur dans le shell courant. Elle fournit des informations sur le temps CPU utilisé par le shell et ses sous-processus, ce qui est utile pour analyser la performance des scripts et des commandes exécutées.

## Usage
La syntaxe de base de la commande `times` est très simple :

```bash
times
```

Cette commande ne prend pas d'options ou d'arguments. Lorsque vous l'exécutez, elle affiche le temps total CPU utilisé par le shell et tous ses processus fils.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `times` :

### Exemple 1 : Afficher le temps d'exécution après l'exécution d'une commande
```bash
# Exécutez une commande qui prend du temps
sleep 5

# Affichez le temps CPU utilisé
times
```
Dans cet exemple, la commande `sleep 5` fait une pause de 5 secondes, après quoi la commande `times` affiche le temps CPU utilisé par le shell pendant cette période.

### Exemple 2 : Utilisation dans un script
```bash
#!/bin/bash

# Un script simple qui effectue plusieurs opérations
echo "Début du script..."
sleep 2
echo "Fin du script."

# Afficher le temps CPU utilisé
times
```
Dans ce script, après l'exécution des commandes, la commande `times` affiche le temps CPU total utilisé par le script.

## Tips
- Utilisez `times` à la fin de vos scripts pour obtenir une vue d'ensemble du temps CPU utilisé, ce qui peut vous aider à optimiser vos scripts.
- Gardez à l'esprit que `times` ne montre que le temps CPU et non le temps réel écoulé. Pour des mesures plus complètes, envisagez d'utiliser des outils comme `time` pour obtenir des informations sur le temps d'exécution total.