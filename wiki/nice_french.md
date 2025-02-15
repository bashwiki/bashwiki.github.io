# [리눅스] Bash nice 사용법

## Overview
La commande `nice` est utilisée dans les systèmes Unix et Linux pour modifier la priorité d'exécution d'un processus. Son but principal est de permettre aux utilisateurs de spécifier la priorité d'un processus lorsqu'il est lancé, ce qui peut être utile pour gérer les ressources système et éviter que certains processus ne monopolise le CPU. En ajustant la "niceness" d'un processus, vous pouvez rendre un processus plus ou moins prioritaire par rapport aux autres.

## Usage
La syntaxe de base de la commande `nice` est la suivante :

```bash
nice [OPTION] [COMMAND [ARGUMENTS...]]
```

### Options courantes :
- `-n, --adjustment=N` : Définit la valeur de "niceness" du processus. La valeur par défaut est 10. Les valeurs peuvent aller de -20 (priorité maximale) à 19 (priorité minimale).
- `--help` : Affiche l'aide et les options disponibles pour la commande.
- `--version` : Affiche la version de la commande `nice`.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `nice`.

### Exemple 1 : Lancer un processus avec une priorité réduite
Pour lancer un script Python avec une priorité réduite, vous pouvez utiliser la commande suivante :

```bash
nice -n 10 python mon_script.py
```

Dans cet exemple, le script Python `mon_script.py` sera exécuté avec une valeur de "niceness" de 10, ce qui signifie qu'il aura une priorité inférieure par rapport aux autres processus.

### Exemple 2 : Lancer un processus avec une priorité élevée
Pour lancer un processus avec une priorité plus élevée, vous pouvez utiliser une valeur de "niceness" négative. Par exemple :

```bash
sudo nice -n -5 ./mon_programme
```

Ici, `mon_programme` sera exécuté avec une priorité plus élevée, ce qui peut être utile pour les tâches critiques.

## Tips
- Utilisez `nice` avec précaution, car un processus avec une priorité trop élevée peut affecter la réactivité du système.
- Pour vérifier la "niceness" d'un processus en cours d'exécution, vous pouvez utiliser la commande `ps` avec l'option `-o` pour afficher la colonne `NI` (niceness).
- Si vous devez modifier la priorité d'un processus déjà en cours d'exécution, utilisez la commande `renice` au lieu de `nice`.

En suivant ces conseils, vous pourrez gérer efficacement les priorités de vos processus et optimiser l'utilisation des ressources de votre système.