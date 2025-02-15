# [리눅스] Bash renice 사용법

## Overview
La commande `renice` est utilisée dans les systèmes Unix et Linux pour modifier la priorité d'exécution des processus en cours. La priorité d'un processus détermine la quantité de temps CPU qui lui est allouée par le système d'exploitation. En ajustant la priorité, les utilisateurs peuvent influencer le comportement des processus, en leur permettant de consommer plus ou moins de ressources système selon les besoins.

## Usage
La syntaxe de base de la commande `renice` est la suivante :

```bash
renice [valeur] -p [PID]
```

### Options courantes :
- `valeur` : Un entier qui représente la nouvelle priorité. Les valeurs vont de -20 (priorité maximale) à 19 (priorité minimale).
- `-p` : Indique que vous souhaitez modifier la priorité d'un processus spécifique en utilisant son identifiant de processus (PID).

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `renice`.

### Exemple 1 : Changer la priorité d'un processus
Pour changer la priorité d'un processus avec un PID de 1234 à une priorité de 10, vous pouvez utiliser la commande suivante :

```bash
renice 10 -p 1234
```

### Exemple 2 : Changer la priorité de plusieurs processus
Si vous souhaitez modifier la priorité de plusieurs processus en une seule commande, vous pouvez spécifier plusieurs PIDs. Par exemple, pour changer la priorité des processus avec les PIDs 1234 et 5678 à -5 :

```bash
renice -5 -p 1234 -p 5678
```

## Tips
- Utilisez `renice` avec précaution, car une priorité trop élevée pour un processus peut entraîner une dégradation des performances des autres processus.
- Pour vérifier la priorité actuelle d'un processus, vous pouvez utiliser la commande `ps` avec l'option `-o` pour afficher la colonne `ni` (nice value) :
  
  ```bash
  ps -o pid,ni,cmd
  ```

- Il est recommandé d'utiliser `renice` avec des privilèges d'administrateur (sudo) pour modifier la priorité des processus qui ne vous appartiennent pas.
- Pensez à surveiller l'impact des modifications de priorité sur le système, surtout dans un environnement de production.